-- Migration 051: assumption-ledger closure_shape v1.
--
-- engine-v55 -> engine-v56 (S201 DV-S201-1 closes OI-S196-3 by-mechanism).
--
-- Why:
--   OI-S196-3 was named the C-3 closure-shape enum primitive in S196's
--   disaster-recovery deliverable-mining triage (DV-S196-1) with the 5
--   canonical shapes from the disaster-recovery arc retrospective
--   {convergence, completion, containment-resolved, supersession,
--   stable-held}. DV-S020-5 in the disaster-recovery arc explicitly rejected
--   partial-by-component and posture-downgrade closure dispositions which
--   forces a CLOSED enum at v1 (no escape hatch).
--
--   EF-S196-2 binds DV-S190-2 graduation-discipline against watch-FR
--   deferral for engine primitives evidenced by completed multi-session
--   application arcs / operator-curated synthesis. The disaster-recovery arc
--   IS that synthesis; spec-only or watch-FR-deferral landings are
--   precluded. Substrate column ships at v1.
--
--   Deliberation D-S201-1 (3-perspective: P-1 schema-minimality + P-2
--   codex shape-consult folded as openai perspective per prompt-development
--   v6 §1.5 + P-3 adversarial-overbreadth) sealed at S201 with synthesis:
--
--     - Adopt P-1 + P-2 convergent shape: closure_shape on
--       assumption_ledger only at v1 (NOT issues, NOT close_records;
--       cross-artefact extension preserved as future-direction).
--     - 5-value closed CHECK with no TEXT escape hatch and no DEFAULT;
--       explicit-or-NULL only (P-1 + P-2 + DV-S020-5 + M-3 S194 schema-
--       correctness threshold).
--     - status='closed' requires closure_shape NOT NULL (no anonymous
--       closure; P-1 + P-2 convergence).
--     - status IN (unverified, assumed, active-with-conflict) requires
--       closure_shape IS NULL (no premature labelling; P-1 + P-2).
--     - status='superseded' allows closure_shape NULL or 'supersession'
--       only (narrowing per P-1 + P-2; double-encoding-acknowledged but
--       not forced).
--     - status='invalidated' forbids any closure_shape (none of the 5
--       cleanly expresses invalidation; P-2 named ontologically distinct).
--     - Handler-side validation fires before SQL CHECK with actionable
--       error naming the offending field (P-1 tightening adopted at D-2).
--
--   Reject P-3 spec-only-ship as rejection-basis=operator_override per
--   EF-S196-2 binding. Preserved as M-2 minority watch-trigger: if zero
--   query-by-shape read pattern surfaces across N>=5 sessions, retrospective
--   calibration-EF candidate to remove the column and revert to spec-only
--   vocabulary.
--
--   Reject 6th-value or TEXT escape hatch as rejection-basis=
--   inferior_tradeoff per DV-S020-5 + M-3 S194 schema-correctness threshold.
--   Preserved as M-1 minority watch-trigger: if calibration-EFs name
--   containment-resolved-vs-convergence collapse OR supersession double-
--   encoding across N>=3 sessions, gate-promotion OI for shape-merge.
--
-- Schema delta:
--   assumption_ledger:
--     + closure_shape TEXT NULL CHECK (closure_shape IS NULL OR closure_shape IN
--         ('convergence','completion','containment-resolved','supersession',
--         'stable-held'))
--     + CHECK (status != 'closed' OR closure_shape IS NOT NULL)
--     + CHECK (status NOT IN ('unverified','assumed','active-with-conflict')
--         OR closure_shape IS NULL)
--     + CHECK (status != 'superseded' OR closure_shape IS NULL
--         OR closure_shape = 'supersession')
--     + CHECK (status != 'invalidated' OR closure_shape IS NULL)
--
-- Why T-15-CALIBRATED rebuild over ALTER ADD COLUMN:
--   SQLite ALTER ADD COLUMN cannot add a column with cross-column CHECK
--   constraints (the new column's CHECK can only reference NEW row but
--   the engine forbids them on ADD). The status-shape coupling CHECKs are
--   cross-column, so we rebuild the table.
--
--   CHECK widening: this migration adds 4 new CHECKs without removing any.
--   It is non-destructive over existing rows (verified pre-rebuild: 4 rows
--   with status='assumed' all satisfy closure_shape IS NULL coupling).
--   T-15-CALIBRATED block records the rebuild.
--
-- Existing-row backfill: every existing row gets closure_shape=NULL. Rows
-- with status='closed' would violate the new CHECK; verified via pre-
-- rebuild query that no such rows exist on the primary substrate (4 rows,
-- all status='assumed'). Future fresh-init substrates start empty.
--
-- No new role_write_capabilities INSERT required: assumption_ledger
-- insert/update capabilities already registered at migration 049.
--
-- No FK-citing trigger touches assumption_ledger; no drop+recreate needed
-- (unlike migration 048/049 which rebuilt the objects table requiring
-- t07a_refs_no_superseded_cite drop+recreate).

PRAGMA foreign_keys = OFF;

BEGIN;

-- T-15-CALIBRATED-BEGIN: widen assumption_ledger CHECK set with closure_shape
-- column + 4 status-shape coupling CHECKs. Pure superset over existing rows
-- (verified: 4 rows all status='assumed', satisfying closure_shape IS NULL
-- coupling). Required so DV-S201-1 closure-shape primitive lands per OI-S196-3.
CREATE TABLE assumption_ledger_new (
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
    closure_shape                       TEXT CHECK (closure_shape IS NULL OR closure_shape IN (
                                            'convergence',
                                            'completion',
                                            'containment-resolved',
                                            'supersession',
                                            'stable-held'
                                        )),
    created_at                          TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    -- DV-S008-1 four-field discipline (preserved from migration 049): when
    -- status='active-with-conflict' all four conflict atoms AND sub_type
    -- MUST be NOT NULL.
    CHECK (
        status != 'active-with-conflict' OR (
            sub_type IS NOT NULL
            AND action_commitment_atom_id IS NOT NULL
            AND both_source_citation_atom_id IS NOT NULL
            AND resolution_path_atom_id IS NOT NULL
            AND expiry_trigger_atom_id IS NOT NULL
        )
    ),
    -- sub_type only meaningful when status='active-with-conflict'.
    CHECK (sub_type IS NULL OR status = 'active-with-conflict'),
    -- DV-S201-1 status-shape coupling: status='closed' requires closure_shape.
    CHECK (status != 'closed' OR closure_shape IS NOT NULL),
    -- Pre-closure statuses forbid closure_shape (no premature labelling).
    CHECK (
        status NOT IN ('unverified','assumed','active-with-conflict')
        OR closure_shape IS NULL
    ),
    -- status='superseded' narrows closure_shape to NULL or 'supersession' only.
    CHECK (
        status != 'superseded'
        OR closure_shape IS NULL
        OR closure_shape = 'supersession'
    ),
    -- status='invalidated' forbids any closure_shape (ontologically distinct exit).
    CHECK (status != 'invalidated' OR closure_shape IS NULL)
) STRICT;

INSERT INTO assumption_ledger_new (
    assumption_id, session_id, statement_atom_id, status, sub_type,
    action_commitment_atom_id, both_source_citation_atom_id,
    resolution_path_atom_id, expiry_trigger_atom_id,
    basis_atom_id, origin_decision_object_id,
    last_transition_decision_object_id, object_id,
    closure_shape, created_at
)
SELECT
    assumption_id, session_id, statement_atom_id, status, sub_type,
    action_commitment_atom_id, both_source_citation_atom_id,
    resolution_path_atom_id, expiry_trigger_atom_id,
    basis_atom_id, origin_decision_object_id,
    last_transition_decision_object_id, object_id,
    NULL AS closure_shape, created_at
FROM assumption_ledger;

DROP TABLE assumption_ledger;
ALTER TABLE assumption_ledger_new RENAME TO assumption_ledger;

CREATE INDEX idx_assumption_ledger_session ON assumption_ledger(session_id);
CREATE INDEX idx_assumption_ledger_status ON assumption_ledger(status);
CREATE INDEX idx_assumption_ledger_origin_decision ON assumption_ledger(origin_decision_object_id);
CREATE INDEX idx_assumption_ledger_last_transition ON assumption_ledger(last_transition_decision_object_id);
CREATE INDEX idx_assumption_ledger_closure_shape ON assumption_ledger(closure_shape);
-- T-15-CALIBRATED-END

UPDATE workspace_metadata
   SET value = 'engine-v56'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('051-assumption-ledger-closure-shape-v1.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
