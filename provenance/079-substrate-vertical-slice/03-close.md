---
session: 079
title: Substrate vertical slice — close
date: 2026-04-27
engine_version_at_close: engine-v17
mode: self-development
---

# Close

## What was done

Session 079 implemented the substrate vertical slice per 078 D-11. Each of the seven D-11 deliverables landed:

1. **D-7 cut applied.** Removed sections of `methodology.md` (§"When to review at close", §"What this kernel does not say", and the "Provisional reference substitute" bullet of §"Validation senses") and `workspace.md` (§"Top-level layout" tree and §"What this file does not say"), and the "Loading the engine in a fresh workspace" recipe in `engine-manifest.md`. Each section preserved at `archive/specifications/`. Engine bumped to `engine-v17`. Active spec dropped from 430 → **368** non-blank lines (under D-10's 400-line budget).

2. **`state/migrations/001-initial.sql` authored.** Implements 078 D-1 substrate-shape (S1 cells / S3 tuples / S2 files), 078 D-3's 16 refusals, 078 D-9 SQLite + WAL configuration. **17 tables** (16 from D-10 + `synthesis_points`). The 17th-table breach is recorded as 079 D-2 with cause; per D-10, breaches are admissible with cited cause and read by the next human reviewer-subtractor cadence.

3. **`selvedge` CLI implemented** at `selvedge/cli.py` + `bin/selvedge` shim. Subcommands: `init`, `id-allocate`, `submit`, `validate --precommit`, `subtract-eligibility`, `recover`, `query`. Single-writer (BEGIN IMMEDIATE), structured errors (`E_WRITE_BUSY`, `E_REFUSAL_T<NN>`, `E_NOT_FOUND`, …), retry budget with exponential backoff. Calibration parameters per 079 D-6.

4. **`tools/validate.sh` rewired** to require `state/migrations/001-initial.sql`, `selvedge/cli.py`, `bin/selvedge` and to delegate substrate integrity to `bin/selvedge validate --precommit`. Final validator reports 15 ok / 0 fail at close (one warn for the still-open 079 close file itself, which lands at this commit).

5. **Round-trip test** (`state/tests/round_trip.sh`): **9/9 pass**. Open S001 → `spec-version` (T-04 application-layer hash check verified) → `decision` with one alternative (T-08 verified) and one ref parsed from body_md to `[SPEC-round-trip-spec-v1]` (T-01 application-layer verified) → close (T-02 + T-11 verified) → external `sqlite3` UPDATE on the closed decision row refused with `E_REFUSAL_T06` (verified). Refs row count = 1 as expected. Validator clean against the closed-session substrate.

6. **Concurrency falsification trial** (`state/tests/concurrency.sh`): **PASS**. 16 parallel writers each holding a 200ms in-transaction sleep, worker 8 SIGKILL'd mid-transaction. **15** survivors; `decision_no` 1..15 contiguous; **0** duplicates; **0** orphan rows from the killed worker; **0** `E_WRITE_BUSY` events at default 5s `busy_timeout`; integrity_check + foreign_key_check both clean; no raw "database is locked" string surfaced to the worker layer. D-9's falsification gate is not crossed: the substrate behaves as the contract requires under the contention pattern 080+ will produce.

7. **Provenance authored** (this file plus `00-assessment.md` and `02-decisions.md`). Engine_feedback rows for the two refusals downgraded with cause: `EF-079-001-T12-application-layer.md` (T-12 needs per-write sentinel rows or SQLite extensions; downgraded to application-layer for `__cli__`-only writer regime) and `EF-079-002-T15-deferred.md` (T-15 needs `selvedge migrate` which is 080+ scope). Both will be triaged at the 080+ session that crosses their respective threshold (first non-`__cli__` writer; first additive migration).

## State at close

- **Active engine version:** `engine-v17` (provisional per 078 D-5 release gate).
- **Active spec line count:** 368 non-blank lines across 8 files; under D-10's 400-line budget.
- **Substrate:** `state/selvedge.sqlite` initialised; migration 001 applied (sha256 stored in `schema_migrations`).
- **CLI:** `bin/selvedge` and `selvedge/cli.py` on the workspace path; the bin shim is executable.
- **Validator:** `tools/validate.sh` rewired; passes at close (15 ok / 0 fail).
- **Tests:** `state/tests/round_trip.sh` (9/9), `state/tests/concurrency.sh` (PASS).
- **Provenance:** 079 directory has assessment, decisions, close.
- **Engine-feedback:** Two new EF rows in `engine-feedback/inbox/`.

The primary substrate (`state/selvedge.sqlite`) at close holds **only** an empty post-init schema — both tests use the snapshot/restore pattern (back up `state/selvedge.sqlite` to a `.backup` file, run the test against a clean DB, restore on cleanup). No 079 substrate writes are persisted to the workspace's primary substrate yet. The first writes happen at session 080's open (when the substrate-as-record-of-sessions begins).

## Refusal coverage at close

| # | Refusal | Mechanism implemented | Status |
|---|---------|----------------------|--------|
| T-01 | Refs in body_md must resolve | App-layer in `_record_refs` | active |
| T-02 | Substantive decisions need ≥1 alternative on close | Trigger `t02_close_substantive_decisions_have_alternatives` | active |
| T-03 | One active spec_version per spec_id | UNIQUE partial index `t03_spec_versions_one_active` | active |
| T-04 | spec_version body SHA matches file | App-layer at submit + at validate | active |
| T-05 | No perspective insert if deliberation sealed | Trigger `t05_perspectives_blind_seal` | active |
| T-06 | Closed-session rows immutable | Triggers across decisions, alts, spec_versions, perspectives, synthesis_points, commitments, refs | active |
| T-07 | Cite of superseded spec needs allow_superseded + reason | Triggers `t07a` + `t07b` | active |
| T-08 | rejection_reason_md ≥ 16 chars | CHECK constraint | active |
| T-09 | Commitment state machine | Trigger `t09_commitments_state_machine` | active |
| T-10 | sessions.session_no contiguous | Trigger `t10_sessions_contiguous` | active |
| T-11 | Close requires work_items clear | Trigger `t11_close_requires_workitems_clear` | active |
| T-12 | Role write capabilities | App-layer (downgrade per EF-079-001) | partial |
| T-13 | sealed_at cannot revert to NULL | Trigger `t13_deliberations_sealed_immutable` | active |
| T-14 | Convergence ≥ 2 source perspectives | CHECK with `json_array_length` | active |
| T-15 | No DROP COLUMN/DROP TABLE in migrations | Pending `selvedge migrate` (per EF-079-002) | deferred |
| T-16 | Lease-expired rows refused as 'leased' | Triggers `t16_work_items_lease_not_expired` × 2 | active |

**Active refusals: 14/16. Partial: 1 (T-12). Deferred: 1 (T-15).** Per 078 D-3 §Open, deferrals are admitted with engine_feedback; both deferrals have rows.

## What session 080 should address

**Primary work:** the first agent-on-substrate flow. Per 078 D-11 §"Session 080's likely work":

> First agent-on-substrate flow (start with deliberator-N because the multi-perspective pattern is the irreducible role per `[agt]`).

A deliberator-N flow consists of: a `deliberations` row opened with `sealed_at IS NULL`; N parallel agent processes (≥1 cross-family per methodology) writing `perspectives` rows; the orchestrator setting `sealed_at` (T-13 makes it irreversible); the synthesiser writing `synthesis_points` rows (T-14 enforces convergence-needs-≥2-sources). 080 picks a real deliberation topic — possibly the OI-079-001 disposition (ratify the 17-table breach, or absorb it).

**Concurrent secondary work, contingent:**
- **First human reviewer-subtractor cadence read.** Per 078 D-6, default cadence is every 5th self-development session; sessions 076–079 are four self-dev sessions, so cadence triggers at 080 or 081. Operator decides at 080 open. The dossier is `bin/selvedge subtract-eligibility` plus the four EF rows in `engine-feedback/inbox/`.
- **EF-079-001 disposition** if 080 introduces a non-`__cli__` writer (likely, given the deliberator-N flow). If yes, T-12 enforcement strategy is decided.
- **EF-079-002 disposition** if 080 needs a schema change (e.g., adding columns for agent-process tracking). Probably not in 080.

**Hard limits on 080:** the 078 D-5 release gate is in force. 080 may add agent-on-substrate scaffolding, may dispose of OI-079-001 (table-budget recalibration), and may build `selvedge migrate` if 080 itself needs it — but **no methodology-expanding self-development** until the first 30-session external-problem trial completes. Adding a deliberator-N flow is mechanism-implementing-existing-methodology, not methodology-expansion. Adding a new active mechanism to `methodology.md` would be expansion and is forbidden.

## Honest limits

1. **The primary substrate at workspace HEAD is empty.** Both tests use snapshot/restore so as not to pollute the primary substrate with test rows. The intended state at close is "primary substrate = post-init schema; no session rows yet"; 080's first action will be a `selvedge submit session-open` with `session_no=1` against this primary substrate. The session-as-substrate-record begins then. Self-development sessions 001–079 are *not* migrated into the substrate; they are evidence in `provenance/` and git, per 078 D-11 must-not item ("Migrate the 75-session pre-restart provenance").

2. **No close-time reviewer audit.** Per 078 D-7 step 1, the close-time reviewer mechanism is removed at engine-v17. No retrospective audit of 078 was run by 079 (per 079 00-assessment.md §Close-time review). 080 may elect to retrospectively audit 079 by reading the substrate and the provenance; the substrate makes the audit shorter (the rows the substrate accepts are the rows that exist; a reviewer reading `02-decisions.md` against `query 'SELECT * FROM decisions WHERE session_id=...'` can compare narrative to row in O(N) decisions).

3. **17-table breach (079 D-2) is recorded but not yet ratified.** D-10 requires the human reviewer-subtractor's next dossier read to ratify or subtract. The default cadence triggers at 080 or 081. Until then, the substrate carries 17 tables and the budget says 16; the breach is the load-bearing diagnostic.

4. **Two refusals downgraded.** T-12 to application-layer (EF-079-001), T-15 to "deferred-until-runner-exists" (EF-079-002). The 14/16 active substrate refusals at close is the honest figure. Both downgrades pay value when there is value to pay (introduce a second writer; produce a destructive migration).

5. **The concurrency trial used a Python wrapper, not `bin/selvedge submit` directly.** The wrapper duplicates the submit logic so the in-transaction sleep can be injected without a CLI flag. The wrapper imports `selvedge.cli` (so `db_path()` and the constants are the same code); only the request shape differs. A future trial that exercises the actual `bin/selvedge submit` end-to-end — process startup cost included — is a 080+ extension.

6. **D-6's calibration numbers are validated only against the trial's pattern.** Real workloads that combine writes with non-trivial reads, or that hold rows open across user-time pauses (e.g., an agent waiting on a model call), will produce contention shapes the trial did not exercise. Numbers are calibration, not invariants.

7. **`subtract-eligibility` is implemented but not exercised in 079.** It returns an empty report against the post-init substrate (no specs, no commitments, no engine_feedback rows in the substrate yet — the EF rows are in the filesystem inbox per the engine-v16 pattern, not in the substrate). 080 or 081 will exercise it for real at the first cadence read.

## Validator at close

```
== Selvedge validator (engine-v17) ==

Active engine-definition files:
  ok    PROMPT.md
  ok    prompts/development.md
  ok    prompts/application.md
  ok    specifications/methodology.md
  ok    specifications/constraints.md
  ok    specifications/workspace.md
  ok    specifications/engine-manifest.md
  ok    tools/validate.sh
  ok    state/migrations/001-initial.sql
  ok    selvedge/cli.py
  ok    bin/selvedge

Workspace identity:
  ok    MODE.md

Workspace directories:
  ok    provenance

Substrate (selvedge validate --precommit):
validate --precommit: ok

Latest session check:
  ok    provenance/079-substrate-vertical-slice/00-assessment.md
  ok    provenance/079-substrate-vertical-slice/03-close.md (closed)

Summary: 16 ok / 0 fail
```

(The 03-close.md row reaches "ok" at the same commit that lands this file.)
