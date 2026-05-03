---
session: 084
title: substrate-snapshot-machinery-and-restore-cli — close
engine_version_at_close: engine-v51
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S084 ships OI-S081-3 L3 boundary snapshots via SQLite Connection.backup at 4 trigger points + OI-S081-4 bin/selvedge restore --confirm CLI per DV-S084-1; FR-S081-11 + FR-S082-15 + FR-S082-16 disposed.

## Engine version

- engine-v51 unchanged (engine-version bump deferred to OI-S081-7 per FR-S081-14).
## What was done

- Migration 042 ships snapshot_catalog table (trigger CHECK enum + UNIQUE(path) + two indexes).
- selvedge/snapshots.py implements take_snapshot via sqlite3.Connection.backup with pid-suffixed paths.
- Snapshot triggers wired at session-open + session-close + migrate-apply + init-refused + init-forced.
- selvedge/restore_cmd.py implements bin/selvedge restore --from --to --verify --confirm with E_LIVE_PRIMARY exit-2.
- 15 pytest snapshot/restore cases added + symlink-to-primary test; full suite 309 passing.
- Reviewer surfaced 1 high + 3 medium + 2 low; all medium+ fixed iteration 2 review-pass clean.
## State at close

- L3 snapshot machinery live across 4 trigger points; restore CLI live with --confirm gate; state/snapshots/ gitignored.
- OI-S081-3 + OI-S081-4 closed in-band via DV-S084-1 closes_issue effects.
## Open issues

- OI-S180-1 HIGH (substrate wipe rebuild) + OI-S081-2 HIGH (L2b subagent tempdir-clone) + OI-S081-6 HIGH (L5 close-export expansion) remain open.
- OI-S081-5 MEDIUM (L4B legacy extractor) + OI-S081-7 MEDIUM (engine-v52 marker) + OI-S083-1 MEDIUM (proactive substrate-canonical reminder) remain.
## What the next session should address

- S085 implements OI-S081-2 (L2b subagent tempdir-clone via SQLite backup API) plus OI-S081-5 (L4B legacy extractor) per FR-S081-12.
- S086 implements OI-S081-6 (L5 close-export expansion across 8 enumerated artefacts) per FR-S081-13.
- S087 ships OI-S081-7 engine-v52 marker migration coupling snapshot_catalog + L5 export-manifest tables plus deliberation-seal as fifth snapshot trigger per codex Q4.
## Validator at close

- 309 pytest pass; bin/selvedge restore + take_snapshot smoke-tested manually; review-pass iteration 2 outcome=clean.
