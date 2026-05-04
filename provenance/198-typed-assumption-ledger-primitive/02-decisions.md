---
session: 198
title: typed-assumption-ledger-primitive — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S198 ships typed-assumption-ledger v1 (6-status closed enum + 3-value sub-type + four-field DV-S008-1 discipline + mutable-status-update + AR object-registration); closes OI-S196-1.

**Kind:** schema_migration.  **Outcome:** adopt migration `049-assumption-ledger-v1`.

**Why.**

- (deliberation) P-1 schema-minimality stance argued 6-value status enum tighter than codex 9-value (commentary-shaped values rejected) plus 3-value disaster-recovery sub-type plus reject history table. [P-6-P-1]
- (deliberation) P-2 engine-self-consumer-readiness stance argued §8.5 audit-step is primary v1 consumer; AR alias must be citable from EF body_md or §8.5 stays referentially broken. [P-6-P-2]
- (deliberation) P-3 codex shape-consult verdict SHIP-WITH-NAMED-EDITS endorsed object-registration mandatory plus four-field discipline plus AR alias scheme; 5 of 6 named edits adopted. [P-6-P-3]
- (engine_feedback) EF-S198-1 codex shape-consult endorsed v1 design with 6 named edits; 5 adopted (AR alias plus closed-CHECK plus two-handler split plus four-field plus drop-priority); 1 rejected (history table) per P-1+P-2 convergence. [EF-S198-1]
- (engine_feedback) EF-S196-2 bounded-scope binding precluded watch-FR deferral for engine primitives evidenced by completed multi-session arc plus operator-curated synthesis; bias-toward-build-now applies. [EF-S196-2]
- (engine_feedback) EF-S196-1 codex S196 sequencing named C-1 typed-assumption-ledger after C-2 typed-supersession-ledger; S197 shipped C-2 (DV-S197-1) so S198 ships C-1 per FR-S197-13 sequencing. [EF-S196-1]
- (prior_decision) DV-S081-1 substrate-loss-defense binds: typed primitive over objects.alias graph composes with chain_walks T-32; AR-S<wno>-<seq> object-registration preserves substrate-canonical invariant. [DV-S081-1]
- (prior_decision) DV-S189-1 markdown-only-recovery binds: no synthetic-row backdating; legacy disaster-recovery markdown A-NNN rows are not auto-imported as typed rows. [DV-S189-1]
- (prior_decision) DV-S197-1 supersession-ledger v1 sets the typed-primitive ship pattern (handler plus alias plus object-registration plus T-15-CALIBRATED rebuild plus role_write_capabilities inline) which v1 mirrors. [DV-S197-1]

**Effects.**

- creates assumption_ledger v1 table + 2 submit kinds
- adds_migration 049-assumption-ledger-v1
- closes_issue OI-S196-1 — OI-S196-1 by-mechanism via v1 ship
- modifies prompt-development v3 §8.5: A-NNN -> AR-S<wno>-<seq>

**Rejected alternatives.**

- **R-1.1.** Ship 9-value status enum from codex P-3 starting set (unverified, monitored, assumed, unknown, worst-case-assumed, active-with-conflict, closed, superseded, invalidated).
  - (inferior_tradeoff) P-1 audit found monitored/unknown/worst-case-assumed as commentary-shaped not state-machine-shaped; admitting them risks generic-status drift mirroring S197 R-1.1 7-value rejection.
- **R-1.2.** Ship P-2 9-value engine-self enum (proposed/active/accepted-implicit/etc) reframing the primitive around §8.5 audit-step disposition vocabulary.
  - (inferior_tradeoff) OI-S196-1 explicitly cites disaster-recovery arc sub-types as the typed source; P-2 use-case framing collapses status-vs-disposition distinction; preserved as M-2 minority.
- **R-1.3.** Ship P-2 supersession-only transitions (no mutable status; all later movement via supersession_ledger AR edges).
  - (inferior_tradeoff) Closure is not the same relation as object replacement; mixing the two ledgers weakens audit readability; preserved as M-1 minority watch-trigger if status-mutation drift surfaces.
- **R-1.4.** Ship dedicated assumption_status_changes history table at v1 per codex named edit #4 (change_id PK plus from_status plus to_status plus changed_at plus origin_decision_object_id plus basis_atom_id plus note_atom_id).
  - (inferior_tradeoff) P-1+P-2 convergence: replay walks decisions_v2+decision_supports+effects against assumption.object_id; second channel courts dual-channel watch-trigger S197 just paid for; M-3 minority preserved as v2 promotion-trigger.
- **R-1.5.** Defer ship to second-arc evidence per DV-S190-2 graduation-discipline; ship watch-FR-only at v1 with no substrate primitive.
  - (violates_gate) EF-S196-2 bounded-scope binding precludes watch-FR deferral for engine primitives evidenced by completed multi-session arc plus operator-curated synthesis plus named recurrence; bias-toward-build-now applies per S197 precedent.
- **R-1.6.** Add priority TEXT NULL CHECK in (high, medium, low) column for [P3]-style overlay round-tripping legacy disaster-recovery markers.
  - (too_large_for_session) Priority is foreclosed by deliberation scope at convening; legacy [P3] markers are commentary-shaped per P-1; admit later via single-line column-add migration if recurrence demands.
- **R-1.7.** Use object_kind='assumption_ledger' matching S197 supersession_ledger naming for kind-name consistency.
  - (redundant_with_existing) P-1 explicit: the _ledger suffix is post-hoc and the table-name carries the _ledger semantic without redundancy in kind column; future tables prefer unsuffixed form.
