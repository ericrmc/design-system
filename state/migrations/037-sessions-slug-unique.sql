-- Migration 037: sessions.slug UNIQUE (engine-v49 unchanged).
--
-- Why:
--   D-28 C-3 four-way convergence + DV-S179-1 closes OI-S122-1 by-mechanism.
--   sessions.slug currently has no UNIQUE constraint; concurrent same-microsecond
--   writes could create duplicates. Pre-flight: zero duplicate slugs at S179.
--
--   Implementation choice: CREATE UNIQUE INDEX rather than table rebuild.
--   A unique index is functionally equivalent to a UNIQUE constraint in
--   SQLite for INSERT-time refusal, and avoids rebuilding the sessions
--   table (which carries 14 triggers t02/t10/t11/t18/t19/t20/t22/t23/t29
--   /t30/t39/t39b/t40/t41 that would all need to be re-created on a
--   rebuild path). Index-based approach is strictly less destructive
--   per T-15 and matches the convention used by idx_sessions_workspace
--   _session_no for workspace_session_no UNIQUE-via-index.
--
--   Pre-flight defense lives in the application layer; if a duplicate
--   slug exists at apply time, the CREATE UNIQUE INDEX statement itself
--   will fail with a clear sqlite_constraint error naming the duplicate.
--
-- T-15 compliance:
--   Additive CREATE INDEX only — no DROP, no ALTER, no rebuild. No
--   T-15-CALIBRATED block needed.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE UNIQUE INDEX idx_sessions_slug_unique ON sessions(slug);

INSERT INTO schema_migrations (name, sha256) VALUES ('037-sessions-slug-unique.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
