# Section A: Data Foundation & Preparation

This index records the files supplied in `Step A/` and reorganized on 2 October 2026 using the repository's existing `Data/`, `Reports/`, and `docs/` structure. The brief requires a clear structure but does not mandate these directory names.

All 22 files retain their original filenames and contents. SHA-256 comparisons before and after relocation matched for every file. This was a file organization check, not an independent validation of the analyses. Task completion and ownership remain as recorded in the [Week 1 sprint notes](../sprints/WEEK-01.md).

## Reports and reference guides

These five workbooks were previously in `Step A/Part A explanation/`.

| File | Current purpose and location |
|---|---|
| [A1_Data_Profiling_Report.xlsx](../Reports/profiling/A1_Data_Profiling_Report.xlsx) | Profiling report in `Reports/profiling/` |
| [A2_Data_Cleaning_Log.xlsx](../Reports/data_quality/A2_Data_Cleaning_Log.xlsx) | Cleaning log in `Reports/data_quality/` |
| [A3_Integrated_Tables_Guide.xlsx](A3_Integrated_Tables_Guide.xlsx) | Integrated tables reference in `docs/` |
| [A4_Feature_Dictionary.xlsx](A4_Feature_Dictionary.xlsx) | Feature definitions in `docs/` |
| [A5_Section_A_Completion_Summary.xlsx](../Reports/validation/A5_Section_A_Completion_Summary.xlsx) | Completion summary in `Reports/validation/` |

## Cleaned tables

Moved from `Step A/cleaned/cleaned/` to `Data/processed/cleaned/`:

- [branches.csv](../Data/processed/cleaned/branches.csv)
- [customers.csv](../Data/processed/cleaned/customers.csv)
- [inventory_master.csv](../Data/processed/cleaned/inventory_master.csv)
- [invoices.csv](../Data/processed/cleaned/invoices.csv)
- [payments.csv](../Data/processed/cleaned/payments.csv)
- [products.csv](../Data/processed/cleaned/products.csv)
- [purchase_orders_header.csv](../Data/processed/cleaned/purchase_orders_header.csv)
- [purchase_orders_lines.csv](../Data/processed/cleaned/purchase_orders_lines.csv)
- [sales_orders_header.csv](../Data/processed/cleaned/sales_orders_header.csv)
- [sales_orders_lines.csv](../Data/processed/cleaned/sales_orders_lines.csv)
- [stock_ledger.csv](../Data/processed/cleaned/stock_ledger.csv)
- [suppliers.csv](../Data/processed/cleaned/suppliers.csv)

## Integration outputs

Moved from `Step A/Integration/` to `Data/processed/integrated/`:

- [customer_features.csv](../Data/processed/integrated/customer_features.csv)
- [inventory_position.csv](../Data/processed/integrated/inventory_position.csv)
- [purchase_orders_header.csv](../Data/processed/integrated/purchase_orders_header.csv)
- [sales_orders_header.csv](../Data/processed/integrated/sales_orders_header.csv)
- [stock_movements_enriched.csv](../Data/processed/integrated/stock_movements_enriched.csv)

The cleaned and integrated folders are kept separate to preserve their supplied grouping and avoid collisions between identically named order-header files. Existing workbook text is unchanged; any references to the former folders can be resolved using the mappings above. No external workbook relationships, external-link parts, connections, or query-table parts were found in the five workbooks.

## Data handling

Keep original, unmodified downloads in `Data/raw/` when available. The supplied Section A files are prepared outputs and have not been relabeled as raw data. Before building further analyses, review the actual table keys, relationships, field definitions, and preparation evidence.
