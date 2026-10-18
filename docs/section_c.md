# Section C: Warehouse Operations & Efficiency

The 14 files supplied in `section_c/section_c/` were organized on 16 October 2026. This index links the four task workbooks, 9 CSV outputs, and the section completion summary.

## Locations and preservation

| Original files | Current location |
|---|---|
| `section_c/section_c/*.csv` (9 files) | `Data/processed/integrated/section_c/C1/` through `C7/` |
| `section_c/section_c/C1_*.xlsx`, `C2_C3_*.xlsx`, `C4_C5_*.xlsx`, `C6_C7_*.xlsx` (4 files) | `Reports/warehouse_operations/` |
| `section_c/section_c/C_Section_C_Completion_Summary.xlsx` | `Reports/validation/` |

All original filenames and file contents were preserved; before-and-after SHA-256 comparisons matched for all 14 files. The five workbooks opened with no external links found. Embedded text may still refer to the original folder; use the mapping above.

## Task reports

| Task | Analysis | Workbook |
|---|---|---|
| C1 | Warehouse Space Utilisation Analysis | [C1_Warehouse_Space_Utilisation.xlsx](../Reports/warehouse_operations/C1_Warehouse_Space_Utilisation.xlsx) |
| C2 | Warehouse Throughput Analysis | [C2_C3_Throughput_and_Capacity.xlsx](../Reports/warehouse_operations/C2_C3_Throughput_and_Capacity.xlsx) |
| C3 | Warehouse Capacity Analysis | [C2_C3_Throughput_and_Capacity.xlsx](../Reports/warehouse_operations/C2_C3_Throughput_and_Capacity.xlsx) |
| C4 | Product–Warehouse Alignment | [C4_C5_Alignment_and_Performance.xlsx](../Reports/warehouse_operations/C4_C5_Alignment_and_Performance.xlsx) |
| C5 | Warehouse Performance Scoring | [C4_C5_Alignment_and_Performance.xlsx](../Reports/warehouse_operations/C4_C5_Alignment_and_Performance.xlsx) |
| C6 | Operational Bottleneck Detection | [C6_C7_Bottlenecks_and_Benchmarking.xlsx](../Reports/warehouse_operations/C6_C7_Bottlenecks_and_Benchmarking.xlsx) |
| C7 | Warehouse Utilisation Benchmarking | [C6_C7_Bottlenecks_and_Benchmarking.xlsx](../Reports/warehouse_operations/C6_C7_Bottlenecks_and_Benchmarking.xlsx) |

[Section C completion summary](../Reports/validation/C_Section_C_Completion_Summary.xlsx)

The C2/C3, C4/C5, and C6/C7 workbooks each cover two tasks; their canonical locations above are shared. The 9 CSVs were grouped into C1-C7 task folders under `Data/processed/integrated/section_c/`. These are derived analytical outputs; cleaned source tables remain shared Section A inputs. See the [Data directory guide](../Data/README.md).

## CSV outputs

Dimensions below were read from the supplied CSV files; row counts exclude the header.

| Task | File | Rows | Columns |
|---|---|---:|---:|
| C1 | [C1_warehouse_space_utilisation.csv](../Data/processed/integrated/section_c/C1/C1_warehouse_space_utilisation.csv) | 6 | 28 |
| C2 | [C2_warehouse_throughput.csv](../Data/processed/integrated/section_c/C2/C2_warehouse_throughput.csv) | 6 | 26 |
| C3 | [C3_warehouse_capacity.csv](../Data/processed/integrated/section_c/C3/C3_warehouse_capacity.csv) | 6 | 36 |
| C4 | [C4_abc_mix_by_branch.csv](../Data/processed/integrated/section_c/C4/C4_abc_mix_by_branch.csv) | 18 | 9 |
| C4 | [C4_top_products_by_branch.csv](../Data/processed/integrated/section_c/C4/C4_top_products_by_branch.csv) | 18 | 8 |
| C5 | [C5_warehouse_performance_scores.csv](../Data/processed/integrated/section_c/C5/C5_warehouse_performance_scores.csv) | 6 | 32 |
| C6 | [C6_bottleneck_detection.csv](../Data/processed/integrated/section_c/C6/C6_bottleneck_detection.csv) | 6 | 28 |
| C7 | [C7_network_benchmarks.csv](../Data/processed/integrated/section_c/C7/C7_network_benchmarks.csv) | 7 | 5 |
| C7 | [C7_utilisation_benchmarking.csv](../Data/processed/integrated/section_c/C7/C7_utilisation_benchmarking.csv) | 6 | 28 |

Branch-level tables cover 6 branches; the C4 tables cover 18 branch-level rows each.

## Review status

Files have been organized and inventoried; their analytical calculations, input versions, and business conclusions have not been independently validated in this organization task. The supplied completion summary is a team artifact, not proof of independent review. Existing task owners and statuses in the [Week 2 sprint notes](../sprints/WEEK-02.md) are preserved.

Before relying on the results, check their methods and source versions against the current integrated data, including the adopted adjustment repair and documented unresolved data-quality issues. These files are analysis outputs, not original source data. No Section C generation scripts were included in the supplied folder; add the actual working code or queries when available.
