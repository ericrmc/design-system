-- Migration 019: harvested_engine_feedback ledger for monitor-external harvest-ef.
-- engine-v32 -> engine-v33 (S110 D-1, closing the substrate-direct harvest gap).
--
-- Why:
--   Engine-v26 (S094) made `submit engine-feedback` the canonical author path so
--   external workspaces write feedback rows directly to substrate, no markdown
--   intermediate. But _me_harvest_ef (added engine-v31) still walks the peer's
--   engine-feedback/EF-*.md directory. Against substrate-only peers (the
--   disaster-recovery workspace is the live example) it returns
--   "no engine-feedback/ directory" and silently fails to harvest anything.
--
--   S110 D-1 adopts substrate-direct read: harvest-ef now opens the peer
--   sqlite via file:?mode=ro and queries the engine_feedback table. To make
--   re-runs idempotent at row precision (the prior --since-session filter is
--   coarse and admits partial-harvest re-run as duplicate inserts), this
--   migration adds a small ledger table keyed by the peer's workspace_id +
--   peer feedback_id with a FK to the locally-imported objects row.
--
--   The deliberation (substrate deliberation_id=10, P-1 anthropic + P-2 codex
--   cross-family) converged on per-row keys over body_md provenance markers
--   (R-1.3 rejected: parse-prose-as-state for the control plane is the
--   pattern engine-v20 eliminated for the data plane; ledger is cheap and
--   structurally honest).
--
-- Schema:
--   harvested_engine_feedback
--     - harvest_id INTEGER PRIMARY KEY
--     - peer_workspace_id TEXT NOT NULL  (peer's workspace_metadata.workspace_id)
--     - peer_feedback_id INTEGER NOT NULL  (peer's engine_feedback.feedback_id)
--     - peer_alias TEXT  (peer's objects.alias if present at harvest time, else NULL)
--     - imported_object_id INTEGER NOT NULL REFERENCES objects(object_id)
--         (the self-dev objects row created by submit engine-feedback)
--     - session_id INTEGER NOT NULL REFERENCES sessions(session_id)
--         (the self-dev session that performed the harvest)
--     - harvested_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
--     - UNIQUE (peer_workspace_id, peer_feedback_id)
--
-- T-15 compliance: this migration uses CREATE TABLE + INSERT INTO
--   role_write_capabilities + INSERT INTO schema_migrations only. No DROP
--   TABLE, no DROP COLUMN, no ALTER TABLE. The selvedge migrate runner's T-15
--   pre-check verifies this before applying.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TABLE harvested_engine_feedback (
    harvest_id          INTEGER PRIMARY KEY,
    peer_workspace_id   TEXT NOT NULL,
    peer_feedback_id    INTEGER NOT NULL,
    peer_alias          TEXT,
    imported_object_id  INTEGER NOT NULL REFERENCES objects(object_id),
    session_id          INTEGER NOT NULL REFERENCES sessions(session_id),
    harvested_at        TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    UNIQUE (peer_workspace_id, peer_feedback_id)
) STRICT;

CREATE INDEX idx_harvested_ef_peer_workspace
    ON harvested_engine_feedback (peer_workspace_id);

INSERT INTO role_write_capabilities (role, table_name, write_op)
VALUES ('__cli__', 'harvested_engine_feedback', 'insert');

INSERT INTO schema_migrations (name, sha256)
VALUES ('019-harvested-engine-feedback-ledger.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
