# Week 2 Sprint Notes

## Scrum Master
Nadir Abdulhadi

## Sprint Goal
Finish Section B product and inventory analysis and start Section C warehouse operations analysis.

## Activities
| Task | Owner | Status |
|------|-------|--------|
| Prepare the Week 2 sprint notes | Nadir | Done |

## Step A Tasks
| Code | Task | Owner | Status | Report or reference |
|---|---|---|---|---|
| A1 | Data Profiling & Structure Analysis | Nadir | Done | [Profiling report](../Reports/profiling/A1_Data_Profiling_Report.xlsx) |
| A2 | Data Cleaning & Quality Improvement | Nadir | Done | [Cleaning log](../Reports/data_quality/A2_Data_Cleaning_Log.xlsx) |
| A3 | Data Integration & Dataset Merging | Golla | Done | [Integrated tables guide](../docs/A3_Integrated_Tables_Guide.xlsx) |
| A4 | Feature Engineering for Analytics | Festus | Done | [Feature dictionary](../docs/A4_Feature_Dictionary.xlsx) |
| A5 | Data Validation & Consistency Checks | Festus | Done | [Validation and completion summary](../Reports/validation/A5_Section_A_Completion_Summary.xlsx) |
| A6 | Data Dictionary & Documentation | Ammar | Done | [Dictionary index](../docs/A6_Data_Dictionary_Index.md) |

## Step B Tasks
| Code | Task | Owner | Status | Report or reference |
|---|---|---|---|---|
| B1 | Product Performance Analysis | Nadir | Done | [B1 report](../Reports/product_inventory/B1_Product_Performance_Analysis.xlsx) |
| B2 | Fast-Moving Product Identification | Golla | Done | [B2 report](../Reports/product_inventory/B2_Fast_Moving_Products.xlsx) |
| B3 | Slow-Moving & Dead Stock Identification | Ammar | Done | [B3 report](../Reports/product_inventory/B3_Slow_Dead_Stock.xlsx) |
| B4 | Inventory Turnover Analysis | Festus | Done | [B4 report](../Reports/product_inventory/B4_Inventory_Turnover.xlsx) |
| B5 | Stock Health Assessment | Golla | Done | [B5 report](../Reports/product_inventory/B5_Stock_Health_Assessment.xlsx) |
| B6 | Inventory Aging Analysis | Festus | Done | [B6 report](../Reports/product_inventory/B6_Inventory_Aging.xlsx) |
| B7 | ABC / Pareto Product Classification | Ammar | Done | [B7 report](../Reports/product_inventory/B7_ABC_Pareto_Classification.xlsx) |
| B8 | Overstock & Understock Detection | Nadir | Done | [B8 report](../Reports/product_inventory/B8_Overstock_Understock_Detection.xlsx) |
| B9 | Product Demand Trend Analysis | Nadir | Done | [B9 report](../Reports/product_inventory/B9_Product_Demand_Trends.xlsx) |

## Step C Tasks
| Code | Task | Owner | Status |
|------|-------|--------|
| C1 | Warehouse Space Utilisation Analysis | Ammar | In Progress |
| C2 | Warehouse Throughput Analysis | Ammar | In Progress |
| C3 | Warehouse Capacity Analysis | Nadir | In Progress |
| C4 | Product–Warehouse Alignment | Golla | In Progress |
| C5 | Warehouse Performance Scoring | Festus | In Progress |
| C6 | Operational Bottleneck Detection | Golla | In Progress |
| C7 | Warehouse Utilisation Benchmarking | Festus | In Progress |

## Meeting Notes
Everyone attended the meeting.
And everyone agreed on the tasks they've been assigned.

## Completed Work
  1. Step A tasks: [file index and supporting reports](../docs/section_a.md).
  2. Step B tasks: [file index and supporting reports](../docs/section_b.md).

## Blockers
- Repeated invoice IDs: 196 groups contain conflicting records.
- Repeated payment IDs: 201 groups contain conflicting records.
- Inventory reconciliation: 14 product–branch positions differ from
  their final ledger balances; snapshot timing needs clarification.
- Cancelled-order movements: 1,275 outbound and 1,542 inbound movements
  reference orders currently marked cancelled; their treatment needs
  investigation.

## Next Steps
- Work on the assigned Step C tasks.
- Agree on Section C KPI formulas and thresholds before producing results.
