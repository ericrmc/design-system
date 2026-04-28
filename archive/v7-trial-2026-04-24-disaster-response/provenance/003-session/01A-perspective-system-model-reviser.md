---
session: 003
title: 01A System-Model Reviser — raw perspective
date: 2026-04-24
status: complete
perspective: system-model-reviser
committed_at: 2026-04-24
---

## Q1. View count and axes

I propose a **three-view shape with a persistent ID catalogue**, totalling four sections in one file. The single-document v1 is **subsumed as the catalogue section, not retained as an independent base layer**. Rationale: a parallel base-plus-views scheme doubles the maintenance surface and invites drift between v1 prose and v2 tables — the very failure mode D-010's four-link traceability was meant to prevent.

Concretely, `system-model.md` v2 contains:

1. **§A — ID Catalogue** (flat list of every `POP-*`, `INF-*`, `SVC-*`, `DEP-*`, `EXT-*`, `SIL-*` with one-line canonical definition). This is the ID-of-record. Every view cites from it. No view re-defines a row.
2. **§B — View 1: Per-service dependency chain** (one block per `SVC-*`, showing upstream `INF-*` / `SVC-*` / `DEP-*` and downstream cohort reach). This is the view most directly motivated by Session 002's 23 re-derivation instances — the supplementary context names chain-walking (`SVC-03 → INF-04/INF-01 → INF-30 → INF-32`; `SVC-08 → SVC-05 → INF-11/INF-31`) as the cleanest empirical pattern.
3. **§C — View 2: Cohort × critical-service matrix** (rows: `POP-08`..`POP-15` plus other cohorts; columns: the clinically load-bearing services — dialysis/cold-chain/oxygen/potable-water/shelter-heat). Cells contain `DEP-*` IDs and time-to-harm flags. This captures the cohort-fragility axis D-012 already uses in the risk register and makes the cohort individuation (D-003) structurally enforced rather than disciplinary.
4. **§D — View 3: Evidence & silence index** (rows: every `SIL-*` plus every `ASM-*` / `GIV-*` the system model depends on, with the view and ID each backs). This keeps silence first-class per D-001 — silences are not buried in notes columns, they have their own section.

**Alternatives considered and rejected**:

- *Settlement-local topology as a fourth view.* Rejected: D-006 explicitly made settlement an attribute, not an axis. Promoting it to a view would reverse a Session 001 decision without new evidence; Session 002's re-derivation pattern did not concentrate on settlement-level reasoning (the 23 instances were dominated by chain-walking and cohort-service lookup).
- *Two-view shape (drop the cohort matrix, keep chain + evidence).* Rejected: cohort×service is the second-most-cited re-derivation shape in the supplementary context (the `POP-12` internal split is named explicitly as a §5.1 instance), and dialysis/cold-chain lookups will recur. Two views under-serve the observed pattern.
- *Five-view shape (add settlement + EXT-split).* Rejected: beyond four sections the reader has to learn the view taxonomy before reading — the re-derivation cost migrates from chain-walking to view-selection. Three views plus catalogue is the smallest set that covers the observed pattern.

## Q2. ID discipline

**v1 IDs remain canonical.** §A is the sole definition site. §B/§C/§D cite IDs; they do not mint replacements. This keeps `risk-register.md` and `response-plan.md` v1 citations resolvable without rewriting — their `POP-09` / `SVC-03` / `INF-04` references land in §A unchanged.

I propose **no view-scoped derived IDs** (no `COH-POP-09`, no `CHAIN-SVC-03`). Derived IDs look tidy but create a second namespace downstream artefacts would eventually cite, re-creating the drift problem. Instead, views use **compound citations** in-line: a chain row reads `SVC-03 ⇐ INF-04, INF-01 ⇐ INF-30 ⇐ INF-32 ⇐ ASM-11` — all canonical IDs, assembled by the view.

Drift prevention is **mechanical, not disciplinary**: a linter check (or manual closure check at session end) verifies every ID appearing in §B/§C/§D exists in §A, and every §A ID appears in at least one view or is flagged `catalogue-only` in §A itself. This is the same closure discipline D-010's four-link traceability already implies; v2 makes it enumerable.

The ID-preservation rule is: **§A rows are immutable within a session; splits (like `ASM-19` → `ASM-19a`/`ASM-19b`, or `POP-12` → `POP-12a`/`POP-12b`) are session decisions logged to the assumption ledger, not view-time edits.**

## Q3. `ASM-19` split

Split per D-018:

- **`ASM-19a` recipient-reliability**: the Laurel Delta incident command's capacity to receive, triage, and act on central-government communication within the acute window. Falsifier: two or more central-government directives during `WIN-acute` go un-acknowledged or un-actioned beyond their stated response window. Review trigger: any directive with response-window ≤12h that lapses unacknowledged.
- **`ASM-19b` delivery-reliability**: central government's capacity to deliver promised resources (fuel, medical supplies, personnel rotations) within committed timeframes. Falsifier: any committed delivery slips its stated ETA by >50% or is silently cancelled. Review trigger: first missed delivery, or any silent cancellation.

Both need review triggers because they fail independently: recipient failure is a local-capacity problem, delivery failure is a counterparty-capacity problem, and response actions differ (recipient failure prompts ICS re-staffing; delivery failure prompts substitute-supplier activation).

In v2 §A these appear as two rows citing `EXT-01` as the shared interface. §B's `EXT-01`-consuming chains (fuel in particular — `ACT-005` cold-chain and `RSK-014` generator-fuel both depend on it) cite `ASM-19b` specifically; directives-acknowledgement chains cite `ASM-19a`.

**Downstream flag (Session 004+)**: `RSK-019` currently references `ASM-19` as a single row. Once v2 ships, `RSK-019` is under-specified: it conflates two failure modes with different response actions. I flag this for Session 004+ risk-register v1.1; I do not propose updating `RSK-019` this session (out of scope per problem statement §2).

## Q4. `POP-12` sub-individuation

**Split `POP-12` into `POP-12a` (oxygen-dependent) and `POP-12b` (CPAP-dependent) at v2.** Session 001 D-007 declined on count-silence grounds (`ASM-06`), but the v2 shape changes the cost calculus: the cohort×service matrix (§C) places oxygen and CPAP in separate columns because their time-to-harm differs (oxygen failure is minutes-to-hours; CPAP failure is nightly, with cumulative fatigue/cardiac load over days). Keeping `POP-12` aggregate forces the matrix cell to carry a dual time-window note — exactly the "re-derive under session pressure" cost §5.1 names.

Falsifiers for the count silences:

- `SIL-POP-12a-count` (new): the oxygen-dependent subpopulation count is unknown; falsifier is any authoritative enumeration (e.g., registered-device registry access, or door-to-door welfare survey ≥80% coverage).
- `SIL-POP-12b-count` (new): the CPAP-dependent count is unknown; falsifier is the same enumeration source.

`ASM-06` is retained as the parent assumption and cited by both new silences; it is not deleted because the aggregate count uncertainty still binds.

`RSK-004`'s dual-window treatment becomes cleanly expressible in v1.1: one sub-risk per sub-cohort rather than a compound row. I flag this for Session 004+ and do not rewrite `RSK-004` here.

## Q5. Migration and supersession

**Preferred: option (A) supersession-chain file.** `applications/001-disaster-response/system-model-v1.md` is retained verbatim with frontmatter `status: superseded-by-v2, superseded-at-session: 003, supersession-reason: §5.1 multi-view activation warrant fired at Session 002 close (D-019)`. The new file `system-model.md` carries `supersedes: system-model-v1.md, version: 2, last-revised-session: 003`.

Why (A) over alternatives:

- **(B) copy-plus-reference** duplicates content in the provenance record; the workspace-structure v5 §applications clause admits it but the cost here (six sections of v1 prose) is unnecessary when git + an explicit file is cheaper.
- **(C) git-history-only** loses the standalone readability of v1 for future sessions auditing the shape change. The §5.1 preserved minority warrants auditable provenance of what it superseded.

Frontmatter also carries `validation: workspace-only` (unchanged from v1 per kernel v6 §7) and `preserves-ids-from: v1` as an explicit closure marker for the Q2 discipline.

## Q6. Risk-plan downstream impact

Yes — v2 makes several v1 rows visibly thinner. Flagging for Session 004+ v1.1:

- **`RSK-014` (generator-fuel multi-downstream)**: v2 §B's `SVC-07` / fuel-dependent chains will enumerate every downstream cohort impact (dialysis, cold chain, oxygen concentrators, water pumping). `RSK-014` currently compounds these into one row; post-v2 it is visibly under-decomposed. Candidate v1.1: split into per-downstream sub-risks or add an explicit downstream-cohort list citing the §B chain.
- **`RSK-019` (EXT-01 cross-cutting)**: already flagged under Q3; conflates `ASM-19a`/`ASM-19b`.
- **`ACT-005` (cold-chain POP-13/14/15)**: v2 §C's cold-chain column exposes that POP-13/14/15 have distinct time-to-harm profiles for the same service. `ACT-005` currently treats them as a group; post-v2 the grouping is visibly coarse. Candidate v1.1: per-cohort sub-actions or explicit time-to-harm triage within the action.
- **`RSK-015` (freight-rail-bridge + fibre shared-fate)**: v2 §B makes shared-fate visible as two chains converging on one `INF-*`. The risk row stays correct but its warrant strengthens; likely a citation update rather than a decomposition.
- **`RSK-008` (aged-care cluster welfare)**: v2 §C exposes aged-care cohorts' multi-service dependency (power + cold-chain + oxygen + potable-water). `RSK-008`'s single-row welfare framing becomes visibly thin. Candidate v1.1: decompose into per-dependency sub-risks.

Summary: at least `RSK-014`, `RSK-019`, `ACT-005`, and `RSK-008` are visibly thinner post-v2. `RSK-015` tightens but does not thin. Session 004+ inherits a non-trivial v1.1 queue; this is an honest consequence of the multi-view adoption, not a defect of the proposal.

## Q7. Anti-laundering check

External frames the three-view proposal resembles:

- **Lifelines / critical-infrastructure-sector taxonomies (`EXT-SURVEY-04`)**: §B's per-service chain view resembles lifeline dependency mapping. **Surveyed-and-adopt-with-reason**: the chain shape is warranted by Session 002's 23 re-derivation instances (workspace evidence), not by the lifelines catalogue. Adoption is pattern-coincident, not taxonomy-imported: I use `SVC-*` IDs from v1, not lifeline sector names.
- **UN/IASC clusters (`EXT-SURVEY-02`)**: §C's cohort × service matrix could superficially resemble cluster-based programming. **Surveyed-and-declined as structure**: clusters are supply-side service-provider groupings; §C is demand-side cohort-fragility. The columns are the services v1 already names, not the 11 IASC clusters. Coincidence of tabular shape, not taxonomic import.
- **ICS/NIMS (`EXT-SURVEY-01`)**: not resembled by the proposal; ICS is operational-command, v2 is system-model. **Surveyed-and-declined**.
- **Enterprise architecture (TOGAF / Zachman / C4)**: Zachman's "views on the same underlying model" pattern is the closest pretrained analogue to what I am proposing. **Ambivalent, leaning adopt-with-reason**: the single-catalogue-plus-views structure is a genuinely Zachman-shaped idea; I name the resemblance here rather than silently import it. The warrant for adoption is the §5.1 activation evidence, not Zachman's authority. If a future session finds this resemblance is doing more taxonomic work than acknowledged, it warrants re-examination.
- **Systems-dependency frames (DoDAF OV-5, ArchiMate, causal-loop diagrams)**: §B's chain view partially resembles these. **Surveyed-and-declined as notation**: I use plain `ID ⇐ ID` chain syntax, not DoDAF boxes or ArchiMate glyphs. The shape is Session 002-evidence-driven.

## Honest limits

I have not participated in Sessions 001 or 002. My read of the 23 re-derivation instances is from the supplementary context's summary, not the underlying perspective transcripts — if the instances cluster on an axis I haven't named (e.g., temporal / sub-window), the three-view proposal under-serves that pattern. The Vulnerability Advocate is better placed to test whether §C's cohort matrix captures the fragility dimensions they actually reason with.

I have not tested whether four sections fit the 8,000-word ceiling for a catalogue of 107 IDs (24+19+15+22+3+24) plus three views. A rough estimate (one line per catalogue ID, ~15 chain blocks in §B, a ~24×6 matrix in §C, ~24 silence rows in §D) fits comfortably, but I have not mocked a page. If §A-alone runs long, the view sections compress first.

My `POP-12` split recommendation leans on a clinical time-to-harm claim (oxygen minutes-to-hours vs CPAP nightly-cumulative) that is general knowledge; I have not sourced it to workspace evidence and `ASM-20`'s no-pretrained-clinical-numbers rule is adjacent. The shape argument (matrix column separation) stands regardless, but the falsifier language may need workspace-local re-grounding by the Reviser-proper at write time.
