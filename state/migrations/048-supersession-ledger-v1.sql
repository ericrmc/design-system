-- Migration 048: supersession-ledger v1 typed cross-artefact primitive.
-- engine-v52 -> engine-v53 (S197 DV-S197-1 closes OI-S196-2 by-mechanism).
--
-- Why:
--   OI-S196-2 named typed-supersession-ledger as the biggest schema gap
--   surfaced by the disaster-recovery 21-session arc (operator-curated
--   after-action retrospective §6). Existing channels are narrow:
--     - decision_effects.effect_kind='supersedes' has 1 historical row
--       across 196 sessions (the SPEC-prompt-development v1->v2 supersession).
--     - refs.relation='supersedes' carries spec-version supersession only.
--   No cross-artefact typed primitive exists for supersession events that
--   span decisions / specs / issues / EFs / OIs. The deliberation D-S197-1
--   (3-perspective: P-1 schema-minimality + P-2 backcompat-and-objects-graph
--   + P-3 adversarial-failure-modes) plus codex EF-S197-1 shape-consult
--   converged on objects-FK polymorphism + 5-value enum + soft-deprecation
--   of decision_effects.supersedes.
--
--   EF-S196-2 bounded-scope binding precluded watch-FR deferral; bias-
--   toward-build-now per the 21-session arc evidence + retrospective.
--
-- Schema:
--   supersession_ledger
--     - source_object_id FK objects: the superseding entity (the new).
--     - target_object_id FK objects: the superseded entity (the old).
--     - relation_kind TEXT CHECK closed enum (5 values per P-1 stance):
--         'supersedes-fully'    — the new fully replaces the old; the
--                                 old's authority is fully migrated.
--         'supersedes-partial'  — the new replaces some scope of the old;
--                                 the old retains other scope.
--         'bounded-by'          — the new bounds the old's interpretation
--                                 (e.g. EF-S196-2 bounds DV-S190-2 graduation-
--                                 discipline scope; the old still applies
--                                 in its now-bounded shape).
--         'replaces-mechanism'  — the new replaces a specific mechanism of
--                                 the old while preserving the old's
--                                 broader frame.
--         'retracted-by'        — the old is withdrawn entirely; the new
--                                 is the retraction record (no replacement
--                                 substantive content).
--     - sealed_at_session_id FK sessions: when the supersession was sealed.
--     - reason_atom_id FK text_atoms: 8-240 char reason atom under
--       atom_type='support_claim' (closest existing atom_type).
--     - cite_object_id FK objects NULL: optional citation to the
--       authoring decision_v2 (or other authority) emitting the supersession.
--     - object_id FK objects NULL: back-pointer to the registered
--       supersession_ledger object (alias SL-S<wno>-<seq>).
--     - sealed_at TEXT default now.
--     - UNIQUE (source_object_id, target_object_id, relation_kind):
--       refuses duplicate supersession edges per the same triple.
--     - CHECK (source_object_id != target_object_id): refuses self-
--       supersession at insert (C-5 convergence).
--
-- Why objects-FK polymorphism (not source_kind/target_kind enum):
--   The objects table's object_kind enum already discriminates 30 typed
--   row classes; reaching all of them via a single FK avoids parallel
--   discriminator drift (P-1 + P-3 schema-correctness threshold). This
--   composes natively with chain_walks T-32 over objects.alias.
--
-- Why object-registration of supersession_ledger rows:
--   P-2 named that ledger rows must register as first-class objects to
--   participate in chain-walks T-32 graph. The handler allocates an
--   alias SL-S<wno>-<seq> per ledger row and inserts an objects row
--   with object_kind='supersession_ledger'. P-3 minority preserved that
--   eager registration is ceremony-before-evidence; M-1 watch-trigger
--   names dead-channel risk if N>=5 sessions zero inserts.
--
-- Why omit C-4 origin column at v1:
--   Codex EF-S197-1 verdict and all 3 perspectives converged on omitting
--   a forward-FK to a not-yet-existing external_events table. C-4 will
--   add origin_event_id when the stakeholder-event primitive lands; v1
--   reason_atom + cite_object_id bound the unmodeled-event risk.
--
-- Why soft-deprecate decision_effects.supersedes (not hard-cutover):
--   D-3 divergence: P-1 keep readable, P-2 compat projection, P-3 hard-
--   cutover. Synthesis adopted P-1+P-2 soft-deprecation: keep CHECK
--   admissible for historical replay; route NEW writes through ledger
--   via handler discipline (selvedge/submit/decision.py routes new
--   supersedes effects through ledger when source/target resolvable).
--   M-1 P-3 watch-trigger preserved: if dual-channel persists, future
--   session ships hard-cutover migration.
--
-- Backfill of legacy decision_effects.supersedes row:
--   The 1 legacy row (effect_id=26, decision_v2_id=5 DV-S186-1) records
--   the SPEC-prompt-development-v1 -> v2 supersession. Migrated as one
--   typed supersession_ledger row:
--     source_object_id=725 (SPEC-prompt-development-v2 — the new)
--     target_object_id=516 (SPEC-prompt-development-v1 — the old)
--     relation_kind='supersedes-fully'
--     sealed_at_session_id=7 (S186 session_id)
--     reason_atom: pinned via INSERT INTO text_atoms below
--     cite_object_id=727 (DV-S186-1 — the authoring decision)
--   Per DV-S189-1 markdown-only-recovery binding, this is a typed-row
--   migration of an existing typed row, not a synthetic-row reconstruction.
--   The legacy decision_effects.supersedes row is preserved (soft-
--   deprecation); reading code may consult both channels until cutover.
--
-- T-15 compliance:
--   - CHECK relaxation (admitting one new object_kind value
--     'supersession_ledger') is non-destructive: admits strictly more
--     rows than prior CHECK. T-15-CALIBRATED block records the rebuild.
--   - PRAGMA foreign_keys=OFF for the duration of the rebuild.
--   - Trigger t07a_refs_no_superseded_cite references objects in its body
--     and is dropped + recreated around the rebuild.
--
-- role_write_capabilities INSERT inline (S194 lesson per DV-S194-1
-- close-record: 045 created table without capability INSERT, blocking
-- handler INSERT until 046 split-out backfilled it; future migrations
-- ship table + capability together).

PRAGMA foreign_keys = OFF;

BEGIN;

-- Drop the trigger whose body references objects (recreated below).
DROP TRIGGER t07a_refs_no_superseded_cite;

-- T-15-CALIBRATED-BEGIN: widen objects.object_kind CHECK to admit supersession_ledger. Pure superset; no kind removed. Required so SL-S<wno>-<seq> aliases register in objects per DV-S197-1 D-2 + P-2.
CREATE TABLE objects_new (
    object_id      INTEGER PRIMARY KEY,
    object_kind    TEXT NOT NULL CHECK (object_kind IN (
        'decision','spec_version','perspective','deliberation',
        'commitment','engine_feedback','session','synthesis_point',
        'work_item','subtraction','agent_run',
        'assessment','decision_v2','alternative_v2','spec_section',
        'spec_clause','perspective_position','perspective_claim',
        'review_finding','text_atom','legacy_import','spec_clause_link',
        'decision_support','decision_effect','alternative_rejection',
        'close_record','close_state_item','assessment_agenda_item',
        'reference_harness','supersession_ledger'
    )),
    typed_row_id   INTEGER NOT NULL,
    alias          TEXT UNIQUE,
    created_at     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
) STRICT;
INSERT INTO objects_new (object_id, object_kind, typed_row_id, alias, created_at)
    SELECT object_id, object_kind, typed_row_id, alias, created_at FROM objects;
DROP TABLE objects;
ALTER TABLE objects_new RENAME TO objects;
CREATE INDEX idx_objects_kind_typed_row ON objects (object_kind, typed_row_id);
-- T-15-CALIBRATED-END

-- Recreate the dropped trigger.
CREATE TRIGGER t07a_refs_no_superseded_cite
BEFORE INSERT ON refs
FOR EACH ROW
WHEN NEW.relation = 'cites'
 AND NEW.allow_superseded = 0
 AND EXISTS (
    SELECT 1
    FROM objects o JOIN spec_versions sv ON sv.object_id = o.object_id
    WHERE o.object_id = NEW.target_object_id AND sv.status = 'superseded'
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T07: cite targets a superseded spec_version (set allow_superseded=1 with reason)');
END;

-- ============================================================================
-- supersession_ledger: typed cross-artefact supersession events.
-- ============================================================================
CREATE TABLE supersession_ledger (
    ledger_id              INTEGER PRIMARY KEY,
    source_object_id       INTEGER NOT NULL REFERENCES objects(object_id),
    target_object_id       INTEGER NOT NULL REFERENCES objects(object_id),
    relation_kind          TEXT NOT NULL CHECK (relation_kind IN (
                              'supersedes-fully',
                              'supersedes-partial',
                              'bounded-by',
                              'replaces-mechanism',
                              'retracted-by'
                           )),
    sealed_at_session_id   INTEGER NOT NULL REFERENCES sessions(session_id),
    reason_atom_id         INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    cite_object_id         INTEGER REFERENCES objects(object_id),
    sealed_at              TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    object_id              INTEGER REFERENCES objects(object_id),
    UNIQUE (source_object_id, target_object_id, relation_kind),
    CHECK (source_object_id != target_object_id)
) STRICT;

CREATE INDEX idx_sl_source ON supersession_ledger(source_object_id);
CREATE INDEX idx_sl_target ON supersession_ledger(target_object_id);
CREATE INDEX idx_sl_session ON supersession_ledger(sealed_at_session_id);
CREATE INDEX idx_sl_relation ON supersession_ledger(relation_kind);

-- role_write_capabilities INSERT inline (S194 split-out lesson).
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','supersession_ledger','insert'),
    ('__cli__','supersession_ledger','update');

-- ============================================================================
-- Backfill: migrate the 1 legacy decision_effects.supersedes row
-- (effect_id=26, DV-S186-1, SPEC-prompt-development v1 -> v2) when present.
--
-- Conditional via INSERT...SELECT...WHERE EXISTS: on a fresh init applying
-- migrations 001-048 with no spec_versions/decisions_v2 seeded yet, the
-- WHERE clause filters to zero rows and the backfill is a no-op. On the
-- production substrate carrying the historical row, the backfill lands.
-- This pattern preserves migration determinism without requiring a
-- separate "production-only" migration.
-- ============================================================================
INSERT INTO text_atoms (atom_type, text, created_session_id)
    SELECT 'support_claim',
           'Migrated from decision_effects.effect_kind=supersedes effect_id=26 (DV-S186-1 SPEC-prompt-development v1 to v2 L2b subagent tempdir-clone) at S197 supersession-ledger v1 ship per DV-S197-1.',
           18
    WHERE EXISTS (SELECT 1 FROM objects WHERE alias='SPEC-prompt-development-v2')
      AND EXISTS (SELECT 1 FROM objects WHERE alias='SPEC-prompt-development-v1')
      AND EXISTS (SELECT 1 FROM objects WHERE alias='DV-S186-1')
      AND EXISTS (SELECT 1 FROM sessions WHERE session_id=18);

INSERT INTO supersession_ledger (
    source_object_id, target_object_id, relation_kind,
    sealed_at_session_id, reason_atom_id, cite_object_id, sealed_at
)
    SELECT
        (SELECT object_id FROM objects WHERE alias='SPEC-prompt-development-v2'),
        (SELECT object_id FROM objects WHERE alias='SPEC-prompt-development-v1'),
        'supersedes-fully',
        (SELECT session_id FROM sessions WHERE workspace_session_no=186),
        (SELECT MAX(atom_id) FROM text_atoms WHERE atom_type='support_claim' AND text LIKE 'Migrated from decision_effects.effect_kind=supersedes effect_id=26%'),
        (SELECT object_id FROM objects WHERE alias='DV-S186-1'),
        '2026-04-30T00:00:00.000Z'
    WHERE EXISTS (SELECT 1 FROM objects WHERE alias='SPEC-prompt-development-v2')
      AND EXISTS (SELECT 1 FROM objects WHERE alias='SPEC-prompt-development-v1')
      AND EXISTS (SELECT 1 FROM objects WHERE alias='DV-S186-1')
      AND EXISTS (SELECT 1 FROM sessions WHERE workspace_session_no=186);

-- Register the legacy row as object SL-S186-1 when the backfill landed.
INSERT INTO objects (object_kind, typed_row_id, alias)
    SELECT 'supersession_ledger', ledger_id, 'SL-S186-1'
    FROM supersession_ledger sl
    WHERE sl.source_object_id = (SELECT object_id FROM objects WHERE alias='SPEC-prompt-development-v2')
      AND sl.target_object_id = (SELECT object_id FROM objects WHERE alias='SPEC-prompt-development-v1')
      AND sl.relation_kind='supersedes-fully';

-- Update back-pointer.
UPDATE supersession_ledger
   SET object_id = (SELECT object_id FROM objects WHERE alias='SL-S186-1')
 WHERE source_object_id = (SELECT object_id FROM objects WHERE alias='SPEC-prompt-development-v2')
   AND target_object_id = (SELECT object_id FROM objects WHERE alias='SPEC-prompt-development-v1')
   AND relation_kind='supersedes-fully';

-- ============================================================================
-- Engine version bump.
-- ============================================================================
UPDATE workspace_metadata
   SET value = 'engine-v53'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('048-supersession-ledger-v1.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
