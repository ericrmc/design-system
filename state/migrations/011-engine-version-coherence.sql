-- Migration 011: workspace_metadata.current_engine_version coherence.
-- Engine-v24 → engine-v25 (session 091).
--
-- Why:
--   Two sources of truth for engine version diverged across S087/S088/S089/S090:
--     - spec_versions row for spec_id='engine-manifest' with status='active'
--     - workspace_metadata row for key='current_engine_version'
--   Migration 007 seeded the metadata row at engine-v20 and no subsequent
--   bump propagated to it structurally. By S091 open, spec_versions said
--   engine-manifest v24 was active while the metadata still said engine-v23,
--   so session-open and orient both used the stale value. The handler change
--   in `selvedge/cli.py` _submit_spec_version (S091) now updates the metadata
--   atomically when a spec_id='engine-manifest' row is inserted.
--
-- Two changes here:
--   1. Seed `__cli__` UPDATE capability on workspace_metadata so the handler
--      can call _check_role_capability without raising T-12. T-12 is
--      application-layer; the seed is the gate.
--   2. One-time backfill: bring `current_engine_version` to 'engine-v24',
--      the value implied by the active spec_versions row at S091 open. The
--      backfill runs unconditionally; in a derived workspace where the row
--      already says engine-v24 the UPDATE is a no-op.
--
-- T-15 compliance: this migration is INSERT + UPDATE only; no DDL of any
--   kind. The selvedge migrate runner's T-15 pre-check passes without a
--   calibrated block.

PRAGMA foreign_keys = ON;

BEGIN;

INSERT OR IGNORE INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__', 'workspace_metadata', 'update');

UPDATE workspace_metadata
   SET value = 'engine-v24'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('011-engine-version-coherence.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
