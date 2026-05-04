-- Migration 045: engine_feedback_anchors typed-FK graph for chain-walk
-- reachability of historical-harvest engine_feedback rows.
--
-- Sealed at S194 DV-S194-1 closing the S193 discoverability gap: 22
-- EF-S193-* historical-harvest rows were substrate-resident but orphaned
-- in the chain-walk graph (no inbound citations from decision_v2 supports
-- since chain-walks traverse decision_supports.cited_object_id only).
-- A future agent contemplating a deliberation could not discover the
-- harvested pre-S180 reasoning via SQL FK joins from active deliberation
-- surfaces; only via one-shot orient-untriaged listing or LIKE-grep on
-- body_md (requires the agent to already know the search term).
--
-- The 4-perspective deliberation D-S194-1 (P-1 chain-walk-integrity +
-- P-2 context-surfacing-ergonomics + P-3 substrate-schema-discipline +
-- P-4 gate-risk-friction) converged on option C as primary substrate
-- mechanism: typed-FK anchor table from engine_feedback to objects.
-- Cross-perspective convergence on FK-only-no-free-form-labels per P-3
-- schema-correctness threshold (M-3 minority preserved). Codex (gpt-5.5
-- xhigh) shape-consult per EF-S194-1 endorsed C + light E + single-arc.
--
-- Why typed FK to objects (not free-form topic strings):
--   The chain_walks walker (T-32, engine-v48) traverses objects.alias as
--   its primary node-set. Anchoring engine_feedback to objects via FK
--   composes with chain_walks: walking from a decision_v2 anchor that
--   has an anchor row reaches the engine_feedback row via the same
--   typed graph, no string-match heuristic needed. Free-form atom topics
--   (option A) would re-introduce the LIKE-grep failure mode that the
--   harvest's stated chain-walk-utility purpose was meant to escape, per
--   P-1 risk-of-untyped-pseudo-links and P-3 schema-correctness reject.
--
-- Why FK to objects.object_id (not engine_feedback citing objects via
-- ref_v2 or similar):
--   ref_v2 records body_md auto-detected aliases; that already runs at
--   engine_feedback insert. But ref_v2 is a forensic record of what
--   aliases were named in body prose, not a typed declaration of which
--   substrate entities the harvest row anchors to semantically. The
--   anchor table is the latter — submit-time-declared semantic edges
--   under a closed enum of anchor_role values. ref_v2 remains the prose
--   record; anchors are the typed graph.
--
-- anchor_role enum (closed CHECK; M-3 binds against future TEXT escape):
--   - 'about': the harvest row IS about / contains rationale for the
--     anchor entity (e.g. EF-S193-18 about ceremony-subtraction discipline
--     anchors to DV-S081-1 substrate-loss-defense as the active spec
--     descendant of S109 retirement).
--   - 'descended_from': the anchor entity descends from / supersedes the
--     historical reasoning the harvest row pointed at (e.g. current
--     methodology-kernel descended-from archive/pre-restart/methodology-
--     kernel-v5).
--   - 'calibrates': the harvest row records operator-feedback or
--     calibration that shaped the anchor entity (e.g. EF-075 reviewer-
--     cost-not-target calibrates current validation-approach posture).
--   - 'supersedes_context': the harvest row preserves narrative-context
--     for an anchor entity that superseded an earlier shape (e.g. the
--     DV-S109-1 retirement narrative is preserved by the harvest pointer
--     to provenance/109-subtract-constraints-from-manifest as context
--     for the active manifest).
--
-- Authority: handler-side enforcement. The engine-feedback submit
-- handler refuses with E_REFUSAL_T37 when body_md begins with
-- 'historical-harvest:' AND no anchors[] entry was provided. Trigger-side
-- enforcement is structurally infeasible because anchors are inserted
-- AFTER the engine_feedback row inside the same write_tx; SQLite has no
-- DEFER trigger semantics. Handler-side enforcement matches the same
-- shape used for T-32 chain-walks dispatch (handler walks inside the
-- same write_tx as the decision-record submit). Receipt for failure is
-- E_REFUSAL_T37 with substrate-named recovery hint listing the
-- closest-matching objects.alias values for the operator to anchor against.
--
-- Backfill of 22 EF-S193-* rows in same session: a one-shot script
-- reads each EF-S193-N row's body_md, extracts referenced aliases that
-- already resolve in current substrate via objects.alias lookup,
-- and inserts one engine_feedback_anchors row per resolved anchor with
-- role inferred from body_md context. Rows resolving to zero anchors
-- get zero anchor rows (P-3 zero-anchors-acceptable per DV-S189-1
-- markdown-only-recovery; pre-S180 substrate continuity broken at wipe
-- boundary admits some harvest rows referencing now-vanished aliases).
-- No synthetic alias creation per DV-S189-1.
--
-- Forward-references emitted (recorded in close_record next_session_should):
--   - FR-S194-1: watch-trigger graduation of D per M-2 (3 calibration-EFs
--     across N>=5 sessions name missed-context graduate to T-NN deliberation-
--     open precheck per DV-S190-2 receipt-pattern).
--   - FR-S194-2: predicted-future-FR-to-reject any topic_label TEXT
--     escape hatch column pressure per M-3 schema-correctness threshold.
--   - FR-S194-3: chain-walks walker bidirectional traversal extension
--     preserved as forward-direction per P-1 open question (v1 ships
--     inbound-only).

PRAGMA foreign_keys = OFF;

BEGIN;

CREATE TABLE engine_feedback_anchors (
    feedback_anchor_id  INTEGER PRIMARY KEY,
    feedback_id         INTEGER NOT NULL REFERENCES engine_feedback(feedback_id) ON DELETE CASCADE,
    anchor_object_id    INTEGER NOT NULL REFERENCES objects(object_id),
    anchor_role         TEXT    NOT NULL
                                CHECK (anchor_role IN ('about','descended_from','calibrates','supersedes_context')),
    created_at          TEXT    NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    UNIQUE (feedback_id, anchor_object_id, anchor_role)
);

CREATE INDEX idx_efa_anchor ON engine_feedback_anchors(anchor_object_id);
CREATE INDEX idx_efa_feedback ON engine_feedback_anchors(feedback_id);

INSERT INTO schema_migrations (name, sha256) VALUES ('045-engine-feedback-anchors.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
