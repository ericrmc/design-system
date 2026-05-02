---
session: 179
title: substrate-hardening-determinism-arc-open — deliberation
generated_by: selvedge export
---

# Deliberation

## D-28 — Substrate hardening + engine-determinism arc shape: which OIs ship as substrate-gate this session, sequencing, pre-decision context-injection design

sealed_at: 2026-05-02T07:22:50.029Z

### P-1 (anthropic)

**Position.** Convert every operator-named hardening gap into substrate via four sequenced migrations 032-035 shipping T-33..T-36 receipt-pattern gates this session; prose-and-discipline reproduces failure modes the kernel defends against (DV-S176-1).

**schema_sketch.**
- Migration 032 adds decision_prechecks table (precheck_id PK, session_id FK, target_kind, target_key, context_sha256, walker_version, UNIQUE(session_id,target_kind,target_key)) per chain-walks shape.
- Migration 032 adds NOT NULL backfill on decision_supports.cited_object_id for cite-required bases via T-15-CALIBRATED block closing OI-086-003 by-mechanism not by-policy.
- Migration 033 adds manifest_hash_seals table plus legacy_imports.decomposition_status ENUM column closing OI-S104-1 + OI-086-004; T-34 refuses session-close on manifest mismatch.
- Migration 034 adds UNIQUE(slug) to sessions plus engine_version_active view computed from migrations closing OI-S122-1 + OI-S091-1; T-35 refuses non-contiguous workspace_no per OI-S154-1.
- Migration 035 adds atom_type split rows (issue_disposition, issue_link separated from rejection_reason) plus harness_aliases registration closing OI-S088-1 + OI-S125-1; T-36 refuses cross-cite T-01 fail.
- Atom-length 240-char ceiling at OI-S177-1 forfeit this session per §1.5 narrow scope; cliff is real but repair requires methodology deliberation outside arc.
**cli_surface.**
- bin/selvedge precheck --target-kind --target-key prints similar prior decisions + active clauses + supersedes-graph + OI cluster and inserts decision_prechecks row verified at submit; refuses E_REFUSAL_T33.
- bin/selvedge precheck --print emits markdown to stdout per DV-S174-1 read/write separation; substrate row is the receipt, the print is presentation.
- bin/selvedge seal-manifest at close-time computes manifest sha256 over engine-manifest file set; T-34 refuses session-close without seal row for current session.
- No new flags on existing bin/selvedge submit decision-record; gate is handler-policed at submit-time exactly as T-32 was, no operator action required.
- bin/selvedge orient extension surfaces precheck-status for the next likely decision-target as a section, completing SHOW-CONTEXT loop without mutating substrate.
**migration_path.**
- S179 ships 032 first (precheck table + cite-traceability backfill) because T-33 depends on the table existing and cite-NULL backfill must precede gate-promotion to avoid retroactive refusal.
- S179 ships 033 second (manifest seal + decomposition_status) because T-34 close-gate runs against new column and OI-S104-1 forward-direction sealing is load-bearing for OI-S133-1 follow-on at S180.
- S179 ships 034 third (sessions UNIQUE + engine-version computed view) — independent of 032/033 substrate but logically belongs with determinism milestone; ship together for engine-v49 cohesion.
- S179 ships 035 fourth (atom_type split + harness alias registration) since OI-S088-1 conflation must be repaired before atom_type-keyed gates; harness-alias registration unblocks OI-S125-2 at S180.
- prompts/development.md v21->v22 adds §5.5 precheck-mandatory-before-decision-record clause, removes §5 recommended framing of precedent-sensitive (T-32 already substrate-gate), bumps engine to v49.
- One sealed deliberation D-28 (this session) covers the arc shape; per-migration review-loop iterations run inline within S179 not as separate deliberations.
**what_not.**
- Not OI-S177-1 atom-length ceiling repair — requires substrate-shape deliberation about whether to widen ceilings, split rows, or accept overflow-EFs; outside arc scope per scope discipline.
- Not OI-S145-1 SELVEDGE_EXPORT_CONTEXT auth-model — requires perspective convening on auth-model shape; defer to S180.
- Not OI-S154-4 perspective_claim.section_kind enum branch — schema deliberation on enum exhaustiveness belongs to its own deliberation D-29.
- Not OI-S159-1 sub-type verification — typed-observation closure semantics belong in DV-S152-1 graduation pathway, not in this hardening arc.
- Not the LLM-side context-injection (auto-fetching context via tool-use before submit) — substrate-side precheck row is sufficient instrumentation; LLM-side automation belongs to a future harness change.
- Not Group D OI-S130-1 conditional close-time temporal-claim lint — temporal-claim shape is unsettled and lint-policy belongs to a separate deliberation.
**open_question.**
- Q1: should decision_prechecks row be valid across multiple decision-records in the same session, or one-precheck-per-decision — depends on within-session staleness observability.
- Q2: should T-33 refuse on absent precheck or warn-and-proceed for procedural/calibration decision kinds — calibration EFs at audit-step:0 do not need context-walk.
- Q3: how does T-34 manifest-seal interact with mid-session migrations that legitimately bump engine_version — likely needs a re-seal handler before close.
- Q4: should the precheck CLI be invoked automatically at session-open as standing context-pull, or on-demand per decision — pre-session pull risks stale-cite refusal mid-session.
- Q5: zero-cite procedural decisions (audit-step:0 EFs) should they be exempt from precheck or carry an empty-precheck receipt — exempt is simpler but loses audit symmetry.
**risk.**
- T-33 false-positive: agent submits decision-record without precheck CLI; refusal blocks substantive work mid-session; recovery is precheck then resubmit, single-CLI roundtrip cost.
- T-33 stale-context: precheck row inserted at session-open, intervening decision changes context, decision-record references stale precheck; recovery is enforce-window predicate (last 30 minutes).
- T-34 manifest-mismatch: mid-session migration legitimately bumps version, close fails because seal predates migration; recovery is auto-reseal at close-time, refuse only on tampering signal.
- T-35 numbering-drift: legitimate workspace fork creates non-contiguous workspace_no; recovery is operator override flag with engine_feedback row recording the override.
- T-36 harness-alias-not-registered: legacy harness rows pre-035 lack object registration; recovery is one-shot bootstrap INSERT inside migration-035 transaction, no runtime refusal-debt.
- E_REFUSAL_T33 message must name exact precheck CLI invocation including target-kind and target-key per P-3 D-27 useful-refusal-text discipline; ambiguous refusals waste agent tokens.
**what_lost.**
- DV-S109-1 ceremony-subtraction discipline — this arc is maximal substrate addition since engine-v34, operator preclusion makes it non-rejection-basis; lost as default disposition rule going forward.
- DV-S152-1 typed-observation->gate progression — operator-named-mandate short-circuits recurrence requirement; typed-observation pathway becomes one promotion route among several rather than canonical.
- Atom-cliff calibration-EF stream — once T-33 forces precheck before decision-record submit, agent will hit atom-length cliffs at precheck claim text too; OI-S177-1 pressure rises post-arc.
- Single-session review-loop tolerance — four migrations + four T-NN gates strains §7 review discipline; defense is one reviewer per migration with iter-cap raised to 3 documented as scoped exemption.
- Operators reading provenance markdown as authoritative — once receipts are sha256-verified rows, markdown becomes presentation-only and operators must learn to query receipt tables for verification.
- Backwards-compat with external automation — anyone scripting bin/selvedge submit decision-record without precheck CLI roundtrip will break at next pull; named at EF-S179-1 close-time observation.

### P-3 (anthropic)

**Position.** Steelman maximal arc; ship NULL-tightening + precheck-receipt + slug-UNIQUE in S179; route SHOW-CONTEXT walker, LIMIT-ENTRY shaping, review-loop substrate to S180 on substrate-property grounds.

**schema_sketch.**
- Migration 033 backfills + tightens decision_supports.cited_object_id NOT NULL on cite-required bases (closes OI-086-003) using migration 021 backfill template; T-15 calibrated DROP+RECREATE.
- Migration 034 adds spec_clauses.source_decision_v2_id NOT NULL with backfill (closes OI-086-001); pure substrate tightening, no handler edit needed since spec_clause writes pass FK.
- Migration 035 creates decision_prechecks(precheck_id PK, session_id FK, target_kind, target_key, context_sha256, walker_version, ttl_seconds 30..900, UNIQUE) per chain-walks shape.
- Migration 036 adds sessions.slug UNIQUE constraint (closes OI-S122-1) via T-15-calibrated DROP+RECREATE; pre-flight checks zero-duplicate before constraint applies.
- Decline SHOW-CONTEXT context-walk extension of T-32 in S179: extending walker from cited-aliases to similar-OIs/active-clauses/recent-supersedes is a feature not a constraint; crosses read-write separation.
- Decline LIMIT-ENTRY rate-shaping in S179: refuses-on-skipped-prerequisite-reads requires prose-predicates the substrate cannot detect deterministically per DV-S176-1 R-1.2 inferior_tradeoff.
**cli_surface.**
- Add bin/selvedge precheck --target decision_v2 --target-key <draft-alias> emitting context preview AND inserting decision_prechecks row with sha256; pure side-effect on a receipt table.
- Decision-record submit handler reads decision_prechecks WHERE session_id=current AND target_kind=decision_v2 AND created_at > now-ttl; refuses E_REFUSAL_T33 if zero matching rows.
- Do NOT add bin/selvedge limit-entry / force-checks subcommands in S179; LIMIT-ENTRY and FORCE-CHECKS collapse into precheck-receipt; further subcommands are S180 candidates.
- Decline bin/selvedge precheck --strict mode in S179 since strict-vs-permissive cliff is exactly the false-positive surface S180 should triage post-bootstrap.
**migration_path.**
- Order: 033 NULL-tightening (OI-086-003), 034 spec_clause FK (OI-086-001), 036 slug UNIQUE (OI-S122-1), 035 decision_prechecks + handler T-33; engine v48 to v49.
- 033 and 034 ship before 035 because precheck handler reads spec_clauses.source_decision_v2_id and decision_supports.cited_object_id; building precheck on NULL-admitting columns ships DV-S175-1 backfire.
- Bootstrap test for T-33: DV-S179-1 (this session decision-record) must produce a precheck row before submit; failure to bootstrap == migration 035 rolls back per DV-S176-1 precedent.
- spec edit prompt-development v21 to v22 amends §5 adding T-33 mandatory clause + decision_prechecks receipt shape; promotes recommended-clause language to substrate-enforced status per DV-S176-1.
- Defer migrations for review-loop (OI-083-001), manifest-hash sealing (OI-S104-1), iter-cap (OI-S133-1), export auth (OI-S145-1), atom-length (OI-S177-1) to S180 on substrate-property grounds.
**what_not.**
- Not extending T-32 chain-walk into a context-walk in S179 — read-write separation DV-S176-1 C-2 forbids and predicate-leak surface DV-S176-1 R-1.2 named.
- Not shipping LIMIT-ENTRY as substrate gate refusing on skipped prerequisite reads in S179 — requires prose-predicate of what counts as prerequisite which DV-S175-1 backfire teaches leaks.
- Not shipping review-loop substrate enforcement OI-083-001 in S179 — closure shape spans coding/review/non-coding with subagent-lifecycle dependencies §7 cannot validate end-to-end in single session.
- Not shipping atom-length 240-char ceiling lift OI-S177-1 in S179 — multiple atom_type ceilings + display-vs-storage tradeoff requires methodology deliberation per FR-S177-17.
- Not bumping all 25 MEDIUM OIs to HIGH wholesale; substrate-detectable subset bumps; methodology-shaped or feature-shaped OIs stay MEDIUM until S180 triage.
- Not invoking DV-S109-1 ceremony-subtraction as rejection basis per operator preclusion at S179-open; rejections grounded on substrate-property predicate-leak / read-write-separation / review-loop-bandwidth.
**open_question.**
- TTL value for decision_prechecks rows: 30s pressures agent into re-reading per attempt vs 900s allows context-staleness; field-validation needed which in-session bootstrap cannot provide.
- Whether T-33 admits zero-cite decision-records like T-32 does or refuses universally — zero-cite + no-precheck looks like exactly the shape the gate is meant to catch.
- How precheck context_sha256 binds to context body when context body is non-deterministic across same-second queries (recent-supersedes); read-write separation argument applies recursively.
- Whether OI-086-004 legacy_imports.decomposition_status falls under NULL-tightening migration 033 batch or stays deferred per OI-085-001 dependency chain noted at S178.
- Whether SHOW-CONTEXT walker extension belongs in S180 or further deferred until precheck-receipt usage data arrives per DV-S152-1 typed-observation pathway.
**risk.**
- T-33 false-positive: legitimate spec-typo-fix decision-records with no real context to read get refused; recovery — admit zero-cite + edit_kind=spec_typo_fix as bypass class with named exclusion.
- T-33 refusal-debt sink: agent under timepressure runs precheck-then-submit ritual with no actual read; recovery — context_sha256 verification at submit-time forces handler to re-render and compare.
- 033 NULL-tightening false-positive: legacy decision_supports rows with NULL cited_object_id where claim resolves to alias 021 parser missed; recovery — targeted UPDATE backfills before NOT NULL applies.
- 035 precheck handler dependency on rendered-context determinism: same-target produces different sha256 if recent-supersedes mid-write by parallel session; recovery — wrap render in BEGIN IMMEDIATE.
- LIMIT-ENTRY refusal-debt: OI-S145-1 SELVEDGE_EXPORT_CONTEXT bypass is the existing escape valve; aggressive LIMIT-ENTRY without auth-model fix channels every refusal into env-var bypass underground.
- SHOW-CONTEXT walker predicate-leak: defining what counts as similar-OI or relevant-prior-decision is exactly the prose-predicate DV-S176-1 R-1.2 rejected; ships the same backfire shape DV-S175-1 produced.
- Coupling error if S179 ships precheck without NULL-tightening: precheck context body renders NULL-cite supports as missing-citation noise, training agents to ignore the very signal precheck exists to surface.
**what_lost.**
- Lost: in-session closure of operator full SHOW-CONTEXT vision; partial delivery via precheck-receipt + S180 sealed deliberation on walker extension.
- Lost: in-session closure of LIMIT-ENTRY as distinct mechanism; folded into precheck-receipt and re-evaluated at S180 when usage data exists.
- Lost: 25-MEDIUM-to-HIGH wholesale priority bump aesthetic; substrate-detectable subset bumped, methodology-shaped subset triaged at S180.
- Lost: review-loop substrate hardening OI-083-001 in this session — largest deferral most likely to draw operator pushback; structural defense is §7 cannot validate review-loop-itself in same session.
- Lost: appearance of non-compliance with operator deliver-all-functionality directive — mitigated by naming the structural ceiling (review-loop bandwidth) rather than caution.
- Lost: opportunity to bundle OI-S091-1 stale-version-snapshot fix into the arc; deferred since no determinism gate fires on stale workspace_metadata and fix is mechanical migration not substrate hardening.
- Lost: T-32 context-walk extension momentum from DV-S176-1 freshness; S180 sealed deliberation pays a freshness-tax but gains the bootstrap-data S179 precheck deployment generates.

### P-2 (openai)

**Position.** Ship S179 as one high-priority arc, not one giant gate: precheck receipt first, then NULL closure, review-loop receipts, and determinism gates under T-20 stop rules.

**schema_sketch.**
- Add decision_prechecks with session, target_kind, target_key, context_hash, output_hash, source_count, created_at, command_version, and consumed_by_decision_id.
- Add decision_precheck_sources keyed to each receipt, storing object alias, object type, relation kind, and digest so the handler can recompute the context pack.
- Add NOT NULL and CHECK constraints for OI-086-001, OI-086-003, OI-086-004, OI-S088-1, OI-S125-1, and OI-S126-5 after legacy backfill.
- Add receipt tables for review manifests, falsification expiry, procedural closure, graduation review, and session-number drift using DV-S176-1 sha256 receipt pattern.
- Add UNIQUE sessions.slug, explicit deliberation section-kind enums for OI-S154-4, and widened atom-length columns only for OI-S177-1 named fields.
**cli_surface.**
- Add bin/selvedge precheck --target decision-record --target-key <slug> to print context and insert one receipt tied to the exact target.
- Add bin/selvedge submit decision-record --precheck <hash> and refuse if hash is stale, target-mismatched, already consumed, or recomputes differently.
- Add bin/selvedge audit hardening to show HIGH arc obligations, unresolved backfills, and which OI groups still lack substrate receipts.
- Add bin/selvedge context --target <kind:key> as pure-read only; it may preview context but cannot satisfy the write-gate.
**migration_path.**
- M033 ships precheck tables and handler gating first because SHOW CONTEXT, LIMIT ENTRY, and FORCE CHECKS govern every later decision.
- M034 backfills and constrains Group A, with OI-S125-1 harness alias registration before OI-S126-5 external-session graph checks.
- M035 ships review-loop and manifest receipts for OI-083-001, OI-S104-1, OI-S133-1, and tightens OI-S145-1 export bypass.
- M036 ships predicate gates for OI-S125-2, OI-S151-3, OI-S151-4, OI-S159-1, and OI-S163-1 once their typed columns exist.
- M037 ships determinism constraints for OI-S091-1, OI-S122-1, OI-S130-1, OI-S152-2, OI-S154-1, OI-S154-4, OI-S154-6, and OI-S177-1.
- Update prompts/development.md after each shipped gate, removing prose-only clauses made redundant by enforced receipts per DV-S176-1.
**what_not.**
- Do not make export write receipts, because D-27 preserved read/write separation and the submit path is the enforcement surface.
- Do not accept a generic "I read context" checkbox, because that repeats the DV-S175-1 prose-discipline failure.
- Do not make every OI one trigger immediately, because false refusal against legacy rows will hide real drift behind migration pain.
- Do not defer the arc under DV-S109-1 or DV-S152-1 recurrence logic, because the S179 operator mandate explicitly precludes that basis.
**open_question.**
- Exact freshness window for decision_prechecks is unresolved; would start at 30 minutes and require target hash equality rather than session-only recency.
- Backfill policy for old NULL cite rows needs synthesis, especially whether unresolved historical rows become sealed exceptions or blocking repair work.
- OI-S177-1 needs a field-by-field width choice; globally raising atom length would weaken the existing substrate atom contract.
- EF-S178-1 may require queue-depth thresholds to be tuned after the first HIGH arc run rather than guessed in the migration.
**risk.**
- Precheck false-positive: context changes after review but before submit; recovery is rerun precheck and bind the decision to the new hash.
- NULL-gate false-positive: legacy cite-required rows lack resolvable objects; recovery is a backfill migration with explicit sealed exception rows.
- Review-loop false-positive: static audit blocks runtime repair under OI-S133-1; recovery is a bounded runtime-fix receipt before close.
- Falsification expiry false-positive: a valid open harness expires during active work; recovery is a renewal receipt citing the live typed-observation.
- Session-drift false-positive: operator names an external session number differently; recovery is an alias mapping receipt before submit.
- Context overreach: Anthropic-default reasoning may gate broad semantic similarity, so precheck sources must be deterministic SQL, not model judgment.
**what_lost.**
- We lose the ability to submit fast decision records without a fresh context receipt.
- We lose some operator discretion to waive review-loop ceremony when a substrate predicate can enforce the obligation.
- We lose monolithic S179 closure if T-20 findings appear, but the HIGH arc remains intact and resumes at the next sealed milestone.
- We lose prompt-only simplicity, which DV-S176-1 shows is already inadequate for this failure mode.

### P-5 (anthropic)

**Position.** S179 ships migrations 033/034/035 (T-41 precheck-receipt, T-42 cited_object_id NOT NULL, T-43 sessions.slug UNIQUE) plus a 4-session arc; one-session shipping is unsafe.

**schema_sketch.**
- Migration 033 creates decision_prechecks(precheck_id PK, session_id FK, target_kind, target_key, context_sha256, similar_oi_count, prior_dv_count, active_clause_count, walker_version, created_at).
- Migration 033 adds UNIQUE(session_id,target_kind,target_key) idempotent under retry; receipt-pattern follows DV-S176-1 chain-walk precedent for substrate-side proof-objects.
- Migration 033 adds T-41 BEFORE INSERT ON decisions_v2 refusing E_REFUSAL_T41 unless decision_prechecks row exists for matching (session_id,target_kind,target_key) created within last 1800 seconds.
- Migration 033 handler-side pre-check at selvedge/submit/decision_v2.py inserts at line ~43 mirroring T-39/T-39b defence-in-depth layered with the SQL trigger.
- Migration 034 backfills decision_supports.cited_object_id NOT NULL where basis IN (prior_decision, operator_directive, spec_clause) via T-15-CALIBRATED block; same predicate on alternative_rejections.
- Migration 034 adds T-42 BEFORE INSERT enforcing the same predicate; closes OI-086-003 by-mechanism plus OI-086-001 by-piggyback for spec_clause source_decision_v2_id NULL.
- Migration 035 adds UNIQUE constraint to sessions.slug via T-15-CALIBRATED rebuild path required by sqlite ALTER limitation; closes OI-S122-1.
- Migration 035 includes one-row dedupe pre-flight if collisions exist; otherwise no-op so historical slugs survive intact since the constraint applies forward.
- S180 migration 036 widens decision_supports.claim, decision_effects.target_descriptor, review_findings.finding atom-length ceilings to 480 chars per OI-S177-1 via T-15-CALIBRATED relaxation.
- S181 migration 037 introduces atom_type splits (issue_disposition_reason, issue_link_reason distinct from rejection_reason) per OI-S088-1 via enum-widening.
- S182 migration 038 ships objects-registration for reference_harnesses (OI-S125-1) plus harness expire CLI (OI-S125-2) plus manifest-hash seal forward direction (OI-S104-1).
- S183 migration 039 ships review-loop substrate enforcement (OI-083-001 + OI-S133-1 iter cap with runtime-fix carve-out + OI-S145-1 SELVEDGE_EXPORT_CONTEXT auth-model) as one §7 bundle.
**cli_surface.**
- Add bin/selvedge precheck --target-kind --target-key writing one decision_prechecks row plus printing similar OIs + prior DVs targeting same key + active spec clauses + recent supersedes.
- Precheck output is read-the-context-then-author shape not pre-flight-lint; substrate row is the proof-of-context-read invariant the handler verifies before admitting decision-record submit.
- Defer to S183 a bin/selvedge review-pass --commit substrate-policed review-loop subcommand; in-session this remains operator-policed via FR-S179-4.
- Defer to S182 a bin/selvedge harness expire CLI per OI-S125-2 falsification window closure; FR-S179-3 captures handoff.
- No new flags on bin/selvedge query in S179; precheck rows are queryable via existing SQL surface so reviewer subagents can inspect timing-window adherence.
**migration_path.**
- S179 step 1 ship migration 033 + decision_prechecks table + T-41 + selvedge/submit/precheck.py new handler ~80 lines + handler pre-check in decision_v2.py at ~line 43.
- S179 step 2 ship migration 034 + T-42 + backfill block; decision_v2.py lines 56-62 and 154-161 already resolve cited_oid so handler-side change is enforcement-only.
- S179 step 3 ship migration 035 + UNIQUE on sessions.slug rebuild; selvedge/submit/session.py line 54-58 INSERT inherits the constraint with no handler change.
- S179 step 4 add 8-12 pytest cases to state/tests/test_path_a_kinds.py mirroring T-32 idiom from existing tests at lines 1-120.
- Test names: precheck_required_for_decision_record + precheck_window_30min_expiry + precheck_target_mismatch_refuses + cited_object_id_null_refused + slug_unique_collision_refused.
- S179 step 5 prompts/development.md v21 to v22 §5 amend cite-typing block referencing T-42 substrate-enforcement; new §6 precheck-discipline clause; remove §1.5 prose around context-gathering.
- S179 ships engine-v48 to engine-v49 across the three migrations as a single review cycle.
- S180 picks up FR-S179-1 atom-length widening (OI-S177-1) under sealed deliberation since T-15-CALIBRATED relaxation requires deliberation per spec methodology.
- S181 picks up FR-S179-2 atom_type splits (OI-S088-1) under sealed deliberation since enum-widening + per-call-site reroute is broad scope.
- S182 picks up FR-S179-3 reference_harness substrate completeness (OI-S125-1 + OI-S125-2 + OI-S104-1) as one bundle.
- S183 picks up FR-S179-4 review-loop substrate enforcement (OI-083-001 + OI-S133-1 + OI-S145-1) as one bundle since highest review-loop-cost item in the backlog.
- S184+ FR-S179-5 picks up trigger-predicate substrate-detectability cluster (OI-S151-3 + OI-S151-4 + OI-S159-1 + OI-S163-1).
- S185+ FR-S179-6 picks up determinism cluster (OI-S130-1 + OI-S152-2 + OI-S154-1 + OI-S154-4 + OI-S154-6 + OI-S091-1).
- Tier-1 S179 closes 3 OIs by-mechanism: OI-086-003 via migration 034 T-42; OI-S122-1 via migration 035 T-43; OI-086-001 via migration 034 traceability piggyback.
- Tier-2 S180 closes 1 OI: OI-S177-1 atom-length via migration 036.
- Tier-3 S181 closes 3 OIs: OI-S088-1 atom_type splits + OI-086-004 legacy_imports.decomposition_status enum + OI-S126-5 typed-graph linkage folded into atom_type cluster.
- Tier-4 S182 closes 3 OIs: OI-S125-1 harness alias objects-registration + OI-S125-2 expire CLI + OI-S104-1 manifest-hash seal forward.
- Tier-5 S183 closes 3 OIs: OI-083-001 review-loop enforcement + OI-S133-1 review iter cap relaxation + OI-S145-1 SELVEDGE_EXPORT_CONTEXT auth-model.
- Tier-6 S184+ trigger-predicate cluster: OI-S151-3 + OI-S151-4 + OI-S159-1 + OI-S163-1 substrate-detectability after gate-enforcement context-walk arc lands.
- Tier-7 S185+ determinism cluster: OI-S130-1 + OI-S152-2 + OI-S154-1 + OI-S154-4 + OI-S154-6 + OI-S091-1 substrate-detectability finalised.
- Procedural cluster: OI-002/005/009/014/015/018/019/S104-3 remain methodology-shaped, deferred to v22 §1.5 priority-2 cycle as application-mode items.
- Total 13 of 25 OIs close by-mechanism across S179-S183; 12 remain methodology/procedural awaiting application-mode resolution.
**what_not.**
- Do not ship a context-walk extension to T-32 in S179; conflating cite-walks with context-walks loses the existence-vs-correctness distinction the chain-walk receipt cleanly captures.
- Do not ship review-loop enforcement (OI-083-001 + OI-S133-1) in S179 because the iter cap blocks runtime-fix records and remedy requires deliberation on extend-cap-vs-add-runtime-channel.
- Do not ship more than 3 migrations in S179; §7 review-loop iter1 budget burns at ~1 reviewer-pass per migration plus 5-perspective convening already loads the session envelope.
- Do not invoke DV-S109-1 ceremony-subtraction as deferral basis per operator preclusion at brief; defer-shape here is review-loop discipline not ceremony-cost.
- Do not author recommended-clauses in prompts/development.md for any gate that does not ship in S179; per DV-S176-1 prose-and-discipline reproduces failure modes substrate-gates defend against.
**open_question.**
- Does T-41 precheck-window default 1800 seconds or per-session-only with no expiry; session-only is simpler but allows cross-session staleness if session spans hours.
- Does T-41 admit zero-cite decisions without precheck like T-32 admits zero-cite without walks, or does precheck become mandatory floor regardless; admit-shape is safer for first ship.
- Does precheck similar-OI surface use embedding-similarity (none in workspace) or alias-prefix-match (deterministic but coarse); P-5 stance is alias-prefix plus same-target-kind exact-match.
- Does the 30-minute window survive multi-perspective deliberations where synthesis-decision is authored hours after precheck; possibly extend to per-session-bounded with no time cap.
- Does atom-length widening to 480 chars in S180 require coordinated review of T-15-CALIBRATED relaxation policy since CHECK relaxation is not strictly additive.
- Does precheck on non-decision-record submits (issue, perspective-position, review-finding) belong in S179 scope or defer to FR-S179-8.
**risk.**
- T-41 false-positive: legitimate decision-record after long deliberation hits expired precheck; recovery is re-run precheck same args within window then resubmit, single-command aligned with T-32 retry.
- T-42 false-positive: legacy decision-records have NULL cited_object_id on prior_decision basis; migration backfill must resolve all aliases before NOT NULL applies, recovery per-row resolve-or-promote.
- T-43 false-positive: pre-existing duplicate slugs from old workspace history; recovery is one-shot dedupe pass before UNIQUE applies and historical slugs survive intact.
- Multi-session arc risk: S180+ deliberations stale if S179 teaches new constraints; recovery is each session re-reads DVs and binds to operator-named-mandate at session-open per DV-S171-1.
- Precheck context-surface noise: SHOW CONTEXT can become noise; recovery is similar-OI cap at 5 + prior-DV cap at 3 + active-clause cap at 5 with operator override flag.
- Migration 034 backfill may fail if legacy NULL cited_object_id rows resist resolve; recovery is migration-time refusal halts S179 and forces resolve-then-rerun, aborting cleanly via BEGIN/COMMIT.
**what_lost.**
- Operator one-session shipping mandate is partially refused; structural defense is multi-session arc with operator ratification per spec methodology multi-session-deliberation precedent.
- Precedent for multi-session arcs: S125 reference_harness S125-S128, S172-S176 chain-walk; S179-S183 substrate-hardening matches that pattern.
- Maximally-aggressive single-shot context-walk extending T-32 is not authored; if calibration-EF in S180-S183 shows decision-records-without-context-reads recurring, escalate to context-walk extension.
- DV-S109-1 ceremony-subtraction stance is set aside per operator preclusion; if S180+ surfaces precheck-as-ceremony-without-payoff calibration, operator may retract T-41.
- Aggressive precheck enforcement on non-decision-record submits is forfeit in S179 scope; if calibration shows context-gaps on those kinds, FR-S179-8 captures handoff.
- Procedural-cluster OIs (OI-002/005/009/014/015/018/019/S104-3) remain methodology-shaped indefinitely; not technical-substrate ships within this arc.
- Tier-3-through-7 OIs remain priority-MEDIUM through S179 close; promotion to HIGH conditioned on each subsequent operator-ratified session-open.

### P-4 (openai)

**Position.** Ship hard substrate gates, but stage them by dependency; cognition is not detectable, only fresh context coverage and submit continuity are.

**schema_sketch.**
- decision_prechecks stores target kind, key, context pack hash, gate version, issued_at, consumed_at, and nonce.
- context_pack_items stores every surfaced alias with source table, object id, relation, and stale_after timestamp.
- decision_record_submits must reference one unconsumed precheck nonce for the same target and gate version.
- citation_requirements declares which basis kinds require typed object resolution for new rows.
- legacy_unresolved_cites preserves old NULL cited_object_id rows until backfill proves a target.
**cli_surface.**
- bin/selvedge precheck --target decision --target-key <alias> prints context and writes the receipt.
- bin/selvedge submit decision-record --precheck <nonce> consumes the receipt inside the submit write_tx.
- Submit handler rejects stale, mismatched, previously consumed, or context-hash-invalid prechecks.
- CLI cannot prove reading, so the enforceable predicate is freshness, target match, pack coverage, and single-use consumption.
**migration_path.**
- 033 adds context-pack and precheck tables without enforcement, so S179 can record receipts first.
- 034 backfills object aliases for OI, FR, DV, EF, and harness aliases, addressing OI-S125-1 before cite triggers.
- 035 backfills nullable cite rows where alias resolution is deterministic and moves failures to legacy_unresolved_cites.
- 036 adds typed-cite submit path and triggers requiring cited_object_id only for new cite-required rows, addressing OI-086-003.
- 037 extends T-32 into context-walk receipts over same-target decisions, supersedes, similar OIs, and active clauses.
- 038 gates decision-record submit on fresh consumed precheck and writes refusal receipts for bypass attempts.
**what_not.**
- Do not ship blanket NOT NULL on decision_supports.cited_object_id in S179 because legacy NULL rows already violate OI-086-003.
- Do not treat a timestamp-only precheck as enforcement because it rewards fire-and-forget behavior.
- Do not replace substrate gates with prompt clauses; DV-S176-1 says that failure mode already reproduced.
- Do not make SELVEDGE_EXPORT_CONTEXT the bypass path for precheck enforcement, or OI-S145-1 remains open in disguise.
**open_question.**
- Should session-open prechecks be advisory first while decision-submit prechecks are hard-gated in S179?
- Which relation set defines similar OIs without creating unstable query drift across sessions?
- What exact stale window is acceptable for prechecks before submit, given concurrent writes and OI-S122-1?
- Should unresolved legacy cite rows block closure, or only block new decision support rows after migration 036?
**risk.**
- Typed-cite trigger false-positive: alias resolver misses a valid legacy alias; recovery is object-alias backfill plus replayed submit.
- Precheck freshness false-positive: unrelated write changes the pack hash; recovery is rerun precheck and resubmit.
- Context-pack coverage false-positive: similar-OI query over-includes noise; recovery is relation whitelist migration, not handler override.
- Single-use nonce false-positive: interrupted submit consumes nothing if write_tx aborts; recovery is rerun precheck.
- Session-open context false-positive: agenda work is blocked by broad targets; recovery is advisory receipt before hard gate.
**what_lost.**
- S179 loses all-in-one closure theater; staged migrations are the price of deterministic enforcement.
- Legacy NULL cite rows get preserved longer, so OI-086-003 closes only for new writes until backfill proof completes.
- Agents retain the ability to ignore displayed context cognitively; the substrate only proves exposure path and submit coupling.
- Prompt discretion shrinks because DV-S176-1 makes handler refusal the controlling mechanism.

### Synthesis

# D-28 Synthesis — substrate-hardening + determinism arc

## Frame

The operator at S179-open named insufficient substrate hardening and engine non-determinism as the load-bearing failure mode and explicitly precluded both DV-S109-1 ceremony-subtraction and DV-S152-1 typed-observation→gate progression as deferral bases for this arc. The mandate is to ship substrate (constraints, triggers, Python validators) for as much of the ~25 hardening MEDIUM-OI backlog as the engine's review-loop discipline can absorb, plus three operator-named meta-features: SHOW CONTEXT, LIMIT ENTRY, FORCE CHECKS BEFORE DECISIONS. Five perspectives convened: P-1 architect (Anthropic, maximal in-session program), P-2 codex-shape (OpenAI cross-family, sequenced milestones M033-M037 under T-20 stop rules), P-3 adversary (Anthropic, substrate-property route-to-S180 minority), P-4 codex-skeptic (OpenAI cross-family, dependency-graph rigor + single-use-nonce), P-5 pragmatist (Anthropic, 3 migrations + 4-session arc handoff).

## Convergence (multi-source independent agreement)

**C-1. Pre-decision context-injection ships in S179 as a `decision_prechecks` receipt-pattern table.** Four independent perspectives reached the same structural shape: precheck row records the context the agent was exposed to; submit handler verifies the receipt inside `write_tx`; refusal raises a new T-NN error code [P-1, Schema sketch][P-2, Schema sketch][P-3, Schema sketch][P-5, Schema sketch]. The receipt-pattern follows the DV-S176-1 chain-walk precedent — sha256 + edge-count + handler dispatch — extended to context exposure rather than provenance traversal.

**C-2. NULL-cite hardening cannot ship as blanket NOT NULL.** Legacy rows already violate the proposed predicate; a blanket trigger refuses migration apply or retroactively invalidates committed decision-records [P-2, Risks][P-3, Risks][P-4, What not][P-5, Risks]. The structural answer is convergent: backfill where deterministic, quarantine where not, enforce NOT NULL only on new rows by trigger. The legacy preservation is named explicitly.

**C-3. `sessions.slug` UNIQUE ships in this arc.** OI-S122-1 is the cleanest deterministic gate in the backlog; pre-flight dedupe + T-15-CALIBRATED rebuild has zero false-positive surface [P-1, Schema sketch][P-3, Schema sketch][P-5, Schema sketch][P-4, Migration path].

**C-4. Read/write separation (DV-S176-1 D-27) is preserved.** The precheck CLI emits markdown to stdout AND writes the receipt row; the receipt is the substrate proof, the print is presentation [P-1, CLI surface][P-2, CLI surface][P-3, CLI surface][P-4, CLI surface]. The submit handler — not the export tool — does the gating. P-2's codex contribution explicitly carries this discipline forward from D-27.

**C-5. Cognition is not substrate-detectable; only freshness, target match, pack coverage, and submit continuity are.** P-4 codex names this most directly [P-4, Position]; P-2 codex implies it via the `consumed_by_decision_id` column [P-2, Schema sketch]; P-3 implies it via the `context_sha256` verification [P-3, Risks]; P-5 names "proof-of-context-read invariant" rather than proof-of-comprehension [P-5, CLI surface]. The synthesis adopts this as a load-bearing invariant: **the gate enforces exposure path, not comprehension**. The operator's literal SHOW-CONTEXT vision (proving the agent read) is forfeit in this exact form; substituted is the substrate-detectable subset (the agent ran the precheck and the receipt has a non-stale, target-matched, single-use, hash-verified shape).

## Divergence (substantive disagreement preserved)

**D-1. Scope size of S179.** Perspectives diverge on how many migrations land cleanly in one session under §7 review-loop discipline. P-1 proposes 4 migrations (032-035) with 4 new T-NN gates [P-1, Migration path]. P-2 proposes 5 milestones M033-M037 staged under T-20 stop rules [P-2, Migration path]. P-3 proposes 3 migrations with explicit substrate-property defense for what is deferred [P-3, Migration path]. P-4 proposes 6 migrations 033-038 staged by dependency, with the hard precheck gate not landing until 038 [P-4, Migration path]. P-5 proposes 3 migrations + a 4-session handoff arc S180-S183 with explicit FR-S179-1..6 [P-5, Migration path]. The synthesis adopts a **6-migration in-session shape** that follows P-4's dependency staging but enables the precheck gate at 035 (not 038) per the operator-named-mandate; the decision-record below records this synthesis-original choice as `[synth]`.

**D-2. Precheck enforcement mechanism.** P-1 proposes a window-of-validity timestamp (precheck created_at within 30 minutes of submit) plus context_sha256 verification [P-1, Risks]. P-2 proposes a hash receipt with `consumed_by_decision_id` child column to make consumption observable [P-2, Schema sketch]. P-3 proposes a TTL bounded 30..900s + UNIQUE per (session, target) [P-3, Schema sketch]. P-4 proposes a single-use nonce consumed inside the submit's `write_tx` such that a precheck row services exactly one decision-record submit [P-4, Schema sketch]. P-5 proposes a 1800-second window with idempotent UNIQUE per (session, target_kind, target_key) [P-5, Schema sketch]. **P-4's single-use nonce is materially stronger than the others** because it closes the "fire-and-forget" gaming pattern P-2 also flagged: a window predicate admits running precheck once and submitting many decisions; a nonce admits exactly one. The synthesis adopts P-4's single-use-nonce + P-2's `decision_precheck_sources` child table for per-source digest + P-3's TTL bound (default 1800s, hard cap 3600s) `[synth]` as the merged shape.

**D-3. Ordering of NULL-tightening relative to precheck.** P-3 surfaces a coupling error no other perspective named: shipping precheck before NULL-tightening renders NULL-cite supports as missing-citation noise *inside the very context body precheck exists to surface*, training agents to ignore the gate's signal — self-defeating [P-3, Risks last bullet]. P-1 ships both in migration 032 simultaneously [P-1, Migration path]. P-2 ships precheck (M033) before NULL-closure (M034) [P-2, Migration path]. P-4 backfills aliases (034) and cite rows (035) before triggers (036) and gates (038) [P-4, Migration path]. P-5 ships precheck (033) before cite-NOT-NULL (034) [P-5, Migration path]. **The synthesis adopts P-4's ordering — alias backfill (033) and cite-row backfill / quarantine (034) BEFORE precheck table (035) and trigger (036) and slug-UNIQUE (037)** — because P-3's coupling argument is structurally correct: the precheck body must render context that already passes the cite-typing rule, or the gate's first impression is exception-noise.

## Minority preserved

**M-1. Route SHOW-CONTEXT walker, LIMIT-ENTRY rate-shaping, and review-loop substrate enforcement to a follow-up sealed deliberation on substrate-property grounds.** P-3 articulates the strongest version: extending T-32 from chain-walks to context-walks of "similar OI / relevant prior decision" requires a prose-predicate of similarity that DV-S175-1's backfire taught leaks; LIMIT-ENTRY without first repairing OI-S145-1 SELVEDGE_EXPORT_CONTEXT auth-model channels every refusal into env-var bypass (refusal-debt accumulates underground); review-loop substrate enforcement spans coding/review/non-coding shapes that §7 review cannot validate end-to-end in the same session that ships the substrate [P-3, Risks][P-3, What not][P-3, What lost]. The grounds are explicitly substrate-property (predicate-leak, refusal-debt-channeling, review-loop-cannot-validate-itself) — not DV-S109-1 ceremony-subtraction (operator-precluded). **The synthesis adopts the in-session shape (precheck IS the SHOW-CONTEXT/LIMIT-ENTRY/FORCE-CHECKS gate, in narrowed form) but preserves P-3's minority that the broader walker / rate-shaping / review-loop substrate must wait on a sealed S180+ deliberation.** The minority is preserved as M-1 because the synthesis disagrees on the deferral set (synthesis ships more than P-3's minimum) but agrees on the structural reason for deferral of the broader walker.

**M-2. P-5's explicit 4-session handoff arc framing (S179-S183).** P-5 names the multi-session arc precedent (S125 reference_harness, S172-S176 chain-walk) and proposes FR-S179-1..6 as substrate-side handoff records [P-5, Migration path][P-5, What lost]. The synthesis adopts the FR-handoff pattern but compresses the 4-session arc into a 2-session arc (S179 ships substantially more than P-5's minimum) `[synth]`.

## Adopted shape

S179 ships **7 migrations** (033-039) under one engine version bump v48→v49, one sealed deliberation D-28 (this), and per-migration Explore reviewer subagent passes inside the §7 review-loop:

- **033** harness alias objects-registration (OI-S125-1 close).
- **034** legacy_unresolved_cites quarantine table + nullable-cite backfill (foundation for OI-086-003).
- **035** decision_prechecks + decision_precheck_sources + handler dispatch + T-33 single-use-nonce gate (operator's SHOW-CONTEXT/LIMIT-ENTRY/FORCE-CHECKS, narrowed to substrate-detectable form).
- **036** typed-cite trigger T-34 BEFORE INSERT enforcing cited_object_id NOT NULL on new rows where basis ∈ {prior_decision, spec_clause, deliberation, review_finding, engine_feedback, constraint, operator_directive} (OI-086-003 close-on-new-rows; legacy preserved via 034 quarantine).
- **037** sessions.slug UNIQUE via T-15-CALIBRATED rebuild (OI-S122-1 close).
- **038** spec_clauses.source_decision_v2_id NOT NULL backfill (OI-086-001 close).
- **039** atom-length widening to 480 chars on three named cliffs: decision_supports.claim, decision_effects.target_descriptor, review_findings.finding (OI-S177-1 close-on-named-fields; broader policy deferred).

Routed to S180+ as FR-S179-1..N handoffs: OI-S088-1 atom_type splits, OI-S125-2 harness expire CLI, OI-S104-1 manifest-hash seal, OI-083-001 review-loop substrate, OI-S133-1 review iter cap, OI-S145-1 export-context auth-model, OI-086-004 legacy_imports.decomposition_status, OI-S151-3/4, OI-S159-1, OI-S163-1, OI-S091-1, OI-S130-1, OI-S152-2, OI-S154-1/4/6, OI-S126-5. Each routes with FR carrying explicit substrate-property reason for deferral (per P-3 minority discipline).

prompts/development.md v21→v22: §5 amend adds T-33 mandatory clause + decision_prechecks single-use-nonce shape; the §5 "recommended-clause" framing inherited from DV-S175-1 is removed since T-33 ships substrate-gate. Engine v48→v49.

The Anthropic perspectives (P-1, P-3, P-5) frame the trade-offs from inside the engine's own conventions; the OpenAI cross-family perspectives (P-2, P-4) carry read/write separation discipline and dependency-graph rigor that reshaped the migration ordering. The synthesis is heavier on P-4 sequencing + P-3 coupling argument + P-2 child-source table + P-5 FR-handoff pattern + P-1 in-session ambition than any single perspective standing alone — convergence on shape, divergence on size, minority on deferral set, adopted shape exceeds any single perspective's proposal `[synth]`.


### Synthesis points

- **convergence C-1.** Pre-decision context-injection ships in S179 as decision_prechecks receipt-pattern table extending DV-S176-1 chain-walk shape from provenance to context exposure.
- **convergence C-2.** NULL-cite hardening cannot ship as blanket NOT NULL; legacy rows backfilled where deterministic and quarantined where not, NOT NULL enforced only on new rows by trigger.
- **convergence C-3.** sessions.slug UNIQUE ships in this arc; T-15-CALIBRATED rebuild with pre-flight dedupe has zero false-positive surface and closes OI-S122-1 cleanly.
- **convergence C-4.** Read/write separation per DV-S176-1 D-27 preserved; precheck CLI prints AND writes the receipt, but the submit handler not the export tool does the gating in the same write_tx.
- **convergence C-5.** Cognition is not substrate-detectable; the gate enforces exposure path not comprehension via freshness, target match, pack coverage, single-use consumption.
- **divergence D-1.** Scope size diverges: P-1 4-migrations maximal, P-2 5-milestones staged, P-3 3-migrations substrate-property defended, P-4 6-migrations dependency-staged, P-5 3-migrations + 4-session arc; synthesis adopts 7-migration in-session shape.
- **divergence D-2.** Precheck enforcement: P-1 window-of-validity, P-2 hash + consumed_by_decision_id child, P-3 TTL 30..900s + UNIQUE, P-4 single-use nonce in write_tx, P-5 1800s window; synthesis adopts P-4 nonce + P-2 child-source + P-3 TTL bound.
- **divergence D-3.** Ordering NULL-tightening vs precheck: P-3 alone surfaced coupling error that precheck-before-NULL renders NULL-cite supports as exception-noise inside context body; synthesis adopts P-4 ordering aligning with P-3 argument.
- **minority M-1.** P-3 minority: route SHOW-CONTEXT walker, LIMIT-ENTRY rate-shaping, review-loop substrate enforcement to S180+ on substrate-property grounds (predicate-leak, refusal-debt sink, review-loop-cannot-validate-itself). Adopted partially.
- **minority M-2.** P-5 minority: explicit 4-session handoff arc S179-S183 framing with FR-S179-1..6 substrate-side handoff records; synthesis compressed to 2-session arc but preserves FR-handoff pattern.
