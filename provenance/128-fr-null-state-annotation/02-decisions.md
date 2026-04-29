---
session: 128
title: fr-null-state-annotation — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt orient-time FR null-state annotation closing OI-S126-4 with phrase-pattern detection.

**Kind:** substantive.  **Outcome:** adopt process_rule `fr-null-state-orient-annotation`.

**Why.**

- (deliberation) Convergence C-1: both perspectives reject discipline-only and require null-state items be visibly differentiated.
- (operator_directive) Operator selected OI-S126-4 as the session target; FR-S126-8 framed it as a small low-friction substrate fix.
- (engine_feedback) Current FR queue contains FR-S117-11 as a pure null-state placeholder; orient surfaces it every session indefinitely.

**Effects.**

- modifies selvedge/orient.py adds null_state boolean per FR item, emitted as bracketed null-state markdown annotation.
- modifies selvedge/paths.py adds FR_NULL_STATE_RE regex co-located with FR_ISSUE_CITE_RE.
- closes_issue OI-S126-4 — OI-S126-4 next_session_should null-state forward references resolved via orient annotation.

**Rejected alternatives.**

- **R-1.1.** Add fr_state column to close_state_items with null_state value plus close-record submit refusal plus default elision per P-2.
  - (too_large_for_session) Schema migration plus submit handler change plus mixed-item splitting exceeds the small low-friction scope FR-S126-8 named.
  - (inferior_tradeoff) Single pure null-state case in 22 FRs is too thin a sample to design substrate columns around; heuristic suffices.
- **R-1.2.** Discipline-only: clarify section 8.5 disposition guidance without code change.
  - (no_feedback_loop) Current state is discipline-only; FR-S117-11 has persisted across ten sessions despite section 8.5 disposition requirement.
- **R-1.3.** Elide null-state FRs from default orient render with --include-null-state escape hatch.
  - (violates_gate) Orient is documented as a live read of substrate state; default elision conflicts with that contract and adds a flag operators must remember.

## D-2. Defer P-2 schema-column enforcement direction (fr_state, submit refusal, mixed splitting) until null-state items recur after annotation lands.

**Kind:** substantive.  **Outcome:** defer process_rule `fr-null-state-enforcement-direction`.

**Why.**

- (deliberation) M-1 minority preserves P-2 enforcement direction conditional on annotation alone failing to discipline future close-records.
- (engine_feedback) Reopen criterion: a second pure null-state FR registered after annotation ships, or operator observation that mixed items resist disposition.

**Effects.**

- modifies Engine direction noted; no substrate change. Reopen via new OI when reopen criterion fires.

**Rejected alternatives.**

- **R-2.1.** Adopt P-2 enforcement now alongside annotation as a layered defense.
  - (redundant_with_existing) Annotation alone may suffice; layered enforcement before observing annotation efficacy adds ceremony before earning it.
