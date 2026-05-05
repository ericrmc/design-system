---
session: 204
title: stakeholder-event-f-n-row-primitive-v1 — counterfactuals
generated_by: selvedge export --session
---

# Deliberation counterfactuals

## D-10 — S204 C-4 stakeholder-event F-N primitive shape: 2-table event_ledger+event_effects v1 design knots

### Counterfactual 1

- **position.** Ship codex 6-value enum verbatim with T-43 refuse-on-target-kind-absence at v1 for forward-readiness.
- **why.** Enum cardinality stays stable v1 to v2; agents see full vocabulary; reduces v2 widening migration ceremony.
- **disposition.** addressed-in-synthesis — preserved as M-2 minority watch-trigger; v1 ships 2-value tight per AR-S203-1.

### Counterfactual 2

- **position.** Single-table denormalized event header with N effects encoded as repeated columns or JSON.
- **why.** Avoids 2-table join cost; simpler v1 surface area; cycle_ledger ships single-table with optional FKs as precedent.
- **disposition.** nilled-by-exclusion (exclusion_kind=barred-by-constraint)

### Counterfactual 3

- **position.** Auto-cascade invalidates-assumption to AR.status=invalidated at handler dispatch.
- **why.** Reduces operator friction; events emit substantive state transitions at insert; mirrors typed-handler cascading.
- **disposition.** addressed-in-synthesis — preserved as M-3 minority watch-trigger; codex blind-spot self-named in EF-S204-1.

### Counterfactual 4

- **position.** Ship origin_event_id forward-FK on supersession_ledger this session wiring SL provenance to events.
- **why.** Closes the deferred S197 forward-FK preserving SL-event linkage from day one; smaller v2 scope.
- **disposition.** nilled-by-exclusion (exclusion_kind=out-of-scope)

### Counterfactual 5

- **position.** Typed temporal column (TIMESTAMP or INT epoch) instead of free-text event_time_atom.
- **why.** Enables query-by-time and chronological ordering at SQL layer; avoids string parsing at agent layer.
- **disposition.** nilled-by-exclusion (exclusion_kind=barred-by-constraint)
