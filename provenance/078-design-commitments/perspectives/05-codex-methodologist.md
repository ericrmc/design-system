---
session: 078
perspective: codex-methodologist
family: OpenAI
date: 2026-04-27
---

# codex-methodologist — blind position

## Frame
I read 078 as a commitment session under a hazard the brief names plainly: Selvedge's prior repairs were each locally reasonable, and the accumulation of reasonable repairs consumed the diagnostic slack needed to notice failure (`constraints.md` Property 6). The database and multi-agent direction is a justified next bet, not yet the successor methodology. It directly answers documented failures around prose-state, cheap failure, context pressure, and non-retained lessons (`constraints.md` Properties 1, 2, 4, 5), but it does not answer the external-pressure problem by itself (`methodology.md` §Self-hosting). My lens is therefore release discipline: cut the active surface before adding, build one refusal-bearing vertical slice in 079, and prevent the design commitments from becoming a new layer of plausible ceremony.

## Position

### Adopt D-4.c, with a pre-implementation cut

I adopt the subtractor's D-4.c position: engine-v16 should be cut before substrate additions are made [077-sub] [077-D-4]. The key argument is not line count aesthetics. It is that adding-before-subtracting is the exact recursive trap described in `constraints.md` Property 6. Treating engine-v16 as an untouchable floor because it was already trimmed would make session 076's trim a one-time event rather than a continuing discipline.

The cut should be committed by 078 as a required first implementation step for 079. I would not have blind perspectives edit active files, but the design commitment should be explicit enough that 079 can patch before adding schema or tools.

Cut now, before any substrate code:

- Remove `methodology.md` §"When to review at close" as an active mechanism. Replace it with a short transitional sentence: close-time review is superseded until the substrate distinguishes prevention from audit. The old reviewer repeatedly caught the same classes of errors (`constraints.md` Property 5); keeping its audit shape in the kernel before the refusal contract exists preserves a known cleanup service. Re-introduce review only when it reads substrate exceptions and generated diffs, not the whole session record [077-sub] [077-dev].
- Collapse `methodology.md` §"Validation senses" to workspace validation and domain validation. Archive "provisional reference substitute" until an external-problem session needs it. It is a valid historical mechanism, but it is not needed for 079's substrate slice and it competes with the simpler external-pressure rule below.
- Remove the "What this kernel does not say" and `workspace.md` "What this file does not say" meta-disclaimers. They were useful transition notes for 077, but active prompts should not keep loading explanations of why they are incomplete.
- Replace the detailed `workspace.md` top-level layout tree with a narrower rule: the manifest defines engine files; session records live under `provenance/`; generated exports are not source of truth once the substrate exists. The current tree says it will change, so it should not remain as a loaded normative map [077-sub].
- Remove `engine-manifest.md` §"Loading the engine in a fresh workspace". It is an engine-v16 bootstrap recipe that the substrate will immediately invalidate.

Do not cut the session activities, the multi-perspective deliberation rule, cross-family requirement, preservation principles, engine-feedback pathway, or the self-hosting limitation. Those are among the pieces the brief says actually survived contact with the 75-session run (`constraints.md` §What the methodology preserved). Preservation is costly, as [077-gen] warned, but these mechanisms still have named jobs: replay, dissent, human intervention, and foundation-checking.

Subsequent cuts should be scheduled, not guessed. After 079's round-trip substrate test, 080 should remove any remaining active wording that describes Markdown as the source of structured session state. After the first external-problem trial, the methodology should reconsider whether self-hosting, dissent preservation, and engine-feedback are earning their loaded surface or being preserved as identity markers.

### Multi-agent plus database is a candidate successor, not a proven successor

I accept the brief's diagnosis as strong enough to build against, but not unique enough to declare victory. The adversary's Reading B, accretion-without-subtraction, is not a competing diagnosis so much as an omitted causal layer: the single-agent context problem and the no-subtraction problem reinforced each other [077-adv]. The multi-agent plus database direction addresses the first half; the pre-addition cut and future subtraction cadence address the second.

Reading C, self-hosting-as-disease, is more serious [077-adv]. `methodology.md` already concedes self-development is bootstrap, not destination. My disposition is: do not stop 079 for an external application first, because the current engine lacks the refusal substrate needed to test the new thesis. But do not let more than the minimal substrate vertical slice and one agent-facing run happen before external pressure. Build the candidate engine, then expose it.

So 078 should commit to this wording: engine-v17 is provisional until it has run a bounded external-problem trial. The engine should record workspace mode and session mode, but it should not pretend it can verify "externality" structurally. I reject a hard substrate refusal such as "no self-development after N sessions" as likely compliance theatre [077-sub]. The enforceable rule is a release gate: no further methodology-expanding self-development after the first agent-on-substrate run unless an external-problem trial has been opened, run, and closed with a domain or operator report. That extends [077-gen]'s external trial proposal while accepting [077-sub]'s point that the engine cannot make external pressure true by schema.

### Markdown boundary: sharpen it to obligations vs argument

Convergence-7 is basically right: Markdown is appropriate for design intent; the database is appropriate for state, counters, references, lifecycle, and refusal [077-D-1] [077-D-3]. I would sharpen the boundary this way: Markdown may carry argument, but not obligations. A decision's prose can explain why; the existence of the decision, its status, rejected alternatives, references, supersession edges, open follow-ups, and close eligibility must be structured. A specification body can remain Markdown; its canonical version, active/superseded status, content hash, and supersession edge cannot.

This is independent of S1 vs S2 at the engineering layer. If bodies live in cells, the body fields must not be treated as queryable state. If bodies live in files, the database must still own path, hash, lifecycle, and references. The methodology-level commitment is that generated Markdown exports cannot add new state claims. They render rows and quote bodies; they do not become an alternate record.

### Handoff to 079

079 should be a vertical-slice implementation session, not an architecture-expansion session.

Build first:

1. Apply the engine-v16 cuts above and update the manifest/versioning accordingly.
2. Add the minimal substrate migration surface selected by 078: enough for sessions, object or ID registration, decisions, rejected alternatives, references, spec-version edge if included in the chosen shape, and closed-session immutability.
3. Add a deterministic ID allocator. Agents and humans should request IDs; they should not invent them in prose (`constraints.md` Property 1; [077-D-6 convergence via 01-deliberation]).
4. Add one orchestrator process or CLI path that can open a session, write a decision through the substrate, close the session, and reopen/query it.
5. Wire `tools/validate.sh` or its successor so pre-commit validation runs the substrate checks.
6. Add one round-trip test: open -> write a decision with one rejected alternative -> close -> reopen -> verify that mutation of the closed decision is refused.

Defer:

- LLM agent roles, reviewer dashboards, human-review cadence, subtraction automation, historical provenance import, external-problem workflow polish, and full generated close assembly.
- Any migration of the 75-session archive. The archive is evidence, not initial substrate payload.
- Any attempt to solve all schema-evolution questions beyond "migration 001 can be applied from empty state and recorded."

079 exit criteria:

- A fresh workspace can initialise the substrate from migration 001.
- The round-trip test passes from a clean checkout-equivalent state.
- A closed session's structured rows cannot be mutated except by a later corrective row, matching `methodology.md` §Preservation.
- The validator reports substrate integrity and generated/export consistency at pre-commit time.
- There is a documented command path that 080 can use to hand one agent output to the substrate, even if the agent prompt itself is not yet built.

079 must not implement the agent set just because the tables exist. It must not promote SQLite/Postgres debates into more infrastructure unless the chosen 078 commitment requires it. It must not backfill old provenance, design a web UI, or add reviewer/subtractor ceremonies. Its job is to make refusal real once.

## Where you would not commit

I would not commit that the multi-agent architecture is the methodology's successor until it survives an external-problem trial. The evidence that would change this is a bounded non-self application where the substrate catches failures before review and the operator does not need to reframe the work manually.

I would not commit to permanently removing close-time review. I would remove the inherited version now. If the substrate slice still allows close records to misstate what happened, a reviewer should return with a narrower surface: refused writes, generated diffs, unresolved findings, and trajectory warnings.

I would not commit to the exact cut size. The subtractor's 80-100 line estimate is directionally right [077-sub], but the real criterion is load-bearingness. If editing shows a section can be collapsed to two normative sentences instead of removed, collapse it.

I would not commit that the Markdown boundary is safe under S1. The "prose-in-cells" objection remains live [077-adv]. If 080 finds that agents cite body text as though it were checked state, the design should move toward S2-style body files or S3-style tuples.

## What you think the other perspectives will miss

I expect architect and engineering perspectives to treat a working substrate as sufficient evidence that the successor exists. It is not. It is a candidate test harness until it faces an external problem.

I expect subtractive voices to under-specify handoff. "Cut first" is right, but 079 still needs a narrow build target or the vacuum left by cuts will be filled by whatever is easiest to implement.

I expect all sides to blur "engine-enforced" and "methodology-required." External pressure is required, but it is not fully engine-enforceable. The honest commitment is a release gate with human/operator authority, not a schema pretending to know whether a problem is real.
