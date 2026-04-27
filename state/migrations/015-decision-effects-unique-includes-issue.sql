-- Migration 015: extend decision_effects UNIQUE to include target_issue_id.
-- engine-v28 review-finding remediation (S098 review iteration 1).
--
-- Migration 014 added decision_effects.target_issue_id but did not extend the
-- pre-existing UNIQUE (decision_v2_id, effect_kind, target_object_id,
-- target_descriptor). With the new column meaningful, two closes_issue
-- effects on DIFFERENT issues with the same target_descriptor text would
-- collide on the UNIQUE constraint even though they describe distinct
-- effects. Extending the constraint to include target_issue_id makes the
-- constraint correctly weaker (admits more rows), so no existing row is
-- retroactively invalidated.
--
-- Implementation: SQLite UNIQUE is part of CREATE TABLE; changing it
-- requires the calibrated table-recreation dance per S084 D-1. Only the
-- recreate primitives (CREATE TABLE_new + INSERT + DROP TABLE + RENAME)
-- live inside the calibrated block, because the runner's validator splits
-- the block body on ";" and a CREATE TRIGGER's BEGIN…END; would surface
-- as a bare "END" statement and fail validation. CREATE INDEX and CREATE
-- TRIGGER are not on the T-15 forbidden list and run outside the block.
-- DROP TABLE drops dependent indexes and triggers (t17 / t27 / t28); they
-- are reissued below.

PRAGMA foreign_keys = ON;

BEGIN;

-- T-15-CALIBRATED-BEGIN: extend decision_effects UNIQUE to include target_issue_id; non-destructive (admits strictly more rows than the prior UNIQUE).
CREATE TABLE decision_effects_new (
    effect_id           INTEGER PRIMARY KEY,
    decision_v2_id      INTEGER NOT NULL REFERENCES decisions_v2(decision_v2_id),
    effect_kind         TEXT NOT NULL CHECK (effect_kind IN (
        'creates','modifies','supersedes','opens_issue','bumps_engine','closes_issue','adds_migration'
    )),
    target_object_id    INTEGER REFERENCES objects(object_id),
    target_descriptor   TEXT CHECK (target_descriptor IS NULL OR length(target_descriptor) BETWEEN 2 AND 120),
    object_id           INTEGER REFERENCES objects(object_id),
    target_issue_id     INTEGER REFERENCES issues(issue_id),
    UNIQUE (decision_v2_id, effect_kind, target_object_id, target_issue_id, target_descriptor)
) STRICT;

INSERT INTO decision_effects_new (effect_id, decision_v2_id, effect_kind, target_object_id, target_descriptor, object_id, target_issue_id)
SELECT effect_id, decision_v2_id, effect_kind, target_object_id, target_descriptor, object_id, target_issue_id
FROM decision_effects;

DROP TABLE decision_effects;

ALTER TABLE decision_effects_new RENAME TO decision_effects;
-- T-15-CALIBRATED-END

CREATE INDEX idx_decision_effects_target_issue
    ON decision_effects(target_issue_id)
    WHERE target_issue_id IS NOT NULL;

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

INSERT INTO schema_migrations (name, sha256) VALUES ('015-decision-effects-unique-includes-issue.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
