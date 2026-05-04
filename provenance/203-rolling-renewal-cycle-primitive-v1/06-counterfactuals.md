---
session: 203
title: rolling-renewal-cycle-primitive-v1 — counterfactuals
generated_by: selvedge export --session
---

# Deliberation counterfactuals

## D-9 — cycle_ledger v1 shape: locus + suppression + polymorphic-allowlist + classifier + closure-path-reuse

### Counterfactual 1

- **position.** Hard-cutover migration deprecating assumption_ledger.sub_type=rolling-renewal channel: refuse new sub_type writes; force all rolling-renewal status into cycle_ledger v1 from day one.
- **why.** Avoids dual-channel watch-trigger risk that S197 named (M-1 minority preserved at DV-S197-1); compositional purity over backwards-compat.
- **disposition.** addressed-in-synthesis — Synthesis preserves cycle_ledger as new-write surface with sub_type=rolling-renewal soft-deprecated; M-1 watch-trigger if dual-channel persists.

### Counterfactual 2

- **position.** Substrate-detected substantial classifier via mechanical state-diff between consecutive cycle snapshots; agent-cite only required when overriding engine signal.
- **why.** Eliminates classifier subjectivity at insert-time; substrate becomes single-source-of-truth for cycle state-machine reasoning.
- **disposition.** nilled-by-exclusion (exclusion_kind=out-of-scope)

### Counterfactual 3

- **position.** Cycle-specific closure_path enum disjoint from closure_shape: cycle-rollover, cycle-replacement, attestation-passed, drift-retire, plan-rescoping as cycle-only closure semantics.
- **why.** Domain-specific closure paths that disaster-recovery DV-S011-5 surfaced (path-a convergence, path-b plan-rescoping) read more naturally as cycle-bound than assumption-bound.
- **disposition.** nilled-by-exclusion (exclusion_kind=barred-by-constraint)
