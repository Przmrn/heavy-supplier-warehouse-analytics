# Repository Progress and Readiness Checker

**Decision document and proposed build plan**  
**Project:** Heavy Supplier, Inventory & Warehouse Analytics  
**Prepared:** 3 October 2026  
**Status:** Draft for Ammar and the team to review. Implementation is not authorized by this document.

## 1. Recommendation

Build a Python command-line checker with two layers:

1. **Local checks:** inspect files, Git state, task evidence, documentation, and data relationships. Produce repeatable results and specific suggestions without an AI API.
2. **Optional AI review:** explain the verified findings, suggest clearer documentation, and highlight possible contradictions for human review.

Start with the local checks, then add AI once the evidence and reports are reliable. Keep checking separate from editing: the first version should not repair data, rewrite notes, stage files, commit, push, or submit anything.

The goal is to answer **"What is ready, what is missing, and what should we do next?"** It cannot prove that a repository is perfect or guarantee CadetX acceptance.

### Does it need an AI API?

| Approach | What it can do | Trade-off |
|---|---|---|
| Local rules only | Detect missing files, failed checks, broken links, unsupported completion claims, and give predefined repair guidance | No model API or recurring model charge; cannot interpret arbitrary writing as flexibly |
| Local rules plus hosted AI | All local checks, plus contextual explanations and draft wording | Requires an API account, credentials, network access, usage budget, and agreement on the information sent |
| Local rules plus a local model | Adds model-generated review without sending the review packet to a hosted provider | Requires a model runtime and suitable hardware; quality and installation effort need evaluation |

**Recommended choice:** local rules first, hosted AI as an optional second phase. An agent framework, database, web application, and autonomous tool execution are unnecessary for this scope.

## 2. What the team would see

Each run should produce a short terminal summary and a detailed Markdown report. A JSON report would preserve the same evidence for comparisons and later automation.

Illustrative output only; these are not current audit results:

```text
Week: 01
Reviewed: working files at the recorded file hashes

Commit preparation: NEEDS ATTENTION
Push assessment:   UNKNOWN - remote not checked
Submission:        NEEDS ATTENTION

Reported completed tasks: 6
Completed tasks with current validation evidence: 4

1. An output is present locally but not included in the proposed commit.
2. Sprint notes say an existing file is missing.
3. A repaired candidate exists, but the declared final dataset is unchanged.

Full report: <generated report path>
AI review: not requested
```

Every finding should contain a stable check ID, severity, affected readiness verdict, exact file or task, observed evidence, expected condition, impact, suggested action, and a command or check to verify the resolution. It should also show whether it came from a deterministic check, an AI suggestion, or a human assertion.

An example suggestion should say: "The canonical ledger still fails the adjustment-sign check. A candidate exists under Data/interim/adjustment_review/. Review its change log, validate it, and explicitly adopt the intended final output." It should not say merely "Fix your data."

## 3. Three different readiness questions

### A. Ready to commit the intended changes?

Inspect the proposed commit, including its staged file contents. Check unresolved merge conflicts, staged Python syntax, malformed declared configuration, missing files required by the intended change, and likely accidental inclusion of credentials or temporary files. Secret-pattern findings require evidence redaction and human review; this is not a comprehensive security guarantee.

Unstaged edits and untracked files are normal before committing. List them and explain whether a declared deliverable would be left out. Do not demand an empty working tree as a precondition for committing.

Committing a documented work-in-progress checkpoint may be useful even when the dataset has unresolved issues. Distinguish that from a submission-ready commit; analytical defects do not automatically forbid saving progress.

### B. Ready to push the intended commits?

Inspect the branch, configured upstream, outgoing commits, and required deliverables in those commits. Distinguish "nothing new to push," "local commits awaiting push," "remote comparison unavailable," and "branch divergence needs attention."

A clean working tree does not prove that changes were pushed. Unrelated local edits do not inherently prevent pushing existing commits, but the report must explain that those edits will not be included.

Offline mode may show cached remote-tracking information, explicitly labeled as cached. An opt-in online check can obtain the current remote tip. If ancestry cannot be established from locally available objects, report UNKNOWN or use an explicitly requested fetch; fetching updates Git metadata and must be disclosed. Do not infer remote permissions, reviewer access, or an accepted push from local state alone.

### C. Ready for the selected weekly submission?

Check the selected sprint's deliverables, supporting methods, documentation consistency, applicable validations, and disclosed limitations. Check whether that same evidence is included in the committed and remotely verified version when online checking is requested.

Do not require all catalogue tasks or every future folder to be populated. Step B tasks can remain in progress during a Week 1 foundation submission.

The report should recommend readiness under the team's recorded criteria, never "CadetX approved." Portal submission remains a separate human-confirmed event unless a future authorized integration provides evidence.

### Verdict rules

| Verdict | Meaning |
|---|---|
| READY | Applicable required checks ran and passed; no unresolved review gate for this target |
| READY WITH DISCLOSED LIMITATIONS | A weekly submission is supported by evidence, and the team explicitly recorded acceptable unresolved limitations and their impact |
| NEEDS ATTENTION | A known unmet requirement or contradiction affects this target |
| UNKNOWN | Required evidence is missing, stale, unreadable, or a necessary check could not run |
| NOT APPLICABLE | This target does not apply, such as no outgoing commits to push |

Never average critical failures into a high overall score. Display all reasons; if a target has both known failures and unknown checks, show NEEDS ATTENTION and retain the unknowns. A missing AI response must not change deterministic results.

"READY WITH DISCLOSED LIMITATIONS" requires a human decision with the issue, owner, rationale, affected analyses, and review date. Do not automatically accept an issue merely because somebody wrote "known issue." Unresolved merge conflicts, detected credential exposure, or inability to inspect essential submission evidence cannot be waived as analytical limitations.

## 4. Evidence and task tracking

Keep `sprints/WEEK-01.md` as the team's readable progress record. Add a small, version-controlled JSON manifest describing stable task IDs, intended deliverables, validation rules, dependencies, and which sprint they belong to. Avoid duplicating status and ownership in two files: read those from the sprint table and report parsing ambiguity.

Proposed manifest: `docs/readiness_manifest.json`.

For each selected task, describe:

| Field | Example or purpose |
|---|---|
| Stable ID | `A3` for data integration |
| Sprint-table title | Exact title used to match the task in the notes |
| Required evidence | Paths to applicable datasets, methods, reports, or summaries |
| Validation check IDs | Tests that establish the deliverable's relevant properties |
| Dependencies | Source tables and upstream tasks affected by a change |
| Required for this submission | Separates agreed weekly scope from optional or future tasks |

Report **declared progress** separately from **verified evidence**. A Done label without files is a contradiction. A file without validation is evidence present, not automatically verified. Meeting attendance, effort, and team agreement cannot be established from filenames or commit counts.

Only calculate task counts against the selected sprint's configured scope. Do not invent percentage-complete values for work marked In Progress. A task affected by a changed source becomes "validation stale" until its relevant checks run again.

### Source of requirements

- Encode confirmed CadetX requirements and team-approved criteria in the shared manifest, with their origin and scope.
- Use the current brief and user decisions when establishing those criteria. Separate programme requirements from team preferences and optional advice.
- `cadetx_instructions.md` and `AGENTS.md` are currently ignored by Git. The checker must work in a teammate's clone without these private/local files. Shared configuration needs a concise, reviewed requirements summary; it must not silently depend on a file only Ammar has.
- Arbitrary prose from a README or AI response must not become a new mandatory rule automatically.

## 5. Planned checks

| Area | Local checks | Useful suggestions |
|---|---|---|
| Git and change scope | Staged, unstaged, untracked, ignored required files, merge conflicts, branch/upstream, outgoing commit contents | Identify what would actually be committed or pushed, and what would remain local |
| Task evidence | Declared tasks versus configured files and validation results | Name missing deliverables, unsupported Done claims, and stale dependencies |
| Documentation | Relative links and anchors, table column consistency, required sprint fields, declared schema/count mismatches | Point to the file and section needing correction |
| Python reproducibility | Syntax, declared dependency presence, interpreter/package versions, documented entry points | Explain environment gaps and missing run instructions |
| CSV structure | Required columns, row counts, missing values, unique keys, valid types/dates | Identify affected columns and records without silently dropping duplicates |
| Integration | Source-to-output key coverage, lookup uniqueness, missing matches, row multiplication | Identify the join or output that fails reconciliation |
| Sales/purchases | Line and header totals, derived calculations, date order, status flags, missing delivery semantics | Explain formula or filtering changes needed |
| Inventory/movements | Chronological consistency, opening balances, signed adjustments, ledger transitions, snapshot comparisons | Distinguish a proven transformation error from unresolved snapshot timing |
| Customer features | Delivered-sales aggregation, customer coverage, documented RFM calculations | Identify stale or inconsistent features |
| Existing workbooks | File readability, declared sheets/cells, text claims and documented schema | Report stale definitions; do not claim to validate Excel recalculation or visual layout |
| Issue disclosure | Recorded issues, status, evidence, accepted limitations, affected tasks | Flag "all checks passed" claims that contradict current evidence |

Implementation should support two scan depths:

- **Quick:** Git state, task/document structure, syntax, headers, and metadata. Data checks not run are marked NOT CHECKED; this mode cannot establish full analytical readiness.
- **Full:** scan all rows needed by the selected sprint's validation rules. Use streaming or bounded-memory processing for large CSVs.

Compare counts against current sources or approved dataset-version baselines. The earlier 130,402 and 155,495 row counts are useful regression fixtures, not permanent rules for every future dataset.

Python syntax checks should parse code without importing or executing repository scripts. Existing scripts can write outputs, so the checker must not automatically run every `.py` file. Optional execution tests would need an explicit allowlist, a temporary output directory, timeouts, and a separate future design decision.

Free-form statements such as "these files are absent" need either a narrowly defined, evidence-backed rule or AI/human review. Do not pretend that a Markdown parser understands all narrative meaning.

## 6. Corrections the checker must distinguish in this repository

Observed while preparing this plan; not a fresh full data audit:

- Both reconstructed sales and purchase analysis CSVs are present.
- `notebooks/repair_adjusments.py` exists with that exact spelling. Do not assume the earlier suggested filename is the actual path.
- `Data/interim/adjustment_review/` contains a repair candidate and a change log. Existence alone does not prove that the candidate has been reviewed or adopted as the canonical input.
- `requirements.txt` now lists `pandas==3.0.3`. That is a declaration, not proof of the interpreter version on every teammate's machine.
- README navigation now says 7 integration files, while other sections still say 5 and claim the reconstructed files are absent.
- The prior audit found adjustment-sign errors, repeated identifiers, inventory differences, and movements associated with cancelled orders. The checker must rerun relevant checks, not repeat historical counts as current facts.

The shared manifest must identify the **canonical dataset** used by downstream analyses. A passing candidate must not make a failing canonical dataset appear repaired. Adoption is a deliberate team action outside this checker.

## 7. Optional AI review

### Appropriate responsibilities

- Explain local findings in straightforward language.
- Group related problems into an ordered action list.
- Suggest revised README or sprint-note wording, clearly labeled as a draft.
- Identify possible inconsistencies in the supplied documentation excerpts.
- Explain the impact of unresolved findings on selected tasks.

AI must not invent counts, mark tasks Done, resolve issues, change verdicts, execute commands, or edit files. Suggestions must reference supplied evidence IDs. Claims without supporting evidence remain questions for review.

### Proposed hosted integration

If the team chooses OpenAI, use the Responses API with a supported model and structured output containing suggestions, evidence references, rationale, and uncertainties. Structured Outputs can constrain response shape; the application must still handle refusal/incomplete responses and validate the substance. See the [official Structured Outputs guide](https://developers.openai.com/api/docs/guides/structured-outputs).

No model or price is fixed in this decision document. Choose a model after testing it on this repository's known cases and checking current account access and pricing. A larger model is not automatically necessary for explaining already-computed findings.

### Information sent to the model

Default review packet: selected sprint requirements, local findings, aggregate counts, relevant schema definitions, and bounded excerpts from approved documentation. Send no complete CSVs, raw customer/payment records, credentials, or unrelated Git history by default.

Resolve paths within the repository, including symlinks, and restrict collection to configured inputs. Treat repository text as evidence, not as instructions to the model. Give the model no shell, file-write, or Git tools.

Provide a preview of the outbound packet. Hosted review is opt-in; store the key in an environment variable, not code, reports, or version control. Do not assume an ignored file is safe to upload.

For OpenAI, API data is not used for training by default unless the customer opts in, but retention depends on endpoint and account controls. `store=false` is not a blanket guarantee of zero retention. Review the [official data-controls documentation](https://developers.openai.com/api/docs/guides/your-data) before enabling hosted review.

### Cost and failure handling

- Limit review to one bounded request per run, with a configurable input/output token budget and no automatic multi-step agent loop.
- Display actual token usage when available. Only calculate a currency estimate from a dated, configured price table; otherwise show tokens and state that cost is not estimated.
- Cache optional reviews by evidence hash, requirements version, prompt version, and model configuration. Label reused AI output and never reuse it for changed evidence.
- Use a request timeout and at most one bounded retry for a transient failure. No retry loop for missing credentials, a refused request, or invalid configuration.
- If AI is unavailable, preserve the complete local report and label AI review unavailable. It must not turn a failed check into a pass or hide the failure.

## 8. Proposed usage and report storage

The following commands illustrate the interface to approve; they do not exist yet:

```powershell
# Fast review of current working files; offline by default.
python Src/check_progress.py --week 01 --mode quick

# Full review of current working files for the selected weekly scope.
python Src/check_progress.py --week 01 --mode full --target submission

# Review the exact proposed commit, not later unstaged edits.
python Src/check_progress.py --week 01 --mode full --target commit --snapshot staged

# Check outgoing committed work against fresh remote information.
python Src/check_progress.py --week 01 --target push --online

# Optional hosted review: preview the packet, then explicitly request it.
python Src/check_progress.py --week 01 --mode full --preview-ai
python Src/check_progress.py --week 01 --mode full --ai
```

The commit check must read the full index snapshot, including unchanged staged-version dependencies. It cannot validate an unstaged correction and claim the staged version passes. The push check uses the outgoing committed snapshot. Submission reports must state whether they describe working files, a commit, or a remotely verified commit.

Snapshot collection needs a start/end fingerprint. If files change during inspection, invalidate affected results and request a rerun; never combine inconsistent versions silently. Record commit ID, snapshot type, input content hashes, rule/manifest version, Python/dependency versions, UTC time, and local display time (Asia/Jakarta by default).

Routine output: `.readiness/runs/<unique-run-id>/report.md` and `report.json`. This directory would be ignored by Git so running the checker does not continually dirty the project. Adding the ignore rule would be an explicit implementation change, not part of this planning task.

An explicit export option could write a submission snapshot to `Reports/validation/`. It should identify the input snapshot and exclude generated reports from their own evidence fingerprint. Exporting evidence must not alter any task status automatically.

Suggested exit codes: `0` = applicable checks completed without blocking findings (warnings still printed); `1` = known blocking findings; `2` = invalid configuration, incomplete required checks, or internal error. Always retain the more detailed per-target verdict in JSON. Quick mode success means only that quick checks passed.

## 9. Proposed file layout

Create these only after design approval; avoid introducing an elaborate framework.

| Proposed file | Responsibility |
|---|---|
| `Src/check_progress.py` | Small CLI entry point |
| `Src/readiness/config.py` | Manifest validation and selected-sprint scope |
| `Src/readiness/evidence.py` | Working/index/commit snapshots, content hashes, provenance |
| `Src/readiness/checks.py` | Git, documentation, and task-evidence rules |
| `Src/readiness/data_checks.py` | Shared CSV checks and project-specific analytical validations |
| `Src/readiness/report.py` | Findings, target verdicts, terminal/Markdown/JSON rendering |
| `Src/readiness/ai_review.py` | Optional review packet, API call, response validation |
| `docs/readiness_manifest.json` | Team-approved task-to-evidence mapping and validation policy |
| `docs/readiness_checker.md` | Installation, usage, verdict explanations, and troubleshooting |
| `tests/readiness/` | Small synthetic fixtures and regression tests |

Use Python and Git already familiar to the team. Prefer standard-library CSV/JSON/AST utilities for core checks. Add a read-only workbook library only when needed for configured workbook checks, and the provider SDK only for the optional AI phase. Record dependency versions actually tested; do not assume every teammate has the same environment.

## 10. Build sequence after decisions

This is a milestone plan for choosing scope, not a code-level implementation specification. No script, API integration, hooks, or configuration will be created until the team approves the design.

| Phase | Deliverable | Acceptance gate |
|---|---|---|
| 1. Local progress report | Manifest, file/task checks, documentation checks, working-tree Git inventory, Markdown/JSON report | Names missing evidence and contradictions correctly; works offline; leaves project files unchanged except requested reports |
| 2. Analytical validation | Full CSV checks, project-specific formulas, issue linkage, source hashes | Reproduces the known defects on fixtures; corrected inputs pass; source files stay unchanged |
| 3. Commit/push/submission targets | Staged and committed snapshots, separate verdicts, optional remote verification | No false readiness from unstaged fixes, stale remote data, or missing required evidence |
| 4. Optional AI explanations | Sanitized packet, structured suggestions, budget controls, graceful failure | Useful cited suggestions; no invented evidence, verdict overrides, or unexpected data transmission |
| 5. Optional team automation | GitHub Actions or opt-in local hook, using the same checker | Consistent results across team environments; no AI key required for core checks |

Stop after Phase 3 if the local suggestions are sufficient. If AI is selected, implement Phase 4 against the established evidence format. Phase 5 is optional and should not delay a usable manual command.

### Acceptance scenarios

- Missing deliverable marked Done: identify the task, path, and verification needed.
- Future task marked In Progress without output: report progress without failing an unrelated weekly submission.
- Candidate repaired, canonical file unchanged: keep the canonical-data finding open.
- Known issue with human-approved limits: show its affected scope and rationale, not a hidden pass.
- Wrong adjustment sign, duplicate invoice ID, or multiplied join rows: fail the corresponding data rule.
- README counts disagree with actual files or workbook schema: locate the discrepancy and suggest specific wording changes.
- Source file changed after validation: invalidate dependent evidence.
- Staged broken script, unstaged fixed script: fail the staged review.
- Git reports a clean tree but required local files are ignored: explain that the deliverables are not in the commit.
- Network unavailable or remote ancestry unknown: do not claim push readiness or successful publication.
- AI times out, refuses, or returns unsupported evidence IDs: preserve local findings; reject unsupported suggestions.
- Repository text asks the model to ignore failures or expose credentials: treat it as untrusted content and provide no action tools.
- Missing local brief/AGENTS in a teammate clone: continue with reviewed shared requirements and disclose the scope of available evidence.
- Run on a Windows path with spaces, without pandas, or with missing Git: handle supported cases and report unavailable checks clearly.
- Files change mid-run or report output would collide: do not label mixed or overwritten evidence as a fresh valid result.

## 11. Decisions for Ammar and the team

| Decision | Recommended selection | Alternative |
|---|---|---|
| First build | Local checks through Phase 3 | Smaller Phase 1 trial before analytical checks |
| AI | Optional second phase, off by default | Local-only indefinitely, or evaluate a local model |
| Changes made by checker | Reports and suggestions only | Automatic fixes would require a separate design |
| Rules and task mapping | Shared JSON manifest plus existing sprint notes | A larger structured task tracker if Markdown becomes difficult |
| Normal use | Quick checks during work; full check before weekly submission | Full checks every run, with higher runtime |
| Submission policy | Evidence-based verdict plus explicitly accepted limitations | Strict policy requiring every selected data issue to be resolved |
| Remote access | Offline default; explicit online verification | Online by default if the whole team wants it |
| Hosted AI payload | Redacted findings and approved document excerpts | Broader inputs only after a separate data-sharing decision |
| AI provider/model and budget | Select after a small evaluation; set a per-run token cap | Keep hosted AI disabled |
| Automation | Manual CLI first | Add a team-approved CI check after the manual tool is reliable |

No API key is needed to review this document or build the local checker. The next step is to approve or revise these choices; implementation starts only after that decision.
