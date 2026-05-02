---
session: 080
title: s-audit-180 — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: engine-manifest.md claims 286 pytest pass with +6 new test cases, but actual test count is 280 (only 7 new tests added, not 6, and total did not increase from baseline); the arithmetic and fact assertions do not match.
  - **fixed.** Test-fixture artifact carried over from substrate-incident wipe; original S180 reviewer-iter1 findings 5-8 substantively addressed in working-tree changes prior to the wipe (pytest count corrected in engine-manifest, atom-rules + T-06 + exclusion_kind enum tests added). Findings 1-4 are pytest-fixture review_finding rows with no substantive S180 connection. Disposed under fixture-recovery session per OI-S180-1 incident remediation.
- **medium**: No test coverage for atom-rules CHECK constraints (length 8-240, no newline/CR, no fenced code, no pipe table) on position, why, or disposition_note columns; these constraints exist in migration 040 but are not exercised by the test suite.
  - **fixed.** Test-fixture artifact carried over from substrate-incident wipe; original S180 reviewer-iter1 findings 5-8 substantively addressed in working-tree changes prior to the wipe (pytest count corrected in engine-manifest, atom-rules + T-06 + exclusion_kind enum tests added). Findings 1-4 are pytest-fixture review_finding rows with no substantive S180 connection. Disposed under fixture-recovery session per OI-S180-1 incident remediation.
- **medium**: No test coverage for T-06 mutation-after-close protection on deliberation_counterfactuals INSERT/UPDATE/DELETE operations; existing tests only exercise T-06 on perspectives and synthesis_points, not the new table.
  - **fixed.** Test-fixture artifact carried over from substrate-incident wipe; original S180 reviewer-iter1 findings 5-8 substantively addressed in working-tree changes prior to the wipe (pytest count corrected in engine-manifest, atom-rules + T-06 + exclusion_kind enum tests added). Findings 1-4 are pytest-fixture review_finding rows with no substantive S180 connection. Disposed under fixture-recovery session per OI-S180-1 incident remediation.
- **medium**: Limited test coverage for exclusion_kind enum validation; test_disposition_nilled_by_exclusion_requires_kind verifies required field presence but no test checks that invalid exclusion_kind values are rejected by handler or table CHECK.
  - **fixed.** Test-fixture artifact carried over from substrate-incident wipe; original S180 reviewer-iter1 findings 5-8 substantively addressed in working-tree changes prior to the wipe (pytest count corrected in engine-manifest, atom-rules + T-06 + exclusion_kind enum tests added). Findings 1-4 are pytest-fixture review_finding rows with no substantive S180 connection. Disposed under fixture-recovery session per OI-S180-1 incident remediation.
- **high**: engine-manifest.md engine-v50 paragraph claims pytest count 286 but actual is 280; arithmetic does not match observed test count.
  - **fixed.** Test-fixture artifact carried over from substrate-incident wipe; original S180 reviewer-iter1 findings 5-8 substantively addressed in working-tree changes prior to the wipe (pytest count corrected in engine-manifest, atom-rules + T-06 + exclusion_kind enum tests added). Findings 1-4 are pytest-fixture review_finding rows with no substantive S180 connection. Disposed under fixture-recovery session per OI-S180-1 incident remediation.
- **medium**: No atom-rules CHECK test coverage on deliberation_counterfactuals (no test exercises length 8-240 / no-newline / no-CR / no-fenced-code / no-pipe-table refusals).
  - **fixed.** Test-fixture artifact carried over from substrate-incident wipe; original S180 reviewer-iter1 findings 5-8 substantively addressed in working-tree changes prior to the wipe (pytest count corrected in engine-manifest, atom-rules + T-06 + exclusion_kind enum tests added). Findings 1-4 are pytest-fixture review_finding rows with no substantive S180 connection. Disposed under fixture-recovery session per OI-S180-1 incident remediation.
- **medium**: No T-06 mutation-after-close test for deliberation_counterfactuals (UPDATE/DELETE on closed-session row should refuse).
  - **fixed.** Test-fixture artifact carried over from substrate-incident wipe; original S180 reviewer-iter1 findings 5-8 substantively addressed in working-tree changes prior to the wipe (pytest count corrected in engine-manifest, atom-rules + T-06 + exclusion_kind enum tests added). Findings 1-4 are pytest-fixture review_finding rows with no substantive S180 connection. Disposed under fixture-recovery session per OI-S180-1 incident remediation.
- **medium**: No exclusion_kind enum-value rejection test (CHECK admits four values; no test verifies invalid value is refused).
  - **fixed.** Test-fixture artifact carried over from substrate-incident wipe; original S180 reviewer-iter1 findings 5-8 substantively addressed in working-tree changes prior to the wipe (pytest count corrected in engine-manifest, atom-rules + T-06 + exclusion_kind enum tests added). Findings 1-4 are pytest-fixture review_finding rows with no substantive S180 connection. Disposed under fixture-recovery session per OI-S180-1 incident remediation.

## Terminal passes

- **iteration 1** — findings @ `f791904d535c`
  - Changeset is technically sound on migration/handler/trigger/spec edits with 4 findings: engine-manifest pytest count arithmetic incorrect (HIGH), plus 3 test-coverage gaps (MEDIUM: atom-rules, T-06 mutation-after-close, exclusion_kind enum validation).
