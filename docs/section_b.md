# Section B: Product & Inventory Analytics

The 25 files supplied in `section_b/` were organized on 5 October 2026. This index links all nine task reports, 15 CSV outputs, and the section completion summary.

## Locations and preservation

| Original files | Current location |
|---|---|
| `section_b/*.csv` (15 files) | `Data/processed/integrated/section_b/B1/` through `B9/` |
| `section_b/B1_*.xlsx` through `section_b/B9_*.xlsx` (9 files) | `Reports/product_inventory/` |
| `section_b/B_Section_B_Completion_Summary.xlsx` | `Reports/validation/` |

All original filenames and file contents were preserved; all 25 before-and-after SHA-256 comparisons matched. The ten workbooks passed ZIP integrity checks, with no external relationships, external-link parts, connections, or query-table parts found. Embedded text may still refer to the original folder; use the mapping above.

## Task reports

| Task | Analysis | Workbook |
|---|---|---|
| B1 | Product Performance Analysis | [B1_Product_Performance_Analysis.xlsx](../Reports/product_inventory/B1_Product_Performance_Analysis.xlsx) |
| B2 | Fast-Moving Product Identification | [B2_Fast_Moving_Products.xlsx](../Reports/product_inventory/B2_Fast_Moving_Products.xlsx) |
| B3 | Slow-Moving & Dead Stock Identification | [B3_Slow_Dead_Stock.xlsx](../Reports/product_inventory/B3_Slow_Dead_Stock.xlsx) |
| B4 | Inventory Turnover Analysis | [B4_Inventory_Turnover.xlsx](../Reports/product_inventory/B4_Inventory_Turnover.xlsx) |
| B5 | Stock Health Assessment | [B5_Stock_Health_Assessment.xlsx](../Reports/product_inventory/B5_Stock_Health_Assessment.xlsx) |
| B6 | Inventory Aging Analysis | [B6_Inventory_Aging.xlsx](../Reports/product_inventory/B6_Inventory_Aging.xlsx) |
| B7 | ABC / Pareto Product Classification | [B7_ABC_Pareto_Classification.xlsx](../Reports/product_inventory/B7_ABC_Pareto_Classification.xlsx) |
| B8 | Overstock & Understock Detection | [B8_Overstock_Understock_Detection.xlsx](../Reports/product_inventory/B8_Overstock_Understock_Detection.xlsx) |
| B9 | Product Demand Trend Analysis | [B9_Product_Demand_Trends.xlsx](../Reports/product_inventory/B9_Product_Demand_Trends.xlsx) |

[Section B completion summary](../Reports/validation/B_Section_B_Completion_Summary.xlsx)

On 6 October 2026, the 15 CSVs were grouped into B1-B9 task folders under `Data/processed/integrated/section_b/`. These are derived analytical outputs; cleaned source tables remain shared Section A inputs. See the [Data directory guide](../Data/README.md).

## CSV outputs

Dimensions below were read from the supplied CSV files; row counts exclude the header.

| Task | File | Rows | Columns |
|---|---|---:|---:|
| B1 | [B1_product_performance.csv](../Data/processed/integrated/section_b/B1/B1_product_performance.csv) | 30 | 25 |
| B2 | [B2_fast_moving_products.csv](../Data/processed/integrated/section_b/B2/B2_fast_moving_products.csv) | 30 | 26 |
| B3 | [B3_slow_dead_stock.csv](../Data/processed/integrated/section_b/B3/B3_slow_dead_stock.csv) | 30 | 30 |
| B4 | [B4_inventory_turnover.csv](../Data/processed/integrated/section_b/B4/B4_inventory_turnover.csv) | 30 | 21 |
| B5 | [B5_stock_health_by_product.csv](../Data/processed/integrated/section_b/B5/B5_stock_health_by_product.csv) | 30 | 15 |
| B5 | [B5_stock_health_detail.csv](../Data/processed/integrated/section_b/B5/B5_stock_health_detail.csv) | 180 | 47 |
| B6 | [B6_inventory_aging_by_product.csv](../Data/processed/integrated/section_b/B6/B6_inventory_aging_by_product.csv) | 30 | 10 |
| B6 | [B6_inventory_aging_detail.csv](../Data/processed/integrated/section_b/B6/B6_inventory_aging_detail.csv) | 180 | 22 |
| B7 | [B7_ABC_classification.csv](../Data/processed/integrated/section_b/B7/B7_ABC_classification.csv) | 30 | 20 |
| B8 | [B8_overstock_by_product.csv](../Data/processed/integrated/section_b/B8/B8_overstock_by_product.csv) | 30 | 9 |
| B8 | [B8_overstock_understock_detail.csv](../Data/processed/integrated/section_b/B8/B8_overstock_understock_detail.csv) | 180 | 52 |
| B9 | [B9_class_a_yearly_trend.csv](../Data/processed/integrated/section_b/B9/B9_class_a_yearly_trend.csv) | 54 | 6 |
| B9 | [B9_trend_by_month_seasonality.csv](../Data/processed/integrated/section_b/B9/B9_trend_by_month_seasonality.csv) | 12 | 6 |
| B9 | [B9_trend_by_year.csv](../Data/processed/integrated/section_b/B9/B9_trend_by_year.csv) | 6 | 8 |
| B9 | [B9_trend_by_year_month.csv](../Data/processed/integrated/section_b/B9/B9_trend_by_year_month.csv) | 72 | 4 |

## Review status

Files have been organized and inventoried; their analytical calculations, input versions, and business conclusions have not been independently validated in this organization task. The supplied completion summary is a team artifact, not proof of independent review. Existing task owners and statuses in the [Week 1 sprint notes](../sprints/WEEK-01.md) are preserved.

Before relying on the results, check their methods and source versions against the current integrated data, including the adopted adjustment repair and documented unresolved data-quality issues. These files are analysis outputs, not original source data. No Section B generation scripts were included in the supplied folder; add the actual working code or queries when available.

