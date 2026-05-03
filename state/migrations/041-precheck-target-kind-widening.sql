-- Migration 041: widen decision_prechecks.target_kind CHECK to admit all decision target_kinds.
--
-- Why:
--   Calibration surfaced at S081 mid-deliberation: T-33 (handler-side, engine-v49) requires
--   precheck.target_kind == decision_v2.target_kind. But migration 035 narrowed precheck CHECK
--   to ('decision_v2') only, while decisions_v2.target_kind admits seven values
--   (process_rule, spec_version, migration, issue, review_rule, engine_version, open_question)
--   and explicitly does NOT admit 'decision_v2'. The two CHECK constraints are mutually
--   exclusive, making T-33 impossible to satisfy for any substantive or schema_migration
--   decision-record.
--
--   Migration 035 line 32 anticipated this: "future kinds may admit ... via migration
--   NN-CALIBRATED widening." This migration is that widening.
--
--   Selvedge/precheck.py PRECHECK_TARGET_KINDS and selvedge/cli.py argparse choices
--   are widened in the same engine-v51 release.
--
-- Schema change:
--   decision_prechecks.target_kind CHECK admits the seven decision target_kinds plus
--   the legacy 'decision_v2' (which migration 035 was the only producer of, kept for
--   backward-compat with any rows produced before this calibration).
--
-- T-15 calibrated rebuild dance:
--   SQLite cannot ALTER a CHECK constraint in-place; we drop+recreate the table and
--   restore data. The decision_prechecks substrate is small (1 row at S081) so this
--   is mechanical.

PRAGMA foreign_keys = OFF;

BEGIN;

-- T-15-CALIBRATED-BEGIN: relax decision_prechecks.target_kind CHECK to admit all decision target_kinds; SQLite cannot ALTER CHECK in-place.
CREATE TABLE decision_prechecks_new (
    precheck_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id         INTEGER NOT NULL REFERENCES sessions(session_id),
    target_kind        TEXT NOT NULL CHECK (target_kind IN (
                          'decision_v2',
                          'process_rule',
                          'spec_version',
                          'migration',
                          'issue',
                          'review_rule',
                          'engine_version',
                          'open_question'
                       )),
    target_key         TEXT NOT NULL CHECK (length(target_key) BETWEEN 2 AND 120),
    context_sha256     TEXT NOT NULL CHECK (length(context_sha256) = 64),
    nonce              TEXT NOT NULL CHECK (length(nonce) BETWEEN 16 AND 64),
    ttl_seconds        INTEGER NOT NULL DEFAULT 1800 CHECK (ttl_seconds BETWEEN 30 AND 3600),
    walker_version     TEXT NOT NULL CHECK (length(walker_version) >= 1),
    created_at         TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    consumed_at        TEXT,
    consumed_by_decision_v2_id INTEGER REFERENCES decisions_v2(decision_v2_id),

    UNIQUE(session_id, target_kind, target_key, nonce)
) STRICT;

INSERT INTO decision_prechecks_new
    SELECT precheck_id, session_id, target_kind, target_key, context_sha256, nonce,
           ttl_seconds, walker_version, created_at, consumed_at, consumed_by_decision_v2_id
    FROM decision_prechecks;

DROP TABLE decision_prechecks;
ALTER TABLE decision_prechecks_new RENAME TO decision_prechecks;
-- T-15-CALIBRATED-END

CREATE INDEX idx_decision_prechecks_session ON decision_prechecks(session_id);
CREATE INDEX idx_decision_prechecks_target ON decision_prechecks(target_kind, target_key);

UPDATE workspace_metadata SET value = 'engine-v51' WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('041-precheck-target-kind-widening.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
