-- Migration 033: harness alias objects-registration (closes OI-S125-1).
-- engine-v48 unchanged (CHECK widening; additive backfill INSERT).
--
-- Why:
--   OI-S125-1 named that reference_harnesses.alias rows are NOT registered
--   in the objects table, so cross-citation [RH-S<N>-N] from decision-
--   records would fail T-01 alias resolution. DV-S179-1 closes OI-S125-1
--   by-mechanism via this migration: widen objects.object_kind CHECK to
--   admit 'reference_harness', then backfill objects rows for every
--   reference_harness so the alias becomes citable.
--
-- T-15 compliance:
--   CHECK relaxation (admitting one new object_kind value 'reference_harness')
--   is non-destructive: admits strictly more rows than the prior CHECK. The
--   T-15-CALIBRATED block records the rebuild required by SQLite for CHECK
--   relaxation. PRAGMA foreign_keys=OFF for the duration of the rebuild
--   (standard SQLite recipe for CHECK widening on a table with incoming FKs).
--   Trigger t07a_refs_no_superseded_cite references the objects table in its
--   body and is dropped + recreated around the rebuild so trigger validation
--   does not fire against the briefly-absent objects symbol.

PRAGMA foreign_keys = OFF;

BEGIN;

-- Drop the only trigger whose body references objects (recreated below).
DROP TRIGGER t07a_refs_no_superseded_cite;

-- T-15-CALIBRATED-BEGIN: widen objects.object_kind CHECK to admit reference_harness. Pure superset; no kind removed. Required so harness aliases register in objects per OI-S125-1 close.
CREATE TABLE objects_new (
    object_id      INTEGER PRIMARY KEY,
    object_kind    TEXT NOT NULL CHECK (object_kind IN (
        'decision','spec_version','perspective','deliberation',
        'commitment','engine_feedback','session','synthesis_point',
        'work_item','subtraction','agent_run',
        'assessment','decision_v2','alternative_v2','spec_section',
        'spec_clause','perspective_position','perspective_claim',
        'review_finding','text_atom','legacy_import','spec_clause_link',
        'decision_support','decision_effect','alternative_rejection',
        'close_record','close_state_item','assessment_agenda_item',
        'reference_harness'
    )),
    typed_row_id   INTEGER NOT NULL,
    alias          TEXT UNIQUE,
    created_at     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
) STRICT;
INSERT INTO objects_new (object_id, object_kind, typed_row_id, alias, created_at)
    SELECT object_id, object_kind, typed_row_id, alias, created_at FROM objects;
DROP TABLE objects;
ALTER TABLE objects_new RENAME TO objects;
CREATE INDEX idx_objects_kind_typed_row ON objects (object_kind, typed_row_id);
-- T-15-CALIBRATED-END

-- Recreate the dropped trigger.
CREATE TRIGGER t07a_refs_no_superseded_cite
BEFORE INSERT ON refs
FOR EACH ROW
WHEN NEW.relation = 'cites'
 AND NEW.allow_superseded = 0
 AND EXISTS (
    SELECT 1
    FROM objects o JOIN spec_versions sv ON sv.object_id = o.object_id
    WHERE o.object_id = NEW.target_object_id AND sv.status = 'superseded'
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T07: cite targets a superseded spec_version (set allow_superseded=1 with reason)');
END;

-- Backfill: register every reference_harness in objects with alias.
INSERT INTO objects (object_kind, typed_row_id, alias)
    SELECT 'reference_harness', harness_id, alias
    FROM reference_harnesses
    WHERE alias IS NOT NULL
      AND alias NOT IN (SELECT alias FROM objects WHERE alias IS NOT NULL);

-- Note: reference_harnesses.object_id back-pointer is NOT updated here because
-- T-36 refuses non-lifecycle UPDATEs on reference_harnesses. Alias resolution
-- works through objects.alias directly; the back-pointer is convenience-only
-- and a future T-36 calibration may admit a one-shot back-pointer fill.

INSERT INTO schema_migrations (name, sha256) VALUES ('033-harness-alias-objects-registration.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
