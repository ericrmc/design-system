---
session: 079
title: Decisions — substrate vertical slice
date: 2026-04-27
engine_version_at_decision: engine-v17
decisions: 8
---

# Decisions

Session 079 implements the 078 D-11 vertical-slice handoff. Decisions below are calibration commitments arising from implementation: numbers chosen against trial results, refusals downgraded with cause, the engine-version bump itself, and disposition of items 078 left open. No multi-perspective deliberation was convened; per 078 honest-limit-2 the implementation surface is unambiguous and 079 records what implementation produced.

---

## D-1 — Engine-v16 → engine-v17 bump applied

**What.** The active engine version is now `engine-v17`. `engine-manifest.md` v17 (this commit) is the authority. The v16 → v17 transition consists of: D-7 cut applied to `methodology.md` and `workspace.md`; substrate landed (`state/migrations/001-initial.sql`, `selvedge` CLI, `bin/selvedge` shim); `tools/validate.sh` rewritten to delegate substrate integrity to `selvedge validate --precommit`.

**Why.** Per 078 D-11 step 1: "Apply the D-7 cut to engine-v16 active spec; bump to engine-v17 in `engine-manifest.md`; archive the removed sections per `methodology.md` §Preservation. *This is 079's first action.*"

Per 078 D-7: removed sections preserved at `archive/specifications/methodology-v1-removed-sections.md`, `archive/specifications/workspace-v1-removed-sections.md`, `archive/specifications/engine-manifest-v15-loading-recipe.md`. Each carries `status: superseded` frontmatter and the reason for removal.

Engine-v17 is **provisional** per 078 D-5 release gate: no methodology-expanding self-development modifies engine-v17 active spec until the close of the first external-problem trial of 30 sessions. This decision records the start of that release-gated period.

**Rejected alternatives.**
- **R-1.1 — Defer the cut to a later session.** Rejected per 078 D-11 R-11.2 (already disposed): "the cut tests subtraction discipline; deferring it past the substrate landing gives the substrate first-mover and accretes around it."
- **R-1.2 — Bump to engine-v18 because the substrate is structurally larger than a typical revision.** Rejected: 078 D-11's exit criteria explicitly cap 079 at one engine-version increment, and the substrate-as-state is not active spec per 078 D-12 §Why ("State substrate is the methodology's *envelope*").

**Open.** None.

---

## D-2 — Migration 001 schema breaches D-10's 16-table budget by 1 (synthesis_points)

**What.** `state/migrations/001-initial.sql` defines **17** tables, not 16. The 17th is `synthesis_points`, required by refusal T-14 (per 078 D-3) and explicitly listed under S3 tuples in 078 D-1.

**Why.** 078 D-10's enumeration of 16 tables omitted `synthesis_points` inadvertently. The omission is observable on a careful read of D-10's parenthetical (`sessions, objects, decisions, decision_alternatives, spec_versions, perspectives, deliberations, refs, commitments, engine_feedback, work_items, role_write_capabilities, read_log, subtraction_log, schema_migrations, agent_runs`) against D-1's listing of S3 tuples (`decision_alternatives, refs (including supersession edges), commitments, synthesis_points`). 079 closes the omission deterministically: the table is required by the refusal contract and adding it preserves the contract's integrity.

D-10 explicitly admits breaches with cause: *"breachable with cause (a session may exceed the budget if its decision record cites the breach explicitly and the human reviewer-subtractor's next dossier read does not subtract the breach)."* This decision is the cited cause. The next human reviewer-subtractor cadence reads this row and either ratifies or subtracts.

**Rejected alternatives.**
- **R-2.1 — Drop synthesis_points; absorb into a JSON column on deliberations.** Rejected: violates 078 D-1's S3-tuples principle for synthesis_points and makes T-14's CHECK constraint impossible to express at row-level; would require trigger-on-deliberations-update validating internal JSON, which is exactly the prose-state-in-JSON failure that 078 D-1 addresses.
- **R-2.2 — Defer synthesis_points to a later additive migration; defer T-14 too.** Rejected: T-14 is in 078 D-3's binding 16-refusal contract for migration 001. Deferring T-14 silently relaxes the contract; deferring with explicit engine_feedback is admissible but is a strictly worse position than absorbing the breach now (the breach is one table, not one refusal).
- **R-2.3 — Recalibrate D-10's table budget to 17 in this decision.** Rejected: D-10's number is not derived from synthesis_points; recalibration belongs in a 080+ session that has data on whether 17 is the right limit. 079 records the breach; 080+ judges.

**Open.** Whether the human reviewer-subtractor's next dossier read should ratify the new budget at 17 or treat synthesis_points as eligible for subtraction. The latter would require absorbing T-14 elsewhere; not currently feasible.

---

## D-3 — T-12 (role write capabilities) downgraded from trigger to application-layer for engine-v17

**What.** Refusal T-12 is enforced at the application layer in `selvedge submit` (function `_check_role_capability`), not as a SQLite trigger. The migration ships `role_write_capabilities` rows for the `__cli__` role only; LLM agent roles (specifier, decider, deliberator-N, human reviewer-subtractor) are added as 080+ deliberations introduce them.

**Why.** SQLite triggers cannot read a connection-scoped session variable (e.g., a "current role" PRAGMA) without per-table sentinel rows or extension functions. The clean trigger-form would require either (a) a `current_role` table that each transaction stamps before INSERT — requiring two writes per submit and substrate-level coordination — or (b) an SQLite C extension binding a SET-style function. Neither pays in 079's single-writer regime where the CLI is the only writer.

Per 078 D-3 §Open: "If 079 finds a refusal cannot be implemented as specified (e.g., T-01's body_md ref-parsing is intractable at trigger time), 079 records an engine_feedback row and the contract revises in 080+ deliberation." 079 records this as engine_feedback (`engine-feedback/EF-079-001-T12-application-layer.md`) and the contract revises at the first 080+ session that introduces a non-`__cli__` writer.

**Rejected alternatives.**
- **R-3.1 — Implement T-12 via per-write `current_role` table.** Rejected for 079: the pattern is two writes per submit (set role, then write), which doubles the contention surface for marginal benefit while no LLM agents exist.
- **R-3.2 — Defer T-12 entirely.** Rejected: even the application-layer enforcement is load-bearing the moment a second writer (CLI + agent process) appears; shipping the role lookup table now and the application-layer check now means the substrate-level addition is purely tightening rather than introducing the concept.

**Open.** 080+ revisits T-12 substrate enforcement when introducing the first LLM-writer role.

---

## D-4 — T-04 spec_version body-hash check is application-layer at submit + at validate

**What.** T-04 is enforced (a) in `_submit_spec_version` (the file is hashed and compared to the declared body_sha256 before INSERT) and (b) in `selvedge validate --precommit` (every active spec_version's file is re-hashed; mismatch fails the validator). It is not a trigger.

**Why.** The hash check requires reading the filesystem, which a SQLite trigger cannot do. 078 D-3's mechanism column for T-04 already says "Pre-commit `selvedge validate --hashes`"; this decision records that the same check additionally runs at submit time, which is the strictest reasonable position (refuse the row before it lands; the validator catches drift introduced after landing, e.g., by an editor not going through `selvedge`).

**Rejected alternatives.**
- **R-4.1 — Validate-only (per the literal D-3 text).** Rejected: a row whose declared hash does not match the file at the moment of insertion is unambiguously wrong; refusing at submit time turns it into structural friction rather than audit-after-the-fact.
- **R-4.2 — Submit-only.** Rejected: a file edited after the spec_version row landed (e.g., direct editor write) escapes detection until the next submit. The validator is the safety net; both gates are needed.

**Open.** If 080+ decides spec bodies must round-trip from substrate to file (write `body_md` to the substrate; render to `body_path` on read), the file-hash relationship inverts and T-04 changes shape. Not in 079 scope.

---

## D-5 — T-15 (no DROP COLUMN / DROP TABLE) is implementation-deferred to 080's first additive migration

**What.** The migration runner that enforces T-15 is **not implemented in 079**. Migration 001 ships as an executable SQL script run directly by `selvedge init`; there is no `selvedge migrate` subcommand yet. Future migrations (002 onwards) require the `selvedge migrate` CLI that pre-checks for `DROP COLUMN` / `DROP TABLE` and refuses.

**Why.** 079's migration count is one. The runner exists implicitly inside `cmd_init` (executes the script in a transaction). Building a `selvedge migrate --dry-run` plus the additive-vs-contract classifier (per 078 D-8) would add ~150 lines of CLI for a feature with zero callers in 079. Per 078 D-11 "must NOT": "Solve schema-evolution questions beyond migration 001. D-8's protocol governs; 079 implements only migration 001." Building the runner is solving schema-evolution beyond migration 001.

**Rejected alternatives.**
- **R-5.1 — Build `selvedge migrate` now to make T-15 active.** Rejected per 078 D-11 must-not list.
- **R-5.2 — Mark T-15 as "documented but unenforced" and never raise engine_feedback.** Rejected: T-15 is in the binding contract; implementation deferral must be recorded as engine_feedback for 080+ triage, just like T-12. This decision records the deferral; the engine_feedback row is `EF-079-002-T15-deferred-to-080.md`.

**Open.** 080+'s first additive migration triggers building the runner. T-15 becomes active enforcement at that point.

---

## D-6 — Substrate calibration parameters

**What.** `selvedge` ships with these defaults (constants in `selvedge/cli.py`):

| Parameter | Value | Rationale |
|---|---|---|
| `DEFAULT_BUSY_TIMEOUT_MS` | 5000 | Concurrency trial showed 16 parallel writers with 200ms in-tx sleep produced no `E_WRITE_BUSY` at 5s timeout. |
| `DEFAULT_RETRY_BUDGET` | 5 | Exponential backoff at 50/100/200/400/800ms; total retry window ≤ 1.55s. The trial used 0 retries (timeout absorbed contention). |
| `DEFAULT_RETRY_BASE_MS` | 50 | First retry quick; backoff exponential. |
| `DEFAULT_LEASE_SECONDS` | 300 | Default lease for `work_items`. Operator can override on submit; not exercised in 079. |
| `journal_mode` | WAL | Per 078 D-9. |
| `synchronous` | NORMAL | Acceptable durability for a workspace-local substrate; FULL is overkill for single-machine. |

**Why.** Per 078 D-9 §Open: "The exact `busy_timeout`, retry budget, and lease-expiry interval are 079 implementation parameters set against the falsification trial's results." The trial passed at these defaults with zero `E_WRITE_BUSY` events across 16 contending writers (one killed). The numbers are calibration, not invariants; 080+ may revisit if real workloads expose pathological patterns.

**Rejected alternatives.**
- **R-6.1 — `synchronous = FULL`.** Rejected: durability cost (extra fsync per commit) for a single-machine substrate without crash-survival requirements beyond what NORMAL provides. WAL+NORMAL is the SQLite-recommended baseline.
- **R-6.2 — Higher retry budget.** Rejected: trial passed with 0 retries; raising the budget without evidence of need is speculative.

**Open.** If a real workload (an external-problem trial) exposes `E_WRITE_BUSY` at >1% of submits, the budget revises upward. Workspace-level `selvedge.toml` for parameter override is **not** built in 079 — environment overrides via subprocess env are sufficient until a need surfaces.

---

## D-7 — Idempotency-key composition for work_items

**What.** `work_items.idempotency_key` is a UNIQUE TEXT column. The CLI does **not** generate keys in 079. Callers (080+ agent processes) supply the key per 078 D-9: "`(work_item_id, output_kind, output_hash)`". For 079, no work_items are written; the column is present and unique-indexed for 080+ to use.

**Why.** The 078 D-9 idempotency triple includes `output_hash`, which is meaningless until an agent produces an output. 079 has no agent outputs. The schema is correct; the CLI surface for it is 080+ scope.

**Rejected alternatives.**
- **R-7.1 — Auto-generate idempotency keys in `selvedge submit work-item`.** Rejected: the key's purpose is to let a crashed-and-restarted caller deduplicate against itself; the CLI cannot know whether the call is a retry or a first attempt. The caller must own the key.

**Open.** 080+ specifies the agent-side idempotency-key generator (likely `sha256(work_item_id || output_kind || canonical_json(output))` truncated to 32 chars).

---

## D-8 — Trial results (round-trip + concurrency)

**What.** Trial outcomes recorded for 080+ reference:

**Round-trip** (`state/tests/round_trip.sh`): **9/9 pass**.
1. `selvedge init` applies migration 001 cleanly.
2. `session-open` accepted with `session_no=1` (T-10 verified).
3. `spec-version` inserted with body_sha256 verified against file (T-04 application-layer verified).
4. `decision` inserted with one alternative (T-08 16-char rule satisfied) and one ref parsed from `body_md` to `[SPEC-round-trip-spec-v1]` (T-01 application-layer verified).
5. `session-close` succeeded (T-02 alternatives present; T-11 work_items empty).
6. Direct `sqlite3` UPDATE on the closed decision row was refused with `E_REFUSAL_T06` (verified).
7. Direct `sqlite3` UPDATE on a closed-session `decision_alternatives` row was refused with `E_REFUSAL_T06` (verified).
8. `refs` contained exactly 1 row (verified).
9. `selvedge validate --precommit` passed against the closed-session substrate.

**Concurrency** (`state/tests/concurrency.sh`): **PASS**.
- 16 parallel `python3` workers wrapping the CLI's submit path, each holding a 200ms in-transaction sleep.
- Worker 8 SIGKILL'd mid-transaction (after marker file confirmed it had entered the tx).
- Surviving submits: **15** (= 16 − 1 killed). All committed; decision_no contiguous 1..15; no duplicates.
- `E_WRITE_BUSY`: **0** observed at default 5s `busy_timeout`. (The retry budget did not fire; the timeout absorbed contention.)
- Killed worker left **0** decision rows, **0** orphaned objects, **0** orphaned alternatives. Atomicity preserved.
- `PRAGMA integrity_check`: ok.
- `PRAGMA foreign_key_check`: 0 violations.
- No raw "database is locked" string reached the worker layer (the worker itself converts to `E_WRITE_BUSY`).

D-9 falsification gate: not falsified. SQLite single-writer + BEGIN IMMEDIATE + 5s busy_timeout is adequate for the contention pattern 080+ will produce (single-machine workspace, ≤16 simultaneous writers).

**Why this disposition belongs in the decision record.** Per 078 D-11 step 7: "Close S079 with a decision recording the trial results and any engine_feedback rows raised." This is that decision. The trial passed; calibration parameters from D-6 are validated by the same evidence; the substrate is operational.

**Rejected alternatives.** None — the trials are evidence, not choices. The choice was whether to record the evidence as a decision (yes, per 078 D-11) or as a non-decision artefact (no, per the same).

**Open.** The trial does not exercise: cross-machine substrate access (out of scope per D-9); long-running agent processes (no agents in 079); migration runner under contention (no migrate command); reader load (read_log not exercised). 080+ extends as roles are introduced.

---

## Engine-version impact

`engine-v16` → `engine-v17`. Recorded at `specifications/engine-manifest.md` (this commit). The version bump is the substrate landing + the D-7 cut + the validator wiring; no further bumps are admitted in 079.

## Open issues raised by this session

- **OI-079-001:** D-10's table budget of 16 vs. the actual 17. Either ratify 17 as the new budget or subtract `synthesis_points` (which would require absorbing T-14 elsewhere). Reviewer decision.
- **OI-079-002:** T-12 substrate enforcement deferred to 080+'s first non-`__cli__` writer.
- **OI-079-003:** T-15 substrate enforcement deferred until `selvedge migrate` is built (080+'s first additive migration).
- **OI-079-004:** Trial coverage gaps (no migrate runner, no agent processes, no cross-machine, no read_log discipline). 080+ extends.

## Engine-feedback raised by this session

- **EF-079-001** — T-12 trigger-form not implementable without per-write sentinel rows or SQLite extensions; downgraded to application-layer for engine-v17. Triage: 080+ deliberation when the first non-`__cli__` writer is introduced.
- **EF-079-002** — T-15 enforcement requires `selvedge migrate` which is deferred per 078 D-11 must-not list. Triage: 080+ at first additive migration.
