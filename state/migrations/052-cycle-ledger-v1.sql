-- Migration 052: cycle-ledger v1 typed primitive (C-6 rolling-renewal cycle).
-- engine-v56 -> engine-v57 (S203 DV-S203-1 closes OI-S196-6 by-mechanism).
--
-- Why:
--   OI-S196-6 named the C-6 rolling-renewal cycle primitive in S196's
--   disaster-recovery deliverable-mining triage (DV-S196-1). Evidence base:
--   A-018 (satellite uplink rationing, 5 cycles T+214h to T+382h) and A-020
--   (medevac slots, 3 cycles T+208h to T+280h) from disaster-recovery arc;
--   plus DV-S011-5 design pattern naming 24h-rolling-renewal with body-field
--   snapshots and 3-consecutive-cycles trigger conditions. Codex ratified
--   2-case evidence sufficient at S196 with operator-named-mandate.
--
--   S202 meta-session pre-scoped the shape: codex shape-consult per FR-S196-16
--   gave SINGLE-SHIP verdict + 6-knot positions + priority-ordering 1+3+6
--   load-bearing-v1 and 2+4+5 deferrable-v2 (EF-S202-1). Cross-application
--   generalization (subscription-renewal, ML-calibration, compliance-review,
--   sprint reviews, periodic risk reassessment) lifted as AR-S202-1 per
--   operator-named-mandate at S202 turn that future apps not all disaster-
--   recovery focused. DV-S202-1 sealed meta-then-coding split.
--
--   Deliberation D-9 at S203 (3-perspective: P-1 schema-minimality AR-only,
--   P-2 cross-app aggressive [assumption,issue,decision_v2] allowlist,
--   P-3 codex shape-consult middle-ground) sealed with 5 convergence + 2
--   divergence + 3 minority synthesis points; 3 counterfactuals dispositioned.
--   Synthesis: codex P-3 middle ground adopted on knots 1+3+6 with P-1
--   AR-only (M-1) and P-2 broader-allowlist (M-2) preserved as watch-trigger
--   minorities + CF-1 hard-cutover (M-3) preserved.
--
-- Schema:
--   cycle_ledger
--     - cycle_id PK INTEGER AUTOINCREMENT.
--     - session_id FK sessions: origin session (per-session seq for
--       CYC-S<wno>-<seq> alias generation).
--     - subject_object_id FK objects NOT NULL: polymorphic FK admitting
--       any registered object alias whose object_kind is in the v1
--       allowlist (= 'assumption' only at v1; broader admit at v2 per
--       M-2 watch-trigger). Allowlist enforced via T-42 trigger reading
--       objects.object_kind on insert.
--     - cycle_no INTEGER NOT NULL: per-subject iteration number,
--       monotonic-via-UNIQUE not strict-+1 (codex stance + P-1 P-2 P-3
--       convergence).
--     - observed_at TEXT NOT NULL DEFAULT now: when this cycle's state
--       was observed (distinct from created_at which is the row insert).
--     - snapshot_atom_id FK text_atoms NOT NULL: 8-480 char snapshot of
--       observed state under atom_type='support_claim' (codex C-5 atom-tier
--       convergence per OI-S177-1 widening).
--     - classification TEXT NOT NULL CHECK closed-2 enum
--       {'substantial', 'non-substantial'}: agent-judged classification
--       (D-2 P-1+P-3 simpler stance over P-2+P-3 hybrid; P-3 hybrid-with-
--       diff-metadata preserved as forward-direction).
--     - classification_reason_atom_id FK text_atoms NULL: required when
--       classification='substantial' via row CHECK; admits NULL when
--       classification='non-substantial' (codex stance: cycle-row-IS-proof
--       of observation suffices for non-substantial).
--     - citing_supersession_object_id FK objects NULL: optional FK to a
--       supersession_ledger SL alias when substantial cycle marks a real
--       supersession relation (knot 3 codex stance: substantial MAY cite
--       SL when supersession exists; non-substantial NEVER cites SL).
--     - object_id FK objects NULL: back-pointer to registered cycle
--       object (alias CYC-S<wno>-<seq>).
--     - created_at TEXT default now.
--     - UNIQUE (subject_object_id, cycle_no): refuses duplicate cycle
--       numbers per subject.
--     - CHECK (classification != 'substantial' OR classification_reason_atom_id
--       IS NOT NULL): substantial requires reason atom (D-2 synthesis).
--
-- Why polymorphic-via-objects-FK with assumption-only allowlist (D-1):
--   P-1 AR-only stance (cycle_ledger.assumption_id direct FK) preserved
--   as M-1 minority watch-trigger; P-2 broader-allowlist [assumption,
--   issue, decision_v2] preserved as M-2 minority watch-trigger.
--   Adopted: P-3 codex middle ground per priority-ordering load-bearing
--   knot 6 + DV-S197-1 polymorphism precedent + AR-S202-1 cross-app
--   generalization signal. Allowlist starts with 'assumption' only at v1;
--   v2 extends to 'issue' (compliance-review cycles) and 'decision_v2'
--   (ML-calibration retrain cycles) once cross-app evidence accumulates.
--
-- Why cycle row IS proof of observation (knot 3 C-1):
--   All 3 perspectives converge: cycle_ledger row IS the substrate proof
--   of cycle observation (avoid the dual-channel watch-trigger that S197
--   shipped as M-1). Non-substantial cycles emit zero supersession_ledger
--   rows (the noise-suppression value of the primitive). Substantial
--   cycles MAY optionally cite an SL row when a real supersession
--   relation exists (operator/agent decides; handler does not auto-emit).
--
-- Why reuse closure_shape from S201 (knot 5 C-2):
--   All 3 perspectives converge: closure_shape (DV-S201-1, 5-value enum
--   {convergence, completion, containment-resolved, supersession,
--   stable-held}) lives on parent assumption_ledger; cycle_ledger does
--   not carry own column at v1 per DV-S201-1 no-premature-unification
--   binding. Closure semantics flow via parent assumption FK lookup at
--   query time. CF-3 (cycle-specific closure_path enum) nilled-by-
--   exclusion barred-by-constraint.
--
-- Why defer typed cycle_trigger to v2 (knot 4 C-3):
--   All 3 perspectives converge on defer per ceremony-subtraction;
--   N-cycle reasoning is query-time at v1 not typed-row at v1. P-2 and
--   P-3 stances (typed cycle_trigger) preserved as forward-direction
--   per DV-S152-1 typed-observation->gate progression: calibration-EF
--   surfacing N-cycle reasoning need across N>=2 sessions opens v2
--   migration adding cycle_trigger child rows + closed pattern_kind
--   CHECK enum.
--
-- Why object_kind='cycle' (drops _ledger suffix):
--   DV-S198-1 P-1 stance precedent: drop _ledger suffix that adds no
--   signal beyond table name. Cycle alias CYC-S<wno>-<seq> per session
--   matches DV/EF/OI/FR/SL/AR convention.
--
-- Watch-triggers (DV-S203-1 minorities preserved):
--   M-1 P-1 AR-child-only: zero non-assumption subjects across N>=5
--   sessions OR allowlist-extension blocked by subject_kind-specific
--   semantics opens gate-promotion OI for AR-FK direct table refactor.
--
--   M-2 P-2 broader-allowlist: cross-app cycles attempting registration
--   under non-allowlist subject_kind (issue/decision_v2) across N>=2
--   sessions opens gate-promotion OI for allowlist extension migration.
--
--   M-3 hard-cutover (CF-1): dual-channel writes persisting OR cycle_-
--   ledger 0 inserts across N>=5 sessions opens gate-promotion OI for
--   hard-cutover deprecating sub_type='rolling-renewal' channel.
--
-- T-15 compliance:
--   - CHECK relaxation (admitting one new object_kind value 'cycle')
--     is non-destructive: admits strictly more rows than prior CHECK.
--     T-15-CALIBRATED block records the rebuild.
--   - PRAGMA foreign_keys=OFF for the rebuild duration.
--   - Trigger t07a_refs_no_superseded_cite references objects in body
--     and is dropped + recreated around the rebuild (per migration
--     048/049/051 precedent).
--
-- T-42 (new): cycle_ledger subject allowlist gate.
--   BEFORE INSERT trigger refusing rows where subject_object_id resolves
--   to an object whose object_kind is not in the v1 allowlist set.
--   Refusal text names allowlist + recovery (file calibration-EF if
--   subject_kind extension warranted; opens M-2 gate-promotion path).
--
-- role_write_capabilities INSERT inline (S194 lesson per DV-S194-1):
--   ('__cli__','cycle_ledger','insert')

PRAGMA foreign_keys = OFF;

BEGIN;

-- Drop the trigger whose body references objects (recreated below).
DROP TRIGGER t07a_refs_no_superseded_cite;

-- T-15-CALIBRATED-BEGIN: widen objects.object_kind CHECK to admit 'cycle'. Pure superset; no kind removed. Required so CYC-S<wno>-<seq> aliases register in objects per D-9 C-5 + P-1 P-2 P-3 convergence.
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
        'reference_harness','supersession_ledger','assumption','cycle'
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
-- cycle_ledger: typed rolling-renewal cycle primitive (C-6).
-- ============================================================================
CREATE TABLE cycle_ledger (
    cycle_id                       INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id                     INTEGER NOT NULL REFERENCES sessions(session_id),
    subject_object_id              INTEGER NOT NULL REFERENCES objects(object_id),
    cycle_no                       INTEGER NOT NULL,
    observed_at                    TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    snapshot_atom_id               INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    classification                 TEXT NOT NULL CHECK (classification IN (
                                       'substantial',
                                       'non-substantial'
                                   )),
    classification_reason_atom_id  INTEGER REFERENCES text_atoms(atom_id),
    citing_supersession_object_id  INTEGER REFERENCES objects(object_id),
    object_id                      INTEGER REFERENCES objects(object_id),
    created_at                     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    -- D-2 synthesis: substantial requires classification_reason atom.
    CHECK (
        classification != 'substantial'
        OR classification_reason_atom_id IS NOT NULL
    ),
    -- Refuse duplicate (subject, cycle_no) per knot 1 + codex.
    UNIQUE (subject_object_id, cycle_no)
) STRICT;

CREATE INDEX idx_cycle_ledger_session ON cycle_ledger(session_id);
CREATE INDEX idx_cycle_ledger_subject ON cycle_ledger(subject_object_id);
CREATE INDEX idx_cycle_ledger_classification ON cycle_ledger(classification);
CREATE INDEX idx_cycle_ledger_supersession ON cycle_ledger(citing_supersession_object_id);

-- T-42: cycle_ledger subject allowlist gate (assumption only at v1).
-- M-1 watch-trigger graduation path opens AR-FK refactor OI if zero
-- non-assumption subjects accumulate; M-2 graduation path opens allowlist
-- extension OI if cross-app cycles attempt registration.
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

-- role_write_capabilities INSERT inline (S194 split-out lesson).
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','cycle_ledger','insert');

-- ============================================================================
-- Engine version bump.
-- ============================================================================
UPDATE workspace_metadata
   SET value = 'engine-v57'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('052-cycle-ledger-v1.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
