---
feedback_id: EF-047-session-input-files-redundant-with-verbatim-capture
source_workspace_id: selvedge-self-development
source_session: 047
created_at: 2026-04-24
reported_by: operator
target: methodology
target_files:
  - provenance/047-session/arc-plan.md
  - prompts/application.md
  - specifications/multi-agent-deliberation.md
severity: observation
status: inbox
---

# EF-047 — Per-session input-files (`session-inputs/session-NNN-input.md`) are redundant with existing operator-verbatim-capture-at-session-open discipline

## Observation

The S047 arc-plan (at `provenance/047-session/arc-plan.md` §3 + §11) mandates a `applications/001-disaster-response/session-inputs/` subdirectory in the external workspace, with one `session-NNN-input.md` file per non-T0 session carrying the operator-delivered constraint-update brief sealed at session delivery. The pattern was synthesised from four perspectives' convergent recommendations during the S047 MAD.

The operator, post-S047 out-of-session, observed that this pattern duplicates work the engine already does naturally: **operator messages at session-open are captured verbatim in each session's `provenance/NNN-session/00-assessment.md` §2 (operator agenda verbatim)** as established convention across self-dev Path OS sessions (S036/S043/S044/S045/S046/S047) and consistent with `multi-agent-deliberation.md` v4 §Stance Briefs recording discipline. Creating a separate `session-NNN-input.md` file is therefore a second pointer to content that is already recorded in provenance.

The operator's refinement: **drop the `session-inputs/` subdirectory and per-session input files entirely.** Instead, operator pastes the reveal content (in the four-section format the arc-plan specified — New Facts / Invalidated Prior Assumptions / Constraints for This Session / Do Not Resolve By Editing Prior Sessions) as the session-open message when opening Claude Code in the external workspace. The session's Case Steward captures this verbatim in `00-assessment.md` §2, producing identical provenance-level artefact without the file-placement step between sessions.

## Why It Matters

Three concrete improvements from the operator's refinement:

1. **Operational simplicity**: operator workflow reduces from "draft input → place file → git-commit → open Claude Code" to "draft reveal → paste at session-open". No intermediate file-placement step.

2. **Consistency with existing engine discipline**: verbatim capture of operator input in 00-assessment.md §2 is already how Path OS sessions work in self-dev. External sessions should inherit the same discipline rather than inventing a parallel mechanism. The session-inputs/ pattern was arc-plan-level over-engineering.

3. **Removes a minor leakage signal**: the `session-inputs/` directory name is plural, mildly suggesting multi-session structure. For hidden-arc applications (see companion `EF-047-brief-slot-template-hidden-arc-leakage.md`), eliminating the directory removes one of several small leakage surfaces. Not load-bearing alone but contributes.

Additionally: the arc-plan's §7 anti-laundering guards reference `session-input.md` as the pointer target for artefact-revision traceability (guard 2: "every revision after S001 updates `last-revised-session` and includes a `supersedes` OR `change_reason` entry naming the triggering `session-input.md` file"). Substituting the pointer target to `provenance/NNN-session/00-assessment.md` §2 preserves the guard's traceability function without requiring the file.

The S047 MAD did not surface this simplification because all four perspectives converged on the session-input-file pattern — none questioned whether the pattern was necessary given existing verbatim-capture discipline. This is a case of **4-of-4 convergence potentially indicating shared-frame blindness** (flagged in S047 `01-deliberation.md` §7 as a risk but not caught for this specific over-engineering).

## Suggested Change

Two levels of change:

**Practice-level (immediate, for `selvedge-disaster-response` arc execution)**: the operator follows the refined flow — no `session-inputs/` directory created in the external workspace; reveals pasted at session-open; captured verbatim in each external session's `00-assessment.md` §2. No engine-level change required for this to work; it falls under operator-discretion within the arc-plan §11 "operator is the transport" framing.

**Spec-level (post-arc review for future hidden-arc applications)**: the arc-plan-template pattern embedded in the S047 arc-plan should not be reproduced for future external-application arc-plans. Candidate additions to `prompts/application.md` §Engine-feedback pathway or a new paragraph in `specifications/workspace-structure.md` v5 §engine-feedback explicitly noting that operator-mediated per-session reveals use the existing 00-assessment.md §2 verbatim-capture discipline; no per-session input-file convention is required. OI-002 classification: **minor documentary amendment**.

## Evidence

- Arc-plan at `provenance/047-session/arc-plan.md` §3b-§3e (per-session stubs referencing `session-inputs/session-00N-input.md`) and §11 (transport instructions referencing the subdirectory).
- Self-dev Path OS precedent: `provenance/036-session-assessment/00-assessment.md` §2, `provenance/043-session-assessment/00-assessment.md` §2, `provenance/044-session-assessment/00-assessment.md` §2, `provenance/045-session-assessment/00-assessment.md` §2, `provenance/046-session/00-assessment.md` §2, `provenance/047-session/00-assessment.md` §2 — each captures operator session-open message verbatim in §2. This is established convention.
- `multi-agent-deliberation.md` v4 §Stance Briefs Step 3: "The returned response is committed verbatim as a raw-output file... with the same naming convention" — the verbatim-capture discipline extends from participant outputs to operator inputs by convention.

## Application-Scope Disposition

The `selvedge-disaster-response` arc has not yet begun. The refined flow (no session-inputs/, verbatim-capture at session-open) will be applied from Session 001 onward. The arc-plan's text at §3/§7/§11 referencing `session-inputs/` is operationally superseded by this refinement; the arc-plan file itself is sealed per D-017 and carries the over-engineered text as historical witness.

This observation is **lower severity than the companion EF-047-brief-slot-template-hidden-arc-leakage.md record** — it's a simplification opportunity rather than a risk of execution-time failure. Recorded as `severity: observation` vs. companion's `severity: friction`. Suggested handling: batch with the brief-slot-template feedback for post-arc self-dev review, since both relate to hidden-arc-application patterns.

No in-session resolution occurred; the observation arose out-of-session during discussion of the brief.md slot-template concern.
