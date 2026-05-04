---
session: 198
title: typed-assumption-ledger-primitive — deliberation
generated_by: selvedge export
---

# Deliberation

## D-6 — OI-S196-1 typed-assumption-ledger v1 schema and submit-kind shape

sealed_at: 2026-05-04T11:17:27.798Z

### P-1 (anthropic)

**Position.** Ship smallest primitive: one row per assumption, 6-status enum, NULL-or-enum sub_type, four conflict atom-FKs optional with CHECK when status=active-with-conflict, AR-S<wno>-<seq> alias. Reject 9-status enum and history table at v1.

**schema_sketch.**
- assumption_ledger STRICT table: assumption_id PK, session_id FK, object_id FK, claim_atom_id FK, status TEXT CHECK 6-value enum, sub_type TEXT NULL CHECK 3-value, four conflict atom-FK columns NULL-admitted.
- Status closed enum: unverified, assumed, active-with-conflict, closed, superseded, invalidated. Six values cover every transition the disaster-recovery arc actually fires.
- Sub_type closed enum NULL or in {plan-vs-resource, contested-authority, rolling-renewal}. Single column, sparse. NOT NULL only when status=active-with-conflict via single CHECK.
- Single CHECK enforces all four conflict atom-FK columns NOT NULL plus sub_type NOT NULL when status=active-with-conflict; otherwise all NULL admitted.
- Atom length 8-480 via support_claim tier (matches S197 precedent). object_kind admitted to objects CHECK. UNIQUE(object_id) implicit via 1:1 with objects row.
- Explicitly omit assumption_status_changes history table; recoverable from decisions_v2 closes/supersedes effects via replay walk.
- Omit monitored, unknown, worst-case-assumed status values; commentary-shaped not state-machine-shaped.
- Omit last_status_change_at and last_status_change_decision_id columns; recoverable via objects + decision_supports JOIN.
- Omit any TEXT escape-hatch on sub_type or status; matches DV-S197-1 R-1.6 bar against JSON/TEXT relation_metadata escape.
**cli_surface.**
- bin/selvedge submit assumption: required claim_atom (8-480), status default assumed, session_id; optional sub_type plus four atoms; engine assigns AR-S<wno>-<seq> alias.
- Assumption submit refuses E_REFUSAL_T-39 if status=active-with-conflict and any of the five required-when-conflict fields (sub_type plus four atoms) missing.
- bin/selvedge submit assumption-status-update: required assumption_alias, new_status, citing_decision_v2_alias; refuses if cited decision not closed or transition not reachable (E_REFUSAL_T-40).
- Status changes that cite a sealed decision are the audit trail; no separate history-write required.
- No bin/selvedge query assumption surface at v1; reads use existing query CLI over objects plus JOINs, mirroring S197 R-no-CLI-query M-2 minority.
- Refusal codes: T-39 conflict-discipline incomplete, T-40 illegal status transition or unsealed citation, reuse T-01 unresolvable alias, atom-length already covered.
**migration_path.**
- v1 to v1.1: if rolling-renewal pressure produces measurable need for per-renewal snapshots, add assumption_renewal_observations as a SECOND table; keep parent row tight.
- v1 to v1.2: if status-history queries become hot AND replay-via-decisions proves insufficient, add assumption_status_changes ONLY THEN; shape parallel to supersession_ledger.
- v1 to v1.3: enum widening (e.g. admit monitored if second-arc evidence) is single-line CHECK rebuild migration; no row rewrite required.
- v1 to v2: discriminated sub_type-per-status sub-tables only if cross-status sub_type bleed becomes a real bug; not anticipated.
**what_not.**
- Reject 9-status closed enum. Specifically reject monitored (synonym for assumed plus active observation), unknown (collapses to assumed/unverified), worst-case-assumed (stance in claim_atom prose not state).
- Reject assumption_status_changes table at v1; audit trail already exists as decisions_v2 plus decision_supports plus effects against object_id. Separate history table doubles writes and invites dual-channel watch-trigger.
- Concede codex two-handler split for assumption-insert vs assumption-status-update (different required fields), but reject the history table that would make handler-versioning matter.
- Reject per-status sub_type sub-tables. One column, sparse, NULL admitted is the v1 shape.
- Reject atom-typing beyond support_claim. The four conflict-discipline atoms do not need a new atom_type; semantics live in column names.
**open_question.**
- Should claim_atom be UNIQUE(object_id) or admit multiple atoms per assumption? v1 vote: one claim atom; additional context lives in support atoms on the registering decision.
- object_kind=assumption_ledger or just assumption? Vote: assumption — the _ledger suffix in S197 was post-hoc and table-name redundancy adds no signal.
- Status closed-set: should closed be reachable directly from active-with-conflict, or route through superseded/invalidated? Arc evidence (DV-S014-1) suggests direct closed reachable.
- When a decision both opens an assumption and immediately marks it active-with-conflict (DV-S011-5 pattern), is that one submit or two? Vote: one submit at insert with four atoms required.
**risk.**
- If second arc produces a status the six-value enum cannot accommodate, pay one CHECK rebuild migration. Cost: small, well-precedented (S197 did this for 5-value relation enum).
- If status-history queries become hot, agents may reach for nonexistent assumption_status_changes table. Mitigation: citing_decision_v2_alias on each update IS the history; query is a JOIN.
- Sparse NULL columns for four conflict-discipline atoms invite use outside active-with-conflict context. Mitigation: CHECK enforces all-NULL when status<>active-with-conflict.
**what_lost.**
- Codex 9-status enum carries finer-grained agent-readability (monitored vs assumed semantic signal). Engine pays for it as attention-budget-on-status-noise instead of attention-on-claim-prose.
- Dedicated status_changes table makes show-me-every-status-change-in-last-N-sessions a one-table scan. Forgo that for the JOIN cost.
- Codex two-handler split makes insert and status-update payload schemas independently versionable; half-conceded (keep two handlers) but reject the history table that would make versioning matter.
- Worst-case-assumed as distinct status carries real disaster-recovery semantic; bury it inside claim_atom prose at v1, costing some retrieval ergonomics for what is judged commentary not state.

### P-2 (anthropic)

**Position.** Close §8.5 AR primitive at session-close: typed handler, AR-S<wno>-<seq> alias, object-registration, 4-field CHECK, 9-status enum, 3-sub-type enum. Workspace-scope; do not displace L4. Transitions via supersession_ledger, not UPDATE.

**schema_sketch.**
- assumption_register STRICT: assumption_id PK, body_atom_id FK text_atoms, sub_type CHECK closed-3, status CHECK closed-9, origin_session_id FK sessions, sealed_at TEXT, object_id FK objects.
- Sub-types closed enum: interpretive_choice (close-time audit lift; primary v1 consumer), prospective_scoping (hooks OI-S196-5), external_input_admission (disaster-recovery rolling-renewal use case).
- Status closed 9-value enum: proposed, active, active-with-conflict, superseded, retracted, invalidated, deferred, accepted-implicit, nilled-by-exclusion. Engine-self needs active, accepted-implicit, superseded day one.
- Status transitions write supersession_ledger row using relation_kind in {supersedes-fully, bounded-by, retracted-by}. No state column mutation; transitions are append-only typed edges.
- Four-field CHECK: status NOT NULL AND sub_type NOT NULL AND body_atom_id NOT NULL AND origin_session_id NOT NULL. Refuses ambiguous half-rows like DV-S197-1 CHECK refuses self-supersession.
- Object-registration: every row registers in objects with object_kind=assumption_register and alias AR-S<wno>-<seq>; rebuild objects.object_kind CHECK in same migration mirroring 048 pattern.
- Reason-atom uses support_claim atom_type per OI-S177-1 widening (8-480 chars); same length budget as supersession reason.
**cli_surface.**
- bin/selvedge submit assumption with payload sub_type, body, status returns alias AR-S<wno>-<seq> and object_id. Default status=active; accepted-implicit allowed at submit so audit-step EF can encode disposition.
- origin_session_id defaults to the open session, mirroring _atom_session_id resolution in supersession.py handler.
- Audit-step workflow: (1) submit assumption row capture alias; (2) submit engine_feedback audit-step row citing AR alias; (3) future revisions via fresh assumption + supersession-ledger row. No new transition kind.
- Refusals: E_VALIDATION for missing body or bad enum values; E_ATOM_LENGTH for body outside 8-480; no E_REFUSAL_T<N> at v1 (§8.5 clause is operator-policed today).
**migration_path.**
- v2 admits external_input_admission as primary consumer and adds nullable arc_id FK once arc-primitives land (currently absent; do not invent at v1).
- v2 adds bin/selvedge query --register surface for rolling-renewal listing once second arc demonstrates need; DV-S190-2 graduation-discipline still applies for read CLIs.
- v2 may add confidence column or evidence_atom_id; v1 punts to keep audit-step lift cheap (480-char body suffices). Adding optional columns later is non-breaking.
- v3 may admit cross-register conflict edges via a fifth relation_kind in supersession ledger if 5-value enum proves under-shaped.
**what_not.**
- No status-mutation column at v1; transitions go through supersession_ledger exclusively. Rejects R-1 mutable-status on same grounds DV-S197-1 R-1.6 rejected JSON escape hatches.
- No new alias scheme; reuse AR-S<wno>-<seq> workspace-scoped, mirroring SL-S<wno>-<seq> and DV-S<wno>-<seq>. Reject any global A-NNN numbering.
- No FK to reference_harness_assumptions. The L4 table is harness-sealed-immutable; the register is workspace-scope. Two tables, two purposes.
- No cross-arc auto-import of legacy markdown A-NNN rows from disaster-recovery; DV-S189-1 markdown-only-recovery binds against synthetic-row backdating.
- No CLI query surface at v1; P-3 M-2 minority from DV-S197-1 generalises here.
**open_question.**
- Should accepted-implicit rows be admitted to assumption_register at all, or stay as inline EF body text only? v1 admits them so audit-step EF can cite a real alias; cost is more rows. Admission is optional not mandatory.
- Should spec amendment fold §8.5 clause A-NNN shorthand into AR-S<wno>-<seq> literally, or leave clause text alone? P-2 view: amend in-session per DV-S197-1 precedent.
**risk.**
- Engine-self under-readiness: if v1 ships without object-registration or citable alias from EF body_md, next audit-step EF cannot cite real AR alias and §8.5 clause stays referentially broken. Highest-priority risk.
- Schema-creep into application-arc shapes too early: if v1 admits arc_id or confidence to satisfy hypothetical second arc, columns become required-in-handler-validation but non-load-bearing for engine-self use.
- Status-mutation drift: if v1 admits UPDATE path for status, engine grows hidden mutation surface bypassing chain-walk reachability — same failure mode P-3 named in DV-S197-1 R-1.6.
**what_lost.**
- A frictionless multi-arc rolling-renewal interface; v2 must add it.
- A unified A-NNN scheme matching disaster-recovery markdown convention; v1 uses AR-S<wno>-<seq> instead, preserving substrate alias discipline at cost of clause-text re-amendment.
- Mutable-status ergonomics for application authors who want to flip an assumption state in-place; v1 forces supersession-ledger detour, more verbose but typed.

### P-3 (openai)

**Position.** VERDICT SHIP-WITH-NAMED-EDITS. Adopt 9 disaster-recovery base statuses; 3 active-with-conflict sub-types closed. Ship assumption-status-update plus assumption_status_changes history table at v1 with 4-field discipline.

**schema_sketch.**
- 9-status closed CHECK enum: unverified, monitored, assumed, unknown, worst-case-assumed, active-with-conflict, closed, superseded, invalidated. The 9 disaster-recovery base statuses are the right v1 set.
- 3-value sub_type closed CHECK NULL or in {plan-vs-resource, contested-authority, rolling-renewal}. NOT NULL when status=active-with-conflict; NULL otherwise.
- Four conflict-discipline atom-FKs: action_commitment_atom_id, both_source_citation_atom_id, resolution_path_atom_id, expiry_trigger_atom_id. All NOT NULL when status=active-with-conflict via CHECK.
- Object-registration: alias AR-S<wno>-<seq>; row registers in objects with object_kind=assumption_ledger, similar to SL-S<wno>-<seq> for supersession_ledger at S197.
- Atom length 8-480 chars (support_claim tier per OI-S177-1 widening).
- Mandatory assumption_status_changes history table at v1: change_id PK, assumption_id FK, from_status, to_status, changed_at, origin_decision_object_id FK, basis_atom_id NULL, note_atom_id NULL.
**cli_surface.**
- bin/selvedge submit assumption (insert): required statement_atom, status, session_id; optional sub_type and four conflict atoms (NOT NULL via CHECK when active-with-conflict); optional verification atoms.
- bin/selvedge submit assumption-status-update (transitions): required assumption_alias, new_status, origin_decision_object_id; refusal if 4-field discipline incomplete when transitioning to active-with-conflict.
- Refusal codes: E_VALIDATION on missing fields/bad enum, E_REFUSAL_T01 on unresolvable alias, E_ATOM_LENGTH on atom outside 8-480, E_REFUSAL_CHECK on conflict-discipline incomplete.
**migration_path.**
- Object registration, alias uniqueness, closed status enum, conflict 4-field CHECK, status history table, and handler refusal when conflict status lacks four atoms ARE the primitive — not deferrable.
- Verification logs, rolling day-N snapshots, priority column, richer supersession trace fields, and subtype expansion CAN defer to v2.
- v2 promotion-trigger: real AR rows showing repeated need for verification-event granularity or additional conflict types.
**what_not.**
- No [P3] as status — that is priority overlay not lifecycle state. If priority is load-bearing add priority TEXT NULL CHECK in (high,medium,low) as separate column. Bias: omit unless DV-S008-1 receipts demand it.
- No other escape-hatch for sub_type. Closed enum plus future migration when evidence demands. Sparse is fine.
- No global A-NNN numbering — that is external-app phrasing from §8.5 and should be treated as prompt-development placeholder. Engine substrate stays in DV/EF/OI/FR/SL style.
**open_question.**
- Should §8.5 audit-step EF body shape be amended in-session to use AR-S<wno>-<seq> literally? P-3 view: yes; mirrors DV-S197-1 in-session spec amendment precedent.
**risk.**
- If status transitions go solely through supersession_ledger (M-1 minority), CLOSED/INVALIDATED/ACTIVE-WITH-CONFLICT become semantically split across two ledgers; audit readability weakens.
- If history table omitted, status field overwrites lose prior-state without indirect reconstruction via decisions_v2 walk; replay has higher cost.
- Formulaic-compliance failure: agents writing four-field atoms perfunctorily to satisfy CHECK; v2 promotion-trigger is exclusion-rationale shape checks (mirrors DV-S180-1 M-1 minority pattern).
**what_lost.**
- Strongest M-1 minority dissent codex preserves: ship insert-only and force later movement through supersession_ledger so C-1 stays pure immutable capture while C-2 owns temporal replacement. P-3 rejects: closure is not supersession.
- Also lost: external-app A-NNN shorthand readability; AR-S<wno>-<seq> requires §8.5 spec amendment.

### Synthesis

**Synthesis: ship typed-assumption-ledger v1 via 6-status closed enum + 3-value disaster-recovery sub-type set + four-field DV-S008-1 discipline + mutable-status with assumption-status-update kind + reject dedicated history table + AR-S<wno>-<seq> object_kind=assumption + atom 8-480 + bias-toward-build-now per EF-S196-2 closing OI-S196-1 by-mechanism in-session.**

**Convergence (3-of-3).** C-1 alias AR-S<wno>-<seq>. C-2 object-registration mandatory. C-3 four-field CHECK at SQL plus handler-side actionable refusal. C-4 atom 8-480 support_claim. C-5 closed CHECK enums; no TEXT escape hatch. C-6 no CLI query surface at v1.

**Divergence.** D-1 status enum cardinality 6 vs 9 vs 9 — adopt P-1 6-value (unverified, assumed, active-with-conflict, closed, superseded, invalidated); P-2/P-3 9-value sets preserved as M-2/M-3 minority. D-2 sub_type semantics conflict-elaboration vs use-case-discriminator — adopt P-1+P-3 conflict-elaboration; P-2 use-case framing preserved as M-1 minority. D-3 status mutation channel — adopt P-1 mutable status with assumption-status-update kind requiring citing_decision FK; reject P-3 history table (replay walks decisions_v2 + decision_supports + effects against assumption.object_id); P-2 supersession-only preserved as M-1 minority. D-4 object_kind name — adopt P-1 'assumption' (drop _ledger).

**Minorities.** M-1 P-2 supersession-only transitions: preserved for v2 if status-mutation drift surfaces. M-2 P-2 sub_type-as-use-case-discriminator: forward-direction. M-3 P-3 history table: v2 promotion-trigger if replay-via-decisions insufficient. M-4 P-1 single-handler-with-mode: conceded to two-handler split per payload schema legibility.

**Counterfactuals.** CF-1 ship-insert-only-via-supersession-only addressed-in-synthesis (closure is not replacement). CF-2 history-table-at-v1 nilled-by-exclusion barred-by-constraint per dual-channel watch-trigger from S197. CF-3 NULL-sub-type-at-conflict nilled-by-exclusion barred-by-constraint per DV-S008-1. CF-4 priority-column-for-P3-overlay nilled-by-exclusion out-of-scope.

**Bias-toward-build-now per EF-S196-2.** Ship v1 in S198. Codex EF-S198-1 6-edit verdict: 5 adopted, 1 rejected (history table), 1 out-of-scope deferred (priority).

**Spec amendment in-session per DV-S197-1 precedent.** §8.5 audit-step clause amended A-NNN -> AR-S<wno>-<seq>; surface new submit kinds; citing_decision FK on transitions.


### Synthesis points

- **convergence C-1.** AR-S<wno>-<seq> alias scheme converged across 3 perspectives; avoids assessment alias collision; workspace-scoped per substrate convention.
- **convergence C-2.** Object-registration mandatory; alias citable from EF body_md per chain-walks T-32 reachability mirroring SL-S<wno>-<seq>.
- **convergence C-3.** Four-field DV-S008-1 discipline at SQL CHECK plus handler-side actionable refusal; defense-in-depth per S197 self-supersession precedent.
- **convergence C-4.** Atom length 8-480 via support_claim atom_type per OI-S177-1 widening; matches S197 precedent.
- **convergence C-5.** Closed CHECK enums; no TEXT escape hatch; matches DV-S197-1 R-1.6 schema-correctness threshold bar.
- **convergence C-6.** No CLI query surface at v1; existing query CLI suffices until citation evidence demands; mirrors S197 R-no-CLI-query M-2.
- **divergence D-1.** Status enum cardinality: P-1 6-value vs P-2 9-engine-self vs P-3 9-disaster-recovery. Synthesis adopts P-1 6-value tighter set.
- **divergence D-2.** Sub-type semantics: P-1+P-3 conflict-elaboration disaster-recovery 3-value vs P-2 use-case-discriminator. Adopts P-1+P-3 conflict-elaboration.
- **divergence D-3.** Status mutation channel: P-1 mutable status-update vs P-2 supersession-only vs P-3 mutable plus history-table. Adopts P-1 mutable; rejects history-table.
- **divergence D-4.** Object_kind name: P-1 'assumption' vs P-3 'assumption_ledger'. Adopts P-1; future tables drop _ledger suffix.
- **minority M-1.** P-2 supersession-only transitions: preserved as v2 promotion-trigger if calibration-EFs name status-mutation drift.
- **minority M-2.** P-2 sub_type-as-use-case-discriminator: preserved as forward-direction if multi-axis discrimination becomes load-bearing.
- **minority M-3.** P-3 dedicated assumption_status_changes history table: preserved as v2 promotion if replay-via-decisions proves insufficient.
