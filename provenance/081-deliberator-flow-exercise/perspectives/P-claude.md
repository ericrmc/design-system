**Position: C, with one tightening.** Enumerate `objects` as substrate-infrastructure exempt from the 16-table budget *and* explicitly name the criterion that separates infrastructure from domain tables, so the exemption can be re-applied or refused on principle later. Record as a `calibration` decision (not `substantive`) because the schema does not change.

## Why C over A

A and C reach the same schema and the same prose-edit set. The difference is the *reason* attached to the budget arithmetic. Under A, the budget becomes 17 because the workspace decided to admit the breach. Under C, the budget remains "16 domain tables" with `objects` carved out as a different category, and the only breach is the legitimate addition of `synthesis_points` (1 over the 16-domain budget, recorded as cause).

That distinction matters for one reason: the next time someone proposes adding a table, the budget question has a sharper edge. Under A, "we ratified to 17 last time, why not 18 now?" is a coherent argument and the only thing stopping it is the invocation of the "with cause" clause again, which is rhetorical force, not structure. Under C, "we ratified `synthesis_points` because it carries T-14 as a CHECK constraint that has nowhere else to live; what does *your* table do?" is a sharper question to put to a future addition.

The criterion the calibration should name explicitly: a table is **infrastructure** if it has no domain semantics of its own and exists only to make cross-cutting operations on domain rows possible. `objects` qualifies — every row is just `(object_kind, typed_row_id, citable_alias)`; the table's job is the indirection. `schema_migrations` is a sibling case (records the substrate's state about itself, not workspace work). Both should sit on the infrastructure side of the ledger if we draw it.

## What I take seriously against C

The release-gate worry. Drawing a new category — "infrastructure tables" vs "domain tables" — is on the boundary of methodology-expansion. The 078 D-5 gate forbids new active-spec content in `methodology.md` and peers; the question is whether enumeration-shape change in `engine-manifest.md` counts. My read: the manifest already classifies content (engine-definition vs not, active spec vs substrate); adding one more sub-distinction inside the substrate enumeration is enumeration-shape, not new methodology content. But it is *close*, and a perspective that argued otherwise would be reasonable. If C trips the gate, A is the fallback.

The ceremony worry. `specifications/constraints.md` §6 names the failure mode: "each addition the engine made in response to perceived deficiencies consumed the bandwidth the engine needed to see deficiencies in the first place." Drawing a new category to clarify a 17-vs-16 prose discrepancy is exactly the shape of "addition that is locally reasonable." Honest answer: yes, it is. The mitigation is that the addition is a single sentence in one file and changes nothing about how anything is *used* — `objects` already exists, `synthesis_points` already exists. We are paying one sentence to get a sharper budget question for the next session that proposes a table. That seems like a net cost reduction, not an accretion.

## Why not B

Two reasons, in order:

1. **Structurally blocked.** OI-080-001 documents that the `selvedge migrate` runner doesn't exist; option B requires migration 002, which requires the runner. Choosing B in S081 means committing the session to building the runner and then doing the schema change — at which point S081 is a different session (option 3 from S080's close, plus a substantive schema decision). The operator selected option 1 for S081 explicitly.

2. **Even unblocked, B is the wrong subtraction.** T-14 is a CHECK constraint on a single column (`source_perspectives` JSON-length ≥ 2 when kind = 'convergence'). Absorbing it into `deliberations.synthesis_md` as JSON moves it from a structural refusal (substrate refuses malformed input) to an application-layer parse problem. That is the move `constraints.md` §1 calls out as the LLM-default failure mode (prose pretending to be state). The substrate is doing exactly the right thing by carrying convergence as a typed row with a CHECK; subtracting that table to honour a budget number would be optimising for the wrong invariant.

## The unstated assumption I want surfaced

The framing treats the 17-vs-16 discrepancy as a budget-arithmetic question. The deeper question is: **what was the 16-table budget for?** If the budget existed to pressure-test additions against necessity, then the right disposition is whatever sharpens that pressure for the next addition (C). If the budget existed to bound substrate-design complexity for a finite-context orchestrator, then the right disposition is whatever keeps the *manifest enumeration* short and readable (A — fewer categories, just list 17). I think the first is the budget's actual purpose given Selvedge's history; a perspective that thought the second would land on A.

## What I don't know

Whether 078's D-10 author intended `objects` to count as one of the 16 or implicitly excluded it as plumbing. The 078 decision text would tell me; I haven't read it in this session. If D-10 enumerated 16 specific tables and `objects` was on the list, A is cleaner. If D-10 said "16 domain tables" and `objects` was an oversight in the count, C is what was always meant.
