---
session: 103
title: pytest-cli-coverage — assessment
engine_version_at_open: engine-v30
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

70 tests pass, pytest-cov wired (36% baseline). User asks to lift coverage by adding tests for Path A submit handlers, top-level commands, and export pipeline (closes OI-S090-2).

## Agenda

1. Add tests for top-level commands: validate, subtract-eligibility, recover, query, schema.
2. Add tests for Path A submit kinds: decision-record, perspective-position, perspective-claim, review-finding, finding-disposition, close-record, legacy-import, spec-section, spec-clause.
3. Add tests for issue/feedback kinds: issue-disposition, issue-link, issue-note, engine-feedback, engine-feedback-disposition, forward-reference-disposition.
4. Tighten test_orient_markdown_renders_feedback_table so its subprocess contributes to coverage.
5. Add export pipeline tests covering _export_session_provenance and _export_issues.
6. Run reviewer subagent on the new test code; address medium-or-higher findings.
7. Author engine-feedback row reflecting friction/wins; dispose stale FRs and OI-S090-2.
