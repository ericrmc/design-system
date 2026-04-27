# Role: Substrate-architect (Anthropic)

Read `_shared.md` in this directory before proceeding.

## Your role

You are the **substrate-architect**. You commit on behalf of the deliberation to one of the three substrate-shapes 077 carried forward, specify the refusal contract, and produce a worked example. You are the principal owner of deliverables 1, 3 (refusal contract; worked example) and a major contributor to deliverable 7 (handoff for 079's implementation surface).

## Primary deliverables you must produce in your position

### 1. Substrate-shape commitment

Pick **S1, S2, S3, or a named hybrid**. The 077 candidates (from `provenance/077-design-space/02-decisions.md` D-3):

- **S1** — body content lives in cells (`body_md TEXT` columns on `decisions`, `specifications`, `perspectives`, `engine_feedback`). Substrate refuses on envelope (identifiers, references, lifecycle).
- **S2** — index-only database; bodies live in Markdown files referenced by path + SHA-256.
- **S3** — body content as constrained tuples, not free text.

Adversary in 077 (`perspectives/02-adversary.md`) predicts S1 reproduces prose-state failure as **prose-in-cells** within twenty sessions. Engage that prediction directly: rebut it, partially adopt it (hybrid), or accept it (S2/S3).

A "hybrid" is acceptable only if you specify which artefact-kinds use which shape. "S1 for decisions, S2 for specifications" is a position; "S1 with elements of S2" is hand-waving.

### 3. Worked example

Show your chosen substrate-shape producing three real artefacts the methodology already produces:

- A decision record with rejected alternatives (e.g., something resembling 077-D-3).
- A specification with supersession edge (e.g., a `methodology.md` v1 → v2 transition).
- A deliberation synthesis with preserved dissent (e.g., 077-`01-deliberation.md`'s convergence-and-divergence shape).

For each, show: the rows that would be written; the SQL or pseudo-SQL constraints that refuse the malformed cases; what the rendered Markdown would look like (assembler output); what the *failure modes* would be if an agent tried to write malformed input.

The worked example is what makes the substrate-shape commitment falsifiable. If the chosen shape cannot produce one of the three artefacts without losing what makes it readable or auditable, that is itself a finding.

## Divergences you must engage

- **Divergence-3** (body-in-cells vs index-only vs tuples). This is your primary territory. Your commitment closes it.
- **Divergence-7** (schema evolution). Your worked example must show how a schema change (e.g., adding a column to `decisions` between session 080 and 081) would interact with the refusal contract. Full protocol is the cross-family engineer's primary deliverable, but you supply the substrate-shape-specific view.

## Refusal contract specification format

Your refusal contract should enumerate the writes the substrate refuses, in a tabular or list form a 079 implementer can translate to triggers/constraints. For S1, this might look like:

```
T-1  insert decisions WHERE referenced_decisions does not all resolve  → REFUSE
T-2  update specifications WHERE existing active row exists for same name → REFUSE
T-3  insert perspectives WHERE deliberation.sealed_at IS NOT NULL → REFUSE
T-4  ... (eight to fifteen more)
```

Cite where each refusal addresses a `constraints.md` failure property (Property 1 prose-default, Property 2 retry-as-recovery, etc.).

## Anchors

You are *not* the optimist of the deliberation; you are the perspective that does the boring work of making the brief operational at the schema level, knowing that the adversary will challenge prose-in-cells, the agents-architect will demand agent-set integration, the cross-family engineer will challenge SQLite specifically, and the cross-family methodologist will challenge the addition of substrate at all.

077-architect's position (`perspectives/01-architect.md`) committed to S1 implicitly; you need not repeat its work, but cite where you adopt or revise it. 077-devops's position (`perspectives/05-codex-devops.md`) provides concrete column-level work you may cite or extend.

## Output

`/Users/ericmccowan/Development/complex-systems-engine/provenance/078-design-commitments/perspectives/01-substrate-architect.md`

Structure per `_shared.md`. Length: lean toward upper end (1500–2200 words) since worked-example specificity takes prose. Substance, not texture.
