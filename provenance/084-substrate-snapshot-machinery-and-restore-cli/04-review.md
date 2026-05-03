---
session: 084
title: substrate-snapshot-machinery-and-restore-cli — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: UNIQUE(path) constraint on snapshot_catalog permits catalog-row collision if snapshot file backup fails silently: snapshot file remains on disk but row insert fails, then same-microsecond retry writes to same path and INSERT fails with constraint violation.
  - **fixed.** selvedge/snapshots.py path now embeds os.getpid() so two simultaneous calls cannot collide on UNIQUE(path) — within-process microsecond resolution + cross-process pid isolation.
- **medium**: Symlink to primary substrate at --to not followed: if --to resolves via symlink to the primary, the symlink check at restore_cmd.py:127 will not match primary path and --confirm will be bypassed.
  - **fixed.** Path.resolve() canonicalises through symlinks so a symlink-to-primary at --to resolves to the canonical primary path and trips E_LIVE_PRIMARY; new test_restore_refuses_symlink_to_primary covers the case; comment added at restore_cmd.py:97.
- **medium**: Snapshot taken after source DB connection closed: in submit/__init__.py session-open/close snapshots fire after c.close(), creating a window where source DB could be mutated between commit and backup; snapshot captures post-mutation state but catalog row uses pre-snapshot sha256.
  - **fixed.** _source_db_sha256() now invoked AFTER backup() completes so both src_sha and snap_sha capture state at snapshot-completion time; docstring updated to describe the WAL-flatten reason for divergence rather than the pre-backup drift window.
- **medium**: UNIQUE(path) defensibility unclear: multiple migrate --apply runs in same microsecond with same migrations pending would collide. migrate_apply triggers one snapshot per run (correct), but path namespace is not explicitly bounded by migration count or run ID.
  - **fixed.** Same pid-suffix path fix as RF-S084-16; migrate_apply now safe against same-microsecond cross-process collision via os.getpid() in path.
- **low**: restore_cmd.py sidecar unlink issues: -wal/-shm unlink uses with_name() which fails if dst contains dots or unusual path patterns; the check/unlink is logged as warning (not error) so restore succeeds with stale WAL/SHM on disk.
  - **adjudicated.** with_name(name + -wal) is the SQLite WAL/SHM convention regardless of dot-segments in the dbname (sqlite always names sidecars <db>-wal/-shm); warning-not-error on unlink failure is intentional since restore can succeed (a fresh sidecar is written by the next open) and an unlink-blocking dir would also block the copy itself surfacing the deeper problem.
- **low**: restore_cmd.py mkdir(parents=True) at line 137 may create unintended directory tree if --to is a deeply nested path with missing ancestors; the verify-before-copy order does not atomically prevent intermediate dir creation on copy failure.
  - **adjudicated.** mkdir(parents=True) before copy mirrors mkdir -p semantics; orphan ancestor dirs on copy failure are a benign leftover (operator targeted that path explicitly, no work to defend against). Atomicity would require copying to tempfile+rename; reserved as a follow-up if mkdir-orphaning surfaces in the field.

## Terminal passes

- **iteration 2** — clean @ `d50a685`
  - Iteration 2 clean: 4 medium+ fixed (pid in path + post-backup sha + symlink test); 2 low adjudicated; 15 snapshot tests + full suite green.
