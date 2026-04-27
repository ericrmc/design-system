-- 005-workspace-session-numbering.sql
-- engine-v20 follow-up; ships in S084 alongside 003+004.
-- Per S084 reviewer / operator: substrate session_no is a substrate-internal
-- counter (1, 2, 3, ...) and does NOT match the workspace session number
-- (S080, S081, ...). Export, citation, and provenance directory naming all
-- need the workspace number. Add `workspace_session_no` and backfill the 5
-- historical rows.

-- ============================================================================
-- 1. Add workspace_session_no column (additive ALTER ADD; T-15 admits).
-- ============================================================================
ALTER TABLE sessions ADD COLUMN workspace_session_no INTEGER;

-- ============================================================================
-- 2. One-time backfill of the 5 historical rows.
-- substrate session_no 1 → S080, 2 → S081, 3 → S082, 4 → S083, 5 → S084.
-- Sessions has no T-06 protection on the sessions row itself (T-06 protects
-- child rows of closed sessions), so the UPDATE is admitted directly.
-- ============================================================================
UPDATE sessions SET workspace_session_no = 80 WHERE session_no = 1;
UPDATE sessions SET workspace_session_no = 81 WHERE session_no = 2;
UPDATE sessions SET workspace_session_no = 82 WHERE session_no = 3;
UPDATE sessions SET workspace_session_no = 83 WHERE session_no = 4;
UPDATE sessions SET workspace_session_no = 84 WHERE session_no = 5;

-- ============================================================================
-- 3. UNIQUE index on workspace_session_no (partial; allows NULL during
-- the post-migration transition).
-- ============================================================================
CREATE UNIQUE INDEX idx_sessions_workspace_session_no
    ON sessions (workspace_session_no) WHERE workspace_session_no IS NOT NULL;

-- ============================================================================
-- 4. T-22: future session inserts must carry workspace_session_no.
-- (Engine-v21+ will tighten this; engine-v20 keeps it as a soft requirement
-- via this trigger so the historical rows remain valid even if the column
-- ever drifts.)
-- ============================================================================
CREATE TRIGGER t22_sessions_workspace_no_required_ins
BEFORE INSERT ON sessions
FOR EACH ROW
WHEN NEW.workspace_session_no IS NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T22: sessions.workspace_session_no is required for engine-v20+ inserts');
END;

INSERT INTO schema_migrations (name, sha256) VALUES ('005-workspace-session-numbering.sql', 'COMPUTED-AT-APPLY-TIME');

-- End migration 005.
