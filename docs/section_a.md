# Section A: Data Foundation & Preparation

Task index organized using A1-A6 labels on 5 October 2026, matching the Section B index. The current foundation files include 12 cleaned CSVs, 7 integration-folder CSVs, 5 workbooks, and 2 Python scripts. The A6 reference below points to existing dictionary content rather than duplicating it.

## Task reports and evidence

| Code | Task | Report or reference | Supporting files |
|---|---|---|---|
| A1 | Data Profiling & Structure Analysis | [A1_Data_Profiling_Report.xlsx](../Reports/profiling/A1_Data_Profiling_Report.xlsx) | Table inventory, relationships, quality notes, and field dictionary in the workbook |
| A2 | Data Cleaning & Quality Improvement | [A2_Data_Cleaning_Log.xlsx](../Reports/data_quality/A2_Data_Cleaning_Log.xlsx) | [12 cleaned tables](../Data/processed/cleaned/section_a/A2/) |
| A3 | Data Integration & Dataset Merging | [A3_Integrated_Tables_Guide.xlsx](A3_Integrated_Tables_Guide.xlsx) | [Integration outputs](../Data/processed/integrated/section_a/); [reconstruction script](../notebooks/build.analysis_tables.py) |
| A4 | Feature Engineering for Analytics | [A4_Feature_Dictionary.xlsx](A4_Feature_Dictionary.xlsx) | Sales, purchase, inventory, movement, and customer features in the integration outputs |
| A5 | Data Validation & Consistency Checks | [A5_Section_A_Completion_Summary.xlsx](../Reports/validation/A5_Section_A_Completion_Summary.xlsx) | Workbook sheet `A5_Validation_Log`; [adjustment repair script](../notebooks/repair_adjusments.py); [change log](../Data/interim/section_a/A5/adjustment_review/A5_adjustment_changes.csv) |
| A6 | Data Dictionary & Documentation | [A6_Data_Dictionary_Index.md](A6_Data_Dictionary_Index.md) | Locates the existing source-field dictionary, relationships, integration definitions, and feature formulas |

## CSV outputs

On 6 October 2026, all 22 Section A CSVs received task prefixes: A2 for cleaned tables, A3 for integrated tables, A4 for customer features, and A5 for adjustment-review evidence. A shared file can support multiple tasks; its prefix identifies its primary role. Both Python scripts and current documentation use the new paths. CSV contents are unchanged. Files are now grouped by section and task within each processing stage; see the [Data directory guide](../Data/README.md). Section B filenames already carry B-task prefixes.

Original workbooks retain their original filenames in descriptions. Use the [old-to-new filename mapping](section_a_filenames.md) when following those references or updating a teammate's local code or data connection.

Dimensions below were checked against the current files. Row counts exclude headers.

### A2: Cleaned source tables

| Code | File | Rows | Columns |
|---|---|---:|---:|
| A2 | [A2_branches.csv](../Data/processed/cleaned/section_a/A2/A2_branches.csv) | 6 | 14 |
| A2 | [A2_customers.csv](../Data/processed/cleaned/section_a/A2/A2_customers.csv) | 500 | 15 |
| A2 | [A2_inventory_master.csv](../Data/processed/cleaned/section_a/A2/A2_inventory_master.csv) | 180 | 8 |
| A2 | [A2_invoices.csv](../Data/processed/cleaned/section_a/A2/A2_invoices.csv) | 18,033 | 10 |
| A2 | [A2_payments.csv](../Data/processed/cleaned/section_a/A2/A2_payments.csv) | 19,257 | 5 |
| A2 | [A2_products.csv](../Data/processed/cleaned/section_a/A2/A2_products.csv) | 30 | 23 |
| A2 | [A2_purchase_orders_header.csv](../Data/processed/cleaned/section_a/A2/A2_purchase_orders_header.csv) | 24,000 | 10 |
| A2 | [A2_purchase_orders_lines.csv](../Data/processed/cleaned/section_a/A2/A2_purchase_orders_lines.csv) | 155,495 | 9 |
| A2 | [A2_sales_orders_header.csv](../Data/processed/cleaned/section_a/A2/A2_sales_orders_header.csv) | 20,000 | 11 |
| A2 | [A2_sales_orders_lines.csv](../Data/processed/cleaned/section_a/A2/A2_sales_orders_lines.csv) | 130,402 | 9 |
| A2 | [A2_stock_ledger.csv](../Data/processed/cleaned/section_a/A2/A2_stock_ledger.csv) | 237,230 | 9 |
| A2 | [A2_suppliers.csv](../Data/processed/cleaned/section_a/A2/A2_suppliers.csv) | 8 | 12 |

### A3-A4: Integration and feature outputs

| Code | File | Rows | Columns | Role |
|---|---|---:|---:|---|
| A3 / A4 | [A3_sales_analysis.csv](../Data/processed/integrated/section_a/A3/A3_sales_analysis.csv) | 130,402 | 48 | Reconstructed sales-line analysis with calculated features |
| A3 / A4 | [A3_purchase_analysis.csv](../Data/processed/integrated/section_a/A3/A3_purchase_analysis.csv) | 155,495 | 49 | Reconstructed purchase-line analysis with calculated features |
| A3 / A4 | [A3_inventory_position.csv](../Data/processed/integrated/section_a/A3/A3_inventory_position.csv) | 180 | 39 | Product-branch inventory positions and features |
| A3 / A4 / A5 | [A3_stock_movements_enriched.csv](../Data/processed/integrated/section_a/A3/A3_stock_movements_enriched.csv) | 237,230 | 32 | Enriched movements, including the adopted adjustment-sign repair |
| A4 | [A4_customer_features.csv](../Data/processed/integrated/section_a/A4/A4_customer_features.csv) | 500 | 32 | Customer-level features |
| A3 support | [A3_purchase_orders_header.csv](../Data/processed/integrated/section_a/A3/A3_purchase_orders_header.csv) | 24,000 | 10 | Header table supplied in the original integration folder |
| A3 support | [A3_sales_orders_header.csv](../Data/processed/integrated/section_a/A3/A3_sales_orders_header.csv) | 20,000 | 11 | Header table supplied in the original integration folder |

The order-header tables are supporting inputs, not substitutes for the line-level sales and purchase analysis outputs.

## A5: Repair evidence

| File | Purpose |
|---|---|
| [repair_adjusments.py](../notebooks/repair_adjusments.py) | Validates the source sequence and creates a candidate adjustment-sign repair; filename retained as supplied |
| [A5_adjustment_changes.csv](../Data/interim/section_a/A5/adjustment_review/A5_adjustment_changes.csv) | Record of changes to signed quantities |
| [A5_stock_movements_enriched_candidate.csv](../Data/interim/section_a/A5/adjustment_review/A5_stock_movements_enriched_candidate.csv) | Review candidate; downstream analyses should use the declared integrated output above |

The review folder also retains [A5_stock_movements_enriched.csv](../Data/interim/section_a/A5/adjustment_review/A5_stock_movements_enriched.csv), a separate review copy. Use the A3 integrated output for downstream analyses.

The reconstruction script [build.analysis_tables.py](../notebooks/build.analysis_tables.py) covers selected A3-A4 sales and purchase outputs; it is not a complete reproduction of every original Section A operation. Both scripts refuse to overwrite their existing output targets. The filename update preserves calculations and overwrite guards.

## History and review status

The original `Step A/` package contained 22 files: 12 cleaned CSVs, 5 integration-folder CSVs, and 5 workbooks. On 2 October 2026, those files were moved without changing their contents; before-and-after hashes matched. The two analysis CSVs were subsequently reconstructed and the movement output was subsequently repaired, so the original move's preservation check is not a claim that all files remain unchanged today.

Original folder mapping:

| Original location | Current location |
|---|---|
| `Step A/cleaned/cleaned/` | `Data/processed/cleaned/section_a/A2/` |
| `Step A/Integration/` | `Data/processed/integrated/section_a/A3/` and `A4/` |
| `Step A/Part A explanation/A1_*.xlsx` | `Reports/profiling/` |
| `Step A/Part A explanation/A2_*.xlsx` | `Reports/data_quality/` |
| `Step A/Part A explanation/A3_*.xlsx` and `A4_*.xlsx` | `docs/` |
| `Step A/Part A explanation/A5_*.xlsx` | `Reports/validation/` |

The original dictionaries describe 52 sales columns and 51 purchase columns; the reconstructed outputs currently have 48 and 49. Incompletely specified classification bands were omitted, and the schemas are not exact reproductions of the original reports. Refer to actual CSV headers when consuming these files.

This update organizes evidence and adds task labels; it does not certify analytical completeness. Existing team owners and statuses are recorded in the [Week 1 sprint notes](../sprints/WEEK-01.md), together with unresolved data-quality issues. Original source downloads belong in `Data/raw/` when available; these prepared tables should not be relabeled as raw data.

Related: [Section B file index](section_b.md).
