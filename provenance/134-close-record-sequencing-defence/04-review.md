---
session: 134
title: close-record-sequencing-defence — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: T-39 fires only on UPDATE; INSERT with status=closed bypasses gate. Add T-39b INSERT-guard for defence-in-depth.
  - **fixed.** Migration 028 adds T-39b INSERT-guard refusing INSERT INTO sessions with status=closed without close_records; companion to T-39 (UPDATE-side). Engine-v41 unchanged.
- **medium**: SQLite trigger ordering on UPDATE OF status is unspecified; T-39 may mask T-11/T-18/T-19/T-20/T-30 refusals when multiple gates would fire.
  - **adjudicated.** SQLite trigger ordering on UPDATE OF status is unspecified; this risk class predates T-39 (T-11/T-18/T-19/T-20/T-30 share it). Operators iterate close attempts to discover next-gate; not addressed in S134.
- **high**: _validate_atom called after _check_role_capability in _insert_atom; the role-capability SELECT is SQL so the 'before any SQL fires' contract is inaccurate.
  - **fixed.** Reordered _validate_atom before _check_role_capability in _insert_atom (selvedge/submit/_helpers.py). Docstring updated to say 'before any atom INSERT or SQL role-capability lookup' for accuracy.
- **medium**: _ATOM_LENGTH_TIERS lists only special tiers; default 8-240 fallback is correct but creates fragility if a future migration adds a tier-specific atom_type without updating the dict.
  - **fixed.** Added comment block above _ATOM_LENGTH_TIERS noting fallback contract and naming the future-migration obligation when adding tier-specific atom_types.
- **high**: _submit_close_record pre-validates atoms before INSERTs; assessment, decision_v2, harness, etc. do not. Asymmetric coverage of the partial-INSERT-then-rollback class.
  - **adjudicated.** Asymmetric pre-validation is DV-S134-1's documented scope: close-record surfaced the gap. Other handlers use per-atom _validate_atom in _insert_atom; write_tx atomicity prevents persisted partial state. Manifest v42 explicit.
- **medium**: _submit_close_record pre-validation assumes p['items'] is a list; malformed payload surfaces TypeError instead of structured error.
  - **adjudicated.** Payload structure validation (items must be list) is a general issue spanning every atom-bearing handler in the engine; out of scope for S134 which is about close-record sequencing specifically. Future review opportunity.
- **high**: submit_minimal_close_record fixture in conftest.py uses expect_ok=False; close-record failures are silently swallowed and tests proceed without close_record, causing T-39 to mask the test's actual assertion.
  - **fixed.** Changed submit_minimal_close_record fixture to use default expect_ok=True so close-record submission failures surface as test errors rather than being silently swallowed.
- **high**: No explicit test exercises T-39 refusal (close without close_record) or admission (close with close_record); regressions in trigger logic would not be caught.
  - **fixed.** Added test_t39_refuses_session_close_without_close_record, test_t39_admits_session_close_with_close_record, and test_t39b_refuses_direct_insert_of_closed_session in state/tests/test_close_record_sequencing.py.
- **medium**: No unit tests for _validate_atom covering each E_ATOM_* code, length tiers, field-path prefixing.
  - **fixed.** Added 11 unit tests for _validate_atom covering each E_ATOM_* code, length tier (default/spec_clause/legacy_import), field-path prefixing, and the GLOB pipe-table parity via single-pipe admission test.
- **medium**: No tests verify E_ATOM_* error codes propagate through CLI subprocess to callers as structured payloads.
  - **fixed.** Added 4 CLI-subprocess tests verifying E_ATOM_* codes propagate through the JSON error envelope: oversized close-record summary, oversized close-record items[i].text, oversized decision-record title, newline in close-record summary.
- **medium**: engine-manifest v41 claim that _submit_close_record pre-validation is 'asymmetric to other handlers' is implicit; manifest should make the scoping explicit.
  - **fixed.** engine-manifest v42 supersedes v41 with scope-limiting language: close-record-only payload pre-validation; other handlers rely on per-atom _validate_atom plus write_tx atomicity. Migration 028 also enumerated.
- **low**: tools/update-external-workspace.sh header reviewer marker says engine-v40; should bump to engine-v41 with S134 review note.
  - **fixed.** Updated tools/update-external-workspace.sh header marker to 'Last reviewed: engine-v41 (S134; migration 027 + T-39 + parse-time atom validator)'. Note migration enumeration is dynamic so 027/028 ship automatically.
- **medium**: Pipe-table validator uses count compared against 2; SQL CHECK uses GLOB pattern requiring at least two pipe chars. Equivalent but parity needs a clarifying comment.
  - **fixed.** Added a comment block above the pipe-table check in _validate_atom explaining the GLOB-equivalence: count of pipe chars >= 2 mirrors the SQL pattern requiring at least two pipes.
## Iteration 2

- **medium**: engine-manifest v42 body says engine-v41 unchanged but workspace_metadata.current_engine_version is engine-v42; narrative drift inside v42 paragraph requires correction.
  - **fixed.** engine-manifest v43 supersedes v42 with narrative correction; v43 names engine-v43 as the active engine version and explicitly cites the iter-1 v42 drift it corrects.

## Terminal passes

- **iteration 3** — clean @ `1bf8928da1`
  - iter-3 reviewer confirmed iter-2 narrative-correction (F180) landed correctly; engine-v43 active; all 220 tests pass; no NEW medium+ findings.
