# Data directory guide

Organized on 6 October 2026; extended with Sections C and D on 16 October 2026. Navigate by processing stage, then section, then task. Each task folder contains the CSVs associated with that task; shared inputs stay in Section A.

```text
Data/
|-- raw/                         Original downloads, when available
|-- processed/
|   |-- cleaned/
|   |   `-- section_a/
|   |       `-- A2/              12 cleaned source tables
|   `-- integrated/
|       |-- section_a/
|       |   |-- A3/              6 integration tables
|       |   `-- A4/              1 customer-feature table
|       |-- section_b/
|       |   |-- B1/              Product performance (1 CSV)
|       |   |-- B2/              Fast-moving products (1 CSV)
|       |   |-- B3/              Slow/dead stock (1 CSV)
|       |   |-- B4/              Inventory turnover (1 CSV)
|       |   |-- B5/              Stock health (2 CSVs)
|       |   |-- B6/              Inventory aging (2 CSVs)
|       |   |-- B7/              ABC classification (1 CSV)
|       |   |-- B8/              Overstock/understock (2 CSVs)
|       |   `-- B9/              Demand trends (4 CSVs)
|       |-- section_c/
|       |   |-- C1/              Space utilisation (1 CSV)
|       |   |-- C2/              Throughput (1 CSV)
|       |   |-- C3/              Capacity (1 CSV)
|       |   |-- C4/              Alignment (2 CSVs)
|       |   |-- C5/              Performance scoring (1 CSV)
|       |   |-- C6/              Bottlenecks (1 CSV)
|       |   `-- C7/              Benchmarking (2 CSVs)
|       `-- section_d/
|           |-- D1/              Contribution (2 CSVs)
|           |-- D2/              Reliability (1 CSV)
|           |-- D3/              Performance (1 CSV)
|           |-- D4/              Dependency (1 CSV)
|           |-- D5/              Critical suppliers (1 CSV)
|           `-- D6/              Diversification (2 CSVs)
|-- interim/
|   `-- section_a/
|       `-- A5/
|           `-- adjustment_review/  3 review/evidence CSVs
`-- external/                   External data, when needed
```

`cleaned` holds prepared source tables. `integrated` holds joined tables, features, and derived analytical outputs. Sections B, C, and D currently supply analytical results, so their CSVs belong under `integrated/section_b/`, `integrated/section_c/`, and `integrated/section_d/` respectively. Add a `cleaned/` folder for a later section only if distinct cleaned inputs are actually produced for that section; reuse existing A2 tables otherwise.

Task prefixes are retained in filenames so exported files remain identifiable. Files that support multiple tasks have one canonical location; for example, the A3 sales table also contains A4 features. A1 reports and A6 documentation are linked from the Section A index rather than represented by empty data folders.

| Find | Location |
|---|---|
| Cleaned source inputs | [Section A / A2](processed/cleaned/section_a/A2/) |
| Joined analysis tables | [Section A / A3](processed/integrated/section_a/A3/) |
| Customer features | [Section A / A4](processed/integrated/section_a/A4/) |
| Adjustment review evidence | [Section A / A5](interim/section_a/A5/adjustment_review/) |
| Product and inventory outputs | [Section B / B1-B9](processed/integrated/section_b/) |
| Warehouse outputs | [Section C / C1-C7](processed/integrated/section_c/) |
| Supplier outputs | [Section D / D1-D6](processed/integrated/section_d/) |
| Section A reports, scripts, and CSV index | [Section A index](../docs/section_a.md) |
| Section B reports and CSV index | [Section B index](../docs/section_b.md) |
| Section C reports and CSV index | [Section C index](../docs/section_c.md) |
| Section D reports and CSV index | [Section D index](../docs/section_d.md) |
| Original Section A filenames mapped to current paths | [Filename mapping](../docs/section_a_filenames.md) |

Both Python scripts use the new task folders. Update saved external data connections or teammates' local scripts to these paths. The original workbooks may retain old path descriptions; their contents have been preserved.
