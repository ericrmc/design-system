---
session: 097
title: self-driving-dispatch-and-disposition-handlers — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Self-driving dispatch: ship forward_reference_dispositions, engine-feedback-disposition handler, and prompt-development v3 (engine-v27).

**Kind:** substantive.  **Outcome:** adopt engine_version `engine-v27`.

**Why.**

- (engine_feedback) EF-S095-1 surfaced that prompts/development.md has no analogue of application.md §When friction surfaces. [EF-S095-1]
- (engine_feedback) EF-S096-1 surfaced that next_session_should items have no substrate link to the resolving session. [EF-S096-1]
- (engine_feedback) EF-S096-2 surfaced that the engine-feedback insert path landed at engine-v26 but disposition still required raw SQL. [EF-S096-2]
- (operator_directive) Operator directed batching of these three remedies in one session to clear narrative-to-substrate friction before tackling OI-016.

**Effects.**

- adds_migration state/migrations/013-forward-reference-dispositions.sql
- creates submit handler engine-feedback-disposition
- creates submit handler forward-reference-disposition
- modifies _orient_sections forward-references query: drop 3-session window, filter on dispositions, render FR-S<wno>-<seq> ids
- supersedes SPEC-prompt-development-v2
- supersedes SPEC-engine-manifest-v26
- bumps_engine engine-v26 -> engine-v27

**Rejected alternatives.**

- **R-1.1.** Pick only EF-S096-2 (smallest) and leave forward-reference resolution + prompt amendment for later.
  - (operator_override) Operator directed all three to ship together so the queue is drainable before OI-016.
- **R-1.2.** Implement EF-S096-1 with closes_forward_reference effect_kind on decision_effects (option a in EF-S096-1) instead of a dedicated table.
  - (inferior_tradeoff) Dedicated table mirrors the established issue_dispositions / finding-disposition pattern, keeps the resolved_at/note semantics first-class, and avoids a CHECK relaxation on decision_effects.
