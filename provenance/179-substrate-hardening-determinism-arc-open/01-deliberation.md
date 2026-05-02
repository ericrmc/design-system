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

### P-5 (anthropic)

### P-4 (openai)

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
