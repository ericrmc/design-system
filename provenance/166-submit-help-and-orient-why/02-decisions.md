---
session: 166
title: submit-help-and-orient-why — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Ship submit-help schema registry plus orient §Why this engine exists section per FR-S161-15

**Kind:** substantive.  **Outcome:** adopt process_rule `submit-help-and-orient-why`.

**Why.**

- (engine_feedback) EF-S161-1 named the kernel-narrative gap retirement of constraints.md v1 created at DV-S109-1 and proposed orient extension as remedy. [EF-S161-1]
- (engine_feedback) EF-S162-1 vindicated external-pilot-plus-harvest pathway providing concrete recent grounding for the recursive-self-application thesis. [EF-S162-1]
- (operator_directive) Operator PROMPT.md instruction to prioritise FR-S161-15 in this session.

**Effects.**

- creates selvedge/submit/_schemas.py declarative payload registry covering all 37 submit kinds
- creates selvedge/submit_help.py and bin/selvedge submit-help CLI subcommand
- modifies selvedge/orient.py adds §Why this engine exists section to packet and markdown output

**Rejected alternatives.**

- **R-1.1.** Per-handler docstring tags scraped at runtime instead of a separate registry file.
  - (inferior_tradeoff) Docstring scraping couples documentation shape to function source format and complicates evolving the schema entry shape.
- **R-1.2.** Adopt full JSONSchema format and validate payloads at submit time against the registry.
  - (too_large_for_session) Validation duplicates handler logic already running and would push this session past coding-loop scope; FR-S161-15 names registry only.
- **R-1.3.** Source §Why content from a substrate constants table read at orient time rather than a module constant.
  - (redundant_with_existing) No constants table exists; adding one for one row is ceremony without payoff and introduces migration cost for content edited rarely and reviewed deliberately.
