-- Migration 009: issues substrate table + supporting link/note/disposition tables.
-- engine-v21 → engine-v22 (session 088 D-1).
--
-- Adopts the synthesis of deliberation_id=4 (three perspectives: P-1 anthropic-pragmatic,
-- P-2 codex-cross-family, P-3 anthropic-adversarial). Closed-enum status, preserved
-- historical citable_alias on issues directly (not via objects), dedicated
-- link/note/disposition tables, atomized title + summary + optional legacy_import body
-- atom, four CLI kinds (issue / issue-disposition / issue-link / issue-note). Replaces
-- 25 markdown files in open-issues/ as the canonical dispatch surface.
--
-- Design choice: issues do NOT register in the `objects` table. Their alias lives in
-- `issues.citable_alias` directly. Rationale: cross-citation of issues from decisions
-- is rare (decision_supports already has its own alias resolution path), and skipping
-- the objects recreation avoids the FK-cascade pain that the trigger t07a +
-- spec_versions FK chain creates when objects is dropped/recreated. If a future session
-- needs issues to be T-01-citable from arbitrary tables, that migration adds the
-- objects.object_kind widening separately, with the trigger drop/recreate dance.
--
-- Trigger discipline:
--   T-22: alias-format check (GLOB) refuses citable_alias not matching legacy
--         OI-NNN[-...] or new OI-SNNN-N[-...] form.
--   T-22a: status-consistency check refuses status→{resolved,superseded} unless
--         resolved_session_id and resolved_at are set in the same statement.
--   T-23: refuse self-loop in issue_links (CHECK + trigger; belt + suspenders).
--   Cycle detection on `blocks` is deferred to validate-time (post-backfill); SQLite
--         recursive triggers are too expensive for per-insert detection.
--
-- T-15 compliance: this migration adds new tables and triggers only. No DROP TABLE,
-- DROP COLUMN, ALTER TABLE … DROP. No T-15-CALIBRATED block needed.

PRAGMA foreign_keys = ON;

BEGIN;

-- ============================================================================
-- 1. issues: the row per issue.
-- ============================================================================
CREATE TABLE issues (
    issue_id              INTEGER PRIMARY KEY,
    citable_alias         TEXT NOT NULL UNIQUE,
    surfaced_session_id   INTEGER NOT NULL REFERENCES sessions(session_id),
    title_atom_id         INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    summary_atom_id       INTEGER REFERENCES text_atoms(atom_id),
    body_atom_id          INTEGER REFERENCES text_atoms(atom_id),
    priority              TEXT NOT NULL CHECK (priority IN ('HIGH','MEDIUM','LOW')),
    status                TEXT NOT NULL DEFAULT 'open' CHECK (status IN (
                              'open','in_progress','blocked','resolved','superseded'
                          )),
    resolved_session_id   INTEGER REFERENCES sessions(session_id),
    resolved_at           TEXT,
    created_at            TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    CHECK (
        -- terminal statuses require resolved_session + resolved_at;
        -- non-terminal statuses leave them NULL.
        (status IN ('resolved','superseded') AND resolved_session_id IS NOT NULL AND resolved_at IS NOT NULL)
        OR (status NOT IN ('resolved','superseded') AND resolved_session_id IS NULL AND resolved_at IS NULL)
    )
) STRICT;

-- citable_alias format: OI-NNN[-NNN][-...slug...] for legacy preservation;
-- new aliases use OI-S<NNN>-<ord>. Validated by GLOB to stay portable across
-- SQLite builds (REGEXP not always linked).
CREATE TRIGGER t22_issues_alias_format
BEFORE INSERT ON issues
FOR EACH ROW
WHEN NOT (
    NEW.citable_alias GLOB 'OI-[0-9]*'
    OR NEW.citable_alias GLOB 'OI-S[0-9][0-9][0-9]-[0-9]*'
)
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T22: issues.citable_alias must match OI-NNN[-...] or OI-SNNN-N[-...]');
END;

-- T-22a: status terminal transitions require resolved_session_id + resolved_at
-- in the same statement.
CREATE TRIGGER t22_issues_status_consistency
BEFORE UPDATE OF status ON issues
FOR EACH ROW
WHEN NEW.status != OLD.status
 AND ((NEW.status IN ('resolved','superseded')) AND (NEW.resolved_session_id IS NULL OR NEW.resolved_at IS NULL))
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T22: status to resolved/superseded requires resolved_session_id and resolved_at set in same statement');
END;

-- Hot-path indexes for dispatch.
CREATE INDEX idx_issues_status_priority ON issues(status, priority);
CREATE INDEX idx_issues_surfaced ON issues(surfaced_session_id);

-- ============================================================================
-- 2. issue_links: directed edges between issues.
-- ============================================================================
CREATE TABLE issue_links (
    link_id              INTEGER PRIMARY KEY,
    source_issue_id      INTEGER NOT NULL REFERENCES issues(issue_id),
    target_issue_id      INTEGER NOT NULL REFERENCES issues(issue_id),
    relation             TEXT NOT NULL CHECK (relation IN (
                            'blocks','supersedes','duplicates','folds_into','related'
                         )),
    reason_atom_id       INTEGER REFERENCES text_atoms(atom_id),
    session_id           INTEGER NOT NULL REFERENCES sessions(session_id),
    created_at           TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    UNIQUE (source_issue_id, target_issue_id, relation),
    CHECK (source_issue_id != target_issue_id)
) STRICT;

CREATE INDEX idx_issue_links_source ON issue_links(source_issue_id, relation);
CREATE INDEX idx_issue_links_target ON issue_links(target_issue_id, relation);

-- T-23: self-loops already refused by CHECK above; trigger reinforces with a
-- specific error label for diagnostics.
CREATE TRIGGER t23_issue_links_no_self
BEFORE INSERT ON issue_links
FOR EACH ROW
WHEN NEW.source_issue_id = NEW.target_issue_id
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T23: issue_links self-loop refused');
END;

-- ============================================================================
-- 3. issue_notes: append-only annotation rows on an issue.
-- ============================================================================
CREATE TABLE issue_notes (
    note_id              INTEGER PRIMARY KEY,
    issue_id             INTEGER NOT NULL REFERENCES issues(issue_id),
    seq                  INTEGER NOT NULL,
    note_atom_id         INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    session_id           INTEGER NOT NULL REFERENCES sessions(session_id),
    created_at           TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    UNIQUE (issue_id, seq)
) STRICT;

CREATE INDEX idx_issue_notes_issue ON issue_notes(issue_id, seq);

-- ============================================================================
-- 4. issue_dispositions: state-transition rows. Status moves only via these.
-- ============================================================================
CREATE TABLE issue_dispositions (
    disposition_id       INTEGER PRIMARY KEY,
    issue_id             INTEGER NOT NULL REFERENCES issues(issue_id),
    seq                  INTEGER NOT NULL,
    from_status          TEXT NOT NULL CHECK (from_status IN (
                            'open','in_progress','blocked','resolved','superseded'
                         )),
    to_status            TEXT NOT NULL CHECK (to_status IN (
                            'open','in_progress','blocked','resolved','superseded'
                         )),
    reason_atom_id       INTEGER NOT NULL REFERENCES text_atoms(atom_id),
    session_id           INTEGER NOT NULL REFERENCES sessions(session_id),
    created_at           TEXT NOT NULL DEFAULT (strftime('%Y-%m-%dT%H:%M:%fZ','now')),
    UNIQUE (issue_id, seq),
    CHECK (from_status != to_status)
) STRICT;

CREATE INDEX idx_issue_dispositions_issue ON issue_dispositions(issue_id, seq);

-- ============================================================================
-- 5. role_write_capabilities: admit __cli__ writes on the new tables.
-- ============================================================================
INSERT INTO role_write_capabilities (role, table_name, write_op) VALUES
    ('__cli__','issues','insert'),
    ('__cli__','issues','update'),
    ('__cli__','issue_links','insert'),
    ('__cli__','issue_notes','insert'),
    ('__cli__','issue_dispositions','insert');

-- Record the migration. Runner replaces the placeholder sha after applying.
INSERT INTO schema_migrations (name, sha256) VALUES ('009-issues-table.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
