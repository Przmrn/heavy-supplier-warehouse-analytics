# Week 5 Sprint Notes

## Scrum Master

Ammar Naufal

## Sprint Goal

Repository work completed in this session: organize the task F files forecasting outputs, add a file index and results summary, and record review limits.

## Activities

| Activity | Owner | Status |
|---|---|---|
| Organize the files for tasks 5 and commit to the repository | Ammar | Done |
| Confirm the Week 4 meeting, Tasks owners, and sprint objectives | Ammar | Done |

## Section F Tasks

The supplied completion summary includes outputs for F1-F6. The package does not identify task owners; no individual assignments are inferred here.

| Code | Task | Owner | Status | Evidence |
|---|---|---|---|---|
| F1 | Product Demand Forecasting | Festus | Done | [F1 workbook](../Reports/forecasting/F1_Product_Demand_Forecast.xlsx) |
| F2 | Inventory Level Forecasting | Golla | Done | [F2-F3 workbook](../Reports/forecasting/F2_F3_Inventory_Forecast_and_Stockout_Risk.xlsx) |
| F3 | Stockout Risk Prediction | Nadir | Done | [F2-F3 workbook](../Reports/forecasting/F2_F3_Inventory_Forecast_and_Stockout_Risk.xlsx) |
| F4 | Reorder Point Optimisation | Festus | Done | [F4-F5 workbook](../Reports/forecasting/F4_F5_ROP_and_Safety_Stock.xlsx) |
| F5 | Safety Stock Calculation | Golla | Done | [F4-F5 workbook](../Reports/forecasting/F4_F5_ROP_and_Safety_Stock.xlsx) |
| F6 | Scenario-Based Inventory Forecasting | Festus | Done | [F6 workbook](../Reports/forecasting/F6_Scenario_Based_Forecasting.xlsx) |

## Meeting Notes and Decisions

No meeting notes.

## Results and Review Limits

- The supplied forecast totals 198,861.4 units for the next 12 months versus 199,858 actual units in the previous 12 months; 25 products are Stable, 3 Declining, and 2 Growing.
- The inventory detail covers 180 product-branch pairs and labels all as Minimal stockout risk. Median reported cover is 96.7 years.
- Mean calculated ROP is 416.6 units; mean safety stock is 87.1 units.
- These values and row counts were checked against the CSV exports. Forecast accuracy, formula assumptions, and source-version alignment were not validated. See the [Section F index](../docs/section_f.md).
- The extreme stock-cover result needs investigation before acting on the workbook's replenishment or stock-reduction advice.

## Blockers and Next Steps

- Review forecast validation and assumptions, including the sales history period, demand units, lead-time calculation, service levels, and treatment of cancelled orders and stock adjustments.
- Confirm the inventory snapshot and units behind the reported years of cover; reconcile against Section A and relevant inventory analyses.
- Record actual Week 5 dates, Scrum Master, meeting decisions, and task owners if available from the team.
- Stage and commit the Week 5 package, push it to GitHub, verify the remote, and submit the repository link separately in the CadetX portal. 
