---
session: 103
title: pytest-cli-coverage — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: test_path_a_kinds review_finding alias check is tautological (startswith RF-S only); does not pin the wno-iteration-id format.
  - **fixed.** addressed in DV-S103-1 followup commit; assertions tightened per reviewer.
- **high**: test_path_a_kinds decision_record alias check is tautological (startswith DV-S only); should pin DV-S{wno:03d}-{decision_no}.
  - **fixed.** addressed in DV-S103-1 followup commit; assertions tightened per reviewer.
- **high**: test_export dry_run negation assertion is fragile; should be explicit not exists rather than or-clause.
  - **fixed.** addressed in DV-S103-1 followup commit; assertions tightened per reviewer.
- **high**: test_issue_kinds engine_feedback_disposition missing-identifier test should also pin the validation message string.
  - **fixed.** addressed in DV-S103-1 followup commit; assertions tightened per reviewer.
- **medium**: test_top_level_commands schema_unknown_table_is_handled accepts any rc; should pin a single expected outcome.
  - **fixed.** addressed in DV-S103-1 followup commit; assertions tightened per reviewer.
- **medium**: test_export session write only checks substring of one file; should also assert structural markers (Assessment heading).
  - **fixed.** addressed in DV-S103-1 followup commit; assertions tightened per reviewer.
- **medium**: test_path_a_kinds perspective_position only asserts object_id is not None; should verify object_kind and typed_row_id pair.
  - **fixed.** addressed in DV-S103-1 followup commit; assertions tightened per reviewer.
- **low**: test_existing_kinds orient_markdown seeds engine_feedback via raw SQL; reviewer flagged but this test exercises orient renderer not handler — adjudicate.
  - **adjudicated.** test_orient_markdown_renders_feedback_table targets the orient renderer, not the engine-feedback handler; raw-SQL seed is appropriate here.
