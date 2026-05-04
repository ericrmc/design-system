---
session: 197
title: typed-supersession-ledger-primitive — counterfactuals
generated_by: selvedge export --session
---

# Deliberation counterfactuals

## D-5 — OI-S196-2 typed-supersession-ledger v1 schema and submit-kind shape

### Counterfactual 1

- **position.** Hard-cutover BOTH decision_effects.supersedes AND refs.supersedes at v1: drop both CHECK values, migrate both legacy rows, leave supersession_ledger as the only writable channel.
- **why.** Would eliminate two-channel risk symmetrically rather than asymmetrically; forces clean v1 cutover instead of a soft-deprecation carry; future reader could argue synthesis chose ceremony over discipline.
- **disposition.** addressed-in-synthesis — P-2 replay-parity warning + refs.supersedes hot in spec-version handler; cutting both at v1 forces spec-version refactor outside OI-S196-2 scope; synthesis chose targeted asymmetric cutover.

### Counterfactual 2

- **position.** Add a relation_metadata JSON column or notes TEXT escape hatch to supersession_ledger at v1 for cases the closed enum cannot capture.
- **why.** Would relax the closed-enum constraint and allow ledger residency for unmatched relation kinds without future migration; risks turning ledger into a generic relations dump.
- **disposition.** nilled-by-exclusion — M-3 S194 schema-correctness threshold + P-3 explicit rejection bar TEXT escape hatches; migration discipline (47 through S195) handles enum extension when calibration-EF names a real case.
