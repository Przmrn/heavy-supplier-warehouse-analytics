# heavy-supplier-warehouse-analytics
CadetX team project analysing supplier performance, inventory health, and warehouse efficiency using data analytics and forecasting.

## Team roles
| Member | Technical role | Sprint |
|---|---|---|
| Ammar Naufal | Data Analyst | Week 1 Scrum Master |
| Nadir Abdulhadi | Data Analyst | Week 2 Scrum Master |
| Golla Bhumika | Data Analyst | Week 3 and Week 6 Scrum Master |
| Festus Ejideaku | BI Analyst | Week 4 Scrum Master |

The repository roster records four members (three Data Analysts and one BI Analyst). The CadetX brief describes a three-person team (two Data Analysts and one Data Scientist). The repository does not record whether this roster difference was approved; the listed names and roles are retained as recorded.

## Project files

| Location | Contents |
|---|---|
| [Section A: cleaned tables](Data/processed/cleaned/section_a/A2/) | 12 cleaned source-table CSVs from Section A |
| [Section A: integration and features](Data/processed/integrated/section_a/) | 7 Section A integration and feature CSVs |
| [Section B: task outputs](Data/processed/integrated/section_b/) | 15 analysis CSVs organized into B1-B9 task folders |
| [Section C: task outputs](Data/processed/integrated/section_c/) | 9 analysis CSVs organized into C1-C7 task folders |
| [Section D: task outputs](Data/processed/integrated/section_d/) | 8 analysis CSVs organized into D1-D6 task folders |
| [Section E: task outputs](Data/processed/integrated/section_e/) | 21 customer-analysis CSVs organized into E1-E9 task folders |
| [Section F: task outputs](Data/processed/integrated/section_f/) | 13 forecasting CSVs in task folders; the shared F4/F5 CSV is stored under F4 |
| [Section G: task outputs](Data/processed/integrated/section_g/) | 6 risk, anomaly, and control CSVs organized into G1-G4 task folders |
| [Reports/product_inventory](Reports/product_inventory/) | Nine Section B analysis workbooks covering B1-B9 |
| [Reports/warehouse_operations](Reports/warehouse_operations/) | Four Section C analysis workbooks covering C1-C7 |
| [Reports/supplier_procurement](Reports/supplier_procurement/) | Three Section D analysis workbooks covering D1-D6 |
| [Reports/customer_analytics](Reports/customer_analytics/) | Six Section E analysis workbooks covering E1-E9 |
| [Reports/forecasting](Reports/forecasting/) | Four Section F analysis workbooks covering F1-F6 |
| [Reports/risk_control](Reports/risk_control/) | Four Section G analysis workbooks covering G1-G4 |
| [Reports/profiling](Reports/profiling/) | Data profiling report |
| [Reports/data_quality](Reports/data_quality/) | Data cleaning log |
| [Reports/validation](Reports/validation/) | Section A-G completion summaries |
| [docs](docs/README.md) | A1-A6, B1-B9, C1-C7, D1-D6, E1-E9, F1-F6, and G1-G4 file indexes, dictionaries, and integration guides |
| [sprints](sprints/) | Weekly sprint notes ([Week 1](sprints/WEEK-01.md), [Week 2](sprints/WEEK-02.md), [Week 3](sprints/WEEK-03.md), [Week 4](sprints/WEEK-04.md), [Week 5](sprints/WEEK-05.md), [Week 6](sprints/WEEK-06.md)), task ownership, and progress |

`Data/raw/` is reserved for original, unmodified source data; the supplied cleaned and integrated files are stored under `Data/processed/`. `Data/external/`, `Src/`, and `Reports/visuals/` currently contain placeholders for future work.

Data folders follow processing stage, section, then task; see the [Data directory guide](Data/README.md). Section A CSV filenames use A2-A5 task prefixes; see the [filename mapping](docs/section_a_filenames.md) for old references.

## Reproducing the work

The Section A scripts use pandas; install the listed dependency with `python -m pip install -r requirements.txt`. The entry points are `python Notebooks/build.analysis_tables.py` for the selected sales and purchase outputs and `python Notebooks/repair_adjusments.py` for the stock-movement repair candidate. Both scripts stop when their output targets already exist. Those targets are populated in this repository, so these commands will not reproduce the outputs from the current checkout as-is. Reproduction requires a separate, empty output location or a deliberate code/configuration change to point the scripts there; do not delete team outputs to rerun them. The pinned dependency and commands have not been verified in this audit environment.

Sections B-G contain workbooks with written method descriptions and static results, plus CSV exports. The workbooks do not contain executable spreadsheet formulas, except for one formula cell in the G2 workbook, and no generation scripts for those sections are included. These outputs cannot be regenerated from this repository alone. Their analytical review and input-version checks remain open as described in the section indexes.

## Weekly delivery

- [Week 1 sprint notes](sprints/WEEK-01.md): repository setup and Section A tasks, recorded as complete by the team.
- [Week 2 sprint notes](sprints/WEEK-02.md): Section B completion and Section C warehouse tasks in progress.
- [Week 3 sprint notes](sprints/WEEK-03.md): confirm organized Section C/D outputs and agree the next analysis scope.
- [Week 4 sprint notes](sprints/WEEK-04.md): organize the Section E customer-analytics package; Section F is deferred.
- [Week 5 sprint notes](sprints/WEEK-05.md): organize the Section F forecasting and predictive-analytics package.
- [Week 6 sprint notes](sprints/WEEK-06.md): organize the Section G risk, anomaly, and control-analytics package.
- [Section A file index](docs/section_a.md): A1-A6 task labels, current CSV dimensions, reports, scripts, and repair evidence.
- [Section B file index](docs/section_b.md): all 25 supplied files organized on 5 October 2026, covering B1-B9. File integrity was checked; analytical review remains separate.
- [Section C file index](docs/section_c.md): all 14 supplied files organized on 16 October 2026, covering C1-C7. File integrity was checked; analytical review remains separate.
- [Section D file index](docs/section_d.md): all 12 supplied files organized on 16 October 2026, covering D1-D6. File integrity was checked; analytical review remains separate.
- [Section E file index](docs/section_e.md): all 28 supplied files organized on 29 October 2026, covering E1-E9. File integrity and CSV dimensions were checked; analytical review remains separate.
- [Section F file index](docs/section_f.md): 18 supplied files organized on 4 November 2026, covering F1-F6. File integrity and selected CSV summaries were checked; forecast validation remains open.
- [Section G file index](docs/section_g.md): 11 supplied files organized on 13 November 2026, covering G1-G4. File count, CSV dimensions, and workbook archive readability were checked; analytical validation remains open.

## Section A results summary

Section A deliverables include 12 cleaned source tables, 7 CSVs in
the integration folder, 5 supporting workbooks, and Python scripts
for reconstructing analysis tables and repairing adjustment signs.

The reconstructed sales analysis contains 130,402 rows and 48 columns.
The purchase analysis contains 155,495 rows and 49 columns. These
outputs omit classification bands whose thresholds were not fully
specified in the original documentation, so they do not exactly
reproduce the documented original schemas.

The stock-movement repair corrected 1,227 adjustment signs across
237,230 movements. Other fields were preserved. The verified candidate
has been adopted as Data/processed/integrated/section_a/A3/A3_stock_movements_enriched.csv.
The source stock ledger remains unchanged.

Section A foundation work is delivered with outstanding data-quality
limitations. These include conflicting invoice/payment identifiers,
inventory-to-ledger balance differences, and stock movements associated
with cancelled orders. Analyses using these records require further
investigation or explicitly documented treatment.

## Section B results summary

Section B deliverables cover B1-B9 product and inventory analysis:
15 CSVs in `Data/processed/integrated/section_b/B1/` through `B9/`,
nine workbooks in `Reports/product_inventory/`, and the completion
summary in `Reports/validation/`. All 30 products and all 180
product-branch combinations are covered.

Revenue is highly concentrated in Delivered sales (22.96B total,
tied to `A3_sales_analysis` Delivered `line_total`). The top two
products hold 35.9% of revenue; the nine Class A products hold
about 78%. Turnover is extremely low (around 0.01x), and overstock
is flagged for all 30 products at all six branches by the current
max-stock thresholds. Demand was stable to slightly declining from
2019 (3.87B) to 2024 (3.68B).

These findings remain limited by unresolved inputs: workbook-only
methods with no generation scripts, unrecorded input versions
relative to the adjustment-sign repair, negative ageing-day values
needing a method fix, and the Section A data-quality issues above.
Do not base procurement cuts on the overstock figures until the
threshold and balance questions are resolved.

## Section C results summary

Section C deliverables cover C1-C7 warehouse operations and
efficiency: 9 CSVs in `Data/processed/integrated/section_c/C1/`
through `C7/`, four workbooks in `Reports/warehouse_operations/`
(C2/C3, C4/C5, and C6/C7 workbooks each cover two tasks), and the
completion summary in `Reports/validation/`.

Per the team summary, all six warehouses are under heavy stock load:
total capacity is 226,080 sqft (tied to the C1 CSV), density runs
288-380x the max-stock design across sites, and every branch holds
the full 30-product catalogue with about 80% of stock value in
Class A. Inbound volume exceeds outbound at every site while the
turns proxy sits near 0.01, so capacity pressure comes from stock
held rather than traffic peaks. Kolkata and Ahmedabad benchmark
highest on value density; Delhi and Chennai score relatively
stronger but remain far above design density. No single warehouse
is flagged as the primary bottleneck, pointing to a network-wide
stock-level problem rather than one broken site.

These are team-reported findings: methods are workbook-only with
no generation scripts, input versions relative to the
adjustment-sign repair are unrecorded, and the Section A
data-quality issues above carry into these outputs.

## Section D results summary

Section D deliverables cover D1-D6 supplier and procurement
analytics: 8 CSVs in `Data/processed/integrated/section_d/D1/`
through `D6/`, three workbooks in `Reports/supplier_procurement/`
(the D2/D3/D4 and D5/D6 workbooks each cover multiple tasks), and
the completion summary in `Reports/validation/`.

Per the team summary, spend is evenly spread across 8 suppliers
(shares 12.1-12.9%, summing to 100% in the D1 CSV; top-3 share
38.1%, HHI 1,250 - diversified). On-time delivery ranges 84.1-85.6%
across suppliers with no outliers on either side. Every product is
supplied by all 8 suppliers, so no product is single-sourced. Two
suppliers sit in the top criticality tier for priority contract and
buffer review; score gaps elsewhere are modest.

These are team-reported findings: methods are workbook-only with
no generation scripts, input versions relative to the
adjustment-sign repair are unrecorded, and the Section A
data-quality issues above (including invoice/payment identifier
conflicts relevant to purchase records) carry into these outputs.

## Section E results summary

Section E covers customer purchase behaviour, RFM, personas, customer lifetime value, retention, churn, cohorts, high-value customers, and at-risk customers. The package contains 21 CSVs, six workbooks, and a completion summary; the CSVs are organized under `Data/processed/integrated/section_e/E1/` through `E9/`.

The supplied results cover 500 distinct customers and 22.96B total delivered-sales revenue. The yearly table reports 99.6-100% retention from 2019 through 2023; the churn list contains 5 customers. The high-value list contains 223 customers, while the priority at-risk list contains 46 high-value customers. The highest predicted-CLV quintile represents 59.2% of predicted CLV.

These are team-reported output figures, not independent validation. The workbooks contain written method sheets but no executable formulas, and no Section E generation script was supplied. The separate E6 and E9 at-risk lists contain 110 and 174 customers respectively; their definitions need reconciliation before using the classifications for decisions. See the [Section E index](docs/section_e.md) for dimensions and review limitations.

## Section F results summary

Section F covers product demand forecasting, inventory-level forecasting, stockout-risk ranking, reorder points, safety stock, and scenario analysis. The package contains 13 CSVs, four task workbooks, and a completion summary. CSVs are organized under `Data/processed/integrated/section_f/F1/` through `F6/`; workbooks are in `Reports/forecasting/`.

The supplied results forecast 198,861 units over the next 12 months versus 199,858 units in the previous 12 months. Demand is classified as Stable for 25 products, Declining for 3, and Growing for 2. The inventory detail covers 180 unique product-branch positions; all are labeled Minimal stockout risk, with median cover of about 96.7 years. The reported mean reorder point is about 417 units and mean safety stock about 87 units. Under the combined stress scenario, median cover remains about 80.6 years.

These figures were cross-checked against the CSV exports, not independently validated as forecasts. The package provides moving-average/trend methods in its workbooks but no generation script or backtest evidence. The analysis uses delivered-sales history; demand, lead-time, service-level, stock-balance, and source-version assumptions need review before operational use. The extreme stock-cover results are a reason to verify inventory balances and units before acting on proposed replenishment or stock-reduction policies. See the [Section F index](docs/section_f.md) for file dimensions and limitations.

## Section G results summary

Section G covers inventory-movement anomaly detection, stock-shrinkage reconciliation, operational-risk monitoring, and data-integrity checks. The package contains six CSVs, four task workbooks, and a completion summary. CSVs are organized under `Data/processed/integrated/section_g/G1/` through `G4/`; workbooks are in `Reports/risk_control/`.

The supplied outputs identify 18 notable movement anomalies from 237,230 ledger movements, all on adjustment records; no extreme anomalies are reported. The reconciliation table flags a balance gap and sales-to-ledger-out mismatch at all 180 product-branch positions, with aggregate gaps of -69,656 and +110,107 units respectively. The risk-register CSV records 3 High, 8 Medium, and 4 Low risks. Data-integrity outputs report 28 checks: 2 High findings and 26 OK.

These are supplied output figures, not independent control validation. The completion summary says there are 9 Medium risks, while the underlying risk-register CSV has 8; this needs reconciliation. No Section G generation scripts or test evidence were supplied. Balance, movement, adjustment, stock-unit, and source-version assumptions need review before interpreting reconciliation gaps as shrinkage or using the risk register for operational decisions. See the [Section G index](docs/section_g.md) for dimensions and limitations.
