---
session: 153
title: close-record-items-required — assessment
engine_version_at_open: engine-v43
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S147-S150 close-records carry zero close_state_items rows; T-39 admits empty close-records, EF-S151-2 surfaced calibration.

## Agenda

1. Address FR-S152-19 / EF-S151-2: tighten T-39 so empty close-records cannot land at session-close.
2. Decide enforcement layer: handler-side refusal in _submit_close_record plus trigger-side refusal at session-close (defence in depth, mirroring T-39 / T-39b).
3. Decide minimum-item threshold: start at >=1 to catch the regression; defer per-facet coverage as a separate decision.
4. Write migration 029 adding T-40 close_state_items required at session-close.
5. Add handler-side refusal in _submit_close_record when items array is empty.
6. Run coding review loop; address findings to clean.
7. Author engine-feedback row, dispose FR-S152-19 and EF-S151-2, close session, export, commit, push.
