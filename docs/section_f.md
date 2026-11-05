# Section F: Forecasting & Predictive Analytics

The supplied Section F package covers product demand forecasting, inventory-level forecasting, stockout-risk ranking, reorder-point and safety-stock calculations, and scenario analysis. Its completion summary contains results and deliverables for F1-F6; that records supplied work, not independent validation of the methods or forecasts.

The original package contained 13 CSVs and five workbooks. All 18 files were moved on 4 November 2026; SHA-256 hashes matched before and after. CSVs are under `Data/processed/integrated/section_f/`, analysis workbooks are under `Reports/forecasting/`, and the completion summary is under `Reports/validation/`.

## Deliverables

| Task | CSV outputs | Dimensions | Workbook / evidence |
|---|---|---|---|
| F1 Product Demand Forecasting | [Monthly demand detail](../Data/processed/integrated/section_f/F1/F1_monthly_demand_detail.csv); [product forecast](../Data/processed/integrated/section_f/F1/F1_product_demand_forecast.csv) | 2,160 × 5; 30 × 23 | [F1 workbook](../Reports/forecasting/F1_Product_Demand_Forecast.xlsx) |
| F2 Inventory Level Forecasting | [Product inventory forecast](../Data/processed/integrated/section_f/F2/F2_product_inventory_forecast.csv); [product-branch detail shared with F3](../Data/processed/integrated/section_f/F2/F2_F3_inventory_forecast_detail.csv) | 30 × 12; 180 × 29 | [F2-F3 workbook](../Reports/forecasting/F2_F3_Inventory_Forecast_and_Stockout_Risk.xlsx) |
| F3 Stockout Risk Prediction | [Relative stockout-risk ranking](../Data/processed/integrated/section_f/F3/F3_relative_stockout_risk_rank.csv) | 50 × 30 | [F2-F3 workbook](../Reports/forecasting/F2_F3_Inventory_Forecast_and_Stockout_Risk.xlsx) |
| F4 Reorder Point Optimisation | [ROP and safety-stock table shared with F5](../Data/processed/integrated/section_f/F4/F4_F5_rop_safety_stock.csv) | 30 × 27 | [F4-F5 workbook](../Reports/forecasting/F4_F5_ROP_and_Safety_Stock.xlsx) |
| F5 Safety Stock Calculation | Same shared F4-F5 CSV above | 30 × 27 | [F4-F5 workbook](../Reports/forecasting/F4_F5_ROP_and_Safety_Stock.xlsx) |
| F6 Scenario-Based Inventory Forecasting | [Scenario summary](../Data/processed/integrated/section_f/F6/F6_scenario_summary.csv); five scenario detail CSVs (30 × 24 each); [base sell-down path](../Data/processed/integrated/section_f/F6/F6_selldown_path_base.csv) | 5 × 11; 30 × 24 each; 30 × 21 | [F6 workbook](../Reports/forecasting/F6_Scenario_Based_Forecasting.xlsx) |

The completion summary is [F_Section_F_Completion_Summary.xlsx](../Reports/validation/F_Section_F_Completion_Summary.xlsx). Shared outputs have one canonical data location to avoid duplicate files.

## Results recorded in the supplied package

- The F1 CSV forecasts 198,861.4 units for the next 12 months, compared with 199,858 actual units in the preceding 12 months. It classifies 25 products Stable, 3 Declining, and 2 Growing.
- The F2-F3 detail contains 180 unique product-branch pairs. Each is labeled Minimal risk; the median reported inventory cover is 96.7 years, with no rows flagged below reorder or safety stock.
- The F4-F5 table reports mean ROP of 416.6 units and mean safety stock of 87.1 units.
- In F6's combined stress scenario, median reported cover is 80.6 years. The supplied summary says all 30 products remain above ROP after its 60-month base sell-down projection.

The CSV checks confirmed these counts and summary values; they do not establish forecast accuracy or validate the spreadsheet methods.

## Review limits and follow-up

- The workbook describes moving-average and trend-based demand estimates using delivered-sales history. No Section F generation script or forecast backtest evidence was supplied, so the outputs are not reproducible or accuracy-tested from this repository alone.
- The completion workbook refers to `/home/workdir/artifacts/section_f/`, an environment-specific source path. The files have been relocated here, but workbook internals were preserved.
- The approximately 97-year median stock cover and stock levels far above calculated ROP are unusually large. Verify stock units and balances, demand aggregation, and source versions before acting on replenishment or stock-reduction recommendations.
- Confirm how cancelled sales, stock movements, the adjusted Section A ledger, lead times, and service-level choices were handled. Those choices affect both forecast inputs and policy parameters.
- Owners, Week 5 meeting details, dates, and Scrum Master were not recorded in the supplied Section F package or current Week 5 notes. They are left unassigned in the sprint record.

See [Week 5 sprint notes](../sprints/WEEK-05.md) for the repository work and outstanding review actions.
