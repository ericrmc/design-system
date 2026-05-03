---
session: 185
title: init-session-offset-bump — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Bump init_session_offset 79 to 179 to halt post-wipe folder collisions; preserve S080-S084 substrate aliases as historical artefact of S180 wipe.

**Kind:** substantive.  **Outcome:** adopt process_rule `session-numbering-offset-policy`.

**Why.**

- (prior_decision) DV-S081-1 substrate-loss-defense established T-06 closed-session text_atom immutability as load-bearing engine defense; the 84 atom rows referencing S08x in closed-session prose are unrewritable without T-06 carve-out which would create the same shape as the subagent destructive-op that caused the S180 wipe. [DV-S081-1]
- (prior_decision) Operator at S185-open selected path A from three enumerated options after the initial S085 proposal was caught as continuing the collision pattern; path A bumps offset only and preserves S080-S084 substrate aliases intact treating the five collision folders as historical record of the wipe and recovery arc. [DV-S081-1]

**Effects.**

- modifies workspace_metadata.init_session_offset 79 to 179; future sessions number S185+.
- adds_migration migration 043-bump-init-session-offset.sql; session opens as S185.

**Rejected alternatives.**

- **R-1.1.** Path B: substrate renumber S080-S084 to S180-S184 via T-06 carve-out; UPDATE objects.alias, issues.alias, sessions.workspace_session_no, text_atoms.text across 84 closed-session atom rows.
  - (violates_gate) T-06 closed-session text_atom immutability is a load-bearing defense per DV-S081-1; a carve-out for renumber maintenance creates the same shape as the subagent destructive-op the engine specifically defends against.
- **R-1.2.** Path C: snapshot-rollback substrate to pre-S080 via L3 boundary snapshot machinery from DV-S081-1; replay S080-S084 work as S180-S184 cleanly.
  - (too_large_for_session) Replay of five sessions of substrate-loss-defense work is methodology-disruptive; loses the calibration EFs that were authentic to the original sessions and the actual operator-decision shape recorded in DV-S081-1.
