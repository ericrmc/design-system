---
session: 112
title: orient-superseded-spec-discoverability — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Enrich orient with a Recent supersessions section to surface spec_version rationale.

**Kind:** substantive.  **Outcome:** adopt process_rule `orient-recent-supersessions`.

**Why.**

- (engine_feedback) EF-S110-10 reflection named cross-typed-row link gaps; orient already enriches FRs and is the natural surface for supersession rationale. [EF-S110-10]
- (prior_decision) DV-S101-1 set precedent for orient-time derivations (FR-rot annotation) over new tables. [DV-S101-1]
- (operator_directive) FR-S111-7 sequences OI-S110-1 immediately after the S111 stale body_path migration.

**Effects.**

- modifies selvedge/cli.py _orient_sections adds recent_supersessions and unlinked_supersedes_count keys
- modifies selvedge/cli.py _orient_markdown renders Recent supersessions table with OI-S110-3 hint
- closes_issue OI-S110-1 — orient now surfaces decision-linked supersessions plus unlinked count pointer to OI-S110-3

**Rejected alternatives.**

- **R-1.1.** Add a dedicated bin/selvedge spec-history subcommand instead of enriching orient.
  - (inferior_tradeoff) Discoverability is the named gap; a separate subcommand requires the operator already know to look, which is exactly what orient solves.
- **R-1.2.** Surface every superseded spec_version row regardless of decision_effects linkage by descriptor parsing.
  - (inferior_tradeoff) Descriptor parsing is brittle and would mask the linkage gap that OI-S110-3 already tracks for backfill.
