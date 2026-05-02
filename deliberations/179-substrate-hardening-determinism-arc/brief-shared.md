# Shared brief — S179 substrate-hardening + determinism arc

> The following sections are **byte-identical** across all perspectives. Only the role-specific `STANCE` section at the end of each per-perspective brief differs.

## Methodology context

You are one of 5 perspectives convened in **S179 of the Selvedge self-development workspace** (`/Users/ericmccowan/Development/complex-systems-engine`). Selvedge is a methodology-and-substrate engine — perspectives reason together, durable artefacts are produced, reasoning is preserved as substrate rows in `state/selvedge.sqlite`, and the engine evolves by running its own mechanic on its own outputs.

The substrate is the only writable surface for session state. Markdown in `provenance/` is a generated export from substrate rows. Every session phase is `bin/selvedge submit <kind>`. Atoms are 8–240 chars, no newlines, no fenced code, no pipe tables — the substrate refuses these by trigger.

The current engine version is **engine-v48**. Migrations 001..032 are applied. The most recently shipped substrate gate is **T-32** (DV-S176-1, migration 031): the decision-record submit handler walks every cited alias inside the same write_tx and inserts a `decision_chain_walks` receipt, refusing on walker exception, unresolved alias, or count mismatch. T-32 was promoted from a "recommended-clause" S175 backfire (DV-S175-1) — the lesson preserved at DV-S176-1 is **prose-and-discipline reproduces the failure modes the kernel defends against**.

Read these clauses for full context:
- `prompts/development.md` §1.5 (self-driving dispatch + starvation-breaker + operator-diagnosis-as-named-mandate).
- `prompts/development.md` §5 (decision-record + cite typing + T-32 precedent-sensitive provenance check + "authority and the prose-clauses-without-instrumentation lesson").
- `specifications/methodology.md` §When-to-convene-multiple-agents and §Synthesis (citation discipline, dissent preservation, seal-grade clause, reopen-on-new-reading).

## Problem statement

The operator at S179 named the failure mode: **insufficient substrate hardening, insufficient determinism**. Quoting:

> "The substrate must be used in full (constraints, triggers, etc) even the Python part of it can help. There is too much drift, not enough checks in place. The engine methodology must be as consistent and deterministic as possible. Plan the arc to deliver all functionality required in this session and mark everything high priority. Do NOT reduce scope, ENFORCE usage. SHOW CONTEXT AT RIGHT TIMES, LIMIT ENTRY, FORCE CHECKS BEFORE DECISIONS ARE MADE."

This is an **operator-named-mandate** per `prompts/development.md` §1.5 — admissible as substantive scope under operator presence regardless of priority-order queue, and per the DV-S176-1 lesson, prose-and-discipline must yield to substrate-gate where the substrate could dispatch automatically.

There are ~25 MEDIUM-priority open issues that map to substrate-hardening or determinism gaps, plus three operator-named meta-features (SHOW CONTEXT, LIMIT ENTRY, FORCE CHECKS BEFORE DECISIONS). The operator's directive is to **promote them all to HIGH and ship the arc**.

The substrate-detectable hardening backlog by group:

**Group A — cite/traceability NULL gaps (substrate admits NULLs that policy forbids):**
- OI-086-001 spec_clause source_decision_v2_id traceability is unenforced.
- OI-086-003 decision_supports / alternative_rejections allow NULL cited_object_id on cite-required bases.
- OI-086-004 legacy_imports.decomposition_status untracked.
- OI-S088-1 atom_type conflation: issue dispositions and links reuse rejection_reason atom_type.
- OI-S125-1 harness alias not registered in objects; cross-citation `[RH-…]` from decision-records would fail T-01.
- OI-S126-5 typed-graph linkage thins in external-problem sessions.

**Group B — review-loop / gate enforcement still operator-policed:**
- OI-083-001 substrate enforcement of the coding review loop.
- OI-S104-1 manifest-hash sealing as forward direction.
- OI-S133-1 review loop static audit misses integration-test failures; iter cap blocks runtime-fix records.
- OI-S145-1 SELVEDGE_EXPORT_CONTEXT bypass mechanism too permissive.

**Group C — trigger predicates needing substrate-detectable shape:**
- OI-S125-2 falsification trigger expiry-window enforcement deferred to harness expire CLI.
- OI-S151-3 visibility-gap seam: deliberation-atom reachability from artefact-set.
- OI-S151-4 second-arc reference_harness re-evaluation gate predicate must be substrate-detectable.
- OI-S159-1 sub-type verification at typed-observation closure.
- OI-S163-1 procedural-closure-discipline gates.

**Group D — concurrency / determinism / drift:**
- OI-S091-1 migration 011 encodes engine-v24 as a snapshot; fresh workspaces start versions stale.
- OI-S122-1 sessions.slug has no UNIQUE constraint.
- OI-S130-1 conditional close-time temporal-claim lint.
- OI-S152-2 graduation-review trigger for typed-observation pathway.
- OI-S154-1 operator-session vs substrate-session numbering-drift enforcement gap.
- OI-S154-4 perspective_claim.section_kind enum branch on deliberation kind.
- OI-S154-6 orient queue-depth alert when untriaged engine_feedback exceeds threshold.
- OI-S177-1 atom-length 240-char ceiling friction at decision_supports.claim, decision_effects.target_descriptor, review_findings.finding.

**Plus three operator-named meta-features:**
- **SHOW CONTEXT at right times.** Before decision-record submit (and other load-bearing submits), the engine should automatically present relevant prior decisions, similar OIs, recent supersedes, and active spec clauses.
- **LIMIT ENTRY.** Submit handlers should refuse more aggressively when the agent attempts to skip prerequisite reads or context-gathering.
- **FORCE CHECKS BEFORE DECISIONS.** A pre-decision gate (`bin/selvedge precheck`) that the agent must pass through, leaving a substrate receipt, before decision-record submit will be accepted.

## Design questions

You are asked to author a position covering each of the following:

**Q1 (arc shape).** What is the right shape of this arc? One milestone per group, several together, all in one session, multi-session? The operator said "deliver all functionality required in this session" but that must be balanced against substrate review-loop discipline (T-20 medium-or-higher findings must be addressed) and seal-grade scrutiny.

**Q2 (sequencing).** Which gates ship first and why? Some gates depend on substrate columns the previous gate would not yet have established. Identify the dependency graph and propose a milestone order.

**Q3 (pre-decision context-injection design).** Operator named SHOW CONTEXT, LIMIT ENTRY, FORCE CHECKS. Propose a concrete substrate + handler design. Possibilities (you are not limited to these):
  (a) New table `decision_prechecks` recording the agent's read of prior-decision context, similar OIs, active spec clauses; T-NN refuses decision-record submit unless a precheck row exists for the same session within N seconds.
  (b) `bin/selvedge precheck --target <kind> --target-key <key>` CLI that prints relevant context AND inserts a row whose hash the submit handler verifies.
  (c) Extension of T-32 chain-walk to a wider "context-walk" that also surfaces same-target prior decisions and supersedes graphs.
  (d) Something else.

**Q4 (in-session deliverability).** The operator forbade scope reduction. What is the maximum substantive content this session can ship without violating §7 review-loop discipline or §4 seal-grade discipline? Be concrete: name the migrations, handler edits, spec edits. If you believe full delivery in one session is unsafe, name the structural defense (multiple sealed deliberations? Pre-staged migrations vetted in S180?).

**Q5 (false-positive / over-fitting risk).** Substrate-gates that fire on legitimate decision-records produce ceremony at best and refusal-debt at worst. For each major gate you propose, name the false-positive shape and the recovery path.

**Q6 (prompt-development edits).** What clauses must be added or removed in `prompts/development.md` v21→vN to reflect the new substrate gates? Which clauses become redundant once the gate ships?

## Evidence base

- The substrate gate **T-32** shipped at S176/DV-S176-1 (migration 031) following the **DV-S175-1 backfire**: a recommended-clause without instrumentation produced ceremony without measurement, and the operator named the failure mode at S176-open. The promotion-trigger language in S175 required calibration-EFs that required the same prose-pattern-match the recommended-clause already failed to ensure. **Lesson preserved at DV-S176-1: when discipline depends on the agent reaching for a tool the substrate could dispatch automatically, ship the substrate dispatch.**
- **DV-S171-1** at S171 amended `prompts/development.md` §1.5 to insert tractable MEDIUM-OI as priority-2 ahead of untriaged EFs, and added the starvation-breaker clause. This was operator-named-mandate at S171-open; the v18→v19 edit shipped without further deferral. The pattern repeats here.
- **DV-S109-1** ceremony-subtraction discipline argues against substrate enforcement until prompt-only proves insufficient. The operator at S179 has explicitly **operator-precluded DV-S109-1 as rejection basis**: "Do not 'wait for usage evidence'." Treat DV-S109-1 as background but do not invoke it as a basis to defer a substrate-gate.
- **DV-S152-1** typed-observation→gate progression precedent: typed-observation comes first, substrate-gate after recurrence. Same operator preclusion applies here — the operator has named the failure mode and is short-circuiting the recurrence requirement.
- The **`decision_chain_walks` table (migration 031)** is the canonical "receipt" pattern: substrate-side row + sha256 + edge_count is the proof object; markdown is presentation. Future receipt-tables (precheck, manifest-hash seal, falsification expiry) should follow this shape.
- **`engine-v48`** is the current version. The arc will likely bump to engine-v49 or v50 depending on milestone count.
- Recent migrations show the shape: `state/migrations/031-decision-chain-walks-substrate-gate.sql` for the chain-walk gate, `state/migrations/030-harness-typed-observation-columns.sql` for harness columns, `state/migrations/029-close-state-items-required-at-close.sql` for T-NN refusing close without close_state_items.
- The substrate currently has **48 open issues**, **87 undisposed forward-references**, **2 untriaged engine_feedback rows** (EF-S178-1 calibration about priority-2 drain, EF-S178-2 audit-step:0).

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

When you reference an OI/DV/EF/FR alias, use the canonical form (`OI-086-003`, `DV-S176-1`, `EF-S178-1`, `FR-S178-7`). Do NOT cite OI- or FR- aliases in the typed-cite slot of any future decision-record (T-01 / cite-typing rule); fold them into claim text instead.

## Constraint on external imports

Per `specifications/methodology.md` §Cautions, **do not import ideas from outside this engine's process** as commitments. If you have an external concept (a pattern from another framework, a database design from a textbook), surface it as a hypothesis to deliberate inside your position — name it, name where it came from, name what evidence in *this workspace* supports it. Unsourced external claims are discipline failures.

## Output target

Write your full position to `/Users/ericmccowan/Development/complex-systems-engine/deliberations/179-substrate-hardening-determinism-arc/perspective-<N>.json` where `<N>` is your perspective number (provided in your role section). The JSON shape is:

```
{
  "deliberation_id": 28,
  "label": "P-<N>",
  "family": "<anthropic | openai | google | other-llm | human>",
  "stance": "<short stance phrase, 8–240 chars>",
  "body_md": "<full markdown body>"
}
```

Then submit the perspective:

```
bin/selvedge submit perspective --payload @deliberations/179-substrate-hardening-determinism-arc/perspective-<N>.json
```

**Do not run `git commit`, `git push`, `git add` for the purpose of staging-to-commit, or any commit-like operation.** The orchestrator commits at session-close after `bin/selvedge export --write`. Author payloads, run `bin/selvedge submit ...`, write files when authorised, but do not finalise git state.

You are perspective P-<N>. Your role-specific stance follows below.
