-- Migration 029: close_state_items required at session-close (trigger T-40).
-- engine-v43 → engine-v44 (session 153, DV-S153-1 closing the close-record
-- empty-items regression that T-39 alone could not catch).
--
-- Why:
--   T-39 (migration 027) refuses session-close when no close_records row
--   exists, but admits a close_records row that has zero close_state_items.
--   S147-S150 closed under this gap: the operator submitted close-record with
--   summary only, omitting (or empty-arraying) the items[] payload, and
--   session-close passed because close_records was non-empty even though
--   close_state_items was empty for that close_record_id. The exported
--   provenance/<wno>/03-close.md collapsed to a 14-line stub (summary only),
--   losing the engine_version/what_was_done/state_at_close/open_issues/
--   next_session_should/validator_summary signal that downstream sessions
--   read at orient time. EF-S151-2 names this exact failure mode and
--   FR-S152-19 names tighten-T-39 as the remedy.
--
-- Resolution per DV-S153-1 (no deliberation; calibration extending T-39 by
--   established pattern):
--
--   T-40 fires BEFORE UPDATE OF status ON sessions when OLD.status='open' and
--   NEW.status='closed' and the session's close_records row has zero
--   close_state_items rows. Trigger-level placement (not handler-only) per
--   the precedent set by T-39: any caller — `_submit_session_close`, a
--   future handler, an interactive `sqlite3` UPDATE — encounters the gate.
--
--   Threshold is fixed at >=1 row. Per-facet coverage (every required facet
--   present at close) is a separate decision deferred to a future session;
--   this migration ships the minimum sufficient to catch the
--   S147-S150-class regression.
--
--   T-39 is left intact (close_records existence remains separately
--   required); T-40 layers on top. Together: a closed session has a
--   close_records row, and that close_records row has at least one
--   close_state_items row. The S147-S150 historical rows are unaffected:
--   T-40 fires BEFORE UPDATE OF status, so existing closed-status rows do
--   not re-trigger. Backfilling synthetic items into S147-S150 was
--   considered and rejected (operator-policy decision; out of scope here,
--   matching the S133 precedent in migration 027).
--
-- Companion change (selvedge/submit/close.py): handler-side pre-check
--   refuses _submit_close_record when items[] is missing or empty,
--   surfacing E_VALIDATION before any INSERT runs. Mirrors the
--   parse-time atom validator pattern from DV-S134-1 (defence in depth
--   per the established T-39 / T-39b shape). Not a SQL change.
--
-- T-15 compliance: CREATE TRIGGER + UPDATE workspace_metadata only. No DDL
--   on tables, no CHECK relaxation, no DROP TABLE / DROP COLUMN /
--   ALTER … DROP. No T-15-CALIBRATED block required.

PRAGMA foreign_keys = ON;

BEGIN;

-- T-40 is scoped to the case where close_records *exists* but
-- close_state_items is empty for that close_record_id. The
-- close_records-missing case is T-39's domain; making T-40 refuse only when
-- T-39 would have admitted keeps the two gates' refusal codes aligned with
-- the failure mode (a caller debugging E_REFUSAL_T40 knows the close_record
-- row is present but items[] was empty, distinct from E_REFUSAL_T39 which
-- says the close_record itself is absent).

CREATE TRIGGER t40_close_requires_state_items
BEFORE UPDATE OF status ON sessions
FOR EACH ROW
WHEN OLD.status = 'open'
 AND NEW.status = 'closed'
 AND EXISTS (
    SELECT 1 FROM close_records WHERE session_id = NEW.session_id
 )
 AND NOT EXISTS (
    SELECT 1
      FROM close_records cr
      JOIN close_state_items csi
        ON csi.close_record_id = cr.close_record_id
     WHERE cr.session_id = NEW.session_id
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T40: session-close requires the close_records row to carry at least one close_state_items entry; resubmit close-record with non-empty items[] before session-close');
END;

UPDATE workspace_metadata
   SET value = 'engine-v44'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('029-close-state-items-required-at-close.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
