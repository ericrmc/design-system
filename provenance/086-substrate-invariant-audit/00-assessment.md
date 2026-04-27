---
session: 086
title: substrate-invariant-audit — assessment
engine_version_at_open: engine-v20
mode: self-development
generated_by: selvedge export
---

# Assessment

## State at open

S085 closed clean at engine-v20; spec_versions v2 rows registered for prompts but body_canonical_in_substrate=0 pending re-decomposition (OI-085-001).

## Agenda

1. Confirm no open_issues table or submit kind exists; quantify the markdown-only carrier.
2. Audit spec_versions / spec_sections / spec_clauses / spec_clause_links: active vs superseded counts, orphaned source_decision_v2_id, clauses without decision backing.
3. Audit refs: dangling targets, kind mismatches, stale-alias body text.
4. Audit legacy_imports for unratified or in_progress decomposition_status; cost the residual.
5. Audit decisions_v2: orphaned alternatives without rejection, substantive decisions without supports, effects pointing at non-existent target_object_id.
6. Decompose findings into review_finding rows; address each before close per T-20.
7. Record decisions for any rule clarifications or unenforced-invariant calls; close-record; export; commit.
