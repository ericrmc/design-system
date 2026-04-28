---
session: 109
title: subtract-constraints-from-manifest — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Remove constraints.md from the engine-definition file set and archive it

**Kind:** substantive.  **Outcome:** adopt spec_version `constraints-v1`.

**Why.**

- (operator_directive) Operator identified constraints.md as historical rationale with no operational content for external-problem agents and directed subtraction.
- (constraint) Every substantive constraint in constraints.md is already encoded structurally in the substrate triggers and the methodology kernel; loading the rationale document at session open is redundant weight.
- (constraint) Substrate decisions are queryable and deterministic; the design rationale is permanently available via bin/selvedge query without a file in the load path.

**Effects.**

- supersedes constraints spec-version row status set to superseded
- modifies engine-manifest: remove constraints.md row from engine-definition file set table, note substrate as rationale store
- bumps_engine engine-v31 to engine-v32

**Rejected alternatives.**

- **R-1.1.** Retain constraints.md in engine-definition set, load on demand via a pointer markdown
  - (no_feedback_loop) A pointer markdown is untracked provenance — a new markdown artifact not recorded in the substrate, reintroducing the prose-state failure mode the engine was built to eliminate.
- **R-1.2.** Keep constraints.md in the engine-definition set unchanged
  - (inferior_tradeoff) Loads historical rationale into every session context without providing operational guidance; costs context budget with no return for external-problem agents.
