---
session: 204
title: stakeholder-event-f-n-row-primitive-v1 — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S204 ships event-ledger v1 typed C-4 stakeholder-event F-N row primitive (2-table polymorphic objects-FK + 2-value enum + assumption-only allowlist + inert + EV alias); closes OI-S196-4.

**Kind:** schema_migration.  **Outcome:** adopt migration `054-event-ledger-v1`.

**Why.**

- (deliberation) P-1 schema-minimality stance argued 2-value enum + assumption-only allowlist per AR-S203-1 polymorphism-shape-without-substance lesson; codex 6-value enum names target object_kinds not registered in Selvedge today. [P-10-P-1]
- (deliberation) P-2 cross-app aggressive stance argued 4-value enum {invalidates-assumption, confirms-assumption, supersedes-claim, raises-concern} with broader allowlist preparing for cross-app per AR-S202-1; preserved as M-1 minority watch-trigger. [P-10-P-2]
- (deliberation) P-3 codex shape-consult returned SHIP-WITH-NAMED-EDITS verdict with 5 named edits (2-table, EV alias, polymorphic + SQL-trigger coupling, inert, defer SL-FK) + KNOT-2 6-value enum; preserved as M-2 forward-direction. [P-10-P-3]
- (engine_feedback) EF-S204-1 codex shape-consult per FR-S196-16 + FR-S203-11 returned SHIP-WITH-NAMED-EDITS; 5-of-5 named edits adopted; KNOT-2 enum cardinality is the load-bearing departure from codex per AR-S203-1 lesson. [EF-S204-1]
- (engine_feedback) EF-S196-2 bounded-scope binding precludes watch-FR or evidence-deferral for engine primitives evidenced by completed multi-session arc; OI-S196-4 is last MEDIUM substrate-promotion candidate from S196 21-session disaster-recovery harvest. [EF-S196-2]
- (prior_decision) DV-S203-1 cycle_ledger v1 ship pattern: standalone polymorphic via objects-FK with assumption-only allowlist + handler-side actionable refusal + SQL trigger backstop + alias CYC-S<wno>-<seq>; reused at v1 for event_ledger. [DV-S203-1]
- (prior_decision) DV-S197-1 supersession-ledger v1 polymorphism-via-objects-FK precedent + 5-value relation enum + closed CHECK + alias SL-S<wno>-<seq> + soft-deprecation pattern; precedent for 2-table 1:N pattern. [DV-S197-1]
- (prior_decision) DV-S198-1 typed-assumption-ledger v1 ship pattern: T-15-CALIBRATED rebuild + handler-side actionable refusal + closed CHECK + alias AR-S<wno>-<seq>; reused for object_kind widening. [DV-S198-1]
- (prior_decision) DV-S196-1 deliverable-mining triage opening OI-S196-4 with effects vocabulary {invalidates-assumption, invalidates-node, opens-risk, blocks-resolution-path}; harvest framing scoped at v1 to existing-kind targets per AR-S203-1. [DV-S196-1]

**Effects.**

- creates event_ledger v1 table + event_effects child + handler + submit kind
- adds_migration 054-event-ledger-v1
- bumps_engine engine-v58 to engine-v59
- closes_issue OI-S196-4 — OI-S196-4 by-mechanism via v1 ship
- modifies prompt-development v8 to v9 surfacing event submit kind + watch-triggers + cross-app generalization

**Rejected alternatives.**

- **R-1.1.** Ship codex P-3 6-value enum verbatim {invalidates-assumption, confirms-assumption, invalidates-node, opens-risk, blocks-resolution-path, advances-resolution-path} with T-43 refuse-on-target-kind-absence at v1 for forward-readiness.
  - (inferior_tradeoff) Names target object_kinds (node, risk, resolution_path) not registered as Selvedge primitives; AR-S203-1 polymorphism-shape-without-substance binds; substance-without-shape is wrong v1 shape; M-2 forward-direction preserved.
- **R-1.2.** Ship P-2 4-value enum {invalidates-assumption, confirms-assumption, supersedes-claim, raises-concern} with broader allowlist {assumption, decision_v2} from day one.
  - (inferior_tradeoff) supersedes-claim blurs against supersession_ledger primitive creating dual-channel risk per S197 M-1 precedent; raises-concern as catch-all risks generic-event-table drift; preserved as M-1 watch-trigger.
- **R-1.3.** Ship origin_event_id forward-FK on supersession_ledger this session wiring SL provenance to events.
  - (too_large_for_session) S197 deferred this forward-FK at C-4 explicitly; codex named edit #5 universal P-1+P-2+P-3 convergence on defer-to-v2; ship event primitive first; v2 wires SL provenance when an immediate producer + invariant exists.
- **R-1.4.** Auto-cascade invalidates-assumption to AR.status='invalidated' at handler dispatch.
  - (breaks_invariant) Mirrors S203 cycle no-auto-SR: cycle row IS proof of observation; events should be inert records like cycles per D-S204-1 C-3 universal convergence; codex named edit #4; M-3 watch-trigger preserved if external-app demand surfaces.
- **R-1.5.** Defer event_ledger ship pending second-arc evidence per DV-S190-2 graduation-discipline; ship watch-FR-only at v1.
  - (violates_gate) EF-S196-2 bounded-scope binding precludes watch-FR deferral for engine primitives evidenced by completed 21-session arc + operator-curated synthesis; OI-S196-4 is last MEDIUM substrate-promotion candidate from S196 mining.
- **R-1.6.** Single-table denormalized event header with N effects encoded as repeated columns or JSON blob.
  - (breaks_invariant) 1:N normalization invariant + universal P-1+P-2+P-3 convergence on 2-table per codex KNOT-1; events naturally have N effects per source-and-claim; mirrors decision_v2 + decision_effects precedent.
- **R-1.7.** Typed temporal column (TIMESTAMP or INT epoch) instead of free-text event_time_atom.
  - (breaks_invariant) DR-arc T+Nh format heterogeneity bars typed temporal commitment at v1; cross-app future events may use ISO or domain-specific; free-text atom admits all formats; v2 typed if query-by-time need.
