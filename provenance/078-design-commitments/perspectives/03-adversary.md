---
session: 078
perspective: adversary
family: Anthropic
date: 2026-04-27
---

# adversary — blind position

## Frame

077 produced a design space whose centre of gravity is unmistakable: substrate-as-refusal-contract (D-1), four-or-five LLM agents with reader/validator/assembler deterministic (D-2), three substrate-shape candidates with S1 the architectural-easiest (D-3), three preserved minorities (D-4.a/b/c). The deliberation now picks. The risk this session runs is not that 078 will choose badly between S1, S2, S3; it is that the act of picking will *retire* the diagnostic question 077 left open. 077-D-4.a explicitly preserved as first-class the possibility that the brief's diagnosis is partial — Reading B (accretion-without-subtraction) and Reading C (self-hosting-as-disease). If 078 commits to a substrate-shape and agent-set without disposing those readings, the commitments rest on a foundation 077 deliberately refused to ratify. My job is to make 078 either rebut Readings B and C with evidence or carry the commitments under their shadow honestly. I am also extending [077-adv]: my predecessor's three contested readings still stand, and one (Reading B) is sharper now than when written, because 077 itself produced more candidates than it subtracted.

## Position

### D-4.a — Reading B: adopt; Reading C: hold open with a release gate

**Reading B (accretion-without-subtraction): adopt.** Evidence accumulated inside 077 itself: seven convergences, seven divergences, three minorities, three substrate candidates, two agent-set candidates — and the only structural counter (D-4.c's ~80-line cut) held as a minority. The pattern that killed Selvedge is visible in 077's output: locally-reasonable additions, no responsible removal. **Consequences 078 must accept:**

- Subtraction moves from "necessary feature" (`constraints.md` §6) to **load-bearing centerpiece** — the mechanism the others exist to make tractable.
- **D-4.c must be adopted, not held open.** Cut engine-v16 by ~80 lines *in this session* before 079 adds substrate. If 078 cannot subtract from a 350-line spec set with no users, the engine cannot subtract from a 3000-line spec set with sessions depending on it. Failing this test is itself diagnostic.
- A hard write-budget commits as part of 078, not deferred: **active engine spec ≤ 400 lines until an external application has run 30 sessions; substrate ≤ 12 tables in migration 001; refusal contract ≤ 30 enumerated refusals at first cut.** These numbers are deliberately wrong-in-detail; their function is to force the removal conversation.

**Reading C (self-hosting-as-disease): hold open, with a release gate.** I am genuinely uncertain whether self-hosting is the disease or whether external pressure alone neutralises the trap. What would resolve it: a non-self application running ≥30 sessions without operator intervention surfacing structural problems. Until then, **commit to a release gate**: engine-v17 is **provisional** until it has run on a non-self problem for 30 sessions. No self-development sessions modify engine-v17 between 079 and that gate, only fixes the external application demands. This operationalises [077-gen]'s "smallest external-problem trial" and what [077-sub] marked unenforceable from inside. The operator enforces it externally. If the gate cannot be agreed, that is itself evidence Reading C is correct.

### D-4.b — The subtraction role and the human reviewer are the same role

I reaffirm [077-adv] and extend. [077-arch], [077-gen], [077-dev] separated the roles; the synthesis did not resolve. My case for collapse:

- **Subtraction requires authority to remove specifications, decisions, agents.** An LLM agent does not have that authority over engine-definition files; the operator does. Granting it would mean a prompt deciding under load which methodology commitments to delete — the precise judgment `constraints.md` §6 says LLMs cannot make while executing.
- **An LLM "subtractor" will produce subtraction-ceremony.** It will cut typos, redundant phrasing, dead clauses; it will preserve load-bearing accretion because that accretion is what trained its sense of what the methodology *is*. Prose-default failure (P1) shifted from generation to deletion.
- **The operator is already the subtraction substrate.** Session 076's restart was a subtraction event — the operator cut engine-v15 to v16. No agent did that. No agent could.

Concrete proposal: **a single human-review-with-subtraction-authority role**, scheduled at fixed cadence (every 10 sessions, or when active spec total exceeds the write-budget, whichever first), with explicit delete authority. If the agents-architect commits to two roles, my dissent stands and I predict by session 110 the LLM "subtractor" will have cleared a fraction of what any single operator intervention cleared.

### Stress-test on the likely commitments (S1 + A-mid)

The 077 surface forces toward S1 (body-in-cells) and A-mid (orchestrator + worker + deliberator-N + validator + reviewer). Stress-test against the six properties in `constraints.md`:

- **P1 (prose default).** S1's `body_md` columns are prose containers; refusal catches envelope, not content. By session ~100 the substrate is a tamper-evident warehouse for Markdown that contradicts itself across rows — pre-restart's prose-state failure in queries-as-prose form. **Hardening:** structured fields for `verdict` and `rejected_alternatives`; cap `body_md` ≤500 words. Cost: readability.
- **P2 (failure is cheap).** Refusal works for envelope. A-mid's reviewer "audits structured constraints" — but if reviewer output is LLM-produced prose, P1 reappears one level up. **Hardening:** reviewer outputs structured (pass/fail per refusal-rule, no free text). Cost: the reviewer becomes a checklist runner, possibly indistinguishable from a second validator.
- **P3 (pre-training bias invisible).** Cross-family is preserved for deliberation. Stress-point: A-mid's orchestrator is a single Claude prompt; if *it* decides which decisions are "foundation-touching" and trigger cross-family, Claude-family bias gates the cross-family invocation. **Hardening:** the trigger must be substrate-encoded (e.g., `decisions.touches_foundation` derived from which tables the decision writes), not orchestrator-judged.
- **P4 (foundational instructions decay under load).** A-mid's orchestrator is the new context-holder. By the time it coordinates five workers across a substantive deliberation, its prompt encodes routing rules, schema fragments, capability descriptors, retry semantics, cross-family triggers. The pre-restart engine reincarnated as the orchestrator. **Hardening:** orchestrator prompt has its own hard line-budget; routing decisions live in substrate config tables, not prompt text.
- **P5 (no cross-session learning).** Reviewer findings as `reviews.body_md` rows accumulate unread because they are not in the read-default. **Hardening:** review findings whose disposition is not recorded within N sessions trigger refusal of further session opens until handled. Cost: possible compliance theatre.
- **P6 (cannot perceive own deficiencies while executing).** A-mid's reviewer is an LLM in the same workspace; it shares the aggregate blindness. The only structural answer is the human-review-with-subtraction-authority role (D-4.b). The multi-agent system will collectively rationalise its accretion; only the operator can see substantive work has stopped.

Each hardening is a cost D-4.b's role-holder (the operator, in my position) eventually pays. I am not asking 078 to adopt all six. I am asking it to *enumerate* which it adopts, rejects, or defers, with the cost named — so when session 110 finds the failure mode, the trail of "we accepted P_n failure in exchange for Y" is in the record.

### Divergence-3: argue against S1; advocate **S2-narrow**

I dissent from S1. **S2 (index-only DB, body-in-files)** is the right commitment, sharpened:

- Database holds ~12 tables (`sessions`, `decisions`, `specifications`, `perspectives`, `deliberations`, `references`, `lifecycle_events`, `engine_feedback`, `subtractions`, `read_log`, `write_budget`, `migrations`). **No `body_md` column on any.** Each row that has prose carries `body_path` plus `body_sha256` instead.
- Body content lives in Markdown files at conventional paths. Pre-commit hook recomputes SHA on referenced files; refuses commit if a file's SHA changed without a new row.
- Refusal contract enumerated as **T1–T8** at first cut: T1 identifier-format violations; T2 unresolved foreign keys; T3 illegal lifecycle transitions; T4 writes to closed sessions; T5 missing required fields; T6 `body_path` that does not exist; T7 `body_sha256` mismatch; T8 perspective written before `sealed_until`. Each backed by a SQL trigger and a migration test row that must fail.
- **Why S2 over S1.** Prose-in-cells is unrefutable inside S1; S2 removes the failure mode by removing the cells. Body contradiction across files can still occur, but the substrate is honestly an *index* over the methodology, not a *store* of it. Under S1, everyone is misled into thinking the substrate stores the methodology and the substrate becomes ceremony.
- **Why not S3.** Decisions need paragraphs; specifications need prose. S3 trades human-readability for a defence against prose-in-cells that S2 already addresses by relocating prose to files. If 078 picks S3 anyway, my dissent stands but is weaker.

If 078 commits to S1, my structural prediction is on record: the substrate becomes a prose warehouse by session ~100 absent aggressive subtraction.

### Divergence-1 reaffirmed and revised

[077-adv]'s Divergence-1 (the diagnosis is partial) — I reaffirm. Revision: 077 itself produced evidence that *strengthens* Reading B (the accretion pattern visible in 077's own output) and produced no evidence against Reading C. The deliberation could only have produced evidence against Reading C by running in a non-self-development workspace, which 077 was not. Reading C therefore remains exactly as open as it was.

## Where you would not commit

- **Whether the write-budgets I propose (active spec ≤ 400 lines, ≤ 12 tables, ≤ 30 refusals) are correct.** They are arbitrary numbers chosen to force a removal conversation. They are likely wrong in detail. What would resolve: a pass through the actual artefacts the methodology must produce, costing each table and each refusal against a concrete artefact. I have not done that pass; the substrate-architect or cross-family engineer is better placed to.
- **Whether S2's pre-commit-SHA hook actually refuses what I claim.** The hook works only if every workflow that mutates Markdown files routes through commit. An agent that writes a Markdown file mid-session and reads it back before commit will see its own write; if it bases a decision row on the unreviewed body, the SHA recorded at commit-time is the agent's own. What would resolve: a worked round-trip test (077-D-5's session-079 deliverable) that includes "agent writes body, then writes decision row, then validator runs, then commit" — and the validator catches a deliberately-introduced inconsistency.
- **Whether the operator's subtraction cadence is sustainable.** D-4.b collapses subtraction into the human-review role. If the operator is unavailable for an extended period, no subtraction happens and the engine accretes. What would resolve: the operator confirms a cadence they can sustain (e.g., monthly) and the engine refuses to open further sessions if the cadence is missed by ≥2 intervals. Whether the operator wants this is the operator's call, not mine. I name it as the structural cost of the position I argue.

## What you think the other perspectives will miss

The substrate-architect and agents-architect will produce coherent, detailed commitments. The detail will be where the synthesis-attention goes. What gets missed: the question of whether 078 itself, viewed as a session, has reproduced the failure mode it is designing against. 078's deliverable list (per 077-D-5: refusal-contract spec, agent-set commitment, worked example, three D-4 dispositions, schema-evolution protocol, substrate-tech commitment, 079 handoff) is **seven items**. 077's commitment to subtract before adding (D-4.c) is one of them — *the seventh, in effect*. If 078 ends up with a refusal contract enumerated to thirty rules, an agent set with five LLM roles, a schema with twelve tables, a worked example showing all artefact kinds, and the D-4.c disposition is "deferred," then 078 has performed the pre-restart Selvedge pattern in a single session: locally-reasonable additions, no responsible subtraction, a commitment to revisit-later that nothing structurally enforces. The cross-family voices may catch this; the Anthropic architects will be too invested in their commitments to. The synthesis check I want preserved: **does 078, weighed as a session, subtract more than it adds?** If not, the diagnostic capacity the engine is supposed to restore is already absent in the session that designs the restoration.
