-- Migration 053: cycle-ledger v1.1 — auto-SR suppression CHECK at SQL layer.
-- engine-v57 -> engine-v58 (S203 within-session refinement addressing
-- review-finding F-03 reviewer-iter-1; closes review path of DV-S203-1 ship).
--
-- Why:
--   D-9 C-1 synthesis at S203: cycle row IS the substrate proof of
--   observation; "non-substantial NEVER cites SL; substantial MAY cite SL
--   when real supersession relation exists". Migration 052 enforced the
--   substantial-requires-reason coupling at SQL CHECK + handler layer, but
--   omitted the dual coupling (non-substantial-cannot-cite-SL). Reviewer
--   F-03 surfaced the gap: the deliberation synthesis was substrate-
--   underenforced.
--
--   Handler-side validation alone is a weaker form of the discipline (per
--   DV-S176-1 lesson: when a discipline depends on the agent reaching for
--   a tool the substrate could dispatch automatically, ship the substrate
--   dispatch). Within-session refinement adds the missing CHECK before
--   close.
--
-- Schema change:
--   cycle_ledger: add CHECK (
--       classification != 'non-substantial'
--       OR citing_supersession_object_id IS NULL
--   )
--   This is a strict superset over existing rows (the 1 existing row
--   CYC-S203-1 from the migration-052 smoke-test has classification=
--   'non-substantial' and citing_supersession_object_id=NULL, satisfying
--   the new CHECK). T-15-CALIBRATED rebuild records the constraint addition.
--
-- T-15 compliance:
--   - CHECK is non-destructive: admits strictly more rows than necessary
--     (it forbids only the (non-substantial + non-NULL FK) state which
--     was always semantically illegal per D-9 C-1).
--   - PRAGMA foreign_keys=OFF for the rebuild duration.
--   - cycle_ledger has no incoming refs from triggers, so no trigger drop/
--     recreate is needed (T-42 reads objects in WHEN clause but does not
--     reference cycle_ledger by name).
--
-- T-42 trigger preservation:
--   T-42 (cycle_ledger BEFORE INSERT subject allowlist) is recreated as
--   part of the rebuild because triggers attach to the table not the
--   table-name; dropping cycle_ledger drops the trigger.

PRAGMA foreign_keys = OFF;

BEGIN;

-- Drop the trigger; recreated below after rebuild.
DROP TRIGGER t42_cycle_subject_allowlist;

-- T-15-CALIBRATED-BEGIN: add CHECK enforcing non-substantial cycles cannot cite SL per D-9 C-1 synthesis. Pure superset over existing rows (verified: 1 row CYC-S203-1 with classification='non-substantial' AND citing_supersession_object_id=NULL satisfies new CHECK).
CREATE TABLE cycle_ledger_new (
    cycle_id                       INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id                     INTEGER NOT NULL REFERENCES sessions(session_id),
    subject_object_id              INTEGER NOT NULL REFERENCES objects(object_id),
    cycle_no                       INTEGER NOT NULL,
    observed_at                    TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    snapshot_atom_id               INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    classification                 TEXT NOT NULL CHECK (classification IN (
                                       'substantial',
                                       'non-substantial'
                                   )),
    classification_reason_atom_id  INTEGER REFERENCES text_atoms(atom_id),
    citing_supersession_object_id  INTEGER REFERENCES objects(object_id),
    object_id                      INTEGER REFERENCES objects(object_id),
    created_at                     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    -- D-9 D-2 synthesis (existing): substantial requires classification_reason atom.
    CHECK (
        classification != 'substantial'
        OR classification_reason_atom_id IS NOT NULL
    ),
    -- D-9 C-1 synthesis (NEW): non-substantial cycles cannot cite SL per
    -- "non-substantial NEVER cites SL"; reviewer F-03 fix.
    CHECK (
        classification != 'non-substantial'
        OR citing_supersession_object_id IS NULL
    ),
    UNIQUE (subject_object_id, cycle_no)
) STRICT;

INSERT INTO cycle_ledger_new (
    cycle_id, session_id, subject_object_id, cycle_no, observed_at,
    snapshot_atom_id, classification, classification_reason_atom_id,
    citing_supersession_object_id, object_id, created_at
) SELECT
    cycle_id, session_id, subject_object_id, cycle_no, observed_at,
    snapshot_atom_id, classification, classification_reason_atom_id,
    citing_supersession_object_id, object_id, created_at
FROM cycle_ledger;

DROP TABLE cycle_ledger;
ALTER TABLE cycle_ledger_new RENAME TO cycle_ledger;

CREATE INDEX idx_cycle_ledger_session ON cycle_ledger(session_id);
CREATE INDEX idx_cycle_ledger_subject ON cycle_ledger(subject_object_id);
CREATE INDEX idx_cycle_ledger_classification ON cycle_ledger(classification);
CREATE INDEX idx_cycle_ledger_supersession ON cycle_ledger(citing_supersession_object_id);
-- T-15-CALIBRATED-END

-- Recreate the T-42 subject allowlist trigger.
CREATE TRIGGER t42_cycle_subject_allowlist
BEFORE INSERT ON cycle_ledger
FOR EACH ROW
WHEN (
    SELECT object_kind
    FROM objects
    WHERE object_id = NEW.subject_object_id
) NOT IN ('assumption')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T42: cycle_ledger subject must be assumption-kind at v1 (allowlist=assumption); v2 extends to issue/decision_v2 once cross-app evidence accumulates per M-2 watch-trigger');
END;

-- Engine version bump.
UPDATE workspace_metadata
   SET value = 'engine-v58'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('053-cycle-ledger-suppression-check.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
