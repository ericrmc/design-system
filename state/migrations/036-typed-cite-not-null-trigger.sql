-- Migration 036: typed-cite T-34 BEFORE INSERT (engine-v49 unchanged).
--
-- Why:
--   D-28 closes OI-086-003 by-mechanism. cite-typing rule (DV-S158-1, EF-S157-1)
--   names cite-required bases for decision_supports + alternative_rejections;
--   the substrate currently admits NULL cited_object_id even when basis falls
--   in the cite-required set. Migration 021 records the historical residual
--   (132 decision_supports + 153 alternative_rejections measured at S179);
--   D-28 C-2 cross-family convergence: legacy preserved, NEW rows refused.
--
--   Trigger fires only on INSERT, so existing rows are untouched. The
--   handler resolve_alias_to_object_id pre-walks the cite path before this
--   trigger fires; failure on the handler side raises E_REFUSAL_T01 with a
--   basis-aware hint. T-34 is the substrate-side defense-in-depth refusing
--   any direct INSERT bypass with NULL cited_object_id on cite-required basis.
--
-- Cite-required basis sets (per prompts/development.md §5):
--   decision_supports.basis IN (prior_decision, spec_clause, deliberation,
--     review_finding, engine_feedback, constraint, operator_directive)
--   alternative_rejections.basis: closed enum of 8 bases; cite-required
--     subset is empty per current cite-typing rule (rejections may cite
--     but are not required to). Trigger applies only to decision_supports.
--
-- T-15 compliance:
--   Additive triggers only — no DROP, no ALTER, no CHECK relaxation.
--   No T-15-CALIBRATED block needed.

PRAGMA foreign_keys = ON;

BEGIN;

CREATE TRIGGER t34_decision_supports_cite_required_not_null
BEFORE INSERT ON decision_supports
FOR EACH ROW
WHEN NEW.basis IN (
    'prior_decision','spec_clause','deliberation','review_finding',
    'engine_feedback','constraint','operator_directive'
) AND NEW.cited_object_id IS NULL
BEGIN
    SELECT RAISE(ABORT, 'E_REFUSAL_T34: decision_supports basis requires non-NULL cited_object_id; legacy NULL rows preserved by trigger fires only on INSERT');
END;

INSERT INTO schema_migrations (name, sha256) VALUES ('036-typed-cite-not-null-trigger.sql', 'COMPUTED-AT-APPLY-TIME');

COMMIT;
