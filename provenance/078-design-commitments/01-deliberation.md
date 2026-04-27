---
session: 078
title: Design-commitments deliberation — synthesis
date: 2026-04-27
perspectives: 5
families: 2 (Anthropic ×3, OpenAI ×2)
sealed: true
---

# Synthesis

Five blind positions were written before any perspective saw another's. Three Anthropic (substrate-architect, agents-architect, adversary), two OpenAI (cross-family engineer, cross-family methodologist). This synthesis names what converged, what diverged, what dissent is preserved as first-class. It is not a decision; the decision record is `02-decisions.md`. Per `methodology.md` §When to convene multiple agents, "the synthesis of perspectives is not itself a decision; it feeds Decide. Synthesis preserves dissent."

For traceability, claims are tagged `[arch]` (substrate-architect), `[agt]` (agents-architect), `[adv]` (adversary), `[eng]` (codex-engineer), `[meth]` (codex-methodologist). A position with multiple tags converged; a position with one tag is a minority preserved as such.

## What converged

### C-1 — Refusal contract is operationalisable; first cut enumerated

All five perspectives carry forward 077-D-1's framing of the substrate as refusal contract. Three perspectives produced concrete enumerations:

- `[arch]` enumerated **T-1 through T-17** with each refusal mapped to a `constraints.md` failure property and each implementable as SQL trigger or CHECK constraint.
- `[adv]` enumerated **T1–T8** as a tighter first cut tied to a write-budget (≤30 refusals total at first cut).
- `[eng]` enumerated a "minimum refusals" list with overlapping coverage: foreign keys, lifecycle transitions, supersession edges, ordinal uniqueness, lease expiry, schema staleness, close-blocking validations.

The three lists overlap on: identifier-resolution (T-1/T1), sealed-perspective protection (T-5/T8), closed-session immutability (T-6/T4), supersession-without-acknowledgement (T-7/T3), required-rejected-alternatives. The convergent claim: enumeration is feasible at session-078 specificity, and 079 can implement triggers from these lists directly.

### C-2 — SQLite, single-writer, local-only for engine-v17

`[arch]`, `[eng]`, and `[agt]` (implicit via reference to `[arch]`'s schema) commit to **SQLite 3** with WAL, foreign_keys=ON, STRICT tables. `[eng]` adds the sharpest framing: "the real concurrency decision is not 'which database tolerates many writers'; it is 'where is the single serialization point for Selvedge state?'" `[arch]` agrees ("agents run sequentially through the orchestrator's work-item queue, so there is exactly one writer at a time"). `[meth]` does not specify technology but is compatible with the choice.

The convergent commitment: **remote agents are compute, not database writers**. A remote codex/Claude call returns an output envelope; the local `selvedge submit` command performs the write. No agent process opens the SQLite file over a sync surface. If the engine later requires multi-machine direct writers, that is a new substrate decision.

`[eng]` further specifies the falsification trial: 16 parallel `selvedge submit decision` processes against one active session, with injected sleep and one killed mid-transaction, expected to produce contiguous local ordinals, no partial rows, recoverable work items, and `PRAGMA integrity_check` clean. This is the smallest concurrency-trial 079 can run.

### C-3 — D-4.b: adopt the collapse (subtractor = human)

Four-of-five perspectives that engaged D-4.b adopt the collapse:

- `[adv]` reaffirms 077-adversary's collapse argument and extends: "an LLM 'subtractor' will produce subtraction-ceremony; the operator is already the subtraction substrate; session 076's restart was a subtraction event no agent could perform."
- `[agt]` "adopt collapse" — one human reviewer-with-subtraction-authority, scheduled cadence, three write authorities (reframe, subtract, spec-revision).
- `[meth]` aligns: "the operator-as-diagnostic-substrate pattern wasn't accidental — it was the structural feature." Cadence-overdue-refusal makes the cadence real.
- `[arch]` substrate-shape-neutral but admits both shapes; notes the role-write-capabilities table (T-14) admits either model.

`[eng]` does not engage D-4.b directly.

What survives of `[077-arch]`'s rule-bound LLM subtractor: the **eligibility report** as a deterministic CLI (`selvedge subtract-eligibility`) that the human reads and acts on. The rules are codified; the judgment is human. `[agt]` made this concrete; `[adv]` and `[meth]` agree.

The convergent claim: **one human reviewer-with-subtraction-authority role, scheduled cadence, deterministic eligibility report, substrate-enforced cadence (refuses session open if review overdue).**

### C-4 — D-4.c: adopt the cut

Three-of-five explicitly adopt D-4.c (cut engine-v16 by ~80–100 lines before adding):

- `[adv]` "must be adopted, not held open. Cut engine-v16 by ~80 lines in this session before 079 adds substrate. If 078 cannot subtract from a 350-line spec set with no users, the engine cannot subtract from a 3000-line spec set with sessions depending on it."
- `[meth]` "adopt with a pre-implementation cut" — specific targets: `methodology.md` §When to review at close, §Validation senses (provisional reference substitute), meta-disclaimers, `workspace.md` layout tree, `engine-manifest.md` loading recipe.
- `[arch]` "leans toward `[077-sub]`'s cuts but defers to subtractor-perspective on which."

`[agt]` and `[eng]` do not engage D-4.c.

The convergent claim: **078 commits to a concrete cut list; 079 applies the cut as its first action before substrate code.** `[meth]`'s specific cut targets become the working list.

### C-5 — Reading C (self-hosting): hold open with a release gate

`[adv]` and `[meth]` both adopt a release gate; the gate is the strongest convergent commitment on D-4.a's Reading C:

- `[adv]` "engine-v17 is provisional until it has run on a non-self problem for 30 sessions. No self-development sessions modify engine-v17 between 079 and that gate, only fixes the external application demands."
- `[meth]` "engine-v17 is provisional until it has run a bounded external-problem trial. The enforceable rule is a release gate: no further methodology-expanding self-development after the first agent-on-substrate run unless an external-problem trial has been opened, run, and closed with a domain or operator report."

Both perspectives explicitly **reject** a hard substrate refusal ("no self-development after N sessions") as compliance theatre; the gate is operator-enforced, not schema-enforced. The convergent claim: **engine-v17 carries a release-gate annotation; the operator is the enforcer; the engine records workspace mode but does not pretend to verify externality structurally.**

### C-6 — Schema evolution: additive by default; contract changes are foundation-touching

`[arch]` and `[eng]` agree on the protocol shape:

- Additive migrations (new column, new table, new index, stricter trigger applying only to future rows) are normal session work, decided by the current session, with `column_introduced_session` (`[arch]`) or `created_schema_version` (`[eng]`) metadata so refusals do not fire on legacy rows.
- Contract changes (drop column, drop table, change refusal semantics, rewrite identity, move body-storage shape) require multi-perspective deliberation with at least one cross-family voice — i.e., they are foundation-touching per `methodology.md`.
- Schema migrations are themselves session-shaped: `decisions` row of `kind='schema-migration'` (`[arch]`) or `kind='schema_change'` (`[eng]`), tied to a `state/migrations/NNN-<slug>.sql` file, with `schema_migrations` registry rows.
- Rollback is two-tier: pre-close failure → SQLite transaction rollback plus pre-migration `.backup`; post-close failure → forward-only corrective migration.

`[arch]`'s T-17 ("no destructive migrations; ADD-only") is the structural sharpening of `[eng]`'s additive-vs-contract split. Convergent claim: **migration 001 establishes the schema-evolution protocol; the additive-vs-contract split is the protocol; rollback is two-tier.**

### C-7 — Sharper Markdown boundary: argument vs obligations

`[meth]` sharpened 077-Convergence-7:

> Markdown may carry argument, but not obligations. A decision's prose can explain why; the existence of the decision, its status, rejected alternatives, references, supersession edges, open follow-ups, and close eligibility must be structured. A specification body can remain Markdown; its canonical version, active/superseded status, content hash, and supersession edge cannot.

`[arch]`'s S1+ design implements this exactly: rejected_alternatives are S3-style tuples (one row per alternative with structured rejection_reason_md); supersession is a typed `refs` row; status is a column; bodies remain Markdown. `[adv]`'s S2-narrow and `[eng]`'s S1-with-satellites are also consistent with this boundary.

Convergent claim: **the Markdown-vs-database boundary is argument vs obligations, not prose vs structured-data per se. Generated Markdown exports render rows; they cannot author state claims.**

### C-8 — Deliberator blindness substrate-enforced via `sealed_until`

`[arch]` and `[agt]` both make 077-`03-close.md` honest-limit-5 (blind discipline procedurally enforced) structurally enforced going forward:

- `[arch]`'s T-5 and T-15: refuse `perspectives` insert after `deliberation.sealed_at IS NOT NULL`; refuse UPDATE on `sealed_at = NULL`.
- `[agt]`: substrate refuses a `perspectives` write whose `created_at` is after `sealed_until`; "078 commits this to the schema."

Convergent claim: **`deliberations.sealed_until` is a load-bearing column in migration 001; T-5 and T-15 close 077's procedural-only-blind-discipline gap.**

### C-9 — Object registry and substrate-allocated IDs

All five perspectives reach this convergence (extending 077's Convergence-6):

- `[arch]` `objects(object_id, object_type, lifecycle_state, created_session_id)` registry across artefact-kinds; IDs allocated inside the same transaction.
- `[agt]` agents/humans request IDs; do not invent in prose; the orchestrator's work-item envelope contains object IDs.
- `[adv]` T1 covers identifier-format violations.
- `[eng]` "IDs are allocated inside the same transaction as the object insertion. There is no 'next ID' call that hands an agent a value to remember." Display IDs are derived from committed rows.
- `[meth]` "Add a deterministic ID allocator. Agents and humans should request IDs; they should not invent them in prose."

Convergent claim: **IDs are substrate-allocated in-transaction; never agent-typed; display ordinals are derived.**

### C-10 — Reading B (accretion-without-subtraction): adopt or partial-adopt

`[adv]` and `[meth]` adopt Reading B — `[adv]` fully ("Reading B: adopt"), `[meth]` as "an omitted causal layer" rather than a competing diagnosis. Neither rejects Reading A (single-agent overload); both see the readings as compounding.

`[adv]`'s consequences for 078: subtraction becomes load-bearing centerpiece; D-4.c adoption is not optional; hard write-budgets in this session (≤400 active spec lines, ≤12 tables, ≤30 refusals at first cut).

`[arch]`, `[agt]`, `[eng]` do not engage Reading B explicitly. Convergent claim: **Reading B carries; the multi-agent + database direction addresses Reading A; Reading B's fix (subtraction + write budget) is operationalised through C-3, C-4, and (per `[adv]`) write-budget commitments 078 must address.**

## What diverged

### Div-1 — Substrate-shape (Divergence-3 from 077): S1-with-satellites vs S2-narrow

The headline divergence. Three positions:

- **S1+ / S1-with-typed-satellites (`[arch]`, `[eng]`, `[agt]`-implicit).** Body-in-cells default for decisions, engine_feedback. Structured tables for rejected_alternatives (S3-style tuples), supersession edges (typed `refs` rows), commitments (capped summary_md). `[arch]` additionally puts spec and perspective bodies as files-with-SHA (S2-style for those specific artefact-kinds). `[eng]` argues against any S2 file-shape on grounds of two-phase consistency.
- **S2-narrow (`[adv]`).** No `body_md` column on any table. Every prose-bearing row carries `body_path` + `body_sha256`. ~12 tables, T1–T8 first-cut refusals. Argues S1 is unrefutable on prose-in-cells; S2 honestly admits the substrate is an *index* over the methodology, not a *store*.
- **Substrate-shape-neutral (`[meth]`).** "Independent of S1 vs S2 at the engineering layer" so long as the Markdown boundary (C-7) is sharp. Notes the prose-in-cells objection remains live; if 080 finds agents citing body text as checked state, move toward S2 or S3.

The internal disagreement within the S1-coalition: `[arch]` puts spec and perspective bodies in files (S2-style) for stated reasons (large bodies, sealed-discipline via hash, file-diff valued in git history). `[eng]` rejects this as introducing two-phase consistency. The disagreement is not paper-vs-paper but engineering-judgment-on-atomicity: file+row atomicity requires a transactional bridge `[eng]` does not trust the engine to build correctly.

**Preserved as live disagreement.** Three live positions:

- S1-with-satellites: bodies in cells; structured satellites for envelope; refuse via SQL triggers only (`[eng]`).
- S1+: like above plus file-shape for specs and perspectives specifically (`[arch]`).
- S2-narrow: no body_md columns; everything index-only (`[adv]`).

Session 078's commitment record must pick one of these three or hybridise with a stated rule for each artefact-kind. The synthesis does not pick.

### Div-2 — Reviewer disposition

Three positions:

- **Kept narrower-scope with removal trigger (`[arch]`, `[agt]`).** `[agt]` made it concrete: three structured queries (refused-write history, reference-warning history, trajectory metrics); 16 KiB context budget; cadence every 5th session; **10-session removal trigger**: if 10 consecutive runs produce zero engine_feedback rows that result in refusal-tightening, the role is cut.
- **Remove now; return narrower (`[meth]`).** "Remove `methodology.md` §When to review at close as an active mechanism. Re-introduce review only when it reads substrate exceptions and generated diffs, not the whole session record."
- **Subsume into human (`[adv]`, partial).** No LLM reviewer; the human-reviewer-subtractor handles audit. `[adv]` does not explicitly forbid an LLM reviewer but treats the human role as the structural answer to P6 (cannot perceive own deficiencies while executing).

`[eng]` does not engage.

The decision record must commit to one of: keep-narrow-with-trigger, remove-and-return-narrower, or subsume-into-human. The three positions overlap on the *shape* the reviewer (if kept) should take — substrate-query-only, no full session prose — and diverge on the *timing* of the cut and on whether an LLM reviewer is needed at all.

### Div-3 — Assembler: deterministic-only vs probationary-LLM-narrative

Two positions:

- **Deterministic only (`[arch]`, `[eng]`, `[meth]`).** Close artefacts are templated; "assembly is a query over the substrate" (`[arch]`); "assembler is `sqlite3` plus a template" (077-`[arch]` cited).
- **Probationary LLM narrative (`[agt]`).** Bulk is templated; one narrative paragraph ("what was done; what state the workspace is in; what the next session should address") is LLM-authored with 16 KiB context budget. **5-session removal trigger**: if 5 consecutive next-session assessments do not cite the prior narrative, the role is cut.

`[adv]` does not engage but is consistent with the deterministic position.

This is a smaller divergence than Div-1 or Div-2 because `[agt]`'s position carries its own removal trigger. Decision-record-level options: (a) deterministic-only, no LLM assembler; (b) probationary-LLM-narrative with `[agt]`'s 5-session trigger.

### Div-4 — Hard write-budgets in 078

Only `[adv]` proposes hard numbers in this session: ≤400 active engine-spec lines until external trial completes; ≤12 tables in migration 001; ≤30 refusals at first cut. The numbers are explicitly marked "deliberately wrong-in-detail; their function is to force the removal conversation."

`[arch]`'s T-1 through T-17 are 17 refusals (under `[adv]`'s 30 cap). `[eng]`'s minimum-refusal list is shorter. `[arch]`'s schema sketch is ~16 tables (over `[adv]`'s 12 cap). Active engine-spec is currently ~350 lines, well under `[adv]`'s 400 cap; the cut from D-4.c would bring it lower.

`[meth]` "would not commit to the exact cut size" — directionally agrees with budgets but does not propose numbers.

`[arch]`, `[agt]`, `[eng]` do not propose budgets.

**Preserved as a load-bearing minority proposal.** The decision record must commit to: (a) adopt budgets at `[adv]`'s numbers; (b) adopt budgets at different numbers; (c) reject budgets in favour of qualitative subtraction discipline; (d) defer budgets to operator-direction at human-review cadence.

### Div-5 — Whether 078 itself reproduces the failure mode

Only `[adv]` raises this as the meta-question:

> Does 078, weighed as a session, subtract more than it adds? If not, the diagnostic capacity the engine is supposed to restore is already absent in the session that designs the restoration. 078's deliverable list is seven items… If 078 ends up with a refusal contract enumerated to thirty rules, an agent set with five LLM roles, a schema with twelve tables, a worked example showing all artefact kinds, and the D-4.c disposition is "deferred," then 078 has performed the pre-restart Selvedge pattern in a single session.

`[arch]`, `[agt]`, `[eng]`, `[meth]` do not engage this framing directly. `[meth]` partially aligns ("prevent the design commitments from becoming a new layer of plausible ceremony") without applying the test self-referentially to 078.

**Preserved as a first-class minority diagnostic.** The decision record should explicitly run `[adv]`'s test against itself: line up what 078 adds (substrate-shape commitment, agent-set commitment, refusal contract, schema-evolution protocol, substrate technology commitment, three D-4 dispositions, 079 handoff) against what 078 subtracts (the D-4.c cut list; the explicit deletion of any active-engine content the commitments make redundant). If the subtraction column is shorter than the addition column, the dissent is recorded as a structural finding.

## Cross-family observations

The cross-family voices contributed three sharpenings the Anthropic perspectives did not produce:

- `[eng]`: **single serialization point** as the framing for concurrency, displacing "which database tolerates many writers." Remote agents are compute; local CLI writes. Displacement avoids premature distributed-database commitments.
- `[eng]`: **two-phase consistency cost of S2** as engineering critique of the substrate-architect's file-shape choice for specs and perspectives. The Anthropic substrate-architect treated file-storage as a feature; the cross-family engineer treats it as an atomicity hazard. The synthesis does not resolve this; it surfaces it as Div-1's internal disagreement.
- `[meth]`: **release gate as the honest commitment** that the engine cannot enforce externality from inside; the operator is the enforcer; engine-v17 is provisional until external trial. This sharpens 077-Divergence-5 (`[077-sub]` cut external-pressure as engine-feature; `[077-gen]` proposed external trial as release gate) into a concrete commitment shape.

These are session-078 commitment inputs, not session-077-style design-space candidates.

## What this synthesis is not

This synthesis does not pick the substrate-shape, the reviewer disposition, or the assembler shape. It does not adopt or reject `[adv]`'s write-budgets. It does not run `[adv]`'s "does 078 subtract more than it adds?" test on 078 itself. The decision record runs all four.

This synthesis does not commit to: a specific cut from D-4.c (`[meth]`'s cut list is the working list, not a binding choice); the exact numeric write-budgets if any are adopted; the operator-cadence default for human review (5th / 10th sessions are guesses per `[agt]`); the specific three queries the reviewer audits (`[agt]`'s three are placeholders); the specific 12 / 16 tables in migration 001.

## What carries forward to `02-decisions.md`

The decision record will commit to: (a) the substrate-shape from Div-1; (b) the agent-set commitment with reviewer disposition from C-3 + Div-2 + Div-3; (c) the refusal-contract enumeration as the union of the three perspective enumerations, with explicit additions and removals; (d) D-4.a Reading B disposition (adopt; consequences); (e) D-4.a Reading C disposition (hold open with release gate per C-5); (f) D-4.b disposition (adopt collapse per C-3); (g) D-4.c disposition (adopt cut per C-4) with the specific cut list from `[meth]`; (h) schema-evolution protocol per C-6; (i) substrate technology commitment per C-2; (j) write-budget disposition per Div-4; (k) the 078-self-test per Div-5; (l) the 079 handoff at the level of `[meth]`'s vertical-slice criteria.

This synthesis is the input. The decisions follow.
