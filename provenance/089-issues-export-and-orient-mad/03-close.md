---
session: 089
title: issues-export-and-orient-mad — close
engine_version_at_close: engine-v23
mode: self-development
generated_by: selvedge export
---

# Close

## Summary

S089 ships engine-v23: substrate-native dispatch tooling (selvedge orient + schema + export --issues), issue↔work_item M:N linkage with T-24 orphan-on-resolve refusal, three-perspective MAD synthesis preserving dissent.

## Engine version

- engine-v22 to engine-v23 via migration 010 + three new CLI subcommands.
## What was done

- Extended bin/selvedge export with --issues flag; materialises open-issues/<alias>.md from substrate (per-issue files plus regenerated index).
- Convened three-perspective MAD on issue↔work_item linkage and orient/schema CLI design; captured 74 claims across P-1 anthropic-pragmatic, P-2 codex-cross-family, P-3 anthropic-adversarial.
- Sealed deliberation 5 with synthesis preserving dissent; recorded 5 convergence + 5 divergence + 2 minority synthesis-points.
- DV-S089-1 adopts: issue_work_items M:N join (admits one work_item closing multiple issues), markdown-default orient with --json flag, derived state via LEFT JOIN, minimal kind-enum widening, T-24 only.
- Migration 010 ships issue_work_items table + work_items.kind widening + T-24 trigger; coding review iteration 1 cleared at medium+; iteration 2 caught and fixed missing T-11 drop-and-recreate.
- selvedge orient + selvedge schema CLI handlers added; reviewer caught HIGH unbounded open_issues in orient packet which was capped at 30 with elision footer.
- PROMPT.md and prompts/development.md updated to point at bin/selvedge orient as the first session step; engine-manifest.md bumped to v23 and decomposed (6 sections, 105 clauses).
- Three new follow-up issues surfaced via substrate: OI-S089-1 implement submit issue-work-item CLI handler; OI-S089-2 T-25 lease-renewal trigger; OI-S089-3 reconsider decomposition_status column.
## State at close

- current_engine_version=engine-v23; 34 issues in substrate (26 open, 8 resolved); migration 010 applied; no open review findings; orient/schema/export verified end to end.
## Open issues

- Top dispatch (per orient): OI-016 and OI-085-002 (HIGH); OI-S089-1 sits at MEDIUM and is the natural next-up since it completes the issue-work-item CLI surface.
## What the next session should address

- Either implement OI-S089-1 (submit issue-work-item handler completes the M:N CLI surface) or work the dispatch queue: OI-016 / OI-085-002 are HIGH.
## Validator at close

- Pending bash tools/validate.sh post-export; expected pass.
