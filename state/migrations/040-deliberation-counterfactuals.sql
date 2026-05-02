-- Migration 040: deliberation_counterfactuals typed substrate primitive (T-36, engine-v49 to v50).
--
-- Why:
--   DV-S180-1 graduates seal-grade out of engine_feedback prefix-prose into
--   a typed substrate kind. D-29 cross-family deliberation (P-1 anthropic
--   architect + P-2 openai-codex + P-3 anthropic adversary + P-4 anthropic
--   coherence) converged on C-1 graduate-to-typed (with M-1 P-3 ship-nothing
--   preserved as minority) under operator-named-mandate at S180-open
--   ("constraints without compromise") + mid-deliberation ("use triggers and
--   types deterministically; can be expanded later with more types"). DV-S109-1
--   ceremony-subtraction operator-precluded as rejection basis per the same
--   §1.5 admissibility lineage used at DV-S171-1 + DV-S176-1.
--
--   D-1 divergence single-table (P-1 adopted) vs obligations+items (P-2) vs
--   synthesis_points enum (P-4): single dedicated table chosen at v1; P-2's
--   obligations meta-table preserved as forward-direction if a second
--   mandated synthesis artefact graduates; P-4's UNION-view across stance-
--   space surfaces preserved as forward-direction. D-2 universal-mandatory
--   (P-1 adopted) vs conditional-by-kind (P-2): operator directive limit-
--   what-an-agent-can-do favors universal with cheap nil-attestation absorb-
--   ing tactical-seal refusal-debt per §8.5 audit-step:0 precedent.
--
-- Schema:
--   deliberation_counterfactuals             INTEGER PRIMARY KEY
--     One row per counterfactual under one deliberation; UNIQUE(deliberation_id,
--     seq) gives an ordered inventory; row count IS the seal-grade count
--     (substrate-derivable per C-5; replaces narrated 'seal-grade: <count>'
--     headline in EF body).
--   deliberation_counterfactuals.deliberation_id  FK CASCADE
--     Counterfactual rows cascade with their parent deliberation; the FK is
--     the substrate-traceable parent link the engine_feedback prefix-row
--     never had (NULL-FK shape T-34/T-35 just hardened against).
--   deliberation_counterfactuals.session_id       FK
--     Denormalised for query speed and t06 mutation-after-close enforcement.
--   deliberation_counterfactuals.seq              INTEGER >= 1
--     Author-ordered seq starting at 1; UNIQUE(deliberation_id, seq).
--   deliberation_counterfactuals.position         TEXT 8..240
--     The position no perspective took; atom-rules enforced via direct CHECK
--     (no newlines / no carriage return / no fenced code / no pipe table).
--   deliberation_counterfactuals.why              TEXT 8..240
--     Why the position would change the synthesis if adopted; same atom-rules.
--   deliberation_counterfactuals.disposition      TEXT enum CHECK
--     Three values mirror the prior prose-prefix clause:
--       addressed-in-synthesis  -- synthesis text already covers the alternative
--       deferred-to-FR          -- FR row warrants future revisit
--       nilled-by-exclusion     -- position acknowledged but excluded
--   deliberation_counterfactuals.disposition_note TEXT NULL 8..240
--     Synthesis_md anchor when disposition=addressed-in-synthesis; FR alias
--     (e.g. 'FR-S180-1') when disposition=deferred-to-FR; NULL when
--     disposition=nilled-by-exclusion (exclusion_kind carries the rationale).
--     Text-not-FK because FR aliases live in forward_reference_dispositions
--     not objects per §5 cite-typing rule (T-34 refuses NULL FK on cite
--     slots; we sidestep by keeping disposition_note as text reference).
--   deliberation_counterfactuals.exclusion_kind   TEXT NULL enum CHECK
--     Four values when disposition=nilled-by-exclusion:
--       preserved-as-divergence -- already a synthesis_points {divergence,minority} row
--       barred-by-constraint    -- recorded constraint/prior-decision/spec-clause cited at convening
--       micro-decision          -- wording/ordering/naming variant
--       out-of-scope            -- foreclosed by deliberation scope at convening
--   deliberation_counterfactuals.nil_attestation  INTEGER 0|1 default 0
--     When 1: seq=1, disposition=nilled-by-exclusion, exclusion_kind populated;
--     encodes 'seal-grade: 0 -- exclusions applied: <which>' as one substrate
--     row (cheap-exit per C-6, mirrors §8.5 audit-step:0 precedent).
--   deliberation_counterfactuals.created_at       TEXT default CURRENT
--   UNIQUE(deliberation_id, seq)
--     One ordered inventory per deliberation; idempotent under retry.
--
-- T-36 substrate-gate (engine-v50):
--   BEFORE UPDATE OF sealed_at ON deliberations: refuses the seal transition
--   (NULL -> non-NULL) when COUNT(deliberation_counterfactuals WHERE
--   deliberation_id=NEW.deliberation_id) = 0. Refusal text names the cheap-
--   exit recipe so an agent who hits the refusal can recover with one submit.
--
-- T-13 immutability after seal:
--   BEFORE INSERT ON deliberation_counterfactuals: refuses inserts on a
--   deliberation already sealed. Counterfactuals must precede seal; this
--   mirrors synthesis_points / perspectives ordering discipline.
--
-- T-06 mutation-after-close protection:
--   BEFORE UPDATE / DELETE: refuses if parent session is closed.
--
-- Forward-only per DV-S176-1 C-4: no auto-backfill of 8 historical seal-grade
-- engine_feedback rows; they remain as legacy evidence per methodology
-- §Preservation. C-8 convergence (P-1, P-2, P-3 all explicit on no-backfill).

PRAGMA foreign_keys = OFF;

BEGIN;

CREATE TABLE deliberation_counterfactuals (
    counterfactual_id INTEGER PRIMARY KEY AUTOINCREMENT,
    deliberation_id   INTEGER NOT NULL REFERENCES deliberations(deliberation_id) ON DELETE CASCADE,
    session_id        INTEGER NOT NULL REFERENCES sessions(session_id),
    seq               INTEGER NOT NULL CHECK (seq >= 1),
    position          TEXT NOT NULL,
    why               TEXT NOT NULL,
    disposition       TEXT NOT NULL CHECK (disposition IN (
                          'addressed-in-synthesis','deferred-to-FR','nilled-by-exclusion'
                      )),
    disposition_note  TEXT,
    exclusion_kind    TEXT CHECK (exclusion_kind IS NULL OR exclusion_kind IN (
                          'preserved-as-divergence','barred-by-constraint','micro-decision','out-of-scope'
                      )),
    nil_attestation   INTEGER NOT NULL DEFAULT 0 CHECK (nil_attestation IN (0,1)),
    created_at        TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),

    UNIQUE(deliberation_id, seq),

    -- Atom-rules on text columns: 8..240 chars, no newline, no CR, no fenced code, no pipe-table.
    CHECK (length(position) BETWEEN 8 AND 240),
    CHECK (instr(position, char(10)) = 0),
    CHECK (instr(position, char(13)) = 0),
    CHECK (position NOT GLOB '*```*'),
    CHECK (position NOT GLOB '*|*|*'),
    CHECK (length(why) BETWEEN 8 AND 240),
    CHECK (instr(why, char(10)) = 0),
    CHECK (instr(why, char(13)) = 0),
    CHECK (why NOT GLOB '*```*'),
    CHECK (why NOT GLOB '*|*|*'),
    CHECK (disposition_note IS NULL OR length(disposition_note) BETWEEN 8 AND 240),
    CHECK (disposition_note IS NULL OR instr(disposition_note, char(10)) = 0),
    CHECK (disposition_note IS NULL OR instr(disposition_note, char(13)) = 0),
    CHECK (disposition_note IS NULL OR disposition_note NOT GLOB '*```*'),
    CHECK (disposition_note IS NULL OR disposition_note NOT GLOB '*|*|*'),

    -- Disposition-conditional NOT-NULL guards.
    CHECK (disposition <> 'addressed-in-synthesis' OR disposition_note IS NOT NULL),
    CHECK (disposition <> 'deferred-to-FR' OR disposition_note IS NOT NULL),
    CHECK (disposition <> 'nilled-by-exclusion' OR exclusion_kind IS NOT NULL),

    -- nil_attestation=1 ⇒ seq=1 AND disposition=nilled-by-exclusion AND exclusion_kind populated.
    CHECK (nil_attestation = 0 OR (seq = 1 AND disposition = 'nilled-by-exclusion' AND exclusion_kind IS NOT NULL))
) STRICT;

CREATE INDEX idx_deliberation_counterfactuals_delib ON deliberation_counterfactuals(deliberation_id, seq);
CREATE INDEX idx_deliberation_counterfactuals_session ON deliberation_counterfactuals(session_id);

-- T-36: BEFORE UPDATE OF sealed_at on deliberations.
CREATE TRIGGER t36_deliberation_seal_requires_counterfactual
BEFORE UPDATE OF sealed_at ON deliberations
FOR EACH ROW
WHEN OLD.sealed_at IS NULL AND NEW.sealed_at IS NOT NULL
     AND (SELECT COUNT(*) FROM deliberation_counterfactuals WHERE deliberation_id = NEW.deliberation_id) = 0
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T36: deliberation has zero deliberation_counterfactuals rows; author at least one via `bin/selvedge submit deliberation-counterfactual` (or one nil_attestation=1 row with exclusion_kind populated as cheap-exit per DV-S180-1) before deliberation-seal');
END;

-- T-13: counterfactuals must precede seal (mirror synthesis_points / perspectives ordering).
CREATE TRIGGER t13_deliberation_counterfactuals_no_insert_after_seal
BEFORE INSERT ON deliberation_counterfactuals
FOR EACH ROW
WHEN EXISTS (SELECT 1 FROM deliberations WHERE deliberation_id = NEW.deliberation_id AND sealed_at IS NOT NULL)
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T13: parent deliberation already sealed; counterfactuals must be authored before deliberation-seal');
END;

-- T-06: mutation-after-close protection on parent session.
CREATE TRIGGER t06_deliberation_counterfactuals_no_mut_after_close_del
BEFORE DELETE ON deliberation_counterfactuals
FOR EACH ROW
WHEN EXISTS (SELECT 1 FROM sessions WHERE session_id = OLD.session_id AND status = 'closed')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: deliberation_counterfactual belongs to a closed session');
END;

CREATE TRIGGER t06_deliberation_counterfactuals_no_mut_after_close_upd
BEFORE UPDATE ON deliberation_counterfactuals
FOR EACH ROW
WHEN EXISTS (SELECT 1 FROM sessions WHERE session_id = OLD.session_id AND status = 'closed')
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: deliberation_counterfactual belongs to a closed session');
END;

INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES ('__cli__', 'deliberation_counterfactuals', 'insert');

UPDATE workspace_metadata SET value = 'engine-v50' WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('040-deliberation-counterfactuals.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
