-- Migration 024: reference_harness hardening (T-30 review loop iteration 1).
-- engine-v35 → engine-v36 (S125 review-finding remediation).
--
-- Why:
--   The S125 reviewer surfaced four high and three medium findings against
--   migration 023. This migration addresses the substrate-level findings:
--
--     F1 (high)   assumption_basis sub-table absent from P-4 schema.
--     F2 (high)   T-32 seal-immutability is BEFORE INSERT only; UPDATE and
--                 DELETE after seal are unguarded, allowing rewrites or
--                 destruction of evidence.
--     F3 (high)   Falsification trigger firing does not cascade to set
--                 parent harness.status='reopened' so logical state and DB
--                 state diverge.
--     F5 (medium) reference_harnesses table allows UPDATE of non-status
--                 columns on sealed rows (T-33 only guards status enum).
--     T-34 widening (low) alias GLOB previously admitted only 3 or 4 digit
--                 session numbers; now admits 3+ digits per the migration
--                 023 commentary.
--
--   Three findings are adjudicated rather than fixed in this migration and
--   tracked as follow-up issues in S125 decision-records:
--
--     F4 (high)    Harness alias not in `objects` (cross-citation gap) —
--                  mirrors issues precedent (migration 009 commentary);
--                  promoting harness to T-01 citizenship requires a
--                  calibrated table-rebuild widening objects.object_kind.
--     F6 (medium)  Expiry enforcement on trigger fire — deferred to the
--                  bin/selvedge harness expire CLI work.
--     F7 (medium)  Auto-OI on load-bearing claim breakage — application-
--                  layer concern, deferred to a future session that
--                  surfaces the pattern after pilot use.
--
-- T-15 compliance:
--   Adds new table, indexes, and triggers only. No DROP TABLE, no DROP
--   COLUMN, no ALTER TABLE … DROP, no CHECK widening on existing columns.
--   Updates workspace_metadata.current_engine_version. The pre-existing
--   T-34 trigger is replaced (DROP + CREATE) — admitted under T-15 as a
--   trigger redefinition, since DROP TRIGGER is not in the calibrated-
--   rebuild trap class. Migration 017 uses the same pattern for T-20.

PRAGMA foreign_keys = ON;

BEGIN;

-- ============================================================================
-- 1. reference_harness_assumptions: P-4 assumption_basis sub-table.
-- ============================================================================
--
-- One row per load-bearing assumption the harness depends on. Origin session
-- is captured directly (P-4 explicit requirement). Status is recorded for
-- future reads but is seal-immutable in this migration; assumption
-- invalidation flows through reference_harness_triggers (falsification
-- pathway) per S125 design. If a future session needs status transitions
-- on a sealed harness, that requires a follow-up migration.
CREATE TABLE reference_harness_assumptions (
    assumption_id        INTEGER PRIMARY KEY,
    harness_id           INTEGER NOT NULL REFERENCES reference_harnesses(harness_id),
    ord                  INTEGER NOT NULL,
    assumption_atom_id   INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    origin_session_id    INTEGER NOT NULL REFERENCES sessions(session_id),
    status               TEXT NOT NULL DEFAULT 'active' CHECK (status IN (
                            'active','invalidated','deferred'
                         )),
    UNIQUE (harness_id, ord)
) STRICT;

CREATE INDEX idx_reference_harness_assumptions_harness
    ON reference_harness_assumptions(harness_id, ord);

CREATE TRIGGER t32_reference_harness_assumptions_seal_immutable_ins
BEFORE INSERT ON reference_harness_assumptions
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_assumptions cannot be added after harness seal');
END;

CREATE TRIGGER t32_reference_harness_assumptions_seal_immutable_upd
BEFORE UPDATE ON reference_harness_assumptions
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_assumptions cannot be modified after harness seal');
END;

CREATE TRIGGER t32_reference_harness_assumptions_seal_immutable_del
BEFORE DELETE ON reference_harness_assumptions
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = OLD.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_assumptions cannot be deleted after harness seal');
END;

INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','reference_harness_assumptions','insert');

-- ============================================================================
-- 2. T-32 widening: BEFORE UPDATE and BEFORE DELETE triggers on existing
--    sub-tables (targets, claims, stresses, results, dissent).
-- ============================================================================
--
-- The reference_harness_triggers table is special-cased below — its UPDATE
-- path admits the firing transition on a sealed harness.

-- targets
CREATE TRIGGER t32_reference_harness_targets_seal_immutable_upd
BEFORE UPDATE ON reference_harness_targets
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_targets cannot be modified after harness seal');
END;

CREATE TRIGGER t32_reference_harness_targets_seal_immutable_del
BEFORE DELETE ON reference_harness_targets
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = OLD.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_targets cannot be deleted after harness seal');
END;

-- claims
CREATE TRIGGER t32_reference_harness_claims_seal_immutable_upd
BEFORE UPDATE ON reference_harness_claims
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_claims cannot be modified after harness seal');
END;

CREATE TRIGGER t32_reference_harness_claims_seal_immutable_del
BEFORE DELETE ON reference_harness_claims
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = OLD.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_claims cannot be deleted after harness seal');
END;

-- stresses
CREATE TRIGGER t32_reference_harness_stresses_seal_immutable_upd
BEFORE UPDATE ON reference_harness_stresses
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_stresses cannot be modified after harness seal');
END;

CREATE TRIGGER t32_reference_harness_stresses_seal_immutable_del
BEFORE DELETE ON reference_harness_stresses
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = OLD.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_stresses cannot be deleted after harness seal');
END;

-- results (parent harness via JOIN through claims)
CREATE TRIGGER t32_reference_harness_results_seal_immutable_upd
BEFORE UPDATE ON reference_harness_results
FOR EACH ROW
WHEN (
    SELECT rh.status
      FROM reference_harnesses rh
      JOIN reference_harness_claims rc ON rc.harness_id = rh.harness_id
     WHERE rc.claim_id = NEW.claim_id
) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_results cannot be modified after harness seal');
END;

CREATE TRIGGER t32_reference_harness_results_seal_immutable_del
BEFORE DELETE ON reference_harness_results
FOR EACH ROW
WHEN (
    SELECT rh.status
      FROM reference_harnesses rh
      JOIN reference_harness_claims rc ON rc.harness_id = rh.harness_id
     WHERE rc.claim_id = OLD.claim_id
) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_results cannot be deleted after harness seal');
END;

-- dissent
CREATE TRIGGER t32_reference_harness_dissent_seal_immutable_upd
BEFORE UPDATE ON reference_harness_dissent
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_dissent cannot be modified after harness seal');
END;

CREATE TRIGGER t32_reference_harness_dissent_seal_immutable_del
BEFORE DELETE ON reference_harness_dissent
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = OLD.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_dissent cannot be deleted after harness seal');
END;

-- triggers: UPDATE admits firing transition on sealed harness only.
CREATE TRIGGER t32_reference_harness_triggers_update_guard
BEFORE UPDATE ON reference_harness_triggers
FOR EACH ROW
WHEN NOT (
    -- Admitted: firing transition on a sealed harness — fired_at and
    -- reopened_session_id move NULL → NOT NULL atomically; identity columns
    -- unchanged. Any other UPDATE shape is refused.
    (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) = 'sealed'
    AND OLD.fired_at IS NULL AND NEW.fired_at IS NOT NULL
    AND OLD.reopened_session_id IS NULL AND NEW.reopened_session_id IS NOT NULL
    AND NEW.harness_id = OLD.harness_id
    AND NEW.ord = OLD.ord
    AND NEW.trigger_atom_id = OLD.trigger_atom_id
)
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_triggers UPDATE only admits firing (NULL->NOT NULL on fired_at + reopened_session_id) on a sealed harness');
END;

CREATE TRIGGER t32_reference_harness_triggers_seal_immutable_del
BEFORE DELETE ON reference_harness_triggers
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = OLD.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_triggers cannot be deleted after harness seal');
END;

-- ============================================================================
-- 3. T-36: refuse UPDATE on reference_harnesses non-lifecycle columns after
--    open. Lifecycle columns (status, sealed_at, sealed_session_id,
--    expired_at, reopened_session_id) are admitted; T-33 governs status
--    transitions specifically.
-- ============================================================================
CREATE TRIGGER t36_reference_harnesses_no_mutate_after_open
BEFORE UPDATE ON reference_harnesses
FOR EACH ROW
WHEN OLD.status != 'open'
 AND (
        NEW.alias != OLD.alias
        OR NEW.session_id != OLD.session_id
        OR NEW.arc_slug != OLD.arc_slug
        OR NEW.stage_n != OLD.stage_n
        OR NEW.absence_declaration_atom_id != OLD.absence_declaration_atom_id
        OR NEW.expiry_sessions != OLD.expiry_sessions
        OR NEW.created_at != OLD.created_at
        OR NEW.object_id IS NOT OLD.object_id
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T36: reference_harnesses non-lifecycle columns are immutable after open (lifecycle columns: status, sealed_at, sealed_session_id, expired_at, reopened_session_id)');
END;

-- ============================================================================
-- 4. T-37: AFTER UPDATE on reference_harness_triggers — when a trigger fires
--    (fired_at moves NULL → NOT NULL on a sealed harness), cascade the
--    parent harness status to 'reopened' atomically.
-- ============================================================================
--
-- T-33 admits sealed → reopened, so the cascade UPDATE passes validation.
-- T-36 admits status + reopened_session_id changes (lifecycle columns).
-- SQLite default `recursive_triggers = OFF`: the cascade UPDATE does not
-- re-enter T-37 (which is on a different table anyway).
CREATE TRIGGER t37_reference_harness_trigger_fire_cascade
AFTER UPDATE OF fired_at ON reference_harness_triggers
FOR EACH ROW
WHEN OLD.fired_at IS NULL AND NEW.fired_at IS NOT NULL
BEGIN
    UPDATE reference_harnesses
       SET status = 'reopened',
           reopened_session_id = NEW.reopened_session_id
     WHERE harness_id = NEW.harness_id
       AND status = 'sealed';
END;

-- ============================================================================
-- 5. T-34 widening: admit 3-or-more digit workspace_session_no.
-- ============================================================================
DROP TRIGGER t34_reference_harnesses_alias_format;

CREATE TRIGGER t34_reference_harnesses_alias_format
BEFORE INSERT ON reference_harnesses
FOR EACH ROW
WHEN NOT (NEW.alias GLOB 'RH-S[0-9][0-9][0-9]*-[0-9]*')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T34: reference_harnesses.alias must match RH-SNNN-N (3-or-more digit session number)');
END;

-- ============================================================================
-- 6. Engine version bump.
-- ============================================================================
UPDATE workspace_metadata
   SET value = 'engine-v36'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('024-reference-harness-hardening.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
