-- Migration 038: spec_clauses.source_decision_v2_id NOT NULL on new rows.
-- engine-v49 unchanged.
--
-- Why:
--   D-28 + DV-S179-1 close OI-086-001 by-mechanism. spec_clauses currently
--   admits NULL source_decision_v2_id which breaks decision-record →
--   spec-clause traceability. At S179 there are 747 NULL rows in legacy
--   data; backfill all 747 from spec_versions.source_decision_v2_id is
--   non-trivial because not every clause's authoring DV is captured.
--   D-28 C-2 cross-family convergence applies: legacy preserved, NEW rows
--   refused via BEFORE INSERT trigger.
--
--   Future migration may backfill legacy rows by joining spec_clauses to
--   spec_versions via spec_section_id; that is a separate scope item per
--   FR-S179-1 if review-loop bandwidth allows in a future session.
--
-- T-15 compliance:
--   Additive trigger only — no DROP, no ALTER, no CHECK relaxation. No
--   T-15-CALIBRATED block needed.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TRIGGER t35_spec_clauses_source_dv_required_on_insert
BEFORE INSERT ON spec_clauses
FOR EACH ROW
WHEN NEW.source_decision_v2_id IS NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T35: spec_clauses requires non-NULL source_decision_v2_id; legacy NULL rows preserved by trigger fires only on INSERT');
END;

INSERT INTO schema_migrations (name, sha256) VALUES ('038-spec-clauses-source-decision-v2-id-trigger.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
