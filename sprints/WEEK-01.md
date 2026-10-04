# Week 1 Sprint Notes

## Scrum Master
Ammar Naufal

## Sprint Goal
Prepare the dataset for analysis by checking data quality, cleaning and integrating the relevant tables, and validating the results.

## Activities
| Task | Owner | Status |
|------|-------|--------|
| Set up the GitHub repository and invite teammates | Ammar | Done |
| Set up the directory structure in the Repo | Golla | Done |

## Step A Tasks
| Task | Owner | Status |
|------|-------|--------|
| Data Profiling & Structure Analysis | Nadir | Done |
| Data cleaning & Quality Improvement | Nadir | Done |
| Data Integration & Dataset Merging | Golla | Done |
| Feature Engineering for analytics| Festus | Done |
| Data Validation & Consistency Checks | Festus | Done |
| Data Dictionary & Documentation | Ammar | Done |

## Step B Tasks
| Task | Owner | Status |
|------|-------|--------|
| Product Performance Analysis | Nadir | In Progress |
| Fast-Moving Product Identification | Golla | In Progress |
| Slow-Moving & Dead Stock Identification | Ammar | In Progress |
| Inventory Turnover Analysis | Festus | In Progress |
| Stock Health Assessment | Golla | In Progress |
| Inventory Aging Analysis | Festus | In Progress |
| ABC / Pareto Product Classification | Ammar | In Progress |
| Overstock & Understock Detection | Nadir | In Progress |
| Product Demand Trend Analysis | Nadir | In Progress |

## Meeting Notes
Everyone attended the meeting.
And everyone agreed on the tasks they've been assigned.

## Completed Work
  1. GitHub repository setup
  2. Step A tasks: [file index and supporting reports](../docs/README.md).
  3. Tasks A
  4. Adopted the verified stock-adjustment repair on [actual date].
    Corrected 1,227 signed quantities and preserved all other fields.
    The adopted file's hash matches the reviewed candidate.
    Correction evidence: Data/interim/adjustment_review/adjustment_changes.csv.

### Section A results summary

- **Dataset coverage:** 12 cleaned tables cover 30 products, 6 branches, 8 suppliers, and 500 customers. These entity counts were checked against the current CSVs and match the [profiling report](../Reports/profiling/A1_Data_Profiling_Report.xlsx).
- **Cleaning and missing values:** the [cleaning log](../Reports/data_quality/A2_Data_Cleaning_Log.xlsx) documents date conversion and extraction of numeric warehouse capacity. A check of the current purchase-order headers found 2,370 blank `received_date` values, all on cancelled orders, consistent with the log's explanation. CSV date columns still need explicit date parsing when loaded into analysis tools.
- **Available feature outputs:** `inventory_position.csv` contains 180 rows and 39 columns; `stock_movements_enriched.csv` contains 237,230 rows and 32 columns; `customer_features.csv` contains 500 rows and 32 columns. These dimensions match the [feature dictionary](../docs/A4_Feature_Dictionary.xlsx), which documents inventory metrics, movement features, and customer RFM features.
- **Inventory finding:** all 180 rows in the current `inventory_master.csv` have `current_stock > max_stock`, confirming the observation in the cleaning log. Section B should investigate the stock balances and thresholds before making procurement recommendations.
- **Validation evidence and limitation:** the [completion summary](../Reports/validation/A5_Section_A_Completion_Summary.xlsx) records passing relationship, quantity, date-ordering, and feature checks. Those checks have not all been independently rerun. The [integration guide](../docs/A3_Integrated_Tables_Guide.xlsx) and completion summary list `sales_analysis.csv` and `purchase_analysis.csv`, but neither file is present in this repository. The available sales and purchase order-header CSVs do not replace the documented line-level integrated tables.

### File organization - 2 October 2026
- Organized the 22 supplied Section A files into `Data/processed/cleaned/`, `Data/processed/integrated/`, `Reports/`, and `docs/`.
- Preserved all filenames and contents; all 22 before-and-after SHA-256 comparisons matched.
- Added repository navigation and a complete Section A file index. This organization work does not independently validate the analyses or confirm portal submission.

## Blockers

- Repeated invoice IDs: 196 groups contain conflicting records.
- Repeated payment IDs: 201 groups contain conflicting records.
- Inventory reconciliation: 14 product–branch positions differ from
  their final ledger balances; snapshot timing needs clarification.
- Cancelled-order movements: 1,275 outbound and 1,542 inbound movements
  reference orders currently marked cancelled; their treatment needs
  investigation.

## Next Steps
- Confirm technical roles and the draft Step B task allocation with the team.
- Agree on Section B, C, D KPI formulas, time periods, and classification thresholds before producing results; investigate the inventory overstock observation.
