-- Migration 002: tighten deliberation immutability (engine-v18, session 082).
-- Closes OI-080-001 structurally:
--   (a) T-06 had no triggers on `deliberations` UPDATE/DELETE; a closed-session
--       deliberation's topic and synthesis_md were silently mutable from any
--       direct-SQL writer. Add the missing pair (UPD + DEL).
--   (b) T-13 only refused non-NULL → NULL transitions on `sealed_at`. A direct
--       UPDATE that set sealed_at to a different non-NULL timestamp was admitted,
--       polluting the audit trail. Replace with a tightened condition that
--       refuses any change to a non-NULL sealed_at (NULL → timestamp at seal
--       remains admitted; idempotent same-value writes admitted).
--
-- T-15 compliance: this migration uses DROP TRIGGER and CREATE TRIGGER only.
-- It does not DROP TABLE or DROP COLUMN. The selvedge migrate runner's T-15
-- pre-check verifies this before applying.

PRAGMA foreign_keys = ON;

BEGIN;

-- ----------------------------------------------------------------------------
-- (b) Tighten T-13: sealed_at is immutable once non-NULL.
--
-- Old condition (migration 001):
--   WHEN OLD.sealed_at IS NOT NULL AND NEW.sealed_at IS NULL
-- New condition:
--   WHEN OLD.sealed_at IS NOT NULL AND NEW.sealed_at IS NOT OLD.sealed_at
--
-- Truth table on `IS NOT` semantics in SQLite:
--   OLD='A' NEW=NULL  → NULL IS NOT 'A' = 1  → fires (refused).  ✓
--   OLD='A' NEW='B'   → 'B'  IS NOT 'A' = 1  → fires (refused).  ✓ (the gap)
--   OLD='A' NEW='A'   → 'A'  IS NOT 'A' = 0  → admits no-op.     ✓
--   OLD=NULL NEW='A'  → first conjunct false → admits seal.       ✓
-- ----------------------------------------------------------------------------
DROP TRIGGER IF EXISTS t13_deliberations_sealed_immutable;
CREATE TRIGGER t13_deliberations_sealed_immutable
BEFORE UPDATE OF sealed_at ON deliberations
FOR EACH ROW
WHEN OLD.sealed_at IS NOT NULL AND NEW.sealed_at IS NOT OLD.sealed_at
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T13: sealed_at is immutable once non-NULL');
END;

-- ----------------------------------------------------------------------------
-- (a) Add T-06 triggers on `deliberations` UPDATE/DELETE for closed sessions.
--
-- Mirrors the pattern used for decisions, decision_alternatives, perspectives,
-- synthesis_points, commitments, and refs in migration 001. The seal handler
-- runs against an open session (T-06 admits open); a session-close (which
-- moves status open → closed) is handled by T-02/T-11 at its own seam.
-- ----------------------------------------------------------------------------
CREATE TRIGGER t06_deliberations_no_mut_after_close_upd
BEFORE UPDATE ON deliberations
FOR EACH ROW
WHEN (SELECT status FROM sessions WHERE session_id = OLD.session_id) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: deliberation belongs to a closed session');
END;

CREATE TRIGGER t06_deliberations_no_mut_after_close_del
BEFORE DELETE ON deliberations
FOR EACH ROW
WHEN (SELECT status FROM sessions WHERE session_id = OLD.session_id) = 'closed'
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T06: deliberation belongs to a closed session');
END;

-- Record the migration. The selvedge migrate runner replaces the placeholder
-- with the file's real sha256 after executescript completes.
INSERT INTO schema_migrations (name, sha256) VALUES ('002-tighten-deliberation-immutability.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
