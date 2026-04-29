-- Migration 025: reference_harness iteration-2 review remediation.
-- engine-v36 → engine-v37 (S125 T-30 review iteration 2).
--
-- Why:
--   Iteration 2 of the S125 review surfaced one CRITICAL and one MEDIUM
--   substrate-level finding plus design-shape findings adjudicated as
--   replay-creates-new-harness (OI-S125-4). This migration addresses:
--
--     RF-2-CRIT (critical) T-36 lifecycle columns (sealed_at, sealed_session_id,
--                          expired_at, reopened_session_id) were unguarded
--                          when the status was unchanged on the same UPDATE.
--                          A direct UPDATE setting sealed_at to a falsified
--                          timestamp on a sealed harness was admitted.
--                          Fix: T-36 admits lifecycle-column writes only
--                          when the status is also transitioning in the
--                          same UPDATE (the legitimate seal/fire/expire
--                          path). Standalone lifecycle-column rewrites
--                          are now refused.
--
--     RF-2-MED  (medium)   reference_harnesses parent row had no
--                          BEFORE DELETE trigger; a sealed/reopened/expired
--                          harness could be deleted wholesale, destroying
--                          evidence and orphaning sub-table rows (or
--                          cascading their deletion under FK rules).
--                          Fix: T-38 refuses DELETE on any harness whose
--                          status is not 'open'. Open harnesses can be
--                          deleted (their creating session may abort
--                          before seal); sealed evidence cannot.
--
--   Adjudicated, not fixed (tracked as OI-S125-4):
--
--     RF-2-HIGH-A  Reopened harness cannot register new triggers — schema
--                  child-table writes are gated on status='open'.
--     RF-2-HIGH-B  Reopened harness cannot fire additional triggers —
--                  T-32 admits trigger fire only on status='sealed'.
--                  Together these enforce the design choice that one
--                  harness corresponds to one stress cycle. Replay = a
--                  new harness with a forward link to the reopened one.
--                  This is consistent with substrate immutability after
--                  seal. If the disaster-response pilot demonstrates
--                  multi-event replay-on-same-harness is genuinely needed,
--                  reopen OI-S125-4.
--
-- T-15 compliance: this migration adds a trigger and replaces a trigger
-- (DROP + CREATE), no DROP TABLE, no DROP COLUMN, no ALTER TABLE … DROP,
-- no CHECK widening. Mirrors migration 017's T-20 redefinition pattern.

PRAGMA foreign_keys = ON;

BEGIN;

-- ============================================================================
-- 1. Strengthen T-36: lifecycle-column writes admitted only on status-changing
--    UPDATEs.
-- ============================================================================
DROP TRIGGER t36_reference_harnesses_no_mutate_after_open;

CREATE TRIGGER t36_reference_harnesses_no_mutate_after_open
BEFORE UPDATE ON reference_harnesses
FOR EACH ROW
WHEN OLD.status != 'open'
 AND (
        -- Always-immutable identity columns: change refused after open.
        NEW.alias != OLD.alias
        OR NEW.session_id != OLD.session_id
        OR NEW.arc_slug != OLD.arc_slug
        OR NEW.stage_n != OLD.stage_n
        OR NEW.absence_declaration_atom_id != OLD.absence_declaration_atom_id
        OR NEW.expiry_sessions != OLD.expiry_sessions
        OR NEW.created_at != OLD.created_at
        OR NEW.object_id IS NOT OLD.object_id
        -- Lifecycle columns: admitted only on a status-changing UPDATE.
        -- A standalone UPDATE that rewrites sealed_at/sealed_session_id/
        -- expired_at/reopened_session_id without changing the status is
        -- timeline falsification and refused.
        OR (NEW.status = OLD.status AND (
                NEW.sealed_at IS NOT OLD.sealed_at
                OR NEW.sealed_session_id IS NOT OLD.sealed_session_id
                OR NEW.expired_at IS NOT OLD.expired_at
                OR NEW.reopened_session_id IS NOT OLD.reopened_session_id
           ))
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T36: reference_harnesses non-lifecycle columns are immutable after open; lifecycle columns (sealed_at, sealed_session_id, expired_at, reopened_session_id) admit changes only on a status-transitioning UPDATE');
END;

-- ============================================================================
-- 2. T-38: refuse DELETE on any harness past the open phase.
-- ============================================================================
CREATE TRIGGER t38_reference_harnesses_no_delete_after_open
BEFORE DELETE ON reference_harnesses
FOR EACH ROW
WHEN OLD.status != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T38: reference_harnesses cannot be deleted after open (sealed, expired, and reopened harnesses are permanent evidence)');
END;

-- ============================================================================
-- 3. Engine version bump.
-- ============================================================================
UPDATE workspace_metadata
   SET value = 'engine-v37'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('025-reference-harness-iter2-fixes.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
