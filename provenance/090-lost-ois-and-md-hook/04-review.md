---
session: 090
title: lost-ois-and-md-hook — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **medium**: Zero pytest coverage for _submit_spec_version supersession path; bug recurred S087/S088/S089. T-20 loop 1 (handler reorder).
  - **fixed.** Added test_spec_version_supersedes_flips_prev_to_superseded and test_spec_version_two_active_refused_by_t03; both pass.
- **medium**: Hook bypass via SELVEDGE_EXPORT_CONTEXT=1 was silent; global export of the var would disable guard undetectably. T-20 loop 2 (markdown hook).
  - **fixed.** Added stderr log line on bypass activation.
- **medium**: Bash-mediated writes outside hook scope; not documented. T-20 loop 2 (markdown hook).
  - **fixed.** Added Scope and known gaps section to docstring documenting Bash limitation, global-export visibility, and outbound symlink edge case.
- **medium**: $CLAUDE_PROJECT_DIR unquoted in .claude/settings.json command; breaks on workspace paths with spaces per Claude Code docs. T-20 loop 2 (markdown hook).
  - **fixed.** Wrapped variable in JSON-escaped double quotes.
