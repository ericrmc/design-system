-- Migration 022: opens_issue effect target_issue_id enforcement.
-- engine-v33 → engine-v34 (session 118, EF-S117-1 remedy via DV-S118-1).
--
-- Closes the asymmetry surfaced by EF-S117-1: cross-session anchor-trace
-- (DV-S116-1, S117) had to fall back to a word-boundary regex over
-- decision_effects.target_descriptor for `opens_issue` effects because 8/14
-- such rows carried NULL target_issue_id. The closes_issue side has been
-- typed and trigger-enforced since engine-v28 (T-27, T-28 / DV-S098-1);
-- opens_issue was the remaining case.
--
-- Resolution per DV-S118-1:
--
--   1. T-31 refuses any opens_issue effect with NULL target_issue_id.
--      Mirrors T-27 (closes_issue): structural enforcement at the substrate
--      layer means any write-path that bypasses the handler still fails.
--
--   2. Dispatch is in the Python handler (_submit_decision_record): the
--      opens_issue branch resolves `target` (issue alias) via
--      _resolve_issue_alias, sets target_issue_id, leaves target_descriptor
--      optional (existing semantics). Issue creation itself remains a
--      separate `bin/selvedge submit issue` call upstream of the
--      decision-record — unlike closes_issue, which folds the disposition
--      transition in-band, opens_issue's `target` must already exist.
--      Rationale: issue creation requires title + priority + (optional)
--      summary/body; folding all four into decision_effects payload bloats
--      the schema for marginal ergonomic gain (R-1.1 rejection on
--      DV-S118-1).
--
-- Pre-existing rows: 8 opens_issue effects in this workspace carry NULL
-- target_issue_id and name future intent the operator never registered as
-- an issue (work_item placeholders, prose descriptors, alias forms that
-- later became different concrete aliases). T-31 fires BEFORE INSERT only,
-- so existing rows are unaffected; the trigger only applies to new writes
-- post-engine-v34. Operators encountering this refusal should either
-- create the issue first via `submit issue`, or use a different
-- effect_kind (creates/modifies) when no issue identity is being tracked.
--
-- Known limitation: chain-walk export (_decisions_citing_issue, cli.py
-- ~L2830) retains its target_descriptor LIKE word-boundary regex fallback
-- to traverse those 8 legacy NULL rows. Going forward only new opens_issue
-- writes will be FK-typed; the legacy substring path remains live until
-- those rows are either backfilled (mirroring migration 021) or aged out
-- by a future calibrated rebuild. Deleting an issue whose alias is named
-- only in a legacy descriptor would silently orphan that anchor-trace
-- edge.
--
-- T-15 compliance: CREATE TRIGGER + UPDATE workspace_metadata only. No
-- DDL on tables, no CHECK relaxation, no DROP TABLE / DROP COLUMN /
-- ALTER … DROP. No T-15-CALIBRATED block required.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TRIGGER t31_opens_issue_requires_target_issue
BEFORE INSERT ON decision_effects
FOR EACH ROW
WHEN NEW.effect_kind = 'opens_issue'
 AND NEW.target_issue_id IS NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T31: opens_issue effect requires target_issue_id (resolved from the issue alias by the handler; create the issue first via `submit issue` if needed)');
END;

UPDATE workspace_metadata
   SET value = 'engine-v34'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('022-opens-issue-target-issue-id-enforcement.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
