-- Migration 012: T-25 lease-renewal monotonicity trigger on work_items.
-- Engine-v25 → engine-v25 (session 092, OI-S089-2).
--
-- Why:
--   T-16 (migration 010) refuses inserting/updating a leased work_item with
--   an already-expired lease_expires_at. It does not refuse a "renewal" that
--   moves lease_expires_at *backwards* while OLD.status='leased' and
--   NEW.status='leased' — i.e. trimming a live lease, which would let one
--   leaseholder shrink another holder's window.
--
--   T-25 makes lease renewal monotonic-forward: if both OLD and NEW are
--   leased and both lease_expires_at values are non-null, NEW value must
--   strictly exceed OLD value. Operations that legitimately reset the lease
--   (un-lease/complete/fail by setting NEW.status != 'leased' or
--   NEW.lease_expires_at IS NULL) are unaffected.
--
-- T-15 compliance: trigger creation only; no CHECK relaxation, no table
--   recreation. Standard ADD-only DDL.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TRIGGER t25_work_items_lease_renewal_monotonic
BEFORE UPDATE OF lease_expires_at ON work_items
FOR EACH ROW
WHEN OLD.status = 'leased'
 AND NEW.status = 'leased'
 AND OLD.lease_expires_at IS NOT NULL
 AND NEW.lease_expires_at IS NOT NULL
 AND NEW.lease_expires_at <= OLD.lease_expires_at
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T25: lease renewal must push lease_expires_at strictly forward');
END;

INSERT INTO schema_migrations (name, sha256) VALUES ('012-t25-lease-renewal.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
