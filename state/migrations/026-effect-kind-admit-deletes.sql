-- Migration 026: widen decision_effects.effect_kind CHECK to admit 'deletes'.
-- engine-v37 → engine-v38 (S129 closing OI-S104-2).
--
-- Why:
--   specifications/methodology.md §Coding review loop names the trigger as
--   "produces, modifies, or deletes executable logic". The substrate's
--   decision_effects.effect_kind CHECK admits creates, modifies, supersedes,
--   opens_issue, bumps_engine, closes_issue, adds_migration — but not deletes.
--   A session that deletes executable logic cannot record the effect honestly
--   today. Surfaced as OI-S104-2 (P-2/codex in S104 D-8) and queued in
--   FR-S104-13, FR-S120-8, FR-S121-9, FR-S125-11 as a low-friction calibration.
--
-- Implementation: SQLite CHECK constraints are part of CREATE TABLE; widening
--   the enum requires the calibrated table-recreation dance per S084 D-1,
--   matching the pattern in migration 015. The widening admits strictly more
--   rows than the prior CHECK (every previously-valid row remains valid), so
--   the change is non-destructive. Indexes and triggers are dropped by
--   DROP TABLE and reissued verbatim outside the calibrated block.
--
-- Scope: CHECK widening only. No column adds, no FK changes, no UNIQUE change.
--   Handler code (selvedge/submit/decision_v2.py) does not enumerate effect_kind
--   values; the substrate CHECK is the single point of enforcement, so widening
--   the enum unlocks 'deletes' end-to-end without code changes.

PRAGMA foreign_keys = ON;

BEGIN;

-- T-15-CALIBRATED-BEGIN: widen decision_effects.effect_kind CHECK to admit 'deletes'; non-destructive (admits strictly more rows than the prior CHECK).
CREATE TABLE decision_effects_new (
    effect_id           INTEGER PRIMARY KEY,
    decision_v2_id      INTEGER NOT NULL REFERENCES decisions_v2(decision_v2_id),
    effect_kind         TEXT NOT NULL CHECK (effect_kind IN (
        'creates','modifies','deletes','supersedes','opens_issue','bumps_engine','closes_issue','adds_migration'
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

CREATE TRIGGER t31_opens_issue_requires_target_issue
BEFORE INSERT ON decision_effects
FOR EACH ROW
WHEN NEW.effect_kind = 'opens_issue'
 AND NEW.target_issue_id IS NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T31: opens_issue effect requires target_issue_id (resolved from the issue alias by the handler; create the issue first via `submit issue` if needed)');
END;

UPDATE workspace_metadata
   SET value = 'engine-v38'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('026-effect-kind-admit-deletes.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
