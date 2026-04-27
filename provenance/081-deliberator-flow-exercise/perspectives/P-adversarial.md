# Adversarial perspective — OI-079-001 disposition

## Position

I would commit to a **fourth option, D**: dispose of OI-079-001 by **rewriting the budget rule itself**, not its number. Replace D-10's "≤16 tables, breachable with cause" with "**no schema changes admitted under the release gate; substrate count is whatever migration 001 says it is until the 30-session external trial closes**." Record as `calibration`. Stop adjudicating the number. The number is the wrong object.

A is the second-best option and is what I expect the deliberation to land on by default. The rest of this perspective is the case against it.

## Adversarial work — against A (ratify 17)

A presents itself as the conservative, no-schema-change option. It is not. A is the option that quietly **legitimises the budget mechanism itself** at the moment the budget mechanism just demonstrated it doesn't work.

The workspace narrative is: "D-10 inadvertently omitted `synthesis_points`; 079 D-2 caught it; the breach clause did its job; now we ratify." Read the trail again. D-10 produced a count that didn't match the schema 078 D-1 itself enumerated (`02-decisions.md` D-2: "*observable on a careful read of D-10's parenthetical against D-1's listing of S3 tuples*"). Two specifications in the same session disagreed by one table and nobody noticed for two sessions. Then `objects` — the spine of T-01 ref resolution, referenced by **every other table's `object_id` FK** in `001-initial.sql` — was *also* omitted from the manifest's prose enumeration (`engine-manifest.md` §Substrate lists 15) and nobody noticed for *three* sessions until S080's assessment surfaced it (`00-assessment.md` §Discrepancy).

That is two omissions, in two different documents, of two different tables, across three sessions, by an engine whose entire premise (`constraints.md` property 1) is "models default to prose" and whose remedy is "structured state belongs in a database that refuses malformed input." The 16-table budget is **prose state about the database**. It is exactly the failure mode the substrate was built to eliminate, recurring one layer up. Ratifying 17 patches the count and leaves the mechanism that produced two miscounts in a row fully intact, blessed, and now load-bearing.

The unsurfaced strongest case against A: **the budget is a derived quantity masquerading as a constraint**. `SELECT COUNT(*) FROM sqlite_master WHERE type='table'` is one query. The validator already runs pre-commit. A budget the substrate can compute itself but which is instead asserted in two prose documents that drift from each other is precisely the "counter narrated, not derived" pattern `constraints.md` §"Friction at write time" warns against. Ratifying the new prose number reinstalls the bug.

C is worse than A on the same grounds — it adds a *category distinction* ("substrate-infrastructure exempt") that has to be maintained in prose by future authors, which is more surface for the same drift, not less.

## The unstated assumption

The framing assumes **the table count is a meaningful budget** — that 16 vs 17 vs 18 carries information about engine size or ceremony. It does not. `objects` is one table with three columns and an index; it is structurally trivial. `synthesis_points` is one table that carries a CHECK constraint other tables would otherwise have to fake in JSON. The post-restart engine is "deliberately small" (`constraints.md`) measured in **active-spec lines and agent-context load**, not in DDL object counts. D-10's "≤16" never derived a falsifiable claim from the number; it was a vibe expressed numerically. The deliberation is being asked to ratify, subtract, or recategorise against a yardstick that was never calibrated to anything.

## Question the deliberation must answer

**What does the table-count budget protect against that the validator, the release gate, and the migration runner (when it exists) do not already protect against?** If the answer is "nothing specific, it is a heuristic against accretion," then the heuristic should be replaced by the structural mechanism the workspace already has — the release gate forbidding new active-spec content under 078 D-5 — and OI-079-001 dissolves rather than resolves.

## What would change my mind

I retract option D and accept A if someone produces a concrete failure mode the table-count budget catches that (a) the release gate does not already forbid, (b) the migration runner's additive-vs-contract classifier (078 D-8) won't catch when built, and (c) is plausible inside a 30-session external trial. Absent that, ratifying 17 is ceremony defending ceremony — exactly the recursive trap `constraints.md` property 6 names as the reason Selvedge restarted.
