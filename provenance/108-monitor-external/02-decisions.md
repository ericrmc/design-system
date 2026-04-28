---
session: 108
title: monitor-external — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Adopt bin/selvedge monitor-external subcommand group with status, next-input, and harvest-ef per DV-S106-3 contract.

**Kind:** substantive.  **Outcome:** adopt process_rule `monitor-external-cli-surface`.

**Why.**

- (prior_decision) DV-S106-3 prescribed a thin three-subcommand monitor-external CLI as the orchestration mechanism for external-application arcs. [DV-S106-3]
- (engine_feedback) EF-S107-1 named the engine-v31 substrate-enforced coding review loop as the discipline this implementation should exercise. [EF-S107-1]
- (review_finding) Iter-4 reviewer pass returned clean after addressing all eight medium-or-higher findings across iterations 1 to 3.

**Effects.**

- creates selvedge.cli.cmd_monitor_external + helpers (status, next-input, harvest-ef)
- creates state/tests/test_monitor_external.py with 21 tests
- closes_issue OI-S106-2 — OI-S106-2 monitor-external implementation

**Rejected alternatives.**

- **R-1.1.** Pure operator transport: no CLI tooling; operator does all status reads, input drafting, and EF transport manually.
  - (operator_override) DV-S106-3 already adopted the three-subcommand surface as primary; pure-operator path was preserved as activation-warranted minority M-1 not as primary.
- **R-1.2.** Permit harvest-ef to write under cwd-inferred workspace_root (engine-v23 default) when SELVEDGE_WORKSPACE is unset.
  - (breaks_invariant) Iter-3 review F-92 showed cwd inference routes writes to whichever workspace contains MODE.md upward; refusing on unset env is the only unambiguous discipline.
