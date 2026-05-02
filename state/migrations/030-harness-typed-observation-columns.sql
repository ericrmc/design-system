-- Migration 030: harness typed-observation columns (workspace-experimental).
-- engine-v47 unchanged (additive substrate columns, no kernel methodology change).
--
-- Why:
--   DV-S152-1 adopted the hybrid typed-observation pathway for conflict and
--   closure vocabulary at the workspace-experimental harness substrate kind:
--   nullable opt-in atoms with no closed enum, kernel methodology names no
--   canonical values, second-arc evidence becomes possible without committing
--   to a fixed taxonomy. Methodology v9 records this clause; OI-S152-1
--   tracks the substrate addition.
--
--   S172 burns down OI-S152-1 narrowly: two columns, no CHECK enum, no
--   handler enum vocabulary. Kernel-agnostic exactly as DV-S152-1 ratified.
--
-- Schema:
--   reference_harnesses.closure_kind_atom_id          INTEGER NULL FK text_atoms
--     Optional closure-shape observation captured at seal time. NULL is the
--     valid default; arbitrary non-empty atom text accepted; no enum CHECK.
--     Lives on the closure/transition row per S152 D-20 deliberation lines
--     65-66.
--   reference_harness_dissent.conflict_kind_atom_id   INTEGER NULL FK text_atoms
--     Optional conflict-shape observation captured per dissent row.
--     NULL is the valid default; arbitrary non-empty atom text accepted;
--     no enum CHECK. Lives on the active-conflict observation row per
--     S152 D-20 deliberation lines 65-66.
--
-- Per S152 synthesis: typed-observation columns live on the harness substrate
-- kind not on kernel rows; the slot is opt-in with NULL as valid default;
-- a graduation-review trigger criteria (OI-S152-2) governs when second-arc
-- evidence might motivate promotion to canonical enum.
--
-- T-15 compliance:
--   Additive only — ALTER TABLE ADD COLUMN with NULL default and FK
--   reference. No DROP TABLE, DROP COLUMN, ALTER TABLE ... DROP, no
--   widening of existing CHECK constraints. No T-15-CALIBRATED block needed.

PRAGMA foreign_keys = ON;

BEGIN;

ALTER TABLE reference_harnesses
    ADD COLUMN closure_kind_atom_id INTEGER REFERENCES text_atoms(atom_id);

ALTER TABLE reference_harness_dissent
    ADD COLUMN conflict_kind_atom_id INTEGER REFERENCES text_atoms(atom_id);

INSERT INTO schema_migrations (name, sha256) VALUES ('030-harness-typed-observation-columns.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
