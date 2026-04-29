---
session: 118
title: enforce-opens-issue-target-issue-id — assessment
engine_version_at_open: engine-v33
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S117 closed clean shipping cross-session anchor-trace v1; FR-S117-9 surfaces opens_issue effects carrying NULL target_issue_id 8/14 of the time forcing descriptor-substring fallback in chain-walk export.

## Agenda

1. Decide enforcement shape for opens_issue effects: pre-created issue + T-NN trigger only, in-band issue dispatch mirroring closes_issue, or both paths admitted.
2. Land migration adding T-NN refusing opens_issue effects with NULL target_issue_id; update _submit_decision_record opens_issue branch accordingly.
3. Run reviewer subagent loop on the migration and handler change; address every medium-or-higher finding.
4. Bump engine-manifest to engine-v34 and propagate workspace_metadata.current_engine_version inside the same migration.
5. Update prompts/development.md §5 to document the new opens_issue dispatch surface.
6. Close-time reflection: dispose FR-S117-9, dispose EF-S117-1 with citing decision, author S118 engine-feedback observation.
