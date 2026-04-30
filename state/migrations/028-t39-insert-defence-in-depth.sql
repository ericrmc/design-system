-- Migration 028: defence-in-depth INSERT-guard for T-39 close_record requirement.
-- engine-v41 → engine-v41 (no version bump; same review cycle as migration 027).
--
-- Why:
--   S134 review iter-1 finding F167: migration 027 added T-39 on UPDATE OF
--   status, refusing closed transitions without a close_records row. INSERTs
--   into `sessions` with `status='closed'` directly bypass the gate. No
--   handler currently uses that path (`_submit_session_open` always inserts
--   with `status='open'`), so the practical risk is low; but an interactive
--   `sqlite3` direct INSERT or a hypothetical future handler would create a
--   closed session without a close_record, recreating the S133-class gap by a
--   different route.
--
-- Resolution: T-39b mirrors T-39 on the INSERT side. Together they make
--   `sessions.status='closed'` reachable only via a path that has already
--   committed a close_record row (UPDATE) or is being created in a transaction
--   that has one (INSERT — though no such handler exists today).
--
-- T-15 compliance: CREATE TRIGGER only. No DDL on tables, no CHECK relaxation.
--   No engine-version bump (same review cycle as 027).

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TRIGGER t39b_insert_closed_requires_close_record
BEFORE INSERT ON sessions
FOR EACH ROW
WHEN NEW.status = 'closed'
 AND NOT EXISTS (
    SELECT 1 FROM close_records
    WHERE session_id = NEW.session_id
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T39B: cannot INSERT session with status=closed before its close_records row exists');
END;

INSERT INTO schema_migrations (name, sha256) VALUES ('028-t39-insert-defence-in-depth.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
