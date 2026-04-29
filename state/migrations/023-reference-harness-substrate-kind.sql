-- Migration 023: reference_harness substrate kind (workspace-experimental).
-- engine-v34 → engine-v35 (S125 closing OI-S124-2 per DV-S124-2).
--
-- Why:
--   S124 D-2 commissioned reference_harness as a workspace-experimental
--   substrate kind for the disaster-response arc stage-2-onward pilot. Per
--   the synthesis (S-C: subtract now, pilot harness, defer kernel-promote),
--   the methodology kernel was kept at two validation senses (workspace +
--   domain) in v6; the harness is a substrate-row mechanism the disaster-
--   response arc uses to surface empirical material on validation-without-
--   domain-actor (S106 commission). Kernel-promotion of harness to a third
--   sense is deferred to arc-close evaluation (OI-S124-1).
--
-- Schema (P-4 schema with P-2 epistemic guardrails baked in):
--
--   reference_harnesses                — one row per harness
--     - alias RH-S<NNN>-<seq> (T-34 GLOB-format)
--     - arc_slug + stage_n locate the harness on an external arc/stage
--     - absence_declaration_atom_id NOT NULL: P-2 guardrail. Every harness
--       row carries an explicit declaration of why no domain-actor is
--       available; absence is articulated, not implicit. There is no
--       boolean flag to flip — the declaration text is the substrate
--       evidence.
--     - expiry_sessions: session-distance after which harness must be
--       replayed if the artefact remains active (P-4 expiry field)
--     - status enum: open | sealed | expired | reopened
--       T-33 enforces transitions: open→sealed, sealed→{expired,reopened}.
--       Open admits sub-table writes; sealed freezes them (T-32).
--
--   reference_harness_targets         — target_artifacts (P-4)
--   reference_harness_claims          — claim_set (P-4); load_bearing flag
--                                       distinguishes claims that block
--                                       progression on broken result vs
--                                       claims that merely emit issues
--   reference_harness_stresses        — stress_protocols (P-4) with
--                                       protocol_kind ∈ {constraint_replay,
--                                       counterfactual, adversarial} per
--                                       P-4 cli_surface
--   reference_harness_results         — claim-level results (P-4 results)
--                                       enum: survived | strained | broken
--                                       | untestable | deferred. THERE IS
--                                       NO domain_validated VALUE — this
--                                       CHECK constraint is the structural
--                                       expression of P-2's epistemic
--                                       guardrail: a passing harness can
--                                       never upgrade an artefact to
--                                       domain-validated status because
--                                       that label cannot be written.
--   reference_harness_dissent         — dissent_trace (P-4) preserves
--                                       minority surrogate objections
--   reference_harness_triggers        — falsification_triggers (P-4):
--                                       later facts/changes that auto-
--                                       reopen; fired_at + reopened_session_id
--                                       record the reopen event when fired.
--
-- Triggers added:
--   T-32: refuse INSERT on each harness sub-table when parent harness
--         status != 'open' (seal-immutability).
--   T-33: refuse harness status transitions other than the lifecycle
--         (open→sealed, sealed→{expired,reopened}).
--   T-34: refuse harness alias not matching RH-SNNN-N format.
--
-- Scope deferred to a follow-up issue:
--   bin/selvedge harness {create,replay,stress,expire,triggers,summarize}
--   convenience verbs (P-4 cli_surface). Substrate-first discipline: the
--   submit handlers are the canonical write surface; CLI sugar can come
--   later if the pilot demonstrates it pays for itself.
--
-- Engine version bump rationale:
--   New substrate kind expands the workspace's vocabulary; current_engine_version
--   bumps from v34 to v35 so any session opened after this migration
--   records its engine-version-at-open coherently. workspace-experimental
--   scope (NOT yet kernel) means methodology.md is not amended; the bump
--   tracks the substrate addition only.
--
-- T-15 compliance: this migration adds new tables, indexes, and triggers
-- only. No DROP TABLE, DROP COLUMN, ALTER TABLE … DROP, no widening of
-- existing CHECK constraints. No T-15-CALIBRATED block needed.

PRAGMA foreign_keys = ON;

BEGIN;

-- ============================================================================
-- 1. reference_harnesses: one row per harness.
-- ============================================================================
CREATE TABLE reference_harnesses (
    harness_id                    INTEGER PRIMARY KEY,
    alias                         TEXT NOT NULL UNIQUE,
    session_id                    INTEGER NOT NULL REFERENCES sessions(session_id),
    arc_slug                      TEXT NOT NULL CHECK (length(arc_slug) BETWEEN 2 AND 120),
    stage_n                       INTEGER NOT NULL CHECK (stage_n >= 1),
    absence_declaration_atom_id   INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    expiry_sessions               INTEGER NOT NULL CHECK (expiry_sessions >= 1),
    status                        TEXT NOT NULL DEFAULT 'open' CHECK (status IN (
                                      'open','sealed','expired','reopened'
                                  )),
    sealed_at                     TEXT,
    sealed_session_id             INTEGER REFERENCES sessions(session_id),
    expired_at                    TEXT,
    reopened_session_id           INTEGER REFERENCES sessions(session_id),
    created_at                    TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    object_id                     INTEGER REFERENCES objects(object_id),
    CHECK (
        (status = 'open' AND sealed_at IS NULL AND sealed_session_id IS NULL)
        OR (status IN ('sealed','expired','reopened')
            AND sealed_at IS NOT NULL
            AND sealed_session_id IS NOT NULL)
    )
) STRICT;

CREATE INDEX idx_reference_harnesses_session ON reference_harnesses(session_id);
CREATE INDEX idx_reference_harnesses_arc ON reference_harnesses(arc_slug, stage_n);
CREATE INDEX idx_reference_harnesses_status ON reference_harnesses(status);

-- T-34: alias format. RH-S<NNN>-<seq> (NNN is 3+ digits per workspace_session_no).
CREATE TRIGGER t34_reference_harnesses_alias_format
BEFORE INSERT ON reference_harnesses
FOR EACH ROW
WHEN NOT (NEW.alias GLOB 'RH-S[0-9][0-9][0-9]-[0-9]*'
         OR NEW.alias GLOB 'RH-S[0-9][0-9][0-9][0-9]-[0-9]*')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T34: reference_harnesses.alias must match RH-SNNN-N (3 or 4 digit session number)');
END;

-- T-33: status lifecycle.
--   open → sealed (harness-seal handler)
--   sealed → expired (expiry CLI / scheduled task)
--   sealed → reopened (falsification trigger fires)
-- All other transitions refused.
CREATE TRIGGER t33_reference_harnesses_status_transitions
BEFORE UPDATE OF status ON reference_harnesses
FOR EACH ROW
WHEN OLD.status != NEW.status
 AND NOT (
    (OLD.status = 'open'   AND NEW.status = 'sealed')
    OR (OLD.status = 'sealed' AND NEW.status IN ('expired','reopened'))
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T33: invalid reference_harness status transition (admitted: open->sealed, sealed->expired, sealed->reopened)');
END;

-- ============================================================================
-- 2. reference_harness_targets: target_artifacts list.
-- ============================================================================
CREATE TABLE reference_harness_targets (
    target_id           INTEGER PRIMARY KEY,
    harness_id          INTEGER NOT NULL REFERENCES reference_harnesses(harness_id),
    ord                 INTEGER NOT NULL,
    descriptor_atom_id  INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    artifact_path       TEXT,
    artifact_sha256     TEXT CHECK (artifact_sha256 IS NULL OR length(artifact_sha256) = 64),
    UNIQUE (harness_id, ord)
) STRICT;

CREATE INDEX idx_reference_harness_targets_harness ON reference_harness_targets(harness_id, ord);

-- T-32a: targets sealed after harness seal.
CREATE TRIGGER t32_reference_harness_targets_seal_immutable
BEFORE INSERT ON reference_harness_targets
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_targets cannot be added after harness seal');
END;

-- ============================================================================
-- 3. reference_harness_claims: claim_set list with load_bearing flag.
-- ============================================================================
CREATE TABLE reference_harness_claims (
    claim_id                   INTEGER PRIMARY KEY,
    harness_id                 INTEGER NOT NULL REFERENCES reference_harnesses(harness_id),
    ord                        INTEGER NOT NULL,
    claim_atom_id              INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    world_constraint_atom_id   INTEGER REFERENCES text_atoms(atom_id),
    surrogate_frame_atom_id    INTEGER REFERENCES text_atoms(atom_id),
    load_bearing               INTEGER NOT NULL DEFAULT 0 CHECK (load_bearing IN (0,1)),
    UNIQUE (harness_id, ord)
) STRICT;

CREATE INDEX idx_reference_harness_claims_harness ON reference_harness_claims(harness_id, ord);

CREATE TRIGGER t32_reference_harness_claims_seal_immutable
BEFORE INSERT ON reference_harness_claims
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_claims cannot be added after harness seal');
END;

-- ============================================================================
-- 4. reference_harness_stresses: stress_protocols.
-- ============================================================================
CREATE TABLE reference_harness_stresses (
    stress_id            INTEGER PRIMARY KEY,
    harness_id           INTEGER NOT NULL REFERENCES reference_harnesses(harness_id),
    ord                  INTEGER NOT NULL,
    protocol_kind        TEXT NOT NULL CHECK (protocol_kind IN (
                            'constraint_replay','counterfactual','adversarial'
                         )),
    description_atom_id  INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    UNIQUE (harness_id, ord)
) STRICT;

CREATE INDEX idx_reference_harness_stresses_harness ON reference_harness_stresses(harness_id, ord);

CREATE TRIGGER t32_reference_harness_stresses_seal_immutable
BEFORE INSERT ON reference_harness_stresses
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_stresses cannot be added after harness seal');
END;

-- ============================================================================
-- 5. reference_harness_results: claim-level results. P-2 GUARDRAIL HERE.
-- ============================================================================
--
-- The CHECK enum admits exactly five values. There is no `domain_validated`
-- — that absence is the structural expression of P-2's epistemic guardrail:
-- a passing harness cannot upgrade the targeted artefact to domain-validated
-- status because the label cannot be written into the substrate.
--
-- One result per claim (UNIQUE on claim_id). Re-running stress against a
-- claim requires a new harness (or a reopened one) per the lifecycle.
CREATE TABLE reference_harness_results (
    result_id          INTEGER PRIMARY KEY,
    claim_id           INTEGER NOT NULL UNIQUE REFERENCES reference_harness_claims(claim_id),
    result             TEXT NOT NULL CHECK (result IN (
                          'survived','strained','broken','untestable','deferred'
                       )),
    evidence_atom_id   INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    recorded_at        TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now'))
) STRICT;

CREATE INDEX idx_reference_harness_results_claim ON reference_harness_results(claim_id);

-- T-32d: results are recorded only while the parent harness is open.
CREATE TRIGGER t32_reference_harness_results_seal_immutable
BEFORE INSERT ON reference_harness_results
FOR EACH ROW
WHEN (
    SELECT rh.status
      FROM reference_harnesses rh
      JOIN reference_harness_claims rc ON rc.harness_id = rh.harness_id
     WHERE rc.claim_id = NEW.claim_id
) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_results cannot be added after harness seal');
END;

-- ============================================================================
-- 6. reference_harness_dissent: minority surrogate objections.
-- ============================================================================
CREATE TABLE reference_harness_dissent (
    dissent_id        INTEGER PRIMARY KEY,
    harness_id        INTEGER NOT NULL REFERENCES reference_harnesses(harness_id),
    ord               INTEGER NOT NULL,
    dissent_atom_id   INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    source_claim_id   INTEGER REFERENCES reference_harness_claims(claim_id),
    UNIQUE (harness_id, ord)
) STRICT;

CREATE INDEX idx_reference_harness_dissent_harness ON reference_harness_dissent(harness_id, ord);

CREATE TRIGGER t32_reference_harness_dissent_seal_immutable
BEFORE INSERT ON reference_harness_dissent
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_dissent cannot be added after harness seal');
END;

-- ============================================================================
-- 7. reference_harness_triggers: falsification_triggers.
-- ============================================================================
--
-- Each trigger names a later fact/change that auto-reopens the harness when
-- it fires. The fired_at + reopened_session_id columns record the reopen
-- event. Triggers themselves can only be added during the open phase
-- (T-32); firing a trigger (UPDATE setting fired_at) is admitted on a
-- sealed harness because that's how reopen happens.
CREATE TABLE reference_harness_triggers (
    trigger_id            INTEGER PRIMARY KEY,
    harness_id            INTEGER NOT NULL REFERENCES reference_harnesses(harness_id),
    ord                   INTEGER NOT NULL,
    trigger_atom_id       INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    fired_at              TEXT,
    reopened_session_id   INTEGER REFERENCES sessions(session_id),
    UNIQUE (harness_id, ord),
    CHECK (
        (fired_at IS NULL AND reopened_session_id IS NULL)
        OR (fired_at IS NOT NULL AND reopened_session_id IS NOT NULL)
    )
) STRICT;

CREATE INDEX idx_reference_harness_triggers_harness ON reference_harness_triggers(harness_id, ord);

CREATE TRIGGER t32_reference_harness_triggers_seal_immutable
BEFORE INSERT ON reference_harness_triggers
FOR EACH ROW
WHEN (SELECT status FROM reference_harnesses WHERE harness_id = NEW.harness_id) != 'open'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T32: reference_harness_triggers cannot be added after harness seal');
END;

-- ============================================================================
-- 8. role_write_capabilities: admit __cli__ writes on the new tables.
-- ============================================================================
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','reference_harnesses','insert'),
    ('__cli__','reference_harnesses','update'),
    ('__cli__','reference_harness_targets','insert'),
    ('__cli__','reference_harness_claims','insert'),
    ('__cli__','reference_harness_stresses','insert'),
    ('__cli__','reference_harness_results','insert'),
    ('__cli__','reference_harness_dissent','insert'),
    ('__cli__','reference_harness_triggers','insert'),
    ('__cli__','reference_harness_triggers','update');

-- ============================================================================
-- 9. Engine version bump.
-- ============================================================================
UPDATE workspace_metadata
   SET value = 'engine-v35'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('023-reference-harness-substrate-kind.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
