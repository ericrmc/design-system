---
session: 168
title: operator-absent-default-clause — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Bump prompt-development v17 to v18: add operator-absent-default clause to §1.5 (prefer tactical scope under bare-prompt).

**Kind:** substantive.  **Outcome:** supersede spec_version `prompt-development`.

**Why.**

- (engine_feedback) EF-S165-1 first-run bare-prompt friction proposed clause if second auto-proceed also tactical. [EF-S165-1]
- (engine_feedback) EF-S167-1 second-instance friction confirms tactical-skip and names the satisfaction route. [EF-S167-1]
- (prior_decision) DV-S164-1 established §1.5 bare-prompt auto-proceed mode this clause refines. [DV-S164-1]

**Effects.**

- supersedes prompt-development v17 active row flips to superseded; v18 ships with new §1.5 clause.

**Rejected alternatives.**

- **R-1.1.** Keep §1.5 as-is and let priority-order leverage suffice without naming an operator-absent default.
  - (inferior_tradeoff) Two auto-proceed sessions (S165, S167) both reached tactical via priority-2 leverage; explicit clause prevents future re-derivation from priority-order alone.
