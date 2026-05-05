-- Migration 054: event-ledger v1 typed primitive (C-4 stakeholder-event F-N row).
-- engine-v58 -> engine-v59 (S204 DV-S204-1 closes OI-S196-4 by-mechanism).
--
-- Why:
--   OI-S196-4 named the C-4 stakeholder-event F-N row primitive in S196's
--   disaster-recovery deliverable-mining triage (DV-S196-1). The OI summary
--   atom: "Substrate-promotion MEDIUM; effects: invalidates-assumption,
--   invalidates-node, opens-risk, blocks-resolution-path; T+Nh timestamp +
--   named source per system-model 33-43." This is the last MEDIUM substrate-
--   promotion candidate from the S196 mining; C-1 (S198 assumption_ledger),
--   C-2 (S197 supersession_ledger), C-3 (S201 closure-shape enum), C-5
--   (S199 prospective-scoping gate), and C-6 (S203 cycle_ledger) shipped
--   in the prior arc.
--
--   Codex shape-consult per FR-S196-16 + FR-S203-11 returned SHIP-WITH-
--   NAMED-EDITS verdict (EF-S204-1) with 5 named edits: 2-table event_ledger
--   + event_effects, alias EV-S<wno>-<seq>, polymorphic target with SQL-
--   trigger coupling, inert at v1 (no auto-cascade), defer SL.origin_event_id
--   to v2; widened DR-only 4-value enum to 6-value with positive
--   counterparts.
--
--   3-perspective deliberation D-S204-1 P-1 schema-minimality + P-2
--   cross-app aggressive + P-3 codex middle-ground sealed with 7
--   convergence + 2 divergence + 3 minority synthesis points + 5
--   counterfactuals dispositioned (2 addressed-in-synthesis, 3 nilled-by-
--   exclusion).
--
--   Synthesis: P-1 + P-2 partial-merge over P-3 codex on D-1 enum cardinality
--   at v1. The load-bearing departure is 2-value enum {invalidates-assumption,
--   confirms-assumption} not codex 6-value: codex 4 additional kinds (node,
--   risk, resolution_path) name target object_kinds NOT REGISTERED in
--   Selvedge today. AR-S203-1 polymorphism-shape-without-substance lesson
--   binds: shipping enum values whose targets cannot resolve is the inverse
--   failure mode (substance-without-shape). v2 widens via T-15-CALIBRATED
--   rebuild when (a) Selvedge ships node/risk/resolution_path primitives or
--   (b) external-app substrates demand them. Codex 6-value preserved as
--   M-2 forward-direction.
--
--   AR-S203-2 synthesis-vs-CHECK coupling lesson: pre-check at migration
--   draft. Constraints named in synthesis encoded at SQL layer:
--     - 2-value enum: SQL CHECK on event_effects.effect_kind.
--     - assumption-only allowlist on target: T-43 trigger.
--     - required event_time + source + claim atoms: NOT NULL on FK columns.
--     - 1:N event-effects: structural (FK NOT NULL on parent).
--     - inert (no auto-cascade): structural (handler emits no side effects).
--   Effects-array-non-empty discipline (P-1 stance) stays handler-only
--   because SQLite cannot enforce parent-with-no-children refusal at
--   parent-INSERT time without deferred CHECKs (which SQLite does not
--   support on row-level CHECK).
--
-- Schema:
--   event_ledger
--     - event_id PK INTEGER AUTOINCREMENT.
--     - session_id FK sessions: origin session.
--     - source_atom_id FK text_atoms NOT NULL: who reported the event
--       (8-480 char support_claim atom).
--     - event_time_atom_id FK text_atoms NOT NULL: when the event
--       occurred (free-text admitting T+Nh, ISO, or domain-specific
--       formats; typed temporal column deferred to v2 if calibration-EF
--       surfaces query-by-time need).
--     - claim_atom_id FK text_atoms NOT NULL: the event's claim
--       (8-480 char support_claim atom).
--     - sealed_at TEXT default now: when the event was sealed in
--       substrate (distinct from event_time which is the observed time).
--     - object_id FK objects NULL: back-pointer to registered event
--       object (alias EV-S<wno>-<seq>); object_kind='event'.
--     - created_at TEXT default now: row-insert timestamp.
--
--   event_effects
--     - effect_id PK INTEGER AUTOINCREMENT.
--     - event_id FK event_ledger NOT NULL: parent event.
--     - ord INTEGER NOT NULL DEFAULT 0: ordering of effects per event.
--     - effect_kind TEXT NOT NULL CHECK closed-2 enum at v1:
--         'invalidates-assumption' — event-claim contradicts a registered
--                                     assumption; target must be assumption-
--                                     kind. Handler does NOT auto-flip
--                                     assumption_ledger.status (inert per
--                                     C-3 + S203 cycle no-auto-SR precedent).
--         'confirms-assumption'   — event-claim corroborates a registered
--                                     assumption; counters DR-bias toward
--                                     negative-only effect kinds per
--                                     AR-S202-1 cross-app generalization.
--     - target_object_id FK objects NOT NULL: polymorphic FK admitting
--       any registered object alias whose object_kind is in the v1 per-
--       effect-kind allowlist. T-43 trigger refuses non-assumption target
--       on insert.
--     - reason_atom_id FK text_atoms NULL: optional 8-480 char rationale
--       atom under support_claim.
--     - UNIQUE (event_id, ord): refuses duplicate-ord effects per event.
--
-- Why two tables (D-S204-1 C-1 universal convergence + codex KNOT-1):
--   Stakeholder events are naturally 1:N: one sourced claim can invalidate
--   an assumption AND confirm another. Single denormalized row would
--   either duplicate source/claim metadata across rows or force weak
--   multi-target encoding. 2-table mirrors decision_v2 + decision_effects
--   precedent.
--
-- Why polymorphic target_object_id via objects-FK + T-43 SQL trigger
-- (D-S204-1 C-2 universal convergence):
--   Mirrors S197 supersession_ledger + S203 cycle_ledger pattern. AR-S203-2
--   synthesis-vs-CHECK lesson: per-effect-kind to target-object-kind
--   coupling enforced at SQL trigger level not handler-only. Handler
--   duplicates with actionable error message naming the allowlist for the
--   rejected effect_kind.
--
-- Why 2-value enum at v1 (D-S204-1 D-1 P-1+P-2 over P-3 codex):
--   Codex EF-S204-1 KNOT-2 named 6-value enum widening with node/risk/
--   resolution_path target kinds. Those object_kinds DO NOT EXIST as
--   registered Selvedge primitives. AR-S203-1 polymorphism-shape-without-
--   substance binds: ship shape, allowlist narrows so semantic-coupling
--   stays bounded. Shipping enum values whose targets cannot resolve is
--   substance-without-shape; v1 ships only kinds whose targets resolve
--   (assumption today). v2 widens cheaply via T-15-CALIBRATED rebuild
--   when external-app substrates land OR Selvedge ships node/risk/
--   resolution_path primitives. P-3 codex 6-value preserved as M-2
--   forward-direction.
--
-- Why object-registration of event_ledger rows (D-S204-1 C-5):
--   Mirrors AR/SL/CYC pattern. The handler allocates an alias
--   EV-S<wno>-<seq> per event row and inserts an objects row with
--   object_kind='event' (drops _ledger suffix per DV-S198-1 P-1 stance
--   precedent). event_effects child rows do NOT register as objects
--   (mirrors decision_supports + decision_effects + cycle_trigger
--   precedent: child rows are sub-records of the parent typed object).
--
-- Why inert at v1 (D-S204-1 C-3 universal + codex named edit #4):
--   invalidates-assumption does NOT auto-set assumption_ledger.status=
--   'invalidated'. Events record sourced external claims and intended
--   effects; agent/operator decides if the AR.status transitions. Mirrors
--   S203 cycle no-auto-SR precedent (cycle row IS proof of observation;
--   non-substantial cycles emit zero SL rows). Codex blind-spot
--   acknowledged: external applications may demand handler-side cascade;
--   M-3 watch-trigger.
--
-- Why defer supersession_ledger.origin_event_id to v2 (D-S204-1 C-4 +
-- codex named edit #5):
--   S197 deferred this forward-FK at C-4 (rejection: "All 3 omit.
--   Migration adds optional FK column when C-4 lands; v1 reason_atom
--   bounds risk."). v1 ships event primitive; v2 wires SL provenance
--   when an immediate producer + invariant exists.
--
-- T-15 compliance:
--   - CHECK relaxation (admitting one new object_kind 'event') is non-
--     destructive: admits strictly more rows than prior CHECK.
--     T-15-CALIBRATED block records the rebuild.
--   - PRAGMA foreign_keys=OFF for the rebuild duration.
--   - Trigger t07a_refs_no_superseded_cite references objects in body
--     and is dropped + recreated around the rebuild (per migration
--     048/049/051/052 precedent).
--   - Trigger t42_cycle_subject_allowlist references objects in body
--     and is dropped + recreated around the rebuild.
--
-- T-43 (new): event_effects per-effect-kind target object_kind coupling.
--   BEFORE INSERT trigger refusing rows where target_object_id resolves
--   to an object whose object_kind is not admitted by the effect_kind's
--   v1 allowlist. At v1 both effect_kind values bind targets to
--   assumption-kind only. Refusal text names the effect_kind, the
--   resolved target object_kind, and the allowed target_kinds.
--
-- role_write_capabilities INSERT inline (S194 lesson per DV-S194-1):
--   ('__cli__','event_ledger','insert')
--   ('__cli__','event_effects','insert')

PRAGMA foreign_keys = OFF;

BEGIN;

-- Drop the triggers whose body references objects (recreated below).
DROP TRIGGER t07a_refs_no_superseded_cite;
DROP TRIGGER t42_cycle_subject_allowlist;

-- T-15-CALIBRATED-BEGIN: widen objects.object_kind CHECK to admit 'event'. Pure superset; no kind removed. Required so EV-S<wno>-<seq> aliases register in objects per D-S204-1 C-5 + codex named edit #1.
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
        'reference_harness','supersession_ledger','assumption','cycle','event'
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

-- Recreate the dropped triggers.
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

CREATE TRIGGER t42_cycle_subject_allowlist
BEFORE INSERT ON cycle_ledger
FOR EACH ROW
WHEN (
    SELECT object_kind
    FROM objects
    WHERE object_id = NEW.subject_object_id
) NOT IN ('assumption')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T42: cycle_ledger subject must be assumption-kind at v1 (allowlist=assumption); v2 extends to issue/decision_v2 once cross-app evidence accumulates per M-2 watch-trigger');
END;

-- ============================================================================
-- event_ledger: typed stakeholder-event header (C-4 F-N primitive).
-- ============================================================================
CREATE TABLE event_ledger (
    event_id            INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id          INTEGER NOT NULL REFERENCES sessions(session_id),
    source_atom_id      INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    event_time_atom_id  INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    claim_atom_id       INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    sealed_at           TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    object_id           INTEGER REFERENCES objects(object_id),
    created_at          TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
) STRICT;

CREATE INDEX idx_event_ledger_session ON event_ledger(session_id);
CREATE INDEX idx_event_ledger_sealed ON event_ledger(sealed_at);

-- ============================================================================
-- event_effects: 1:N child of event_ledger (C-1 + codex KNOT-1).
-- ============================================================================
CREATE TABLE event_effects (
    effect_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    event_id         INTEGER NOT NULL REFERENCES event_ledger(event_id),
    ord              INTEGER NOT NULL DEFAULT 0,
    effect_kind      TEXT NOT NULL CHECK (effect_kind IN (
                         'invalidates-assumption',
                         'confirms-assumption'
                     )),
    target_object_id INTEGER NOT NULL REFERENCES objects(object_id),
    reason_atom_id   INTEGER REFERENCES text_atoms(atom_id),
    created_at       TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    UNIQUE (event_id, ord)
) STRICT;

CREATE INDEX idx_event_effects_event ON event_effects(event_id);
CREATE INDEX idx_event_effects_target ON event_effects(target_object_id);
CREATE INDEX idx_event_effects_kind ON event_effects(effect_kind);

-- T-43: event_effects per-effect-kind target object_kind coupling.
-- Both v1 effect kinds (invalidates-assumption, confirms-assumption) bind
-- target.object_kind='assumption'. Refusal text names the effect_kind, the
-- resolved target object_kind, and the allowed target_kinds for actionable
-- recovery.
CREATE TRIGGER t43_event_effects_target_coupling
BEFORE INSERT ON event_effects
FOR EACH ROW
WHEN NEW.effect_kind IN ('invalidates-assumption','confirms-assumption')
 AND (
    SELECT object_kind
    FROM objects
    WHERE object_id = NEW.target_object_id
 ) != 'assumption'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T43: event_effects.effect_kind in (invalidates-assumption, confirms-assumption) requires target.object_kind=assumption at v1; v2 extends per-effect-kind allowlist when node/risk/resolution-path primitives ship per M-2 watch-trigger');
END;

-- role_write_capabilities INSERT inline (S194 lesson per DV-S194-1).
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','event_ledger','insert'),
    ('__cli__','event_effects','insert');

-- ============================================================================
-- Engine version bump.
-- ============================================================================
UPDATE workspace_metadata
   SET value = 'engine-v59'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('054-event-ledger-v1.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
