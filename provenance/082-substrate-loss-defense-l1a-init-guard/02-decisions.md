---
session: 082
title: substrate-loss-defense-l1a-init-guard — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S082 ships L1a init-guard substrate refusal plus prompt-development v1 §4 boilerplate amendment, slicing the smallest L1a defense from DV-S081-1.

**Kind:** substantive.  **Outcome:** adopt process_rule `l1a-init-guard`.

**Why.**

- (prior_decision) DV-S081-1 adopted layered defense L1a+L2b+L3+L4+L5+engine-v51-marker; FR-S081-10 routes S082 to L1a + boilerplate as the smallest slice. [DV-S081-1]
- (engine_feedback) S082 codex-shape-consult endorsed kind=coding, predicate-(a) any-sessions-row over fixture-allowlist, and named development.md as canonical (FR-S081-10 prose was loose). [EF-S082-1]

**Effects.**

- creates L1a init --force live-substrate refusal in selvedge/init_cmd.py with --really-force escape
- creates selvedge/cli.py argparse adds --really-force flag for init subparser
- creates state/tests/test_init_guard.py 5 tests covering guard predicate and override
- modifies prompts/development.md §4 boilerplate adds do-not-mutate-substrate part as L1a twin
- closes_issue OI-S081-1 — OI-S081-1 closed by-mechanism via L1a guard shipping per FR-S081-10
- closes_issue OI-S081-8 — OI-S081-8 closed by-mechanism via §4 boilerplate amendment per OI-S180-1 step 5

**Rejected alternatives.**

- **R-1.1.** Ship the entire DV-S081-1 package (L1a+L2b+L3+L4+L5+engine-v51 marker) in S082 as a single arc.
  - (too_large_for_session) FR-S081-10..14 sequenced the package across S082..S086 deliberately to keep each session's review surface tractable.
- **R-1.2.** Detect live substrate via workspace_metadata.current_engine_version presence rather than sessions row count.
  - (inferior_tradeoff) Predicate (b) overfires: workspace_metadata is seeded by migration 001 on an otherwise empty post-init substrate, refusing legitimate post-init reinit.
- **R-1.3.** Detect live substrate via fixture-allowlist of session numbers permitting init --force on fixture-only state.
  - (inferior_tradeoff) Introduces a subtle escape hatch absent first-class fixture schema; predicate-(a) is simpler and harder to bypass.
- **R-1.4.** Implement the guard as a SQLite trigger on the sessions table rather than in init_cmd.py.
  - (violates_gate) init unlinks the file before opening any connection; a trigger inside the substrate cannot fire on an unlink that precedes the connection.
