-- Migration 027: close-record-required-at-close trigger T-39.
-- engine-v40 → engine-v41 (session 134, DV-S134-1 closing structural-coupling gap from S133 incident).
--
-- Why:
--   S133 closed `status='closed'` without a `close_records` row. Cause:
--   close-record handler refused (atom over 240-char limit on items[2]); the
--   close script ran `submit session-close` next without checking the
--   close-record return code, and session-close succeeded. None of the
--   pre-existing close-time triggers (T-11, T-18, T-19, T-20, T-30) verified
--   close_record presence. constraints.md property 5 names this exact failure
--   mode: detection without a structural feedback loop into prevention does
--   not correct anything.
--
-- Resolution per DV-S134-1 (4-perspective deliberation, deliberation_id=18,
--   cross-family P-2 converged with P-1 and P-4 on SQL-trigger placement):
--
--   T-39 refuses UPDATE OF status ON sessions when OLD.status='open' and
--   NEW.status='closed' if no `close_records` row references the
--   session_id. Trigger-level placement (not handler-level) per the engine's
--   established pattern for cross-row close-time integrity (T-11, T-18,
--   T-19, T-20, T-30): any caller — `_submit_session_close`, a future
--   handler, an interactive `sqlite3` UPDATE — encounters the gate.
--
-- Pre-existing rows: S133 is the only session in workspace history with
--   status='closed' and no close_records row. T-39 fires BEFORE UPDATE OF
--   status, so existing rows are unaffected; the trigger only applies to
--   new close transitions post-engine-v41. The S133 gap remains
--   reconstructable from DV-S133-1 + EF-S131-1 + EF-S132-1 + EF-S133-1 +
--   EF-S134-1 + commit messages — backfilling a synthetic close_record was
--   considered and rejected (operator-policy decision, not in scope here).
--
-- Companion change (selvedge/cli.py): parse-time atom validator mirroring
--   the text_atoms.text CHECK and T-21 CR-guard, raising structured
--   E_ATOM_LENGTH/NEWLINE/CR/FENCED_CODE/PIPE_TABLE codes from `_insert_atom`
--   so callers see structured failures before the SQL CHECK fires. Defence
--   B per DV-S134-1; not a SQL change.
--
-- T-15 compliance: CREATE TRIGGER + UPDATE workspace_metadata only. No DDL
--   on tables, no CHECK relaxation, no DROP TABLE / DROP COLUMN /
--   ALTER … DROP. No T-15-CALIBRATED block required.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TRIGGER t39_close_requires_close_record
BEFORE UPDATE OF status ON sessions
FOR EACH ROW
WHEN OLD.status = 'open'
 AND NEW.status = 'closed'
 AND NOT EXISTS (
    SELECT 1 FROM close_records
    WHERE session_id = NEW.session_id
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T39: session-close requires a close_records row; submit close-record before session-close');
END;

UPDATE workspace_metadata
   SET value = 'engine-v41'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('027-close-record-required-at-close.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
