---
session: 187
title: l5-close-time-export-expansion — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: Harness file reconciliation missing in _export_session_provenance: stale harness files are not deleted on rerun when harness rows vanish, mirroring the L5 reconciliation gap this session ships.
  - **adjudicated.** Out of scope for OI-S081-6: harness file reconciliation has a distinct invariant (cross-session anchoring of provenance/<open_wno>-<open_slug>/harnesses/<alias>.md plus T-06 post-seal immutability limiting the rows-vanished failure mode). FR opened to revisit as a separate slice; this session ships L5 only.
- **medium**: Test coverage gap mirrors finding 1: no test asserts that stale harness files are unlinked on rerun, parallel to test_l5_session_export_reconciles_stale_files.
  - **adjudicated.** Tracks adjudicated finding 28 (HIGH); the test gap follows the implementation gap. Resolution is the same FR for revisiting harness reconciliation as a separate slice with the cross-session anchoring invariant in scope.
- **medium**: Workspace-wide indexes (specifications/_versions.md and open-issues/index.md) lack an idempotency assertion across reruns of selvedge export --session N --write.
  - **fixed.** Extended test_l5_session_export_idempotent to snapshot specifications/_versions.md and open-issues/index.md alongside per-session files, asserting workspace-wide indexes are byte-identical across reruns.

## Terminal passes

- **iteration 1** — clean @ `46a767ce9a0e`
  - Reviewer iter-1: 1 HIGH + 2 MEDIUM surfaced; 30 fixed via idempotence-test extension; 28+29 adjudicated to FR for cross-session anchoring scope.
