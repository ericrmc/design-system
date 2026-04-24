---
feedback_id: EF-047-brief-slot-template-hidden-arc-leakage
source_workspace_id: selvedge-self-development
source_session: 047
created_at: 2026-04-24
reported_by: operator
target: engine
target_files:
  - prompts/application.md
  - tools/bootstrap-external-workspace.sh
  - specifications/workspace-structure.md
severity: friction
status: inbox
---

# EF-047 — `applications/NNN-<slug>/brief.md` slot-template leaks arc structure under hidden-arc applications

## Observation

The Selvedge engine's external-application slot-template for `applications/NNN-<slug>/brief.md` (sourced from `prompts/application.md` §This application's context, instantiated by `tools/bootstrap-external-workspace.sh`) carries the section set: **Problem statement / Constraints / Stakeholders / Success condition / Initial state / Session arc (optional) / Notes for Session 001 (optional)**.

This set was designed for external-problem applications where scope is fully known at Session 001 (the canonical pattern per `prompts/application.md` §How to operate). For applications under the **hidden-arc constraint** — where the operator intentionally withholds future-session content from the executing sessions, per the S047 arc-plan §2.5 amendment for `selvedge-disaster-response` — populating some sections honestly would reveal the arc structure the constraint is protecting:

- **Success condition** framed at arc level (e.g., "plan supports evolving situations across multiple sessions") reveals multi-session arc design.
- **Session arc (optional)** populated with pre-planned structure (e.g., "4-5 sessions with per-session constraint invalidation") fully discloses the arc.
- **Notes for Session 001 (optional)** populated with meta-design notes risks disclosing the feedback-yield optimisation target.

The operator noticed the leakage when about to populate the template with S047 arc-plan §2a+§2b+§2c content and found that §2c alone did not fill all required sections, while filling the other sections naturally would either leak (Success-condition arc-framing) or expose the arc's existence (Session-arc populated).

## Why It Matters

The engine's spec-level description of external applications does not distinguish "fully-scoped-at-T0" applications from "hidden-arc" applications. The slot-template's section presence presupposes the former. For hidden-arc applications — which the engine supports operationally via operator-mediated per-session reveals and the S047-adopted three-part D-017-compliant invalidation mechanism — the template's shape creates a **pre-execution design friction** that the operator has to adjudicate ad-hoc at setup time.

Concretely: the operator must decide, for each section header, (a) whether populating honestly reveals too much, (b) whether leaving empty is acceptable or signal-of-something-withheld, and (c) whether the section header's presence alone conveys information. There is no spec guidance on this; each operator re-invents the judgement for each hidden-arc application.

This also has a provenance consequence: if the operator follows `prompts/application.md` literally and populates all sections at first commit, the git history of `brief.md` permanently carries the arc-leakage. The workaround (populate lean; leave optional sections empty; commit once; then `git init`) is operationally sound but is operator-discipline not engine-enforced.

The friction was caught pre-execution by operator observation. If it had not been caught, Session 001 of `selvedge-disaster-response` would have read a brief that either leaked the arc structure or read as suspiciously incomplete — either way compromising the hidden-scenario constraint the arc-plan depends on.

## Suggested Change

Two options, not mutually exclusive:

**(a) Add a "hidden-arc mode" to `prompts/application.md` §This application's context and to `tools/bootstrap-external-workspace.sh`.** The bootstrap script could accept a flag like `--hidden-arc` that emits a leaner `brief.md` stub omitting "Session arc (optional)" and "Notes for Session 001 (optional)" sections and replacing "Success condition" placeholder guidance with T0-only phrasing. `prompts/application.md` gets a new paragraph in §This application's context explaining the hidden-arc case and how to scope brief.md sections accordingly.

**(b) Document the operator-discipline workaround as convention in `specifications/workspace-structure.md` §applications.** Add a clause naming hidden-arc applications and specifying: Session arc + Notes sections should be left empty; Success condition should be T0-scoped; session-input-or-reveal-content should not be duplicated into brief.md after first commit.

Option (a) is more robust (engine-level mechanism); option (b) is minimally-invasive (documentation clarification). OI-002 classification: (a) is minor for a new bootstrap-script flag plus documentary addition to `prompts/application.md`; (b) is minor documentary amendment to `workspace-structure.md`. Neither triggers engine-v bump on its own; if both are adopted together they could be bundled as a single minor amendment.

## Evidence

- Arc-plan §11 transport instructions at `provenance/047-session/arc-plan.md` §11 currently include the directive "populate brief.md with §2a + §2b + §2c + statement that subsequent session inputs will arrive at each T0". **The clause "statement that subsequent session inputs will arrive at each T0" is itself a leakage bug** (concession by Case Steward during post-S047 operator discussion). The arc-plan is sealed per D-017; the bug lives there permanently as historical witness; this feedback record captures it forward.
- Bootstrap slot-template text currently at `tools/bootstrap-external-workspace.sh` step 6 (the `brief.md` heredoc content around lines 330-380 of the script); produces the seven-section template.
- `prompts/application.md` §This application's context lines 9-31 specifies the slot structure that the bootstrap script mirrors.

## Application-Scope Disposition

The `selvedge-disaster-response` external-application has NOT yet begun Session 001 as of this feedback's creation (2026-04-24). The friction was caught pre-execution. The operator will apply the lean-populate-plus-leave-optionals-empty workaround for this specific application's Session 001; that workaround is documented in the post-S047 out-of-session conversation (commit history may also carry the discussion).

The in-flight application's arc-plan is sealed per D-017 and carries the §11 leakage-language bug; the workaround addresses the execution-time impact but does not retroactively fix the arc-plan text. Post-arc self-dev review (per S047 D-150 obligation) should consider adopting option (a) and/or (b) above as part of the accumulated feedback-triage batch.

No in-session resolution occurred because the friction was caught out-of-session before Session 001 of the external application ran.
