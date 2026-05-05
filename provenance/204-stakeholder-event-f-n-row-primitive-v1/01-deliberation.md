---
session: 204
title: stakeholder-event-f-n-row-primitive-v1 — deliberation
generated_by: selvedge export
---

# Deliberation

## D-10 — S204 C-4 stakeholder-event F-N primitive shape: 2-table event_ledger+event_effects v1 design knots

sealed_at: 2026-05-05T09:18:45.097Z

### P-1 (anthropic)

### P-2 (anthropic)

### P-3 (openai)

### Synthesis

**Adopted shape: P-1 + P-2 partial-merge over P-3 codex.** Standalone 2-table event_ledger + event_effects polymorphic via objects-FK; v1 enum is 2-value tight {invalidates-assumption, confirms-assumption} per AR-S203-1 polymorphism-shape-without-substance lesson + AR-S203-2 synthesis-vs-CHECK coupling lesson; events inert at v1 per codex named edit #4 + S203 cycle no-auto-SR precedent; defer supersession_ledger.origin_event_id to v2 per codex named edit #5; alias EV-S<wno>-<seq> per codex named edit #1; required event_time_atom + source_atom + claim_atom per codex named edit + KNOT-8 universal convergence; T-43 SQL trigger enforcing effect-kind to target object_kind coupling at SQL not handler-only per AR-S203-2 lesson.

**The load-bearing departure from codex P-3 is enum cardinality at v1: 2-value not 6-value.** P-1 surfaced that codex's 4 additional effect-kinds (invalidates-node, opens-risk, blocks-resolution-path, advances-resolution-path) name target object_kinds that do NOT EXIST in Selvedge's substrate today. AR-S203-1 (lifted at S203) explicitly bounds polymorphism to shape without substance: v1 ships shape, allowlist narrows so semantic-coupling stays bounded. Shipping enum values whose targets cannot resolve is the inverse failure mode — substance-without-shape, naming kinds that have no semantics. P-2 partially agreed with a 4-value middle ground including supersedes-claim + raises-concern; rejected as introducing dead-channel risk for kinds (supersedes-claim, raises-concern) that are not directly evidenced in the disaster-recovery harvest the OI was mined from. The 2-value enum at v1 is the minimum-viable-evidenced ship; v2 widens via cheap T-15-CALIBRATED rebuild (DV-S198-1 ledger-rebuild precedent) when (a) Selvedge ships node/risk/resolution_path primitives or (b) external-app substrates demand them.

**Convergence.**
- C-1 (KNOT-1): two tables (event_ledger header + event_effects child) — 1:N is naturally 1:N pattern (P-1+P-2+P-3 all converge per codex KNOT-1).
- C-2 (KNOT-3): polymorphic target_object_id via objects + T-43 SQL trigger for effect-kind → target object_kind coupling enforced at SQL not handler-only (P-1+P-2+P-3 all converge per AR-S203-2 lesson).
- C-3 (KNOT-4): events are inert at v1; no auto-cascade — invalidates-assumption does NOT auto-set assumption_ledger.status='invalidated' (P-1+P-2+P-3 all converge per codex named edit #4 + S203 cycle no-auto-SR precedent).
- C-4 (KNOT-5): defer supersession_ledger.origin_event_id forward-FK to v2 (P-1+P-2+P-3 all converge per codex named edit #5; S197 deferral preserved).
- C-5 (KNOT-6): alias EV-S<wno>-<seq> per row + object_kind='event' (drops _ledger suffix per DV-S198-1 P-1 stance precedent) (P-1+P-2+P-3 all converge per codex named edit #1).
- C-6 (KNOT-8): required event_time_atom + source_atom + claim_atom on event_ledger header (P-1+P-2+P-3 all converge per codex named edit + KNOT-8 universal).
- C-7 (cross-cutting): atom 8-480 char support_claim tier per OI-S177-1 widening; mirrors AR/SL/CYC precedent.
- C-8 (cross-cutting): no event-update kind at v1; events are append-only sealed claims (P-1+P-2 explicit; P-3 implicit).

**Divergence.**
- D-1 (KNOT-2 enum cardinality at v1): P-1 2-value tight {invalidates-assumption, confirms-assumption} only-existing-target-kinds vs P-2 4-value middle {invalidates-assumption, confirms-assumption, supersedes-claim, raises-concern} cross-app preparatory vs P-3 codex 6-value with node+risk+resolution-path kinds whose targets do not resolve. Adopted: P-1 2-value tight per AR-S203-1 + AR-S203-2 lessons. P-2 4-value preserved as M-1 minority watch-trigger. P-3 6-value preserved as M-2 minority watch-trigger + forward-direction.
- D-2 (KNOT-7 v1 allowlist): P-1+P-3 codex bounded-allowlist {assumption} (D-1 implies this) vs P-2 broader-allowlist {assumption, decision_v2, supersession_ledger, cycle}. Adopted: assumption-only at v1 per D-1 synthesis. P-2 wider-allowlist preserved as M-1 minority watch-trigger.

**Minority preserved.**
- M-1 P-2 4-value enum + wider allowlist {assumption, decision_v2}: if calibration-EFs across N>=3 future sessions surface attempted-but-refused supersedes-claim or raises-concern shapes mapping to existing-decision_v2-or-supersession_ledger targets, gate-promotion OI for enum widening + per-kind coupling extension. Substrate-canonical pattern: T-43 trigger refusals with target_kind not in allowlist hint surface in calibration-EFs.
- M-2 P-3 codex 6-value enum + node/risk/resolution-path target kinds: if Selvedge engine introduces typed node/risk/resolution-path primitives in future sessions OR an external-application substrate registers these object_kinds, gate-promotion OI for full 6-value codex enum widening per the original codex shape-consult position.
- M-3 codex blind-spot — auto-cascade alternative: if calibration-EFs surface external-application demand for handler-side cascade semantics (e.g., compliance-application requiring invalidates-assumption to auto-flip AR.status), gate-promotion OI for cascade-handler shape (P-3 codex blind-spot self-named).

**Counterfactual dispositions.**
- CF-1 ship codex 6-value enum verbatim with refuse-on-target-kind-absence: addressed-in-synthesis preserved-as-divergence M-2 watch-trigger (rejected at v1 basis=premature-substance-without-evidence per AR-S203-1).
- CF-2 ship single-table denormalized event header with N effects as JSON or repeated columns: nilled-by-exclusion barred-by-constraint (codex KNOT-1 + universal P-1+P-2+P-3 convergence + 1:N normalization invariant).
- CF-3 auto-cascade invalidates-assumption to AR.status='invalidated': addressed-in-synthesis preserved-as-divergence M-3 watch-trigger.
- CF-4 ship origin_event_id forward-FK on supersession_ledger this session: nilled-by-exclusion out-of-scope (codex named edit #5 universal convergence; S197 deferral preserved).
- CF-5 typed temporal column (TIMESTAMP or INT epoch) instead of free-text event_time_atom: nilled-by-exclusion barred-by-constraint (text_atoms invariant + DR-arc T+Nh format heterogeneity bars typed column premature commitment).

**Bias-toward-build-now applied per EF-S196-2 bounded-scope binding.** Codex SHIP-WITH-NAMED-EDITS verdict from EF-S204-1 honored on 5 of 5 named edits + 6 of 6 universal-convergence knots; departure on enum cardinality at v1 explicitly reasoned via AR-S203-1 + AR-S203-2 lessons surfaced at deliberation-open. Codex blind-spots flagged in EF-S204-1 preserved as M-2 + M-3 watch-triggers per Selvedge own-precedent counter-weight discipline.


### Synthesis points

- **convergence C-1.** two tables event_ledger header + event_effects child; 1:N pattern (codex KNOT-1 universal convergence)
- **convergence C-2.** polymorphic target_object_id via objects + T-43 SQL trigger for effect-kind to target object_kind coupling per AR-S203-2 lesson
- **convergence C-3.** events inert at v1; no auto-cascade; codex named edit #4 + S203 cycle no-auto-SR precedent
- **convergence C-4.** defer supersession_ledger.origin_event_id forward-FK to v2; codex named edit #5 + S197 deferral preserved
- **convergence C-5.** alias EV-S<wno>-<seq> + object_kind=event drop _ledger suffix per DV-S198-1 P-1 precedent; codex named edit #1
- **convergence C-6.** required event_time_atom + source_atom + claim_atom on event_ledger header; codex KNOT-8 universal
- **convergence C-7.** atom 8-480 char support_claim tier per OI-S177-1 widening mirroring AR/SL/CYC precedent
- **divergence D-1.** KNOT-2 enum cardinality at v1: P-1 2-value vs P-2 4-value vs P-3 codex 6-value; adopted P-1 2-value tight per AR-S203-1 polymorphism-shape-without-substance
- **divergence D-2.** KNOT-7 v1 allowlist: assumption-only (P-1+P-3) vs broader [assumption, decision_v2] (P-2); adopted assumption-only per D-1 synthesis
- **minority M-1.** P-2 4-value enum + wider allowlist watch-trigger: N>=3 calibration-EFs surface attempted-supersedes-claim or raises-concern shapes opens enum widening OI
- **minority M-2.** P-3 codex 6-value enum forward-direction: when node/risk/resolution-path primitives ship OR external-app substrate registers them, gate-promotion OI for full codex enum
- **minority M-3.** auto-cascade alternative watch: external-app demand for handler-side cascade semantics opens cascade-handler shape OI per codex blind-spot self-named
