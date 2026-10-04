# heavy-supplier-warehouse-analytics
CadetX team project analysing supplier performance, inventory health, and warehouse efficiency using data analytics and forecasting.

## Team roles
| Member | Technical role |
|---|---|
| Ammar Naufal | Data Analyst | Week 1 SCRUM Master
| Nadir | Data Analyst |
| Golla | Data Analyst |
| Festus | BI Analyst |

## Project files

| Location | Contents |
|---|---|
| [Data/processed/cleaned](Data/processed/cleaned/) | 12 cleaned source-table CSVs from Section A |
| [Data/processed/integrated](Data/processed/integrated/) | 7 CSVs supplied in the Section A Integration folder |
| [Reports/profiling](Reports/profiling/) | Data profiling report |
| [Reports/data_quality](Reports/data_quality/) | Data cleaning log |
| [Reports/validation](Reports/validation/) | Section A completion summary |
| [docs](docs/README.md) | Integrated tables guide, feature dictionary, and Section A file index |
| [sprints](sprints/WEEK-01.md) | Weekly sprint notes, task ownership, and progress |

`Data/raw/` is reserved for original, unmodified source data; the supplied cleaned and integrated files are stored under `Data/processed/`. `Data/external/`, `Src/`, and `Reports/visuals/` currently contain placeholders for future work.

## Weekly delivery

- [Week 1 sprint notes](sprints/WEEK-01.md): repository setup and Section A tasks, recorded as complete by the team.
- [Section A file index](docs/README.md): links to all 22 supplied files and their current locations.

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
has been adopted as Data/processed/integrated/stock_movements_enriched.csv.
The source stock ledger remains unchanged.

Section A foundation work is delivered with outstanding data-quality
limitations. These include conflicting invoice/payment identifiers,
inventory-to-ledger balance differences, and stock movements associated
with cancelled orders. Analyses using these records require further
investigation or explicitly documented treatment.
