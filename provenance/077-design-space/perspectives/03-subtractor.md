---
session: 077
perspective: subtractor
family: Anthropic
date: 2026-04-27
---

# subtractor — blind position

## Frame

The deliberation reads, on the surface, as "what does the next engine add — a database, more agents, a subtraction role, a human-review role?" My frame: the brief's own diagnosis (`constraints.md` §1.6) is that Selvedge died of additions that were each locally reasonable. The most dangerous artefact 077 could produce is a competent-looking design space full of locally-reasonable additions. The deliberation's real subject is the discipline of refusal. Every prescription gets one question: *what does this prevent that engine-v16 cannot prevent today?* If the answer is not concrete and load-bearing, the prescription is ceremony in a new costume.

## Position

### 1. Subtract from engine-v16 itself

The trim cut to ~350 lines. That is not yet minimal.

- **`methodology.md` §"When to review at close"** (lines 66–80) introduces a separate reviewer with three reporting axes. The brief itself (`constraints.md` §1.5) records that the prior reviewer caught the same classes of error session after session — *detection without prevention is a cleanup service*. Keeping a reviewer in the kernel before we have re-derived what prevention looks like preserves the failed mechanism's shape. **Cut; re-introduce only if 077/078 produce a reviewer whose findings are structural inputs, not advisory prose.** Failure mode exposed: errors slip through 077 itself. Acceptable: 077 produces candidates, not commitments.

- **`methodology.md` §"Validation senses"** (lines 84–88) — the "provisional reference substitute" sense addresses a case (no domain-actor, sealed reference) that does not arise during 077–078 self-development. **Cut from active; archive.**

- **`methodology.md` §"What this kernel does not say"** (lines 109–118) and **`workspace.md` §"What this file does not say"** (127–135) are meta-disclaimers. Useful to a human reader once; costly to load every session. **Move to the 077 close note.**

- **`workspace.md` "Top-level layout"** (26–58) enumerates a tree the same file says will change in 077–078. **Replace with: "the manifest is canonical; layout is whatever `engine-manifest.md` and live session records produce."**

- **`engine-manifest.md` §"Loading the engine in a fresh workspace"** (48–58) is a recipe the file says will not survive its first use. **Cut.**

Net subtraction target: ~80–100 lines, leaving ~250 lines of active spec. What survives is load-bearing for 077: the nine activities, the deliberation pattern, preservation rules, engine-feedback, file-class taxonomy.

### 2. Subtract from the brief's eight prescriptions

`constraints.md` §"What this means for the engine's design" lists eight (lines 79–95). Each gets the prevention test.

1. **Multiple agents, tightly scoped context.** Load-bearing. Prevents §1.4 (foundational instructions decay under load). Keep — but see §3 below for which agents.

2. **Database-backed substrate.** Load-bearing. Prevents §1.1 (prose-default state) and §1.2 (failure-as-cheap) by structural refusal. Keep.

3. **Markdown for design intent only.** Load-bearing as a *boundary*: the substrate's discipline is what the boundary enforces. Without (2), this is exhortation. With (2), it is automatic. Keep, but treat as a derivative of (2), not an independent prescription.

4. **Coordination through the substrate, not agent-to-agent messaging.** Load-bearing. Prevents the orchestrator-as-bottleneck failure (§"Risks the successor must hold"). Keep.

5. **Friction at write time, not audit time.** Load-bearing. This is the prescription that makes (2) and (4) actually work — and the prescription whose absence in engine-v16 makes the reviewer (cut above) toxic. Keep; promote to first-class.

6. **A subtraction role with authority to remove.** I will keep this — but only if §4 below makes it real. Otherwise it is decoration and I would rather cut the prescription than ratify a ceremony of subtraction that subtracts nothing.

7. **External pressure as a methodology requirement.** Load-bearing in the meta sense (the methodology won't survive without it) but **not a design feature of the engine**. The engine cannot *enforce* that it be applied externally. **Cut from the engine's active design surface; record as a methodology-validity precondition in the close of 078, not as something the engine builds.** Failure mode exposed: a workspace can self-apply forever and rot. Acceptable: that is already the case and no engine prescription prevents it; pretending otherwise is performative.

8. **A deliberately-built human review role.** Most suspicious. The brief is right that operator-as-diagnostic was structural in the prior engine. But "build it in deliberately" means two different things: (a) name the operator's authority to subtract and reframe in one paragraph of `methodology.md` — cheap, honest; or (b) a scheduled human-review cadence with audit shape, scope, triage queue — exactly the shape that grew into ceremony in the prior reviewer. **Keep (a). Reject (b) until something concrete fails that (a) cannot fix.**

### 3. Subtract from the candidate roster

The brief gestures at seven roles: reader, specifier, decider, deliberator, reviewer, validator, assembler.

- **Reader** — load on demand. **Not an agent; a substrate API.** Calling a SQL query an agent is the prose-default failure reincarnated as architectural ceremony.
- **Specifier** — holds spec and change. **Keep.**
- **Decider** — records decisions with rejected alternatives. **Keep**; the decision record is the methodology's load-bearing artefact.
- **Deliberator group** — multiple perspectives. **Keep**; irreducible.
- **Reviewer** — **defer.** Re-derive only after the substrate refuses what the prior reviewer caught.
- **Validator** — pre-commit integrity gate. **Not an agent; a gate.** Confusing gates with agents produces eight roles where two would do.
- **Assembler** — generates artefacts from the substrate. **Keep**; the only thing that prevents prose-state leaking back in.

Smallest agent set: **specifier, decider, deliberator-N, assembler.** Four roles plus a substrate exposing reader/validator as APIs. Not seven. The seven-roster reads as seven because the prior engine had things called those names; precedent-reflex.

### 4. Make the subtraction role real

A subtraction role that cannot subtract is decoration. Mechanics:

- **When it runs.** Every Nth session (proposed: 5th) and any session whose substrate-derived line-count of active spec exceeds 1.5x the count at the last subtraction.
- **What it removes.** Spec sections, prescriptions, agent roles, decisions whose rejected-alternatives no longer apply, and its own prior subtractions if those added scaffolding instead of removing it.
- **The rule (load-bearing).** A *retention test*, not an inclusion test: a clause is retained only if the subtractor can name a concrete failure that occurred under its absence within the last 10 sessions. "It might be useful" is insufficient. "Session 47 produced a malformed reference because we lacked it" is sufficient.
- **Anti-capture.** The subtractor reads the active spec blind, states which clauses fail retention, *then* reads design rationale. Mirrors the deliberation pattern's anchoring discipline. Removals require operator co-signature; operator may refuse but cannot unilaterally add. Adding requires a normal session.
- **Cross-family.** When subtracting from the kernel, the subtractor must come from a different model family than the session's primary author. §1.3 applies more sharply to subtraction than to addition.

## Where you would not commit

1. **The threshold for triggering subtraction is a guess.** No empirical basis for "1.5x" or "every 5th." Evidence that would change my mind: Selvedge's line-count curve across 1–75 plotted against operator interventions. If diagnostic capacity broke at a specific multiplier, use that; if decline was continuous, make the trigger event-driven (reviewer warnings, operator interventions), not periodic.

2. **Whether the reviewer can be permanently cut or only deferred.** I argue deferral. If 078's substrate refuses the prior reviewer's catches, reviewer is gone — replaced by validator-as-gate. But trajectory-discipline and mechanism-adequacy may be *judgment* problems no substrate refuses. I cannot tell from the brief alone.

3. **Whether four roles suffice.** I subtract on the principle that role-confusion grows superlinearly. Four may be too few if cross-perspective integration needs an integrator distinct from the assembler. Evidence: if 077's synthesis step requires a role none of {specifier, decider, deliberator, assembler} can play, that is the missing role.

4. **The cut to "external pressure as a design surface."** A weaker form is enforceable: the engine could refuse a self-development session if N consecutive priors were self-development. I am uncertain whether that lever should exist.

## What you think the other perspectives will miss

Most likely: every other perspective will treat the brief's eight prescriptions as the floor and propose additions on top. The architect designs a thoughtful schema; the adversary challenges specifics while accepting the prescriptions; the human-review designer elaborates (b) above into a scheduled cadence. Synthesis then collapses to "all of the above, with care" — the same accretion logic the engine just died of, executed one level up. The blindspot: *the brief's eight prescriptions are themselves a candidate output, not a frame*. Treating them as a frame turns 077 into the first session of engine-v17's accretion, not the design space the close asked for.

Second-most-likely miss: the subtraction role and the human-review role solve the same problem (external pressure the system cannot generate from inside). Defining them as two roles double-counts. The operator with authority to subtract *is* the human reviewer; pretending otherwise produces two ceremonies where one structural acknowledgement would do.
