-- Migration 018: grant __cli__ insert capability on review_passes.
-- engine-v31 follow-up (S104; should have been part of 017 but recorded as
-- a separate migration rather than amending 017's already-checksummed row).
--
-- Without this row the submit review-pass handler refuses with E_REFUSAL_T12
-- ("role '__cli__' not permitted to insert review_passes"). The omission
-- was caught by the implementer during CLI handler authoring.

PRAGMA foreign_keys = ON;

BEGIN;

INSERT INTO role_write_capabilities (role, table_name, write_op)
VALUES ('__cli__', 'review_passes', 'insert');

INSERT INTO schema_migrations (name, sha256) VALUES ('018-review-passes-role-capability.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
