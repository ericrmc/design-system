---
session: 118
title: enforce-opens-issue-target-issue-id — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **medium**: Handler control flow for opens_issue branch lacks an explicit comment that the catchall target-resolve at line 1259 is intentionally skipped; future maintainer could refactor incorrectly.
  - **fixed.** Added comment block (cli.py L1255-1256) flagging that the catchall target-resolve at L1259 is intentionally skipped for opens_issue.
- **high**: prompts/development.md step 5 documents closes_issue dispatch but says nothing about opens_issue target-required surface; spec lags engine-v34 contract.
  - **fixed.** prompt-development v7 (SPEC-prompt-development-v7) adds a paragraph after the closes_issue paragraph documenting opens_issue target-required surface, status=open precondition, separate issue creation step, and T-31 refusal.
- **high**: Migration 022 has no down-migration or rollback guidance for engine-v34 to engine-v33 reversion.
  - **adjudicated.** Out of scope. Selvedge has no rollback discipline; migrations are forward-only and engine-version reversion would require a calibrated rebuild, not a down-migration. General operational gap, not session-specific.
- **medium**: Migration 022 comment does not flag that 8 legacy NULL target_issue_id rows persist and continue to depend on the word-boundary regex fallback in _decisions_citing_issue.
  - **fixed.** Added Known limitation block to migration 022 comment header documenting the 8 legacy NULL rows and chain-walk regex fallback dependency.
- **medium**: opens_issue handler does not validate that the resolved issue is in status open; an opens_issue effect could reference a resolved or superseded issue, which is logically inconsistent with the effect kind.
  - **fixed.** Handler now checks resolved issue status==open and refuses with E_VALIDATION otherwise; smoke-tested against OI-085-001 (status=resolved) which correctly refused.
## Iteration 2

- **critical**: opens_issue handler dereferences cur_status without null-guarding; if an issue row were deleted between _resolve_issue_alias and the status SELECT, fetchone() returns None and the ["status"] subscript raises TypeError.
  - **fixed.** Added defensive null-guard: `cur_status is None or cur_status[status] != open`. Error path emits status=DELETED when fetchone returns None.
- **high**: Status=open precondition could be read as preventing same-write_tx issue creation + opens_issue reference; should be adjudicated as false positive since submit-issue and submit-decision-record are already separate write_tx calls.
  - **adjudicated.** False positive. submit-issue and submit-decision-record are separate write_tx invocations by construction; there is no in-band path that creates an issue and references it within the same transaction.
- **medium**: Migration 022 comment cites _decisions_citing_issue at cli.py L2806 but the function is at L2830; off-by-24 stale line number.
  - **fixed.** Migration 022 comment now cites cli.py L2830 (verified via grep) instead of stale L2806; recorded sha synced.
- **medium**: Comment phrasing intentionally skipped is ambiguous; rephrase to make typed-reference rationale obvious to future maintainer.
  - **fixed.** Comment now reads The generic target_object_id resolution further down is not used for opens_issue: the typed reference is target_issue_id, not target_object_id.
- **low**: Status-check error message phrase references a freshly opened issue is misleading; better to state the precondition as references an issue with status=open.
  - **fixed.** Error message now reads opens_issue effect must reference an issue with status=open, but [alias] has status=X; precondition phrased directly.
## Iteration 3

- **critical**: closes_issue branch (cli.py L1234) has the same unguarded fetchone()[status] pattern that opens_issue iter-2 fixed; symmetric null-guard required for consistent defensive posture.
  - **fixed.** closes_issue branch (cli.py ~L1234) now null-guards cur_status with E_NOT_FOUND raise; parity comment cites opens_issue branch.

## Terminal passes

- **iteration 1** — findings @ `20c2da3`
  - iter-1 surfaced 2 high + 3 medium findings; all disposed (4 fixed via code/migration/spec edits, 1 adjudicated as out-of-scope rollback).
- **iteration 2** — findings @ `20c2da3`
  - iter-2 surfaced 1 critical (null-deref) + 1 high (false positive) + 2 medium + 1 low; all disposed (4 fixed, 1 adjudicated).
- **iteration 3** — findings @ `20c2da3`
  - iter-3 surfaced 1 critical parity finding on closes_issue null-guard; addressed via symmetric defensive raise.
- **iteration 4** — clean @ `20c2da3`
  - iter-4 reviewer confirmed closes_issue and opens_issue null-guards consistent; substrate state correct; no further findings.
