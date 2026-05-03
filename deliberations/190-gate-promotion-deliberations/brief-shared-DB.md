# Shared brief — D-B: L5 close-time substrate-filesystem divergence gate (S190)

> The following sections are **byte-identical** across all perspectives of D-B. Only the role-specific `STANCE` section at the end of each per-perspective brief differs.

## Methodology context

You are one of 4 perspectives convened in **S190 of the Selvedge self-development workspace** (`/Users/ericmccowan/Development/complex-systems-engine`). Selvedge is a methodology-and-substrate engine — perspectives reason together, durable artefacts are produced, reasoning is preserved as substrate rows in `state/selvedge.sqlite`, the engine evolves by running its own mechanic on its own outputs.

The substrate is the only writable surface for session state. Markdown in `provenance/` is a generated export from substrate rows. Every session phase is `bin/selvedge submit <kind>`. Atoms are 8–240 chars, no newlines, no fenced code, no pipe tables.

Current engine version is **engine-v52**. Migrations 001..044 are applied. Read these for context:
- `selvedge/export/session.py` — `_export_session_provenance` function; the L5 stale-file reconciliation lives at lines 358-409. Pay attention to the order: reconcile manifest BEFORE unlink, comment lines 399-402 names the failure mode.
- `selvedge/export/manifest.py` — `record_manifest_entry` and `export_manifest` table schema (engine-v52, OI-S081-7, migration 044). Substrate-side recovery index recording session_no + kind + path + sha256 + size_bytes + row_count + generated_at per emitted file.
- `selvedge/submit/session.py` `_submit_session_close` (~line 78) — current handler for `bin/selvedge submit session-close`; substrate-only update (`UPDATE sessions SET status='closed'`); does NOT call export and does NOT check filesystem.
- `prompts/development.md` §9 — the operator-facing close discipline: `session-close` → `bin/selvedge export --session N --write` → `bash tools/validate.sh` → `git add -A && git commit && git push`. The export is the operator-policed step that materialises markdown from substrate; it can be skipped by an inattentive close.
- T-39 (engine-v41): SQL trigger refusing session-close when no `close_records` row exists. Existing substrate-gate sibling on the close path.
- DV-S081-1 substrate-loss-defense-v1, DV-S188-1 export_manifest substrate-side recovery index landing — the "substrate is canonical, markdown is recoverable" architecture.

## Problem statement

The L5 close-time export expansion (DV-S187-1, S187) added 5 session-bounded files (05-engine-feedback / 06-counterfactuals / 07-fr-dispositions / 08-prechecks / 09-chain-walks) plus workspace-wide spec_versions index. Stale-file reconciliation is in-place: when the substrate state no longer projects an L5 file (rows deleted, decisions superseded), `_export_session_provenance` reconciles `export_manifest` then unlinks the on-disk file. This works *when the export runs*.

The reconciliation depends on the operator running `bin/selvedge export --session N --write` between `session-close` and `git add`. The handler does not call export; T-39 only requires `close_records` to exist; nothing prevents `session-close` followed directly by `git commit` of stale on-disk markdown that no longer matches the substrate state.

S187 reviewer iter-1 surfaced this gap (finding 28: harness-file reconciliation; finding 30: workspace-wide idempotency). Finding 30 was fixed in-session; finding 28 was deferred to FR-S187-15 with cross-session anchoring noted as scope-distinguishing. FR-S187-16 then explicitly named the substrate-side gate as a future-session consideration: "promoting the L5 stale-file reconciliation pattern into a substrate-side gate refusing session-close on detected divergence between filesystem and substrate-projected file set." FR-S188-15 reaffirmed the consideration at S188 close.

The architectural question is whether substrate should refuse `session-close` when the on-disk session-bounded files do not match what the substrate would project — and if so, how the check is implemented given that SQLite triggers cannot read filesystem (so the gate must live in the Python submit handler, not as a SQL trigger).

The deliberation's question: should the close-path move from operator-policed (export-then-commit discipline in §9) to substrate-policed (handler-side filesystem walk + sha256 verification against `export_manifest` rows + refusal on divergence)?

## Adjacent precedents (cite-in-position when load-bearing)

- **DV-S176-1** at S176: T-32 substrate-gate for chain-walks. The lesson preserved: "when discipline depends on the agent reaching for a tool the substrate could dispatch automatically, ship the substrate dispatch — prose-and-discipline reproduces the failure modes the kernel defends against." Cuts *for* the gate.
- **DV-S180-1** at S180: T-36 substrate-gate for deliberation-counterfactuals at seal. Same shape — substrate enforces a presence check at a write-time event. Cuts *for*.
- **DV-S109-1** at S109: ceremony-subtraction discipline. "Each addition to the engine should pay for itself in capability." Cuts *against* — every new gate is mechanism whose payment must be evident.
- **DV-S188-1** at S188: export_manifest table landed. The substrate-side recovery index is the data structure a divergence gate would query. Cuts *for* (the substrate now has the data) and *against* (ship export_manifest first, observe whether divergence happens, gate later).
- **T-32 receipt-pattern**: row + sha256 + edge_count is the proof object; markdown is presentation; handler dispatch in-band inside the same write_tx. The model for any new gate's enforcement.
- **No recurrence-pressure**: from S187 (the reconciliation pattern landed) to S189 (last close), the export step has run cleanly each session. No calibration-EF has named a divergence-on-commit landing. The promotion-trigger framing in DV-S152-1 / DV-S159-1 graduation precedent waits for recurrence pressure.

## Design questions

You are asked to author a position covering each of the following:

**Q1 (graduate or status-quo).** Should the close-path move from operator-policed (§9 prose: "run export --write before commit") to substrate-policed (handler refuses session-close on divergence)? Engage DV-S176-1 lesson honestly — does it apply here, or is the export-then-commit discipline already adequately operator-policed because `tools/validate.sh` runs after export and would surface divergence? Take a position.

**Q2 (gate placement, if shipping).** SQLite triggers cannot read filesystem. The gate must live either in (a) the Python `_submit_session_close` handler doing a filesystem walk + sha256 comparison against `export_manifest` rows, or (b) a precondition checked by `bin/selvedge export --session N --write` and stored as a substrate row that `_submit_session_close` then queries (similar to T-32 chain-walk receipts), or (c) a `tools/validate.sh` extension (still operator-policed). Pick a placement and defend it. The substrate-receipt-pattern (b) is closest to the T-32 model.

**Q3 (gate semantics).** What constitutes divergence? Options: (i) a file in `export_manifest` that does not exist on disk; (ii) a file on disk under `provenance/<wno>-<slug>/` not in `export_manifest`; (iii) a sha256 mismatch between disk and `export_manifest`; (iv) a file the dry-run export would now generate that is not on disk (substrate-projected vs filesystem-actual). Pick which divergence shapes the gate refuses on, and which it tolerates. Address universal-mandatory vs cheap-exit (e.g. a `--no-divergence-check` escape hatch for cross-machine workflows; mirror DV-S180-1 nil_attestation cheap-exit pattern).

**Q4 (subtraction discipline).** What concretely gets subtracted from `prompts/development.md` §9 if your design is adopted? If the substrate enforces export-before-close, the §9 prose instruction becomes redundant — name what gets removed. If you propose status-quo, name what evidence would change your position.

**Q5 (false-positive / over-fitting risk).** Substrate-gates that fire on legitimate `session-close` calls produce ceremony at best and refusal-debt at worst. Concretely: (i) cross-machine workflow where one machine substrate-edits and another runs export; (ii) operator deliberately editing a file post-export then closing without re-export; (iii) export_manifest rows for a previous session's files getting touched by other tooling; (iv) race between concurrent processes (cf. EF-S185-2 concurrent-pytest race). Name the false-positive shape and the recovery path. Engage honestly with M-1's strongest insight from D-23: gates prove receipt presence, not epistemic adequacy.

**Q6 (constraint discharge).** Selvedge defends against six failure modes (preserved in `bin/selvedge orient`'s "Why this engine exists" packet from retired `constraints.md` v1):
1. Loses foundational instructions under context pressure.
2. Anchors on most-recent-prior-decision over foundational specification.
3. Confuses authority of speakers.
4. Generates narrative-fitting numbers when substrate values exist.
5. Defaults to mechanism-addition over mechanism-subtraction.
6. Drifts into ceremony when each addition does not pay for itself.

For your proposed design (or status-quo), name how it discharges or fails to discharge each. Lean into #5 and #6 explicitly — both cut against new mechanism on a zero-recurrence observation.

## Evidence base

- **DV-S187-1** at S187: L5 close-time export expansion shipping the 5 session-bounded files + workspace-wide spec_versions index + stale-file reconciliation pattern.
- **DV-S188-1** at S188: engine-v52 marker via migration 044 coupling snapshot_catalog deliberation_seal trigger plus export_manifest recovery index. The export_manifest table is the substrate-side data the gate would query.
- **FR-S187-16** + **FR-S188-15**: explicitly name the substrate-side gate consideration. "Promoting the L5 stale-file reconciliation pattern into a substrate-side gate refusing session-close on detected divergence between filesystem and substrate-projected file set."
- **FR-S187-15**: harness-file reconciliation in `_export_session_provenance` with cross-session anchoring (sealed harness files live under OPENING session dir, not the exporting session dir). Adjacent — same divergence-class but cross-session anchored. Engage whether your gate handles cross-session-anchored files.
- **`_export_session_provenance`** (lines 358-409): the existing reconciliation. Reads `out_dir.exists()`, walks L5_FILENAMES, deletes manifest row before unlink (line 399 comment names the failure mode if order reverses).
- **`_submit_session_close`** (lines 78-115): substrate-only handler. No filesystem read.
- **T-39**: SQL trigger refusing session-close when no `close_records` exists. Existing close-path substrate-gate sibling.
- **EF-S185-2** at S185: concurrent-pytest race wiped primary substrate; recovery via session-open-snapshot. Cross-process race is a real failure shape; engage how a divergence gate behaves under concurrent-process pressure.
- **No recurrence**: from S187 (DV-S187-1 reconciliation landed) to S189 (last close), no calibration-EF has named a stale-file-on-commit landing. 3 closes have run with the reconciliation working.

## Response format

Author a markdown body with **exactly these labeled sections** (the capture subagent decomposes against these labels):

```
**Position.** <one paragraph distillation, 8–240 chars, will become the perspective-position atom.>

**Schema sketch.**
- <bullet, what tables/columns/triggers your design adds or modifies, ≤240 chars>
- ...

**CLI surface.**
- <bullet, what new bin/selvedge subcommands or flags this introduces, or "none" if no CLI change, ≤240 chars>
- ...

**Migration path.**
- <bullet, in what order migrations + handler edits + spec edits ship, ≤240 chars>
- ...

**What not.**
- <bullet, what this proposal explicitly excludes from scope, ≤240 chars>
- ...

**Open questions.**
- <bullet, what you cannot resolve within your stance, ≤240 chars>
- ...

**Risks.**
- <bullet, false-positive shape + recovery path for each major addition, ≤240 chars>
- ...

**What lost.**
- <bullet, what is forfeit if your proposal is adopted, ≤240 chars>
- ...
```

Each bullet must be a single sentence, ≤240 chars, no newlines, no fenced code, no pipe tables. The substrate atom triggers refuse all three; do not embed.

When you reference an OI/DV/EF/FR alias, use the canonical form (`OI-S081-6`, `DV-S187-1`, `EF-S185-2`, `FR-S187-16`). Do NOT cite OI- or FR- aliases in any typed-cite slot of any future decision-record (T-01 / cite-typing rule); fold them into claim text instead.

## Constraint on external imports

Per `specifications/methodology.md` §Cautions, **do not import ideas from outside this engine's process** as commitments. If you have an external concept (a pattern from another framework, a database design from a textbook), surface it as a hypothesis to deliberate inside your position — name it, name where it came from, name what evidence in *this workspace* supports it. Unsourced external claims are discipline failures.

## Output target

Write your full position to `/Users/ericmccowan/Development/complex-systems-engine/deliberations/190-gate-promotion-deliberations/perspective-B-<N>.json` where `<N>` is your perspective number (provided in your role section). The JSON shape is:

```
{
  "deliberation_id": <DB_ID>,
  "label": "P-<N>",
  "family": "<anthropic | openai | google | other-llm | human>",
  "stance": "<short stance phrase, 8–240 chars>",
  "body_md": "<full markdown body>"
}
```

The orchestrator will provide the actual `<DB_ID>` in your role brief once `deliberation-open` has been called.

Then submit:

```
bin/selvedge submit perspective --payload @deliberations/190-gate-promotion-deliberations/perspective-B-<N>.json
```

**Do not run `git commit`, `git push`, `git add` for the purpose of staging-to-commit, or any commit-like operation.** The orchestrator commits at session-close after `bin/selvedge export --write`.

**Do not run any destructive substrate operation against the primary substrate at `state/selvedge.sqlite`**: no `bin/selvedge init` (with or without `--force` / `--really-force`), no `bin/selvedge migrate --apply`, no direct `sqlite3` write/`.recover`/`UPDATE`/`DELETE`/`DROP`/`ALTER`/`PRAGMA writable_schema` against the primary file, no `rm`/`mv` of `state/selvedge.sqlite*`, no edits to files under `state/migrations/`. If your task appears to require any of these, halt and report.

You are perspective P-&lt;N&gt;. Your role-specific stance follows below.
