# Section E: Customer Analytics

The 28 files supplied for Section E were organized on 29 October 2026: 21 CSV outputs, six task workbooks, and the Section E completion summary. Original filenames and contents were preserved; pre-move and post-move SHA-256 hashes matched for all files.

## Locations

| Deliverable | Current location |
|---|---|
| Task CSV outputs (21 files) | `Data/processed/integrated/section_e/E1/` through `E9/` |
| Six task workbooks | `Reports/customer_analytics/` |
| Section E completion summary | `Reports/validation/E_Section_E_Completion_Summary.xlsx` |

These are derived analysis outputs. Existing Section A customer features and sales analysis remain shared inputs; Section E does not introduce a second cleaned-source set.

## Task reports

| Task | Analysis | Workbook |
|---|---|---|
| E1 | Customer Purchase Behaviour Analysis | [E1_Customer_Purchase_Behaviour.xlsx](../Reports/customer_analytics/E1_Customer_Purchase_Behaviour.xlsx) |
| E2 | RFM Analysis | [E2_RFM_Analysis.xlsx](../Reports/customer_analytics/E2_RFM_Analysis.xlsx) |
| E3 | Customer Segmentation and Personas | [E3_Segmentation_Personas.xlsx](../Reports/customer_analytics/E3_Segmentation_Personas.xlsx) |
| E4 | Customer Lifetime Value Estimation | [E4_Customer_Lifetime_Value.xlsx](../Reports/customer_analytics/E4_Customer_Lifetime_Value.xlsx) |
| E5 | Customer Retention Analysis | [E5_E6_Retention_and_Churn.xlsx](../Reports/customer_analytics/E5_E6_Retention_and_Churn.xlsx) |
| E6 | Customer Churn Analysis | [E5_E6_Retention_and_Churn.xlsx](../Reports/customer_analytics/E5_E6_Retention_and_Churn.xlsx) |
| E7 | Customer Cohort Analysis | [E7_E8_E9_Cohorts_HighValue_AtRisk.xlsx](../Reports/customer_analytics/E7_E8_E9_Cohorts_HighValue_AtRisk.xlsx) |
| E8 | High-Value Customer Identification | [E7_E8_E9_Cohorts_HighValue_AtRisk.xlsx](../Reports/customer_analytics/E7_E8_E9_Cohorts_HighValue_AtRisk.xlsx) |
| E9 | At-Risk Customer Identification | [E7_E8_E9_Cohorts_HighValue_AtRisk.xlsx](../Reports/customer_analytics/E7_E8_E9_Cohorts_HighValue_AtRisk.xlsx) |

[E Section completion summary](../Reports/validation/E_Section_E_Completion_Summary.xlsx)

The E5/E6 workbook and E7/E8/E9 workbook each cover multiple tasks. The shared `E5_E6_retention_churn_detail.csv` is stored once under E5 as its canonical location and supports both E5 and E6.

## CSV outputs

Dimensions were read from the current CSVs; row counts exclude the header.

| Task | File | Rows | Columns |
|---|---|---:|---:|
| E1 | [E1_behaviour_by_industry.csv](../Data/processed/integrated/section_e/E1/E1_behaviour_by_industry.csv) | 6 | 6 |
| E1 | [E1_behaviour_by_region.csv](../Data/processed/integrated/section_e/E1/E1_behaviour_by_region.csv) | 6 | 7 |
| E1 | [E1_behaviour_by_type.csv](../Data/processed/integrated/section_e/E1/E1_behaviour_by_type.csv) | 5 | 9 |
| E1 | [E1_customer_behaviour_detail.csv](../Data/processed/integrated/section_e/E1/E1_customer_behaviour_detail.csv) | 500 | 20 |
| E2 | [E2_rfm_customer_detail.csv](../Data/processed/integrated/section_e/E2/E2_rfm_customer_detail.csv) | 500 | 16 |
| E2 | [E2_rfm_segment_profiles.csv](../Data/processed/integrated/section_e/E2/E2_rfm_segment_profiles.csv) | 5 | 14 |
| E3 | [E3_personas.csv](../Data/processed/integrated/section_e/E3/E3_personas.csv) | 5 | 18 |
| E3 | [E3_segment_stats.csv](../Data/processed/integrated/section_e/E3/E3_segment_stats.csv) | 5 | 14 |
| E4 | [E4_clv_by_band.csv](../Data/processed/integrated/section_e/E4/E4_clv_by_band.csv) | 5 | 9 |
| E4 | [E4_clv_by_segment.csv](../Data/processed/integrated/section_e/E4/E4_clv_by_segment.csv) | 5 | 8 |
| E4 | [E4_customer_clv.csv](../Data/processed/integrated/section_e/E4/E4_customer_clv.csv) | 500 | 24 |
| E5 | [E5_E6_retention_churn_detail.csv](../Data/processed/integrated/section_e/E5/E5_E6_retention_churn_detail.csv) | 500 | 21 |
| E5 | [E5_retention_status_summary.csv](../Data/processed/integrated/section_e/E5/E5_retention_status_summary.csv) | 4 | 7 |
| E5 | [E5_yoy_retention.csv](../Data/processed/integrated/section_e/E5/E5_yoy_retention.csv) | 5 | 5 |
| E6 | [E6_at_risk_customers.csv](../Data/processed/integrated/section_e/E6/E6_at_risk_customers.csv) | 110 | 17 |
| E6 | [E6_churned_customers.csv](../Data/processed/integrated/section_e/E6/E6_churned_customers.csv) | 5 | 17 |
| E7 | [E7_cohort_retention_matrix.csv](../Data/processed/integrated/section_e/E7/E7_cohort_retention_matrix.csv) | 1 | 14 |
| E7 | [E7_cohort_revenue.csv](../Data/processed/integrated/section_e/E7/E7_cohort_revenue.csv) | 1 | 7 |
| E8 | [E8_high_value_customers.csv](../Data/processed/integrated/section_e/E8/E8_high_value_customers.csv) | 223 | 17 |
| E9 | [E9_at_risk_customers.csv](../Data/processed/integrated/section_e/E9/E9_at_risk_customers.csv) | 174 | 22 |
| E9 | [E9_priority_at_risk.csv](../Data/processed/integrated/section_e/E9/E9_priority_at_risk.csv) | 46 | 22 |

## Results reported by the supplied summary

The current outputs cover 500 distinct customer IDs and total delivered-sales revenue of 22,958,987,430 in the E1 detail table. The E5 yearly table reports retention between 99.6% and 100% for 2019-2023. E6 lists five churned customers; E8 lists 223 high-value customers; E9 lists 46 priority at-risk customers, all flagged high-value; and the highest CLV quintile contributes 59.2% of predicted CLV.

These figures describe the supplied outputs and team completion summary; they are not independent validation of the formulas or assumptions.

## Review status and limitations

The six task workbooks and the completion summary are readable XLSX archives. They contain written methods/formula sheets but no executable spreadsheet formula cells. No Section E generation script was supplied, so the CSV outputs cannot be regenerated from this package alone.

The E6 at-risk list contains 110 rows, while the E9 at-risk list contains 174. Their definitions and thresholds have not been reconciled in this organization pass. Confirm those definitions, the CLV prediction assumptions, cohort construction, input versions, and the reported retention/churn rules before using the results for decisions. The completion summary is a team artifact, not proof of independent analytical review.
