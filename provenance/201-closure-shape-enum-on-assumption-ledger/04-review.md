---
session: 201
title: closure-shape-enum-on-assumption-ledger — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: Missing test coverage for superseded(supersession) to closed transition: round-trip auto-clear/carry-forward not exercised.
  - **fixed.** Added 5 new tests covering closed/superseded round-trip carry-forward and override paths.
- **high**: Reviewer suggested superseded(supersession) to closed without explicit closure_shape should refuse; per spec carry-forward of supersession to closed is admitted as supersession is in the closed enum.
  - **adjudicated.** Not-a-bug: supersession is in closed CHECK enum; carry-forward to closed is intentional closure-by-supersession semantic per spec; reviewer misread.
- **medium**: Migration 051 docstring auto-clear semantics for closed-to-superseded transitions not documented; superseded narrows to NULL or supersession only.
  - **adjudicated.** Migration sha-drift on already-applied 051 deferred per S199 RF-82 precedent; auto-clear semantic documented in handler docstring (RF-90 fix).
- **medium**: Test gap: no coverage for closed(convergence) to superseded round-trip or subsequent superseded to closed with new shape.
  - **fixed.** Round-trip and superseded-shape-narrowing tests added with RF-86 fix.
- **medium**: Docstring drift in _submit_assumption_status_update: superseded narrowing semantic and superseded-to-closed carry-forward not explained.
  - **fixed.** Expanded _submit_assumption_status_update docstring naming superseded narrowing + closed carry-forward + auto-clear set semantics.
- **low**: Index idx_assumption_ledger_closure_shape appropriate and follows session/status/decision precedent.
  - **adjudicated.** Pattern-conforming; cosmetic.
- **low**: Enum consistency verified across SQL CHECK + _CLOSURE_SHAPE_ENUM + spec clause + test fixtures.
  - **adjudicated.** Cross-surface consistency confirmed.
- **low**: Migration 051 T-15-CALIBRATED rebuild verified: INSERT SELECT with closure_shape=NULL backfills 4 existing rows preserving FKs and indexes.
  - **adjudicated.** Rebuild correctness confirmed.

## Terminal passes

- **iteration 1** — clean @ `3ee018baa3a3`
  - S201 reviewer iter-1 surfaced 8 findings: 3 fixed (RF-86 RF-89 RF-90 round-trip tests + handler docstring) + 2 adjudicated (RF-87 misread + RF-88 sha-drift-deferred) + 3 LOW adjudicated; pytest 429 ok.
