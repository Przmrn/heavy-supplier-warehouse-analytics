# Section D: Supplier & Procurement Analytics

The 12 files supplied in `section_d/section_d/` were organized on 16 October 2026. This index links the three task workbooks, 8 CSV outputs, and the section completion summary.

## Locations and preservation

| Original files | Current location |
|---|---|
| `section_d/section_d/*.csv` (8 files) | `Data/processed/integrated/section_d/D1/` through `D6/` |
| `section_d/section_d/D1_*.xlsx`, `D2_D3_D4_*.xlsx`, `D5_D6_*.xlsx` (3 files) | `Reports/supplier_procurement/` |
| `section_d/section_d/D_Section_D_Completion_Summary.xlsx` | `Reports/validation/` |

All original filenames and file contents were preserved; before-and-after SHA-256 comparisons matched for all 12 files. The four workbooks opened with no external links found. Embedded text may still refer to the original folder; use the mapping above.

## Task reports

| Task | Analysis | Workbook |
|---|---|---|
| D1 | Supplier Contribution Analysis | [D1_Supplier_Contribution.xlsx](../Reports/supplier_procurement/D1_Supplier_Contribution.xlsx) |
| D2 | Supplier Reliability Analysis | [D2_D3_D4_Reliability_Performance_Dependency.xlsx](../Reports/supplier_procurement/D2_D3_D4_Reliability_Performance_Dependency.xlsx) |
| D3 | Supplier Performance Comparison | [D2_D3_D4_Reliability_Performance_Dependency.xlsx](../Reports/supplier_procurement/D2_D3_D4_Reliability_Performance_Dependency.xlsx) |
| D4 | Supplier Dependency Risk Analysis | [D2_D3_D4_Reliability_Performance_Dependency.xlsx](../Reports/supplier_procurement/D2_D3_D4_Reliability_Performance_Dependency.xlsx) |
| D5 | Critical Supplier Identification | [D5_D6_Critical_and_Diversification.xlsx](../Reports/supplier_procurement/D5_D6_Critical_and_Diversification.xlsx) |
| D6 | Supplier Diversification Analysis | [D5_D6_Critical_and_Diversification.xlsx](../Reports/supplier_procurement/D5_D6_Critical_and_Diversification.xlsx) |

[Section D completion summary](../Reports/validation/D_Section_D_Completion_Summary.xlsx)

The D2/D3/D4 and D5/D6 workbooks each cover multiple tasks; their canonical locations above are shared. The 8 CSVs were grouped into D1-D6 task folders under `Data/processed/integrated/section_d/`. These are derived analytical outputs; cleaned source tables remain shared Section A inputs. See the [Data directory guide](../Data/README.md).

## CSV outputs

Dimensions below were read from the supplied CSV files; row counts exclude the header.

| Task | File | Rows | Columns |
|---|---|---:|---:|
| D1 | [D1_supplier_contribution.csv](../Data/processed/integrated/section_d/D1/D1_supplier_contribution.csv) | 8 | 26 |
| D1 | [D1_contribution_by_type.csv](../Data/processed/integrated/section_d/D1/D1_contribution_by_type.csv) | 3 | 6 |
| D2 | [D2_supplier_reliability.csv](../Data/processed/integrated/section_d/D2/D2_supplier_reliability.csv) | 8 | 20 |
| D3 | [D3_supplier_performance.csv](../Data/processed/integrated/section_d/D3/D3_supplier_performance.csv) | 8 | 28 |
| D4 | [D4_dependency_summary.csv](../Data/processed/integrated/section_d/D4/D4_dependency_summary.csv) | 1 | 8 |
| D5 | [D5_critical_suppliers.csv](../Data/processed/integrated/section_d/D5/D5_critical_suppliers.csv) | 8 | 35 |
| D6 | [D6_suppliers_per_product.csv](../Data/processed/integrated/section_d/D6/D6_suppliers_per_product.csv) | 30 | 4 |
| D6 | [D6_diversification_summary.csv](../Data/processed/integrated/section_d/D6/D6_diversification_summary.csv) | 1 | 9 |

Supplier-level tables cover 8 suppliers; the D6 per-product table covers 30 products.

## Review status

Files have been organized and inventoried; their analytical calculations, input versions, and business conclusions have not been independently validated in this organization task. The supplied completion summary is a team artifact, not proof of independent review. The Week 3 sprint draft lists proposed owners and marks statuses for confirmation; these are not confirmed team assignments or completion claims.

Before relying on the results, check their methods and source versions against the current integrated data, including the adopted adjustment repair and documented unresolved data-quality issues. These files are analysis outputs, not original source data. No Section D generation scripts were included in the supplied folder; add the actual working code or queries when available.
