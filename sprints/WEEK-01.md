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

Files are mapped by task code in the [Section A file index](../docs/section_a.md). Existing team-recorded owners and statuses are preserved; unresolved validation issues remain listed below.

| Code | Task | Owner | Status | Report or reference |
|---|---|---|---|---|
| A1 | Data Profiling & Structure Analysis | Nadir | Done | [Profiling report](../Reports/profiling/A1_Data_Profiling_Report.xlsx) |
| A2 | Data Cleaning & Quality Improvement | Nadir | Done | [Cleaning log](../Reports/data_quality/A2_Data_Cleaning_Log.xlsx) |
| A3 | Data Integration & Dataset Merging | Golla | Done | [Integrated tables guide](../docs/A3_Integrated_Tables_Guide.xlsx) |
| A4 | Feature Engineering for Analytics | Festus | Done | [Feature dictionary](../docs/A4_Feature_Dictionary.xlsx) |
| A5 | Data Validation & Consistency Checks | Festus | Done | [Validation and completion summary](../Reports/validation/A5_Section_A_Completion_Summary.xlsx) |
| A6 | Data Dictionary & Documentation | Ammar | Done | [Dictionary index](../docs/A6_Data_Dictionary_Index.md) |

## Step B Tasks

Outputs for all nine tasks were supplied and organized on 5 October 2026: [Section B file index](../docs/section_b.md). Existing owners and statuses below are retained pending the team's review of the outputs.

| Code | Task | Owner | Status |
|------|-------|--------|
| B1 | Product Performance Analysis | Nadir | Done |
| B2 | Fast-Moving Product Identification | Golla | Done |
| B3 | Slow-Moving & Dead Stock Identification | Ammar | Done |
| B4 | Inventory Turnover Analysis | Festus | Done |
| B5 | Stock Health Assessment | Golla | Done |
| B6 | Inventory Aging Analysis | Festus | Done |
| B7 | ABC / Pareto Product Classification | Ammar | Done |
| B8 | Overstock & Understock Detection | Nadir | Done |
| B9 | Product Demand Trend Analysis | Nadir | Done |

### Section B file organization - 5 October 2026

- Organized 15 CSV outputs into `Data/processed/section_b/`, nine analysis workbooks into `Reports/product_inventory/`, and the completion summary into `Reports/validation/`.
- Preserved all 25 filenames and file contents; every before-and-after SHA-256 comparison matched.
- Added links and CSV dimensions in the [Section B file index](../docs/section_b.md). This verifies file organization, not analytical correctness or submission status.

## Meeting Notes
Everyone attended the meeting.
And everyone agreed on the tasks they've been assigned.

## Completed Work
  1. GitHub repository setup
  2. Step A tasks: [file index and supporting reports](../docs/section_a.md).
  3. Tasks A
  4. Adopted the verified stock-adjustment repair on [actual date].
    Corrected 1,227 signed quantities and preserved all other fields.
    The adopted file's hash matches the reviewed candidate.
    Correction evidence: Data/interim/section_a/A5/adjustment_review/A5_adjustment_changes.csv.

### Section A results summary

- **Dataset coverage:** 12 cleaned tables cover 30 products, 6 branches, 8 suppliers, and 500 customers. These entity counts were checked against the current CSVs and match the [profiling report](../Reports/profiling/A1_Data_Profiling_Report.xlsx).
- **Cleaning and missing values:** the [cleaning log](../Reports/data_quality/A2_Data_Cleaning_Log.xlsx) documents date conversion and extraction of numeric warehouse capacity. A check of the current purchase-order headers found 2,370 blank `received_date` values, all on cancelled orders, consistent with the log's explanation. CSV date columns still need explicit date parsing when loaded into analysis tools.
- **Available feature outputs:** `A3_inventory_position.csv` contains 180 rows and 39 columns; `A3_stock_movements_enriched.csv` contains 237,230 rows and 32 columns; `A4_customer_features.csv` contains 500 rows and 32 columns. These dimensions match the [feature dictionary](../docs/A4_Feature_Dictionary.xlsx), which documents inventory metrics, movement features, and customer RFM features.
- **Inventory finding:** all 180 rows in the current `A2_inventory_master.csv` have `current_stock > max_stock`, confirming the observation in the cleaning log. Section B should investigate the stock balances and thresholds before making procurement recommendations.
- **Validation evidence and limitation:** the [completion summary](../Reports/validation/A5_Section_A_Completion_Summary.xlsx) records the team's original checks. Reconstructed `A3_sales_analysis.csv` and `A3_purchase_analysis.csv` are now present; their schemas differ from those originally documented. See the [Section A index](../docs/section_a.md) for current files, dimensions, and repair evidence. The unresolved issues below still limit claims of full validation.

### File organization - 2 October 2026
- Organized the 22 supplied Section A files into `Data/processed/cleaned/`, `Data/processed/integrated/`, `Reports/`, and `docs/`.
- Preserved all filenames and contents; all 22 before-and-after SHA-256 comparisons matched.
- Added repository navigation and a complete Section A file index. This organization work does not independently validate the analyses or confirm portal submission.

### Data folder organization - 6 October 2026

- Grouped 37 CSVs by processing stage, section, and task: A2 cleaned inputs, A3-A4 integrated outputs, A5 review evidence, and B1-B9 analysis outputs.
- Updated both Python scripts and current file links; see the [Data directory guide](../Data/README.md). Earlier organization entries describe the locations used at those dates.
- File contents and task ownership/statuses remain unchanged.

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
