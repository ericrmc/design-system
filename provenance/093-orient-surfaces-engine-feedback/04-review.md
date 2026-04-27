---
session: 093
title: orient-surfaces-engine-feedback — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high**: test_orient_markdown_renders_feedback_table calls selvedge_cli([orient]) and discards the result; assertions only run against a subsequent subprocess call. Dead code that obscures intent.
  - **fixed.** Removed the dead selvedge_cli call; markdown test now uses subprocess only with rc + stderr assertion.
- **medium**: head extraction uses split first-line; if body_md starts with a blank line the rendered table cell is empty.
  - **fixed.** Added _first_nonempty_line helper; head picks first non-empty line capped at 120 chars; covered by test_orient_head_skips_leading_blank_lines.
- **low**: alias fallback for engine_feedback rows missing object_id is untested.
  - **fixed.** Added test_orient_falls_back_when_feedback_object_missing covering the LEFT JOIN orphan-row path.
