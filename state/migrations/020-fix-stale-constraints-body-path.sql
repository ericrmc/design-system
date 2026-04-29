-- Migration 020: fix stale body_path on superseded constraints v1 spec_versions row.
-- Engine-v33 (session 111). Implements DV-S111-1; closes OI-S110-2.
--
-- Why:
--   When S109 subtracted constraints from the engine-definition set, the v1 row
--   in spec_versions transitioned active -> superseded and the file was moved
--   from specifications/constraints.md to archive/specifications/constraints-v1.md.
--   The body_path field on the superseded row was not updated at supersede time;
--   it still points at specifications/constraints.md, which no longer exists.
--   The body_sha256 still matches the archive file (no content change), so the
--   correction is a pointer fix only.
--
--   T-06 (t06_specv_no_mut_after_close_upd) refuses direct UPDATE on closed-session
--   spec_versions rows except for status active->superseded transitions and
--   body_canonical_in_substrate flips. body_path mutation is not exempted, by
--   design: spec content is otherwise immutable post-close.
--
--   Per DV-S111-1 we apply a one-time calibrated backfill rather than widening
--   T-06 to admit body_path mutation generally. The pattern mirrors migration
--   008-widen-t06-for-canonical-flag.sql: drop the trigger, run a scoped UPDATE,
--   recreate the trigger UNCHANGED. This case is unusual (subtraction with file
--   relocation rather than in-place overwrite of the working spec file); the
--   per-incident audit trail is preferable to a broader mutation exemption.
--
-- T-15 compliance: DROP TRIGGER + scoped UPDATE + CREATE TRIGGER. No DROP TABLE,
--   no DROP COLUMN, no ALTER TABLE ... DROP. No CHECK relaxation. No
--   T-15-CALIBRATED block required.
--
-- Scope of UPDATE: exactly the constraints v1 row, selected by (spec_id='constraints'
--   AND version=1). Selector is by spec_id+version (not by spec_version_id) so
--   derived workspaces with different rowids still apply the same intent.

PRAGMA foreign_keys = ON;

BEGIN;

-- Drop the T-06 UPDATE trigger so the one-shot backfill can land.
DROP TRIGGER IF EXISTS t06_specv_no_mut_after_close_upd;

-- Scoped backfill: point the superseded constraints v1 row at its archive location.
-- body_sha256 b632567b2959573ef9c273c8b56a285951380a1efc76677f42a9d38630a517b9
-- already matches archive/specifications/constraints-v1.md; this is a pointer-only fix.
UPDATE spec_versions
   SET body_path = 'archive/specifications/constraints-v1.md'
 WHERE spec_id = 'constraints'
   AND version = 1
   AND status = 'superseded';

-- Recreate the trigger UNCHANGED (same body as migration 008).
CREATE TRIGGER t06_specv_no_mut_after_close_upd
BEFORE UPDATE ON spec_versions
FOR EACH ROW
WHEN (SELECT status FROM sessions WHERE session_id = OLD.session_id) = 'closed'
 AND NEW.status IS OLD.status
 AND NEW.body_canonical_in_substrate IS OLD.body_canonical_in_substrate
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: spec_version body belongs to a closed session');
END;

INSERT INTO schema_migrations (name, sha256) VALUES ('020-fix-stale-constraints-body-path.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
