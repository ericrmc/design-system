---
session: 086
title: substrate-invariant-audit — review
generated_by: selvedge export
---

# Reviewer audit

## Iteration 1

- **high** against `SPEC-engine-manifest-v20`: Three active spec_versions have zero spec_sections: engine-manifest-v20, prompt-application-v2, prompt-development-v2; dispatcher clause queries return empty for these specs.
  - **adjudicated.** Tracked by OI-085-001 (re-decompose v2 spec_versions); fixes pending re-decomposition session.
- **medium**: All 272 spec_clauses have source_decision_v2_id NULL; the traceability column is documented but unused, even for post-restart specs.
  - **adjudicated.** Tracked by OI-086-001 per DV-S086-1; fix deferred under 078 D-5 release gate.
- **medium**: spec_clauses.source_decision_v2_id is nullable, contradicting the schema-sketch contract source_decision_id NOT NULL authored at S084 P-1.
  - **adjudicated.** Tracked by OI-086-001 per DV-S086-1; the NOT NULL contract is restored when source_decision_v2_id constraint lands.
- **medium**: spec_versions has UNIQUE on spec_id+version but no schema constraint preventing two simultaneously-active versions per spec_id.
  - **adjudicated.** Tracked by OI-086-002 per DV-S086-1; partial unique index on (spec_id) WHERE status=active is the candidate fix.
- **medium**: decision_supports and alternative_rejections allow NULL cited_object_id; 16 of 18 rows lack a cite, defeating traceability for prior_decision and operator_directive bases.
  - **adjudicated.** Tracked by OI-086-003 per DV-S086-1; lookup table of basis-to-cite-required is the candidate fix.
- **medium**: No open_issues table or submit kind; 20 active and 6 resolved OI files live in markdown only, contradicting the substrate-only-state direction.
  - **adjudicated.** Folded into OI-085-002 disposition path precondition 2; submit-open-issue is already named there.
- **medium**: engine_feedback table has no submit kind; OI-085-002 names submit-engine-feedback as a precondition for the markdown-restriction harness.
  - **adjudicated.** Folded into OI-085-002 disposition path precondition 2; submit-engine-feedback is already named there.
- **medium**: legacy_imports.decomposition_status is inverted: perspectives 1-5 ratified yet zero positions/claims captured; perspectives 6-8 in_progress but 126 claims plus 3 positions captured.
  - **adjudicated.** Tracked by OI-086-004 per DV-S086-1; either derive status from row presence or assert via trigger.
