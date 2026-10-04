from pathlib import Path

import pandas as pd


# Resolve paths relative to this script, not the terminal location.
ROOT = Path(__file__).resolve().parents[1]
INPUT = ROOT / "Data" / "processed" / "cleaned"
OUTPUT = ROOT / "Data" / "processed" / "integrated"


def load_table(
    name: str,
    date_columns: tuple[str, ...] | list[str] = (),
) -> pd.DataFrame:
    table = pd.read_csv(INPUT / f"{name}.csv")


    for column in date_columns:
        table[column] = pd.to_datetime(
            table[column],
            format="%Y-%m-%d",
            errors="raise",
        )
    return table


def require(condition, message):
    """Stop processing when a validation fails."""
    if not condition:
        raise ValueError(message)


def checked_join(left, right, key):
    """Keep every left-hand row and require one matching lookup."""
    require(
        left[key].notna().all(),
        f"Missing {key} in the transaction table.",
    )
    require(
        right[key].notna().all(),
        f"Missing {key} in the lookup table.",
    )
    require(
        right[key].is_unique,
        f"Duplicate {key} values in the lookup table.",
    )

    overlaps = (set(left.columns) & set(right.columns)) - {key}
    require(
        not overlaps,
        f"Rename overlapping columns before joining: {overlaps}",
    )

    result = left.merge(
        right,
        on=key,
        how="left",
        validate="many_to_one",
        indicator=True,
    )

    unmatched = result["_merge"].ne("both")
    if unmatched.any():
        examples = result.loc[unmatched, key].unique()[:5]
        raise ValueError(f"Unmatched {key} values: {examples}")

    require(len(result) == len(left), f"Row count changed on {key}.")

    return result.drop(columns="_merge")


def add_calendar_fields(table):
    """Add month and quarter fields for grouping."""
    table["order_year"] = table["order_date"].dt.year
    table["order_month"] = table["order_date"].dt.month
    table["order_year_month"] = (
        table["order_date"].dt.to_period("M").astype(str)
    )
    table["order_quarter"] = table["order_date"].dt.quarter
    table["order_year_quarter"] = (
        table["order_year"].astype(str)
        + "-Q"
        + table["order_quarter"].astype(str)
    )


def check_order_lines(table, order_key, expected_rows):
    require(
        len(table) == expected_rows,
        f"Unexpected row count for {order_key}: {len(table):,}",
    )
    require(
        table[[order_key, "line_number"]].notna().all().all(),
        f"Missing order-line keys in {order_key}.",
    )
    require(
        not table.duplicated([order_key, "line_number"]).any(),
        f"Duplicate order lines in {order_key}.",
    )

    for column in ["quantity", "line_total"]:
        require(
            table[column].notna().all()
            and table[column].ge(0).all(),
            f"Missing or negative {column} in {order_key}.",
        )


def main():
    # Avoid accidentally replacing existing team outputs.
    targets = [
        OUTPUT / "sales_analysis.csv",
        OUTPUT / "purchase_analysis.csv",
    ]
    for target in targets:
        if target.exists():
            raise FileExistsError(f"Output already exists: {target}")

    # 1. Load the cleaned source tables.
    sales_lines = load_table("sales_orders_lines")
    sales_headers = load_table(
        "sales_orders_header",
        ["order_date", "delivery_date"],
    )

    purchase_lines = load_table("purchase_orders_lines")
    purchase_headers = load_table(
        "purchase_orders_header",
        ["order_date", "expected_delivery_date", "received_date"],
    )

    products = load_table("products")
    customers = load_table("customers")
    suppliers = load_table("suppliers")
    branches = load_table("branches")

    check_order_lines(sales_lines, "so_id", 130402)
    check_order_lines(purchase_lines, "po_id", 155495)

    # 2. Select lookup fields and give ambiguous columns clear names.
    product_fields = [
        "product_id",
        "product_name",
        "category",
        "machine_type",
        "brand",
        "criticality_level",
        "usage_frequency",
        "unit_cost",
        "unit_price",
        "margin_percentage",
    ]

    sales_products = products.loc[:, product_fields].rename(
        columns={
            "unit_cost": "product_unit_cost",
            "unit_price": "product_list_price",
        }
    )

    purchase_products = products.loc[:, product_fields].rename(
        columns={
            "unit_cost": "product_standard_cost",
            "unit_price": "product_list_price",
        }
    )

    customer_lookup = customers.loc[
            :,
            [
                "customer_id",
                "customer_type",
                "industry_segment",
                "city",
                "region",
                "customer_rating",
                "credit_limit",
                "payment_terms",
            ]
        ].rename(
            columns={
                "city": "customer_city",
                "region": "customer_region",
                "payment_terms": "customer_payment_terms",
            }
        )
    
    branch_lookup = branches.loc[
            :,
            [
                "branch_id",
                "branch_name",
                "city",
                "region",
                "warehouse_type",
                "warehouse_capacity_sqft",
            ]
        ].rename(
            columns={
                "city": "branch_city",
                "region": "branch_region",
            }
        )
    
    supplier_lookup = suppliers.loc[
            :,
            [
                "supplier_id",
                "supplier_name",
                "supplier_type",
                "city",
                "region",
                "lead_time_days",
                "reliability_score",
                "import_duty_rate",
            ]
        ].rename(
            columns={
                "city": "supplier_city",
                "region": "supplier_region",
                "lead_time_days": "supplier_lead_time_days",
            }
        )

    # 3. Build the sales table.
    # Exclude header totals: repeating them on each line can lead
    # to double-counting when someone sums the resulting table.
    sales_header_lookup = sales_headers[
        [
            "so_id",
            "customer_id",
            "branch_id",
            "order_date",
            "delivery_date",
            "order_status",
            "sales_channel",
        ]
    ]

    sales = checked_join(sales_lines, sales_header_lookup, "so_id")
    sales = checked_join(sales, sales_products, "product_id")
    sales = checked_join(sales, customer_lookup, "customer_id")
    sales = checked_join(sales, branch_lookup, "branch_id")

    sales["line_cost"] = sales["quantity"] * sales["product_unit_cost"]
    sales["line_gross_profit"] = sales["line_total"] - sales["line_cost"]

    # A zero-value sale has an undefined percentage margin.
    denominator = sales["line_total"].where(sales["line_total"].ne(0))
    sales["line_gross_margin_pct"] = (
        sales["line_gross_profit"] / denominator * 100
    )

    sales["delivery_days"] = (
        sales["delivery_date"] - sales["order_date"]
    ).dt.days

    sales["is_cancelled"] = sales["order_status"].eq("Cancelled")
    sales["is_delivered"] = sales["order_status"].eq("Delivered")

    # Fixed threshold documented in A4_Feature_Dictionary.xlsx.
    sales["is_high_value_line"] = sales["line_total"].ge(220500)

    add_calendar_fields(sales)

    # 4. Build the purchase table.
    purchase_header_lookup = purchase_headers[
        [
            "po_id",
            "supplier_id",
            "branch_id",
            "order_date",
            "expected_delivery_date",
            "received_date",
            "po_status",
        ]
    ]

    purchases = checked_join(
        purchase_lines, purchase_header_lookup, "po_id"
    )
    purchases = checked_join(
        purchases, purchase_products, "product_id"
    )
    purchases = checked_join(
        purchases, supplier_lookup, "supplier_id"
    )
    purchases = checked_join(purchases, branch_lookup, "branch_id")

    purchases["actual_lead_time_days"] = (
        purchases["received_date"] - purchases["order_date"]
    ).dt.days

    purchases["delay_vs_expected_days"] = (
        purchases["received_date"] - purchases["expected_delivery_date"]
    ).dt.days

    purchases["lead_time_vs_supplier_stated"] = (
        purchases["actual_lead_time_days"]
        - purchases["supplier_lead_time_days"]
    )

    delay = purchases["delay_vs_expected_days"]
    purchases["abs_delay_days"] = delay.abs()

    # Unknown delivery performance stays missing, not False.
    delivery_flags = {
        "on_time_delivery": delay.le(0),
        "is_late": delay.gt(0),
        "is_early": delay.lt(0),
        "is_exact_on_time": delay.eq(0),
    }

    for name, values in delivery_flags.items():
        purchases[name] = values.astype("boolean").where(
            delay.notna(), pd.NA
        )

    add_calendar_fields(purchases)

    # 5. Validate the finished tables before writing either file.
    check_order_lines(sales, "so_id", 130402)
    check_order_lines(purchases, "po_id", 155495)

    require(
        sales["order_date"].notna().all()
        and purchases["order_date"].notna().all(),
        "Missing order dates.",
    )
    require(
        sales["delivery_days"].dropna().ge(0).all(),
        "A sales delivery date precedes its order date.",
    )
    require(
        purchases["actual_lead_time_days"].dropna().ge(0).all(),
        "A purchase receipt date precedes its order date.",
    )

    # 6. Save the results.
    OUTPUT.mkdir(parents=True, exist_ok=True)

    for table, target in zip([sales, purchases], targets):
        table.to_csv(
            target,
            index=False,
            date_format="%Y-%m-%d",
            mode="x",
        )
        print(
            f"Saved {target.name}: "
            f"{len(table):,} rows, {len(table.columns)} columns"
        )


if __name__ == "__main__":
    main()
