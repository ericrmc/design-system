---
session: 153
title: close-record-items-required — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Tighten T-39 with companion T-40 close_state_items requirement at session-close, plus handler-side empty-items refusal.

**Kind:** schema_migration.  **Outcome:** adopt migration `029-close-state-items-required-at-close`.

**Why.**

- (engine_feedback) EF-S151-2 surfaced close_state_items regression: S147 S148 S149 S150 close-records each carry zero rows; T-39 admits empty close-records by design. [EF-S151-2]
- (operator_directive) FR-S152-19 directs tighten-T-39 to refuse close-record with empty items or refuse session-close on items count below threshold.
- (prior_decision) DV-S134-1 established the trigger-level placement plus handler-side defence-in-depth pattern for close-record sequencing gates; T-40 extends that pattern. [DV-S134-1]
- (constraint) Constraints property 5 detection without a structural feedback loop into prevention does not correct anything; trigger-level enforcement closes the loop.
- (review_finding) Pytest run 227 passed including 21 close-record-sequencing assertions covering T-40 trigger T-40 handler admit-1-item round-trip plus prior T-39 T-39b retained.

**Effects.**

- adds_migration Migration 029: T-40 trigger refuses session-close when close_state_items count is zero.
- modifies _submit_close_record refuses empty items[] at handler pre-check with E_VALIDATION.
- bumps_engine engine-v43 to engine-v44 via workspace_metadata UPDATE atomic with trigger creation.

**Rejected alternatives.**

- **R-1.1.** Per-facet coverage threshold: refuse session-close unless every required facet engine_version what_was_done state_at_close open_issues next_session_should validator_summary appears at least once.
  - (too_large_for_session) Per-facet enforcement couples the substrate gate to operator workflow shape and risks false refusals on compact sessions; threshold needs its own decision.
- **R-1.2.** Handler-only refusal without T-40 SQL trigger: rely on _submit_close_record raising E_VALIDATION on empty items[] without a trigger-level gate.
  - (preserves_legacy_path) Direct sqlite3 INSERT or future handler bypassing _submit_close_record would recreate the gap by a different route; matches DV-S134-1 reasoning.
