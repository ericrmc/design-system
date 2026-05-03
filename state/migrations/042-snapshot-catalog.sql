-- Migration 042: snapshot_catalog table for L3 boundary snapshots (DV-S081-1).
--
-- Closes part of OI-S081-3 (snapshot machinery) per FR-S081-11. The catalog
-- carries one row per snapshot file written by selvedge/snapshots.py via
-- sqlite3.Connection.backup() at four trigger points:
--   - session_open    (after submit session-open commits)
--   - session_close   (after submit session-close commits)
--   - migrate_apply   (after migrate --apply succeeds; one row per run)
--   - init_refused    (before E_LIVE_SUBSTRATE refusal in init_cmd)
--   - init_forced     (before unlink in init --really-force path)
-- Plus one operator-driven trigger:
--   - manual          (snapshot kind reserved; not yet exposed via CLI at v1)
--
-- The schema is a pure additive create; no data backfill. Rows are populated
-- by selvedge/snapshots.py in a fresh connection after the trigger event has
-- itself committed (so a rolled-back submit produces no snapshot row).
--
-- Retention metadata: keep_reason carries the policy band that retained the
-- row at last prune ('newest_per_trigger' | 'count_window' | 'time_window' |
-- 'pre_destructive_anchor'). Default at write time is 'count_window' until
-- the first prune fires (engine-v51 ships count + age + per-trigger anchors
-- per S084 codex-consult Q2; prune itself lands at OI-S081-7 marker arc
-- since v1 retention defaults are conservative enough to defer).

PRAGMA foreign_keys = OFF;

BEGIN;

CREATE TABLE snapshot_catalog (
    snapshot_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    created_utc        TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    trigger            TEXT NOT NULL CHECK (trigger IN (
                          'session_open',
                          'session_close',
                          'migrate_apply',
                          'init_refused',
                          'init_forced',
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

CREATE INDEX idx_snapshot_catalog_trigger ON snapshot_catalog(trigger, created_utc DESC);
CREATE INDEX idx_snapshot_catalog_session ON snapshot_catalog(source_session_no);

INSERT INTO schema_migrations (name, sha256) VALUES ('042-snapshot-catalog.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
