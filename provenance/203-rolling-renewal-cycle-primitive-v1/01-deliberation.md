---
session: 203
title: rolling-renewal-cycle-primitive-v1 — deliberation
generated_by: selvedge export
---

# Deliberation

## D-9 — cycle_ledger v1 shape: locus + suppression + polymorphic-allowlist + classifier + closure-path-reuse

sealed_at: 2026-05-04T21:27:59.695Z

### P-1 (anthropic)

**Position.** Ship cycle_ledger v1 as AR-child-only typed primitive: FK to assumption_ledger constrained to sub_type='rolling-renewal', no objects-FK polymorphism, no cycle_trigger, reuse closure_shape; defer v2 until 2nd-app evidence.

**schema_sketch.**
- cycle_ledger(cycle_id PK, session_id FK, assumption_id FK NOT NULL, cycle_index INTEGER NOT NULL, substantial INTEGER NOT NULL CHECK substantial IN (0,1))
- substantial_basis_atom_id FK NOT NULL when substantial=1 else NULL; handler-side actionable refusal mirrors DV-S198-1 four-field-discipline pattern
- supersession_cite_object_id FK NULL admits SL-S<wno>-<seq> only when substantial=1 and a real supersession edge exists per codex knot 3
- snapshot_body_atom_id FK NULL: optional body-field snapshot per DV-S011-5 24h-rolling-renewal pattern
- CHECK at INSERT enforced via handler: assumption_ledger.sub_type must equal 'rolling-renewal' (handler-side not pure SQL because sub_type is mutable)
- UNIQUE (assumption_id, cycle_index) prevents duplicate cycle observations
- cycle row IS proof-of-observation per knot 3; non-substantial cycles emit no SL
**cli_surface.**
- bin/selvedge submit cycle --assumption AR-S<wno>-<seq> --cycle-index N --substantial 0|1 [--basis ATOM] [--cite SL-...]
- alias CYC-S<wno>-<seq> registered in objects with object_kind='cycle' via T-15-CALIBRATED rebuild widening enum per DV-S198-1 + DV-S197-1 precedent
- no query subcommand at v1; same posture as DV-S198-1 no-CLI-query-at-v1 convergence point C-6
**migration_path.**
- migration 052: CREATE TABLE cycle_ledger STRICT + role_write_capabilities INSERT + T-15-CALIBRATED rebuild of objects to admit object_kind='cycle' + engine v56-to-v57
- handler selvedge/submit/cycle.py: alias-resolution + sub_type='rolling-renewal' guard + atom 8-480 support_claim per OI-S177-1 + UNIQUE refusal + actionable error text
- if v2 promotes to polymorphic: rename to object_ref_id + widen enum allowlist via T-15 rebuild; DV-S198-1 ledger-rebuild precedent makes this cheap and known-safe
**what_not.**
- NO objects-FK polymorphism at v1 (codex knot 1 + 6 divergence): allowlist-of-1 is shape-without-substance per DV-S201-1
- NO typed cycle_trigger rows at v1; handler-computed counter via COUNT(*) on cycle_ledger WHERE assumption_id=? AND substantial=1 sufficient for 3-consecutive trigger
- NO diff metadata at v1: pure agent-judged-with-cite simpler than codex hybrid; engine should not pretend to mechanically derive significance
- NO new closure_path enum (knot 5 convergence with codex): reuse C-3 closure_shape on parent assumption_ledger row
- NO cross-artefact rollout at v1: EF-S196-2 bounded-scope binding does not authorize speculative generalization on projected-not-evidenced grounds
**open_question.**
- If v2 surfaces a 2nd application (e.g., subscription-renewal) does AR-child-only constraint refuse-loudly enough to surface gap, or silently reshape data to fit? Watch-FR candidate.
- Does sub_type='rolling-renewal' guard need SQL-level trigger or is handler-actionable sufficient? Same question DV-S198-1 resolved via handler-first.
**risk.**
- v2 rename cost if AR-child-only proves too narrow: mitigated by T-15-CALIBRATED rebuild precedent (migrations 048+049+051 all widened ledger enums cheaply)
- AR-S202-1 cross-application generalization stays projected-not-evidenced for longer; acceptable per S198 status-mutation drift watch-FR-then-promote pattern
- Codex divergence on knots 1+6 must be preserved as M-1 minority watch-trigger (2nd-app evidence opens v2 polymorphism gate)
**what_lost.**
- Up-front polymorphic flexibility codex argued for: substituted with cheap-rebuild-when-evidenced posture per DV-S198-1
- Trigger-counter inspectability as typed rows: substituted with handler-computed view; if N-cycle reasoning becomes opaque, calibration-EF surfaces it and v2 promotes
- Any pretense that disaster-recovery to general renewal is a mechanical generalization: codex blind-spot (a) correct that stability-itself-is-signal but that is a v2 question after stability-domain application exists
**cli_surface.**
- bin/selvedge submit cycle --assumption AR-S<wno>-<seq> --cycle-index N --substantial bool [--basis ATOM] [--cite SL-...]

### P-2 (anthropic)

**Position.** Operator-named AR-S202-1 (future apps not all disaster-recovery) is load-bearing not aspirational; ship polymorphic-via-objects-FK with allowlist {assumption,issue,decision_v2} at v1 mirroring DV-S197-1; converge on knots 2,3,4,5.

**schema_sketch.**
- Standalone cycle_ledger table with primary_object_id FK to objects (polymorphic), object_kind admit-list CHECK in (assumption,issue,decision_v2)
- Alias CY-S<wno>-<seq> registered in objects with object_kind=cycle per DV-S197-1 + DV-S198-1 precedent
- Required: cycle_no INT, observed_at TS, substantial BOOL, classification_reason atom_text 8-480 chars
- Optional: prior_cycle_id self-FK for cycle-chain reachability, cite_object_id pointing to SL row when substantial=true cites real supersession
- Typed cycle_trigger child table per knot 4 codex stance: trigger_kind enum, count INT, computed_at TS
- Closure via parent's closure_shape FK lookup at query time; no cycle-local closure column at v1
**cli_surface.**
- selvedge submit cycle --primary-object AR-... --cycle-no N --substantial true --reason '...' --observed-at ...
- Read-only at v1: agent runs ad-hoc query for cycle reachability; no dedicated CLI query subcommand
**migration_path.**
- Migration 052 STRICT, T-15-CALIBRATED rebuild of objects to widen object_kind CHECK admitting cycle
- role_write_capabilities INSERT for cycle_ledger + cycle_trigger inline in 052
- Engine version v56 to v57; spec amendment SPEC-prompt-development v8 in-session per DV-S197-1 + DV-S198-1 + DV-S201-1 precedent
- No backfill: A-018/A-020 disaster-recovery cycles stay in body-field snapshots until calibration-EF demand surfaces (M-3 watch)
**what_not.**
- No close_records in allowlist at v1 (separate close-ceremony gate; cycles do not gate close)
- No standalone-with-optional-FK (codex 1.A): primary_object_id NOT NULL, polymorphism IS the contract
- No closure_path enum forking from closure_shape (codex stance honored on knot 5)
- No substrate-detected substantial classifier without cite (codex blind-spot: snapshots bias toward operational allocations)
- No classification_reason enum at v1 (free-text atom; enum surfaced as M-1 watch-trigger for v2)
**open_question.**
- Does primary_object_id FK to objects require object_kind admit-list as cross-column CHECK or handler-side validation? Mirror DV-S197-1: handler resolves alias and validates object_kind before INSERT for actionable refusal.
**risk.**
- Premature polymorphism: zero issue/decision_v2 cycles materialize across N>=5 sessions (M-2 watch-trigger calibration-EF; narrow-to-assumption-only as v2 retrospective)
- Allowlist drift: future demand for close_records/spec_versions cycles arrives without typed admit path (M-3 watch; ALTER CHECK migration cheap but spec amendment cost real)
- Cited stability blind-spot recurrence: free-text classification_reason admits 'stable' but agents under-cite (M-1 watch; promote to enum at v2 if calibration-EF surfaces)
**what_lost.**
- Codex narrow-allowlist=assumption-only ships smaller v1 surface and defers polymorphism to evidence-gated v2; my stance accepts wider blast radius now to honor AR-S202-1 explicitly
- Codex standalone-with-optional-FK preserves cycles unattached to any parent; my stance loses 'orphan cycle' use case but gains chain-walk reachability invariant from day one
- classification_reason enum at v1 (P-1 schema-minimality stance would prefer typed-from-day-one); deferred to v2 as M-1 watch
- Substrate-detected substantial classifier rejected by codex blind-spot-(b); my convergence accepts the loss
**cli_surface.**
- selvedge submit cycle-trigger --cycle CY-... --kind closed-enum

### P-3 (openai)

**Position.** Knots are implementation-shaping not discovery-blocking; ship standalone cycle_ledger with required primary-object FK polymorphic via narrow allowlist, cycle row IS proof-of-observation, reuse closure_shape; AR-only is wrong abstraction.

**schema_sketch.**
- Standalone cycle_ledger table not assumption_ledger child; required subject_object_id FK to objects.object_id with narrow object_kind allowlist
- Required cycle_no monotonic per subject via UNIQUE(subject_object_id, cycle_no) with no +1 strict-monotonic enforcement
- Required snapshot_atom_id FK to text_atoms 8-480 char closed CHECK length
- Closed CHECK enum classification IN (substantial, non-substantial); classification_reason_atom_id required when substantial=true via row CHECK
- Optional citing_supersession_object_id FK to objects.object_id resolving SL alias when supersession relation exists
- Required observed_at TEXT default strftime ISO timestamp; required session_id + seq for CYC-S<wno>-<seq> alias
**cli_surface.**
- bin/selvedge submit cycle --payload with subject + snapshot + classification + optional reason + optional citing_supersession + optional cycle_no override
- Handler refusal codes E_VALIDATION + E_REFUSAL_T01 alias-resolve + E_ATOM_LENGTH + E_REFUSAL_CHECK closed-enum + E_REFUSAL_ALLOWLIST object_kind not admitted
- No new query subcommand at v1; bin/selvedge query covers cycle reads
**migration_path.**
- Migration 052 STRICT cycle_ledger create + objects.object_kind CHECK admit cycle + role_write_capabilities INSERT inline + 4 column indexes
- T-15-CALIBRATED rebuild of objects table widening object_kind CHECK; trigger drops/recreates per S197/S198/S201 precedent
- engine_version v56-to-v57 bump in workspace_metadata + test_engine_v52_marker update
**what_not.**
- No typed cycle_trigger child rows at v1; defer to v2 via calibration-EF graduation when N-cycle reasoning becomes load-bearing
- No closure_shape column on cycle_ledger; reuse parent assumption's closure_shape via FK lookup at query time per DV-S201-1 no-premature-unification binding
- No substrate-detected diff metadata at v1; substantial classifier purely agent-judged-with-cite, no engine-side state-snapshot comparison
- No history-table for cycle status changes; cycles are append-only by construction (UNIQUE on (subject, cycle_no) prevents replacement)
**open_question.**
- Allowlist scope at v1: assumption-only is conservative read of 2-case A-018+A-020 evidence; broader [assumption, issue, decision_v2] is operator-named cross-app speculation
- Cycle_no monotonic strict (+1) vs UNIQUE-only: agents may skip numbers; do we refuse or admit?
- citing_supersession FK directionality: cycle cites SL or SL cites cycle? Cycle-cites-SL avoids dual-channel confusion
**risk.**
- Disaster-recovery framing biases substantial-classifier toward improvement/worsening trajectories; many cross-app cycles classify stability-confirmed as substantial
- Snapshot atom 8-480 may be too narrow for compliance attestation context (reviewer identity + policy version + evidence cite); operators may push for typed snapshot at v2
- AR-only allowlist at v1 risks codifying disaster-recovery as canonical shape; calibration-EF surface point if cross-app lands without polymorphism extension
**what_lost.**
- Mechanical state-diff classifier shape at v1 (engine-detected substantial via snapshot diff): too speculative pre-evidence; defer
- Typed cycle-specific closure_path enum disjoint from closure_shape: would prematurely fork closure semantics
- Hard-cutover from sub_type='rolling-renewal' channel: legacy assumption_ledger.sub_type stays admissible, cycle_ledger is new-write surface, dual-channel watch per S197 precedent

### Synthesis

## Synthesis (S203 D-9, cycle_ledger v1)

**Adopted shape: codex P-3 middle ground.** Standalone cycle_ledger table polymorphic via objects-FK with assumption-only allowlist at v1; cycle row IS the proof of observation; non-substantial cycles emit no supersession_ledger row; reuse closure_shape from DV-S201-1 (no own column on cycle_ledger); typed cycle_trigger rows deferred to v2; cited-only substantial classifier (P-1+P-3 simpler over P-3 hybrid-with-diff-metadata).

**Convergence.**
- C-1 (knot 3): cycle row IS proof of observation (P-1+P-2+P-3 all converge); non-substantial cycles emit zero SL rows; substantial cycles MAY cite SL via optional FK when supersession relation exists.
- C-2 (knot 5): reuse closure_shape from S201 (P-1+P-2+P-3 all converge); cycle_ledger does not carry own closure_shape column at v1 per DV-S201-1 no-premature-unification binding; closure semantics live on parent assumption.
- C-3 (knot 4): defer typed cycle_trigger rows to v2 (P-1+P-2+P-3 all converge); v1 triggers are query-time at agent reasoning; calibration-EF graduation per DV-S152-1 typed-observation pathway.
- C-4 (knot 1 partial): standalone cycle_ledger table not assumption_ledger child column (P-2+P-3 converge; P-1 prefers AR-FK but accepts standalone-table-shape).
- C-5 (cross-cutting): atom 8-480 char range for snapshot + classification_reason (support_claim atom_type tier per OI-S177-1 widening; all-perspectives converge on tier).
- C-6 (cross-cutting): alias scheme CYC-S<wno>-<seq> per session; object_kind='cycle' (drop _ledger suffix per DV-S198-1 P-1 stance precedent).

**Divergence.**
- D-1 (knot 6 polymorphism cardinality at v1): P-1 AR-only (cycle_ledger.assumption_id FK direct, not polymorphic) vs P-3 polymorphic-with-assumption-only-allowlist (objects-FK with object_kind CHECK at v1) vs P-2 polymorphic-with-broad-allowlist [assumption, issue, decision_v2]. Adopted: P-3 middle ground per codex priority-ordering load-bearing knot-6 + DV-S197-1 polymorphism precedent + AR-S202-1 cross-app generalization signal.
- D-2 (knot 2 substantial classifier shape): P-1 cited-only-simpler vs P-2+P-3 hybrid-cited (free-text reason atom + optional diff metadata). Adopted: P-1+P-3 simpler stance — cited-only with no engine-side diff metadata at v1 per ceremony-subtraction; P-2+P-3 hybrid preserved as forward-direction.
- D-3 (knot 1 mechanism): P-1 AR-FK direct (cycle_ledger.assumption_id INTEGER NOT NULL REFERENCES assumption_ledger) vs P-2+P-3 objects-FK polymorphic. Adopted: objects-FK polymorphic per D-1 synthesis; AR-FK preserved as M-1 minority watch-trigger.

**Minority preserved.**
- M-1 P-1 schema-minimality AR-child-only stance: if calibration-EFs surface that v1's polymorphism-with-assumption-only-allowlist is shape-without-substance (zero non-assumption subjects across N>=5 sessions OR allowlist-extension blocked by non-trivial subject_kind-specific semantics), the next session opens a gate-promotion OI for AR-FK direct table refactor.
- M-2 P-2 broader-allowlist [assumption, issue, decision_v2] stance: if calibration-EFs surface cross-app cycles attempting to register under non-allowlist subject_kind (issue cycles for compliance review, decision_v2 cycles for ML calibration) across N>=2 sessions, the next session opens a gate-promotion OI for allowlist extension migration.
- M-3 hard-cutover (CF-1 surfaced position): if dual-channel writes persist (assumption_ledger.sub_type='rolling-renewal' rows continuing while cycle_ledger ships) OR cycle_ledger receives 0 inserts across N>=5 sessions, gate-promotion OI for hard-cutover migration deprecating sub_type='rolling-renewal' channel per S197 dual-channel-watch precedent.

**Counterfactual dispositions.**
- CF-1 hard-cutover: addressed-in-synthesis preserved-as-divergence M-3 watch-trigger.
- CF-2 substrate-detected classifier via state-diff: nilled-by-exclusion out-of-scope (knot 2 deferred to v2 per codex priority-ordering).
- CF-3 cycle-specific closure_path enum: nilled-by-exclusion barred-by-constraint (DV-S201-1 no-premature-unification + closure_shape adoption per C-2).

**Bias-toward-build-now applied per EF-S196-2 bounded-scope binding.** Codex SINGLE-SHIP verdict from S202 EF-S202-1 honored at this coding session; meta-then-coding 2-session arc preserved provenance per DV-S202-1 R-1.1 rejection.

### Synthesis points

- **convergence C-1.** cycle row IS proof of observation; non-substantial emits zero SL; substantial may optionally cite SL via FK
- **convergence C-2.** reuse closure_shape from DV-S201-1; no cycle_ledger.closure_shape column; closure semantics on parent assumption
- **convergence C-3.** defer typed cycle_trigger to v2; v1 triggers are agent-query-time; calibration-EF graduation pathway
- **convergence C-4.** standalone cycle_ledger table not assumption_ledger child column; P-2+P-3 fully converge P-1 accepts table-shape
- **convergence C-5.** alias scheme CYC-S<wno>-<seq>; object_kind=cycle drop _ledger suffix per DV-S198-1 P-1 precedent
- **divergence D-1.** knot 6 polymorphism cardinality: P-1 AR-only vs P-3 polymorphic-assumption-only-allowlist vs P-2 broad allowlist; adopted P-3
- **divergence D-2.** knot 2 classifier: P-1+P-3-simpler cited-only vs P-2+P-3-hybrid free-text+diff-metadata; adopted simpler stance
- **minority M-1.** P-1 AR-child-only watch-trigger: zero non-assumption subjects across N>=5 sessions opens AR-FK direct refactor OI
- **minority M-2.** P-2 broader-allowlist [issue, decision_v2]: cross-app cycles under non-allowlist subject_kind across N>=2 opens extension OI
- **minority M-3.** hard-cutover CF-1: dual-channel persistence OR zero ledger inserts N>=5 opens hard-cutover migration OI per S197 precedent
