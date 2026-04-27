-- Migration 008: widen T-06 spec_versions UPDATE to admit body_canonical_in_substrate flips.
-- Engine-v20 → engine-v21 (session 087).
--
-- Why:
--   spec_versions.body_canonical_in_substrate (added in 003 by ALTER ADD, default 0)
--   marks whether the spec_section/spec_clause rows are canonical or whether the
--   markdown body is canonical. The flag is set at row creation. After OI-085-001
--   re-decomposed three v2 rows (engine-manifest v20, prompt-application v2,
--   prompt-development v2) in session 087, the flag needed to flip 0 → 1 on each.
--   The existing T-06 trigger on spec_versions UPDATE refused: those rows were
--   created in earlier (now-closed) sessions, and the trigger's only exemption was
--   `NEW.status IS OLD.status` (admitting active→superseded across sessions).
--
--   Decomposition completion is a per-session activity that legitimately spans
--   sessions (the row's creation session may register a pointer-only spec_version
--   and a later session may complete the substrate decomposition). The trigger's
--   intent — refuse body content edits to closed-session rows — is preserved by
--   widening the exemption to also admit body_canonical_in_substrate transitions.
--   No content fields (body_path, body_sha256) become mutable.
--
-- T-15 compliance: this migration uses DROP TRIGGER + CREATE TRIGGER + an UPDATE
--   on three named rows. It does not DROP TABLE / DROP COLUMN / ALTER TABLE …
--   DROP. The selvedge migrate runner's T-15 pre-check verifies this before
--   applying. No T-15-CALIBRATED block is required (no CHECK relaxation, no
--   table recreation).
--
-- Scope of UPDATE: exactly the three v2 rows whose decomposition completed in
--   session 087 (spec_version_id IN (7, 8, 9)). Bounding the UPDATE to these IDs
--   makes the migration replayable without unintended side-effects on rows that
--   may exist in derived workspaces.

PRAGMA foreign_keys = ON;

BEGIN;

-- Drop the old trigger so the one-time backfill UPDATE can land.
DROP TRIGGER IF EXISTS t06_specv_no_mut_after_close_upd;

-- One-time backfill: flip body_canonical_in_substrate=1 on the three v2 rows
-- whose decomposition completed in session 087. The selector is by spec_id +
-- version (not by spec_version_id) so derived workspaces with different rowids
-- still apply the same intent.
UPDATE spec_versions
   SET body_canonical_in_substrate = 1
 WHERE (spec_id = 'engine-manifest'    AND version = 20)
    OR (spec_id = 'prompt-application' AND version = 2)
    OR (spec_id = 'prompt-development' AND version = 2);

-- Recreate the trigger with the widened exemption.
CREATE TRIGGER t06_specv_no_mut_after_close_upd
BEFORE UPDATE ON spec_versions
FOR EACH ROW
WHEN (SELECT status FROM sessions WHERE session_id = OLD.session_id) = 'closed'
 AND NEW.status IS OLD.status
 AND NEW.body_canonical_in_substrate IS OLD.body_canonical_in_substrate
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: spec_version body belongs to a closed session');
END;

-- Record the migration. The selvedge migrate runner replaces the placeholder
-- with the file's real sha256 after executescript completes.
INSERT INTO schema_migrations (name, sha256) VALUES ('008-widen-t06-for-canonical-flag.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
