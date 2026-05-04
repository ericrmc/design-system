---
session: 199
title: prospective-scoping-discipline-gate — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: Index idx_engine_feedback_session_body migration comment claims composite (session_id, body_md) but actual CREATE INDEX is single-column on session_id; comment overpromises versus implementation.
  - **adjudicated.** RF-82 adjudicated low-impact: the migration comment overpromises composite (session_id, body_md) but the actual single-column session_id index is functionally correct (gate query SELECT body_md WHERE session_id=? has Python prefix-check; SQL has no LIKE filter). Comment-vs-code drift recorded as forward-direction; defer rename + comment-fix to next migration to avoid sha drift on applied 050.
- **high**: Multi-row scoping-pass gate logic returns False on first failing row without checking subsequent rows that may pass; spec says any valid row admits but implementation has first-row-fails-short-circuit semantics.
  - **fixed.** RF-83 fix: rewrote _scoping_pass_receipt_present loop to scan every scoping-pass row and admit if ANY row passes guards. Track last_hint for actionable refusal text; saw_scoping_pass flag distinguishes prefix-absent vs guards-failed cases. Added test_multi_row_first_fails_second_passes covering this case explicitly. 13/13 tests pass.
- **high**: Test coverage gap: _session_produced_substantive_artefact() admits spec_versions row as substantive but no test exercises that path; only DV-substantive path tested.
  - **fixed.** RF-84 fix: added test_spec_version_makes_session_substantive submitting an initial spec-version row and verifying T-41 fires. Test cleanup removes the fixture file so it doesn't leak to git. Covers _session_produced_substantive_artefact() spec_versions branch.
- **medium**: Test coverage gap: no explicit test verifying non-nil scoping-pass: bodies (e.g. scoping-pass: 1 ...) bypass nil_attestation guards #1+#2; current admit tests pass through but semantics not codified.
  - **fixed.** RF-85 fix: added test_non_nil_body_bypasses_nil_guards verifying scoping-pass: 2 ... body with no exclusions-applied and no pattern-name still admits. Codifies non-nil bodies bypass nil_attestation guards #1+#2.

## Terminal passes

- **iteration 2** — clean @ `0617917a2977`
  - iter-2 clean: RF-83/84/85 fixed (multi-row gate logic + spec_version-substantive test + non-nil-bypass test); RF-82 adjudicated low-impact-comment-drift; pytest 408 ok up 13 from S198 395.
