---
session: 082
title: Selvedge migrate runner + migration 002 — close
date: 2026-04-27
engine_version_at_close: engine-v18
mode: self-development
substrate_session_no: 3
---

# Close

## What was done

S082 shipped the `selvedge migrate` runner deferred at S079 close, applied migration 002 to fix the two T-06/T-13 holes documented at S080 close, flipped the strict xfail tests pinning OI-080-001, and bumped the engine version v17 → v18.

### Concretely

1. **Migration 002 authored.** `state/migrations/002-tighten-deliberation-immutability.sql` (sha256 `b97a2564b8b0a0b9a890d1355778037366c73d2390ac69bba10f8201938b8af0`). Drops and recreates `t13_deliberations_sealed_immutable` with the tightened condition `OLD.sealed_at IS NOT NULL AND NEW.sealed_at IS NOT OLD.sealed_at` (admits the seal NULL→timestamp transition; refuses any change-in-place to a non-NULL `sealed_at`; admits idempotent same-value writes). Adds `t06_deliberations_no_mut_after_close_upd` and `t06_deliberations_no_mut_after_close_del` mirroring the existing patterns for decisions/perspectives/synthesis_points.

2. **`selvedge migrate` runner built.** New subcommand in `selvedge/cli.py` with three mutually exclusive modes: `--status` (lists applied + pending), `--dry-run` (parses pending + T-15 check, no writes), `--apply` (applies in lex order, in-transaction, with backup-and-restore on failure). Helpers: `_t15_violations` (regex-based DROP TABLE/COLUMN/ALTER ... DROP detection with comments stripped), `_migration_state` (substrate vs filesystem comparison + drift detection), `_apply_pending` (backup → executescript → sha256 update → commit; restore from `.pre-migrate-backup` on any failure). `cmd_init` now chains `_apply_pending` so a fresh init applies all known migrations, not just 001. `db_path()` and `migrations_dir()` gain `SELVEDGE_DB_PATH` and `SELVEDGE_MIGRATIONS_DIR` env overrides for test isolation.

3. **Migration 002 applied to production substrate.** `bin/selvedge migrate --apply` against `state/selvedge.sqlite` recorded the row at `2026-04-27T06:49:44.736Z` with the real sha256.

4. **Migrate runner tests added.** `state/tests/test_migrate.py` (14 tests). Direct unit tests on `_t15_violations` for each forbidden pattern + comment-stripping + admitted drops; integration tests via subprocess against an isolated tmp-workspace fixture for `--status`/`--dry-run`/`--apply`/idempotency/drift-detection/T-15-refusal-in-dry-run-and-apply/mid-apply-failure-restoring-from-backup. `state/tests/conftest.py`: `clean_substrate` fixture chains `selvedge migrate --apply` after init (defence-in-depth — `init` already auto-applies, but the explicit call surfaces any future regression at fixture-time); `WORKSPACE` is added to `sys.path` so unit tests can import `selvedge.cli` helpers directly.

5. **Strict xfails flipped.** The two strict xfail tests in `state/tests/test_deliberation_kinds.py` (`test_t06_deliberations_update_unprotected_xfail` and `test_t13_permits_resealing_to_other_timestamp_xfail`) were renamed to `test_t06_closed_deliberation_topic_immutable` and `test_t13_refuses_resealing_to_other_timestamp` and the `pytest.mark.xfail` wrappers removed. Both now pass naturally against migration 002.

6. **Engine version bumped v17 → v18.** `specifications/engine-manifest.md` frontmatter `version: 17` → `18`, `updated-by-session: 081` → `082`, supersedes line updated. §Current engine version rewritten to introduce v18 (substrate file table now enumerates migration 002; the `selvedge/` description names the `migrate` subcommand). §Versioning prose adjusted: the gate constrains *what kind* of change can ship, not whether qualifying changes bump the version. §Engine-version history appends a v18 entry. `tools/validate.sh` banner updated; migration 002 added to the file-presence checklist.

7. **Three substrate decisions recorded.** `decisions` rows D-S003-1 (substantive, with three rejected alternatives per T-02), D-S003-2 (disposition closing OI-080-001), D-S003-3 (disposition triaging EF-079-002). All three cite `[D-S001-5]` or `[D-S003-1]` in body_md, producing 3 substrate `refs` rows total (S082 contribution to refs: 4 → 7).

8. **OI-080-001 closed.** `open-issues/OI-080-001.md` → `open-issues/resolved/OI-080-001.md` with `status: resolved`, `resolved-in-session: 082`, `resolved-on: 2026-04-27`. `open-issues/index.md` decremented active count 15 → 14; resolved table appended an OI-080-001 row.

9. **EF-079-002 triaged.** `engine-feedback/triage/EF-079-002-T15-deferred.md` created with `status: resolved`, `triage_session: 082`, `resolved_by: provenance/082-migrate-runner/`. The inbox file stays in place as the archive intake.

10. **Validator at close passes.** `bash tools/validate.sh` reports 16 ok / 0 fail (the 17th row, `provenance/082-migrate-runner/03-close.md`, reaches "ok" at the same commit that lands this file).

## State at close

- **Active engine version:** `engine-v18` (provisional per 078 D-5; first version-bump since v17 ratification at 079; bug-fix + validator-tightening admitted under the gate per the manifest's clarified §Versioning prose).
- **Substrate at close:** sessions=3, deliberations=2, perspectives=5, synthesis_points=5, decisions=11 (8 + S082's 3), decision_alternatives=15 (12 + S082's 3 on D-1), refs=7 (4 + S082's 3), migrations=2 (001 + 002).
- **Validator:** `tools/validate.sh` 16 ok / 0 fail at close (17 ok at the same commit landing this file).
- **Tests:** `pytest state/tests/` **47 passed, 0 xfailed** (was 27 + 2 xfailed at S081 close; +18 from `test_migrate.py` and post-review hardening; the 2 xfails flipped and are now passing under their renamed function names; +4 from a post-close adversarial-reviewer pass that surfaced load-bearing test gaps — see §Post-close reviewer pass). `bash state/tests/round_trip.sh` 9/9 pass. `bash state/tests/concurrency.sh` PASS (15 surviving submits + 1 killed; integrity ok; no orphans).
- **Open issues:** active count 15 → 14 (OI-080-001 closed). The resolved-table count grows by 1.
- **Engine-feedback:** EF-079-002 triaged and resolved at S082; `engine-feedback/triage/` gains one row. EF-079-001 (T-12 application-layer) remains in inbox awaiting its own activation trigger (a future writer role landing).

## Refusal coverage at close

S082 added active enforcement to one previously-deferred refusal and tightened two:

| Refusal | Status pre-S082 | Status post-S082 |
|---|---|---|
| T-06 on `deliberations` UPDATE/DELETE | Missing (OI-080-001 hole, strict xfail pin) | Active triggers `t06_deliberations_no_mut_after_close_upd/del`. Pytest: `test_t06_closed_deliberation_topic_immutable` passes naturally. |
| T-13 on `sealed_at` change-in-place | Refused only NULL transition; admitted timestamp-rewrite (OI-080-001 hole, strict xfail pin) | Refuses any change to non-NULL sealed_at via tightened `IS NOT OLD.sealed_at` condition. Pytest: `test_t13_refuses_resealing_to_other_timestamp` passes naturally. |
| T-15 (no DROP TABLE / DROP COLUMN / ALTER ... DROP in migrations) | Deferred (no migration-runner code path; documentation-only enforcement per EF-079-002) | Active enforcement in `selvedge migrate --dry-run` and `--apply`. Pytest: `test_t15_refuses_drop_table`, `test_t15_refuses_drop_column`, `test_t15_refuses_alter_drop` (parser unit tests) plus `test_t15_refuses_destructive_migration_in_dry_run` and `test_t15_refuses_alter_drop_column` (integration tests). Non-destructive drops admitted: `test_t15_admits_drop_trigger`, `test_t15_admits_drop_index`. |

The remaining unexercised refusals at S082 close (T-03 unique-active spec_version, T-07a/b superseded-cite, T-09 commitment state machine, T-16 lease-expired) are unchanged from S080 close. Future sessions extending pytest coverage to these are admitted under the release gate (mechanism-test-implementing).

## What S083 should address

Three candidates, in priority order:

1. **Human reviewer-subtractor cadence read.** Per 078 D-6, default cadence is every 5th self-development session; S076–S082 are seven self-dev sessions, so the cadence trigger has been hot for *three* sessions running (named at S080 close, named again at S081 close, deferred each time). S083's dossier inputs are richer than S081's: `bin/selvedge subtract-eligibility` (substantive substrate content from S081 + S082), the four EF rows in `engine-feedback/inbox/` minus the EF-079-002 now triaged at S082, OI-081-001 (post-gate review of the table-budget mechanism), all the active OIs in `open-issues/index.md`. The cadence-read complements S082's structural completion of OI-080-001 — the workspace has just removed a HIGH-priority debt and the subtractor has fresh evidence to read.

2. **Numbering-convention text resolution.** S081 D-2 deferred this; S082 also did not take it. The resolution is small (one paragraph in `open-issues/index.md` Conventions section addressing the OI-079-001 / OI-080-001 / OI-081-001 session-prefixed scheme vs the index's "strictly append-only" convention text). Could be done as a 5-minute side-action of any future session.

3. **Pytest coverage extension to T-03 / T-07a/b / T-09 / T-16.** Mechanism-test-implementing under the release gate. Each is one or two test cases; collectively a small expansion of `test_existing_kinds.py`. Useful as the next session's productive interlude if (1) is taken first and produces capacity.

**Hard limit on S083:** the 078 D-5 release gate remains in force. Calibrations under existing breach clauses, dispositions, mechanism-tests-implementing, mechanism-implementing-existing-methodology, and human-subtractor reads are admitted. New active-spec content in `methodology.md` or peers is forbidden.

## Honest limits

1. **Two-tier rollback is tier-1 only.** The runner implements 078 D-8 tier-1 (pre-close failure → SQLite rollback + restore from `.pre-migrate-backup` SQLite copy) and exercises it via `test_failure_mid_apply_restores_from_backup`. Tier-2 (post-close failure → forward-only corrective migration) is documentation-level: by design there cannot be an automated tier-2 path because corrective migrations are operator-authored, not runner-derived. This matches 078 D-8's framing but is worth naming honestly: a migration that succeeds, commits, and then turns out to be wrong has no automated rollback.

2. **T-15 parser is regex-based.** `_t15_violations` strips SQL comments and matches `\bDROP\s+TABLE\b`, `\bDROP\s+COLUMN\b`, and `\bALTER\s+TABLE\b[^;]*\bDROP\b` (case-insensitive). It does **not** parse SQL into an AST and does not handle pathological forms like `DROP` keywords inside string literals. The threat model is migration files written by operators in good faith. An adversarial author who knew the regex could plausibly evade it via creative literal-positioning. Recorded for a future session's hardening pass; the workspace's only migration authors are operators in good faith.

3. **No multi-agent deliberation this session.** S082 was framed at S081 close as gate-admitted single-agent work (mechanism-implementing-existing-methodology + bug-fix). The kernel's cross-family / adversarial-perspective discipline applies to methodology revisions, deliberation-pattern changes, validation-mechanism changes, and database-schema decisions of substance. Migration 002 is bug-fix-against-named-holes; the runner is mechanism-implementing 078 D-3 / D-8. If a future session disagrees that this was the right framing — that S082 should have convened cross-family review on the runner's design — the existing record is auditable: the runner is small (~200 lines), the migration is small (~30 lines of effective DDL), and `provenance/082-migrate-runner/02-decisions.md` D-1 lays out three rejected alternatives.

4. **No close-time reviewer-agent audit of S082 itself.** Per 078 D-7 step 1, the kernel's close-time-review section was removed at engine-v17. The substrate's strict xfail flip + the round_trip + concurrency + pytest passes against migration 001+002 are the structural verification. A future session that elects to retrospectively audit S082 reads `02-decisions.md` against `decisions` rows D-S003-1..3 + their alternatives + the `schema_migrations` row for 002 + the diff at this commit.

5. **`spec_versions` table still empty for active engine-definition specs.** S081 close §Honest-limit-6 named this provenance gap (the `engine-manifest.md` v17 → v18 edit at S082 is not tracked as a `spec_versions` row, just like S081's manifest correction wasn't). A future session that introduces spec-version tracking for the active engine specs in the substrate inherits both gaps; both can be backfilled then.

6. **The release gate clarification was opportunistic.** S082's §Versioning prose adjustment ("the gate constrains *what kind* of change can ship; it does not exempt qualifying changes from the bump rule") corrects a tension between the v17 manifest's optimistic "engine-v17 → engine-v18 is not anticipated until after the first external-problem trial completes" line and the same manifest's §Versioning rule that substrate migrations bump the version. The correction is consistent with what S080 and S081 did (mechanism-implementing-existing-schema kept v17; this session's substrate migration earns v18) but it is a manifest revision, not just an enumeration update. Recorded as part of D-1 rather than as its own decision because the rule it codifies is what the manifest already implies; the new text resolves an inconsistency, not introduces one.

7. **The migrate runner has no `selvedge validate --precommit` integration.** A future session adding "warn if pending migrations exist at validate time" is admitted under the gate as mechanism-implementing-existing.

## Post-close reviewer pass

After the initial close commit (`624e70c`), an adversarial Explore subagent was convened to audit `state/tests/test_migrate.py`, the flipped xfails in `state/tests/test_deliberation_kinds.py`, and the migrate runner in `selvedge/cli.py`. Verdict: BLOCKING (close should be reviewed before push) with three critical findings and several coverage-gap notes. The orchestrator's adjudication and remediation:

| Reviewer finding | Disposition |
|---|---|
| **Critical 1.** "T-13 test passes against migration 001 alone (UPDATE succeeds silently because `NEW.sealed_at IS NULL` is false)." | **Disagree on slip-through claim.** Against migration 001 the UPDATE succeeds *silently* (no exception), so `pytest.raises(sqlite3.IntegrityError)` would fail with "DID NOT RAISE", correctly failing the test. The test does verify migration 002 ran. **Agree on hardening:** strengthened the assertion to require migration 002's specific error text (`immutable once non-NULL`) so a future regression that drifted the wording would be caught. |
| **Critical 2.** "Drift detection bypassed if runner stored placeholder sha forever (`recorded == _PLACEHOLDER_SHA` short-circuits drift compare)." | **Agreed real gap.** Added `test_apply_replaces_placeholder_sha_with_real_hash` which writes a migration containing the placeholder, applies it, and asserts the recorded sha256 is the real hash, not the placeholder. Verified against production substrate (both 001 and 002 carry real sha256s). |
| **Critical 3.** "No test for idempotent same-value `sealed_at` write (migration 002 prose claims this is admitted; no test exercises it)." | **Agreed real gap.** Added `test_t13_admits_idempotent_same_value_sealed_at_write` to `test_deliberation_kinds.py`. Reads the sealed_at value, writes it back via direct SQL, asserts the trigger does not fire and the value is preserved. |
| Important: backup-restore test only checked `schema_migrations`, not the substrate state. | Strengthened `test_failure_mid_apply_restores_from_backup`: now captures pre-apply table count, asserts post-apply table count matches, asserts the bad trigger does not exist post-restore, and asserts the `.pre-migrate-backup` file remains for operator inspection. |
| Important: `cmd_migrate` rc=2 path (no substrate) untested. | Added `test_migrate_against_nonexistent_substrate_returns_rc2` covering `--status`, `--dry-run`, `--apply` against an absent DB. |
| Important: `--apply` with zero pending untested as a standalone path. | Added `test_apply_with_no_pending_is_a_clean_noop`. |
| Nits 9–11 (WAL/SHM cleanup, brittle name assertion, T-06 scope). | Acknowledged; not addressed (low-impact; pytest's `tmp_path` handles WAL cleanup; the name-list assertion is intentional for fixture sanity; T-06 reviewer-confirmed "no gap"). |

Pytest count: 43 → 47 (4 new defensive tests). All pass. The reviewer's BLOCKING verdict is downgraded to ADVISORY-resolved by these additions; the load-bearing gaps (placeholder bypass, idempotent same-value, regression-resistant T-13 wording) are now closed by tests, not just by the implementation.

## Validator at close

```
== Selvedge validator (engine-v18) ==

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
  ok    state/migrations/002-tighten-deliberation-immutability.sql
  ok    selvedge/cli.py
  ok    bin/selvedge

Workspace identity:
  ok    MODE.md

Workspace directories:
  ok    provenance

Substrate (selvedge validate --precommit):
validate --precommit: ok

Latest session check:
  ok    provenance/082-migrate-runner/00-assessment.md
  ok    provenance/082-migrate-runner/03-close.md (closed)

Summary: 17 ok / 0 fail
```

(The 03-close.md row reaches "ok" at the same commit that lands this file.)
