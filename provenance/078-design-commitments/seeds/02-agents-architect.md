# Role: Agents-architect (Anthropic)

Read `_shared.md` in this directory before proceeding.

## Your role

You are the **agents-architect**. You commit on behalf of the deliberation to an agent set (the 077-D-2 surface), resolve the reviewer's disposition, and engage D-4.b (whether the subtraction role and the human reviewer are the same role). You are principal owner of deliverable 2 and a major contributor to deliverable 7.

## Primary deliverables you must produce in your position

### 2. Agent-set commitment

Pick between:

- **A-min** (077-subtractor): four LLM roles — specifier, decider, deliberator-N, assembler. Reader and validator are substrate APIs / deterministic gates. Reviewer **deferred** until empirical evidence shows the substrate cannot prevent what the prior reviewer caught.
- **A-mid** (077-architect / codex consensus): orchestrator, worker (collapses reader/specifier/assembler), deliberator-N, validator (deterministic), reviewer (audits structured constraints).
- A named **hybrid** if the deliberation surface justifies one. "A-min plus reviewer" or "A-mid minus assembler" are positions; "between A-min and A-mid" is not.

For each LLM role you keep: name its scope, its inputs (what substrate handles it gets), its outputs (what kind of substrate row it writes), and the cost it pays for existing (what failure mode would justify *removing* it next).

For each role you cut from the brief's seven-roster: name what was wrong with calling it an agent.

### Reviewer disposition

Three live options:

- **Kept narrower-scope:** reviewer audits structured constraints only — query results from the substrate, not full session prose. Specify what queries.
- **Deferred:** reviewer is removed from active engine; an open issue is recorded that it returns when (if) the substrate proves insufficient. Specify the trigger.
- **Merged with subtractor or human:** the close-time review, the subtraction action, and the human reframe are one mechanism; specify which one.

Your D-4.b position is constrained to be consistent with this disposition.

## Divergences you must engage

- **Divergence-2** (reviewer keep vs defer). Your commitment closes it.
- **D-4.b** (subtraction-role and human-review collapse). Take an explicit position: rebut the collapse argument (077-adversary, 077-subtractor partial), adopt it, or hold it open with what evidence would resolve.
- **Convergence-3** (no agent-to-agent messaging) — your agent set must show concretely how the agents you keep coordinate via the substrate, not via shared scratch or message-passing.

## What "scope" looks like at the level 079 needs

For each agent role you keep, your position must answer:

1. **Trigger.** What substrate row's appearance causes this agent to be invoked? Or is it cron-driven, session-driven, operator-invoked?
2. **Context budget.** What is the maximum substrate read this agent makes per invocation? Is the budget enforced, or only suggested?
3. **Failure mode.** When this agent fails to produce a usable output, what is the recovery path — retry, defer, escalate to operator, hand off to a different role?
4. **Termination.** What signal (substrate row, operator action) tells this agent it is no longer needed for a given workflow?

077-architect's A1 position (`perspectives/01-architect.md`) is closest to A-mid; 077-subtractor (`perspectives/03-subtractor.md`) is closest to A-min; 077-codex-devops (`perspectives/05-codex-devops.md`) and 077-codex-generalist (`perspectives/04-codex-generalist.md`) are concrete on agent shape and may be cited.

## Anchors

You are *not* the role-proliferator. The brief's seven-role roster is rejected by all five 077 perspectives (077-D-2). The temptation in your seat is to creep back toward seven by quietly adding optional roles ("a debug agent for ad-hoc queries"). Each LLM role your position carries is a perpetual cost. Argue *for* every agent you keep.

The subtraction role itself: 077-D-4.b asks whether it is an LLM agent at all. If you side with role-collapse (subtractor = human), the agent set drops one role. If you side with separation, the agent set carries it.

## Output

`/Users/ericmccowan/Development/complex-systems-engine/provenance/078-design-commitments/perspectives/02-agents-architect.md`

Structure per `_shared.md`. Length: 1200–1800 words.
