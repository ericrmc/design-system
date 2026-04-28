---
session: 104
title: enforce-coding-review-loop — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: Fixture default change from coding to spec_only means most close-path tests no longer exercise t30 enforcement, masking potential future regression.
  - **adjudicated.** Reverting fixture to coding adds review-pass ceremony to 7 unrelated close-path tests. Dedicated test_coding_review_loop.py covers t30 happy/refuse/findings/halt paths. Decoupling tests from t30 follows methodology no-ceremony constraint.
- **medium**: T-30 and T-20 rely on implicit NULL-shortcircuit semantics in the MAX(iteration) subquery; future maintainers might refactor incorrectly.
  - **adjudicated.** NULL-shortcircuit correct: NOT EXISTS over zero-row WHERE iter=NULL is TRUE. test_t30_refuses_coding_close_without_review_pass covers empty-table case. Verbose alt requires mig 019 for marginal clarity.
- **medium**: _submit_review_pass did not validate iteration 1-4 range; CHECK trigger raised cryptic message instead of clean E_VALIDATION.
  - **fixed.** Added explicit iteration range check 1-4 in _submit_review_pass before INSERT; now raises E_VALIDATION on out-of-range, mirrored by test_review_pass_iteration_check_refuses_zero and refuses_five.
- **medium**: _submit_review_pass did not validate halt_issue_alias presence on outcome=nonconverged at the application layer; relied on trigger refusal.
  - **fixed.** Added explicit E_VALIDATION when outcome=nonconverged but halt_issue_alias missing; trigger t_review_pass_nonconverged_requires_halt_issue remains as defense-in-depth.
- **medium**: Export pathway in _export_session_provenance for review_passes calls _atom_text without explicit handling of missing atom rows.
  - **adjudicated.** review_passes.summary_atom_id is NOT NULL with FK to text_atoms under PRAGMA foreign_keys=ON. Missing-atom case cannot occur without FK violation. _atom_text degrades to empty string if FK is ever bypassed.

## Terminal passes

- **iteration 2** — clean @ `4618a3e`
  - iter-2 clean: 2 medium fixed, 1 high and 2 medium adjudicated; 140 pytest pass; loop converged.
