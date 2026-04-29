---
session: 130
title: temporal-claim-grounding — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Add temporal-claim grounding discipline to prompt-development; ground-or-omit applies to every submit body

**Kind:** substantive.  **Outcome:** supersede spec_version `prompt-development`.

**Why.**

- (engine_feedback) EF-S127-1 calibrated EF-S126-1's fabricated 4-month gap as narrative-driven number fabrication, exposing trust corrosion as a substrate-warrant failure regardless of prevalence. [EF-S127-1]
- (engine_feedback) EF-S126-1 carried the contaminated row in production prose, demonstrating the failure surface is freeform body_md. [EF-S126-1]
- (deliberation) Deliberation 16 P-1 anthropic and P-2 openai converged on all-submit scope and hard ground-or-omit rule. [P-16-P-1]
- (operator_directive) Operator framed prevalence as non-gating: one confirmed instance is structurally severe in a substrate where rows are normatively load-bearing.

**Effects.**

- supersedes SPEC-prompt-development-v7 — prompt-development v7 superseded by v8 ground-or-omit clause
- creates SPEC-prompt-development-v8 — prompt-development v8 ships ground-or-omit temporal-claim discipline

**Rejected alternatives.**

- **R-1.1.** Apply discipline to engine_feedback bodies only, scoped to the failure-mode locus.
  - (inferior_tradeoff) Calibrates to where fabrication appeared rather than where it could appear; assessments, close summaries, decision supports are equally porous prose surfaces.
- **R-1.2.** Soften to ground OR explicitly mark as unverified estimate, rather than ground-or-omit.
  - (inferior_tradeoff) Preserves the rhetorical slot where fabrication lives; an unverified tag normalises uncalibrated numbers entering the substrate.
- **R-1.3.** Duplicate the clause in methodology spec to mark temporal-provenance as kernel-level.
  - (redundant_with_existing) Methodology stays small-and-stable per kernel doctrine; duplication invites drift between two copies of the same rule.
- **R-1.4.** Ship a close-time lint that scans submit bodies for temporal phrases and forces confirm-or-delete before commit.
  - (too_large_for_session) Premature on one-row contamination; commits to a code path before discipline-only is exercised; deferred as conditional follow-up open issue.

## D-2. Defer close-time temporal-claim lint as conditional follow-up triggered by recurrence.

**Kind:** procedural.  **Outcome:** defer open_question `lint-vs-discipline-only`.

**Why.**

- (deliberation) P-2 openai proposed a lightweight close-time lint as middle-option short of the deferred typed sidecar; P-1 anthropic preferred discipline-only with escalation on recurrence. [P-16-P-2]
- (prior_decision) DV-S130-1 R-1.4 rejected lint-now as too_large_for_session at one-row contamination; OI-S130-1 captures the conditional escalation path. [DV-S130-1]

**Effects.**

- opens_issue OI-S130-1 — OI-S130-1 conditional close-time lint pending recurrence trigger
