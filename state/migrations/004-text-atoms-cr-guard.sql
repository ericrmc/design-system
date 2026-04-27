-- 004-text-atoms-cr-guard.sql
-- engine-v20 follow-up; ships in S084 alongside 003.
-- Per S084 reviewer F6: the text_atoms CHECK forbids LF (char(10)) but not CR
-- (char(13)). Windows-style CRLF line endings would slip through and create
-- silent data inconsistency. Add a trigger-based guard since CHECK constraint
-- modification on the existing table is not additive (operator already
-- ratified one CHECK-relaxation in 003; we keep this fix non-relaxation by
-- adding a refusal trigger instead).

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

INSERT INTO schema_migrations (name, sha256) VALUES ('004-text-atoms-cr-guard.sql', 'COMPUTED-AT-APPLY-TIME');

-- End migration 004.
