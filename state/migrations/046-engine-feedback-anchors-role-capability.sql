-- Migration 046: seed role_write_capabilities for engine_feedback_anchors.
--
-- S194 calibration: migration 045 created the engine_feedback_anchors
-- table per DV-S194-1 but missed the role_write_capabilities INSERT
-- that handler-side _check_role_capability requires. Without this row
-- the engine-feedback handler refuses E_REFUSAL_T12 when attempting to
-- insert any anchor row, blocking the very feature 045 shipped. This
-- migration backfills the capability for the running substrate; fresh
-- init applies 045 (table) then 046 (capability) in sequence.
--
-- The split preserves 045's atomic-table-creation framing and avoids
-- editing an already-applied migration. Future migrations that ship a
-- new substrate-write target should include the capability INSERT
-- alongside the table CREATE in the same migration to avoid this
-- two-step pattern.

PRAGMA foreign_keys = OFF;

BEGIN;

INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES ('__cli__', 'engine_feedback_anchors', 'insert');

INSERT INTO schema_migrations (name, sha256) VALUES ('046-engine-feedback-anchors-role-capability.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
