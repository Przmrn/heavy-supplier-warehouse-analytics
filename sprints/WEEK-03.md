# Week 3 Sprint Notes
  
## Scrum Master
Golla Bhumika

## Sprint Goal (Draft)
Confirm the organized Section C and Section D outputs (owners, review, and validation) and agree the next analysis scope.

## Activities

These task owners and statuses are draft entries pending team confirmation.

| Task | Owner | Status |
|------|-------|--------|
| Prepare the Week 3 sprint notes | Golla | Done |
| Commit and push the Section C/D organization | Ammar | Done |

## Step C Tasks

The Week 2 notes record C1-C7 as In Progress. The current Week 3 table leaves their statuses unconfirmed; the Section C files are now organized, but file presence does not confirm analytical completion. The owner names below are draft allocations; C2 also has a different proposed owner than in Week 2. Confirm owners and statuses with the team before marking tasks complete. Shared workbooks cover two tasks each.

| Code | Task | Owner | Status | Report or reference |
|---|---|---|---|---|
| C1 | Warehouse Space Utilisation Analysis | Ammar | Done | [C1 report](../Reports/warehouse_operations/C1_Warehouse_Space_Utilisation.xlsx) |
| C2 | Warehouse Throughput Analysis | Nadir | Done | [C2/C3 report](../Reports/warehouse_operations/C2_C3_Throughput_and_Capacity.xlsx) |
| C3 | Warehouse Capacity Analysis | Nadir | Done | [C2/C3 report](../Reports/warehouse_operations/C2_C3_Throughput_and_Capacity.xlsx) |
| C4 | Product–Warehouse Alignment | Golla | Done | [C4/C5 report](../Reports/warehouse_operations/C4_C5_Alignment_and_Performance.xlsx) |
| C5 | Warehouse Performance Scoring | Festus | Done | [C4/C5 report](../Reports/warehouse_operations/C4_C5_Alignment_and_Performance.xlsx) |
| C6 | Operational Bottleneck Detection | Golla | Done | [C6/C7 report](../Reports/warehouse_operations/C6_C7_Bottlenecks_and_Benchmarking.xlsx) |
| C7 | Warehouse Utilisation Benchmarking | Festus | Done | [C6/C7 report](../Reports/warehouse_operations/C6_C7_Bottlenecks_and_Benchmarking.xlsx) |

## Step D Tasks

Files were organized on 16 October 2026 (see [Section D file index](../docs/section_d.md)). The owner names below are draft allocations from this note and remain unconfirmed. Task statuses are also unconfirmed and are not completion claims.

| Code | Task | Proposed owner (unconfirmed) | Status (confirm) | Report or reference |
|---|---|---|---|---|
| D1 | Supplier Contribution Analysis | Nadir | Done | [D1 report](../Reports/supplier_procurement/D1_Supplier_Contribution.xlsx) |
| D2 | Supplier Reliability Analysis | Nadir | Done | [D2/D3/D4 report](../Reports/supplier_procurement/D2_D3_D4_Reliability_Performance_Dependency.xlsx) |
| D3 | Supplier Performance Comparison | Festus | Done | [D2/D3/D4 report](../Reports/supplier_procurement/D2_D3_D4_Reliability_Performance_Dependency.xlsx) |
| D4 | Supplier Dependency Risk Analysis | Festus | Done | [D2/D3/D4 report](../Reports/supplier_procurement/D2_D3_D4_Reliability_Performance_Dependency.xlsx) |
| D5 | Critical Supplier Identification | Golla | Done | [D5/D6 report](../Reports/supplier_procurement/D5_D6_Critical_and_Diversification.xlsx) |
| D6 | Supplier Diversification Analysis | Ammar | Done | [D5/D6 report](../Reports/supplier_procurement/D5_D6_Critical_and_Diversification.xlsx) |

## Meeting Notes
TBC - record planning meeting attendees and agreed goal, owners, and statuses.

## Completed Work
  1. Step C files organized on 16 October 2026: [file index](../docs/section_c.md) - 9 CSVs in `Data/processed/integrated/section_c/C1/` through `C7/`, four workbooks in `Reports/warehouse_operations/`, completion summary in `Reports/validation/`. Contents hash-verified; analytical review remains open.
  2. Step D files organized on 16 October 2026: [file index](../docs/section_d.md) - 8 CSVs in `Data/processed/integrated/section_d/D1/` through `D6/`, three workbooks in `Reports/supplier_procurement/`, completion summary in `Reports/validation/`. Contents hash-verified; analytical review remains open.

## Blockers
- Repeated invoice IDs: 196 groups contain conflicting records.
- Repeated payment IDs: 201 groups contain conflicting records.
- Inventory reconciliation: 14 product–branch positions differ from
  their final ledger balances; snapshot timing needs clarification.
- Cancelled-order movements: 1,275 outbound and 1,542 inbound movements
  reference orders currently marked cancelled; their treatment needs
  investigation.
- Section C/D calculations, input versions, and conclusions not yet validated.
- Section C and D owners and completion statuses need team confirmation.

## Next Steps
- Confirm the Week 3 Scrum Master and the Section C/D owners and statuses.
- Validate Section C/D methods against current integrated data; record input versions and assumptions.
- Agree the next tasks and KPI formulas before producing new results.
- Commit, push, verify on GitHub, then submit the portal link and record the date.
