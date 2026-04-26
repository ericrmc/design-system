---
session: 071
title: Shared Brief — phase-2 MAD on three-record joint-scope (EF-067 + EF-059 + EF-068-substrate-load-bearing)
date: 2026-04-26
status: complete
brief_class: shared
---

# Shared Brief — Session 071 phase-2 MAD

## §1 Methodology context

You are participating in the **Selvedge engine**'s self-development application, Session 071. The engine evolves its own specifications by running its own multi-agent deliberation process on its own outputs. The methodology is documented at `specifications/methodology-kernel.md` v6 + `PROMPT.md` + `prompts/development.md`. Multi-agent deliberation discipline is `specifications/multi-agent-deliberation.md` v4. Validation discipline is `specifications/validation-approach.md` v7. Read-discipline is `specifications/read-contract.md` v6.

You are one of four perspectives in a 4-perspective two-family Multi-Agent Deliberation (MAD) at S071, pre-ratified at S070 D-260 per S057 D-196 + S068 D-251 precedent. The lineup:

- **P1 — Harness-Discipline Architect** (Claude family, Anthropic; this brief if you are P1)
- **P2 — Incrementalist Conservator** (Claude family, Anthropic; this brief if you are P2)
- **P3 — Outsider Frame-Completion** (codex/GPT-5.5 family, OpenAI; this brief if you are P3)
- **P4 — Cross-Family Reviewer Laundering-Audit** (codex/GPT-5.5 family, OpenAI; this brief if you are P4)

Your role-specific stance is in your own `01[a-d]-stance-brief-*.md` file alongside this shared brief. You are reasoning in independence-preservation phase: you write your raw perspective without seeing the other three perspectives' outputs. Synthesis happens after all four return.

## §2 Problem statement

Three engine-feedback records are bundled at joint-scope per S069 D-256 (cross-linkage joint-scope expansion of S068 D-251 from two-record to three-record):

- **EF-067-reviewer-wall-clock-self-report-unreliable** (operator-surfaced post-S067 audit; Tier 2.5 (γ) reviewer wall-clock + token self-reports are unreliable; baseline propagates via reviewer-prompt-template).
- **EF-059-harness-telemetry-feed-for-tier-2-reviewer** (application-agent filed at S062; the (γ) reviewer's audit packet is structurally incomplete without harness-telemetry digest covering failed-tool-calls + repeated-Reads + reviewer-cost; (z6) digest specified-deferred per S062 D-225 with three named activation preconditions all satisfied at S067-S068).
- **EF-068-substrate-load-bearing-and-harness-telemetry** (operator-surfaced post-S068 audit; substrate use at session-open is opt-in and orchestrator defaults to opt-out; n=4 (now n=5 with S070; broken to n=1 at S071) consecutive sessions of orchestrator-self-reported substrate non-use; the orchestrator's read-discipline behavior is unobservable to next session, operator audit, and (γ) reviewer).

**The shared structural surface across all three** (per S070 design-space.md §4): claims about cross-session state continue to ride on agent self-report despite spec-side mechanisms intended to enforce harness-side or distinct-agent verification. The principled-asymmetry articulation at validation-approach.md v7 §Principled Asymmetry names the gap directly:

> Claims about unresolved validation debt, substantive progress, engine-definition change, and repeated warnings (the surfaces where self-assessment was empirically insufficient per the S051-S058 honest-limit chain) require Tier 2.5 cross-family review when triggered.

But the asymmetry's **enforcement** is missing across three concrete surfaces: reviewer-cost trajectory (EF-067 self-reported); failed-tool-call/repeated-Read pattern detection (EF-059 telemetry-uncaptured); substrate use at session-open (EF-068 unobservable). Harness-side measurement is the missing primitive for all three.

**The phase-1 design-space at S070** (`provenance/070-session/design-space.md`, ~6,042 words) surveys: EF-068 Direction 1 sub-options (a)-(e) + EF-068 Direction 2 D2.1/D2.2 + EF-067 Directions A/B/C + EF-059 (z6) digest scope (original + EF-068-extended) + capture mechanism candidates CM1-CM4 + cross-product implementation candidates (α)-(ε) + Q1-Q10 design questions + cross-spec interactions.

**Your task as a perspective**: deliberate the design questions Q1-Q10 from your role-specific stance + reach a position on the cross-product candidate (α/β/γ/δ/ε) you favour or oppose + surface reframes if the design-space's framing has missed something + reach a position on adoption shape (same-session-bounded per S058 D-199 OR multi-session phase-3 arc per S062 D-220).

## §3 Design questions Q1-Q10 (from S070 design-space.md §7)

- **Q1**: Harness-side-enforcement vs spec-side-encouragement balance — how far should engine shift from spec-side-only to harness-side-additional?
- **Q2**: Minimum-viable per S062 §10.4-M16 P2 precedent vs full architectural shift — does the joint-scope's resolution land at smallest-scope-addressing-laundering-surface (α/β) or full-scope-addressing-root-cause (γ)?
- **Q3**: Load-by-default vs preserve-deferred-tools-friction — what are the operational implications for context-window pressure (substrate tools loaded at session-open consume context budget) + tool-availability discoverability (deferred-tools require ToolSearch step; teaches what's available)?
- **Q4**: (z6) scope breadth — failed-tool-call only vs orchestrator-side telemetry inclusion vs reviewer-cost inclusion vs all?
- **Q5**: Digest implementation locus — CM1 (Claude Code hooks) vs CM2 (external wrapper) vs CM3 (post-hoc analysis) vs CM4 (in-session emission)?
- **Q6**: Reviewer self-report disposition — Direction A (drop fields entirely) vs Direction B (subsume harness-measured) vs Direction C (honest-limit-only)?
- **Q7**: Check 29 evidence-probe scope — close-narrative grep only vs 00-assessment grep + close-narrative grep vs structured-frontmatter declaration?
- **Q8**: Same-session-bounded adoption per S058 D-199 precedent vs multi-session phase-3 arc per S062 D-220 precedent vs hybrid (minimum-viable same-session + (z6) deferred multi-session)?
- **Q9**: Bundle-vs-defer for EF-068-read-write-rebalance per intake's own framing — should the four-record bundle be opened at S071 phase-2 MAD per operator-discretionary reopen warrant?
- **Q10**: Engine-v impact — minor (spec amendments only) vs substantive (new spec section codifying digest) → engine-v13 candidate trajectory?

## §4 Cross-product candidates (from design-space §6)

Brief recap (full matrix in design-space §6):

- **(α)** Spec-only minimum-viable: load-by-default `.mcp.json` + promote `forward_references` to required step in `prompts/development.md` (engine-v13 candidate). EF-067 Direction C + EF-059 deferred.
- **(β)** Spec + tooling lightweight: (α) + `tools/validate.sh` check 29 candidate (WARN-only evidence-probe).
- **(γ)** Full (z6) digest implementation: harness-side instrumentation hooks + structured-log-emission protocol + `validation-approach.md` v7 → v8 substantive + reviewer-prompt-template extension. EF-067 Direction B (subsumed). EF-068 Direction 1 (a)+(b) bundled. EF-068 Direction 2 D2.1.
- **(δ)** Substrate-aware check 26 activation: implement check 26 substrate-aware branch (currently aspirational comment).
- **(ε)** Hybrid bounded-then-extended: (α)/(β) shipped at S072+ phase-3; (γ) phase-3 deferred to S073++ after observation period.

## §5 Response format

Produce a single markdown file at `provenance/071-session/01<your-letter>-perspective-<your-role-slug>.md` with this structure:

```markdown
---
session: 071
title: Perspective <role> — <one-line stance summary>
date: 2026-04-26
status: complete
perspective: <role-slug>
committed_at: <ISO-8601>
---

## Q1 — <answer>
## Q2 — <answer>
...
## Q10 — <answer>

## Cross-product candidate position
<which of α/β/γ/δ/ε you favour or oppose; argument grounded in the design questions>

## Frame critique (if any)
<reframes if design-space §3-§7 missed something; for P3 + P4 especially>

## Honest limits
<your perspective's known blindspots; pretrained framings flagged as external imports per PROMPT.md rule; uncertainty acknowledged>

## Dissent-preservation
<positions you would want preserved as first-class minority if the synthesis adopts a different direction>
```

Target length: 1,500-3,000 words. Cite design-space §X.Y when referencing the design-space; cite intake/triage record names when grounding in intake; cite spec section numbers when grounding in spec text. Quote key language verbatim where load-bearing.

## §6 Constraint on external imports (PROMPT.md rule)

Per PROMPT.md "Do not import ideas from outside the process": reason primarily from this brief + the design-space.md + the three triage records + your prior knowledge of the workspace's specs. If your reasoning surfaces an idea from your pretraining (a pattern from another methodology, a software-engineering convention, an architectural framing not encoded in the workspace), flag it explicitly as an external input rather than committing it directly. This is required for the workspace's traceability discipline. Such ideas may inform your reasoning but must be marked as `[external import: <source>]` so synthesis can audit pretraining-vs-workspace-derived contributions.

## §7 Read these files before responding

- `provenance/070-session/design-space.md` (PRIMARY brief-extension; ~6,042 words)
- `engine-feedback/inbox/EF-068-substrate-load-bearing-and-harness-telemetry.md`
- `engine-feedback/inbox/EF-067-reviewer-wall-clock-self-report-unreliable.md`
- `engine-feedback/inbox/EF-059-harness-telemetry-feed-for-tier-2-reviewer.md`
- `engine-feedback/triage/EF-068-substrate-load-bearing-and-harness-telemetry.md`
- `engine-feedback/triage/EF-067-reviewer-wall-clock-self-report-unreliable.md`
- `engine-feedback/triage/EF-059-harness-telemetry-feed-for-tier-2-reviewer.md`
- `specifications/validation-approach.md` v7 (especially §Principled Asymmetry + §Tier 2.5 + §(z5) + §(z6) + §10.4-M21 through M25 minorities)
- `specifications/multi-agent-deliberation.md` v4 §Graceful Degradation (referenced if substrate-availability-as-precondition direction surfaced)
- `prompts/development.md` §How to operate paragraph (the substantive amendment surface for EF-068 Direction 1 (b))
- `tools/validate.sh` lines around check 26 substrate-aware branch comment (the implementation surface for EF-068 Direction 1 (e))
- Your `01<your-letter>-stance-brief-*.md` file (your role-specific stance)

## §8 Decision-procedure (recap)

After all four perspectives return, the orchestrator at S071 (Claude family; not a perspective) synthesises to `01-deliberation.md` per cross-family weighted convergence. **3-of-4 across-families adoption signal** (per S058 D-199 + S062 D-220 precedent) triggers same-session-bounded adoption OR multi-session phase-3 arc per direction adopted. Below threshold preserves design-space + names follow-on phase-2 MAD or phase-3 shape.

The synthesis preserves dissent as first-class minorities per `multi-agent-deliberation.md` v4 §Synthesis preserve-dissent discipline. Your `## Dissent-preservation` section is the input that lets the synthesis honor your position even if synthesis adopts a different direction.

A Tier 2.5 (γ) cross-family reviewer at S071 close audits the synthesis + decisions per Layer 2 trigger (b) substantive-arc-class.
