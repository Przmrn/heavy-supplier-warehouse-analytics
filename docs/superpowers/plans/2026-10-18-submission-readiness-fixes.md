# Repository Submission Readiness Fix Plan

> **For agentic workers:** Use this plan task by task. Check off each step only after its verification succeeds.

**Goal:** Make the current Week 3 repository update internally consistent, navigable on GitHub, and honest about what can be reproduced and what remains under review.

**Architecture:** Keep the already committed Week 2 snapshot intact. Make focused updates to the current README, task index, and sprint notes, using existing CSVs and workbooks as evidence. Preserve team names, owners, dates, and completion claims only when the repository or Ammar confirms them; otherwise label them unconfirmed.

**Tech Stack:** Markdown; Git path metadata; Python standard library for read-only CSV and workbook-archive checks.

**Spec:** `cadetx_instructions.md`, repository `AGENTS.md`, and the read-only submission audit from 18 October 2026.

## Global Constraints

- CadetX requires weekly work and Scrum Master sprint notes on GitHub, with the repository link separately submitted in the portal.
- The task catalogue and 12-week roadmap are flexible; do not create new programme requirements.
- Preserve original data and existing team work; do not overwrite analysis outputs.
- Do not invent meeting dates, attendance, task owners, role approvals, or completion status.
- Keep Week 2 history intact; it is already present in commit `f786091`.
- Keep unresolved Section A quality issues and Section B/C/D review limitations visible.
- Do not commit, push, or submit during this fix pass.

## Review Focus

- GitHub uses the exact tracked path casing even though Windows links may resolve with different casing.
- Week 3 task tables must agree with their draft and confirmation notes.
- Week 2 is a historical snapshot; later task changes belong in Week 3.
- Workbook method sheets describe formulas, but the reviewed workbooks contain no executable formula cells and the B/C/D generation scripts are absent.
- README results must continue to match the current indexed CSV outputs and must not imply independent validation where none occurred.

---

### Task 1: Repair repository navigation and file references

**Files:**
- Modify: `docs/section_a.md`
- Check: `README.md`, `Data/README.md`, `docs/README.md`, `docs/section_a_filenames.md`, `docs/section_b.md`, `docs/section_c.md`, and `docs/section_d.md`

- [x] Change all four Section A script-link targets from `../notebooks/...` to the tracked `../Notebooks/...` paths.
- [x] Check every relative Markdown link against the current worktree and compare links to tracked Git paths with case sensitivity enabled.
- [x] Confirm section indexes still point to the current A2-A5 and B1-D6 task folders.

**Acceptance:** No missing Markdown targets; no Git path case mismatches; Section A script links resolve to `Notebooks/build.analysis_tables.py` and `Notebooks/repair_adjusments.py`.

### Task 2: Reconcile sprint records without guessing team decisions

**Files:**
- Modify: `sprints/WEEK-02.md`
- Modify: `sprints/WEEK-03.md`
- Check: `sprints/WEEK-01.md`

- [x] Preserve Week 2's recorded B1-B9 Done and C1-C7 In Progress snapshot.
- [ ] Confirm with the team whether the Week 2 activity row `Prepare the Week 2 sprint notes - In Progress` is a historical snapshot or should be corrected; it was preserved because the repository does not establish a different status.
- [x] In Week 3, correct the statement that C statuses were “preserved” from Week 2: the Week 2 C statuses are In Progress, and the Week 3 table lists Done. Also flag the changed C2 owner for confirmation.
- [x] Reconcile the Week 3 Section D table: it lists named owners and Done statuses while the surrounding text says owners/statuses are not recorded. Until confirmed, label the current assignments and statuses as draft/unconfirmed or replace them with `TBC`.
- [x] Keep the Week 3 meeting and Scrum Master marked unconfirmed until the team confirms them.
- [x] Replace the Week 1 `[actual date]` placeholder with a date supported by existing evidence; if no date can be established, state that it was not recorded.
- [ ] Add sprint date ranges only if the team can confirm them; the brief does not prescribe a date template.

**Acceptance:** Each sprint file distinguishes its own time period, confirmed facts, proposed allocations, and unresolved details. No status is inferred from the mere presence of an output file.

### Task 3: Clarify the team roster in the README

**Files:**
- Modify: `README.md`

- [x] Keep all four currently recorded names and their recorded technical roles.
- [x] Add a short note that the repository roster lists four people (three Data Analysts and one BI Analyst), while the CadetX brief describes a three-person team (two Data Analysts and one Data Scientist).
- [x] Do not remove or relabel a member or imply that CadetX approved an exception.

**Acceptance:** A reviewer can see the documented discrepancy without guessing which record is authoritative.

### Task 4: State the reproducibility boundary clearly

**Files:**
- Modify: `README.md`
- Check: `requirements.txt`, `Notebooks/build.analysis_tables.py`, `Notebooks/repair_adjusments.py`, and `docs/section_b.md`, `docs/section_c.md`, `docs/section_d.md`

- [x] Add the exact Section A entry commands with tracked `Notebooks/` capitalization; document that existing output targets are populated and the overwrite guard prevents rerunning in this checkout.
- [x] Point to `requirements.txt`; do not claim the pinned pandas environment was tested unless it is actually installed and run.
- [x] State that B/C/D workbooks include written method/formula descriptions and static results, while generation scripts and executable workbook formulas are not present.
- [x] Keep the existing analytical limitations and review-status language visible; do not relabel organization or file checks as calculation validation.

**Acceptance:** A reviewer can distinguish what can be rerun from the repository, what can only be inspected, and which findings remain team-reported.

### Task 5: Recheck the submission snapshot

**Files:** No new test framework or data edits.

- [x] Confirm the Week 2 note remains tracked in history and its recorded status snapshot was not rewritten.
- [x] Recheck all Markdown links using Git-tracked path casing.
- [x] Recheck every CSV row/column count listed in the A-D indexes against the current file.
- [x] Confirm all referenced workbooks are readable ZIP archives and all intended current additions are visible in `git status`.
- [x] Run `git diff --check` and inspect the final diff for changes outside the files listed above.
- [x] Report separately that remote GitHub state and portal submission are unverified unless directly checked.

**Acceptance:** The final review gives a clear Week 3 progress-submission verdict, records remaining analysis limitations, and identifies the exact worktree contents for Ammar to commit.
