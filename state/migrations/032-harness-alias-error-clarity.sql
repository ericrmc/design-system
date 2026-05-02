-- Migration 032: harness alias-format error clarity (engine-v48 unchanged).
--
-- Why:
--   DV-S151-1 D-19 named five ergonomic frictions on the reference_harness
--   substrate kind. Friction #3: t34_reference_harnesses_alias_format
--   raised "must match RH-SNNN-N (3-or-more digit session number)" but
--   gave no concrete example. The S151 deliberation noted the HRN-to-RH
--   learning failure where an operator typed HRN- and was forced to
--   reverse-engineer the correct RH- prefix from the GLOB pattern alone.
--   Naming the format with a concrete example removes that friction at
--   the cheapest possible cost (single trigger recreate, no schema
--   change, no row rewrite, no handler change).
--
--   This migration ships friction #3 alone; friction #2 (atom-length
--   widening for review_findings, decision_supports.claim, and
--   decision_effects.target_descriptor — the 240-char cliffs surfaced
--   recurrently at S172-S176) is deferred to OI-S177-1 as a separate
--   substantive change. Frictions #1 (origin_session_id bind-on-null at
--   harness.py:254-259) and #4 (harness-* dry-run via global submit
--   --dry-run) were already implemented at the original substrate-kind
--   landing (S125, fa2b7871) and are confirmed addressed by inspection
--   in DV-S177-1.
--
-- Schema:
--   t34_reference_harnesses_alias_format    BEFORE INSERT trigger recreate
--     Drop and re-create with a longer error message naming the format
--     plus a concrete example. The GLOB pattern is unchanged.
--
-- Per DV-S151-1 scope-change adoption; closes OI-S151-1 by-mechanism
-- alongside OI-S177-1 deferral of friction #2 atom-length widening.

BEGIN;

DROP TRIGGER IF EXISTS t34_reference_harnesses_alias_format;

CREATE TRIGGER t34_reference_harnesses_alias_format
BEFORE INSERT ON reference_harnesses
FOR EACH ROW
WHEN NOT (NEW.alias GLOB 'RH-S[0-9][0-9][0-9]*-[0-9]*')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T34: reference_harnesses.alias must match RH-SNNN-N (3-or-more digit session number, e.g. RH-S172-1)');
END;

INSERT INTO schema_migrations (name, sha256) VALUES ('032-harness-alias-error-clarity.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
