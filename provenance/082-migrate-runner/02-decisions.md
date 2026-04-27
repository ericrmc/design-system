---
session: 082
title: Selvedge migrate runner + migration 002 — decisions
date: 2026-04-27
substrate_session_no: 3
---

# Decisions

Three decisions, recorded in both this file and the substrate (`decisions` rows D-S003-1, D-S003-2, D-S003-3). One substantive (D-1, with three rejected alternatives per T-02), two dispositions (D-2 closing OI-080-001, D-3 triaging EF-079-002).

## D-1 (substantive) — Ship `selvedge migrate` runner + migration 002; close OI-080-001 structurally; bump engine-v17 → engine-v18

**Substrate alias:** `D-S003-1` (object_id 24, decision_id 9). 1 ref recorded against `[D-S001-5]` (S080's OI-080-001 opening decision).

### What

Three coupled deliverables, one decision:

1. **`state/migrations/002-tighten-deliberation-immutability.sql`** authored. Drops and recreates `t13_deliberations_sealed_immutable` with the tightened `WHEN OLD.sealed_at IS NOT NULL AND NEW.sealed_at IS NOT OLD.sealed_at` condition (admits seal NULL→timestamp; refuses any change-in-place to a non-NULL `sealed_at`; admits idempotent same-value writes). Adds `t06_deliberations_no_mut_after_close_upd` and `t06_deliberations_no_mut_after_close_del` mirroring the patterns in 001 for decisions/perspectives/synthesis_points. Records the migration row with the `COMPUTED-AT-APPLY-TIME` placeholder that the runner replaces post-script. Migration sha256: `b97a2564b8b0a0b9a890d1355778037366c73d2390ac69bba10f8201938b8af0`.

2. **`selvedge migrate` subcommand** built in `selvedge/cli.py` with `--status`, `--dry-run`, `--apply` (mutually exclusive, required). Reads `schema_migrations` to determine pending vs applied; verifies file sha256 against the recorded row to detect drift (`E_MIGRATION_DRIFT`); runs the T-15 pre-check (`_t15_violations`) on every pending migration's SQL; takes a `.pre-migrate-backup` SQLite copy before each apply pass; applies in lex order via `executescript`; restores from backup on any execute-time failure (078 D-8 tier-1 rollback). `selvedge init` now chains the runner so a fresh init applies all known migrations, not just 001. `SELVEDGE_DB_PATH` and `SELVEDGE_MIGRATIONS_DIR` env overrides added to `db_path()` and `migrations_dir()` so tests can run against isolated tmp workspaces. The two strict xfail tests in `test_deliberation_kinds.py` flipped to passing post-migration and have been unmarked (renamed to drop `_xfail` suffix; `pytest.mark.xfail` wrappers removed). Pytest at S082 close: 43 passed, 0 xfailed (was 27 + 2 xfailed at S081 close).

3. **Engine version bump v17 → v18** per `engine-manifest.md` §Versioning ("substrate migration" triggers a bump). Manifest substrate-file table enumerates migration 002; engine-version-history appends the v18 entry. `tools/validate.sh` banner updated; `state/migrations/002-tighten-deliberation-immutability.sql` added to file-presence checklist.

### Why

The `D-S001-5` closing condition (S080) named migration 002 as the structural remedy and the runner as its prerequisite. The runner is required for T-15 enforcement (`EF-079-002`'s deferred refusal becomes active enforcement at the moment the runner ships). The 078 D-5 release gate admits this work as bug-fix + validator-tightening: no active-spec content is added to `methodology.md` or peer specifications. The version-bump is structural-record (the substrate refuses strictly more behaviour at v18 than at v17) and is required by the manifest's own §Versioning rule.

### Rejected alternatives

| Label | Alternative | Why rejected |
|-------|-------------|--------------|
| **R-1.1** | Edit `state/migrations/001-initial.sql` in place to add the missing T-06 trigger and tighten T-13. | Forbidden by preservation discipline. Editing 001 invalidates its recorded sha256 in `schema_migrations` (the runner's drift detection would correctly flag every existing substrate as compromised), and the workspace's specs-evolve-via-new-versions rule applies to migrations as much as to prose specs. Migration 002 is the methodology-conformant remedy and was named as such in `D-S001-5`'s closing condition. |
| **R-1.2** | Skip the runner; have `selvedge init` apply every trigger ever needed via runtime SQL, avoiding migrations entirely. | Defeats the point of additive migration files. A fresh init would need to encode the full schema history; existing substrates with rows present (the workspace's own at S081 close has 5 perspectives, 5 synthesis_points, 8 decisions and would lose lineage) can't be re-initialised without subtraction. The runner's purpose is exactly to apply schema deltas to populated substrates idempotently; collapsing that into init is a regression of the design committed at 078 D-8. |
| **R-1.3** | Defer migration 002 until cross-family deliberation has audited the runner design per the kernel's multi-agent guidance. | The kernel's multi-agent guidance applies to methodology revisions, deliberation-pattern changes, validation-mechanism changes, and database-schema decisions of substance. Migration 002 is a bug fix against holes that two strict xfail tests already pin and that `D-S001-5` already adjudicated as HIGH-priority remediation; the runner's design is mechanism-implementing the existing 078 D-3 / D-8 commitments, not new methodology. S081 close's S082 candidate-2 framing explicitly named this as load-bearing and gate-admitted. |

### Open

- The two-tier rollback discipline (078 D-8) is implemented as **tier-1 only** in the runner. Tier-1 (pre-close failure → SQLite rollback + restore from `.pre-migrate-backup`) is exercised by `test_failure_mid_apply_restores_from_backup`. Tier-2 (post-close failure → forward-only corrective migration) is documentation-level: the runner records a definite failure that survives the rollback, leaving the operator to author a corrective migration in a future session. There is no automated tier-2 path because by design there cannot be one — corrective migrations are operator-authored, not runner-derived. This matches 078 D-8's framing.
- The runner's T-15 parser is regex-based with SQL comments stripped. It does **not** parse SQL into an AST and does not handle pathological forms like `DROP` keywords appearing inside string literals (e.g., `INSERT INTO t VALUES ('DROP TABLE …');`). The parser's threat model is migration files written by operators in good faith; an adversarial migration author who knew the parser's exact regex could plausibly evade it via creative literal-positioning. This honest-limit is recorded for a future session's hardening pass; the workspace's only migration authors are operators in good faith.
- The migrate runner has no integration with `selvedge validate --precommit` yet. A future session adding "warn if pending migrations exist at validate time" is admitted under the gate (mechanism-implementing-existing).

## D-2 (disposition) — Close OI-080-001

**Substrate alias:** `D-S003-2` (object_id 25, decision_id 10). 1 ref recorded against `[D-S003-1]`.

OI-080-001's four closing conditions (per the OI file) all met:

1. `selvedge migrate --apply` exists and was exercised against the production substrate at S082 mid-session, applying migration 002.
2. Migration 002 added `t06_deliberations_no_mut_after_close_upd/del` and tightened `t13_deliberations_sealed_immutable` to refuse any change-in-place to a non-NULL `sealed_at`.
3. The two strict xfail tests in `test_deliberation_kinds.py` flipped to passing and have been unmarked, renamed to `test_t06_closed_deliberation_topic_immutable` and `test_t13_refuses_resealing_to_other_timestamp`.
4. Migration sha256 (`b97a2564b8b0a0b9a890d1355778037366c73d2390ac69bba10f8201938b8af0`) recorded in `schema_migrations`; round_trip + concurrency + pytest all rerun green against migration 001+002.

`open-issues/OI-080-001.md` → `open-issues/resolved/OI-080-001.md`; frontmatter updated with `status: resolved`, `resolved-in-session: 082`, `resolved-on: 2026-04-27`. `open-issues/index.md` decrements active count 15 → 14; resolved table appends OI-080-001 row.

## D-3 (disposition) — Triage EF-079-002 (T-15 now active)

**Substrate alias:** `D-S003-3` (object_id 26, decision_id 11). 1 ref recorded against `[D-S003-1]`.

EF-079-002 is resolved by the runner shipped in D-1. T-15 is now active enforcement: every `selvedge migrate --dry-run` and `--apply` invocation parses migration SQL through `_t15_violations`, refusing on `\bDROP\s+TABLE\b`, `\bDROP\s+COLUMN\b`, and `\bALTER\s+TABLE\b[^;]*\bDROP\b` patterns (case-insensitive, with SQL comments stripped to avoid false positives). Three test cases in `test_migrate.py` exercise each forbidden pattern; one verifies `DROP TRIGGER` is admitted (which is what migration 002 itself uses to recreate the tightened T-13).

`engine-feedback/inbox/EF-079-002-T15-deferred.md` stays in place (archive); `engine-feedback/triage/EF-079-002-T15-deferred.md` is created with `status: resolved`, `triage_session: 082`, pointing at `provenance/082-migrate-runner/`.
