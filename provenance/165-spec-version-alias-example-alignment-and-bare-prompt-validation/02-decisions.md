---
session: 165
title: spec-version-alias-example-alignment-and-bare-prompt-validation — decisions
generated_by: selvedge export
---

# Decisions

## D-1. Bump prompt-development v16 to v17: align §6 spec-version supersedes example to SPEC-<spec>-v<n> form per EF-S164-1.

**Kind:** calibration.  **Outcome:** adopt spec_version `prompt-development@17`.

**Why.**

- (engine_feedback) EF-S164-1 named the <spec>@<n> vs SPEC-<spec>-v<n> shape mismatch as ergonomic friction costing one round-trip in S164. [EF-S164-1]
- (prior_decision) DV-S164-1 deferred this alignment to a future spec_only or coding session via FR-S164-9. [DV-S164-1]

**Effects.**

- supersedes SPEC-prompt-development-v17 — prompt-development v16 to v17

**Rejected alternatives.**

- **R-1.1.** Widen _resolve_alias_to_object_id to admit the <spec>@<n> shorthand instead of editing the example.
  - (too_large_for_session) Resolver widening is a coding session with handler+migration scope; example alignment is a single-clause spec edit with the same operator-facing effect.
- **R-1.2.** Defer the alignment to bundle with FR-S164-7 substantive work cluster.
  - (inferior_tradeoff) Bundling delays the friction fix; this session is bare-prompt auto-proceed and the single-clause edit is the natural tactical scope.
