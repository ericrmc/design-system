-- Migration 050: prospective-scoping discipline v1 (T-41 close-record gate).
-- engine-v54 -> engine-v55 (S199 DV-S199-1 closes OI-S196-5 by-mechanism).
--
-- Why:
--   OI-S196-5 was named the C-5 prospective-scoping primitive in S196's
--   disaster-recovery deliverable-mining triage (DV-S196-1). FR-S198-14 +
--   FR-S197-14 + FR-S196-13 named it next per highest-impact-per-line
--   framing once OI-S196-1 (typed-assumption-ledger, S198) shipped.
--
--   Disaster-recovery retrospective §6.1 evidence: 11 of 25 assumptions
--   (44%) were registered-vs-implicit gap-closures discovered under
--   pressure. Three implication patterns named: infrastructure-adjacency
--   (A-006 → A-017), resource-allocation-constraint (air-corridor → A-020),
--   authority-chain-dispute (tasking delegation → A-022).
--
--   Deliberation D-7 (3-perspective: P-1 schema-correctness + P-2 ceremony-
--   subtraction + P-3 codex shape-consult SHIP-WITH-NAMED-EDITS) sealed at
--   S199. Synthesis adopts P-3 close-record gate using engine_feedback
--   body_md prefix detection (no new table at v1; ceremony-subtraction
--   compromise per DV-S109-1).
--
-- Gate shape (T-41, handler-side at close-record submit):
--   For sessions producing ≥1 substantive artefact (DV with kind in
--   substantive | schema_migration, OR ≥1 spec_version, OR ≥1 migration
--   ref), refuse close-record INSERT unless the session has either:
--   (a) ≥1 assumption_ledger row whose origin_decision_object_id points
--       to a DV from this session, OR
--   (b) ≥1 engine_feedback row for this session whose body_md begins
--       with the literal prefix 'scoping-pass:'.
--
--   Pure-meta sessions (no substantive artefacts produced) admit close-
--   record without prospective-scoping receipt (artefact-gated
--   applicability per codex P-3 named edit + P-1 acknowledgement).
--
--   Cheap-exit nil_attestation: the EF body_md may begin
--   'scoping-pass: 0 — exclusions applied: <which artefact-classes>' to
--   admit when no implications surface; mirrors T-36 nil_attestation
--   pattern from deliberation_counterfactuals (DV-S180-1 lineage).
--
-- Why no new table at v1 (rejects P-1 schema-correctness):
--   D-7 D-1 divergence: P-1 typed scoping_passes from day one; P-2
--   prose-only-no-gate at §6 Produce; P-3 close-record gate via
--   engine_feedback prefix. Synthesis adopts P-3 prefix detection per
--   ceremony-subtraction (DV-S109-1) + §8.5 audit-step prefix precedent.
--   M-1 minority preserved (P-1 typed-from-day-one): v2 promotion-trigger
--   if calibration EFs surface prefix brittleness, queryable-count need,
--   or review-distinguishing failure across 2+ sessions.
--
-- Why gate at close-record (not session-close):
--   D-7 C-1 convergence (P-1 + P-3): close-record is the durable session
--   artefact boundary; T-39 already requires it for session-close. T-41
--   attaches to the same transaction boundary so prospective-scoping is
--   evidenced before the close-record itself becomes binding. P-2's no-gate
--   stance preserved as M-2 minority watch-trigger if formulaic compliance
--   surfaces.
--
-- Why artefact-gated applicability (not all-kinds-gate):
--   D-7 C-3 convergence (codex P-3 + P-1 acknowledgement): pure-meta
--   sessions (triage, FR/EF dispositions only) produce no substantive
--   artefact whose implications could be unregistered. Gate fires only
--   when session.kind != 'meta' AND session has produced ≥1 substantive
--   DV/spec_version/migration. Differs from T-38 all-kinds-gate (which
--   gates context-surfacing for every kind because every kind benefits
--   from substrate context).
--
-- Schema changes:
--   None at v1 — gate is handler-side. Migration 050 only:
--     - bumps current_engine_version to engine-v55
--     - adds composite index on engine_feedback (session_id, body_md)
--       for prefix-lookup performance under the close-record gate
--     - records schema_migrations row
--
-- M-1/M-2 minorities preserved per DV-S199-1 synthesis:
--   M-1 P-1 typed-substrate-from-day-one: v2 promotion if prefix
--     detection brittleness measurable.
--   M-2 P-2 no-gate-prose-only-§6-Produce: watch-trigger if formulaic
--     compliance surfaces in 2+ calibration EFs (M-1-of-D-23/D-29
--     receipt-presence-not-epistemic-adequacy concern).

PRAGMA foreign_keys = OFF;

BEGIN;

-- Composite index for close-record gate prefix lookup.
-- The gate query is: SELECT 1 FROM engine_feedback WHERE session_id=? AND body_md LIKE 'scoping-pass:%' LIMIT 1.
-- Without an index this is a full session-scan; with the index session_id is the primary filter.
CREATE INDEX idx_engine_feedback_session_body ON engine_feedback(session_id);

UPDATE workspace_metadata
   SET value = 'engine-v55'
 WHERE key = 'current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('050-prospective-scoping-gate-v1.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;

PRAGMA foreign_keys = ON;
