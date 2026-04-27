---
session: 077
title: Design-space deliberation — synthesis
date: 2026-04-27
perspectives: 5
families: 2 (Anthropic ×3, OpenAI ×2)
sealed: true
---

# Synthesis

Five blind positions were written before any perspective saw another's. Three Anthropic (architect, adversary, subtractor), two OpenAI (cross-family generalist, cross-family devops). This synthesis names what converged, what diverged, and what dissent is preserved as first-class. It is *not* a decision; the decision record is `02-decisions.md`. Per `methodology.md` §When to convene multiple agents, "the synthesis of perspectives is not itself a decision; it feeds Decide. Synthesis preserves dissent."

For traceability, claims are tagged `[arch]`, `[adv]`, `[sub]`, `[gen]`, `[dev]`. A position with all five tags converged across the deliberation; a position with one tag is a minority preserved as such.

## What converged

### Convergence-1 — The substrate is a refusal contract, not a storage choice

All five perspectives explicitly frame the substrate as the *enforcement boundary* rather than as a place to put data. `[arch]` "the substrate refuses writes that violate identifier format, foreign-key resolution, lifecycle-state legality, or required-field presence." `[dev]` "The database is not a convenience layer. It is the enforcement boundary." `[gen]` "the central design question is what the system refuses to accept." `[sub]` "Friction at write time, not audit time" promoted to first-class. `[adv]` agrees in principle but warns the framing alone does not guarantee refusal (see Divergence-3).

The convergent claim: the brief's "database-backed substrate" prescription should be operationalised as *what writes the substrate refuses*, not as schema-as-warehouse. This is a sharper formulation than the brief itself carries.

### Convergence-2 — The brief's seven-role roster is too many

All five perspectives reduce the agent count, with overlapping reasoning. The brief lists seven (reader, specifier, decider, deliberator, reviewer, validator, assembler). The perspectives' reductions:

- `[arch]` Five: orchestrator, worker (reader+specifier+assembler collapsed), deliberator-N, validator (deterministic, not LLM), reviewer.
- `[sub]` Four LLM roles: specifier, decider, deliberator-N, assembler. Reader/validator demoted to substrate APIs/gates. Reviewer deferred until substrate proves insufficient.
- `[gen]` Five LLM roles: deliberator perspectives, specifier, decider, reviewer, subtractor. Validator/assembler/reader deterministic.
- `[dev]` Mixed: deterministic tools (reader, validator, assembler, ID allocator, migrator); LLM agents (deliberators, specifier, reviewer, subtractor, sometimes decider); orchestrator one process.

Common reduction: **reader, validator, and assembler are not LLM agents.** They are deterministic tools or substrate APIs. Calling them agents inherits the precedent-reflex of the prior engine.

Common dissent point inside this convergence: whether to keep or defer the **reviewer**. `[sub]` defers. `[arch] [gen] [dev]` keep, but with sharper scope (audit structured constraints, not full session prose; read less, see sharper exceptions per `[dev]`).

### Convergence-3 — Coordination through the substrate, no agent-to-agent messaging

`[arch]` "Agents do not message each other directly. There is no shared scratch." `[dev]` "Agents do not message each other directly. A work item is UTF-8 JSON, capped at 32 KiB, containing object IDs and requested output shape, not copied workspace context." `[gen]` "no agent-to-agent handoff counts as state until written to the store." `[sub]` ratifies. `[adv]` warns this can be undermined by prose-in-cells (see Divergence-3).

The convergent operationalisation: every agent invocation receives a typed task envelope; emits a typed write; the substrate either accepts or refuses; the orchestrator schedules the next task from substrate state, not from in-memory continuation.

### Convergence-4 — The subtraction role must have structural authority to delete, not advisory authority

All five name this. `[arch]` rule-bound automaton with delete authority over specifications, commitments, engine_feedback rows; `[sub]` retention-test: a clause is retained only if a concrete failure occurred under its absence within the last 10 sessions; `[gen]` "veto-bearing maintenance role"; `[dev]` "Its authority is not advisory; it can propose removal decisions that the normal decision mechanism must accept, reject, or defer with reasons"; `[adv]` agrees the authority is necessary but doubts an LLM can wield it (see Divergence-2).

### Convergence-5 — Closed sessions are immutable; correction is by new rows in later sessions

`[arch]` perspectives row added to a closed deliberation is refused. `[dev]` triggers reject updates to decisions, refs, spec_versions, read_log, reviews where owning session is `closed`. `[gen]` does not specify but does not contradict. Consistent with `methodology.md` §Preservation. No dissent.

### Convergence-6 — Identifiers are substrate-allocated, not agent-typed

`[dev]` most concrete: agents call CLI for next ID, do not type IDs into prose. `[arch]` decision_id PK substrate-allocated, local_ord renders the in-session `D-N`. `[gen]` consistent. `[sub]` consistent. `[adv]` consistent.

This addresses `constraints.md` §1's "identifiers drifted" failure structurally.

### Convergence-7 — Markdown for design intent, database for envelope

The boundary all five accept: specifications and reasoning live in Markdown; identifiers, references, lifecycle, counters live in the database. Generated session artefacts (close files, dossiers) are *views over rows*, not authored prose. `[arch]` `assemble` step is `sqlite3 plus a template`. `[dev]` `state/exports/` is generated, never source of truth. `[gen]` "generated views can satisfy [preservation] only if humans can still read and trust them" — caveat preserved at Divergence-3.

## What diverged

### Divergence-1 — Whether the diagnosis itself is right (adversary's foundational challenge)

Only `[adv]` argues the brief's diagnosis is partial. Two alternative readings preserved:

- **Reading B (accretion-without-subtraction):** The methodology kept *adding* (engine-feedback pathway, retrieval substrate, close-time reviewer, layered audits) without subtracting. The failure was no one was responsible for removal, not single-agent overload. If true, the fix is the subtraction role plus a hard write-budget; the multi-agent decomposition is incidental at best, harmful at worst.

- **Reading C (self-hosting as the disease):** Self-hosting itself is structurally recursive-trap-prone. Applying multi-agent decomposition to the methodology that produced the multi-agent decomposition triggers the same trap one level up. If true, no architectural fix is sufficient; only external pressure (running on a real problem) is.

`[sub]` partially aligns with Reading B (cuts "external pressure as a design surface" because the engine cannot enforce externality). `[gen]` partially aligns with Reading C (proposes external-problem trial as release gate). `[arch] [dev]` do not engage with either reading.

**Preserved as first-class minority:** the diagnosis the brief commits to may be one of several readings of the seventy-five-session record, and session 078's design must either rebut Readings B and C or hold the design space open for them.

### Divergence-2 — Whether the subtraction role and the human reviewer are the same role

`[adv]` "Real subtraction is the operator's. The deliberately-built human review role and the subtraction role are likely the same role, and pretending they are two roles dilutes both." `[sub]` second-most-likely miss: "the subtraction role and the human-review role solve the same problem (external pressure the system cannot generate from inside). Defining them as two roles double-counts."

`[arch]` explicitly separates: subtractor is a rule-following automaton; human is the exogenous unrestricted-authority catch.
`[gen]` separates: subtractor is veto-bearing maintenance; human review is reframing-authority.
`[dev]` separates: subtractor has its own derived-weight reports and removal decision path; human reviewer has its own dashboard surface.

**Preserved as live disagreement.** Anthropic adversary + subtractor argue collapse; architect + both codex perspectives argue separation. The synthesis does not resolve this; session 078 must.

### Divergence-3 — Whether body content lives in database cells or in files

This is the most consequential schema-level divergence and the adversary's sharpest point.

`[arch] [dev] [gen]` propose schemas with `body_md` columns on `decisions`, `specifications`, `perspectives`, `engine_feedback`, etc. The Markdown body lives *in the database row*.

`[adv]` predicts this reproduces the prose-state failure as **prose-in-cells**: queries return tables of identifiers whose `body_md` columns contradict each other, and no validator can detect this without reading prose, and no model under load reads prose carefully (Property 4). Adversary proposes two alternative paths: (a) a much narrower database — IDs, FKs, lifecycle states, supersession edges, no body content — with all body content in Markdown files indexed by the database; or (b) decisions as constrained tuples, not paragraphs, at the cost of readability.

`[sub]` does not specify column-level shape. `[gen]` notes the risk explicitly: "I expect some perspectives will treat 'database' as storage rather than refusal."

**Preserved as a load-bearing open question.** Three live candidate substrate-shapes:

- **S1 (mainstream of this deliberation):** body content in cells, validator enforces *envelope* (identifiers, references, lifecycle), prose bodies remain free-text.
- **S2 (adversary-narrow):** database is index-only; bodies live in Markdown files; substrate refers to files by path+SHA-256.
- **S3 (adversary-tuple):** decisions and other artefacts are constrained tuples not free-text; readability cost accepted.

Session 078 must pick or hybridise; this synthesis records all three.

### Divergence-4 — Whether even more should be cut from engine-v16 itself before adding anything

Only `[sub]` argues this concretely: cut ~80–100 lines from active engine-v16 specs before designing additions. Specifically: the close-time reviewer section in `methodology.md`, the provisional-reference-substitute validation sense, meta-disclaimers, the layout enumeration in `workspace.md`, the loading recipe in `engine-manifest.md`.

`[arch]` does not argue for further cuts; treats engine-v16 as the floor. `[adv]` argues the brief's prescriptions themselves are over-prescribed but does not target engine-v16 directly. `[gen]` warns "preservation, self-hosting, dissent as first-class" may be treated as intrinsically virtuous when they are costly mechanisms — partial alignment with `[sub]`. `[dev]` does not engage.

**Preserved as a minority subtraction proposal** to be evaluated by session 078 alongside the additions. The subtractor's argument is that adding-before-subtracting *is* the prior engine's failure mode. The architect's counter-argument is that engine-v16 is already the trim and re-cutting risks instability for 077 itself.

### Divergence-5 — External pressure as an engine-enforceable property

`[gen]` proposes external-problem trial as a release gate: "every candidate architecture must name the smallest external-problem trial that could falsify it." `[adv]` argues self-hosting may be the disease and external pressure is the only fix.

`[sub]` argues the engine *cannot* enforce that it be applied externally; this is a methodology-validity precondition, not an engine design feature. Cuts from active design surface.

`[arch] [dev]` do not engage.

**Preserved as a methodology-level open question** for the operator and session 078: is "the engine refuses a self-development session if N consecutive priors were self-development" (the weak-form lever `[sub]` mentions and is uncertain about) actually a useful structural commitment, or does it manufacture compliance theatre?

### Divergence-6 — Substrate technology specificity

`[dev]` argues SQLite-first with a clear Postgres promotion path; concrete schema. `[arch]` agrees on "single-file, transactional, recoverable" but flags SQLite specifically as low-confidence. `[gen]` "local relational database" preferred but technology not committed. `[sub] [adv]` do not specify.

**Convergent direction (single-file relational, transactional)** with **preserved low-confidence on SQLite specifically**. Session 078 should treat SQLite as the working hypothesis but the question of distributed/concurrent agents (e.g., remote codex calls writing concurrently with local Claude) requires concrete answer before commit.

### Divergence-7 — Schema evolution

Only `[arch]` calls out that the schema will be wrong somewhere within twenty sessions and the friction-at-write-time substrate must itself be evolvable without breaking historical rows. `[dev]` provides `state/migrations/NNN-name.sql` schema history but does not engage the *deliberation* aspect of schema change. `[gen] [sub] [adv]` do not engage.

**Preserved as an open question for session 078:** what is the schema-change protocol, and is schema change itself a session activity or a separate kind of work? `constraints.md` §"Risks the successor must hold" warns about "schema-evolution overhead and the possibility of state-substrate-substrate-protection ceremony reincarnated in a different form" — engaging this is required, not optional.

## Cross-family observations

The cross-family voices' specific contributions, distinguished from the converged claims:

`[gen]` Two framings the deliberation may share that a fresh reader does not grant:

1. The Claude-perspectives may treat *preservation*, *self-hosting*, and *dissent-as-first-class* as intrinsically virtuous rather than as costly mechanisms that must keep earning their place. Engine-v16 already concedes this in `constraints.md` §"What the methodology preserved" but the preserved-by-default disposition can creep back. Recommendation preserved: preserve less by default; preserve more only where retrieval, replay, or accountability require it.

2. *Refusal-boundary under-specification*: many designs say "use a database" but leave the agent free to narrate around failed writes. The architect's position partially addresses this; `[gen]` argues the design space should require *every* candidate architecture to specify what writes the substrate refuses, as a deliverable.

`[dev]` The engineering specificity the other perspectives missed:

1. **Object registry across artefact kinds** for generic reference-checking without polymorphic foreign-key gaps. The architect's `references` table partially anticipates this; `[dev]` makes it a first-class table.
2. **Work-item leases and recovery semantics** for orchestrator crashes mid-session — none of the Anthropic perspectives engaged this.
3. **Concrete identifier formats** (`S%03d`, `D-S%03d-%03d`, `DEL-S%03d-%03d`, `WI-S%03d-%05d`).
4. **Triggers as the refusal mechanism** rather than application-layer checks: `SQLite triggers should reject updates to decisions/refs/spec_versions where owning session is closed.`

These are session-078 concrete-engineering inputs, not session-077 claims for adjudication.

## What this synthesis is not

This synthesis does not pick the winning architecture. The architect's A1 (five agents, body-in-cells, single-file relational), the subtractor's four-role minimum, the cross-family-devops's schema, the cross-family-generalist's smaller-typed-substrate, and the adversary's three contested readings are *all preserved as candidates in the design space*. Session 078 picks; this synthesis hands over the surface.

It also does not commit to: any of S1/S2/S3 substrate-shape; the role-collapse direction (Divergence-2); the further-cut direction (Divergence-4); the external-pressure-as-engine-feature direction (Divergence-5); the SQLite-specifically direction (Divergence-6); the schema-evolution protocol (Divergence-7).

## What carries forward to `02-decisions.md`

The decision record will commit to: the *shape* of the design space (the candidates above), the *open questions* session 078 must resolve (the divergences above), and the directions *rejected* with reasons (where reasoning warrants it). This synthesis is the input.
