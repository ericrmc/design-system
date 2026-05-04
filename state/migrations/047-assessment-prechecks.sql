-- Migration 047: assessment_prechecks substrate-side gate at assessment-submit.
--
-- Sealed at S195 DV-S195-1 per operator-named-mandate at S194-close: orient
-- was wrong location for context-surfacing (S194 mistake); agents skim orient
-- under context pressure; relocate to assessment-time as substrate-enforced
-- T-38 refusal. Mirrors T-33 decision-record precheck shape (engine-v49,
-- migration 035) but at assessment-submit. Single-use atomic-consume + sha256-
-- over-rendered-pack-content (not current substrate state per codex caution
-- harmless-substrate-drift would invalidate receipts).
--
-- Operator-named at S194-close (precluding wait-for-evidence per DV-S190-2
-- M-2 watch-FR-graduation pattern): "we are 194 sessions in and agents will
-- not do things correctly. the wait-for-evidence approach is no longer
-- appropriate; the provenance is millions of words long before I mandated
-- the substrate layer be used, and added more types and checks. ... we want
-- triggers that return data to them before they start deliberating. we want
-- to show them the context at assessment time, not orient time. ... it
-- should be looking at a light orient, finding the next useful item,
-- getting context related to it by reading or chain-walks, then starting
-- the session in earnest."
--
-- All-kinds-gate (no kind=meta admit-zero): codex shape-consult per EF-S195-1
-- noted triage-only meta sessions still modify durable state via FR/EF
-- dispositions and substrate writes; gate every kind that opens an assessment
-- per operator substrate-friction-is-the-point principle.
--
-- Substrate-presented (not operator-curated): operator-named at S194-close
-- "the substrate is not frictionless and agents tend to avoid using it";
-- bin/selvedge context defaults to undisposed FRs + open HIGH OIs as the
-- substrate-presented floor; agents may narrow with --target but the floor
-- is mandatory and auto-generated.
--
-- Bootstrap-by-ordering: S195 own assessment-submit happens BEFORE this
-- migration applies (open + assessment + DV-S195-1 + implement + migrate
-- + close); T-38 fires from S196 onward. Codex caution: avoid hardcoded
-- session-id exemption; ordering suffices.
--
-- Schema mirrors decision_prechecks at engine-v49 (migration 035) plus
-- targets_json column carrying the JSON array of target aliases the agent
-- enumerated when running bin/selvedge context. The pack content at
-- precheck-time is hashed once; submit-time verification recomputes against
-- the stored pack-content if needed (not against current substrate state).

PRAGMA foreign_keys = OFF;

BEGIN;

CREATE TABLE assessment_prechecks (
    precheck_id        INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id         INTEGER NOT NULL REFERENCES sessions(session_id),
    targets_json       TEXT    NOT NULL CHECK (length(targets_json) >= 2),
    context_sha256     TEXT    NOT NULL CHECK (length(context_sha256) = 64),
    context_md         TEXT    NOT NULL CHECK (length(context_md) >= 8),
    nonce              TEXT    NOT NULL CHECK (length(nonce) BETWEEN 16 AND 64),
    ttl_seconds        INTEGER NOT NULL DEFAULT 1800 CHECK (ttl_seconds BETWEEN 30 AND 3600),
    walker_version     TEXT    NOT NULL CHECK (length(walker_version) >= 1),
    created_at         TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    consumed_at        TEXT,
    consumed_by_assessment_id INTEGER REFERENCES assessments(assessment_id),

    UNIQUE(session_id, nonce)
) STRICT;

CREATE INDEX idx_assessment_prechecks_session ON assessment_prechecks(session_id);
CREATE INDEX idx_assessment_prechecks_nonce ON assessment_prechecks(nonce);

INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES ('__cli__', 'assessment_prechecks', 'insert');
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES ('__cli__', 'assessment_prechecks', 'update');

INSERT INTO schema_migrations (name, sha256) VALUES ('047-assessment-prechecks.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
