-- Migration 021: backfill decision_effects.target_object_id / target_issue_id
-- and decision_supports.cited_object_id where the original write omitted the
-- alias but the descriptor / claim text contains a literal canonical alias.
--
-- Engine-v33 (session 113). Implements DV-S113-1; closes OI-S110-3.
--
-- Why:
--   Effects and supports written before the engine-v28 closes_issue dispatch and
--   before operators routinely supplied the optional `target` / `cite` fields
--   left target_object_id / target_issue_id / cited_object_id NULL even when the
--   descriptor or claim already named a citable alias literally. EF-S110-7
--   wants to traverse decision -> referent edges; orient's recent-supersessions
--   surface (S110-1) already drops 5 effect rows because target_object_id is
--   NULL. The fix is mechanical: parse the alias out of the descriptor / claim,
--   resolve via objects.alias or issues.alias, set the FK.
--
-- Scope (resolved offline by tools/build-decision-target-backfill.py against
-- this workspace; matches are exact-prefix or exact-substring with one alias of
-- the kind matching the basis):
--
--   decision_effects (17 rows)
--     opens_issue   x6: descriptor starts with OI-XXX -> target_issue_id
--     closes_issue  x7: descriptor starts with OI-XXX -> target_issue_id
--                       (these pre-date T-27 / migration 014; the trigger only
--                        fires BEFORE INSERT so this UPDATE is admitted)
--     supersedes    x4: 2 engine-manifest version transitions, 1 DV-S104-3,
--                       1 constraints v1 -> SPEC-constraints-v1
--
--   decision_supports (1 row)
--     engine_feedback x1: claim names EF-S092-3 uniquely.
--
-- Selectors:
--   Each UPDATE keys on (decision_alias, descriptor, effect_kind) for effects
--   and (decision_alias, seq, basis) for supports. Both are stable identities;
--   numeric ids are intentionally avoided so derived workspaces resolve the
--   same rows even when rowids differ. Each UPDATE includes the IS NULL guard
--   so re-application is a no-op.
--
-- Triggers:
--   t17, t27, t28 on decision_effects are all BEFORE INSERT and do not fire on
--   UPDATE. No DROP TRIGGER / RECREATE pattern is required.
--
-- T-15 compliance: pure UPDATE statements, no schema change, no CHECK
-- relaxation, no DDL. No T-15-CALIBRATED block required.
--
-- Out of scope (tracked as residual under OI-S110-3 disposition):
--   * 92 effect rows whose descriptors are file paths, prose, or non-canonical
--     references ("engine-vN to engine-vN+1", migration filenames, "S047
--     arc-plan five-session v1", "Rebuild tools/...") and do not encode a
--     resolvable alias.
--   * 81 support rows whose claims either name no alias, name aliases of a
--     kind that does not match the basis (issues are not objects, so issue
--     references in support claims cannot populate cited_object_id), or name
--     more than one alias of the matching kind (ambiguous; one cited_object_id
--     slot).
--   These will be addressed organically as new write-paths supply the FK at
--   write time; the residual set is bounded and decreasing.

PRAGMA foreign_keys = ON;

BEGIN;

-- ===== decision_effects =====

-- effect: opens_issue OI-086-001 (DV-S086-1)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-086-001')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S086-1')
    AND target_descriptor = 'OI-086-001 spec_clause source_decision_v2_id NOT NULL'
    AND effect_kind = 'opens_issue'
    AND target_issue_id IS NULL;

-- effect: opens_issue OI-086-002 (DV-S086-1)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-086-002')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S086-1')
    AND target_descriptor = 'OI-086-002 single-active spec_version per spec_id'
    AND effect_kind = 'opens_issue'
    AND target_issue_id IS NULL;

-- effect: opens_issue OI-086-003 (DV-S086-1)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-086-003')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S086-1')
    AND target_descriptor = 'OI-086-003 cited_object_id NOT NULL on cite-required bases'
    AND effect_kind = 'opens_issue'
    AND target_issue_id IS NULL;

-- effect: opens_issue OI-086-004 (DV-S086-1)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-086-004')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S086-1')
    AND target_descriptor = 'OI-086-004 legacy_imports decomposition_status semantics'
    AND effect_kind = 'opens_issue'
    AND target_issue_id IS NULL;

-- effect: closes_issue OI-085-001 (DV-S087-1)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-085-001')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S087-1')
    AND target_descriptor = 'OI-085-001 redecomposition + flag-flip complete'
    AND effect_kind = 'closes_issue'
    AND target_issue_id IS NULL;

-- effect: closes_issue OI-085-002 (DV-S090-1)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-085-002')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S090-1')
    AND target_descriptor = 'OI-085-002'
    AND effect_kind = 'closes_issue'
    AND target_issue_id IS NULL;

-- effect: supersedes engine-manifest v23 -> v24 (DV-S090-1) targets v23 row
UPDATE decision_effects SET target_object_id = (SELECT object_id FROM objects WHERE alias='SPEC-engine-manifest-v23')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S090-1')
    AND target_descriptor = 'engine-manifest v23 to v24'
    AND effect_kind = 'supersedes'
    AND target_object_id IS NULL;

-- effect: closes_issue OI-086-002 (DV-S091-1)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-086-002')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S091-1')
    AND target_descriptor = 'OI-086-002'
    AND effect_kind = 'closes_issue'
    AND target_issue_id IS NULL;

-- effect: supersedes engine-manifest v24 -> v25 (DV-S091-1) targets v24 row
UPDATE decision_effects SET target_object_id = (SELECT object_id FROM objects WHERE alias='SPEC-engine-manifest-v24')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S091-1')
    AND target_descriptor = 'engine-manifest v24 to v25'
    AND effect_kind = 'supersedes'
    AND target_object_id IS NULL;

-- effect: closes_issue OI-S089-2 (DV-S092-2)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-S089-2')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S092-2')
    AND target_descriptor = 'OI-S089-2'
    AND effect_kind = 'closes_issue'
    AND target_issue_id IS NULL;

-- effect: closes_issue OI-S089-1 (DV-S092-3)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-S089-1')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S092-3')
    AND target_descriptor = 'OI-S089-1'
    AND effect_kind = 'closes_issue'
    AND target_issue_id IS NULL;

-- effect: closes_issue OI-S089-3 (DV-S092-4)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-S089-3')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S092-4')
    AND target_descriptor = 'OI-S089-3'
    AND effect_kind = 'closes_issue'
    AND target_issue_id IS NULL;

-- effect: closes_issue OI-S090-3 (DV-S092-5)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-S090-3')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S092-5')
    AND target_descriptor = 'OI-S090-3'
    AND effect_kind = 'closes_issue'
    AND target_issue_id IS NULL;

-- effect: supersedes DV-S104-3 (DV-S104-7) targets the deferred decision row
UPDATE decision_effects SET target_object_id = (SELECT object_id FROM objects WHERE alias='DV-S104-3')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S104-7')
    AND target_descriptor = 'DV-S104-3 halted-as-status admission deferred.'
    AND effect_kind = 'supersedes'
    AND target_object_id IS NULL;

-- effect: opens_issue OI-S104-3 (DV-S104-7)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-S104-3')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S104-7')
    AND target_descriptor = 'OI-S104-3 to track halted-as-status-value rebuild when warranted.'
    AND effect_kind = 'opens_issue'
    AND target_issue_id IS NULL;

-- effect: opens_issue OI-S105-1 (DV-S105-1)
UPDATE decision_effects SET target_issue_id = (SELECT issue_id FROM issues WHERE alias='OI-S105-1')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S105-1')
    AND target_descriptor = 'OI-S105-1 methodology kernel third-sense reconciliation'
    AND effect_kind = 'opens_issue'
    AND target_issue_id IS NULL;

-- effect: supersedes constraints v1 (DV-S109-1)
UPDATE decision_effects SET target_object_id = (SELECT object_id FROM objects WHERE alias='SPEC-constraints-v1')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S109-1')
    AND target_descriptor = 'constraints spec-version row status set to superseded'
    AND effect_kind = 'supersedes'
    AND target_object_id IS NULL;

-- ===== decision_supports =====

-- support: engine_feedback EF-S092-3 (DV-S093-1, seq=1)
UPDATE decision_supports SET cited_object_id = (SELECT object_id FROM objects WHERE alias='EF-S092-3')
  WHERE decision_v2_id = (SELECT typed_row_id FROM objects WHERE object_kind='decision_v2' AND alias='DV-S093-1')
    AND seq = 1
    AND basis = 'engine_feedback'
    AND cited_object_id IS NULL;

INSERT INTO schema_migrations (name, sha256) VALUES ('021-backfill-decision-targets-supports.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
