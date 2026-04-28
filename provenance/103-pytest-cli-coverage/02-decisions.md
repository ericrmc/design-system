---
session: 103
title: pytest-cli-coverage — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Lift CLI test coverage from 36% to 78% by exercising Path A handlers, top-level commands, and export pipeline (closes OI-S090-2).

**Kind:** procedural.  **Outcome:** adopt issue `OI-S090-2`.

**Why.**

- (operator_directive) Operator asked for tests against the targets named at S102 close.
- (operator_directive) FR-S099-10 / FR-S100-5 / FR-S101-6 / FR-S102-7 all named OI-S090-2 as the next pickup.

**Effects.**

- creates state/tests/test_top_level_commands.py covering validate, subtract-eligibility, recover, query, schema.
- creates state/tests/test_path_a_kinds.py covering nine Path A submit handlers.
- creates state/tests/test_issue_kinds.py covering issue and engine-feedback handlers.
- creates state/tests/test_export.py covering _export_session_provenance and _export_issues.
- modifies state/tests/test_existing_kinds.py: orient-markdown subtest now uses selvedge_cli fixture for coverage.
- closes_issue OI-S090-2 — Pytest coverage for Path A handlers and export round-trip is now in place at 78% baseline.
