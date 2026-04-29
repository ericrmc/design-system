# Cross-family spot-check — S132 calibration framing

You are a single-agent cross-family (openai) spot-check on a calibration move proposed by the orchestrator (Claude Opus). The session that produced the content (S131) already ran a 6-perspective cross-family deliberation; this is a relocation calibration, not a content question. Your job is to reality-check the move, flag anything missed, and surface conflicts with existing kernel content.

## Engine context (essentials only)

The Selvedge engine has three loadable spec files relevant here:

- **`specifications/methodology.md`** — the kernel. Mode-agnostic. Defines what Selvedge does, the nine activities, when to convene multiple agents, when to review, how preservation works. Header notes: "It replaces the prior split across `methodology-kernel.md`, `identity.md`, `multi-agent-deliberation.md`, and `validation-approach.md`."
- **`prompts/development.md`** — self-development application prompt. The engine working on its own evolution.
- **`prompts/application.md`** — external-problem application prompt. The engine working on a domain problem (software, research, policy, etc.). Says "See prompts/development.md for the concrete payload shapes for each submit kind. They are identical for external-problem sessions."

methodology.md §When-to-convene-multiple-agents currently has: triggers (kernel revision / two-plausible-positions / load-bearing), independence (state before seeing others), citation-of-workspace-material, "I-don't-know vs fabricate", adversarial requirement, cross-family for kernel-touching, synthesis-doesn't-decide, dissent preservation, reopen-on-new-reading.

## What S131 added (currently in prompts/development.md §4 only)

A substantive revision restoring 7 disciplines from the subtracted MAD v4 spec, agreed by 6-perspective cross-family deliberation:

1. **Number.** Floor of 3 valid perspectives. Target 4 for methodology-changing decisions; 3 for narrower load-bearing questions. Below the floor is consultation, not deliberation.
2. **Cross-family.** ≥1 perspective from a different model family (mentions `codex` for OpenAI, `gemini` for Google as concrete tools).
3. **Naming and selection.** Perspectives chosen for *expected disagreement on this problem*. No permanent roster. Free-form labels but stable names across brief/raw/synthesis/decision.
4. **Adversarial requirement.** ≥1 perspective adversarial.
5. **Stance briefs (shared/role-specific split).** Briefs share byte-identical methodology-context/problem-statement/design-questions/evidence/response-format/external-imports-constraint sections; only role-specific stance varies. Diffing two briefs from one deliberation must reveal only the role-specific stance.
6. **Brief immutability.** Briefs committed under `deliberations/<wno>-<slug>/` before any perspective launches; not edited during deliberation.
7. **Independence + Quorum + Graceful degradation.** Perspectives state independently. Fewer than 3 valid outputs is not a deliberation; re-run or reformulate. Refusal is provenance, not error.
8. **Synthesis discipline.** Synthesizer-not-a-perspective, citation `[P-N, Q#]`, `[synth]` markers for synthesizer-original claims, convergence-vs-coverage distinction (only multi-source agreement records as `synthesis_points.kind='convergence'`), dissent preservation as substrate `divergence`/`minority` rows.

Plus mode-specific content that is genuinely application-prompt-level:

- **CLI surface.** `bin/selvedge submit deliberation-open` / `perspective` / `deliberation-seal` / `synthesis-point` — mode-agnostic in payload shape but lives in the prompt because both prompts deliver these.
- **Capture subagent.** Decomposes perspective bodies into `perspective-position` + `perspective-claim` rows under closed `section_kind` enum (position / schema_sketch / cli_surface / migration_path / what_not / open_question / risk / what_lost). Substrate-tooling pattern.

## Proposed move (S132 calibration)

Move items 1–8 above (the kernel-level content) from `prompts/development.md` §4 to `specifications/methodology.md` §When-to-convene-multiple-agents. Trim `prompts/development.md` §4 to keep only CLI surface + capture-subagent pattern, with an explicit pointer to the kernel section. Add the same explicit pointer in `prompts/application.md` so external-problem agents inherit the kernel discipline. Engine-manifest and engine-version bump alongside.

Calibration **kind** because the content was already cross-family deliberated in S131 with 7 convergences (C-1 through C-7); this session is correcting *where* the content lives, not *what* it says.

## Your task

Five questions. Answer each in 2-4 sentences. Total response under 600 words.

**Q1.** Is methodology.md the right home for items 1–8? Specifically: are any of them genuinely application-mode-specific in a way the orchestrator missed? (E.g., does the 4-perspective target hold the same way for external-problem deliberations where domain perspectives may dominate?)

**Q2.** Does any of the new content conflict with what's already in methodology.md §When-to-convene? (Check for: duplication, contradictory rules, ordering changes that would matter.)

**Q3.** Is "calibration" the right decision-kind for this move? Or does the relocation itself constitute a methodology change worth substantive deliberation? (Consider: prompts/application.md inheritors would now be bound to disciplines they did not see deliberated.)

**Q4.** The plan jumps engine-manifest spec from v34 directly to v39, skipping v35-v38, to align spec_version with current_engine_version (engine-v38) plus the pending bump to engine-v39. Is this version-jump legitimate or a smell? (The atomic-propagation logic in `_submit_spec_version` sets `current_engine_version = engine-v{p['version']}` when `spec_id='engine-manifest'`.)

**Q5.** What did the orchestrator most plausibly miss? (Free response. Anything from architectural concern to implementation detail.)

Output: structured Q1-Q5 answers, no preamble, no postamble. If you have no concern under a question, write "No concern; <one-sentence rationale>." rather than padding.
