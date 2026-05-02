-- Migration 034: legacy_unresolved_cites quarantine table.
-- engine-v48 unchanged (additive CREATE TABLE).
--
-- Why:
--   D-28 C-2 cross-family convergence: NULL-cite hardening cannot ship as
--   blanket NOT NULL because legacy decision_supports + alternative_rejections
--   rows already violate the predicate. P-4 codex proposed legacy_unresolved
--   _cites quarantine table as the structural answer: legacy NULL-cite rows
--   stay in their original tables, the quarantine table records the
--   alias-as-claim-text + reason fields surfaced for review tooling, and
--   migration 036 trigger T-34 refuses only NEW rows with NULL cited_object
--   _id on cite-required bases.
--
--   The quarantine table is empty at S179 close; future tooling or operator
--   action populates it from existing NULL-cite rows (132 decision_supports
--   + 153 alternative_rejections measured at S179) where alias-as-claim-text
--   parsing succeeds. At S179 the table SHAPE ships; population is opt-in.
--
-- Schema:
--   legacy_unresolved_cites                            INTEGER PRIMARY KEY
--     One row per legacy NULL-cite row that is captured for review tooling.
--   parent_table                                       TEXT NOT NULL CHECK
--     Enum: decision_supports | alternative_rejections.
--   parent_id                                          INTEGER NOT NULL
--     The decision_support_id or alternative_rejection_id. No FK because
--     the parent rows pre-date this migration and cascade behaviour should
--     not retroactively delete.
--   basis                                              TEXT NOT NULL
--     Mirrors the basis enum from the parent table.
--   alias_text                                         TEXT NULL
--     Best-effort alias extracted from claim text or rejection reason.
--     NULL admitted when alias parser cannot resolve.
--   reason                                             TEXT NOT NULL
--     Capture-time reason ('alias-not-in-objects', 'OI-or-FR-not-citable',
--     'pre-engine-v45', 'malformed-claim-text', other). Non-empty.
--   created_at                                         TEXT default
--
-- T-15 compliance:
--   Additive CREATE TABLE only — no DROP, no ALTER, no CHECK relaxation.
--   No T-15-CALIBRATED block needed.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TABLE legacy_unresolved_cites (
    cite_id INTEGER PRIMARY KEY AUTOINCREMENT,
    parent_table TEXT NOT NULL CHECK (parent_table IN ('decision_supports','alternative_rejections')),
    parent_id INTEGER NOT NULL,
    basis TEXT NOT NULL CHECK (length(basis) > 0),
    alias_text TEXT,
    reason TEXT NOT NULL CHECK (length(reason) > 0),
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    UNIQUE(parent_table, parent_id)
);

CREATE INDEX idx_legacy_unresolved_cites_parent ON legacy_unresolved_cites(parent_table, parent_id);
CREATE INDEX idx_legacy_unresolved_cites_basis ON legacy_unresolved_cites(basis);

INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES ('__cli__', 'legacy_unresolved_cites', 'insert');

INSERT INTO schema_migrations (name, sha256) VALUES ('034-legacy-unresolved-cites-quarantine.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
