---
session: 088
title: issues-table — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt issues substrate table schema per S088 deliberation 4 synthesis.

**Kind:** substantive.  **Outcome:** adopt migration `009-issues-table`.

**Why.**

- (deliberation) Three-perspective deliberation converged on substrate-only canonical, numeric PK with preserved aliases, closed priority enum, dedicated link table, dispatch via NOT-EXISTS filter.
- (prior_decision) S087 DV-S087-1 R-1.3 deferred this work to a focused session, naming status enum, blocks relations, search semantics, migration plan as load-bearing. [DV-S087-1]
- (operator_directive) Operator named the table issues and mandated MAD plus coding reviewer plus subagent backfill per the engine spec.

**Effects.**

- adds_migration 009-issues-table.sql
- creates issues + issue_links + issue_notes + issue_dispositions tables
- creates submit issue / disposition / link / note CLI kinds
- bumps_engine engine-v21 to engine-v22
- closes_issue S087 deferral closed; substrate-native dispatch now possible

**Rejected alternatives.**

- **R-1.1.** P-1 minimal: two-value status open/resolved, single 4000-char body atom, reuse refs for blocking edges, in-migration Python backfill.
  - (inferior_tradeoff) Two-status enum loses in_progress/blocked/superseded distinctions; refs reuse pollutes schema; in-migration backfill couples schema to data.
- **R-1.2.** P-2 maximal-six: six-value status enum, atomized title/summary/next_step/resolution, dedicated link and note tables, subagent backfill.
  - (inferior_tradeoff) Six-value status splits resolved/superseded/wontfix unnecessarily when disposition row carries the reason; next_step adds a dispatch column nobody populates yet.
- **R-1.3.** P-3 strict: five-value status plus reopenable BOOLEAN and reopen_conditions_md, halt-backfill on heterogeneity, terminal-to-open T-trigger refusal.
  - (redundant_with_existing) reopenable column duplicates state already implied by disposition history; can be added later if dispatch finds it necessary.
