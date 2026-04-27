---
feedback_ref: engine-feedback/inbox/EF-079-002-T15-deferred.md
triage_session: 082
status: resolved
classification: substantive
resolved_by: provenance/082-migrate-runner/
---

## Triage disposition

**Accepted at S082** as the activation trigger named in the inbox record itself: "080+'s first additive migration triggers building `selvedge migrate`". S082 ships migration 002 to close OI-080-001 and builds the runner alongside it. T-15 is now active enforcement against migrations applied via `selvedge migrate --dry-run` and `--apply`.

## Resolution

Resolved at S082 via [D-S003-1] (substantive — runner + migration 002 + engine-v17 → v18 bump) + [D-S003-3] (this disposition).

- The runner's T-15 pre-check (`_t15_violations` in `selvedge/cli.py`) parses migration SQL with comments stripped and refuses on `\bDROP\s+TABLE\b`, `\bDROP\s+COLUMN\b`, and `\bALTER\s+TABLE\b[^;]*\bDROP\b` (case-insensitive).
- `state/tests/test_migrate.py` exercises each pattern: `test_t15_refuses_drop_table`, `test_t15_refuses_drop_column`, `test_t15_refuses_alter_drop`, `test_t15_strips_comments_before_match`. Non-destructive drops admitted: `test_t15_admits_drop_trigger`, `test_t15_admits_drop_index` (the latter pair are the patterns migration 002 itself relies on to recreate the tightened T-13).
- The two-tier rollback discipline from 078 D-8 is implemented as tier-1 only (pre-close: `.pre-migrate-backup` SQLite copy taken before each apply pass, restored on any execute-time failure). Tier-2 (post-close failure → forward-only corrective migration) is documentation-level: the runner records a definite failure that survives the rollback, leaving the operator to author a corrective migration. `state/tests/test_migrate.py::test_failure_mid_apply_restores_from_backup` exercises tier-1 against a deliberately broken migration.

## Cross-linkage

- Migration 002 itself: `state/migrations/002-tighten-deliberation-immutability.sql` (sha256 `b97a2564b8b0a0b9a890d1355778037366c73d2390ac69bba10f8201938b8af0`).
- The OI this resolves alongside: `open-issues/resolved/OI-080-001.md` (closed S082 per [D-S003-2]).
