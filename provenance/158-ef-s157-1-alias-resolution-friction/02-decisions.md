---
session: 158
title: ef-s157-1-alias-resolution-friction — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt path B: prompt-development §5 cite-typing callout plus _resolve_alias_to_object_id diagnostic for OI-/FR- shape mismatches.

**Kind:** substantive.  **Outcome:** adopt process_rule `decision-record-cite-resolution-diagnostic`.

**Why.**

- (deliberation) P-1 anthropic and P-2 openai-codex converge on path B as minimum sufficient remedy; both reject A alone preserving misleading unresolved-alias message and C as schema-mandate from one S157 slip.
- (engine_feedback) EF-S157-1 names alias-resolution split surface as operator-facing friction at decision-record submit; OI-/FR- aliases live outside objects table so cite refused with E_REFUSAL_T01.
- (prior_decision) Migration 021 (DV-S113-1) documents 24 OI-mentioning plus 9 FR-mentioning NULL-cite supports as bounded residual; pattern recurs at S157 confirming non-zero recurrence.
- (spec_clause) Methodology preference for minimum sufficient remedy plus subtraction discipline argues against schema-widening when bounded-residual operator-policed remedy suffices.

**Effects.**

- modifies prompt-development §5 cite-typing callout addressing basis-cite kind matrix discipline.
- modifies selvedge/aliases.py _resolve_alias_to_object_id detects OI-/FR- alias shape and emits basis-aware guidance message.

**Rejected alternatives.**

- **R-1.1.** Path A spec-callout only without handler diagnostic improvement.
  - (inferior_tradeoff) P-1 P-2 convergence: A leaves operator-facing diagnostic mute on the structural reason perpetuating the same slip at next refusal; callout alone is operator-policed without recovery surface.
- **R-1.2.** Path C schema widening (add cited_issue_id and cited_forward_ref_id columns; close OI-086-003 structurally).
  - (too_large_for_session) Schema split forces migration plus basis-enum debate plus export and anchor-traversal plus test burden disproportionate to current bounded-residual recurrence; OI-086-003 stays open as graduation-trigger placeholder.
- **R-1.3.** Broader basis-to-cite kind matrix detection covering all basis-cite kind mismatches not just OI-/FR- shape.
  - (inferior_tradeoff) Synthesis C-3: broader matrix accumulates diagnostic logic in code without substrate introspectability; ship narrower OI-/FR- shape detection now and defer broader matrix as forward-reference if recurrence shifts.
