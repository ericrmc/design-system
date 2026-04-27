-- 003-substrate-strict-write-path.sql
-- engine-v19 → engine-v20
-- Path A (per S084 deliberation D-3 P-1): drop prose-in-rows admission for new writes.
-- Operator-ratified at S084 D-1: T-15 admits non-destructive CHECK-relaxation via the
-- calibrated marker pair `-- T-15-CALIBRATED-BEGIN: <reason>` / `-- T-15-CALIBRATED-END`.
-- The migration runner exempts DROP/ALTER inside calibrated blocks.

-- ============================================================================
-- 1. text_atoms: the only language slot for new writes.
-- atom_type determines length cap; atoms forbid newlines, fenced code, pipe tables.
-- ============================================================================
CREATE TABLE text_atoms (
    atom_id            INTEGER PRIMARY KEY,
    atom_type          TEXT NOT NULL CHECK (atom_type IN (
        'title','claim','spec_clause','spec_section_intent','finding',
        'alternative_option','rejection_reason','support_claim','next_step',
        'operator_quote','legacy_import','assessment_item','open_question',
        'perspective_position','perspective_claim','synthesis_claim',
        'engine_version_note','close_summary','close_state_item'
    )),
    text               TEXT NOT NULL,
    created_session_id INTEGER NOT NULL REFERENCES sessions(session_id),
    created_at         TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    CHECK (instr(text, char(10)) = 0),
    CHECK (text NOT GLOB '*```*'),
    CHECK (text NOT GLOB '*|*|*'),
    CHECK (
        CASE
            WHEN atom_type IN ('spec_clause','spec_section_intent') THEN length(text) BETWEEN 16 AND 480
            WHEN atom_type = 'legacy_import' THEN length(text) BETWEEN 8 AND 4000
            ELSE length(text) BETWEEN 8 AND 240
        END
    )
) STRICT;
CREATE INDEX idx_text_atoms_type ON text_atoms (atom_type);
CREATE INDEX idx_text_atoms_session ON text_atoms (created_session_id);

-- ============================================================================
-- 2 + 3. CHECK-relaxation on objects.object_kind and refs.relation (operator-
-- ratified at S084 D-1; calibrated under T-15-CALIBRATED). Refs is recreated
-- BEFORE objects because the old refs table's t07a trigger references objects;
-- dropping objects first would fail trigger validation.
-- ============================================================================
-- T-15-CALIBRATED-BEGIN: widen refs.relation CHECK to admit applies-to, derived-from, restates, implements, opens-issue, bumps-engine, modifies, creates. Pure superset.
CREATE TABLE refs_new (
    ref_id              INTEGER PRIMARY KEY,
    source_object_id    INTEGER NOT NULL,
    target_object_id    INTEGER NOT NULL,
    relation            TEXT NOT NULL CHECK (relation IN (
        'cites','supersedes','responds-to','depends-on','closes',
        'applies-to','derived-from','restates','implements',
        'opens-issue','bumps-engine','modifies','creates'
    )),
    allow_superseded    INTEGER NOT NULL DEFAULT 0 CHECK (allow_superseded IN (0,1)),
    reason_md           TEXT
) STRICT;
INSERT INTO refs_new SELECT * FROM refs;
DROP TABLE refs;
ALTER TABLE refs_new RENAME TO refs;
-- T-15-CALIBRATED-END

-- T-15-CALIBRATED-BEGIN: widen objects.object_kind CHECK to admit Path-A kinds (assessment, decision_v2, alternative_v2, spec_section, spec_clause, perspective_position, perspective_claim, review_finding, text_atom, legacy_import). Pure superset; no kind removed.
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
        'close_record','close_state_item','assessment_agenda_item'
    )),
    typed_row_id   INTEGER NOT NULL,
    citable_alias  TEXT UNIQUE,
    created_at     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
) STRICT;
INSERT INTO objects_new (object_id, object_kind, typed_row_id, citable_alias, created_at)
    SELECT object_id, object_kind, typed_row_id, citable_alias, created_at FROM objects;
DROP TABLE objects;
ALTER TABLE objects_new RENAME TO objects;
CREATE INDEX idx_objects_kind_typed_row ON objects (object_kind, typed_row_id);
-- T-15-CALIBRATED-END

-- Re-create indexes and triggers on the new refs (FKs to objects re-resolve).
CREATE INDEX idx_refs_source ON refs (source_object_id);
CREATE INDEX idx_refs_target ON refs (target_object_id);
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
CREATE TRIGGER t07b_refs_allow_superseded_requires_reason
BEFORE INSERT ON refs
FOR EACH ROW
WHEN NEW.allow_superseded = 1 AND (NEW.reason_md IS NULL OR length(NEW.reason_md) < 16)
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T07: allow_superseded=1 requires reason_md (>=16 chars)');
END;

-- ============================================================================
-- 4. assessments: closes the gap operator named at S084 D-1 #5.
-- ============================================================================
CREATE TABLE assessments (
    assessment_id       INTEGER PRIMARY KEY,
    session_id          INTEGER NOT NULL REFERENCES sessions(session_id),
    state_atom_id       INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (session_id)
) STRICT;
CREATE TABLE assessment_agenda_items (
    item_id             INTEGER PRIMARY KEY,
    assessment_id       INTEGER NOT NULL REFERENCES assessments(assessment_id),
    ord                 INTEGER NOT NULL,
    item_atom_id        INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    UNIQUE (assessment_id, ord)
) STRICT;

-- ============================================================================
-- 5. decisions_v2: P-1 shape. No body_md.
-- ============================================================================
CREATE TABLE decisions_v2 (
    decision_v2_id      INTEGER PRIMARY KEY,
    session_id          INTEGER NOT NULL REFERENCES sessions(session_id),
    decision_no         INTEGER NOT NULL,
    kind                TEXT NOT NULL CHECK (kind IN (
        'substantive','schema_migration','calibration','disposition','procedural'
    )),
    title_atom_id       INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    outcome_type        TEXT NOT NULL CHECK (outcome_type IN (
        'adopt','reject','defer','supersede','ratify'
    )),
    target_kind         TEXT NOT NULL CHECK (target_kind IN (
        'process_rule','spec_version','migration','issue','review_rule','engine_version','open_question'
    )),
    target_key          TEXT NOT NULL CHECK (length(target_key) BETWEEN 2 AND 120),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (session_id, decision_no)
) STRICT;

-- decision_supports: typed reasons, not prose.
CREATE TABLE decision_supports (
    support_id          INTEGER PRIMARY KEY,
    decision_v2_id      INTEGER NOT NULL REFERENCES decisions_v2(decision_v2_id),
    seq                 INTEGER NOT NULL,
    basis               TEXT NOT NULL CHECK (basis IN (
        'constraint','operator_directive','prior_decision','review_finding',
        'deliberation','spec_clause','engine_feedback'
    )),
    claim_atom_id       INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    cited_object_id     INTEGER REFERENCES objects(object_id),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (decision_v2_id, seq)
) STRICT;

-- decision_effects: what the decision changes.
CREATE TABLE decision_effects (
    effect_id           INTEGER PRIMARY KEY,
    decision_v2_id      INTEGER NOT NULL REFERENCES decisions_v2(decision_v2_id),
    effect_kind         TEXT NOT NULL CHECK (effect_kind IN (
        'creates','modifies','supersedes','opens_issue','bumps_engine','closes_issue','adds_migration'
    )),
    target_object_id    INTEGER REFERENCES objects(object_id),
    target_descriptor   TEXT CHECK (target_descriptor IS NULL OR length(target_descriptor) BETWEEN 2 AND 120),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (decision_v2_id, effect_kind, target_object_id, target_descriptor)
) STRICT;
-- One of target_object_id or target_descriptor must be present.
CREATE TRIGGER t17_decision_effects_target_present
BEFORE INSERT ON decision_effects
FOR EACH ROW
WHEN NEW.target_object_id IS NULL AND NEW.target_descriptor IS NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T17: decision_effect requires target_object_id or target_descriptor');
END;

-- alternatives_v2 + alternative_rejections (closes the rejection_reason_md hole).
CREATE TABLE alternatives_v2 (
    alternative_v2_id   INTEGER PRIMARY KEY,
    decision_v2_id      INTEGER NOT NULL REFERENCES decisions_v2(decision_v2_id),
    label               TEXT NOT NULL CHECK (label GLOB 'R-[0-9]*[0-9]*'),
    option_atom_id      INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (decision_v2_id, label)
) STRICT;

CREATE TABLE alternative_rejections (
    rejection_id        INTEGER PRIMARY KEY,
    alternative_v2_id   INTEGER NOT NULL REFERENCES alternatives_v2(alternative_v2_id),
    seq                 INTEGER NOT NULL DEFAULT 1,
    basis               TEXT NOT NULL CHECK (basis IN (
        'no_feedback_loop','operator_override','violates_gate','too_large_for_session',
        'inferior_tradeoff','preserves_legacy_path','redundant_with_existing','breaks_invariant'
    )),
    rejection_atom_id   INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    cited_object_id     INTEGER REFERENCES objects(object_id),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (alternative_v2_id, seq)
) STRICT;

-- T-18: substantive decision_v2 close-gate.
-- Substantive decisions need >=1 support, >=1 alternative, each alternative needs >=1 rejection.
CREATE TRIGGER t18_close_decisions_v2_complete
BEFORE UPDATE OF status ON sessions
FOR EACH ROW
WHEN OLD.status = 'open' AND NEW.status = 'closed'
 AND EXISTS (
    SELECT 1 FROM decisions_v2 d
    WHERE d.session_id = NEW.session_id AND d.kind = 'substantive'
      AND (
          NOT EXISTS (SELECT 1 FROM decision_supports s WHERE s.decision_v2_id = d.decision_v2_id)
          OR NOT EXISTS (SELECT 1 FROM alternatives_v2 a WHERE a.decision_v2_id = d.decision_v2_id)
      )
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T18: substantive decision_v2 missing support or alternative');
END;

CREATE TRIGGER t19_close_alternatives_v2_have_rejection
BEFORE UPDATE OF status ON sessions
FOR EACH ROW
WHEN OLD.status = 'open' AND NEW.status = 'closed'
 AND EXISTS (
    SELECT 1 FROM alternatives_v2 a
    JOIN decisions_v2 d ON d.decision_v2_id = a.decision_v2_id
    WHERE d.session_id = NEW.session_id
      AND NOT EXISTS (SELECT 1 FROM alternative_rejections r WHERE r.alternative_v2_id = a.alternative_v2_id)
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T19: alternative_v2 missing rejection');
END;

-- ============================================================================
-- 6. spec_sections + spec_clauses + spec_clause_links.
-- spec_versions gains body_canonical_in_substrate flag (additive ALTER ADD).
-- ============================================================================
ALTER TABLE spec_versions ADD COLUMN body_canonical_in_substrate INTEGER NOT NULL DEFAULT 0
    CHECK (body_canonical_in_substrate IN (0,1));

CREATE TABLE spec_sections (
    spec_section_id     INTEGER PRIMARY KEY,
    spec_version_id     INTEGER NOT NULL REFERENCES spec_versions(spec_version_id),
    ord                 INTEGER NOT NULL,
    heading_atom_id     INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    intent_atom_id      INTEGER REFERENCES text_atoms(atom_id),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (spec_version_id, ord)
) STRICT;

CREATE TABLE spec_clauses (
    spec_clause_id      INTEGER PRIMARY KEY,
    spec_section_id     INTEGER NOT NULL REFERENCES spec_sections(spec_section_id),
    ord                 INTEGER NOT NULL,
    clause_type         TEXT NOT NULL CHECK (clause_type IN (
        'definition','rule','scope','process','exception','rationale','validation','risk','example','enumeration'
    )),
    normative_level     TEXT NOT NULL CHECK (normative_level IN ('must','should','may','descriptive')),
    clause_atom_id      INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    source_decision_v2_id INTEGER REFERENCES decisions_v2(decision_v2_id),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (spec_section_id, ord)
) STRICT;

CREATE TABLE spec_clause_links (
    link_id             INTEGER PRIMARY KEY,
    source_clause_id    INTEGER NOT NULL REFERENCES spec_clauses(spec_clause_id),
    relation            TEXT NOT NULL CHECK (relation IN ('supersedes','depends_on','implements','restates','exception_to')),
    target_object_id    INTEGER NOT NULL REFERENCES objects(object_id),
    UNIQUE (source_clause_id, relation, target_object_id)
) STRICT;

-- ============================================================================
-- 7. perspective_positions + perspective_claims.
-- Decompose the prose body_md of perspectives into typed atoms.
-- ============================================================================
CREATE TABLE perspective_positions (
    position_id         INTEGER PRIMARY KEY,
    perspective_id      INTEGER NOT NULL REFERENCES perspectives(perspective_id),
    position_atom_id    INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (perspective_id)
) STRICT;

CREATE TABLE perspective_claims (
    claim_id            INTEGER PRIMARY KEY,
    perspective_id      INTEGER NOT NULL REFERENCES perspectives(perspective_id),
    seq                 INTEGER NOT NULL,
    section_kind        TEXT NOT NULL CHECK (section_kind IN (
        'position','schema_sketch','cli_surface','migration_path','what_not','open_question','risk','what_lost'
    )),
    claim_atom_id       INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    cited_object_id     INTEGER REFERENCES objects(object_id),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (perspective_id, seq)
) STRICT;

-- ============================================================================
-- 8. review_findings: lift S083's 04-review.md pattern into the substrate.
-- ============================================================================
CREATE TABLE review_findings (
    review_finding_id   INTEGER PRIMARY KEY,
    session_id          INTEGER NOT NULL REFERENCES sessions(session_id),
    iteration           INTEGER NOT NULL CHECK (iteration BETWEEN 1 AND 4),
    severity            TEXT NOT NULL CHECK (severity IN ('critical','high','medium','low')),
    finding_atom_id     INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    target_object_id    INTEGER REFERENCES objects(object_id),
    disposition         TEXT NOT NULL CHECK (disposition IN ('open','fixed','adjudicated')),
    disposition_atom_id INTEGER REFERENCES text_atoms(atom_id),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (session_id, iteration, review_finding_id)
) STRICT;

-- T-20: a session with any code-touching change (effect_kind in 'creates','modifies'
-- against target object_kind in code-bearing kinds) cannot close while a review_finding
-- of severity in (critical,high,medium) has disposition='open'.
-- (Operator-policed at v19; structurally enforced at v20.)
CREATE TRIGGER t20_close_no_open_medium_plus_findings
BEFORE UPDATE OF status ON sessions
FOR EACH ROW
WHEN OLD.status = 'open' AND NEW.status = 'closed'
 AND EXISTS (
    SELECT 1 FROM review_findings rf
    WHERE rf.session_id = NEW.session_id
      AND rf.disposition = 'open'
      AND rf.severity IN ('critical','high','medium')
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T20: open medium-or-higher review findings prevent close');
END;

-- ============================================================================
-- 9. legacy_imports: bridge old prose rows to text_atoms.
-- decomposition_status tracks whether a backfill session has re-authored.
-- ============================================================================
CREATE TABLE legacy_imports (
    legacy_import_id    INTEGER PRIMARY KEY,
    old_table           TEXT NOT NULL CHECK (old_table IN (
        'decisions','decision_alternatives','perspectives','deliberations',
        'engine_feedback','synthesis_points'
    )),
    old_pk              INTEGER NOT NULL,
    atom_id             INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    decomposition_status TEXT NOT NULL DEFAULT 'unratified' CHECK (decomposition_status IN (
        'unratified','in_progress','ratified','exempt'
    )),
    decomposed_in_session_id INTEGER REFERENCES sessions(session_id),
    UNIQUE (old_table, old_pk)
) STRICT;

-- ============================================================================
-- 10. close_records: substantive close narrative as structured atoms (replaces
-- 03-close.md authorship).
-- ============================================================================
CREATE TABLE close_records (
    close_record_id     INTEGER PRIMARY KEY,
    session_id          INTEGER NOT NULL REFERENCES sessions(session_id),
    summary_atom_id     INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (session_id)
) STRICT;
CREATE TABLE close_state_items (
    state_item_id       INTEGER PRIMARY KEY,
    close_record_id     INTEGER NOT NULL REFERENCES close_records(close_record_id),
    seq                 INTEGER NOT NULL,
    facet               TEXT NOT NULL CHECK (facet IN (
        'what_was_done','state_at_close','open_issues','next_session_should',
        'engine_version','validator_summary'
    )),
    item_atom_id        INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    UNIQUE (close_record_id, seq)
) STRICT;

-- ============================================================================
-- 11. T-06 immutability: extend to all new tables for closed sessions.
-- ============================================================================
CREATE TRIGGER t06_text_atoms_no_mut_after_close_upd
BEFORE UPDATE ON text_atoms
FOR EACH ROW
WHEN EXISTS (SELECT 1 FROM sessions WHERE session_id = OLD.created_session_id AND status = 'closed')
BEGIN SELECT RAISE(ABORT, 'E_REFUSAL_T06: text_atom belongs to a closed session'); END;
CREATE TRIGGER t06_text_atoms_no_mut_after_close_del
BEFORE DELETE ON text_atoms
FOR EACH ROW
WHEN EXISTS (SELECT 1 FROM sessions WHERE session_id = OLD.created_session_id AND status = 'closed')
BEGIN SELECT RAISE(ABORT, 'E_REFUSAL_T06: text_atom belongs to a closed session'); END;

-- ============================================================================
-- 12. role_write_capabilities: seed __cli__ for new tables.
-- ============================================================================
INSERT OR IGNORE INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','text_atoms','insert'),
    ('__cli__','assessments','insert'),
    ('__cli__','assessment_agenda_items','insert'),
    ('__cli__','decisions_v2','insert'),
    ('__cli__','decision_supports','insert'),
    ('__cli__','decision_effects','insert'),
    ('__cli__','alternatives_v2','insert'),
    ('__cli__','alternative_rejections','insert'),
    ('__cli__','spec_sections','insert'),
    ('__cli__','spec_clauses','insert'),
    ('__cli__','spec_clause_links','insert'),
    ('__cli__','spec_versions','update'),
    ('__cli__','perspective_positions','insert'),
    ('__cli__','perspective_claims','insert'),
    ('__cli__','review_findings','insert'),
    ('__cli__','review_findings','update'),
    ('__cli__','legacy_imports','insert'),
    ('__cli__','legacy_imports','update'),
    ('__cli__','close_records','insert'),
    ('__cli__','close_state_items','insert');

-- ============================================================================
-- 13. Record this migration in schema_migrations.
-- ============================================================================
INSERT INTO schema_migrations (name, sha256) VALUES ('003-substrate-strict-write-path.sql', 'COMPUTED-AT-APPLY-TIME');

-- End migration 003.
