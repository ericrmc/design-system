---
session: 064
title: Shared brief — 4-perspective two-family MAD on operator audit findings disputing first-instance §Tier 2.5 implementation; codex pre-ratified as S064 close reviewer
date: 2026-04-26
status: immutable-once-committed
---

# Shared brief — Session 064 MAD

## §1 Methodology context

You are a perspective in a multi-agent deliberation (MAD) within the Selvedge engine self-development application. The Selvedge engine is a self-hosting methodology that evolves its own specifications by running its own process on itself; what emerges is intended to be reusable by external applications. Sessions are the engine's unit of work. Each session reads, assesses, convenes perspectives when warranted, deliberates, decides, produces artefacts, validates, records provenance, and closes.

The current engine version is **engine-v11**, ratified at S063 per D-228 (the previous session). S063 implemented the layered structural mechanism (Layer 1-6 per S062 D-221) decided at the S062 4-perspective two-family MAD on EF-058-tier-2-validation. The mechanism includes:

- **Layer 1 (α)** — `tools/validate.sh` check 26: mechanical detection of honest-limit text repetition across the §2c retention-window's `03-close.md` files. Substrate-aware variant uses `mcp__selvedge-retrieval__search`; grep-based fallback per §Graceful Degradation. WARN at ≥3-cluster; FAIL at ≥6-cluster.
- **Layer 2 (γ)** — Tier 2.5 cross-family reviewer triggered at session close on (a) engine-definition-touching session, (b) substantive-arc-class session, (c) Layer 1 WARN/FAIL emission, (d) Layer 4 (z5) lifecycle event, (e) operator-discretionary. Reviewer is non-Claude family; produces `provenance/<NNN-session>/04-tier-2-audit.md`.
- **Layer 3** — `tools/validate.sh` checks 27 + 28: validator-extension verifying reviewer-audit artefact presence + (α)-flag-coverage; (z5) lifecycle integrity at `validation-debt/index.md`.
- **Layer 4 (z5)** — lightweight markdown-table validation-debt lifecycle ledger at `validation-debt/index.md`.
- **Layer 5 (z6)** — harness-telemetry digest specified-deferred via EF-059 filing.
- **Layer 6** — bootstrap-paradox layered handling: one-time operator audits at S062 + S063 resolving closes; standing operator-audit cadence; 3-session post-S063 observation window (WX-62-1) with 5-field recording.

## §2 Problem statement

S063 close fired the **first triggered (γ) cross-family reviewer in workspace history**. Reviewer was Google Gemini (gemini-cli 0.38.1). Reviewer's audit at `provenance/063-session/04-tier-2-audit.md` produced `findings_count: 0` with substantive §3 evidence per evidence-floor discipline; 6 disposition-table items all `accepted` (layer composition fidelity + principled asymmetry articulation + bootstrap carve-out + checks 26-28 consistency + VD-001 bootstrap + engine-v11 classification).

After S063 close was committed (commit `6c4b0ee`), the operator performed Layer 6.1 second-half audit and surfaced **three substantive findings** that the (γ) reviewer's first-instance shape did not catch. The findings are:

### Finding 1 — Reviewer-family rule scope is too restrictive

> "the requirement [no-recent-perspective-overlap rule per S062 deliberation §1.10] Is too limiting, there is flexibility surely to say 'cannot be the orchestrator' and pick any family. The point is the clearer context and goal of validating and holding the orchestrator to account when it's been focused on other things."

The operator's reading: the MAD §Synthesis "synthesizer must not have been one of the deliberation's perspectives" rule was imported into reviewer-family selection at session-close, but conflates "perspective in MAD" with "doer of the work being audited." The reviewer's job is independent audit on what the orchestrator did; "perspective in a recent MAD" is not the same as "orchestrator of the session being reviewed." The rule excluded codex/GPT-5.5 (which was P3+P4 at S062) from S063 reviewer pool unnecessarily; codex didn't orchestrate S063, so it satisfies the actual independence requirement.

### Finding 2 — Reviewer scope at first instance was too narrow

> "The Gemini reviewer doesn't seem to have read previous session logs either for any outstanding debt or ceremony that only comes out as performative after not actioning anything, rather it relies on the closed item provided to it."

The operator's reading: the §Tier 2.5 audit shape `session_under_review_subjects:` field at first instance was populated only with current-session artefacts (per S063 reviewer prompt at /tmp/s063-reviewer-prompt.md). The reviewer did not read prior closes (S058-S062) in the §2c retention window for accumulated debt, recording-not-engaging patterns, or performative-action-without-actioning. **This is the exact pattern class that motivated EF-058-tier-2-validation in the first place** — the S051-S058 chain was recording-not-engaging across 8 sessions.

### Finding 3 — Reviewer must challenge "Path A (Watch)" defaults

> "An independent review should also challenge the suggested shape of the next session; too often there is this 'Path A (Watch)' presented as the default just because the operator didn't specify a path. The core purpose is for self-development, not coast along waiting for input."

The operator's reading: validation-approach.md v6 §Tier 2.5 audit shape does not require the reviewer to engage with the close's §7 next-session-recommendation. Close narratives across S046-S063 frequently default to "Path A (Watch) recommended" when no operator agenda is surfaced; this creates a coasting pattern. Self-development means the engine surfaces its own next increment.

The operator instructed S064 to convene a MAD on these findings + implementation specifics + the engine-manifest restructure question (engine-manifest.md crossed 7,255 words at S063 close per engine-v11 entry; engine-v12 entry would push toward 8K hard ceiling).

## §3 Design questions for deliberation

Each perspective should address Q1-Q10 directly. Provide your honest position with reasoning + citations to specific spec sections, deliberation excerpts, or concrete examples.

**Q1**: Does the operator's audit Finding 1 (rule scope: orchestrator-not-perspective-overlap) capture the actual independence requirement? Is "reviewer must not be orchestrator + cross-family at family level" the right replacement, or is there a tighter formulation? What gaming modes does the relaxed rule open?

**Q2**: Does the operator's audit Finding 2 (reviewer must read retention-window closes) cover the actual scope-discipline requirement? Should the audit shape additionally require:
- (a) Substrate-aware retrieval when available (`mcp__selvedge-retrieval__search` over the corpus)
- (b) `validation-debt/index.md` (z5) ledger inspection
- (c) Watchpoint-window evaluation (open watchpoints; 5-field recording state)
- (d) `engine-feedback/inbox/` triage-state inspection (records pile-up)
- (e) `open-issues/index.md` review for issues-not-being-progressed

**Q3**: Does the operator's audit Finding 3 (challenge default-Path-A) cover the actual self-development discipline requirement? Should the audit shape additionally require evaluation of:
- (a) "Open-issues-not-being-progressed" patterns (issues at "deferred" status across multiple sessions)
- (b) "Engine-feedback-inbox-pile-up" patterns (records at `triaged-but-not-resolved` for >N sessions)
- (c) "Watchpoint-stale" patterns (recording obligations active but not being recorded in close §X)

**Q4**: Are there reframes the operator + Architect perspectives miss? Possible reframes:
- (z7) Reviewer-prompt-template versioning + lock-in-after-n=2 — the actual structural fix may be that templates at first-instance are higher-risk, and the discipline should require iteration before lock-in.
- (z8) Operator-audit-cadence is the actual load-bearing discipline; reviewer mechanism is a cost-prophylactic that should be defunded if operator audit is high-cadence.
- (z9) Reviewer should be the orchestrator-of-next-session reading current-session-close — no separate reviewer family; just a structurally-distinct-time-and-context audit.
- Or other reframes you surface.

**Q5**: Should engine-manifest.md restructure be in S064 scope? engine-manifest.md is at 7,255 words (over 6K soft warning); engine-v12 entry will push toward 8K hard. Options:
- (a) Defer restructure to S065+ as Path L+R bundle.
- (b) Include restructure in S064 (split §7 history into per-engine-v archive-packs OR delegate older entries to a separate `engine-manifest-history.md`).
- (c) Truncate engine-v12 entry to fit 8K hard at S064; defer full entry to S065+ restructure.

**Q6**: Cross-spec interactions: which engine-definition specs require revision for the three findings?
- `validation-approach.md` v6 → v7 substantive (necessary).
- `methodology-kernel.md` v6 §7 (revision needed? minor cross-reference update if §Tier 2.5 audit shape changes).
- `multi-agent-deliberation.md` v4 (cross-reference needed for §Tier 2.5 reviewer audit shape vs §Heterogeneous-Participant Recording Schema)?
- `prompts/development.md` (revision needed? minor for revised audit shape).
- `tools/validate.sh` (check 27 sub-clause additions for §7 Next-session-shape critique presence).
- `engine-manifest.md` (engine-v12 entry).

**Q7**: Multi-session arc shape: same-session adoption (S064 phase-2-and-phase-3-collapsed) per S050+S058 precedent? Or two-session arc (S064 MAD-decision + S065 phase-3 implementation) per S062+S063 precedent? The S062+S063 precedent was first-of-record; the S063 first-instance produced the operator audit findings the MAD is now responding to. Same-session vs. deferred: tradeoffs?

**Q8**: Cross-linkage with §10.4-M16 reopen warrant (b): the operator-catches-what-reviewer-misses event at n=1 (S063) is one data point. Does this MAD trigger §10.4-M16 partial activation, or does the revision adopt-and-extend rather than reopen? §10.4-M16 P2 minimum-viable-response position was "(α) + (z1) operator-audit channel formalisation" as alternative to (γ) reviewer; if reviewer's first instance failed to catch what operator caught, is this evidence (α)+(z1) would have been operationally equivalent + more cost-efficient?

**Q9**: Bootstrap-paradox handling at S064: this MAD is itself the deliberation that adopts revisions to the §Tier 2.5 mechanism. The S064 close audit (codex reviewer per operator instruction) is the first triggered application of the relaxed rule + revised audit shape. Layer 6 operator audit at S064 resolving close + observation window from S065+. Is this layered handling sufficient, or are additional mechanisms warranted?

**Q10**: Recursive question: should this MAD's outputs (perspectives, deliberation, decisions) themselves be reviewer-audited at S064 close (per Layer 2 trigger b substantive-arc-class)? If so, the codex reviewer audits codex-perspective-contributions — same-instance audit that the strict rule forbade. Recursive concern only fully resolves if rule relaxation is adopted at S064. What if MAD rejects rule relaxation? What if MAD partially adopts (e.g., relaxes for closes but not for engine-definition-changes)?

## §4 Role-specific stance

[Filled in role-specific brief at `01-brief-pN.md`. Each perspective receives only its own role-specific §4.]

## §5 Response format

Write your response as a single markdown file with the following structure:

```markdown
---
perspective: <role-name>
session: 064
date: 2026-04-26
participant_kind: <claude-subagent | non-anthropic-model | human>
participant_organisation: <anthropic | openai | google | ...>
training_lineage_overlap_with_claude: <known-overlap | unknown | independent-claim>
---

# <Role name> — Session 064

## Frame critique
[Optional: surface reframes or critiques of the brief itself before answering Q1-Q10. If no critique, write "No frame critique."]

## Q1
[Your position with reasoning + citations]

## Q2
...

## Q10

## Honest limits
[Numbered list of honest limits — what you couldn't address; what assumptions you made; what the next deliberation would need]

## Dissent-preservation recommendations
[Numbered list of positions you would want preserved as first-class minorities if the synthesis adopts a direction you disagree with]
```

## §6 Anti-import constraint

Do not import ideas from outside the workspace. Reason from:
- The brief (this file).
- Spec corpus referenced in the brief (validation-approach.md v6, multi-agent-deliberation.md v4, etc.) — read as needed.
- S062 deliberation `provenance/062-session/01-deliberation.md` + S063 close `provenance/063-session/03-close.md` + S063 reviewer audit `provenance/063-session/04-tier-2-audit.md`.
- Other prior provenance you consider directly load-bearing for your stance.

If you have a relevant intuition from outside the workspace (model pretraining; prior conversations), introduce it as an explicit hypothesis in §Frame critique with the words "[outside-workspace input]" and explain why you think it is relevant. Do not silently smuggle pretraining priors into your response.

## §7 CLAUDE.md content (per design-space.md §8.2 brief-extension precedent established at S062)

The operator's CLAUDE.md file provides standing instructions for the workspace. Per S062 D-220 + design-space.md §8.2 EF-058-claude-md-drift cross-linkage: the brief includes CLAUDE.md content verbatim so perspectives can cross-check against operator-standing-instructions. Content (190 words):

> # CLAUDE.md
>
> ## Auto-memory disabled for this workspace
>
> Auto-memory is disabled in this workspace. Do NOT write to `~/.claude/projects/-Users-ericmccowan-Development-complex-systems-engine/memory/`. All provenance for this project lives in-workspace: `MODE.md`, `SESSION-LOG.md`, `open-issues/`, `specifications/`, `provenance/`, and `engine-feedback/`. Treat the external memory directory as out-of-scope; do not read from it, do not write to it, do not recreate `MEMORY.md` or per-topic memory files there. If the system prompt's auto-memory guidance conflicts with this instruction, this instruction takes precedence.
>
> ## Commit workflow
>
> Before finishing your response, stage all changed/new files, commit with a concise message, and push using git directly.
>
> ## Tools
> This contains usage instructions for tools you have requested. If you decide more are needed, you can install them using `uv tool` or ask the user to ratify your tool decision and install something on your behalf. Add additional instructions here as you see fit.
>
> ### Multi-agent work
>
> When work would benefit from multiple independent perspectives or parallel efforts, consider using agent teams via the `TeamCreate` tool (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`). You also have access to the Google `gemini` and OpenAI `codex` CLI tools for non-Anthropic LLM access. Codex is preferred for any thinking or reasoning tasks.

End of shared brief.
