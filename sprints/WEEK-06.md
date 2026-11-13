# Week 6 Sprint Notes

## Dates

Not recorded in the available project files. Add the actual sprint dates when the team confirms them.

## Scrum Master

Golla Bhumika

## Sprint Goal

Organize and document the supplied Section G risk, anomaly, and control outputs; record material findings and review limits; and prepare the Week 6 package for the team's GitHub submission.

## Activities

| Activity | Owner | Status |
|---|---|---|
| Organize supplied Section G CSVs and workbooks | Repository update in this session | Done; files moved and destination outputs checked |
| Add the Section G file index and update repository navigation | Repository update in this session | Done |
| Record supplied G1-G4 deliverables and review limits | Repository update in this session | Done |

## Section G Tasks

The supplied package contains deliverables for G1-G4. Task owners below are recorded in the team sprint notes. “Done” means the supplied deliverable is present; independent analytical validation remains pending.

| Code | Task | Owner | Status | Evidence |
|---|---|---|---|---|
| G1 | Inventory Movement Anomaly Detection | Ammar | Done | [G1 workbook](../Reports/risk_control/G1_Movement_Anomaly_Detection.xlsx) |
| G2 | Stock Shrinkage Detection | Festus | Done | [G2 workbook](../Reports/risk_control/G2_Stock_Shrinkage_Detection.xlsx) |
| G3 | Operational Risk Monitoring | Nadir | Done | [G3 workbook](../Reports/risk_control/G3_Operational_Risk_Monitoring.xlsx) |
| G4 | Data Integrity & Error Detection | Golla | Done | [G4 workbook](../Reports/risk_control/G4_Data_Integrity_Error_Detection.xlsx) |

## Meeting Notes and Decisions

No Week 6 meeting date, attendees, decisions, or minutes are recorded in the available project files.

## Results and Review Limits

- The supplied anomaly output lists 18 notable adjustment movements from 237,230 ledger movements and no extreme anomalies.
- The reconciliation output flags all 180 product-branch positions for both a balance gap and a sales-versus-ledger-out mismatch. Its CSV totals are -69,656 and +110,107 units respectively.
- The risk-register CSV has 3 High, 8 Medium, and 4 Low risks. The completion summary instead says 9 Medium; reconcile this difference before reporting the totals.
- The integrity-check CSV has 28 rows: 2 High findings and 26 OK results.
- These facts were checked against the supplied CSV exports. The source data, calculations, and control conclusions remain unvalidated. See the [Section G index](../docs/section_g.md).

## Blockers and Next Steps

- Reconcile the G3 severity-count discrepancy between the completion summary and risk-register CSV.
- Establish snapshot timing, adjustment direction, movement order, units, and sales eligibility before interpreting G2 gaps as shrinkage.
- Review the G1 anomaly method and investigate flagged adjustment movements with operational context.
- Record the actual Week 6 dates and meeting decisions if available from the team.
- Stage and commit the Week 6 package, push it to GitHub, verify the remote, and submit the repository link separately in the CadetX portal. Submission is not confirmed here.

## Submission Checklist

| Item | Status |
|---|---|
| Section G CSVs, workbooks, completion summary, and file index | Ready in the working tree |
| Sprint goal, Scrum Master, task owners, task evidence, results, and review limits | Recorded in this note |
| G3 Medium-risk-count discrepancy | Disclosed; follow-up remains open |
| Week 6 dates and meeting details | Not recorded in available files |
| Commit created | Done |
| Changes pushed to GitHub | Done |
| Repository link submitted in the CadetX portal | Done |
