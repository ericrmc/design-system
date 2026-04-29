---
session: 111
title: fix-stale-constraints-body-path — assessment
engine_version_at_open: engine-v33
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

Workspace at engine-v33 with FR-S110-11 directing the smallest of three S110 follow-ups: OI-S110-2 stale body_path on superseded constraints v1.

## Agenda

1. Confirm root cause: spec_versions row 3 (constraints v1, status=superseded) carries body_path specifications/constraints.md but file was moved to archive/specifications/constraints-v1.md during S109 subtraction.
2. Decide fix: one-time calibrated backfill migration mirroring 008-widen-t06 pattern; drop T-06 UPDATE trigger, update row 3 body_path, recreate trigger unchanged.
3. Write migration 020 with surgical UPDATE scoped by spec_id+version, not rowid.
4. Apply migration and verify the row resolves to the archive file with matching sha256.
5. Run T-30 reviewer loop (Explore subagent adversarial).
6. Surface follow-up: subtraction-supersession (file moved to archive instead of overwritten in place) is a distinct pattern that may warrant a documented convention.
7. Close-time: engine_feedback row, dispose FR-S110-11 partially, close-record, export, commit, push.
