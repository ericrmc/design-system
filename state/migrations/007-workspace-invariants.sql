-- 007-workspace-invariants.sql
-- engine-v20 follow-up; ships in S084.
-- Per operator: workspace_id, mode, current_engine_version are workspace-level
-- invariants and live in workspace_metadata; session-open should not require
-- the caller to repeat them. Slug is immutable after open (otherwise the
-- provenance directory orphans files on re-export).

INSERT INTO workspace_metadata (key, value) VALUES
    ('workspace_id', 'selvedge-self-development'),
    ('mode', 'self-development'),
    ('current_engine_version', 'engine-v20');

-- T-23: slug is immutable after session-open. The provenance directory name
-- is derived from slug + workspace_session_no; renaming mid-session would
-- orphan files in the prior path. If a slug genuinely needs to change, do
-- it via a future explicit `session-rename` kind that ALSO renames the
-- exported directory atomically.
CREATE TRIGGER t23_sessions_slug_immutable
BEFORE UPDATE OF slug ON sessions
FOR EACH ROW
WHEN NEW.slug IS NOT OLD.slug
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T23: sessions.slug is immutable after open');
END;

INSERT INTO schema_migrations (name, sha256) VALUES ('007-workspace-invariants.sql', 'COMPUTED-AT-APPLY-TIME');

-- End migration 007.
