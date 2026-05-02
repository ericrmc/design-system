-- Migration 035: decision_prechecks substrate-gate (T-33, engine-v48 to v49).
--
-- Why:
--   D-28 operator-named-mandate at S179-open: SHOW CONTEXT AT RIGHT TIMES,
--   LIMIT ENTRY, FORCE CHECKS BEFORE DECISIONS ARE MADE. The synthesis
--   adopted the substrate-detectable subset: receipt-pattern table
--   recording the agent's exposure to relevant context (similar OIs,
--   prior decisions targeting the same key, active spec clauses,
--   recent supersedes), with handler-side gate refusing decision-record
--   submit when no fresh, target-matched, single-use, hash-verified
--   precheck row exists.
--
--   Cross-family convergence (P-2 codex + P-4 codex): cognition is not
--   substrate-detectable; only freshness, target match, pack coverage,
--   single-use consumption are. P-4 single-use-nonce closes the
--   fire-and-forget gaming pattern timestamp-window predicates admit.
--   P-2 decision_precheck_sources child table makes consumption
--   observable per source (each surfaced object alias gets its own
--   digest).
--
--   D-28 C-1 four-way convergence + DV-S176-1 receipt-pattern precedent:
--   precheck row + sha256 + handler dispatch in-band inside same write_tx
--   matches the chain-walk shape proven at T-32.
--
-- Schema:
--   decision_prechecks                                 INTEGER PRIMARY KEY
--     One row per (session, target_kind, target_key, nonce). Receipt of
--     the agent's exposure to the precheck output for a specific target.
--   decision_prechecks.session_id                      FK NOT NULL
--     Receipt scoped to the open session. Cross-session reuse refused.
--   decision_prechecks.target_kind                     TEXT enum CHECK
--     decision_v2 only at engine-v49; future kinds may admit (perspective,
--     issue, spec-version) via migration NN-CALIBRATED widening.
--   decision_prechecks.target_key                      TEXT non-empty
--     Free-form key naming the decision-record target. Convention:
--     match the decision_v2.title prefix or target_descriptor.
--   decision_prechecks.context_sha256                  TEXT length=64 CHECK
--     SHA-256 of the rendered context body. Decision-record submit
--     handler recomputes and compares; mismatch => E_REFUSAL_T33.
--   decision_prechecks.nonce                           TEXT length 16..64
--     Single-use nonce generated at precheck-write-time. Decision-record
--     submit handler matches against payload.precheck_nonce and consumes
--     the row inside same write_tx.
--   decision_prechecks.ttl_seconds                     INTEGER 30..3600
--     TTL bound. Default 1800 seconds (30 min). Submit handler refuses
--     if (now - created_at) > ttl_seconds.
--   decision_prechecks.walker_version                  TEXT non-empty
--     Precheck logic version stamp for forward-compat.
--   decision_prechecks.created_at                      TEXT default
--   decision_prechecks.consumed_at                     TEXT NULL
--     Set when single-use consumption occurs. NULL until consumed.
--   decision_prechecks.consumed_by_decision_v2_id      INTEGER NULL FK
--     References the decision_v2 row that consumed this precheck. NULL
--     until consumed.
--   UNIQUE(session_id, target_kind, target_key, nonce)
--
--   decision_precheck_sources                          INTEGER PRIMARY KEY
--     P-2 codex contribution: per-source row inside the precheck pack.
--   decision_precheck_sources.precheck_id              FK NOT NULL CASCADE
--   decision_precheck_sources.ord                      INTEGER >= 0
--     Ordering within the pack for deterministic re-render.
--   decision_precheck_sources.source_kind              TEXT non-empty
--     Free-form (similar_oi | prior_dv | active_clause | recent_supersede
--     | sealed_deliberation, others as walker grows). Open enum at v49.
--   decision_precheck_sources.source_alias             TEXT NULL
--     Cited alias when the source has one. NULL admitted for sources
--     without an alias.
--   decision_precheck_sources.source_object_id         INTEGER NULL FK objects
--   decision_precheck_sources.relation                 TEXT NULL
--     Relation kind (cites, supersedes, opens-issue, etc.) when the source
--     is itself a graph edge.
--   decision_precheck_sources.digest                   TEXT length=64 CHECK
--     SHA-256 of the rendered source row. Aggregate digest is in
--     decision_prechecks.context_sha256.
--
-- T-33 handler-enforced refusal (engine-v49):
--   _submit_decision_v2 reads payload['precheck_nonce']. If kind in
--   ('substantive','schema_migration'), the precheck is mandatory:
--     - SELECT decision_prechecks WHERE session_id=current AND nonce=submitted
--     - Validate ttl, target_kind, target_key match.
--     - Recompute context_sha256 from current state; compare.
--     - UPDATE consumed_at=now, consumed_by_decision_v2_id=did atomically.
--   Refuses E_REFUSAL_T33 on any mismatch with refusal-text naming the
--   exact failure (stale | nonce-not-found | already-consumed | target-
--   mismatched | hash-mismatch).
--   Kind-aware admit predicate (synthesis EF-S179-1 CF-2): kind in
--   ('procedural','calibration','disposition') admits zero-precheck like
--   T-32 admits zero-cite, mirroring the audit-step:0 carve-out for
--   bookkeeping submits. The carve-out is preserved for symmetry.
--
-- T-15 compliance:
--   Additive only — CREATE TABLE, CREATE INDEX, INSERT into
--   role_write_capabilities, UPDATE workspace_metadata. No DROP, no
--   ALTER, no CHECK relaxation. No T-15-CALIBRATED block needed.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TABLE decision_prechecks (
    precheck_id INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id INTEGER NOT NULL REFERENCES sessions(session_id),
    target_kind TEXT NOT NULL CHECK (target_kind IN ('decision_v2')),
    target_key TEXT NOT NULL CHECK (length(target_key) > 0),
    context_sha256 TEXT NOT NULL CHECK (length(context_sha256) = 64),
    nonce TEXT NOT NULL CHECK (length(nonce) BETWEEN 16 AND 64),
    ttl_seconds INTEGER NOT NULL DEFAULT 1800 CHECK (ttl_seconds BETWEEN 30 AND 3600),
    walker_version TEXT NOT NULL CHECK (length(walker_version) > 0),
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    consumed_at TEXT,
    consumed_by_decision_v2_id INTEGER REFERENCES decisions_v2(decision_v2_id),
    UNIQUE(session_id, target_kind, target_key, nonce)
);

CREATE INDEX idx_decision_prechecks_session ON decision_prechecks(session_id);
CREATE INDEX idx_decision_prechecks_nonce ON decision_prechecks(nonce);
CREATE INDEX idx_decision_prechecks_target ON decision_prechecks(target_kind, target_key);

CREATE TABLE decision_precheck_sources (
    source_id INTEGER PRIMARY KEY AUTOINCREMENT,
    precheck_id INTEGER NOT NULL REFERENCES decision_prechecks(precheck_id) ON DELETE CASCADE,
    ord INTEGER NOT NULL CHECK (ord >= 0),
    source_kind TEXT NOT NULL CHECK (length(source_kind) > 0),
    source_alias TEXT,
    source_object_id INTEGER REFERENCES objects(object_id),
    relation TEXT,
    digest TEXT NOT NULL CHECK (length(digest) = 64),
    UNIQUE(precheck_id, ord)
);

CREATE INDEX idx_decision_precheck_sources_precheck ON decision_precheck_sources(precheck_id);

INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES ('__cli__', 'decision_prechecks', 'insert');
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES ('__cli__', 'decision_prechecks', 'update');
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES ('__cli__', 'decision_precheck_sources', 'insert');

UPDATE workspace_metadata SET value='engine-v49' WHERE key='current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('035-decision-prechecks-substrate-gate.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
