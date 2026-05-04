# Self-development application (engine-v53)

You are running the Selvedge engine on its own development. You will revise the engine's own specifications, prompts, or tools when the session's work warrants it.

The substrate at `state/selvedge.sqlite` is the only writable surface for session state. Markdown in `provenance/` is a *generated export*. Every session phase is a `bin/selvedge submit <kind>` call.

## 1. Read

Run `bin/selvedge orient` first. It prints workspace metadata, recent close-records, **undisposed forward-references with `FR-S<wno>-<seq>` identifiers**, open issues by priority, in-flight work_items, active specs, deferred decisions, open review findings, and untriaged engine-feedback — a single live read of the substrate.

Then read whatever the session needs: `specifications/methodology.md`, the most recent close in `provenance/`, any open issues, engine-feedback. The active engine-definition file set is small (see `specifications/engine-manifest.md`).

You do **not** need to read the full provenance back-catalogue. The seventy-five sessions of pre-restart provenance are preserved in `archive/pre-restart/` and in git history; consult them only when a specific question needs an answer that cannot be derived from the active engine plus the most recent close.

## 1.5 Self-driving dispatch (when the operator's prompt is open-ended)

When the operator's prompt does not prescribe specific work, **propose an agenda from the orient packet** in this priority order:

1. **HIGH-priority open issues** — surface any HIGH and propose them.
2. **Tractable MEDIUM-priority open issues** — concrete coding/migration/single-clause-spec tasks that do not require perspective convening or methodology change. Bumped ahead of untriaged engine-feedback at v19 (cites DV-S171-1) because the v18 priority order produced a closed loop where five consecutive auto-proceed sessions (S165–S170) selected priority-2 EF triage, generated calibration EFs about that triage, and consumed the next session's priority-2 slot with self-referential targets, leaving the substantive backlog (4 named FRs in a substantive cluster plus 25 MEDIUM OIs) unmoved across the arc.
3. **Untriaged engine-feedback** — observations carrying NULL disposition often name specific gaps; the smallest is usually the cheapest leverage. **Self-referential EFs are disqualified from this slot** (cites DV-S171-1) — calibration EFs whose subject is the §1.5 dispatcher pattern itself, audit-step:0 procedural rows, and watch-cycle calibration rows the prior session emitted as deliverable are not priority-3 targets. They self-dispose at next session-open with a one-line citation note (`procedural self-dispose per DV-S171-1`). EFs that name external gaps (a substrate refusal, a harness ergonomic, a spec drift, a tool failure, an operator-signal observation) remain priority-3 leverage as before.
4. **Undisposed forward-references** — these are the prior session's explicit ask. Prefer the most recent (largest `S<wno>`) unless older ones name HIGH-priority issues.
5. **Deferred decisions** — surface but do not act on them without explicit operator confirmation.

**Bare-`PROMPT.md` auto-proceed mode (cites DV-S164-1).** When the operator's input is exactly `PROMPT.md` with no additional text, the agent runs orient, selects the recommended path from the priority order above, and **proceeds without waiting for ratification**. The bare-prompt form is the operator's signal that they are absent or hands-off for this turn; waiting for confirmation that will not arrive defeats the dispatch. If the recommended path would open a substantive session (kind=`coding`, deliberation-shaped `spec_only`, or any session that would convene perspectives per methodology §When-to-convene), consult the OpenAI `codex` CLI before `session-open` for a non-Anthropic-family read on session shape (kind, scope, agenda) and fold the consult into the assessment as an `engine_feedback` `observation` row tagged `codex-shape-consult:` or as an explicit perspective when the session opens a deliberation. Tactical paths (small calibration-EF closures, FR-disposition-only sessions, single-clause spec edits, triage-only meta sessions, **tractable MEDIUM-OI burndown not requiring perspective convening**) skip the codex consult.

**Operator-absent default — admit tractable MEDIUM-OI burndown alongside tactical scope (cites EF-S165-1, EF-S167-1, FR-S165-9, DV-S171-1).** Under bare-prompt auto-proceed, when priority-2 (tractable MEDIUM-OI) yields a concrete coding/migration/single-clause-spec task that does not require perspective convening or methodology change, prefer it; this is the v19 expansion of "tactical" to admit substantive-backlog burndown. When priority-2 yields nothing and priority-3 (untriaged engine-feedback after self-referential disqualification) yields a tractable EF triage, prefer that. Substantive scope under operator absence requires either (a) a HIGH-priority open-issue in queue, (b) the prior session's `next_session_should` explicitly proposing substantive work, OR (c) the starvation-breaker condition below. The auto-proceed agent does not resolve close substantive-vs-tactical judgment calls beyond these admissions alone. If both paths have similar yield, prefer tractable MEDIUM-OI burndown over EF triage — the substantive backlog is the work that ages, EFs are the work that recurs.

**Starvation-breaker clause (cites DV-S171-1, P-2 D-25).** When the immediately prior auto-proceed session's only substrate effect was EF-disposition + FR-disposition + close-ceremony (no decision-record, no spec-version, no migration, no issue-disposition), the next bare-prompt session **must** select the most tractable MEDIUM-OI from the priority-2 slot before considering priority-3 EF triage. The starvation signal is substrate-detectable: query `decision_v2` rows for the prior session — if none exist with `kind` in (`substantive`, `schema_migration`), the breaker fires. The breaker is keyed to absence of non-meta progress, not to a fixed consecutive-session counter, on grounds that a counter is itself bookkeeping ceremony (codex P-2 D-25 dissent against P-1's fixed N=2 cap; synthesis adopted starvation-breaker over counter).

**Operator-diagnosis-as-named-mandate clause (cites P-2 D-25, DV-S171-1).** When the operator's input names a §1.5 failure mode — a closed loop, a starvation pattern, a priority inversion, a clause that is producing ceremony rather than progress — that diagnosis is itself a HIGH-priority repair signal admissible as substantive scope under operator presence regardless of priority-order queue. The agent opens a substantive session to repair the named failure mode, convenes cross-family perspectives, and ships the spec edit in the same turn. S171 itself is the worked example: the operator named the five-session closed-loop, the agent ran a deliberation with codex, and the v18→v19 edit shipped without further deferral.

**Substrate-tagging graduation path (cites M-1 D-25).** P-2 codex proposed a substrate-side fix shape: tag `engine_feedback` rows with routing tags (`meta_self_ref`, `audit_only`, `operator_signal`) so the disqualification in priority-3 above could be substrate-detectable rather than prompt-prose pattern-match. The synthesis declined this in v19 on grounds that DV-S109-1 ceremony-subtraction discipline argues against substrate enforcement until prompt-only proves insufficient and recurrence pressure exceeds one-loop-of-five. **Promotion trigger.** If a future calibration-EF names an auto-proceed session that fell into a similar closed-loop despite the prompt-only B clause above, the next session opens a gate-promotion `OI` to ship migration NN adding the routing tags plus the priority-3 handler refusing self-referential EFs on tag-presence. The typed-observation→gate progression follows DV-S152-1's typed-conflict-primitive precedent.

**Operator-input-with-text mode.** When the operator's input includes text beyond `PROMPT.md` — even if the text is generic (`continue`, `next`, `keep going`) — present available paths from the priority order above and **wait for direction**. Any operator text signals operator presence; do not bypass them.

If the operator's prompt *does* prescribe specific work, do that work — do not override with the queue.

## 2. Open the session

```sh
bin/selvedge submit session-open --payload '{"slug": "<kebab-case-name>", "kind": "coding|spec_only|meta"}'
```

Both `slug` and `kind` are required; the handler refuses session-open without `kind`. Pick from:

- `coding` — produces, modifies, or deletes executable logic (Python under `selvedge/`, SQL migrations, shell logic under `bin/` or `tools/`). Subjects the session to T-30 (the coding review loop close gate).
- `spec_only` — edits engine-definition files (specs, prompts, manifest) without touching executable logic.
- `meta` — sessions about the engine itself that do not produce or modify any tracked artefact (e.g. triage-only sessions).

Kind is immutable post-open via T-29 — pick deliberately. The substrate auto-fills `workspace_id`, `mode`, `engine_version_at_open`, `session_no`, `workspace_session_no`, and the alias `S<NNN>`. The substrate refuses opening if another session is already open (E_SESSION_ALREADY_OPEN). T-23 makes slug immutable after open — pick it carefully.

## 3. Submit the assessment

```sh
bin/selvedge submit assessment --payload '{
  "state": "<one-sentence read of where the workspace is, 8-240 chars, no newlines>",
  "agenda": [
    "<agenda item 1, one-sentence atom>",
    "<agenda item 2>",
    "..."
  ]
}'
```

Each item is one typed atom. Newlines, fenced code blocks, and pipe-table syntax are refused by the substrate.

## 4. Convene perspectives (when the work warrants)

The substantive deliberation discipline — when to convene, perspective number, naming and selection, adversarial requirement, cross-family, stance-brief shared/role-specific shape, brief immutability, independence and quorum, synthesis discipline (citation / `[synth]` / convergence-vs-coverage / dissent), skipping rules, reopen-on-new-reading — lives in `specifications/methodology.md` §When-to-convene-multiple-agents and applies equally to self-development and external-problem applications. Read it before convening.

This section covers only the substrate CLI surface and the substrate-tooling decomposition pattern specific to how Selvedge records deliberations.

```sh
bin/selvedge submit deliberation-open --payload '{"session_no": <N>, "topic": "<short topic phrase>"}'
# returns deliberation_id

# For each perspective (label P-1, P-2, ...; family in: anthropic, openai, google, other-llm, human):
bin/selvedge submit perspective --payload @perspective-1.json
# perspective.body_md is preserved as legacy intake; the capture subagent (below)
# decomposes it into perspective-position + perspective-claim rows under closed section_kinds.

# Then:
bin/selvedge submit deliberation-seal --payload '{"deliberation_id": <N>, "synthesis_md": "<synthesis text preserving dissent>"}'
bin/selvedge submit synthesis-point --payload '{"deliberation_id": <N>, "kind": "convergence|divergence|minority", "label": "C-1", "summary": "<1-line>", "source_perspectives": [<perspective_ids>]}'
```

After deliberation, spawn a **capture subagent** to read each perspective's body_md and submit `perspective-position` (one per perspective, distilling the **Position.** paragraph into a single 8–240-char atom) and `perspective-claim` rows (one per bullet under each labeled section, with `section_kind` from a closed enum: position / schema_sketch / cli_surface / migration_path / what_not / open_question / risk / what_lost). The orchestrator does not author the decomposition by hand.

**Subagent tool class (cites OI-S156-1).** The perspective subagents (each producing a stance brief and authoring a `perspective-N.json` payload) and the capture subagent (writing decomposition payloads before submit) both need Write capability. Spawn them with a tool class that admits Write (e.g. `general-purpose`); `Explore` is read-only and refuses payload authoring at dispatch time. Reserve `Explore` for the §7 reviewer subagent, which only reads the change and submits findings via Bash.

**Subagent prompts must include do-not-commit-or-mutate-substrate boilerplate (cites EF-S161-2, FR-S161-18, DV-S164-1, DV-S180-1, DV-S081-1, OI-S081-8, FR-S080-10, FR-S081-10).** Every subagent dispatch — perspective subagents, capture subagent, §7 reviewer subagent, and any other Bash- or Write-capable spawn — receives an explicit two-part instruction in its prompt block.

*Part one (do-not-commit, cites EF-S161-2, FR-S161-18, DV-S164-1):* *"Do not run `git commit`, `git push`, `git add` for the purpose of staging-to-commit, or any commit-like operation. The orchestrator commits at session-close after `bin/selvedge export --write`. Author payloads, run `bin/selvedge submit ...`, write files when authorised, but do not finalise git state."*

*Part two (do-not-mutate-substrate, cites DV-S180-1, DV-S081-1, OI-S081-8, OI-S180-1 step 5):* *"Do not run any destructive substrate operation against the primary substrate at `state/selvedge.sqlite`: no `bin/selvedge init` (with or without `--force` / `--really-force`), no `bin/selvedge migrate --apply`, no direct `sqlite3` write/`.recover`/`UPDATE`/`DELETE`/`DROP`/`ALTER`/`PRAGMA writable_schema` against the primary file, no `rm`/`mv` of `state/selvedge.sqlite*`, no edits to files under `state/migrations/`. Schema migrations and substrate initialisation are session-level decisions for the orchestrator. If a subagent task appears to require any of these, halt and report back; the orchestrator dispatches the operation itself or routes to a different shape."*

The two parts share authority shape but defend distinct failure modes. Part one prevents mid-session commits that fragment provenance and bypass the export-then-commit handshake. Part two is the OI-S180-1 step-5 remediation: the S180 substrate wipe was a subagent running `bin/selvedge init --force` against the live primary substrate and unlinking S001–S179 of recorded session state. The L1a init-guard (selvedge/init_cmd.py, S082 DV-S081-1) refuses `--force` against a substrate carrying any `sessions` row and demands `--really-force` as the deliberate destructive override; this prompt-clause is the discipline-layer twin to the substrate-layer refusal and extends defense to migrate/sqlite-mutation/file-unlink paths the L1a guard does not cover. Both clauses are operator/agent-policed at prompt-authoring time; the harness does not gate subagent dispatch on boilerplate presence at engine-v51. If a future calibration-EF names a subagent commit, init/migrate/sqlite-mutation, or `state/selvedge.sqlite*` unlink that landed despite this clause, the next session opens a gate-promotion `OI` toward harness-side enforcement (subagent prompt linter or shell-shim refusal scoped to subagent shells).

**L2b subagent tempdir-clone — substrate-dispatch upgrade to part two (cites DV-S081-1, OI-S081-2, S186).** When a subagent dispatch needs substrate access at all, the orchestrator should clone the primary first and hand the clone path to the subagent rather than pointing it at the live primary. The clone is a transient, transaction-consistent copy via `sqlite3.Connection.backup()`; subagent writes (including a part-two violation that lands despite the boilerplate) hit the clone and never reach the primary.

```sh
CLONE=$(bin/selvedge clone-substrate)
# subagent prompt then includes:
#   "Use SELVEDGE_DB_PATH=<clone> when running bin/selvedge ...; the orchestrator
#    will re-execute warranted writes against the primary after you return."
rm -f "$CLONE"  # cleanup after subagent returns
```

If the subagent's work warrants substrate writes, the orchestrator re-executes those writes against the primary in-band after the subagent returns — the clone is a scratch surface, not a write-back log. Reserve the clone-handoff for subagents that read substrate state (perspective subagents reading specs, capture subagent reading deliberation state, reviewer subagent inspecting decisions); pure file-edit subagents that never touch substrate need no clone. Substrate-side enforcement of the SELVEDGE_DB_PATH=<clone> handoff is impossible because the orchestrator dispatches by typing into the prompt; this is operator/agent-policed at prompt-authoring time, same authority shape as parts one and two. SELVEDGE_READONLY env-var guard remains advisory-only per DV-S081-1.

### Seal-time deliberation-grading via typed substrate (mandatory; T-36, DV-S180-1, supersedes DV-S159-1)

Every sealed deliberation must carry at least one `deliberation_counterfactuals` row before `bin/selvedge submit deliberation-seal` admits the seal. T-36 (engine-v50, migration 040) refuses `deliberation-seal` when `COUNT(deliberation_counterfactuals WHERE deliberation_id=?)=0`; the receipt-pattern is the substrate proof per DV-S176-1 lesson (when discipline depends on the agent reaching for a tool the substrate could dispatch automatically, ship the substrate dispatch). The prior `seal-grade:` engine_feedback prefix-row clause shipped at DV-S159-1 is superseded; do not author new `seal-grade:` engine_feedback rows.

A *single-frame counterfactual* is a position no perspective took during the deliberation that the synthesis admits as a load-bearing alternative reading — a stance that, if surfaced post-seal by a future reader, would warrant reopening per methodology §Reopen-on-new-reading. For each counterfactual submit one row:

```sh
bin/selvedge submit deliberation-counterfactual --payload '{
  "deliberation_id": <N>,
  "position": "<8-240 char position the deliberation did not take>",
  "why":      "<8-240 char why it would change the synthesis if adopted>",
  "disposition": "addressed-in-synthesis | deferred-to-FR | nilled-by-exclusion",
  "disposition_note": "<synthesis_md anchor (addressed-in-synthesis) | FR alias e.g. FR-S180-1 (deferred-to-FR)>",
  "exclusion_kind":   "preserved-as-divergence | barred-by-constraint | micro-decision | out-of-scope"
}'
```

Disposition-conditional NOT-NULL guards (table-CHECK enforced): `addressed-in-synthesis` and `deferred-to-FR` require `disposition_note`; `nilled-by-exclusion` requires `exclusion_kind`. Exclusion meanings: `preserved-as-divergence` (already a `synthesis_points {divergence,minority}` row), `barred-by-constraint` (recorded constraint/prior-decision/spec-clause cited at convening), `micro-decision` (wording/ordering/naming variant), `out-of-scope` (foreclosed by deliberation scope at convening).

**Cheap-exit nil_attestation.** When the stance-space was exhausted by the perspectives present (typical for tactical or single-axis seals), submit one cheap-exit row with `nil_attestation: 1`, `disposition: "nilled-by-exclusion"`, and `exclusion_kind` set. This encodes "seal-grade: 0 — exclusions applied: <which>" as one substrate row and admits seal — analogous to `audit-step: 0` in §8.5. The substrate refuses `nil_attestation=1` on a deliberation that already has prior counterfactual rows (the cheap-exit must be the only row).

**Authority.** Substrate-gated: T-36 fires inside the same write_tx as `deliberation-seal`. The handler raises `E_REFUSAL_T36` with a refusal text naming the cheap-exit recipe so an agent who hits the refusal can recover with one submit. T-13 (engine-v50, trigger on `deliberation_counterfactuals` INSERT) refuses authoring counterfactuals after seal — they must precede `deliberation-seal` mirroring synthesis_points and perspectives ordering discipline.

**M-1 minority preserved (cites D-23 + D-29 lineage).** P-3's ship-nothing position — that existing `divergence`/`minority` synthesis_points plus methodology §Reopen-on-new-reading already carry the load — is preserved as M-1 minority across both D-23 (DV-S159-1) and D-29 (DV-S180-1). The strongest M-1 insight (presence-gates can reward formulaic one-row compliance while the same synthesizer still misses the real alternative; gates prove receipt presence, not epistemic adequacy) is folded forward as the v2 promotion-trigger: if calibration-EFs surface formulaic-compliance failures of the typed surface, the engine ships stronger gates (item-count thresholds tied to deliberation perspective-count; exclusion-rationale shape checks; disposition-quality audit). Mirrors DV-S152-1 typed-observation→gate progression.

**Forward directions (recorded for v2; not adopted at v1).** P-2 codex's obligations meta-table (`deliberation_obligations` + `seal_grade_items` two-table generic ledger) preserved as forward-direction if a second mandated synthesis artefact graduates — DV-S180-1 is the prior decision to cite for the consolidation deliberation. P-4 anthropic's UNION-view across `synthesis_points {convergence,divergence,minority}` plus `deliberation_counterfactuals` for unified stance-space readers also preserved.

## 5. Record decisions

**Pre-decision precheck (mandatory for kind=substantive | schema_migration; T-33, engine-v49, DV-S179-1, migration 035).** Before submitting a decision-record of kind `substantive` or `schema_migration`, run `bin/selvedge precheck --target-kind decision_v2 --target-key <target_key> --print`. The CLI renders a context pack (similar OIs, prior DVs targeting the same key, active spec clauses, recent supersedes) AND writes a single-use precheck receipt row (`decision_prechecks`); it emits a single-use `nonce` you include in the decision-record payload as `precheck_nonce`. The submit handler verifies the nonce inside the same write_tx (freshness window 30..3600s default 1800s, target-kind + target-key match, context_sha256 recomputation match, single-use consumption); refusal is `E_REFUSAL_T33` with a refusal text naming the exact failure mode. Kind-aware admit predicate: kinds `procedural | calibration | disposition` admit zero-precheck like T-32 admits zero-cite. Cites D-28 + DV-S179-1 + EF-S179-1.

The substrate enforces SHOW-CONTEXT / LIMIT-ENTRY / FORCE-CHECKS through the receipt-pattern shape proven at T-32: row + sha256 + handler dispatch in-band. Cognition is not substrate-detectable; the gate enforces exposure path, not comprehension. Per D-28 C-5 cross-family convergence + DV-S176-1 read-write separation, the precheck CLI emits markdown to stdout AND writes the receipt; the receipt is the substrate proof, the print is presentation; the submit handler not the export tool does the gating.

```sh
bin/selvedge submit decision-record --payload '{
  "title": "<one-sentence decision title, 8-240 chars>",
  "kind": "substantive | schema_migration | calibration | disposition | procedural",
  "precheck_nonce": "<single-use hex from bin/selvedge precheck; required for substantive/schema_migration>",
  "outcome_type": "adopt | reject | defer | supersede | ratify",
  "target_kind": "process_rule | spec_version | migration | issue | review_rule | engine_version | open_question",
  "target_key": "<short key, 2-120 chars>",
  "supports": [
    {"basis": "constraint | operator_directive | prior_decision | review_finding | deliberation | spec_clause | engine_feedback",
     "claim": "<one-sentence support>",
     "cite": "<optional alias to resolve, e.g. DV-S083-2>"}
  ],
  "effects": [
    {"effect_kind": "creates | modifies | supersedes | opens_issue | bumps_engine | closes_issue | adds_migration",
     "target_descriptor": "<short text>",
     "target": "<optional alias>"}
  ],
  "alternatives": [
    {"label": "R-1.1",
     "option": "<the alternative being rejected, 8-240 chars>",
     "rejections": [
       {"basis": "no_feedback_loop | operator_override | violates_gate | too_large_for_session | inferior_tradeoff | preserves_legacy_path | redundant_with_existing | breaks_invariant",
        "reason": "<one-sentence reason, 8-240 chars>",
        "cite": "<optional alias>"}
     ]}
  ]
}'
```

T-18 refuses session-close while a substantive decision lacks support or alternative. T-19 refuses while an alternative lacks a rejection. T-01 refuses unresolved aliases at write time. The label format `R-N.N` (e.g. R-1.1, R-2.3) is enforced by GLOB.

**Cite typing for `supports` and `alternatives.rejections` (cites DV-S158-1, EF-S157-1, DV-S179-1).** The `cite` slot resolves only against `objects.alias` (FK `cited_object_id`). Issues (`OI-...`) live in the `issues` table; forward-reference dispositions (`FR-...`) live in `forward_reference_dispositions`; neither registers in `objects` and so neither can populate `cited_object_id` directly. Migration 021 records the historical residual (24 OI-mentioning + 9 FR-mentioning supports left with NULL `cited_object_id`). At engine-v49, **T-34 (migration 036) refuses NEW `decision_supports` rows with NULL `cited_object_id` when `basis IN (prior_decision, spec_clause, deliberation, review_finding, engine_feedback, constraint, operator_directive)`**; legacy NULL rows are preserved (trigger fires only on INSERT). OI-086-003 closed by-mechanism by DV-S179-1. **T-35 (migration 038) refuses NEW `spec_clauses` rows with NULL `source_decision_v2_id`**; legacy 747 NULL rows preserved. OI-086-001 closed by-mechanism by DV-S179-1. The operator-facing rule is:

- For `basis=engine_feedback`: cite the `EF-S<wno>-<n>` alias (in `objects`), not the `OI-...` it surfaced. Fold the OI reference into claim text.
- For `basis=prior_decision`: cite the `DV-S<wno>-<n>` alias (in `objects`), not the FR or OI it emitted. Fold those into claim text.
- For `basis=spec_clause`: cite the spec section/clause/version object alias (`SPEC-<spec>-v<n>` for the version; sections and clauses register their own aliases).
- For `basis=review_finding | deliberation | constraint | operator_directive`: cite the corresponding object alias only (review_finding, perspective/synthesis_point, constraint atom, decision-record-equivalent).

If you attempt to cite an `OI-...` or `FR-...`, the `_resolve_alias_to_object_id` handler refuses with `E_REFUSAL_T01` and a basis-aware hint naming the alias-kind mismatch and the recovery path. Operators reading the refusal do not need to memorise the table layout; the message recommends the surfacing EF or opening DV.

**Precedent-sensitive provenance check (mandatory at decision-record submit; cites OI-S114-1, DV-S116-1, DV-S117-1, DV-S173-1, DV-S174-1, DV-S175-1, DV-S176-1, OI-S176-1).** The substrate enforces this: the decision-record submit handler walks every cited alias in `supports.cite` ∪ `alternatives.rejections.cite` ∪ `effects.target` in-band inside the same write_tx, inserts a `decision_chain_walks` receipt row per anchor (markdown body + sha256 + edge count + nodes visited + walker_version + truncation_status), and refuses `E_REFUSAL_T32` on any walker exception, unresolved alias, or count mismatch. Engine-v48 ships migration 031 + handler dispatch + T-32. Walk-everything per D-27 C-1+D-1 synthesis: every cited alias triggers a walk unconditionally, no predicate-detection at handler-time. The receipt is the proof object — markdown is presentation, the row + sha256 + edge_count is what audit-readers verify against. P-2 cross-family D-26+D-27 framing: precedent-sensitive provenance, not run-anchor-trace.

**Zero-cite admit.** Decisions with no `supports.cite`, no `alternatives.rejections.cite`, and no `effects.target` admit zero receipts (initial spec-versions, decisions whose claim-text bears the alias references rather than the typed cite slot). The T-32 predicate is `cited_alias_count > 0 AND receipts < cited_alias_count`, not `receipts = 0`.

**CLI surface for tactical reads.** Use `bin/selvedge export --provenance --anchor <alias> --max-depth <N> --print` for session-local reads outside the submit path — `--print` emits the markdown body to stdout with no JSON wrapper and no disk write (FR-S173-1, DV-S174-1). The substrate-side gate handles the load-bearing case (decision-record submit); the export tool handles ad-hoc inspection without mutating substrate (P-2 D-27 read/write separation discipline). `--max-depth` defaults to 3 (hard cap 5); the gate uses the default; widen via `--max-depth N` only at tactical-read time when the chain is sparse.

**Authority and the prose-clauses-without-instrumentation lesson (cites DV-S175-1 backfire, DV-S176-1, S176 operator-named-mandate).** S175 shipped this clause as recommended-only with a watch-FR (FR-S173-3) tracking tactical invocation and a promotion-trigger to substrate-gate via calibration-EF graduation per DV-S152-1 typed-observation pathway. The operator at S176-open named the failure mode immediately: the watch had no substrate measurement (`export --provenance --print` writes no row), the promotion-trigger required calibration-EFs that required the same prose-pattern-match the recommended-clause already failed to ensure, and the compromise produced ceremony without instrumentation. DV-S109-1 ceremony-subtraction was operator-precluded as rejection basis at D-27; the substrate-gate ships now under operator-named-mandate per §1.5 admissibility. The general lesson: when a discipline depends on the agent reaching for a tool the substrate could dispatch automatically, ship the substrate dispatch — prose-and-discipline reproduces the failure modes the kernel defends against.

The `effects` array admits `closes_issue` whose `target` resolves to a citable issue alias (e.g. `"target": "OI-S090-5"`); the handler dispatches `_submit_issue_disposition` inside the same write_tx and transitions the target issue's status to `resolved`. T-27 refuses `closes_issue` effects with NULL `target_issue_id`; T-28 refuses any direct `decision_effects` INSERT bypassing this handler dispatch (per engine-v28).

Symmetrically, the `effects` array admits `opens_issue` whose `target` resolves to an existing issue alias; the handler resolves it to `target_issue_id` and refuses if the issue is not in `status='open'`. Operators register the issue first via `bin/selvedge submit issue` (assigning `alias`, `title`, `priority`) and then reference it from the decision-record. Unlike `closes_issue`, `opens_issue` does not dispatch issue creation in-band. T-31 refuses `opens_issue` effects with NULL `target_issue_id` (per engine-v34).

## 6. Produce — create or revise the artefacts the decisions warrant

This is normal code/spec work. For specs, use `bin/selvedge submit spec-version`, `submit spec-section`, `submit spec-clause`. For migrations, write SQL files under `state/migrations/` and `bin/selvedge migrate --apply`. For CLI/code changes, edit Python under `selvedge/`.

Spec body authoring goes through the substrate too (engine-v29 / OI-S090-5). `submit spec-version` accepts an optional `body_md` field carrying the inline body markdown; the handler validates the body_path against `workspace_root`, computes the sha256, and writes the file in-process *after* the row INSERT succeeds. Use `--payload @file.json` or `--payload -` (stdin) when the body is large; the handler refuses path-traversal escapes, empty/whitespace-only content, and any declared-vs-computed sha mismatch. The legacy two-step (write file via Bash heredoc, then submit with `body_sha256`) remains admitted but is no longer the only path.

**spec-version payload shape (cites OI-S156-2).**

```sh
bin/selvedge submit spec-version --payload '{
  "session_no": <N>,
  "spec_id": "<spec-id>",
  "version": <new-version>,
  "body_path": "specifications/<spec>.md",
  "body_md": "<inline markdown body, required unless using legacy two-step>",
  "supersedes": "<prior alias, e.g. SPEC-methodology-v9>",
  "supersedes_reason_md": "<one-sentence reason>"
}'
```

`session_no` (the open-session number) and `supersedes` (the prior `SPEC-<spec-id>-v<prior-version>` alias) are required for any non-initial version; the handler refuses with `E_NOT_FOUND` if `session_no` does not name an open session, and `E_REFUSAL_T01` if `supersedes` does not resolve. `supersedes_reason_md` is optional but recorded on the resulting `refs` row carrying relation `supersedes`. For an initial version (`version: 1`), omit `supersedes` and `supersedes_reason_md`. T-03 (one active per spec_id) is satisfied by the handler flipping the prior active row to `superseded` BEFORE inserting the new active row, inside the same write_tx (cites OI-S090-4).

**supersession-ledger submit kind (engine-v53, DV-S197-1, OI-S196-2).** Cross-artefact supersession events that span decisions / specs / issues / EFs / OIs are recorded in the typed `supersession_ledger` primitive. Use this kind when a new substrate object supersedes, replaces, narrows, bounds, or retracts a prior one — at any object_kind, not only spec-version supersession (which `refs.relation='supersedes'` continues to carry as a compatibility channel for spec-version-handler internals).

```sh
bin/selvedge submit supersession-ledger --payload '{
  "source": "<alias of the new/superseding entity>",
  "target": "<alias of the old/superseded entity>",
  "relation_kind": "supersedes-fully | supersedes-partial | bounded-by | replaces-mechanism | retracted-by",
  "reason": "<8-480 char reason atom>",
  "cite": "<optional alias of authoring decision_v2 or other authority>"
}'
```

The handler resolves source/target/cite via `_resolve_alias_to_object_id` (objects.alias graph), refuses self-supersession (CHECK source!=target), refuses duplicate (source,target,relation_kind) edges (UNIQUE), pins the reason as a `support_claim` text_atom (8-480), and registers the ledger row as a first-class object with alias `SL-S<wno>-<seq>` so it participates in chain-walks T-32. Refusals: `E_VALIDATION` (missing/bad enum, self-supersession), `E_REFUSAL_T01` (unresolved alias), `E_ATOM_LENGTH` (reason outside 8-480), `E_REFUSAL_CHECK` (duplicate edge or source==target).

**Relation enum semantics (closed CHECK; D-S197-1 D-1 P-1 stance adopted; P-3 4-value tighter set preserved as M-1 minority + watch-trigger).**
- `supersedes-fully` — new fully replaces old; old's authority is migrated.
- `supersedes-partial` — new replaces some scope of old; old retains other scope.
- `bounded-by` — new bounds the old's interpretation; the old still applies in its now-bounded shape (e.g. EF-S196-2 bounds DV-S190-2 graduation-discipline scope).
- `replaces-mechanism` — new replaces a specific mechanism of the old while preserving the old's broader frame.
- `retracted-by` — old is withdrawn entirely; new is the retraction record (no replacement substantive content).

**Soft-deprecation of `decision_effects.effect_kind='supersedes'` (D-S197-1 D-3).** The legacy channel remains admissible at v1 for historical replay, but **new supersession events should be recorded via `submit supersession-ledger`** rather than as `decision_effects` rows. The decision-record handler does not auto-route at v1; this is operator/agent-policed per DV-S109-1 ceremony-subtraction posture. Watch-trigger per M-1 minority (D-S197-1): if dual-channel writes persist or the ledger receives 0 inserts across N≥5 future sessions, the next session opens a gate-promotion `OI` for either hard-cutover migration (drop the `supersedes` value from `decision_effects.effect_kind` CHECK) or handler-side auto-routing.

**Polymorphism via objects-FK (D-S197-1 C-1).** `source_object_id` and `target_object_id` are FKs into `objects.object_id`; no `source_kind`/`target_kind` discriminator columns. Any registered object alias (DV-/SPEC-/EF-/SL-/A-/P-N-N-/etc.) is admissible. C-4 stakeholder-event origin reference is omitted at v1; the C-4 primitive (when shipped) will add an `origin_event_id` FK column without re-shaping the existing schema.

## 7. Validate — and run the coding review loop on any code change

If the session produces, modifies, or deletes executable logic (Python under `selvedge/`, SQL migrations, shell logic under `bin/` or `tools/`), invoke a reviewer subagent — distinct from the implementer — to audit the change. Address every medium-or-higher finding and re-invoke until the reviewer reports clean.

```sh
# For each finding the reviewer surfaces:
bin/selvedge submit review-finding --payload '{
  "iteration": 1,
  "severity": "critical | high | medium | low",
  "finding": "<one-sentence problem statement>",
  "target": "<optional alias to the affected object>",
  "disposition": "open | fixed | adjudicated",
  "disposition_text": "<optional disposition text>"
}'

# To update disposition after addressing:
bin/selvedge submit finding-disposition --payload '{
  "review_finding_id": <id>,
  "disposition": "fixed | adjudicated",
  "disposition_text": "<substantive reason or commit reference>"
}'
```

T-20 refuses session-close while any review_finding has `disposition='open'` and `severity` in (critical, high, medium). The Agent tool with `subagent_type=Explore` and an adversarial prompt is the default reviewer invocation.

If the loop reaches a fourth iteration without converging, halt the session: open an `OI-<workspace_no>-<slug>-findings-unresolved` issue and close in halted state per the methodology spec.

## 8. Record — provenance committed to the substrate

Already done by every prior `submit`. Run `bin/selvedge query` to confirm row counts before close.

## 8.5 Close-time reflection (mandatory)

Before submitting `close-record`, do four things:

1. **Author at least one `engine_feedback` row** capturing what reduced friction this session and what surfaced as friction. Successes worth reinforcing belong here as much as corrections — both signals decay if they only live in working memory. Use `flag` ∈ `observation | reframe | calibration | blocker`.

   ```sh
   bin/selvedge submit engine-feedback --payload '{
     "flag": "observation",
     "body_md": "**<headline>** — what reduced friction; what surfaced as friction; proposed remedy if obvious."
   }'
   ```

2. **Dispose forward-references this session addressed.** Run `bin/selvedge orient` and for each `FR-S<wno>-<seq>` the session resolved, submit a disposition citing the resolving decision/spec/handler:

   ```sh
   bin/selvedge submit forward-reference-disposition --payload '{
     "target_session": <wno>, "seq": <n>,
     "note": "addressed by DV-S<NNN>-<n> (<short reason>)"
   }'
   ```

   Disposition removes the item from `orient`'s queue. Without this, the same forward-reference re-surfaces every session.

3. **Dispose engine-feedback rows this session addressed** (if any), citing the resolving decision:

   ```sh
   bin/selvedge submit engine-feedback-disposition --payload '{
     "alias": "EF-S<NNN>-<n>",
     "disposition": "addressed-by-DV-S<NNN>-<n> (<short reason>)"
   }'
   ```

4. **Audit load-bearing interpretive choices** made during the session and either lift each into the assumption_register (`A-NNN`) or defer it via a self-review forward-reference. See *Close-time interpretive-choice audit* below for definition, exclusions, payload shape, and the promotion trigger.

### Temporal-claim grounding (applies to every submit body)

Any duration, elapsed-time, recency, or sequence claim used as evidence in a submit body — `engine_feedback.body_md`, `assessments.state`, `close_records.summary`, decision-record support claims, alternative-rejection reasons, perspective bodies, synthesis text — must be grounded against substrate timestamps before commit, or omitted entirely.

Concretely: if you are about to write a phrase like "the N-month gap", "X hours since", "after S<wno>", "recently", or "long-running", run the cheap query first, e.g.

```sh
bin/selvedge query "SELECT workspace_session_no, opened_at, closed_at FROM sessions WHERE workspace_session_no IN (110, 126)"
```

and read the elapsed time off the data. The "ground or omit" rule has no "unverified estimate" escape valve: if the claim is load-bearing, the substrate query takes seconds; if it isn't load-bearing, drop the phrase. The substrate's provenance warrant rests on recorded claims being read off data, not generated to fit narrative.

Scope: every submit body, not engine_feedback only — the failure mode is general (narrative-driven number-fitting can land in any prose surface). Substrate-side static checks on freeform `body_md` are impractical, so this discipline is operator/agent-policed; calibration-EFs are the recovery path when slips are caught. Cites EF-S127-1 (calibration of EF-S126-1's fabricated 4-month-gap claim).

### Close-time interpretive-choice audit (mandatory; cites DV-S155-1)

The audit is the §8.5 item-4 closure of OI-S154-2 (HIGH) and OI-S154-3. Peer evidence at disaster-recovery arc S017 measured 11-of-25 plan-prose statements acting on never-lifted `A-NNN` assumptions; the audit is the kernel response.

**Definition.** A *load-bearing interpretive choice* is a choice that was needed to justify a session's plan, prose, spec text, or decision-record content, and that is **not already carried by an existing substrate row**. The exclusion list below is exhaustive; if a choice does not satisfy at least one exclusion, it is in scope.

**Exclusions (the choice is NOT load-bearing for audit purposes if any holds):**

- The choice is reflected in a committed spec row (spec_clause, spec_section, spec_version body) authored or cited by this session.
- The choice is resolved by citing an existing `A-NNN` row in the assumption_register.
- The choice is covered by a closed forward-reference, a closed open-issue, or a sealed deliberation-synthesis the session cited.
- The choice is a micro-decision (wording, ordering of bullets, local naming) whose alteration would not change the session's substantive outcome.

**Payload shape.** Submit one `engine_feedback` row with `flag='observation'` and headline prefix `audit-step:`. The body enumerates each load-bearing choice and its disposition. Each choice receives one of three dispositions: **lifted-to A-NNN** (the choice was promoted to a registered assumption — cite the `A-NNN` row), **deferred-to FR-S<wno>-<seq>** (the choice needs future revisit — cite the forward-reference), or **accepted-implicit** (the choice is acknowledged unregistered — cite the reason, drawing on the exclusion list to justify why no lift or FR is warranted).

```sh
bin/selvedge submit engine-feedback --payload '{
  "flag": "observation",
  "body_md": "**audit-step:** <count> load-bearing interpretive choices.\n\n1. <choice>: lifted-to A-<n> (<short reason>).\n2. <choice>: deferred-to FR-S<wno>-<seq> (<short reason>).\n3. <choice>: accepted-implicit — <which exclusion applied and why>.\n\nIf no load-bearing choices remain after exclusions, state: **audit-step:** 0 — exclusions applied: <which>."
}'
```

If a choice is lifted, submit the `A-NNN` row first (`bin/selvedge submit assumption ...`) and cite its alias in the audit body. If a choice is deferred, submit the `FR` first (`bin/selvedge submit forward-reference ...`) and cite its alias in the audit body. The audit row is the inventory; the lifts and FRs are the substantive substrate work.

**Plan-time discipline (cites M-2 of D-21; carries P-3's warning).** The audit is recovery, not prevention. The primary discipline is to lift `A-NNN` rows *while authoring* plan-prose, deliberation-output, or spec text — not at close. The close-time audit catches what plan-time discipline missed; it does not substitute for it.

**Authority.** This clause is operator/agent-policed. The substrate does not gate `session-close` on audit-row presence at engine-v46. Calibration-EFs are the recovery path when a reader notices a missed audit or a missed lift after close (mirrors temporal-claim grounding).

**Promotion trigger to substrate gate.** If a future session-close lands without an audit row AND a downstream session opens a calibration-EF naming the prior session as having shipped on an unlifted load-bearing assumption, the next session opens a gate-promotion `OI` and the engine ships a T-NN refusing `session-close` on audit-row absence. This is the v2 graduation path; the typed-observation→gate progression follows DV-S152-1's typed-conflict-primitive precedent.

**Scope limits (cites C-1 of D-21).** This audit covers session-close, not deliberation-seal. The deliberation-seal sibling — single-frame counterfactual grading — ships in §4 as `Seal-time deliberation-grading` per DV-S159-1 (closing OI-S154-5 by-mechanism); the two clauses are coordinated but mechanically distinct (different trigger, different actor, different evidence shape).

## 9. Close

```sh
bin/selvedge submit close-record --payload '{
  "summary": "<one-sentence summary of what shipped>",
  "items": [
    {"facet": "engine_version", "text": "engine-vN to engine-vM."},
    {"facet": "what_was_done", "text": "<atom>"},
    {"facet": "state_at_close", "text": "<atom>"},
    {"facet": "open_issues", "text": "<atom>"},
    {"facet": "next_session_should", "text": "<atom>"},
    {"facet": "validator_summary", "text": "<atom>"}
  ]
}'

bin/selvedge submit session-close --payload '{}'
```

`session-close` refuses (E_REFUSAL_T39, engine-v41) when no `close_records` row exists for the session — submit `close-record` first and check its return code before invoking `session-close`. Atom-bearing fields are pre-validated at submit time and surface structured `E_ATOM_LENGTH | NEWLINE | CR | FENCED_CODE | PIPE_TABLE` codes (DV-S134-1, mirroring the `text_atoms.text` CHECK and T-21). Author calibration `engine-feedback` rows *before* `session-close`; the table requires an open session, so post-close calibration must wait for the next session-open.

The substrate auto-fills `engine_version_at_close` from `workspace_metadata.current_engine_version`. If the engine version bumped during the session, run an UPDATE on the metadata row before close (or include it in the version-bumping migration).

Then export and commit:

```sh
bin/selvedge export --session <workspace_session_no> --write
bash tools/validate.sh
git add -A && git commit -m "<message>" && git push
```

The export materialises `provenance/<workspace_no>-<slug>/00-assessment.md`, `01-deliberation.md`, `02-decisions.md`, `03-close.md`, `04-review.md` deterministically from substrate rows. Git history is the cross-machine durable record; `state/selvedge.sqlite` is per-workspace and rebuildable from migrations + the markdown exports.

## Cautions for self-development

- **Don't import ideas from outside the process.** Surface external insight as a hypothesis to deliberate, not a commitment. The methodology's value is traceability of artefacts to the reasoning that produced them.
- **Don't silently re-propose what was rejected before.** Cite the prior rejection by `decision_v2` alias and explain what changed.
- **Don't accumulate ceremony.** Each addition to the engine should pay for itself in capability.
- **Don't trust your own judgment alone on changes to how the methodology works.** Convene cross-family perspectives.
- **Be willing to subtract.** Most of what Selvedge accumulated late was ceremony.
- **Don't author markdown for session state.** Substrate-only.
- **Don't track counters in prose.** Counts come from `bin/selvedge query`. Atoms forbid pipe-tables and fenced code by construction.
