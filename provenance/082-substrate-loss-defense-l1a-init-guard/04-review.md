---
session: 082
title: substrate-loss-defense-l1a-init-guard — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: Missing test: init --really-force without --force succeeds against missing substrate
  - **fixed.** test_init_really_force_succeeds_on_missing_substrate added in state/tests/test_init_guard.py
- **high**: No test coverage for corrupt/partial substrate (sessions table absent despite .sqlite file existing)
  - **fixed.** test_init_force_admits_corrupt_substrate + test_init_force_admits_partial_init_no_sessions_table added; docstring clarifies guard treats no-sessions-table state as not-live by design.
- **medium**: Race condition window: session count check closes DB, then another process could add sessions before unlink executes
  - **adjudicated.** Race window between count-check and unlink is acknowledged narrow: single-agent operation, no concurrent writers in self-development workflow, SQLite WAL provides partial protection, blast-radius reduced further once L3 boundary snapshots ship in S083 per FR-S081-11. Not gating at engine-v51.
- **medium**: Refusal message phrasing "--force will not unlink a populated substrate" is unclear; --force does unlink if sessions table is absent or empty
  - **fixed.** Refusal message phrasing clarified: --force is refused on a substrate with active session rows; test_init_force_refusal_message_clarity asserts the new wording.
- **low**: No test for sessions table with NULL count or other edge NULL states
  - **adjudicated.** NULL-state test gap is minor; COUNT(*) always returns integer in SQLite; test design exhausts practical scenarios per 5-test suite
- **medium**: Boilerplate part-two lacks explicit allowlist for legitimate subagent writes (submit review-finding, submit engine-feedback-disposition) vs. forbidding schema-mutation-only writes
  - **adjudicated.** Part-one boilerplate already grants permission via Author payloads run bin/selvedge submit ...; part-two is a closed list of forbidden destructive ops not an allowlist of permitted submits. Enumerating permitted submit kinds would be open-ended and inverts the discipline shape.
- **low**: Refusal message references unshipped bin/selvedge restore command (OI-S081-4); could confuse operator until shipped
  - **adjudicated.** Message references OI-S081-4 (restore CLI) which is properly scheduled for S083; forward-reference appropriate until shipped

## Terminal passes

- **iteration 2** — clean @ `2efa34cc8bfa`
  - Iteration 2 reviewer subagent verified RF-9 RF-10 RF-12 fixed and RF-11 RF-14 adjudicated; 0 new findings; 294 pytest pass; T-30 admits close.
