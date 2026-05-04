-- Migration 049: assumption-ledger v1 typed primitive (the workspace-scope
-- assumption_register §8.5 audit-step has been referencing as A-NNN since
-- DV-S155-1; the substrate primitive ships at S198 closing OI-S196-1).
--
-- engine-v53 -> engine-v54 (S198 DV-S198-1 closes OI-S196-1 by-mechanism).
--
-- Why:
--   OI-S196-1 was named the C-1 typed-assumption-ledger primitive in S196's
--   disaster-recovery deliverable-mining triage (DV-S196-1). FR-S197-13 named
--   it next per codex C-2-then-C-1 sequencing (S197 shipped C-2 = supersession-
--   ledger; S198 ships C-1 = assumption-ledger).
--
--   §8.5 close-time audit-step (DV-S155-1) instructs agents to "lift each
--   into the assumption_register (A-NNN)" but no substrate primitive existed.
--   Engine-self use case is the immediate consumer; disaster-recovery arc
--   (DV-S008-1 four-field discipline + 3-value sub_type set) is the evidence.
--
--   Deliberation D-6 (3-perspective: P-1 schema-minimality + P-2 engine-self-
--   consumer-readiness + P-3 codex shape-consult) sealed at S198. Synthesis:
--
--     - Adopt P-1 6-status closed enum (rejects P-2/P-3 9-value over-breadth):
--       {unverified, assumed, active-with-conflict, closed, superseded,
--       invalidated}. monitored/unknown/worst-case-assumed are commentary-
--       shaped, not state-machine-shaped (P-1).
--     - Adopt P-1 3-sub-type closed enum (rejects P-2 use-case-discriminator
--       framing as M-2 minority): {plan-vs-resource, contested-authority,
--       rolling-renewal} from disaster-recovery arc evidence (DV-S008-1).
--     - sub_type NOT NULL when status=active-with-conflict (CHECK); NULL
--       otherwise (CHECK).
--     - Four-field CHECK on action_commitment_atom_id, both_source_citation_-
--       atom_id, resolution_path_atom_id, expiry_trigger_atom_id all NOT NULL
--       when status=active-with-conflict.
--     - Mutable status field via assumption-status-update submit kind (P-1).
--     - REJECT P-3 dedicated assumption_status_changes history table (P-1+P-2
--       convergence): replay walks decisions_v2 + decision_supports + effects
--       against the assumption's object_id; a second channel courts the dual-
--       channel watch-trigger S197 just paid for.
--     - Object-registration: alias AR-S<wno>-<seq>; object_kind='assumption'
--       (P-1 drops the _ledger suffix that was post-hoc in S197's
--       supersession_ledger naming).
--     - Atom length 8-480 (support_claim tier per OI-S177-1 widening). All 3
--       perspectives converged.
--     - Status transitions require citing_decision_object_id FK (P-1) so the
--       transition is traceable via decisions_v2 walk; this IS the audit
--       trail without a history table.
--     - Bias-toward-build-now per EF-S196-2: ship v1 in S198 closing the
--       §8.5 referential gap.
--
-- Schema:
--   assumption_ledger
--     - assumption_id PK INTEGER AUTOINCREMENT.
--     - session_id FK sessions: origin session.
--     - statement_atom_id FK text_atoms NOT NULL: the 8-480 char assumption
--       statement under atom_type='support_claim'.
--     - status TEXT NOT NULL CHECK closed-6 enum DEFAULT 'unverified'.
--     - sub_type TEXT NULL CHECK closed-3 enum (NOT NULL when status=
--       active-with-conflict via second CHECK).
--     - action_commitment_atom_id FK text_atoms NULL.
--     - both_source_citation_atom_id FK text_atoms NULL.
--     - resolution_path_atom_id FK text_atoms NULL.
--     - expiry_trigger_atom_id FK text_atoms NULL.
--     - basis_atom_id FK text_atoms NULL: optional basis citation atom.
--     - origin_decision_object_id FK objects NULL: the DV that registered/
--       lifted this assumption (cite at insert when known).
--     - last_transition_decision_object_id FK objects NULL: the DV that
--       most recently transitioned status (set by assumption-status-update
--       handler).
--     - object_id FK objects NULL: back-pointer to the registered
--       assumption object (alias AR-S<wno>-<seq>).
--     - created_at TEXT default now.
--     - CHECK (status != 'active-with-conflict' OR (
--         sub_type IS NOT NULL
--         AND action_commitment_atom_id IS NOT NULL
--         AND both_source_citation_atom_id IS NOT NULL
--         AND resolution_path_atom_id IS NOT NULL
--         AND expiry_trigger_atom_id IS NOT NULL
--       )) — the DV-S008-1 four-field discipline at SQL layer.
--     - CHECK (sub_type IS NULL OR status = 'active-with-conflict') —
--       sub_type only meaningful when conflict status; closed-CHECK refusal
--       on accidental sub_type with non-conflict status.
--
-- Why mutable status (not append-only via supersession_ledger):
--   D-3 divergence: P-1 mutable, P-2 supersession-only, P-3 mutable+history.
--   Synthesis adopts P-1 mutable + P-1 reject-history. Append-only via
--   supersession_ledger (P-2 M-1 minority) is compositionally elegant but
--   creates 9 rows for an assumption with 5 status changes; mixing closure-
--   state with replacement-relation weakens audit readability. Mutable
--   status with citing_decision FK on each transition keeps replay
--   reachable via decisions_v2 walk.
--
--   M-1 minority preserved (P-2 supersession-only): if calibration-EFs
--   surface status-mutation drift (e.g., agents flipping status without
--   citing a decision), the next session opens a gate-promotion OI for
--   either trigger-side citing-decision-required enforcement OR migration
--   to append-only via supersession_ledger.
--
-- Why no history table at v1 (rejects P-3 named edit #3):
--   P-1+P-2 convergence: replay walks decisions_v2 + decision_supports +
--   effects against assumption.object_id. A separate history table doubles
--   writes and invites the dual-channel watch-trigger S197 just paid for
--   (DV-S197-1 D-3 P-3 hard-cutover M-1 minority preservation).
--
--   M-3 minority preserved (P-3 history table): if replay-via-decisions
--   proves insufficient (calibration-EF naming "I cannot reconstruct
--   prior status of AR-S... from substrate alone"), the next session
--   ships migration NN adding assumption_status_changes (shape known per
--   P-3 named edit #4: change_id PK, assumption_id FK, from_status,
--   to_status, changed_at, origin_decision_object_id, basis_atom_id,
--   note_atom_id).
--
-- Why object_kind='assumption' (drops _ledger suffix):
--   P-1 open-question + answer: 'assumption' is cleaner than 'assumption_-
--   ledger' which adds no signal beyond table name. S197 shipped
--   'supersession_ledger' which is fine but the table-name redundancy is
--   real. Future tables prefer the unsuffixed form.
--
-- Why alias scheme AR-S<wno>-<seq>:
--   All 3 perspectives converged. AR avoids A-S<wno> assessment alias
--   collision and reads "assumption record". Workspace-scoped sequence
--   per session matches DV/EF/OI/FR/SL convention.
--
-- Why session_id FK and statement_atom NOT NULL:
--   Required-at-insert minimum so the row carries enough context to be
--   meaningful at chain-walk time. basis/four-conflict-atoms/decision-FKs
--   are NULL-admitting at column level, gated by CHECKs.
--
-- T-15 compliance:
--   - CHECK relaxation (admitting one new object_kind value 'assumption')
--     is non-destructive: admits strictly more rows than prior CHECK.
--     T-15-CALIBRATED block records the rebuild.
--   - PRAGMA foreign_keys=OFF for the duration of the rebuild.
--   - Trigger t07a_refs_no_superseded_cite references objects in its body
--     and is dropped + recreated around the rebuild (per migration 048
--     precedent).
--
-- role_write_capabilities INSERT inline (S194 lesson per DV-S194-1):
--   ('__cli__','assumption_ledger','insert')
--   ('__cli__','assumption_ledger','update')

PRAGMA foreign_keys = OFF;

BEGIN;

-- Drop the trigger whose body references objects (recreated below).
DROP TRIGGER t07a_refs_no_superseded_cite;

-- T-15-CALIBRATED-BEGIN: widen objects.object_kind CHECK to admit 'assumption'. Pure superset; no kind removed. Required so AR-S<wno>-<seq> aliases register in objects per D-6 C-2 + P-1 P-2 P-3 convergence.
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
        'reference_harness','supersession_ledger','assumption'
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
-- assumption_ledger: typed assumption-register primitive.
-- ============================================================================
CREATE TABLE assumption_ledger (
    assumption_id                       INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id                          INTEGER NOT NULL REFERENCES sessions(session_id),
    statement_atom_id                   INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    status                              TEXT NOT NULL DEFAULT 'unverified' CHECK (status IN (
                                            'unverified',
                                            'assumed',
                                            'active-with-conflict',
                                            'closed',
                                            'superseded',
                                            'invalidated'
                                        )),
    sub_type                            TEXT CHECK (sub_type IS NULL OR sub_type IN (
                                            'plan-vs-resource',
                                            'contested-authority',
                                            'rolling-renewal'
                                        )),
    action_commitment_atom_id           INTEGER REFERENCES text_atoms(atom_id),
    both_source_citation_atom_id        INTEGER REFERENCES text_atoms(atom_id),
    resolution_path_atom_id             INTEGER REFERENCES text_atoms(atom_id),
    expiry_trigger_atom_id              INTEGER REFERENCES text_atoms(atom_id),
    basis_atom_id                       INTEGER REFERENCES text_atoms(atom_id),
    origin_decision_object_id           INTEGER REFERENCES objects(object_id),
    last_transition_decision_object_id  INTEGER REFERENCES objects(object_id),
    object_id                           INTEGER REFERENCES objects(object_id),
    created_at                          TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    -- DV-S008-1 four-field discipline: when status=active-with-conflict,
    -- all four conflict-discipline atoms AND sub_type MUST be NOT NULL.
    CHECK (
        status != 'active-with-conflict' OR (
            sub_type IS NOT NULL
            AND action_commitment_atom_id IS NOT NULL
            AND both_source_citation_atom_id IS NOT NULL
            AND resolution_path_atom_id IS NOT NULL
            AND expiry_trigger_atom_id IS NOT NULL
        )
    ),
    -- sub_type only meaningful when status=active-with-conflict.
    CHECK (sub_type IS NULL OR status = 'active-with-conflict')
) STRICT;

CREATE INDEX idx_assumption_ledger_session ON assumption_ledger(session_id);
CREATE INDEX idx_assumption_ledger_status ON assumption_ledger(status);
CREATE INDEX idx_assumption_ledger_origin_decision ON assumption_ledger(origin_decision_object_id);
CREATE INDEX idx_assumption_ledger_last_transition ON assumption_ledger(last_transition_decision_object_id);

-- role_write_capabilities INSERT inline (S194 split-out lesson).
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','assumption_ledger','insert'),
    ('__cli__','assumption_ledger','update');

-- ============================================================================
-- Engine version bump.
-- ============================================================================
UPDATE workspace_metadata
   SET value = 'engine-v54'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('049-assumption-ledger-v1.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
