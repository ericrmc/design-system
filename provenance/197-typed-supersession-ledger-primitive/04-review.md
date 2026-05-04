---
session: 197
title: typed-supersession-ledger-primitive — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: Handler computes alias via COUNT(*) FROM supersession_ledger WHERE sealed_at_session_id=?; under SQLite IMMEDIATE write_tx isolation this serializes correctly but pattern is fragile if isolation downgraded.
  - **adjudicated.** Forward-direction watch-FR per FR-S195-1 race-coverage precedent: SQLite IMMEDIATE serializes write_tx; COUNT inside same tx sees own INSERT; UNIQUE(alias) catches collision. Calibration-EF threading test if dual-write recurs.
- **high**: decision_v2 handler does not auto-route effect_kind=supersedes through supersession_ledger; soft-deprecation discipline is operator/agent-policed not handler-enforced.
  - **fixed.** Addressed by prompt-development v3 spec amendment shipped this session: clause directs agents to use supersession-ledger submit kind for new supersession events; decision_effects.supersedes channel deprecated by-discipline per DV-S109-1 ceremony-subtraction posture.
- **medium**: supersession_ledger.object_id back-pointer FK lacks index; reverse queries from objects to ledger row are infrequent but pattern asymmetric with other typed-row tables.
  - **adjudicated.** Acceptable v1 gap: back-pointer queries are low-volume (chain-walks traverse forward via objects.alias). Calibration-EF if reverse-lookup hot path emerges.
- **medium**: Test suite lacks concurrent-submitter scenario; alias collision under simultaneous writes not exercised though SQLite IMMEDIATE serializes.
  - **adjudicated.** Forward-direction watch-FR per FR-S195-1 race-coverage precedent: SQLite IMMEDIATE bound makes race not real today; threading test added if calibration-EF surfaces double-allocation.
- **medium**: prompt-development v3 spec amendment not yet shipped per codex sequencing-advice (in-session AFTER tests BEFORE close); DV-S197-1 closes OI-S196-2 without governing prompt clause.
  - **fixed.** Addressed in this iteration: spec-version v3 ships next per task-9 before session-close.
- **low**: Handler docstring states reason atom 8-240 chars but support_claim atom_type admits 8-480 per OI-S177-1 widening; doc inconsistent with actual bound.
  - **fixed.** Fixed: handler docstring updated to reflect support_claim 8-480 bound.
- **low**: No test verifies that source/target object_kind is meaningful for supersession (e.g. text_atom or session as supersedee); polymorphism-by-design admits all kinds.
  - **adjudicated.** Out of scope v1: D-S197-1 C-1 convergence on objects-FK polymorphism without source_kind/target_kind discriminator; admitting all object_kinds is the load-bearing design choice.
- **low**: Self-supersession refusal duplicated between handler check (E_VALIDATION) and SQL CHECK constraint (E_REFUSAL_CHECK); arguably redundant defense-in-depth.
  - **adjudicated.** Defense-in-depth intentional: handler check provides actionable error message naming both aliases; SQL CHECK is substrate-canonical refusal protecting against direct-write paths bypassing handler.

## Terminal passes

- **iteration 1** — findings @ `042c41200227`
  - Adversarial review iter-1: 8 findings (2 HIGH 3 MEDIUM 3 LOW) all dispositioned; alias-collision and concurrent-test-gap forwarded as race-coverage watch-FRs; soft-deprecation routing addressed by spec-v3 amendment.
- **iteration 2** — clean @ `042c41200227`
  - Iter-2 clean: F-72 atom-length doc fixed in supersession.py docstring + E_ATOM_LENGTH error message; remaining HIGH F-67 + F-68 + MEDIUM F-69/70/71 carry forward as named watch-FRs or in-session spec-v3 fix; no new findings surfaced.
