# Section G: Risk, Anomaly & Control Analytics

The supplied Section G package covers inventory-movement anomaly detection, stock-shrinkage reconciliation, operational-risk monitoring, and data-integrity checks. It contains derived CSV outputs, static analysis workbooks, and a completion summary; the supplied files do not establish independently validated control results.

The original package contained 11 files. On 13 November 2026, all six CSVs were moved to `Data/processed/integrated/section_g/`, the four task workbooks to `Reports/risk_control/`, and the completion summary to `Reports/validation/`. The target files were checked for presence, CSV dimensions, and readable workbook ZIP archives. A before-and-after hash comparison could not run because the available shell did not provide `Get-FileHash`.

## Deliverables

| Task | CSV outputs | Dimensions | Workbook / evidence |
|---|---|---|---|
| G1 Inventory Movement Anomaly Detection | [Movement anomalies](../Data/processed/integrated/section_g/G1/G1_movement_anomalies.csv); [by branch](../Data/processed/integrated/section_g/G1/G1_anomaly_by_branch.csv); [by product](../Data/processed/integrated/section_g/G1/G1_anomaly_by_product.csv) | 18 × 20; 6 × 5; 30 × 6 | [G1 workbook](../Reports/risk_control/G1_Movement_Anomaly_Detection.xlsx) |
| G2 Stock Shrinkage Detection | [Shrinkage reconciliation](../Data/processed/integrated/section_g/G2/G2_shrinkage_reconciliation.csv) | 180 × 23 | [G2 workbook](../Reports/risk_control/G2_Stock_Shrinkage_Detection.xlsx) |
| G3 Operational Risk Monitoring | [Operational risk register](../Data/processed/integrated/section_g/G3/G3_operational_risk_register.csv) | 15 × 9 | [G3 workbook](../Reports/risk_control/G3_Operational_Risk_Monitoring.xlsx) |
| G4 Data Integrity & Error Detection | [Data-integrity checks](../Data/processed/integrated/section_g/G4/G4_data_integrity_checks.csv) | 28 × 7 | [G4 workbook](../Reports/risk_control/G4_Data_Integrity_Error_Detection.xlsx) |

The [Section G completion summary](../Reports/validation/G_Section_G_Completion_Summary.xlsx) is stored with other completion evidence.

## Results recorded in the supplied package

- G1 reports 18 notable anomalies from 237,230 movements. All 18 are stock-adjustment records; no rows are marked Extreme.
- G2 reports nonzero balance gaps and sales-versus-ledger-out mismatches for all 180 product-branch positions. CSV totals are -69,656 balance-gap units, +110,107 sales-versus-ledger-out units, and +66,990 net signed adjustment units.
- G3's risk-register CSV contains 15 records: 3 High, 8 Medium, and 4 Low.
- G4 contains 28 checks: 2 High findings and 26 OK results.

The CSV calculations above are independent counts and sums of the supplied exports. They do not validate the source data, formulas, or the business interpretation.

## Review limits and follow-up

- The G3 workbook overview agrees with the risk-register CSV at 8 Medium risks. The completion summary instead reports 9 Medium risks; reconcile this discrepancy before using the summary or reporting the register's severity totals.
- G2 identifies reconciliation differences. It does not establish that inventory was lost or stolen: confirm the inventory snapshot date, movement order, adjustment signs and directions, sales eligibility, and units before treating any gap as shrinkage.
- G1 uses statistical movement-size flags. The workbook itself describes anomalies as candidates for review, rather than proof of error or fraud.
- No Section G generation scripts, input-version record, or independent control-test evidence was supplied. Review the Section A adjustment repair and outstanding inventory/ledger issues before relying on these outputs.
- The workbooks are readable archives. They contain no executable formulas except for one cell in the G2 workbook, so they cannot reproduce the analyses from this repository alone.

See [Week 6 sprint notes](../sprints/WEEK-06.md) for the repository work and documentation status.
