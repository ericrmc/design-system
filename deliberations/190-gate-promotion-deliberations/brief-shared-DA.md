# Shared brief — D-A: OI-S083-1 reminder pathway (S190)

> The following sections are **byte-identical** across all perspectives of D-A. Only the role-specific `STANCE` section at the end of each per-perspective brief differs.

## Methodology context

You are one of 4 perspectives convened in **S190 of the Selvedge self-development workspace** (`/Users/ericmccowan/Development/complex-systems-engine`). Selvedge is a methodology-and-substrate engine — perspectives reason together, durable artefacts are produced, reasoning is preserved as substrate rows in `state/selvedge.sqlite`, the engine evolves by running its own mechanic on its own outputs.

The substrate is the only writable surface for session state. Markdown in `provenance/` is a generated export from substrate rows. Every session phase is `bin/selvedge submit <kind>`. Atoms are 8–240 chars, no newlines, no fenced code, no pipe tables.

Current engine version is **engine-v52**. Migrations 001..044 are applied. Read these for context:
- `prompts/development.md` §6 (substrate-canonical authoring path; spec-version body_md surface).
- `prompts/development.md` §1.5 (auto-proceed dispatcher and operator-named-mandate clauses).
- `tools/hooks/refuse-substrate-md.py` (existing PreToolUse refusal that fired at S082 to recover the slip).
- `MODE.md`, `CLAUDE.md` (operator-facing pinned context).
- `specifications/methodology.md` §When-to-convene + §Synthesis (deliberation discipline).

## Problem statement

EF-S083-1 (calibration) recorded the originating slip: at S082 the agent attempted `Edit prompts/development.md` to author spec text, despite §6 of that same file naming the substrate-driven authoring path (`bin/selvedge submit spec-version --payload {body_md: ...}`). The PreToolUse hook `tools/hooks/refuse-substrate-md.py` refused at execution time and named the recovery (SELVEDGE_EXPORT_CONTEXT=1 bypass + spec-version body_md path). Recovery cost was cheap — one round-trip, no substrate damage.

The diagnostic shape EF-S083-1 named: previous three operations (Edit init_cmd.py, Edit cli.py, Write test_init_guard.py) primed an active modify-file tool-shape that carried into the next file without re-evaluating whether the filepath belonged to the substrate-canonical category. Reasoning channel was substrate-aware (the agent had just considered post-S180 spec_versions chain state); action channel was substrate-naive (Edit emitted anyway). The two channels were not connected at the moment of tool selection.

The earliest harness hook surface is **PreToolUse**, which fires at *execution* not at *selection*. The existing refuse-hook is execution-time. The deliberation's question is whether a *selection-time* (or earlier) reminder pathway should ship.

EF-S083-1 enumerated three candidate proactive-reminder pathways, each with cost asymmetry:
- **(a) PreToolUse non-blocking hint mode** — injects a context message before a Read/Edit/Write tool runs against any path matching a substrate-canonical glob, naming the substrate-CLI alternative. Visible to the agent's reasoning channel before the action lands; spends context tokens on every matching tool call.
- **(b) File-header marker** on substrate-canonical files (e.g. a fenced HTML comment block at top of `prompts/development.md`, `specifications/*.md`, `MODE.md`) naming the file as substrate-export and pointing at the authoring CLI. Visible whenever Read fires; spends context tokens proportional to file reads.
- **(c) CLAUDE.md pin** enumerating substrate-canonical paths and their CLI authoring commands in the always-loaded codebase-instruction surface. Visible at every session-open via the `claudeMd` system-reminder; spends one-time context budget at session-open, no per-tool-call cost.

Plus the implicit default:
- **(d) Status-quo** — keep the existing PreToolUse refusal hook only; trust that the recovery message is cheap enough that one slip per N sessions is acceptable cost.
- **(e) Hybrid** — combine two or more.

The OI was opened as the *typed-observation* pathway per DV-S152-1 / DV-S159-1 / DV-S180-1 graduation precedent, with recurrence pressure as the threshold for substrate-gate upgrade. OI-S083-1 sat MEDIUM since S083 with one observed instance (S082). No recurrence has been recorded since.

## Design questions

You are asked to author a position covering each of the following:

**Q1 (graduate or status-quo).** Should a proactive reminder pathway ship, or is status-quo (PreToolUse refusal + cheap recovery) sufficient? The OI is on a one-instance typed-observation. DV-S152-1 graduation precedent waits for recurrence pressure; the operator-named-mandate clause in §1.5 admits substantive scope when an operator names a failure mode. Has the failure mode been named? Take a position.

**Q2 (which pathway, if shipping).** If you favour shipping, which of (a) PreToolUse hint, (b) file-header marker, (c) CLAUDE.md pin, (d) hybrid? Defend on cost-asymmetry: context-budget spent vs which slips reliably caught. Engage with the *channel-connection* failure mode EF-S083-1 named — selection happens earlier than execution; only some pathways intercept before selection.

**Q3 (false-positive / over-fitting risk).** Each pathway has false-positive shapes. PreToolUse hint fires on legitimate reads-of-substrate-canonical-files-for-non-authoring-purposes (e.g. orienting). File-header marker spends context on every Read regardless of whether the agent intended to write. CLAUDE.md pin permanent context-budget cost. Name the false-positive shape and the recovery path. Argue honestly whether your favoured pathway over-fits to one observed instance.

**Q4 (subtraction discipline).** What concretely gets added to or removed from the engine surface if your design is adopted? If you propose hybrid, name *which* combination — coexistence is not free; each addition spends context budget. If you propose status-quo, name what evidence would change your position.

**Q5 (constraint discharge).** Selvedge defends against six failure modes (preserved in `bin/selvedge orient`'s "Why this engine exists" packet from retired `constraints.md` v1):
1. Loses foundational instructions under context pressure.
2. Anchors on most-recent-prior-decision over foundational specification.
3. Confuses authority of speakers.
4. Generates narrative-fitting numbers when substrate values exist.
5. Defaults to mechanism-addition over mechanism-subtraction.
6. Drifts into ceremony when each addition does not pay for itself.

For your proposed pathway (or status-quo), name how it discharges or fails to discharge each. Lean into #5 and #6 explicitly — both cut against new mechanism on a one-instance observation.

**Q6 (graduation-trigger calibration).** If status-quo, name the *exact* recurrence-pressure threshold that should trigger graduation (one more slip? two? a different slip-shape?). If shipping, name the *exact* calibration-EF shape that would trigger your design's withdrawal (e.g. "if the hint fires N times per session on legitimate reads, withdraw"). Substrate-detectable triggers are preferred.

## Evidence base

- **EF-S083-1** at S083: original calibration row naming the slip + the three pathway candidates + the typed-observation→graduation pathway.
- **DV-S152-1**: typed-observation→gate progression precedent. Typed-conflict-primitive shipped after recurrence pressure crossed the threshold; the same pattern names the bar this OI must clear.
- **DV-S109-1** at S109: ceremony-subtraction discipline retired `constraints.md`; "each addition should pay for itself in capability." This cuts strongly against shipping anything on a one-instance observation.
- **DV-S171-1** at S171: §1.5 v18→v19 amendment + operator-named-mandate clause. The user's diagnosis of a §1.5 failure mode is itself admissible substantive scope; here the user has selected this OI for deliberation under operator-presence (not named the failure mode as a §1.5 violation).
- **DV-S176-1** at S176: T-32 substrate-gate. Lesson: "when discipline depends on the agent reaching for a tool the substrate could dispatch automatically, ship the substrate dispatch — prose-and-discipline reproduces the failure modes the kernel defends against." This cuts *for* shipping a pathway since prose-and-discipline (the §6 substrate-canonical authoring instruction the agent was reading at S082) failed.
- **Existing PreToolUse refuse-substrate-md.py**: refuses Edit/Write on glob-matched substrate-canonical files with a recovery hint. Adversarial baseline — works at execution-time, post-selection.
- **CLAUDE.md** at workspace root: contains auto-memory disabled clause and tool usage guidance; loaded at every session-open via the `claudeMd` system-reminder.
- **No recurrence**: from S083 (calibration recorded) to S189 (last close), no calibration-EF has named another instance of the same slip-shape. 7 sessions of substrate-canonical Edits authorised via SELVEDGE_EXPORT_CONTEXT=1 bypass without slip.

## Response format

Author a markdown body with **exactly these labeled sections** (the capture subagent decomposes against these labels):

```
**Position.** <one paragraph distillation, 8–240 chars, will become the perspective-position atom.>

**Schema sketch.**
- <bullet, what files/hooks/CLAUDE.md sections your design adds or modifies, ≤240 chars>
- ...

**CLI surface.**
- <bullet, what new bin/selvedge subcommands or flags this introduces, or "none" if no CLI change, ≤240 chars>
- ...

**Migration path.**
- <bullet, in what order hook-edits + CLAUDE.md edits + spec edits ship, ≤240 chars>
- ...

**What not.**
- <bullet, what this proposal explicitly excludes from scope, ≤240 chars>
- ...

**Open questions.**
- <bullet, what you cannot resolve within your stance, ≤240 chars>
- ...

**Risks.**
- <bullet, false-positive shape + recovery path for each major addition, ≤240 chars>
- ...

**What lost.**
- <bullet, what is forfeit if your proposal is adopted, ≤240 chars>
- ...
```

Each bullet must be a single sentence, ≤240 chars, no newlines, no fenced code, no pipe tables. The substrate atom triggers refuse all three; do not embed.

When you reference an OI/DV/EF/FR alias, use the canonical form (`OI-S083-1`, `DV-S152-1`, `EF-S083-1`, `FR-S189-8`). Do NOT cite OI- or FR- aliases in any typed-cite slot of any future decision-record (T-01 / cite-typing rule); fold them into claim text instead.

## Constraint on external imports

Per `specifications/methodology.md` §Cautions, **do not import ideas from outside this engine's process** as commitments. If you have an external concept (a pattern from another framework, a hook design from another tool), surface it as a hypothesis to deliberate inside your position — name it, name where it came from, name what evidence in *this workspace* supports it. Unsourced external claims are discipline failures.

## Output target

Write your full position to `/Users/ericmccowan/Development/complex-systems-engine/deliberations/190-gate-promotion-deliberations/perspective-A-<N>.json` where `<N>` is your perspective number (provided in your role section). The JSON shape is:

```
{
  "deliberation_id": 2,
  "label": "P-<N>",
  "family": "<anthropic | openai | google | other-llm | human>",
  "stance": "<short stance phrase, 8–240 chars>",
  "body_md": "<full markdown body>"
}
```

Then submit the perspective:

```
bin/selvedge submit perspective --payload @deliberations/190-gate-promotion-deliberations/perspective-A-<N>.json
```

**Do not run `git commit`, `git push`, `git add` for the purpose of staging-to-commit, or any commit-like operation.** The orchestrator commits at session-close after `bin/selvedge export --write`. Author payloads, run `bin/selvedge submit ...`, write files when authorised, but do not finalise git state.

**Do not run any destructive substrate operation against the primary substrate at `state/selvedge.sqlite`**: no `bin/selvedge init` (with or without `--force` / `--really-force`), no `bin/selvedge migrate --apply`, no direct `sqlite3` write/`.recover`/`UPDATE`/`DELETE`/`DROP`/`ALTER`/`PRAGMA writable_schema` against the primary file, no `rm`/`mv` of `state/selvedge.sqlite*`, no edits to files under `state/migrations/`. If your task appears to require any of these, halt and report back.

You are perspective P-&lt;N&gt;. Your role-specific stance follows below.
