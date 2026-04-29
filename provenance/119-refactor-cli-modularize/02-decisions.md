---
session: 119
title: refactor-cli-modularize — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Refactor selvedge/cli.py to a per-concern submodule layout with extracted submit-handler helpers; preserve behavior exactly.

**Kind:** procedural.  **Outcome:** adopt process_rule `cli-py-modular-layout`.

**Why.**

- (operator_directive) Operator directed splitting cli.py so only CLI concerns remain plus helper functions to reduce repetition, prior to FR-S118-10.
- (engine_feedback) Smaller modules reduce blast radius of the upcoming dry-run/sandbox-harness change. [EF-S118-1]

**Effects.**

- modifies selvedge/cli.py reduced to argparse + main
- creates selvedge/ submodules: paths, errors, connection, aliases, migrations, init, id_allocate
- creates selvedge/ submodules: validate, subtract, recover, query, orient, schema, monitor_external
- creates selvedge/submit/ package with per-handler-family modules and shared _helpers
- creates selvedge/export/ package: session, issues, anchor

**Rejected alternatives.**

- **R-1.1.** Pure mechanical splitting with no helper extraction; preserve every function body verbatim.
  - (operator_override) Operator asked for helper functions to reduce repetition, not a verbatim move-only refactor.
- **R-1.2.** Leave cli.py monolithic; extract helpers only.
  - (operator_override) Operator directed only-CLI-concerns in cli.py, motivated by smaller blast radius for the next session.
