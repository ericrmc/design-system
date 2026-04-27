-- Migration 001: initial substrate (engine-v17, session 079).
-- Implements 078 D-1 (substrate-shape: S1 cells + S3 tuples + S2 files),
--            078 D-3 (16 refusals T-01..T-16),
--            078 D-9 (SQLite single-writer; WAL).
-- Table count: 17 (16 from 078 D-10 + synthesis_points).
-- The synthesis_points table is required by T-14 and 078 D-1 listed it among S3 tuples;
-- 078 D-10's enumeration of 16 omitted it inadvertently. 079 closes the omission as a
-- calibration; this migration breaches the D-10 budget by 1 with cause recorded in
-- 079 02-decisions.md (per D-10 "breachable with cause").

-- ============================================================================
-- Pragmas
-- ============================================================================
PRAGMA foreign_keys = ON;
PRAGMA journal_mode = WAL;
PRAGMA synchronous = NORMAL;

BEGIN;

-- ============================================================================
-- Migration metadata (for D-8 protocol; T-15 enforced at apply-time by CLI).
-- ============================================================================
CREATE TABLE IF NOT EXISTS schema_migrations (
    migration_id   INTEGER PRIMARY KEY,
    name           TEXT NOT NULL UNIQUE,
    sha256         TEXT NOT NULL,
    applied_at     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
) STRICT;

-- ============================================================================
-- sessions: T-10 contiguous; T-02/T-11 enforced on close.
-- ============================================================================
CREATE TABLE sessions (
    session_id              INTEGER PRIMARY KEY,
    session_no              INTEGER NOT NULL UNIQUE,
    slug                    TEXT NOT NULL,
    mode                    TEXT NOT NULL CHECK (mode IN ('self-development','external-problem')),
    workspace_id            TEXT NOT NULL,
    engine_version_at_open  TEXT NOT NULL,
    engine_version_at_close TEXT,
    status                  TEXT NOT NULL CHECK (status IN ('open','closed')),
    opened_at               TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    closed_at               TEXT
) STRICT;

-- T-10: session_no = MAX(session_no)+1 (contiguous, monotonic).
CREATE TRIGGER t10_sessions_contiguous
BEFORE INSERT ON sessions
FOR EACH ROW
WHEN NEW.session_no <> (SELECT COALESCE(MAX(session_no), 0) + 1 FROM sessions)
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T10: session_no must equal MAX(session_no)+1');
END;

-- ============================================================================
-- objects: universal addressable identity (T-01 ref targets).
-- typed_row_id is disambiguated by object_kind. citable_alias is the human-readable
-- handle parsed from body_md (e.g. 'D-S079-1', 'SPEC-methodology-v2').
-- ============================================================================
CREATE TABLE objects (
    object_id      INTEGER PRIMARY KEY,
    object_kind    TEXT NOT NULL CHECK (object_kind IN (
        'decision','spec_version','perspective','deliberation',
        'commitment','engine_feedback','session','synthesis_point',
        'work_item','subtraction','agent_run'
    )),
    typed_row_id   INTEGER NOT NULL,
    citable_alias  TEXT UNIQUE,
    created_at     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
) STRICT;
CREATE INDEX idx_objects_kind_typed_row ON objects (object_kind, typed_row_id);

-- ============================================================================
-- decisions: S1 cells. T-02 enforced on session close. body_md may contain
-- citable_alias references like [D-S079-1], parsed into refs at submit time.
-- ============================================================================
CREATE TABLE decisions (
    decision_id   INTEGER PRIMARY KEY,
    session_id    INTEGER NOT NULL REFERENCES sessions(session_id),
    decision_no   INTEGER NOT NULL,
    kind          TEXT NOT NULL CHECK (kind IN ('substantive','schema-migration','calibration','disposition')),
    title         TEXT NOT NULL,
    body_md       TEXT NOT NULL,
    object_id     INTEGER REFERENCES objects(object_id),
    UNIQUE (session_id, decision_no)
) STRICT;

-- ============================================================================
-- decision_alternatives: S3 tuples. T-08: rejection_reason_md must be ≥ 16 chars.
-- ============================================================================
CREATE TABLE decision_alternatives (
    alternative_id        INTEGER PRIMARY KEY,
    decision_id           INTEGER NOT NULL REFERENCES decisions(decision_id),
    label                 TEXT NOT NULL,
    summary               TEXT NOT NULL,
    rejection_reason_md   TEXT NOT NULL CHECK (length(rejection_reason_md) >= 16)
) STRICT;

-- ============================================================================
-- spec_versions: S2 files. T-03 unique-active; T-04 hash via CLI; T-07 supersession.
-- ============================================================================
CREATE TABLE spec_versions (
    spec_version_id   INTEGER PRIMARY KEY,
    spec_id           TEXT NOT NULL,
    version           INTEGER NOT NULL,
    body_path         TEXT NOT NULL,
    body_sha256       TEXT NOT NULL CHECK (length(body_sha256) = 64),
    status            TEXT NOT NULL CHECK (status IN ('active','superseded')),
    session_id        INTEGER NOT NULL REFERENCES sessions(session_id),
    object_id         INTEGER REFERENCES objects(object_id),
    UNIQUE (spec_id, version)
) STRICT;
-- T-03: at most one active row per spec_id.
CREATE UNIQUE INDEX t03_spec_versions_one_active
    ON spec_versions (spec_id) WHERE status = 'active';

-- ============================================================================
-- deliberations + perspectives + synthesis_points.
-- T-05: no perspective insert when deliberation is sealed.
-- T-13: no UPDATE setting sealed_at back to NULL.
-- T-14: convergence requires ≥2 source_perspectives.
-- ============================================================================
CREATE TABLE deliberations (
    deliberation_id   INTEGER PRIMARY KEY,
    session_id        INTEGER NOT NULL REFERENCES sessions(session_id),
    topic             TEXT NOT NULL,
    sealed_at         TEXT,
    synthesis_md      TEXT,
    object_id         INTEGER REFERENCES objects(object_id)
) STRICT;

CREATE TABLE perspectives (
    perspective_id   INTEGER PRIMARY KEY,
    deliberation_id  INTEGER NOT NULL REFERENCES deliberations(deliberation_id),
    label            TEXT NOT NULL,
    family           TEXT NOT NULL CHECK (family IN ('anthropic','openai','google','other-llm','human')),
    body_md          TEXT NOT NULL,
    submitted_at     TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    object_id        INTEGER REFERENCES objects(object_id)
) STRICT;

-- T-05: no insert into perspectives once deliberation is sealed.
CREATE TRIGGER t05_perspectives_blind_seal
BEFORE INSERT ON perspectives
FOR EACH ROW
WHEN (SELECT sealed_at FROM deliberations WHERE deliberation_id = NEW.deliberation_id) IS NOT NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T05: deliberation is sealed; no perspectives may be inserted');
END;

-- T-13: deliberations.sealed_at, once non-NULL, cannot be cleared.
CREATE TRIGGER t13_deliberations_sealed_immutable
BEFORE UPDATE OF sealed_at ON deliberations
FOR EACH ROW
WHEN OLD.sealed_at IS NOT NULL AND NEW.sealed_at IS NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T13: sealed_at cannot be set back to NULL');
END;

CREATE TABLE synthesis_points (
    synthesis_point_id    INTEGER PRIMARY KEY,
    deliberation_id       INTEGER NOT NULL REFERENCES deliberations(deliberation_id),
    kind                  TEXT NOT NULL CHECK (kind IN ('convergence','divergence','minority')),
    label                 TEXT NOT NULL,
    summary               TEXT NOT NULL,
    source_perspectives   TEXT NOT NULL,           -- JSON array of perspective_id
    body_md               TEXT,
    object_id             INTEGER REFERENCES objects(object_id),
    -- T-14: convergence requires ≥2 source perspectives.
    CHECK (kind <> 'convergence' OR json_array_length(source_perspectives) >= 2)
) STRICT;

-- ============================================================================
-- refs: T-01 / T-07 supersession.
-- ============================================================================
CREATE TABLE refs (
    ref_id              INTEGER PRIMARY KEY,
    source_object_id    INTEGER NOT NULL REFERENCES objects(object_id),
    target_object_id    INTEGER NOT NULL REFERENCES objects(object_id),
    relation            TEXT NOT NULL CHECK (relation IN ('cites','supersedes','responds-to','depends-on','closes')),
    allow_superseded    INTEGER NOT NULL DEFAULT 0 CHECK (allow_superseded IN (0,1)),
    reason_md           TEXT
) STRICT;

-- T-07a: cite of a superseded spec_version is refused unless allow_superseded=1.
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

-- T-07b: when allow_superseded=1, reason_md must be present and ≥16 chars.
CREATE TRIGGER t07b_refs_allow_superseded_requires_reason
BEFORE INSERT ON refs
FOR EACH ROW
WHEN NEW.allow_superseded = 1 AND (NEW.reason_md IS NULL OR length(NEW.reason_md) < 16)
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T07: allow_superseded=1 requires reason_md (>=16 chars)');
END;

-- ============================================================================
-- commitments: T-09 state machine open → met | abandoned | superseded.
-- ============================================================================
CREATE TABLE commitments (
    commitment_id   INTEGER PRIMARY KEY,
    decision_id     INTEGER NOT NULL REFERENCES decisions(decision_id),
    summary_md      TEXT NOT NULL CHECK (length(summary_md) <= 280),
    status          TEXT NOT NULL CHECK (status IN ('open','met','abandoned','superseded')),
    object_id       INTEGER REFERENCES objects(object_id)
) STRICT;

-- T-09: state-machine transitions: open → {met,abandoned,superseded}; terminals are immutable.
CREATE TRIGGER t09_commitments_state_machine
BEFORE UPDATE OF status ON commitments
FOR EACH ROW
WHEN NOT (
    (OLD.status = 'open' AND NEW.status IN ('met','abandoned','superseded'))
    OR OLD.status = NEW.status
)
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T09: invalid commitment status transition');
END;

-- ============================================================================
-- engine_feedback: S1 cells.
-- ============================================================================
CREATE TABLE engine_feedback (
    feedback_id    INTEGER PRIMARY KEY,
    session_id     INTEGER NOT NULL REFERENCES sessions(session_id),
    flag           TEXT NOT NULL CHECK (flag IN ('observation','reframe','calibration','blocker','triage')),
    body_md        TEXT NOT NULL,
    disposition    TEXT,
    object_id      INTEGER REFERENCES objects(object_id)
) STRICT;

-- ============================================================================
-- work_items: lease-based queue. T-11 (close requires queue clear); T-16 (lease expiry).
-- ============================================================================
CREATE TABLE work_items (
    work_item_id       INTEGER PRIMARY KEY,
    session_id         INTEGER NOT NULL REFERENCES sessions(session_id),
    kind               TEXT NOT NULL CHECK (kind IN ('specify','decide','deliberate','review','other')),
    payload_json       TEXT NOT NULL,
    status             TEXT NOT NULL CHECK (status IN ('queued','leased','completed','failed')),
    leased_by          TEXT,
    leased_at          TEXT,
    lease_expires_at   TEXT,
    completed_at       TEXT,
    idempotency_key    TEXT UNIQUE
) STRICT;

-- T-16: a leased row whose lease has expired must not be inserted/updated as 'leased'.
-- Application-layer (`selvedge recover`) resets such rows to 'queued'; the trigger refuses
-- direct attempts to declare a leased row whose lease is already expired.
CREATE TRIGGER t16_work_items_lease_not_expired
BEFORE INSERT ON work_items
FOR EACH ROW
WHEN NEW.status = 'leased'
 AND NEW.lease_expires_at IS NOT NULL
 AND NEW.lease_expires_at < strftime('%Y-%m-%dT%H:%M:%fZ','now')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T16: cannot insert leased row with already-expired lease');
END;
CREATE TRIGGER t16_work_items_lease_not_expired_upd
BEFORE UPDATE ON work_items
FOR EACH ROW
WHEN NEW.status = 'leased'
 AND NEW.lease_expires_at IS NOT NULL
 AND NEW.lease_expires_at < strftime('%Y-%m-%dT%H:%M:%fZ','now')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T16: cannot mark row leased with already-expired lease');
END;

-- ============================================================================
-- role_write_capabilities: T-12 lookup table.
-- ============================================================================
CREATE TABLE role_write_capabilities (
    role        TEXT NOT NULL,
    table_name  TEXT NOT NULL,
    write_op    TEXT NOT NULL CHECK (write_op IN ('insert','update','delete')),
    PRIMARY KEY (role, table_name, write_op)
) STRICT;

-- Seed capabilities for engine-v17 roles. The `__cli__` role is the human-driven CLI
-- (no agent in 079); 080+ adds role rows for specifier/decider/deliberator-N/human-reviewer.
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','sessions','insert'),
    ('__cli__','sessions','update'),
    ('__cli__','decisions','insert'),
    ('__cli__','decision_alternatives','insert'),
    ('__cli__','spec_versions','insert'),
    ('__cli__','spec_versions','update'),
    ('__cli__','perspectives','insert'),
    ('__cli__','deliberations','insert'),
    ('__cli__','deliberations','update'),
    ('__cli__','synthesis_points','insert'),
    ('__cli__','refs','insert'),
    ('__cli__','commitments','insert'),
    ('__cli__','commitments','update'),
    ('__cli__','engine_feedback','insert'),
    ('__cli__','engine_feedback','update'),
    ('__cli__','work_items','insert'),
    ('__cli__','work_items','update'),
    ('__cli__','read_log','insert'),
    ('__cli__','subtraction_log','insert'),
    ('__cli__','agent_runs','insert'),
    ('__cli__','agent_runs','update'),
    ('__cli__','objects','insert');
-- T-12 application: every write goes through `selvedge submit`, which opens a transaction,
-- declares the active role (defaulting to `__cli__` in 079), and verifies role+table+op
-- against this table before INSERT/UPDATE. The trigger enforcement layer is added in 080+
-- when LLM agents become writers; until then, T-12 is application-layer only and the
-- substrate refusal is documented but not active. This is recorded as engine_feedback at
-- close (per D-3 Open: refusals that cannot be implemented at trigger level downgrade with
-- explicit feedback). T-12 is downgraded to application-layer for engine-v17 because
-- SQLite triggers cannot read a connection-scoped session variable to learn the active role
-- without per-table sentinel rows; the application-layer check at `selvedge submit` is
-- equivalent in 079's single-writer regime.

-- ============================================================================
-- read_log: per-agent reads.
-- ============================================================================
CREATE TABLE read_log (
    read_id         INTEGER PRIMARY KEY,
    session_id      INTEGER NOT NULL REFERENCES sessions(session_id),
    agent_run_id    INTEGER REFERENCES agent_runs(agent_run_id),
    object_id       INTEGER REFERENCES objects(object_id),
    note            TEXT,
    read_at         TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
) STRICT;

-- ============================================================================
-- subtraction_log: D-6 human reviewer-subtractor's removals.
-- ============================================================================
CREATE TABLE subtraction_log (
    subtraction_id      INTEGER PRIMARY KEY,
    session_id          INTEGER NOT NULL REFERENCES sessions(session_id),
    target_object_id    INTEGER NOT NULL REFERENCES objects(object_id),
    reason_md           TEXT NOT NULL CHECK (length(reason_md) >= 16),
    subtracted_at       TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
) STRICT;

-- ============================================================================
-- agent_runs: per-LLM-invocation record.
-- ============================================================================
CREATE TABLE agent_runs (
    agent_run_id    INTEGER PRIMARY KEY,
    session_id      INTEGER NOT NULL REFERENCES sessions(session_id),
    role            TEXT NOT NULL,
    model_family    TEXT,
    model_id        TEXT,
    work_item_id    INTEGER REFERENCES work_items(work_item_id),
    started_at      TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    ended_at        TEXT
) STRICT;

-- ============================================================================
-- T-02 + T-11: enforce on UPDATE sessions SET status='closed'.
-- T-02: every substantive decision in the session must have ≥1 alternative.
-- T-11: no work_items in queued/leased/failed for the session.
-- ============================================================================
CREATE TRIGGER t02_close_substantive_decisions_have_alternatives
BEFORE UPDATE OF status ON sessions
FOR EACH ROW
WHEN OLD.status = 'open' AND NEW.status = 'closed'
 AND EXISTS (
    SELECT 1 FROM decisions d
    WHERE d.session_id = NEW.session_id
      AND d.kind = 'substantive'
      AND NOT EXISTS (
          SELECT 1 FROM decision_alternatives a WHERE a.decision_id = d.decision_id
      )
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T02: cannot close session with substantive decisions lacking rejected alternatives');
END;

CREATE TRIGGER t11_close_requires_workitems_clear
BEFORE UPDATE OF status ON sessions
FOR EACH ROW
WHEN OLD.status = 'open' AND NEW.status = 'closed'
 AND EXISTS (
    SELECT 1 FROM work_items w
    WHERE w.session_id = NEW.session_id
      AND w.status IN ('queued','leased','failed')
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T11: cannot close session with in-flight work_items');
END;

-- ============================================================================
-- T-06: closed-session immutability.
-- For each protected table, refuse UPDATE/DELETE when the owning session is closed.
-- decision_alternatives, refs, commitments, synthesis_points: protected via the row's
-- decision_id / source_object_id / deliberation_id chain. perspectives: via deliberation.
-- ============================================================================
CREATE TRIGGER t06_decisions_no_mut_after_close_upd
BEFORE UPDATE ON decisions
FOR EACH ROW
WHEN (SELECT status FROM sessions WHERE session_id = OLD.session_id) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: decision belongs to a closed session');
END;
CREATE TRIGGER t06_decisions_no_mut_after_close_del
BEFORE DELETE ON decisions
FOR EACH ROW
WHEN (SELECT status FROM sessions WHERE session_id = OLD.session_id) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: decision belongs to a closed session');
END;

CREATE TRIGGER t06_alts_no_mut_after_close_upd
BEFORE UPDATE ON decision_alternatives
FOR EACH ROW
WHEN (
    SELECT s.status FROM sessions s
    JOIN decisions d ON d.session_id = s.session_id
    WHERE d.decision_id = OLD.decision_id
) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: alternative belongs to a closed session');
END;
CREATE TRIGGER t06_alts_no_mut_after_close_del
BEFORE DELETE ON decision_alternatives
FOR EACH ROW
WHEN (
    SELECT s.status FROM sessions s
    JOIN decisions d ON d.session_id = s.session_id
    WHERE d.decision_id = OLD.decision_id
) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: alternative belongs to a closed session');
END;

CREATE TRIGGER t06_specv_no_mut_after_close_upd
BEFORE UPDATE ON spec_versions
FOR EACH ROW
WHEN (SELECT status FROM sessions WHERE session_id = OLD.session_id) = 'closed'
 AND NEW.status IS OLD.status  -- supersession edits the row's status; permitted across
                               -- sessions per methodology Preservation. We refuse only
                               -- non-status mutations of a closed-session spec_version row.
                               -- Status flips active→superseded are admitted (a later
                               -- session can supersede a row created in an earlier one).
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: spec_version body belongs to a closed session');
END;
CREATE TRIGGER t06_specv_no_mut_after_close_del
BEFORE DELETE ON spec_versions
FOR EACH ROW
WHEN (SELECT status FROM sessions WHERE session_id = OLD.session_id) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: spec_version belongs to a closed session');
END;

CREATE TRIGGER t06_perspectives_no_mut_after_close_upd
BEFORE UPDATE ON perspectives
FOR EACH ROW
WHEN (
    SELECT s.status FROM sessions s
    JOIN deliberations d ON d.session_id = s.session_id
    WHERE d.deliberation_id = OLD.deliberation_id
) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: perspective belongs to a closed session');
END;
CREATE TRIGGER t06_perspectives_no_mut_after_close_del
BEFORE DELETE ON perspectives
FOR EACH ROW
WHEN (
    SELECT s.status FROM sessions s
    JOIN deliberations d ON d.session_id = s.session_id
    WHERE d.deliberation_id = OLD.deliberation_id
) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: perspective belongs to a closed session');
END;

CREATE TRIGGER t06_synpoints_no_mut_after_close_upd
BEFORE UPDATE ON synthesis_points
FOR EACH ROW
WHEN (
    SELECT s.status FROM sessions s
    JOIN deliberations d ON d.session_id = s.session_id
    WHERE d.deliberation_id = OLD.deliberation_id
) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: synthesis_point belongs to a closed session');
END;
CREATE TRIGGER t06_synpoints_no_mut_after_close_del
BEFORE DELETE ON synthesis_points
FOR EACH ROW
WHEN (
    SELECT s.status FROM sessions s
    JOIN deliberations d ON d.session_id = s.session_id
    WHERE d.deliberation_id = OLD.deliberation_id
) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: synthesis_point belongs to a closed session');
END;

CREATE TRIGGER t06_commitments_no_mut_after_close_upd
BEFORE UPDATE ON commitments
FOR EACH ROW
WHEN (
    SELECT s.status FROM sessions s
    JOIN decisions d ON d.session_id = s.session_id
    WHERE d.decision_id = OLD.decision_id
) = 'closed'
 AND NEW.status IS OLD.status  -- T-09 status transitions across sessions are admitted.
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: commitment belongs to a closed session');
END;

CREATE TRIGGER t06_refs_no_mut_after_close_upd
BEFORE UPDATE ON refs
FOR EACH ROW
WHEN (
    SELECT s.status FROM sessions s
    WHERE s.session_id = (
        SELECT CASE o.object_kind
            WHEN 'decision' THEN (SELECT session_id FROM decisions WHERE decision_id = o.typed_row_id)
            WHEN 'spec_version' THEN (SELECT session_id FROM spec_versions WHERE spec_version_id = o.typed_row_id)
            WHEN 'perspective' THEN (
                SELECT d.session_id FROM perspectives p
                JOIN deliberations d ON d.deliberation_id = p.deliberation_id
                WHERE p.perspective_id = o.typed_row_id
            )
            WHEN 'commitment' THEN (
                SELECT d.session_id FROM commitments c
                JOIN decisions d ON d.decision_id = c.decision_id
                WHERE c.commitment_id = o.typed_row_id
            )
            WHEN 'engine_feedback' THEN (SELECT session_id FROM engine_feedback WHERE feedback_id = o.typed_row_id)
            ELSE NULL
        END
        FROM objects o WHERE o.object_id = OLD.source_object_id
    )
) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: ref belongs to a closed session');
END;
CREATE TRIGGER t06_refs_no_mut_after_close_del
BEFORE DELETE ON refs
FOR EACH ROW
WHEN (
    SELECT s.status FROM sessions s
    WHERE s.session_id = (
        SELECT CASE o.object_kind
            WHEN 'decision' THEN (SELECT session_id FROM decisions WHERE decision_id = o.typed_row_id)
            WHEN 'spec_version' THEN (SELECT session_id FROM spec_versions WHERE spec_version_id = o.typed_row_id)
            WHEN 'perspective' THEN (
                SELECT d.session_id FROM perspectives p
                JOIN deliberations d ON d.deliberation_id = p.deliberation_id
                WHERE p.perspective_id = o.typed_row_id
            )
            ELSE NULL
        END
        FROM objects o WHERE o.object_id = OLD.source_object_id
    )
) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: ref belongs to a closed session');
END;

-- objects rows themselves are not subject to T-06 mutation refusal because objects is a
-- pure identity table; deleting an object would orphan typed rows and is independently
-- prevented by FK references from refs.

-- Record the migration.
INSERT INTO schema_migrations (name, sha256) VALUES ('001-initial.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
