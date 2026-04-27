-- 006-workspace-metadata.sql
-- engine-v20 follow-up; ships in S084 alongside 003+004+005.
-- Per operator: instead of callers knowing the workspace session number,
-- store the init offset once and have the CLI auto-compute. session-open
-- in the CLI picks the next substrate row and adds the offset.

CREATE TABLE workspace_metadata (
    key   TEXT PRIMARY KEY,
    value TEXT NOT NULL
) STRICT;

-- This workspace started at S080 (substrate session_no=1). offset = 79.
-- Future workspaces created via `selvedge init` should set this to 0
-- (substrate session 1 = workspace 1) unless retrofitting onto an
-- existing pre-substrate session log.
INSERT INTO workspace_metadata (key, value) VALUES
    ('init_session_offset', '79'),
    ('schema_version_at_init', 'engine-v17');

INSERT INTO schema_migrations (name, sha256) VALUES ('006-workspace-metadata.sql', 'COMPUTED-AT-APPLY-TIME');

-- End migration 006.
