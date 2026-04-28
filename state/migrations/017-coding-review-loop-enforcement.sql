-- Migration 017: substrate enforcement of the coding review loop.
-- engine-v30 → engine-v31 (S104 D-1, D-2, D-4, D-7, closing OI-083-001).
--
-- Why:
--   Methodology specifications/methodology.md §"When to review" defines the
--   coding review loop and explicitly notes "the substrate does not yet
--   enforce this; until it does, the discipline is operator-policed and
--   recorded in 04-review.md." OI-083-001 is the structural-enforcement gap.
--   T-20 only refuses close on open medium+ review_findings; a coding
--   session that records ZERO findings (because the reviewer was never
--   invoked) passes T-20 trivially. This migration closes that hole.
--
-- Shape (per S104 D-8 deliberation synthesis):
--   1. sessions.kind: operator declares classification at open. Default
--      'coding' (the safe default — most self-development sessions touch
--      executable logic). Alternatives 'spec_only' (pure spec/methodology
--      work) and 'meta' (purely substrate-row triage with no artefact
--      production). Immutable post-open via t29 (mirrors t23 slug pattern).
--   2. review_passes: terminal-pass artefact distinct from review_findings.
--      One row per reviewer iteration. Outcome ∈ {clean, findings,
--      nonconverged}. Carries operator-asserted head_sha for staleness
--      audit (substrate cannot verify the sha against working-tree truth;
--      it can require the assertion exist and be format-checked). For
--      nonconverged outcomes, halt_issue_id FK to issues is required.
--   3. t30: close-gate on coding sessions. Refuses (open→closed) on
--      kind='coding' unless the latest review_pass is outcome='clean' OR
--      outcome='nonconverged' with halt_issue_id NOT NULL.
--   4. T-20 narrowed: open medium+ findings refuse close ONLY when the
--      session is not on the halt path. Halt path is signalled by latest
--      review_pass.outcome='nonconverged' — this admits unresolved findings
--      honestly (per methodology: halt is "not a normal close").
--
-- Halted-as-status-value deferred (DV-S104-7):
--   The methodology describes halted as observable from the session row
--   alone. SQLite column-level CHECK cannot be widened in-place; admitting
--   'halted' as a sessions.status value requires a full table-rebuild on a
--   table with eight triggers and dozens of FK referrers. Per migration 016
--   commentary, that is the calibrated table-rebuild trap. For a MEDIUM
--   post-release-gate issue, that cost is unjustified. Halt is encoded
--   here via review_passes.outcome='nonconverged' on a session.status=
--   'closed' row. Promote to status value via OI-S104-3 when warranted.
--
-- Manifest-hash sealing deferred (OI-S104-1):
--   P-2 (codex/openai) cross-family perspective argued declaration is the
--   wrong anchor under context pressure: spec_only sessions mutate into
--   coding sessions late. P-2's full alternative (session_artifact_changes
--   + manifest-hash sealing) requires substrate-side file-tracking that
--   does not exist. head_sha on review_pass is a thinner staleness
--   anchor adoptable now. Adopt P-2's full shape if declaration-based
--   enforcement proves operator-policed in practice.

PRAGMA foreign_keys = ON;

BEGIN;

-- 1. sessions.kind classification at open (immutable post-open per t29).
ALTER TABLE sessions ADD COLUMN kind TEXT NOT NULL DEFAULT 'coding'
    CHECK (kind IN ('coding','spec_only','meta'));

-- 2. review_passes: terminal-pass artefact per reviewer iteration.
CREATE TABLE review_passes (
    review_pass_id      INTEGER PRIMARY KEY,
    session_id          INTEGER NOT NULL REFERENCES sessions(session_id),
    iteration           INTEGER NOT NULL CHECK (iteration BETWEEN 1 AND 4),
    outcome             TEXT NOT NULL CHECK (outcome IN ('clean','findings','nonconverged')),
    head_sha            TEXT NOT NULL CHECK (length(head_sha) BETWEEN 7 AND 64),
    summary_atom_id     INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    halt_issue_id       INTEGER REFERENCES issues(issue_id),
    recorded_at         TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    object_id           INTEGER REFERENCES objects(object_id),
    UNIQUE (session_id, iteration)
) STRICT;

CREATE INDEX idx_review_passes_session_iteration
    ON review_passes(session_id, iteration);

CREATE TRIGGER t_review_pass_nonconverged_requires_halt_issue
BEFORE INSERT ON review_passes
FOR EACH ROW
WHEN NEW.outcome = 'nonconverged' AND NEW.halt_issue_id IS NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_RP1: nonconverged review_pass requires halt_issue_id (FK to the OI-<session>-<slug>-findings-unresolved issue per methodology)');
END;

-- 3. t29: sessions.kind is immutable post-open (mirrors t23 slug pattern).
CREATE TRIGGER t29_sessions_kind_immutable
BEFORE UPDATE OF kind ON sessions
FOR EACH ROW
WHEN NEW.kind IS NOT OLD.kind
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T29: sessions.kind is immutable after open');
END;

-- 4. t30: coding session close requires terminal review_pass.
--    Halt path admitted: latest pass nonconverged + halt_issue_id present.
CREATE TRIGGER t30_close_coding_session_review_pass
BEFORE UPDATE OF status ON sessions
FOR EACH ROW
WHEN OLD.status = 'open'
 AND NEW.status = 'closed'
 AND NEW.kind = 'coding'
 AND NOT EXISTS (
    SELECT 1 FROM review_passes rp
    WHERE rp.session_id = NEW.session_id
      AND rp.iteration = (
          SELECT MAX(iteration) FROM review_passes
          WHERE session_id = NEW.session_id
      )
      AND (
          rp.outcome = 'clean'
          OR (rp.outcome = 'nonconverged' AND rp.halt_issue_id IS NOT NULL)
      )
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T30: coding session close requires terminal review_pass (clean or nonconverged-with-halt-issue) — submit review-pass before close');
END;

-- 5. T-20 narrowed: admit halt path. Open medium+ findings refuse close
--    UNLESS the latest review_pass is nonconverged (halt path is honest
--    about unresolved findings; methodology says halt is "not a normal
--    close" but does not require findings be force-adjudicated).
DROP TRIGGER t20_close_no_open_medium_plus_findings;

CREATE TRIGGER t20_close_no_open_medium_plus_findings
BEFORE UPDATE OF status ON sessions
FOR EACH ROW
WHEN OLD.status = 'open'
 AND NEW.status = 'closed'
 AND NOT EXISTS (
    -- halt path: latest review_pass is nonconverged → unresolved findings admitted
    SELECT 1 FROM review_passes rp
    WHERE rp.session_id = NEW.session_id
      AND rp.outcome = 'nonconverged'
      AND rp.iteration = (
          SELECT MAX(iteration) FROM review_passes
          WHERE session_id = NEW.session_id
      )
 )
 AND EXISTS (
    SELECT 1 FROM review_findings rf
    WHERE rf.session_id = NEW.session_id
      AND rf.disposition = 'open'
      AND rf.severity IN ('critical','high','medium')
 )
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T20: open medium-or-higher review findings prevent close (use halt path via nonconverged review_pass to admit unresolved findings honestly)');
END;

-- 6. Engine version bump.
UPDATE workspace_metadata SET value='engine-v31' WHERE key='current_engine_version';

INSERT INTO schema_migrations (name, sha256) VALUES ('017-coding-review-loop-enforcement.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
