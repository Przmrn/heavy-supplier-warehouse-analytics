import csv
from datetime import date
from decimal import Decimal
from pathlib import Path

def require(condition, message):
    if not condition:
        raise ValueError(message)

def number(value):
    result = Decimal(value)
    require(result.is_finite(), f"Invalid number: {value}")
    return result

def read_csv(path):
    with path.open(encoding="utf-8-sig", newline="") as file:
        reader = csv.DictReader(file)
        fields = reader.fieldnames

        require(bool(fields), f"No columns in {path}")
        require(
            len(fields) == len(set(fields)),
            f"Duplicate columns: {path}"
        )

        rows = list(reader)

        require(
            all(
                None not in row and None not in row.values()
                for row  in rows
            ),
            f"Malformed rows: {path}",
        )

        return fields, rows

def build_candidate(root):
    cleaned = root / "Data" / "processed"/ "cleaned"
    source = root / "Data" / "processed" / "integrated"

    _, inventory = read_csv(cleaned / "inventory_master.csv")
    _, ledger = read_csv(cleaned / "stock_ledger.csv")
    fields, enriched = read_csv(
        source / "stock_movements_enriched.csv"
    )

    previous = {}
    last_date = {}
    originals = {}
    expected = {}
    changes = []

    for row in inventory:
        key = (row["product_id"], row["branch_id"])

        require(all(key), "Blank inventory key.")
        require(
            key not in previous,
            f"Duplicate inventory key: {key}",
        )

        previous[key] = number(row["opening_stock"])

    for row in ledger:
        movement = row["movement_id"]
        key = (row["product_id"], row["branch_id"])

        require(bool(movement), "Blank movement id.")
        require(
            movement not in originals,
            f"Duplicate ledger movement: {movement}",
        )
        require(
            key in previous,
            f"Missing opening stock: {key}",
        )

        day = date.fromisoformat(row["movement_date"])

        require(
            key not in last_date or day >= last_date[key],
            f"Movement dates go backwards at {movement}.",
        )

        quantity = number(row["quantity"])
        balance = number(row["running_balance"])
        before = previous[key]
        change = balance - before
        kind = row["movement_type"]

        require(quantity >= 0, f"Negative quantity: {movement}")

        if kind == "IN":
            require(
                change == quantity,
                f"IN balance mismatch: {movement}",
            )

        elif kind == "OUT":
            require(
                change == -quantity,
                f"OUT balance mismatch: {movement}",
            )

        elif kind == "ADJUSTMENT":
            require(
                abs(change) == quantity,
                f"Adjustment magnitude mismatch: {movement}",
            )

        else:
            raise ValueError(f"Unknown movement type: {kind}")

        originals[movement] = row
        expected[movement] = (before, change)
        previous[key] = balance
        last_date[key] = day

    require(
        len(enriched) == len(ledger),
        "Ledger row counts differ.",
    )

    seen = set()

    # Match each enriched movement to its source record.
    for row in enriched:
        movement = row["movement_id"]

        require(
            movement not in seen,
            f"Duplicate enriched ID: {movement}",
        )
        require(
            movement in originals,
            f"Unknown enriched ID: {movement}",
        )

        seen.add(movement)
        original = originals[movement]

        # Confirm source values before changing the derived feature.
        for column, value in original.items():
            require(
                column in row,
                f"Missing source column: {column}",
            )

            if column in ("quantity", "running_balance"):
                matches = number(row[column]) == number(value)
            else:
                matches = row[column] == value

            require(
                matches,
                f"Source mismatch: {movement}, {column}",
            )

        before, signed = expected[movement]
        old_signed = number(row["signed_quantity"])

        if row["movement_type"] != "ADJUSTMENT":
            require(
                old_signed == signed,
                f"Non-adjustment sign mismatch: {movement}",
            )

        elif old_signed != signed:
            changes.append({
                "movement_id": movement,
                "product_id": row["product_id"],
                "branch_id": row["branch_id"],
                "movement_date": row["movement_date"],
                "quantity": row["quantity"],
                "previous_balance": str(before),
                "running_balance": row["running_balance"],
                "old_signed_quantity": row["signed_quantity"],
                "new_signed_quantity": str(signed),
            })

            row["signed_quantity"] = str(signed)

        require(
            number(row["signed_quantity"]) == signed,
            f"Candidate sign mismatch: {movement}",
        )

    require(
        seen == set(originals),
        "Movement coverage differs.",
    )

    return fields, enriched, changes


def write_csv(path, fields, rows):
    # "x" creates a new file and refuses to overwrite an existing one.
    with path.open("x", encoding="utf-8", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=fields)
        writer.writeheader()
        writer.writerows(rows)


def main():
    root = Path(__file__).resolve().parents[1]
    output = root / "Data" / "interim" / "adjustment_review"

    require(
        not output.exists(),
        f"Review folder already exists: {output}",
    )

    fields, candidate, changes = build_candidate(root)

    print(f"Validated {len(candidate):,} movements.")
    print(f"Adjustments to correct: {len(changes):,}")

    if not changes:
        print("No corrections needed. No files written.")
        return

    # Write only after all input and candidate checks pass.
    output.mkdir(parents=True, exist_ok=False)

    write_csv(
        output / "stock_movements_enriched_candidate.csv",
        fields,
        candidate,
    )

    write_csv(
        output / "adjustment_changes.csv",
        list(changes[0]),
        changes,
    )

    print(f"Candidate and change log saved in: {output}")
    print("Original files unchanged. Review before replacing anything.")
    print("Other data-quality issues remain outside this repair.")


if __name__ == "__main__":
    main()
