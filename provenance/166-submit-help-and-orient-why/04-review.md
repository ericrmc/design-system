---
session: 166
title: submit-help-and-orient-why — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: Example JSON payloads in _schemas.py use placeholder syntax (<N>, <id>, <pid>, <cid>, etc.) instead of valid JSON literals; operators following submit-help would fail to parse examples.
  - **fixed.** Replaced placeholder tokens (<N>, <id>, etc.) with valid JSON literals across all 37 example payloads; added test that json.loads succeeds for every example.
- **high**: Disjunction fields in schema (issue_id or alias, harness_id or alias) listed as required but handlers use optional .get() checks.
  - **fixed.** Refactored disjunctions out of required[] into a new any_of[] slot; submit-help renders them under a One of header with explicit either-or wording.
- **medium**: submit-help cmd_submit_help function handles unknown kind with helpful suggestions, returns exit code 2 correctly.
  - **fixed.** (no disposition recorded)
- **medium**: Schema marks disjunctive fields (e.g. issue_id|alias) as required in single entry; correct interpretation is one-of-two is required, but schema notation is ambiguous to operators reading docs.
  - **fixed.** Same fix as RF-188: any_of[] slot disambiguates id-or-alias patterns from required-both.

## Terminal passes

- **iteration 1** — findings @ `a3c25cd`
  - Audited FR-S161-15: schemas, submit-help, orient changes; found invalid JSON examples and ambiguous schema notation for disjunctive fields.
- **iteration 2** — clean @ `a3c25cd`
  - T-30 iteration 2: all three iteration-1 fixes verified; no regressions found. RF-187/188/190 hold.
