# Data directory guide

Organized on 6 October 2026. Navigate by processing stage, then section, then task. Each task folder contains the CSVs associated with that task; shared inputs stay in Section A.

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
|       `-- section_b/
|           |-- B1/              Product performance (1 CSV)
|           |-- B2/              Fast-moving products (1 CSV)
|           |-- B3/              Slow/dead stock (1 CSV)
|           |-- B4/              Inventory turnover (1 CSV)
|           |-- B5/              Stock health (2 CSVs)
|           |-- B6/              Inventory aging (2 CSVs)
|           |-- B7/              ABC classification (1 CSV)
|           |-- B8/              Overstock/understock (2 CSVs)
|           `-- B9/              Demand trends (4 CSVs)
|-- interim/
|   `-- section_a/
|       `-- A5/
|           `-- adjustment_review/  3 review/evidence CSVs
`-- external/                   External data, when needed
```

`cleaned` holds prepared source tables. `integrated` holds joined tables, features, and derived analytical outputs. Section B currently supplies analytical results, so its CSVs belong under `integrated/section_b/`. Add `cleaned/section_b/` only if distinct cleaned inputs are actually produced for that section; reuse existing A2 tables otherwise.

Task prefixes are retained in filenames so exported files remain identifiable. Files that support multiple tasks have one canonical location; for example, the A3 sales table also contains A4 features. A1 reports and A6 documentation are linked from the Section A index rather than represented by empty data folders.

| Find | Location |
|---|---|
| Cleaned source inputs | [Section A / A2](processed/cleaned/section_a/A2/) |
| Joined analysis tables | [Section A / A3](processed/integrated/section_a/A3/) |
| Customer features | [Section A / A4](processed/integrated/section_a/A4/) |
| Adjustment review evidence | [Section A / A5](interim/section_a/A5/adjustment_review/) |
| Product and inventory outputs | [Section B / B1-B9](processed/integrated/section_b/) |
| Section A reports, scripts, and CSV index | [Section A index](../docs/section_a.md) |
| Section B reports and CSV index | [Section B index](../docs/section_b.md) |
| Original Section A filenames mapped to current paths | [Filename mapping](../docs/section_a_filenames.md) |

Both Python scripts use the new task folders. Update saved external data connections or teammates' local scripts to these paths. The original workbooks may retain old path descriptions; their contents have been preserved.
