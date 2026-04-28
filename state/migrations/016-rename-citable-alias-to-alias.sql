-- Migration 016: rename citable_alias to alias on objects and issues.
-- engine-v29 → engine-v30 (S102 D-1, closing OI-S101-1).
--
-- Why:
--   `citable_alias` is the most-trafficked column name in the schema. The
--   shorter `alias` reduces friction for every agent authoring SQL or
--   payloads against the substrate. Several read-paths already alias the
--   column to `alias` in SELECT (e.g. cli.py:2485 `o.citable_alias AS
--   alias`), confirming the shorter name is the preferred surface. This
--   migration removes the indirection at the storage layer.
--
-- Why ALTER TABLE RENAME COLUMN, not the calibrated table-rebuild dance:
--   The first attempt at this migration used CREATE _new + INSERT + DROP +
--   RENAME on objects and issues. It failed at COMMIT with FOREIGN KEY
--   constraint failure because dropping `objects` orphans dozens of
--   referrers (spec_versions, decisions, perspectives, etc.) within the
--   same transaction. SQLite ≥ 3.25.0 admits `ALTER TABLE … RENAME COLUMN
--   … TO …` as a non-destructive operation that automatically rewrites
--   trigger bodies' column references and preserves all FK references by
--   table name. T-15 admits this: T15_FORBIDDEN_PATTERNS forbids
--   `ALTER TABLE … DROP`, not `ALTER TABLE … RENAME COLUMN`.
--
-- Trigger surface:
--   ALTER TABLE RENAME COLUMN auto-rewrites column references inside
--   trigger bodies but does NOT rewrite string literals. The T-22
--   alias-format trigger's error message says
--   `issues.citable_alias must match …`; we DROP + reissue to update the
--   message to `issues.alias must match …`. T-22a status-consistency and
--   T-24 work-items triggers reference neither the renamed column nor the
--   old name in their messages — they survive the rename untouched.
--
-- Engine version: bumped to engine-v30 by handler dispatch when the
--   subsequent spec-version submission for engine-manifest v30 fires
--   (cf. migration 011 commentary; S091 _submit_spec_version
--   atomically updates workspace_metadata).

PRAGMA foreign_keys = ON;

BEGIN;

-- 1. objects.citable_alias → objects.alias.
ALTER TABLE objects RENAME COLUMN citable_alias TO alias;

-- 2. issues.citable_alias → issues.alias.
ALTER TABLE issues RENAME COLUMN citable_alias TO alias;

-- 3. Reissue T-22 alias-format trigger so the error message names the new
--    column. Column references inside the trigger body were rewritten by the
--    RENAME COLUMN step above; only the string literal in RAISE() needs
--    updating.
DROP TRIGGER t22_issues_alias_format;
CREATE TRIGGER t22_issues_alias_format
BEFORE INSERT ON issues
FOR EACH ROW
WHEN NOT (
    NEW.alias GLOB 'OI-[0-9]*'
    OR NEW.alias GLOB 'OI-S[0-9][0-9][0-9]-[0-9]*'
)
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T22: issues.alias must match OI-NNN[-...] or OI-SNNN-N[-...]');
END;

INSERT INTO schema_migrations (name, sha256) VALUES ('016-rename-citable-alias-to-alias.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
