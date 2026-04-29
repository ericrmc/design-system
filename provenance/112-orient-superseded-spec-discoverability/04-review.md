---
session: 112
title: orient-superseded-spec-discoverability — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **critical**: Recent supersessions query selects s.workspace_session_no without COALESCE on s.session_no; FR query line uses COALESCE for defensive parity.
  - **fixed.** Iter-2: query now uses COALESCE(s.workspace_session_no, s.session_no) AS wno mirroring the FR-rot pattern.
- **high**: Hardcoded OI-S110-3 reference in unlinked-count hint will rot when that issue resolves; FR-rot annotation pattern in DV-S101-1 already solves this dynamically.
  - **fixed.** Iter-2: pointer is computed from issue status; falls back to generic message when OI-S110-3 leaves live status.
- **high**: A single decision superseding multiple specs produces multiple rows with identical alias and title; potentially confusing without grouping.
  - **adjudicated.** Per-effect rows mirror decision_effects ground truth; collapsing would hide which specs each decision touched.
- **medium**: spec_id field is unescaped in markdown table; pipe chars would break alignment if ever introduced.
  - **fixed.** Iter-2: spec_id is now escaped in markdown render alongside title.
- **medium**: INNER JOIN may silently exclude valid supersessions if object/spec_version linkage is partial.
  - **adjudicated.** spec_versions.object_id and objects.typed_row_id linkage is set in _submit_spec_version; substrate guarantees no orphans.
- **low**: LIMIT 10 cap is arbitrary and may hide older but still-relevant supersessions.
  - **adjudicated.** LIMIT 10 matches deferred_decisions and FR cap; raw SQL remains available via bin/selvedge query for completeness.
## Iteration 2

- **low**: Iter-2 clean: COALESCE wno, dynamic OI-S110-3 pointer, spec_id escaping all confirmed; no new findings.
  - **adjudicated.** Iter-2 reviewer pass clean; recorded as a low-severity sentinel for the loop closure trace.

## Terminal passes

- **iteration 1** — findings @ `d7aa00242a5b`
  - Iter-1 surfaced 1 critical, 2 high, 2 medium, 1 low finding on the orient enrichment; medium-or-higher disposed in-iter.
- **iteration 2** — clean @ `d7aa00242a5b`
  - Iter-2 reviewer pass clean; all iter-1 fixes verified, no regressions.
