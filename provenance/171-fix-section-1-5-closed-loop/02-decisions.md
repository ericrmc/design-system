---
session: 171
title: fix-section-1-5-closed-loop — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Bump prompt-development v18 to v19: §1.5 inserts tractable MEDIUM-OI as priority-2 ahead of untriaged EFs; disqualifies self-referential EFs; adds starvation-breaker plus operator-diagnosis-as-named-mandate clauses.

**Kind:** substantive.  **Outcome:** supersede spec_version `SPEC-prompt-development-v19`.

**Why.**

- (operator_directive) Operator named five-session closed-loop S165-S170 as failure mode and instructed: open a session, discuss with codex agent, fix it, prioritise medium issues over recent feedback. [A-S171]
- (deliberation) Cross-family deliberation D-25 with P-1 anthropic and P-2 openai-codex converged on inserting MEDIUM-OI as priority-2 plus disqualifying self-referential EFs plus admitting MEDIUM-OI burndown as tactical under operator absence. [P-25-P-2]
- (engine_feedback) EF-S170-1 calibration recorded fifth-recurrence threshold of priority-2 EF triage concentration as expected behaviour requiring §1.5 meta-pattern naming at next operator-present session. [EF-S170-1]
- (prior_decision) DV-S109-1 ceremony-subtraction discipline argues against substrate-side enforcement until prompt-only proves insufficient; v19 ships prompt-only edit and preserves substrate-tagging as M-1 graduation path. [DV-S109-1]

**Effects.**

- supersedes SPEC-prompt-development-v18 — SPEC-prompt-development-v18 superseded by v19 with §1.5 priority-order and operator-absent-default edits.
- creates SPEC-prompt-development-v19 — SPEC-prompt-development-v19 active body at prompts/development.md.

**Rejected alternatives.**

- **R-1.1.** Direct reorder only: insert MEDIUM-OI as priority-2 without any other §1.5 edit (operator's bare suggestion alone).
  - (inferior_tradeoff) Operator-absent-default clause currently classifies most MEDIUM OIs as substantive deferred; bare reorder would pick MEDIUM then defer, falling through to EF triage and re-entering the loop.
- **R-1.2.** P-1 fixed N=2 consecutive-tactical-counter for the starvation-breaker shape rather than P-2 starvation-breaker keyed to absence of non-meta progress.
  - (redundant_with_existing) Codex P-2 dissent at D-25 argued the counter is itself bookkeeping ceremony; the substrate-detectable absence-of-non-meta-progress signal achieves the same trigger without prompt-side counting.
- **R-1.3.** P-2 substrate-tagging proposal: ship migration NN adding meta_self_ref / audit_only / operator_signal columns to engine_feedback plus priority-3 handler refusing self-referential EFs on tag-presence.
  - (too_large_for_session) DV-S109-1 ceremony-subtraction discipline argues against substrate enforcement until prompt-only proves insufficient; recurrence pressure is one-loop-of-five not multi-loop; preserved as M-1 graduation path with promotion trigger.
- **R-1.4.** Subtract the operator-absent-default clause entirely; let bare-prompt always pick whatever priority-order yields including substantive paths.
  - (preserves_legacy_path) EF-S165-1 plus EF-S167-1 origin trail named the tactical-vs-substantive judgment call as the original failure the clause addressed; retracting it would reopen that prior failure.
