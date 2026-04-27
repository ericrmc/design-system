---
session: 089
title: issues-export-and-orient-mad — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt issue↔work_item linkage + selvedge orient/schema CLI design per S089 deliberation 5 synthesis.

**Kind:** substantive.  **Outcome:** adopt process_rule `issue-workitem-orient-design`.

**Why.**

- (deliberation) Three-perspective MAD (P-1 anthropic-pragmatic, P-2 codex-cross-family, P-3 anthropic-adversarial) converged on no-auto-flip status, kind widening, live schema CLI; diverged on linkage shape (M:1 vs M:N).
- (operator_directive) Operator stated: issues document, work_items help fix; one issue may have 2-3 work_items; new orient CLI should give all context, schema CLI should help with queries.
- (prior_decision) S088 DV-S088-1 established the issues table with citable_alias on issues directly (not via objects); same pattern applies to issue_work_items. [DV-S088-1]

**Effects.**

- creates issue_work_items M:N join table
- modifies work_items.kind enum adds issue_resolution
- creates selvedge orient + selvedge schema CLI subcommands
- creates T-24 trigger refusing issue resolve while linked work_items in flight
- opens_issue new issues track deferred T-25 lease-renewal trigger and decomposition_status column

**Rejected alternatives.**

- **R-1.1.** P-1 single column work_items.issue_id (M:1) — operator said 2-3 work_items per issue so cardinality is many-to-one.
  - (inferior_tradeoff) M:1 fails the realistic case where one work_item closes multiple issues (e.g. one migration fixing OI-086-001..004); join table admits that pattern.
- **R-1.2.** P-2 JSON-default orient output — agents parse keys better than markdown headers.
  - (inferior_tradeoff) Primary consumer is LLM context window; markdown is the native shape. JSON via --json flag covers tooling case without sacrificing default.
- **R-1.3.** P-3 explicit decomposition_status column on issues + T-25 lease-renewal trigger — make state structural.
  - (redundant_with_existing) State derivable from join table presence via LEFT JOIN; column is denormalised cache. T-25 deferred until lease-renewal pattern actually emerges.
