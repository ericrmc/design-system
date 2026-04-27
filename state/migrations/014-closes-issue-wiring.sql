-- Migration 014: closes_issue effect wiring + typed target_issue_id.
-- engine-v27 → engine-v28 (session 098, EF-S096-3 remedy via DV-S098-1).
--
-- Closes the dispatch gap surfaced by EF-S096-3: decision_effects.effect_kind
-- admitted 'closes_issue' but no trigger or handler flipped issues.status, so
-- the closure narrative inside a decision and the actual issue lifecycle row
-- were coupled by orchestrator discipline only.
--
-- Resolution per DV-S098-1:
--
--   1. Identity is a typed reference. New column `target_issue_id` carries
--      the issue identity for closes_issue effects (and, in future, opens_issue).
--      target_descriptor is repurposed to carry the closure-reason text used
--      to construct the disposition reason atom; it stops carrying identity.
--      This honours P-2's preference for a typed reference over broadening
--      the objects ontology.
--
--   2. Dispatch is in the Python handler (_submit_decision_v2): it resolves
--      the issue alias via _resolve_issue_alias, calls _submit_issue_disposition
--      to flip status, and only then inserts the decision_effects row. The
--      handler keeps T-22 / T-24 / text_atoms validation on the existing path.
--
--   3. Two BEFORE INSERT triggers enforce the invariant for any direct write
--      that bypasses the handler:
--        - t27 refuses closes_issue rows without target_issue_id
--        - t28 refuses closes_issue rows whose target issue is not already
--          resolved/superseded by the same transaction
--      This honours P-1's structural-enforcement preference: handler always
--      satisfies the trigger; the trigger catches everyone else.
--
--   4. T-17 is reissued so target_issue_id satisfies the "target present"
--      requirement on its own (a closes_issue row with target_issue_id but
--      no target_object_id and no target_descriptor still describes a target).
--      DROP TRIGGER is not on the T-15 forbidden list (T-15 forbids DROP TABLE,
--      DROP COLUMN, ALTER … DROP); reissuing a trigger is non-destructive
--      against data.
--
-- T-15 compliance: ALTER TABLE … ADD COLUMN, CREATE INDEX, DROP TRIGGER
-- + CREATE TRIGGER, INSERT into role_write_capabilities (none new this
-- migration; the handler reuses existing __cli__ caps), UPDATE
-- workspace_metadata. No forbidden DROP TABLE / DROP COLUMN / ALTER … DROP.
-- No CHECK relaxation; no calibrated block needed.

PRAGMA foreign_keys = ON;

BEGIN;

ALTER TABLE decision_effects
    ADD COLUMN target_issue_id INTEGER REFERENCES issues(issue_id);

CREATE INDEX idx_decision_effects_target_issue
    ON decision_effects(target_issue_id)
    WHERE target_issue_id IS NOT NULL;

DROP TRIGGER t17_decision_effects_target_present;

CREATE TRIGGER t17_decision_effects_target_present
BEFORE INSERT ON decision_effects
FOR EACH ROW
WHEN NEW.target_object_id IS NULL
 AND NEW.target_descriptor IS NULL
 AND NEW.target_issue_id IS NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T17: decision_effect requires target_object_id, target_issue_id, or target_descriptor');
END;

CREATE TRIGGER t27_closes_issue_requires_target_issue
BEFORE INSERT ON decision_effects
FOR EACH ROW
WHEN NEW.effect_kind = 'closes_issue'
 AND NEW.target_issue_id IS NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T27: closes_issue effect requires target_issue_id (resolved from the issue alias by the handler)');
END;

CREATE TRIGGER t28_closes_issue_target_resolved
BEFORE INSERT ON decision_effects
FOR EACH ROW
WHEN NEW.effect_kind = 'closes_issue'
 AND NEW.target_issue_id IS NOT NULL
 AND NOT EXISTS (
    SELECT 1 FROM issues
    WHERE issue_id = NEW.target_issue_id
      AND status IN ('resolved','superseded')
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T28: closes_issue target issue must already be resolved or superseded in the same transaction');
END;

UPDATE workspace_metadata
   SET value = 'engine-v28'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('014-closes-issue-wiring.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
