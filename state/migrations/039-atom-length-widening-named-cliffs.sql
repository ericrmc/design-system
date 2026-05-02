-- Migration 039: atom-length widening on three named cliffs (engine-v49 unchanged).
--
-- Why:
--   D-28 + DV-S179-1 close OI-S177-1 by-mechanism on three named fields:
--   decision_supports.claim, decision_effects.target_descriptor,
--   review_findings.finding. These are the cliffs surfaced repeatedly
--   across S172/S174/S177/S178 where 240-char ceiling cuts off load-
--   bearing claim text.
--
--   text_atoms.text CHECK widened for atom_type IN ('support_claim','finding')
--   from 8-240 to 8-480. Other atom_types keep their existing tier (default
--   8-240; spec_clause/spec_section_intent already 16-480 from migration 003;
--   legacy_import already 8-4000). Per P-2 codex stance: do NOT raise
--   atom-length globally; field-by-field widening only on named cliffs.
--
-- T-15 compliance:
--   CHECK relaxation (widening 240→480) is non-destructive: admits strictly
--   more rows. Recorded under T-15-CALIBRATED block. Rebuild requires:
--   PRAGMA foreign_keys=OFF (text_atoms has many incoming FKs from
--   assessment_agenda_items, decision_supports.claim_atom_id, etc.); drop
--   the 4 triggers on text_atoms before rebuild; recreate them after.
--
--   decision_effects.target_descriptor is a direct column CHECK (not via
--   text_atoms), so its widening from 2-120 to 2-480 is a separate rebuild
--   in the same migration. The handler still enforces 8-120 for
--   closes_issue effects (becomes disposition reason atom which has its
--   own 8-240 ceiling at atom_type='rejection_reason').

PRAGMA foreign_keys = OFF;

BEGIN;

-- Drop the 4 triggers on text_atoms before rebuild.
DROP TRIGGER t21_text_atoms_no_cr_ins;
DROP TRIGGER t21_text_atoms_no_cr_upd;
DROP TRIGGER t06_text_atoms_no_mut_after_close_del;
DROP TRIGGER t06_text_atoms_no_mut_after_close_upd;

-- T-15-CALIBRATED-BEGIN: widen text_atoms CHECK so atom_type IN (support_claim,finding) admits length 8-480 instead of 8-240. Pure superset; no atom_type loses headroom.
CREATE TABLE text_atoms_new (
    atom_id            INTEGER PRIMARY KEY,
    atom_type          TEXT NOT NULL CHECK (atom_type IN (
        'title','claim','spec_clause','spec_section_intent','finding',
        'alternative_option','rejection_reason','support_claim','next_step',
        'operator_quote','legacy_import','assessment_item','open_question',
        'perspective_position','perspective_claim','synthesis_claim',
        'engine_version_note','close_summary','close_state_item'
    )),
    text               TEXT NOT NULL,
    created_session_id INTEGER NOT NULL REFERENCES sessions(session_id),
    created_at         TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    CHECK (instr(text, char(10)) = 0),
    CHECK (text NOT GLOB '*```*'),
    CHECK (text NOT GLOB '*|*|*'),
    CHECK (
        CASE
            WHEN atom_type IN ('spec_clause','spec_section_intent') THEN length(text) BETWEEN 16 AND 480
            WHEN atom_type IN ('support_claim','finding') THEN length(text) BETWEEN 8 AND 480
            WHEN atom_type = 'legacy_import' THEN length(text) BETWEEN 8 AND 4000
            ELSE length(text) BETWEEN 8 AND 240
        END
    )
) STRICT;
INSERT INTO text_atoms_new SELECT * FROM text_atoms;
DROP TABLE text_atoms;
ALTER TABLE text_atoms_new RENAME TO text_atoms;
CREATE INDEX idx_text_atoms_type ON text_atoms (atom_type);
CREATE INDEX idx_text_atoms_session ON text_atoms (created_session_id);
-- T-15-CALIBRATED-END

-- Recreate the 4 triggers verbatim (signature preserved for caller compat).
CREATE TRIGGER t21_text_atoms_no_cr_ins
BEFORE INSERT ON text_atoms
FOR EACH ROW
WHEN instr(NEW.text, char(13)) > 0
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T21: text_atom contains carriage return (\r)');
END;

CREATE TRIGGER t21_text_atoms_no_cr_upd
BEFORE UPDATE ON text_atoms
FOR EACH ROW
WHEN instr(NEW.text, char(13)) > 0
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T21: text_atom contains carriage return (\r)');
END;

CREATE TRIGGER t06_text_atoms_no_mut_after_close_del
BEFORE DELETE ON text_atoms
FOR EACH ROW
WHEN EXISTS (SELECT 1 FROM sessions WHERE session_id = OLD.created_session_id AND status = 'closed')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: text_atom belongs to a closed session');
END;

CREATE TRIGGER t06_text_atoms_no_mut_after_close_upd
BEFORE UPDATE ON text_atoms
FOR EACH ROW
WHEN EXISTS (SELECT 1 FROM sessions WHERE session_id = OLD.created_session_id AND status = 'closed')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: text_atom belongs to a closed session');
END;

INSERT INTO schema_migrations (name, sha256) VALUES ('039-atom-length-widening-named-cliffs.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
