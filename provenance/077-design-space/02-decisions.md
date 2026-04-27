---
session: 077
title: Decisions — design-space output
date: 2026-04-27
engine_version_at_decision: engine-v16
decisions: 5
---

# Decisions

This session does not commit to a successor architecture. Per `provenance/076-engine-restart/03-close.md` §"What session 077 should address," 077 produces the *design space* — the candidate architectures, the open questions, and the rejected directions with reasons. Session 078 picks against this surface.

The five decisions below shape the surface 078 inherits. They draw from `01-deliberation.md`'s synthesis, which preserves dissent across the five blind perspectives (`perspectives/01-architect.md`, `02-adversary.md`, `03-subtractor.md`, `04-codex-generalist.md`, `05-codex-devops.md`).

---

## D-1 — Frame the substrate as a refusal contract, not a storage choice

**What.** The design-space surface handed to session 078 frames the database substrate as the system's *enforcement boundary*. Every candidate architecture session 078 considers must specify what the substrate refuses, not only what it stores. Schemas-as-warehouse (where the substrate accepts whatever the agent writes) are out of scope.

**Why.** All five perspectives converged on this framing (Convergence-1). The brief in `constraints.md` §2 names "models treat failure as cheap" as a structural property; refusal at the substrate boundary is the structural friction that makes the failure expensive. The cross-family voices both flagged that "use a database" without refusal-specification reproduces the prose-state failure mode in queries-as-prose form (`[gen]`'s "under-specification at the refusal boundary"; `[dev]`'s "I expect some perspectives will treat 'database' as storage rather than refusal").

This is sharper than the brief's own language ("integrity guarantees") and pulls a load-bearing claim from the deliberation that the brief alone did not commit to.

**Rejected alternatives.**

- **R-1.1 — Substrate as warehouse with audit-time validation.** Rejected because it reproduces `constraints.md` §1.5's pattern: the prior reviewer caught the same classes of error session after session. Detection without prevention is a cleanup service.
- **R-1.2 — Substrate framed as queryable storage with referential integrity only.** Rejected because referential integrity catches `[D-7]` pointing at no row, but does not refuse a `body_md` column whose Markdown contradicts another `body_md` column. The refusal contract must extend to lifecycle states, supersession edges, write authority by role, and (per `[adv]` Divergence-3) potentially to body content shape itself.

**Open.** The exact list of refusals each candidate substrate-shape (S1/S2/S3 below in D-3) carries is open and is session 078's first design task.

---

## D-2 — Smallest agent set is four to five LLM agents plus deterministic gates

**What.** The brief's seven-role roster (reader, specifier, decider, deliberator, reviewer, validator, assembler) is rejected as proliferation. The design space carries forward two convergent reductions:

- **A-min (subtractor):** specifier, decider, deliberator-N, assembler. Reader and validator demoted to substrate APIs / deterministic gates. Reviewer deferred until empirical evidence shows the substrate cannot prevent what the prior reviewer caught.
- **A-mid (architect / codex consensus):** orchestrator, worker (collapses reader/specifier/assembler), deliberator-N, validator (deterministic), reviewer (audits structured constraints, not full-session prose).

Both candidates treat **reader, validator, and assembler** as not-LLM-agents — substrate APIs or deterministic tools. This is the load-bearing reduction.

**Why.** Convergence-2 across all five perspectives. Calling deterministic operations agents inherits the precedent-reflex of the prior engine and creates roles where capabilities suffice. `[arch]` argued explicitly that "splitting them by name produces role-confusion (`constraints.md` §Risks)." `[dev]` argued seven roles "are manageable if four are deterministic tools; seven chatty LLM agents are an operations problem disguised as methodology." `[sub]` argued the seven-roster reads as seven because the prior engine had things called those names — precedent-reflex.

**Rejected alternatives.**

- **R-2.1 — Adopt the brief's seven-role roster as designed.** Rejected because no perspective endorsed it; all five reduced.
- **R-2.2 — Adopt a one-or-two-agent minimum (orchestrator + worker only).** Rejected because it sacrifices the deliberator's multi-perspective pattern, which `constraints.md` §"What the methodology preserved" identifies as the most-validated foundation. Cutting below A-min abandons the foundation.
- **R-2.3 — Treat reader, validator, assembler as LLM agents.** Rejected per all five perspectives' reductions.

**Open (carried to 078).** Whether to adopt A-min or A-mid; whether the reviewer is deferred or kept; whether worker-as-collapsed-three-roles holds under real workload pressure or fragments back into per-task prompting.

---

## D-3 — Three substrate-shape candidates carried to session 078; commitment deferred

**What.** Session 078 inherits three live substrate-shape candidates. It must pick one or hybridise; this session does not commit:

- **S1 — Body-in-cells.** `decisions`, `specifications`, `perspectives`, `engine_feedback` etc. carry `body_md` columns. The substrate refuses on envelope (identifiers, references, lifecycle). This is the mainstream of `[arch] [dev] [gen]`.
- **S2 — Index-only database, body-in-files.** Database holds IDs, FKs, lifecycle states, supersession edges, content_hash; body content remains in Markdown files referenced by path+SHA-256. Adversary's first proposal.
- **S3 — Body as constrained tuples.** Decision bodies and other artefacts decomposed into structured fields, not free-text. Adversary's second proposal. Highest readability cost; strongest refusal surface.

**Why.** Divergence-3 in synthesis. S1 is the path of architectural least resistance and matches `[dev]`'s schema sketch directly. S2 is the adversary's prediction that S1 reproduces the prose-state failure as **prose-in-cells** within twenty sessions. S3 is the fully-structured alternative whose readability cost may itself be a failure mode.

Session 077 lacks the empirical evidence to choose. Session 078 must engage the choice as its first schema-level commitment.

**Rejected alternatives.**

- **R-3.1 — Commit to S1 in 077.** Rejected because the prose-in-cells risk is named explicitly by the adversary and acknowledged structurally by the cross-family generalist; resolving it requires a worked example or a prototype, neither of which 077 produced.
- **R-3.2 — Commit to S2 in 077.** Rejected because no concrete schema for the index-only shape was produced; the architect's and devops's schemas all assume body-in-cells.
- **R-3.3 — Commit to S3 in 077.** Rejected because no perspective produced a tuple-decomposition for decisions or specifications; the readability cost is undefined.

**Open (load-bearing for 078).** Resolve S1 vs S2 vs S3 (or hybrid) before any schema implementation. Required deliverable: a worked example showing the chosen shape produces the methodology's existing artefacts (a decision record with rejected alternatives, a specification with supersession edge, a deliberation synthesis with preserved dissent) without losing what makes them readable.

---

## D-4 — Three load-bearing minority positions are preserved as first-class for session 078

**What.** Three positions held by a single perspective (or two) against the others are preserved as first-class inputs to session 078, not collapsed into the synthesis. Session 078 must rebut, adopt, or hold open each:

- **D-4.a (adversary, partial subtractor + generalist) — The brief's diagnosis may be partial.** Two alternative readings of the seventy-five-session record fit the evidence: Reading B (accretion-without-subtraction; fix is subtraction + write-budget, not multi-agent decomposition) and Reading C (self-hosting itself is structurally trap-prone; only external pressure resolves). 078 must either rebut these readings concretely or design a successor whose architecture works under all three.
- **D-4.b (adversary + subtractor) — The subtraction role and the human reviewer are likely the same role.** Architect and both codex perspectives treat them as separate. 078 must pick. If the same role, the engine carries one human-review-with-subtraction-authority surface; if separate, two distinct mechanisms with potentially-conflicting cadences.
- **D-4.c (subtractor) — Engine-v16 itself should be cut by ~80–100 lines before adding anything.** Subtractor's specific cut targets: `methodology.md` §"When to review at close" (re-introduces only after prevention re-derived); `methodology.md` §"Validation senses" (provisional reference substitute archived); meta-disclaimers; `workspace.md` layout enumeration; `engine-manifest.md` loading recipe. Total ~250 lines remain. 078 must adopt or reject this cut explicitly; treating engine-v16 as the floor without engaging the cut is itself the failure mode the subtractor is calling out.

**Why.** `methodology.md` §"When to convene multiple agents" requires that the synthesis preserve dissent: "a minority position is recorded as a minority, not erased." These three positions are the substantive minorities of this deliberation. Treating them as raw material for collapse-into-consensus replicates the failure mode the deliberation pattern was designed to prevent.

**Rejected alternatives.**

- **R-4.1 — Synthesise the minorities into the convergent majority position.** Rejected because the synthesis explicitly is not a decision (per `methodology.md` §When to convene multiple agents) and the minorities each name a load-bearing risk that the majority did not engage.

**Open.** Each of D-4.a, D-4.b, D-4.c is a session-078 deliverable: explicit position with reasoning, or explicit deferral with what evidence would resolve.

---

## D-5 — Session 078 produces design commitments, not implementation; session 079 begins implementation

**What.** Session 076's close §"What session 077 should address" stated "Session 078 designs the solution against the design space and starts implementation." Session 077 amends this: session 078 produces the *design commitments* (substrate-shape pick from D-3, agent-set pick from D-2, refusal-contract specification per D-1, dispositions on D-4.a/b/c, schema-evolution protocol per Divergence-7), but **does not start implementation**. Implementation begins in session 079 against the explicit design commitments.

**Why.** The synthesis's open questions (Divergences 1, 2, 3, 4, 5, 6, 7) are too numerous and too foundational for one session to both resolve *and* implement against. The cross-family generalist's specific concern — "I would not commit to generated Markdown as the only human-facing record until tested" — applies equally to design commitments themselves: a single session that designs and implements has no slack to discover that an early commitment was wrong.

The brief's diagnosis (`constraints.md` §1.6) is that locally-reasonable additions consumed the bandwidth needed to see deficiencies. Bundling design and implementation in one session reproduces that pressure structurally. Splitting them creates the slack the engine's own diagnosis says it needs.

This is also the more honest acknowledgement of what the deliberation produced: a design space rich enough to need its own decision session before construction.

**Rejected alternatives.**

- **R-5.1 — Honour 076's close verbatim (078 designs *and* starts implementation).** Rejected because the synthesis surfaced more open questions than 076 anticipated. Pretending a single session can resolve seven divergences and write code is the pattern the brief identifies as having killed Selvedge.
- **R-5.2 — Add a 077.5 / 077-followup session before 078.** Rejected because the design-space surface is now stable; what's needed is decision against it, not more deliberation.

**Open.** Session 078's specific deliverables list (carried to 03-close.md handoff): pick from D-3 with worked example; pick from D-2 with the reviewer disposition; refusal-contract specification per D-1; explicit position on each of D-4.a, D-4.b, D-4.c; schema-evolution protocol; substrate technology commitment (SQLite vs alternative). Session 079's specific deliverables: working substrate (migrations 001), one orchestrator process, ID allocator, validator running pre-commit, and one round-trip session test (open → write a decision → close → reopen and verify refusal of mutation) before any agent role is built.

---

## Engine-version impact

**No bump.** No active engine-v16 file was modified by session 077. Session 077 produced provenance only.

The engine-v16 → engine-v17 bump is anticipated at session 078's close (substrate-shape commitment + agent-set commitment will likely require new active spec content) or session 079's close (working substrate is engine-definition).

## Open issues raised by this session

None added in 077. Three minority positions are recorded as `D-4.a/b/c` above and carry to 078; their disposition there determines whether they become open issues, resolved positions, or live design constraints.

## Engine-feedback raised by this session

None. The engine-v16 spec set executed adequately for a design-space-deliberation session. Two operational notes recorded as honest limits in the close (`03-close.md`), not as engine-feedback.
