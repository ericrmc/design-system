---
session: 109
title: subtract-constraints-from-manifest — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: PROMPT.md referenced specifications/constraints.md in two places (spec list and operating discipline), creating a dangling load directive after removal.
  - **fixed.** Both references removed from PROMPT.md in S109 post-reviewer-pass edits.
- **high**: tools/validate.sh required specifications/constraints.md, causing the precommit gate to fail with exit 1 after the file was archived.
  - **fixed.** require line removed from tools/validate.sh in S109 post-reviewer-pass edits.
- **low**: workspace.md line 12 has a parenthetical citation to constraints.md (historical context, not a load directive).
  - **adjudicated.** Reference explains why workspace.md was written; not a load directive. Engine coherence unaffected. No fix warranted.
