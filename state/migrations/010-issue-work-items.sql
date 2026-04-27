-- Migration 010: issue_work_items M:N join + work_items.kind widening + T-24.
-- engine-v22 → engine-v23 (session 089 D-1, deliberation 5 synthesis).
--
-- Adopts DV-S089-1: a work_item may resolve multiple issues (M:N), so the
-- linkage lives in a join table rather than a column on either side. The
-- work_items.kind enum widens to admit 'issue_resolution' (existing values
-- preserved as superset). T-24 refuses an issue's status moving to
-- resolved/superseded while any linked work_item is still queued or leased
-- (orphan-on-resolve refusal).
--
-- T-15 compliance: this migration uses ADD-only DDL on a non-CHECK-relaxation
-- shape PLUS one CHECK relaxation on work_items.kind. The kind widening uses
-- the T-15-CALIBRATED block (table recreation: CREATE TABLE work_items_new +
-- INSERT SELECT + DROP + RENAME + recreate triggers).

PRAGMA foreign_keys = ON;

BEGIN;

-- Defer FK checks for the work_items recreation (other tables have FKs to it).
PRAGMA defer_foreign_keys = 1;

-- ============================================================================
-- 1. issue_work_items: M:N linkage between issues and work_items.
-- ============================================================================
CREATE TABLE issue_work_items (
    issue_work_item_id   INTEGER PRIMARY KEY,
    issue_id             INTEGER NOT NULL REFERENCES issues(issue_id),
    work_item_id         INTEGER NOT NULL REFERENCES work_items(work_item_id),
    relation             TEXT NOT NULL DEFAULT 'resolves' CHECK (relation IN (
                            'resolves','informs','blocks_progress'
                         )),
    created_session_id   INTEGER NOT NULL REFERENCES sessions(session_id),
    created_at           TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    UNIQUE (issue_id, work_item_id, relation)
) STRICT;

CREATE INDEX idx_issue_work_items_issue ON issue_work_items(issue_id, relation);
CREATE INDEX idx_issue_work_items_work_item ON issue_work_items(work_item_id, relation);

-- ============================================================================
-- 2. T-15-CALIBRATED: widen work_items.kind to admit 'issue_resolution'.
-- ============================================================================

-- Drop dependent triggers before recreating the table; recreate them after.
-- T-11 lives on sessions but its body references work_items, so it must also
-- be dropped (SQLite validates trigger bodies at table-drop time).
DROP TRIGGER IF EXISTS t16_work_items_lease_not_expired;
DROP TRIGGER IF EXISTS t16_work_items_lease_not_expired_upd;
DROP TRIGGER IF EXISTS t11_close_requires_workitems_clear;

-- T-15-CALIBRATED-BEGIN: widen work_items.kind to admit issue_resolution. Pure superset; no kind removed.
CREATE TABLE work_items_new (
    work_item_id       INTEGER PRIMARY KEY,
    session_id         INTEGER NOT NULL REFERENCES sessions(session_id),
    kind               TEXT NOT NULL CHECK (kind IN (
                          'specify','decide','deliberate','review','other','issue_resolution'
                       )),
    payload_json       TEXT NOT NULL,
    status             TEXT NOT NULL CHECK (status IN ('queued','leased','completed','failed')),
    leased_by          TEXT,
    leased_at          TEXT,
    lease_expires_at   TEXT,
    completed_at       TEXT,
    idempotency_key    TEXT UNIQUE
) STRICT;
INSERT INTO work_items_new SELECT * FROM work_items;
DROP TABLE work_items;
ALTER TABLE work_items_new RENAME TO work_items;
-- T-15-CALIBRATED-END

-- Recreate T-16 triggers on the renamed table.
CREATE TRIGGER t16_work_items_lease_not_expired
BEFORE INSERT ON work_items
FOR EACH ROW
WHEN NEW.status = 'leased'
 AND NEW.lease_expires_at IS NOT NULL
 AND NEW.lease_expires_at < strftime('%Y-%m-%dT%H:%M:%fZ','now')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T16: cannot insert leased row with already-expired lease');
END;
CREATE TRIGGER t16_work_items_lease_not_expired_upd
BEFORE UPDATE ON work_items
FOR EACH ROW
WHEN NEW.status = 'leased'
 AND NEW.lease_expires_at IS NOT NULL
 AND NEW.lease_expires_at < strftime('%Y-%m-%dT%H:%M:%fZ','now')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T16: cannot mark row leased with already-expired lease');
END;

-- Recreate T-11 (was dropped before work_items recreation).
CREATE TRIGGER t11_close_requires_workitems_clear
BEFORE UPDATE OF status ON sessions
FOR EACH ROW
WHEN OLD.status = 'open' AND NEW.status = 'closed'
 AND EXISTS (
    SELECT 1 FROM work_items w
    WHERE w.session_id = NEW.session_id
      AND w.status IN ('queued','leased','failed')
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T11: cannot close session with in-flight work_items');
END;

-- ============================================================================
-- 3. T-24: refuse issues.status → resolved/superseded while linked work_items
-- are still queued or leased. Orphan-on-resolve refusal per DV-S089-1.
-- ============================================================================
CREATE TRIGGER t24_issues_no_resolve_with_open_work_items
BEFORE UPDATE OF status ON issues
FOR EACH ROW
WHEN NEW.status IN ('resolved','superseded')
 AND OLD.status NOT IN ('resolved','superseded')
 AND EXISTS (
    SELECT 1 FROM issue_work_items iwi
    JOIN work_items w ON w.work_item_id = iwi.work_item_id
    WHERE iwi.issue_id = NEW.issue_id
      AND iwi.relation = 'resolves'
      AND w.status IN ('queued','leased')
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T24: cannot resolve issue with linked queued/leased work_items');
END;

-- ============================================================================
-- 4. role_write_capabilities for issue_work_items.
-- ============================================================================
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','issue_work_items','insert');

INSERT INTO schema_migrations (name, sha256) VALUES ('010-issue-work-items.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
