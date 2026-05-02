# Shared brief — S180 seal-grade typed-graduation

> The following sections are **byte-identical** across all perspectives. Only the role-specific `STANCE` section at the end of each per-perspective brief differs.

## Methodology context

You are one of 4 perspectives convened in **S180 of the Selvedge self-development workspace** (`/Users/ericmccowan/Development/complex-systems-engine`). Selvedge is a methodology-and-substrate engine — perspectives reason together, durable artefacts are produced, reasoning is preserved as substrate rows in `state/selvedge.sqlite`, the engine evolves by running its own mechanic on its own outputs.

The substrate is the only writable surface for session state. Markdown in `provenance/` is a generated export from substrate rows. Every session phase is `bin/selvedge submit <kind>`. Atoms are 8–240 chars, no newlines, no fenced code, no pipe tables.

The current engine version is **engine-v49**. Migrations 001..039 are applied. Read these clauses for full context:
- `prompts/development.md` §4 *Seal-time deliberation-grading* (the clause under deliberation here).
- `prompts/development.md` §5 (decision-record + cite typing + T-32 precedent-sensitive provenance check + "authority and the prose-clauses-without-instrumentation lesson").
- `prompts/development.md` §8.5 *Close-time interpretive-choice audit* (the sibling clause; same prefix-row pattern).
- `specifications/methodology.md` §Synthesis (carries the seal-grade pointer at line 101).
- `provenance/159-oi-s154-5-deliberation-grading-seal-time/` (the originating deliberation D-23 and decision DV-S159-1).

## Problem statement

The operator named the failure mode and demanded the design adhere to constraints **without compromise**. The diagnosis was: seal-grade rows currently live in `engine_feedback` as a prefix-prose row (`seal-grade:` headline + body enumerating counterfactuals + disposition). Held against the six failure modes the kernel defends against (preserved in `bin/selvedge orient`'s "Why this engine exists" packet from the retired `constraints.md` v1):

1. **Loses foundational instructions under context pressure.** Under context pressure, seal-grade rows collapse into the homogeneous "untriaged engine_feedback" backlog; the mandated-synthesis-artefact distinction lives in a sentence in `prompts/development.md`, not in substrate.
2. **Anchors on most-recent-prior-decision over foundational specification.** DV-S159-1 anchored on DV-S155-1's audit-step pattern (recent prior) rather than asking whether the kernel needed a typed counterfactual primitive. Cross-family P-1+P-2 convergence on engine_feedback reuse is still recent-precedent imitation.
3. **Confuses authority of speakers.** `engine_feedback` is the catch-all observation surface — operator friction, agent observations, calibration, audit-step, codex-shape-consult, AND mandated synthesis-quality artefacts all under `flag='observation'`. The triage workflow cannot distinguish "operator noticed friction" from "synthesizer enumerated counterfactuals as required by §4."
4. **Generates narrative-fitting numbers when substrate values exist.** The `seal-grade: <count>` count lives in prose. EF-S179-1 says "4 single-frame counterfactuals" — there is no substrate row to verify against.
5. **Defaults to mechanism-addition over mechanism-subtraction.** This cuts *for* the current engine_feedback choice (no new table). DV-S109-1 ceremony-subtraction explicitly favoured the existing surface.
6. **Drifts into ceremony when each addition does not pay for itself.** Empirical: 8 seal-grade rows authored since DV-S159-1 shipped (S159, S161, S171, S173, S176, S179 plus closure-of-record rows); 7 disposed, mostly via reflexive `procedural-self-dispose per DV-S171-1 §1.5` (no substantive triage). 1 currently untriaged (EF-S179-1). The promotion-trigger in `prompts/development.md:120` requires *both* a seal-without-row AND a downstream calibration-EF naming a missed counterfactual — that trigger has not fired.

The substrate-shape parallel: §5 cite-typing and T-34 just refused NULL `cited_object_id` for cite-required bases (engine-v49). Seal-grade rows have no FK from the row to the deliberation being graded — only prose substring or surfacing-context. That is the same NULL-FK shape T-34/T-35 hardened against.

The deliberation explicitly flagged in advance (`provenance/159-oi-s154-5-deliberation-grading-seal-time/01-deliberation.md:52`): "the structured-headline convention is now load-bearing across three clauses (temporal-claim, audit-step, seal-grade); a fourth or fifth pushes substring-matching analytics past viability and forces typed graduation."

The operator-named-mandate at S180-open is the §1.5 admissibility basis: the user explicitly invoked the constraints section against the current home and asked for a design **without compromise**.

## Design questions

You are asked to author a position covering each of the following:

**Q1 (graduate or subtract).** Should this clause graduate to a typed substrate primitive (new table, FK to deliberation, T-NN gate), graduate to an enum extension on `synthesis_points` (re-use existing primitive with new `kind` value), or be subtracted entirely (revisit M-1 from D-23: P-3's ship-nothing position, trust `divergence`/`minority` synthesis_points + methodology §Reopen-on-new-reading)? Take a position.

**Q2 (substrate shape, if graduating).** Concretely propose: which table, which columns, which CHECK constraints, which triggers, which submit kind, which T-NN refusal. Address the FK-to-deliberation requirement and the disposition enum (`addressed-in-synthesis | deferred-to-FR | nilled-by-exclusion`). Address how the count becomes substrate-derivable rather than narrated.

**Q3 (gate semantics).** If a substrate gate fires on `deliberation-seal`, what is the admit predicate? Universal-mandatory means every deliberation must author at least one row (zero-with-named-exclusion as the cheap exit, mirroring §8.5 `audit-step: 0`). Conditional-by-kind means tactical seals are exempt. Pick a predicate. Defend it against the §1 (loses foundational instructions) and §6 (ceremony drift) failure modes.

**Q4 (subtraction discipline).** What concretely gets subtracted from `prompts/development.md` and `specifications/methodology.md` if your design is adopted? Net coherence-gain requires that the prose-prefix clause be REMOVED, not coexist with the typed primitive. Name the byte-identical clause text that gets deleted.

**Q5 (false-positive / over-fitting risk).** Substrate-gates that fire on legitimate `deliberation-seal` calls produce ceremony at best and refusal-debt at worst. Name the false-positive shape and the recovery path. Engage honestly with M-1's strongest insight from D-23: operator-policed clauses risk the unfired-trigger pile.

**Q6 (constraint-without-compromise discharge).** For each of the six failure modes named in the Problem Statement, name how your design defends against it. Be concrete — do not handwave. If your design fails to defend against any of the six, name it as a residual cost.

## Evidence base

- **DV-S159-1** at S159: original decision shipping seal-grade as `engine_feedback` prefix-row. P-1 anthropic + P-2 openai-codex cross-family convergence on shape; P-3 anthropic ship-nothing minority preserved as M-1. Synthesis declined a new table on DV-S109-1 ceremony-subtraction discipline, with the v2 promotion path documented (`prompts/development.md:120`).
- **DV-S109-1** at S109: ceremony-subtraction discipline retired `constraints.md` and named "each addition should pay for itself." The operator at S180-open has explicitly invoked the constraints-without-compromise framing — DV-S109-1 is preserved as background but does NOT preclude a typed primitive when the operator-named-mandate cites the constraints themselves as the basis for graduation.
- **DV-S176-1** at S176: T-32 chain-walk substrate-gate. The lesson preserved: "when discipline depends on the agent reaching for a tool the substrate could dispatch automatically, ship the substrate dispatch — prose-and-discipline reproduces the failure modes the kernel defends against."
- **DV-S171-1** at S171: §1.5 v18→v19 amendment under operator-named-mandate. Worked example of the operator naming a §1.5 failure mode and the agent shipping the spec edit in the same turn.
- **DV-S179-1** at S179: T-34 (migration 036) and T-35 (migration 038) refusing NEW NULL `cited_object_id` and `source_decision_v2_id` rows. Same NULL-FK-traceability shape as the seal-grade FK gap. Receipt-pattern from T-32 (markdown is presentation, row + sha256 is proof) is the model.
- **Empirical seal-grade row state** (queried 2026-05-03):
  - 8 rows total since DV-S159-1: EF-S159-1, EF-S161-3, EF-S171-1, EF-S173-1, EF-S176-1, EF-S179-1, plus 2 closure-of-record rows (EF-S159-2, EF-S159-3).
  - 7 disposed: EF-S159-1 by DV-S159-1-close (closure-of-record), EF-S161-3 procedural, EF-S171-1 by emit-time-inline-dispositions, EF-S173-1 + EF-S176-1 procedural-self-dispose per DV-S171-1 §1.5.
  - 1 currently untriaged: EF-S179-1 ("4 single-frame counterfactuals — D-28 substrate-hardening + determinism arc shape").
- **Substrate citation grammar at engine-v49** (§5 cite-typing): `cite` slot resolves only against `objects.alias`. `OI-...` and `FR-...` aliases are NOT in `objects` — fold into claim text instead. T-34 refuses NEW `decision_supports` rows with NULL `cited_object_id` for cite-required bases.
- **Receipt-pattern shape (T-32 model)**: row + sha256 + edge_count is the proof object; markdown presentation does not gate. Future receipt-tables (precheck, manifest-hash seal, this proposal if typed) follow this shape.
- The substrate currently has 43 open issues, 90 undisposed forward-references, 4 untriaged engine_feedback rows.

## Response format

Author a markdown body with **exactly these labeled sections** (the capture subagent decomposes against these labels):

```
**Position.** <one paragraph distillation, 8–240 chars, will become the perspective-position atom.>

**Schema sketch.**
- <bullet, what tables/columns/triggers your design adds or modifies, one bullet ≤240 chars>
- ...

**CLI surface.**
- <bullet, what new bin/selvedge subcommands or flags this introduces, ≤240 chars>
- ...

**Migration path.**
- <bullet, in what order migrations + handler edits + spec edits ship, ≤240 chars>
- ...

**What not.**
- <bullet, what this proposal explicitly excludes from scope, ≤240 chars>
- ...

**Open questions.**
- <bullet, what you cannot resolve within your stance, ≤240 chars>
- ...

**Risks.**
- <bullet, false-positive shape + recovery path for each major gate, ≤240 chars>
- ...

**What lost.**
- <bullet, what is forfeit if your proposal is adopted, ≤240 chars>
- ...
```

Each bullet must be a single sentence, ≤240 chars, no newlines, no fenced code, no pipe tables. The substrate atom triggers refuse all three; do not embed.

When you reference an OI/DV/EF/FR alias, use the canonical form (`OI-086-003`, `DV-S176-1`, `EF-S179-1`, `FR-S179-11`). Do NOT cite OI- or FR- aliases in the typed-cite slot of any future decision-record (T-01 / cite-typing rule); fold them into claim text instead.

## Constraint on external imports

Per `specifications/methodology.md` §Cautions, **do not import ideas from outside this engine's process** as commitments. If you have an external concept (a pattern from another framework, a database design from a textbook), surface it as a hypothesis to deliberate inside your position — name it, name where it came from, name what evidence in *this workspace* supports it. Unsourced external claims are discipline failures.

## Output target

Write your full position to `/Users/ericmccowan/Development/complex-systems-engine/deliberations/180-seal-grade-typed-graduation/perspective-<N>.json` where `<N>` is your perspective number (provided in your role section). The JSON shape is:

```
{
  "deliberation_id": 29,
  "label": "P-<N>",
  "family": "<anthropic | openai | google | other-llm | human>",
  "stance": "<short stance phrase, 8–240 chars>",
  "body_md": "<full markdown body>"
}
```

Then submit the perspective:

```
bin/selvedge submit perspective --payload @deliberations/180-seal-grade-typed-graduation/perspective-<N>.json
```

**Do not run `git commit`, `git push`, `git add` for the purpose of staging-to-commit, or any commit-like operation.** The orchestrator commits at session-close after `bin/selvedge export --write`. Author payloads, run `bin/selvedge submit ...`, write files when authorised, but do not finalise git state.

You are perspective P-&lt;N&gt;. Your role-specific stance follows below.
