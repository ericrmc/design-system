---
session: 153
title: close-record-items-required — close
engine_version_at_close: engine-v44
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

DV-S153-1 ships migration 029 + T-40 close_state_items required at session-close trigger plus handler-side empty-items refusal in _submit_close_record per EF-S151-2 calibration; engine-v43 to engine-v44.

## Engine version

- engine-v43 to engine-v44 via migration 029 atomic UPDATE of workspace_metadata.current_engine_version with T-40 trigger CREATE.
## What was done

- Wrote migration 029 introducing T-40 BEFORE UPDATE OF status ON sessions trigger refusing close-transition when close_records exists with zero close_state_items.
- Scoped T-40 WHEN clause to close_records EXISTS so T-39 and T-40 cover distinct failure modes; refusal codes E_REFUSAL_T39 and E_REFUSAL_T40 disambiguate.
- Added handler-side empty-items refusal in _submit_close_record raising E_VALIDATION before any INSERT; mirrors DV-S134-1 atom-validator defence-in-depth pattern.
- Updated _submit_minimal_close_record fixture to carry one well-formed item; added 4 pytest assertions covering T-40 trigger handler-side refusals plus admit-1-item round-trip.
- Coding review loop iter-1 surfaced 2 medium documentation findings F181 F182; both fixed; iter-2 confirmed clean; 227 pytest pass.
- Bumped engine-manifest from v43 to v44 via submit spec-version with inline body_md; added migration 029 row plus engine-v44 paragraph plus history sentence.
- Recorded DV-S153-1 substantive decision adopt schema_migration target migration 029 with 5 supports 3 effects 2 alternatives R-1.1 per-facet R-1.2 handler-only both rejected.
## State at close

- T-39 plus T-40 plus handler pre-check together close the close-record empty-items regression; future S147-S150-class events refused at three layers.
- Per-facet coverage threshold remains an open design question deferred to a future session; current minimum is one close_state_items row.
- 227 pytest assertions pass against engine-v44 substrate including 21 close-record-sequencing checks; review_passes recorded iter-1 findings plus iter-2 clean.
## Open issues

- OI-S151-1 reference_harness ergonomic-fix migrations 029-plus still open; the 029 number used here is for T-40 not for the harness scope-change ergonomic fixes.
- OI-S151-3 visibility-gap seam plus OI-S151-4 second-arc gate plus OI-S152-1 plus OI-S152-2 typed-conflict-primitive seam open.
- Per-facet coverage threshold for close_state_items not yet decided; R-1.1 deferred without an OI for now since the >=1 threshold catches the surfaced regression.
## What the next session should address

- Address FR-S152-16 plus OI-S151-1 plus OI-S152-1 jointly: ship migrations 030-plus for harness ergonomic fixes finding atom-length origin_session_id structural_trigger conflict_kind closure_kind.
- Or address FR-S152-17 plus OI-S151-3 visibility-gap seam in a spec_only session: deliberation-atom reachability from artefact-set for kind=substantive decisions.
- Or address FR-S152-18 plus EF-S151-1 transported finding triage into its own OI per FR-S151-17.
- Per-facet coverage threshold R-1.1 reopen if a future close-record reveals partial-facet shape that the >=1 gate admits and operators want refused.
- Triage 11 untriaged engine-feedback rows including EF-S153-1 just authored about T-40 layering and trigger WHEN-clause scope discipline.
## Validator at close

- 227 pytest pass against engine-v44; iter-2 review_pass clean; T-40 trigger and handler refusals exercised via 4 new assertions plus 21 total close-record-sequencing checks.
