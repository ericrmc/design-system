---
session: 113
title: backfill-decision-targets-supports — assessment
engine_version_at_open: engine-v33
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

Engine-v33 active; orient surfaces 5 unlinked supersedes; OI-S110-3 is the prerequisite to EF-S110-7 graph work per FR-S112-8.

## Agenda

1. Inventory NULL target_object_id / target_issue_id rows in decision_effects and NULL cited_object_id in decision_supports.
2. Resolve supersedes effects (4 of 5) and closes_issue/opens_issue effects whose descriptors begin with a literal issue alias.
3. Resolve decision_supports.cited_object_id where claim text contains a single literal alias matching the basis kind.
4. Land migration 021 as a one-shot calibrated backfill; UPDATE-only, no schema change, no engine version bump.
5. Run reviewer subagent loop on the migration and any tooling; verify orient unlinked-supersedes count drops.
