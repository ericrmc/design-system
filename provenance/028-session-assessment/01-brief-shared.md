---
session: 028
title: Brief (shared) — §5.3 Pacer aggregate-hard-budget minority deliberation
date: 2026-04-23
status: complete
---

# Shared Brief — Session 028

**This brief is byte-identical across all three perspectives in §§1–3, §5–§6. §4 role-specific stance varies per perspective. This file is committed before any perspective is launched and is the deliberation's anchor.**

## §1 Methodology context

You are reasoning within the Selvedge engine, self-development application, Session 028. The engine is at `engine-v4` per `specifications/engine-manifest.md`. The methodology you are following is specified in `specifications/methodology-kernel.md` v5 (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close). Multi-agent deliberation triggers and recording schema are in `specifications/multi-agent-deliberation.md` v4. Two-tier validation is in `specifications/validation-approach.md` v5. The workspace's access discipline (default-read surface vs archive surface) is specified in `specifications/read-contract.md` v2 — **this file is the subject of the current deliberation**.

The Selvedge methodology's value is producing durable artefacts with preserved reasoning, and evolving the system by running the same mechanic on its own outputs. Minorities are preserved as first-class dissent with activation warrants; vindications and activations are recorded; specifications are versioned and superseded rather than overwritten.

## §2 Problem statement

`read-contract.md` v2 §5.3 Pacer aggregate-hard-budget minority (preserved verbatim from Session 023) states:

> Position: adopt aggregate default-read surface hard budget at 90K hard / 80K soft now; naming a budget creates the forcing function that watchpoint-only reporting lacks. Activation warrant: if aggregate exceeds 100,000 words OR grows >10% in a single session without compensating restructure, this position becomes preferred revision direction.

**At Session 027 close, the activation warrant fired.** Aggregate crossed 100,000 words (Session 027 close projected ~102,500; actual post-close 105,399 words across 39 files per Session 028 pre-session validator run). Growth 99,532 → 105,399 = +5,867 = +5.9% (under the 10% trigger; the absolute-threshold disjunct is the primary trigger).

The §5.3 minority has now moved from "preserved with activation warrant" to "preferred revision direction." Session 028's task is to decide what the engine does in response.

## §3 Current state facts

### §3a Aggregate trajectory (validator-measured or validator-projected)

| Session close | Aggregate words | Delta | File count | Threshold state |
|---|---|---|---|---|
| 022 close (post-restructure) | ~81,500 | — | 33 | below advisory (90K) |
| 023 close | ~83,000 | +1.8% | 33 | below advisory |
| 024 close | ~92,500 | +11.4% | 35 | advisory crossed |
| 025 close | 95,675 | +3.4% | 37 | advisory; under activation |
| 026 close | 99,532 | +4.0% | 38 | advisory; within 468 words of activation |
| **027 close** | **105,399** | **+5.9%** | **39** | **activation crossed** |

Growth drivers identified in prior closes:
- Close-file accretion (Session 026 flagged close-verbosity pattern n=2 at Sessions 025/026 Path-A closes; Session 027 close at 5,253 words is the largest to date, driven by substantive-deliberation content).
- New session-close files entering default-read surface at each close (+1 file per session, typically 2,000–5,000 words).
- Substantive-deliberation content temporarily enters default-read during session (three perspective raws + synthesis + brief ≈ 10,000 words during-session aggregate overhead) then moves to archive-surface at close per `read-contract.md` §1 item 8.

### §3b §2a aggregate report at engine-v4 (current)

Per `read-contract.md` v2 §2a (Session 023 D-086 R10):

- **Advisory:** aggregate ≥ 90,000 words. Validator emits advisory note; next session should note the aggregate in close.
- **Activation:** aggregate ≥ 100,000 words OR aggregate grows >10% in a single session without compensating restructure. Session N+1 should deliberate whether to add an aggregate hard budget per §5.3 minority.

At engine-v4 adoption (Session 023), §2a described aggregate at ~81,500 / 33 files — below both thresholds. At Session 028 open, aggregate is 105,399 / 39 files — activation crossed by 5,399 words.

**§2a is informational only at engine-v4.** It does not pass/fail/warn in the validator; it emits advisory or activation notes. The §5.3 minority proposed replacing this with a hard budget.

### §3c Per-file budget state

Per `read-contract.md` v2 §2 (Session 023 D-086 R1–R3):

- Hard ceiling: 8,000 words per default-read file (fail).
- Soft warning: 6,000 words per default-read file (warn).

Current state (validator-measured at Session 028 open):
- `multi-agent-deliberation.md`: 6,386 words — exceeds 6K soft; within 8K hard. Designed soft-warning persistence across five closes per D-088 R1 / D-090 / D-092 / D-094 (Session 023 Skeptic §5.2 minority **retroactively vindicated** at Session 027 because no file reached 7,500 and no restructure-for-budget event occurred within five sessions).
- Largest default-read file (after MAD): `reference-validation.md` at 5,166 words — well within per-file budget.
- Largest `03-close.md`: Session 027 at 5,253 words.

### §3d §5.1 / §5.2 / §5.3 / §5.5 minority states

- **§5.1 Pacer 10K/7.5K per-file:** unactivated; no activation-trigger event.
- **§5.2 Skeptic no-change + warrant-literalism:** retroactively vindicated Session 027; ongoing tracking complete.
- **§5.3 Pacer aggregate-hard-budget:** **activated Session 027; preferred revision direction for Session 028.**
- **§5.5 tokeniser-drift watch:** unactivated; no single-Read token-budget failure.

### §3e Engine-version cadence state

- engine-v4 preserved across Sessions 024–027 (five consecutive non-bump closes).
- §5.4 Session 022 cadence minority: activated-not-escalated; R9 escalation trigger aged out at Session 026 close.
- OI-018 tracks engine-manifest §5 revision; activation-trigger-gated.

**If Session 028's decision produces a substantive revision to `read-contract.md` (engine-definition file), engine-v4 → engine-v5 bumps per engine-manifest §5.** This would be the fourth bump in eight sessions (engine-v2 Session 021; engine-v3 Session 022; engine-v4 Session 023; engine-v5 Session 028 hypothetical) — outside the original "3-bumps-in-4-sessions" R9 window but contributing to the long-run cadence tracked by §5.4 (now activated-not-escalated on content grounds).

### §3f Alternative remediation mechanisms available

If Session 028 declines to adopt an aggregate hard budget but seeks to respond to activation, per `read-contract.md` v2 §8 (default-read budget at session close) remediation options include:

- **Rotate aged session closes to archive-pack form.** Per §1 item 7, every `03-close.md` is default-read; this could be revised to "every `03-close.md` for sessions within the last N sessions is default-read; older closes are archive-surface with SESSION-LOG serving as the index." This would trim aggregate by ≈3,000 × (number of rotated closes) words.
- **Reduce per-file close budget.** Tighten the expected `03-close.md` size via prompt guidance (not a hard budget). Session 026 flagged close-verbosity as pattern n=2; Session 027 close did not adopt a tighter shape.
- **Archive-migrate load-bearing-but-aged specification detail.** E.g., engine-manifest §7 version history's long-form per-version text could move to archive-surface with §7 reduced to a citation-only table.
- **Restructure default-read §1 enumeration.** The §1 enumeration is closed; revising it is substantive but would directly address aggregate.

## §4 Role-specific stance

**(This section varies per perspective; the three role-specific stances are in `01a-perspective-pacer-advocate.md`, `01b-perspective-skeptic-preserver.md`, `01c-perspective-synthesiser-integrator.md`.)**

## §5 Design questions

Each perspective responds to all of Q1–Q7.

**Q1 Adopt-or-preserve.** Should Session 028 convert §5.3 from preserved-minority to active specification (aggregate hard budget becomes normative)? Or continue preservation with activation recorded and state that further evidence is required? Or revise the §5.3 proposal in light of post-activation information (e.g., propose different values than the original 90K/80K)?

**Q2 Budget values.** If adopting an aggregate hard budget, at what values? Options include: the minority's original 90K/80K (hard/soft); the current §2a threshold structure re-framed as budget (100K hard / 90K soft); higher values reflecting current 105K state plus headroom (110K hard / 100K soft); tighter values forcing immediate restructure (85K hard / 75K soft). Justify whatever values you recommend; the minority's original proposal is not privileged over alternatives that post-activation evidence supports.

**Q3 Remediation mechanism.** What happens when aggregate approaches or exceeds the ceiling? Options include: per-file restructure (addresses aggregate only indirectly); aggregate-specific restructure (archive-migrate lowest-value default-read content); old-close rotation (closes before Session N - X become archive-surface); hybrid (validator warns → next session deliberates which lever to pull). What is the right mechanism?

**Q4 Interaction with per-file budgets.** The §5.3 minority proposes aggregate budget in addition to per-file budget. Does the aggregate budget override per-file, supplement it, or operate orthogonally? If aggregate fires while no per-file has (current state), does this imply per-file values are too lax relative to aggregate? Or does it mean per-file control is insufficient alone (the minority's framing)?

**Q5 Engine-version interaction.** A substantive revision to `read-contract.md` is an engine-v bump (engine-v4 → engine-v5 if adopted). This would interact with §5.4 cadence minority (activated-not-escalated; R9 aged out). Should §5.4 be engaged in this deliberation (fold cadence reassessment into Path G), addressed separately per OI-018, or neither? Separately: if Session 028 adopts a non-substantive response (e.g., records activation without conversion), engine-v4 preserves and §5.4 is untouched.

**Q6 Methodology-level observation.** The §2a aggregate report was added Session 023 as a prophylactic. It fired at Session 027 as designed. Is this a "designed mechanism functioning" (like Session 024's MAD 6K-soft) or does activation reveal a gap? What does the activation event teach about the engine's self-scaling mechanisms? Is there a principle that should be added to the methodology (e.g., "prophylactic thresholds should be set at a value the system actually hits within N sessions, not at a value the system rarely approaches")?

**Q7 Anti-laundering self-check.** The engine's discipline against laundering (OI-015) requires that decisions not silently re-propose rejected ideas and that new arguments cite new information. §5.3 was rejected at Session 023 (the majority adopted watchpoint-only §2a over the Pacer's proposed hard budget). It is now preferred-revision-direction. What new information has arrived since Session 023? Is the activation-warrant firing *itself* new information, or does it merely execute a decision already-made at Session 023? Would a Session 023 participant recognise Session 028's Path G as coherent continuation of the preservation discipline or as a reversal?

## §6 Response format

Format your response as a Markdown file with the frontmatter fields:

```yaml
---
session: 028
title: Perspective — <role name>
date: 2026-04-23
status: complete
perspective: <role name>
committed_at: <ISO-8601 timestamp at commit>
---
```

Response body, one section per design question (Q1 through Q7). Target 2,500–4,500 words total body; do not exceed 6,000 words (per `read-contract.md` v2 soft warning). If you exceed 8,000 words, your response will be archive-packed at session close per `read-contract.md` §9.

Include an **Honest Limits** section at the end declaring any claims you could not fully ground in the brief's §§1–3 facts, any positions you left undeveloped for brevity, and any uncertainty ranges in your reasoning.

**Reason primarily from this brief.** Do not perform workspace reads during the independent phase (you are a Claude subagent without tool access in this context). Ideas that arrived through pretraining rather than from the brief's content must be flagged as external inputs per the PROMPT.md rule.

## §7 Constraint on external imports

The Selvedge methodology forbids silent import of ideas from outside the deliberation's explicit inputs. The brief's §§1–3 are your explicit inputs for factual grounding. Your role-specific stance (§4) is your explicit framing. Pretraining-derived knowledge of information-architecture, systems-design, or organisational-scaling principles must be flagged as external input; reason primarily from the Selvedge engine's own specifications and history.

If your analysis requires a factual claim not present in the brief, either: (a) flag it explicitly as external-input and note its source, or (b) note in Honest Limits that the claim would need workspace-verification before a decision could rest on it.

## §8 Closure

End your response after the Honest Limits section. Do not attempt synthesis; synthesis is a separate step performed by a non-perspective synthesiser per MAD v4 §Synthesis.
