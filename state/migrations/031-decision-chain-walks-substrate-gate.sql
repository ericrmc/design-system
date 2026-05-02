-- Migration 031: decision_chain_walks substrate-gate (T-32, engine-v47 to v48).
--
-- Why:
--   DV-S175-1 shipped the chain-walk RECOMMENDED clause in prompts/development.md
--   §5 with substrate-gate deferred to recurrence-EF graduation per FR-S173-5
--   and DV-S152-1 typed-observation pathway. At S176-open the operator named
--   the failure mode: recommended-clause without instrumentation produced
--   ceremony without measurement. FR-S173-3 calibration-watch had no substrate
--   query that returns the watched count; export --provenance --print is a
--   pure-read tool that writes no row. The promotion-trigger required a
--   calibration-EF that required the same prose-pattern-match the recommended-
--   clause already failed to ensure. Operator mandate: ship deterministic
--   substrate-gate now; DV-S109-1 ceremony-subtraction operator-precluded as
--   rejection basis for D-27.
--
--   D-27 (P-1 anthropic primary + P-2 openai-codex cross-family + P-3
--   anthropic adversarial-implementation) converged unanimous on shipping
--   the substrate-gate at S176 (C-1), submit-handler dispatches receipts
--   in-band not export-side-effect (C-2), receipts as substrate rows
--   (C-3), forward-only migration (C-4), walker_version recorded (C-5).
--   D-1 walk-scope adopted P-1 walk-everything over P-2 predicate-detected
--   obligations: walk every cited alias unconditionally for simplicity and
--   broader coverage. P-3 adversarial contributions all adopted (cycle
--   detection, atomicity, useful refusal text, zero-cite admit, bootstrap
--   verification).
--
-- Schema:
--   decision_chain_walks                            INTEGER PRIMARY KEY
--     One row per (decision_v2_id, anchor_alias) snapshot; the decision-
--     record submit handler computes cited alias union from supports +
--     alternatives.rejections + supersedes-target + effects.target and
--     dispatches the existing _export_provenance_anchor walker in-band
--     inside the same write_tx, capturing the rendered markdown body and
--     edge/node counts as proof object.
--   decision_chain_walks.decision_v2_id             FK CASCADE
--     Receipts cascade with their parent decision_v2 row (rare but
--     consistent with engine-v34 effect-row cascade discipline).
--   decision_chain_walks.anchor_alias               TEXT NOT NULL
--     The cited alias the walker rooted at. Resolved at handler time;
--     unresolved alias raises E_REFUSAL_T32 from handler before INSERT.
--   decision_chain_walks.anchor_object_id           INTEGER NULL FK objects
--     The resolved objects.object_id for traceability. NULL for aliases
--     resolved via issues table (OI-...) since issue rows do not register
--     in objects per OI-086-003 schema gap; alias-string remains
--     authoritative for verification.
--   decision_chain_walks.max_depth                  INTEGER 1..5 CHECK
--     The walker depth used; default 3, hard cap 5 per ANCHOR_TRACE.
--   decision_chain_walks.walker_version             TEXT non-empty CHECK
--     Walker logic version stamp. Forward-compat: future migrations
--     changing walker behaviour stamp a new version so receipt readers
--     can render with original logic.
--   decision_chain_walks.nodes_visited              INTEGER >= 1 CHECK
--     Walker BFS visited-set size. Always >= 1 (the root anchor itself).
--   decision_chain_walks.edges_traversed            INTEGER >= 0 CHECK
--     Walker edges_out length. Zero is valid (isolated anchor with no
--     neighbours within the closed edge family).
--   decision_chain_walks.truncation_status          TEXT enum CHECK
--     P-3 D-27 contribution: distinguish a clean walk from a depth-capped,
--     cycle-broken, or walker-errored walk. Enum values:
--       none           — walker completed without truncation.
--       depth_capped   — walker reached --max-depth and frontier remained.
--       cycle_break    — walker visited-set rejected duplicate; bounded.
--       walker_error   — walker raised; receipt insert refused (defensive).
--   decision_chain_walks.result_text                TEXT non-empty CHECK
--     Rendered markdown body from _export_provenance_anchor; the human-
--     readable presentation. Verifiability lives in result_sha256.
--   decision_chain_walks.result_sha256              TEXT length=64 CHECK
--     SHA-256 hex of result_text. P-2 D-27 contribution: edges-only proof
--     object (D-2 divergence preserved; cited-row-content extension
--     deferred to v2 if calibration-EF surfaces stale-cite invalidation).
--   decision_chain_walks.created_at                 TEXT default CURRENT
--     Snapshot timestamp.
--   UNIQUE(decision_v2_id, anchor_alias)
--     One receipt per (decision, alias) pair; idempotent under retry.
--
-- T-32 handler-enforced refusal (engine-v48):
--   _submit_decision_v2 computes cited_aliases = supports.cite +
--   alternatives.rejections.cite + supersedes-target alias + effects.target
--   alias union, dispatches walker per alias, inserts receipts, raises
--   E_REFUSAL_T32 on any walker exception, unresolved alias, or count
--   mismatch (receipts != cited_aliases). Zero-cite decisions (initial
--   spec-version with no supersedes, decisions with no DV/SPEC/EF cites)
--   admit zero receipts; predicate is `cited_count > 0 AND receipts <
--   cited_count` per P-3 D-27 zero-cite admit defense.
--
--   SQL-side trigger T-32 not added: the handler is authoritative and
--   the violation shape (count assertion across decision_v2 + receipts +
--   cite tables) is not synchronously expressible at INSERT-time on any
--   single table. Defense-against-direct-INSERT-bypass is named as a
--   FR-S176-N watch if a calibration-EF surfaces a bypass attempt;
--   handler-policed-with-watch matches T-28's history (handler+trigger
--   came together at engine-v28 only after closes_issue had a
--   synchronously-checkable target_issue_id slot). Receipt-row format
--   integrity is enforced by CHECK constraints above.
--
-- Bootstrap:
--   DV-S176-1 is the first decision-record under the gate. Its supports
--   cite DV-S175-1, DV-S173-1, DV-S109-1, DV-S152-1, DV-S174-1, EF-S173-1,
--   P-27-P-1, P-27-P-2, P-27-P-3 (deliberation perspectives), and effects
--   target DV-S175-1 (supersedes via spec-version chain) and OI-S176-1
--   (closes_issue). The handler must succeed against this exact payload
--   at first invocation; bootstrap test in state/tests verifies this
--   shape end-to-end before COMMIT in S176.
--
-- T-15 compliance:
--   Additive only — CREATE TABLE, CREATE INDEX, INSERT into
--   role_write_capabilities (existing __cli__ caps extended), UPDATE
--   workspace_metadata. No DROP TABLE, DROP COLUMN, ALTER TABLE ... DROP,
--   no widening of existing CHECK constraints. No T-15-CALIBRATED block
--   needed.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TABLE decision_chain_walks (
    chain_walk_id INTEGER PRIMARY KEY AUTOINCREMENT,
    decision_v2_id INTEGER NOT NULL REFERENCES decisions_v2(decision_v2_id) ON DELETE CASCADE,
    anchor_alias TEXT NOT NULL CHECK (length(anchor_alias) > 0),
    anchor_object_id INTEGER REFERENCES objects(object_id),
    max_depth INTEGER NOT NULL CHECK (max_depth BETWEEN 1 AND 5),
    walker_version TEXT NOT NULL CHECK (length(walker_version) > 0),
    nodes_visited INTEGER NOT NULL CHECK (nodes_visited >= 1),
    edges_traversed INTEGER NOT NULL CHECK (edges_traversed >= 0),
    truncation_status TEXT NOT NULL CHECK (truncation_status IN ('none','depth_capped','cycle_break','walker_error')),
    result_text TEXT NOT NULL CHECK (length(result_text) > 0),
    result_sha256 TEXT NOT NULL CHECK (length(result_sha256) = 64),
    created_at TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    UNIQUE(decision_v2_id, anchor_alias)
);

CREATE INDEX idx_decision_chain_walks_decision ON decision_chain_walks(decision_v2_id);
CREATE INDEX idx_decision_chain_walks_anchor ON decision_chain_walks(anchor_alias);

INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES ('__cli__', 'decision_chain_walks', 'insert');

UPDATE workspace_metadata SET value='engine-v48' WHERE key='current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('031-decision-chain-walks-substrate-gate.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
