-- Migration 044: engine-v52 marker — widen snapshot_catalog.trigger CHECK to
-- admit deliberation_seal; create export_manifest substrate-side recovery
-- index over markdown files emitted by `selvedge export`; bump
-- workspace_metadata.current_engine_version to engine-v52.
--
-- Closes OI-S081-7 (engine-v52 marker migration coupling) per FR-S187-14
-- + FR-S186-14 + FR-S084-14 + FR-S081-14. Sealed at S081 DV-1
-- (substrate-loss-defense-v1) C-9 write-capability framing; this session
-- ships implementation, not new design.
--
-- Why three coupled changes in one migration:
--   The three pieces all carry recovery semantics that depend on each other.
--   The deliberation_seal trigger needs the widened CHECK before
--   take_snapshot('deliberation_seal', ...) can land a row. The
--   export_manifest table needs to exist before the export pipeline starts
--   writing to it. The engine version bump is the marker that all three
--   are present together; partial application (just one or two) would
--   leave callers reaching for substrate the marker says is there.
--
-- Codex shape-consult Q3 omissions folded:
--   - SQLite CHECK enum widening requires table rebuild (no ALTER on CHECK).
--   - export_manifest framed as recovery index (not audit log): UNIQUE(path),
--     INSERT OR REPLACE on re-export, no rows for files not actually written.
--   - Path stored relative to workspace_root (cross-machine portable).
--   - sha256 computed AFTER file write (not from pre-write buffer).
--
-- pre_destructive_anchor keep_reason on init_refused / init_forced is
-- threaded through take_snapshot() in selvedge/snapshots.py; the existing
-- keep_reason CHECK enum (newest_per_trigger | count_window | time_window |
-- pre_destructive_anchor) already admits the value, so no schema change is
-- needed for that piece.

PRAGMA foreign_keys = OFF;

BEGIN;

-- T-15-CALIBRATED-BEGIN: widen snapshot_catalog.trigger CHECK to admit
-- deliberation_seal; SQLite cannot ALTER CHECK in-place, so rebuild + copy.
CREATE TABLE snapshot_catalog_new (
    snapshot_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    created_utc        TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    trigger            TEXT NOT NULL CHECK (trigger IN (
                          'session_open',
                          'session_close',
                          'migrate_apply',
                          'init_refused',
                          'init_forced',
                          'deliberation_seal',
                          'manual'
                       )),
    path               TEXT NOT NULL CHECK (length(path) BETWEEN 1 AND 512),
    sha256             TEXT NOT NULL CHECK (length(sha256) = 64),
    source_db_sha256   TEXT NOT NULL CHECK (length(source_db_sha256) = 64),
    sqlite_page_count  INTEGER NOT NULL CHECK (sqlite_page_count >= 0),
    size_bytes         INTEGER NOT NULL CHECK (size_bytes >= 0),
    source_session_no  INTEGER,
    engine_version     TEXT NOT NULL CHECK (length(engine_version) BETWEEN 1 AND 32),
    keep_reason        TEXT NOT NULL DEFAULT 'count_window' CHECK (keep_reason IN (
                          'newest_per_trigger',
                          'count_window',
                          'time_window',
                          'pre_destructive_anchor'
                       )),

    UNIQUE(path)
) STRICT;

INSERT INTO snapshot_catalog_new
    SELECT snapshot_id, created_utc, trigger, path, sha256, source_db_sha256,
           sqlite_page_count, size_bytes, source_session_no, engine_version,
           keep_reason
    FROM snapshot_catalog;

DROP TABLE snapshot_catalog;
ALTER TABLE snapshot_catalog_new RENAME TO snapshot_catalog;
-- T-15-CALIBRATED-END

CREATE INDEX idx_snapshot_catalog_trigger ON snapshot_catalog(trigger, created_utc DESC);
CREATE INDEX idx_snapshot_catalog_session ON snapshot_catalog(source_session_no);

-- export_manifest: substrate-side recovery index over markdown files
-- emitted by `selvedge export`. One row per file actually written.
-- Replace-on-rerun via UNIQUE(path) + INSERT OR REPLACE in the export
-- pipeline. session_no is the workspace_session_no for per-session
-- exports; NULL for workspace-wide artefacts (open-issues index,
-- spec_versions ledger). Loss of state/selvedge.sqlite leaves this
-- index recoverable from the markdown surface itself plus git history.
CREATE TABLE export_manifest (
    manifest_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    session_no         INTEGER,
    kind               TEXT NOT NULL CHECK (kind IN (
                          'assessment',
                          'deliberation',
                          'decisions',
                          'close',
                          'review',
                          'engine_feedback',
                          'counterfactuals',
                          'fr_dispositions',
                          'prechecks',
                          'chain_walks',
                          'harness',
                          'open_issues_index',
                          'open_issue',
                          'spec_versions_index'
                       )),
    path               TEXT NOT NULL CHECK (length(path) BETWEEN 1 AND 512),
    sha256             TEXT NOT NULL CHECK (length(sha256) = 64),
    size_bytes         INTEGER NOT NULL CHECK (size_bytes >= 0),
    row_count          INTEGER NOT NULL DEFAULT 0 CHECK (row_count >= 0),
    generated_at       TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),

    UNIQUE(path)
) STRICT;

CREATE INDEX idx_export_manifest_session ON export_manifest(session_no);
CREATE INDEX idx_export_manifest_kind ON export_manifest(kind);

UPDATE workspace_metadata SET value = 'engine-v52' WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('044-engine-v52-marker.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
