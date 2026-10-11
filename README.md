# heavy-supplier-warehouse-analytics
CadetX team project analysing supplier performance, inventory health, and warehouse efficiency using data analytics and forecasting.

## Team roles
| Member | Technical role |
|---|---|
| Ammar Naufal | Data Analyst | Week 1 Scrum Master |
| Nadir Abdulhadi | Data Analyst | Week 2 Scrum Master |
| Golla Bhumika | Data Analyst |
| Festus Ejideaku | BI Analyst |

## Project files

| Location | Contents |
|---|---|
| [Section A: cleaned tables](Data/processed/cleaned/section_a/A2/) | 12 cleaned source-table CSVs from Section A |
| [Section A: integration and features](Data/processed/integrated/section_a/) | 7 Section A integration and feature CSVs |
| [Section B: task outputs](Data/processed/integrated/section_b/) | 15 analysis CSVs organized into B1-B9 task folders |
| [Reports/product_inventory](Reports/product_inventory/) | Nine Section B analysis workbooks covering B1-B9 |
| [Reports/profiling](Reports/profiling/) | Data profiling report |
| [Reports/data_quality](Reports/data_quality/) | Data cleaning log |
| [Reports/validation](Reports/validation/) | Section A and Section B completion summaries |
| [docs](docs/README.md) | A1-A6 and B1-B9 file indexes, dictionaries, and integration guides |
| [sprints](sprints/) | Weekly sprint notes ([Week 1](sprints/WEEK-01.md), [Week 2](sprints/WEEK-02.md)), task ownership, and progress |

`Data/raw/` is reserved for original, unmodified source data; the supplied cleaned and integrated files are stored under `Data/processed/`. `Data/external/`, `Src/`, and `Reports/visuals/` currently contain placeholders for future work.

Data folders follow processing stage, section, then task; see the [Data directory guide](Data/README.md). Section A CSV filenames use A2-A5 task prefixes; see the [filename mapping](docs/section_a_filenames.md) for old references.

## Weekly delivery

- [Week 1 sprint notes](sprints/WEEK-01.md): repository setup and Section A tasks, recorded as complete by the team.
- [Week 2 sprint notes](sprints/WEEK-02.md): Section B completion and Section C warehouse tasks in progress.
- [Section A file index](docs/section_a.md): A1-A6 task labels, current CSV dimensions, reports, scripts, and repair evidence.
- [Section B file index](docs/section_b.md): all 25 supplied files organized on 5 October 2026, covering B1-B9. File integrity was checked; analytical review remains separate.

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
threshold and balance questions are resolved
