---
session: 082
title: Selvedge migrate runner + migration 002 (close OI-080-001)
date: 2026-04-27
engine_version_at_open: engine-v17
mode: self-development
substrate_session_no: 3
---

# Assessment

## State at open

S081 closed clean at engine-v17 with two pieces of unfinished business named in `provenance/081-deliberator-flow-exercise/03-close.md` §What S082 should address:

1. Human reviewer-subtractor cadence read (cadence trigger firmly hot for two sessions running).
2. **`selvedge migrate` runner + migration 002. Closes OI-080-001 structurally.** ← S082's choice.
3. Numbering-convention text resolution (5-minute side-action, deferred to a session with slack).

Operator selected (2). The work is mechanism-implementing-existing-methodology under the 078 D-5 release gate: it ships the migration-runner code path that 079 deferred (per `engine-feedback/inbox/EF-079-002-T15-deferred.md`) and applies migration 002 to fix the two T-06/T-13 substrate holes documented at S080 close in `D-S001-5` and pinned by two strict xfail tests in `state/tests/test_deliberation_kinds.py`. No new active-spec content is added to `methodology.md` or peer specifications.

### What was waiting

- **OI-080-001** (HIGH) — two substrate holes:
  - (a) T-06 had no triggers on `deliberations` UPDATE/DELETE; closed-session deliberations' `topic` and `synthesis_md` could be silently mutated by any direct-SQL writer.
  - (b) T-13 only refused non-NULL→NULL on `sealed_at`. A direct UPDATE that set `sealed_at` to a different non-NULL timestamp was admitted, polluting the audit trail.
  - Two strict xfail tests pinned current behaviour, ready to flip on migration 002.
- **EF-079-002** — T-15 (no DROP TABLE/DROP COLUMN) deferred until a migration-runner code path existed for the pre-check to fire on. The runner shipping this session activates T-15.
- **Substrate at S081 close**: sessions=2, deliberations=2, perspectives=5, synthesis_points=5, decisions=8, decision_alternatives=12, refs=4. Migration sha256 unchanged from S079 close (single migration: 001-initial.sql).
- **Pytest at S081 close**: 27 passed, 2 xfailed (the strict OI-080-001 forcing functions).

## Agenda for S082

In execution order:

1. Author `state/migrations/002-tighten-deliberation-immutability.sql`: DROP+CREATE the tightened T-13 trigger; add T-06 trigger pair on `deliberations` UPDATE/DELETE; record the migration row.
2. Build `selvedge migrate` subcommand in `selvedge/cli.py` with `--status`, `--dry-run`, `--apply`. Implement T-15 pre-check (refuse `DROP TABLE`, `DROP COLUMN`, `ALTER ... DROP`; admit `DROP TRIGGER`/`DROP INDEX`); idempotency via `schema_migrations` lookup; drift detection (`E_MIGRATION_DRIFT`); 078 D-8 tier-1 rollback via a `.pre-migrate-backup` SQLite copy. Have `selvedge init` chain the runner so a fresh init applies all migrations, not just 001.
3. Add `state/tests/test_migrate.py` covering the parser surface (T-15 patterns plus comment-stripping), end-to-end `--status`/`--dry-run`/`--apply`, idempotency, drift detection, T-15 refusal in dry-run and apply, mid-apply failure restoring from backup. Add `SELVEDGE_DB_PATH` and `SELVEDGE_MIGRATIONS_DIR` env overrides to `selvedge/cli.py` so tests can run against an isolated tmp workspace.
4. Update `state/tests/conftest.py` `clean_substrate` fixture to call `selvedge migrate --apply` after `init` (defence-in-depth — `init` already chains the runner now, but the explicit call surfaces any future regression at fixture-time).
5. Apply migration 002 to the production substrate (`state/selvedge.sqlite`) via `selvedge migrate --apply`.
6. Unmark the two strict xfails in `test_deliberation_kinds.py` (rename functions to drop the `_xfail` suffix; remove the `pytest.mark.xfail` wrapping).
7. Run `pytest state/tests/`, `state/tests/round_trip.sh`, `state/tests/concurrency.sh`, `tools/validate.sh` — all must pass.
8. Open substrate session 3 (T-10 contiguous from session_no=2); submit one substantive decision (D-1, with three rejected alternatives per T-02) recording the runner + migration 002 + engine-version bump; submit two disposition decisions (D-2 closing OI-080-001; D-3 triaging EF-079-002).
9. Move `open-issues/OI-080-001.md` to `open-issues/resolved/`; update `open-issues/index.md` (decrement active count 15→14; add resolved-row). Create `engine-feedback/triage/EF-079-002-T15-deferred.md` with disposition pointing at S082 D-3.
10. Bump engine version v17 → v18 per `engine-manifest.md` §Versioning ("substrate migration" triggers a bump). Update the manifest's substrate file table to enumerate migration 002; append the engine-version-history entry; update `engine_version_at_close` references in validators and the round_trip test (round_trip uses the value as input to `session-close`; it will pick up v18 next time it runs against a v18 substrate, but the value is operator-passed — no test change required, only the production substrate's S082 close uses v18).
11. Update `tools/validate.sh` banner v17 → v18 + add migration 002 to the file-presence checklist.
12. Submit `session-close` for substrate session 3 with `engine_version_at_close=engine-v18`.
13. Write provenance: `00-assessment.md` (this file), `02-decisions.md`, `03-close.md`. Commit + push.

## Hard limits

- **Release gate (078 D-5)** in force. The runner + migration are mechanism-implementing-existing-methodology and bug-fix-against-an-identified-substrate-hole respectively. No active-spec content added to `methodology.md`, `constraints.md`, `workspace.md`. The manifest is updated in two minor ways (bump version; enumerate the new migration file) — both are derived-from-substrate-state, not new-prose.
- **No multi-agent deliberation this session.** The kernel's cross-family / adversarial-perspective discipline applies to methodology revisions, deliberation-pattern changes, validation-mechanism changes, and database-schema decisions of substance (per `prompts/development.md` §Operate). Migration 002 is a bug fix against holes that two strict xfail tests already pin and that `D-S001-5` already adjudicated as HIGH-priority remediation. The runner's design is mechanism-implementing the existing 078 D-3 / D-8 commitments, not new methodology. S081 close's S082 candidate-2 framing explicitly named this as gate-admitted single-agent work.
- **No close-time review of S082 itself.** Per 078 D-7 step 1, the kernel's close-time-review section was removed at engine-v17. The substrate's strict xfail flip + the round_trip + concurrency + pytest passes against migration 001+002 are the structural verification. A future session that elects to retrospectively audit S082 reads `02-decisions.md` against `decisions` rows D-S003-1..3 + their alternatives + the `schema_migrations` row for 002 + the diff at this commit.

## What this session does **not** do

- Reviewer-subtractor cadence read (S082 candidate 1) — deferred to a future session. The cadence trigger remains hot.
- Numbering-convention resolution (S082 candidate 3) — deferred.
- Any prose-spec revision beyond manifest enumeration + version-bump bookkeeping.
- Spec-version row in `spec_versions` for the manifest edit (the substrate's `spec_versions` table is currently empty for the active engine-definition specs; this provenance gap was named at S081 close §Honest-limit-6 and is not addressed here).
