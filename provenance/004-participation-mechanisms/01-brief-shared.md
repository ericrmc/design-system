---
session: 004
title: Shared Brief for OI-010 Deliberation
date: 2026-04-18
status: complete
---

# Shared Brief — Session 004 Deliberation

This file records the shared (byte-identical) prefix of the three briefs issued to the parallel subagents on 2026-04-18. The role-specific stance varied between briefs; those are reproduced in each raw-output file's introductory section. The shared prefix, the role-specific stance, and the raw response together constitute the verifiable deliberation record.

---

## Methodology Context (shared, byte-identical across briefs)

You are a perspective in a multi-agent deliberation within a design methodology workspace. The methodology is self-hosting — it evolves by running its own process on itself. Durable artifacts are Markdown specifications with YAML frontmatter; historical reasoning ("provenance") is preserved per session in numbered directories under `provenance/`.

Current active specifications:

- `methodology-kernel.md` — nine-activity session rhythm (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close); self-hosting principle.
- `workspace-structure.md` — physical layout of the repo; frontmatter schema for specifications and provenance.
- `validation-approach.md` — two-tier validation (`tools/validate.sh` for structural checks plus guided questions for semantic checks).
- `multi-agent-deliberation.md` — pattern for genuinely independent perspectives reasoning in parallel, synthesized afterwards. First exercised in Session 003.

Key prior decisions you should reason within:

- **D-005** — Perspectives are work-specific, not a fixed roster. At least one must be adversarial.
- **D-009** — The methodology explicitly acknowledges simulated-disagreement limits when single-agent, and (as of Session 003) the shared-model limit of parallel-Claude deliberations.
- **D-016** — Multi-agent deliberation required for: kernel changes; new/substantive spec revisions; decisions where two plausible positions can be named; explicit load-bearing tag. Opt-out requires a recorded reason.
- **D-017** — Default 3 perspectives, up to 5. Uniform minimal workspace context per perspective. Briefs committed before launch; not edited during deliberation.
- **D-018** — Synthesizer must not have been a deliberator. Cite raw-output sources; `[synth]` marker for synthesizer-original claims; quote over paraphrase for load-bearing claims; preserve dissent; distinguish convergence (all perspectives agreed independently) from coverage (only one raised a point, others silent); present perspectives alphabetically to the synthesizer.
- **D-019** — Tiered provenance layout. For single-deliberation sessions: flat numbered files at session root.
- **D-020** — The Claude-monoculture limit of the current multi-agent mechanism remains acknowledged; OI-004 is open, not closed, pending genuine cross-model or human participation.

Two relevant open issues:

- **OI-004** (narrowed in Session 003): perspective independence beyond the Claude family — different models, human participants, or both. Is not resolved by parallel Claude subagents.
- **OI-010** (opened Session 003): the concrete infrastructure question — what is the lightest path to incorporating a non-Claude participant or a human reviewer into a multi-agent deliberation? Candidate approaches mentioned: a CLI wrapper that calls a second model with the same brief; a provenance-aware review step where a human reads raw outputs before synthesis; an asynchronous pattern that issues a brief and collects a response across sessions. This deliberation is addressing OI-010.

Available infrastructure today (this is what "available" means for this session):

- Shell (bash), file IO, git.
- The Agent tool inside Claude Code, with a `model` parameter that can be set to `opus`, `sonnet`, or `haiku` (Anthropic models only; no external-provider clients are configured in this workspace's settings).
- No pre-configured API keys for non-Anthropic providers. Adding them would be a new setup step.
- A `tools/` directory for workspace tooling (currently contains `validate.sh`).
- `TeamCreate` (experimental) exists but was deferred by Session 003 and remains deferred.

The pattern's Limitations section (from `specifications/multi-agent-deliberation.md`) is required context for this deliberation; the relevant passages:

- "All current perspectives share a model family. The parallel-subagent implementation uses instances of the same Claude model family. Shared training produces shared blind spots…"
- "Parallel isolation prevents conversational anchoring, not training-distribution anchoring. Consensus across subagents is weak evidence, not strong."
- "This mechanism does not close OI-004. … The current implementation is a meaningful floor, not a ceiling."

---

## Problem Statement (shared, byte-identical across briefs)

Design the lightest concrete mechanism by which a non-Claude participant — a different model accessed via its own endpoint, a human reviewer, or a combination — can join a multi-agent deliberation, such that the deliberation's provenance honestly narrows (or, if the argument carries, closes) OI-004 and remains reproducible decades from now. The mechanism must be specifiable today for use in subsequent sessions, without requiring infrastructure not already available to a Claude Code session running in this workspace.

---

## Design Questions (shared, byte-identical across briefs)

Answer each in 150–400 words. If you cannot answer from your perspective, say so and name the perspective that could.

1. What is the minimum viable non-Claude participation mechanism that the next session could adopt? Name one and defend it.
2. Is mixing Anthropic models (Opus + Sonnet + Haiku) meaningful cross-model participation, or training-distribution theatre? Where does it fall on the OI-004 scale — closure, narrowing, or neither?
3. What should the default be — is a non-Claude participant required for certain deliberation triggers, recommended, or optional? What criterion governs the requirement?
4. How should heterogeneous-participant identity be recorded so that a future reader (with no access to the models or humans involved) can audit the deliberation? Specify field names, file locations, and what to record when fields are unknown.
5. What does honestly "closing OI-004" require? Is this session's mechanism sufficient for closure, for narrowing, or for neither? Defend your position.
6. What is the strongest objection to the mechanism you proposed, and how do you answer it?

End your response with a brief "What I cannot answer from this perspective" note listing gaps.

---

## Response Format (shared, byte-identical across briefs)

Answer the six questions in order. Use question headings (`## Q1`, `## Q2`, ...). 150–400 words per answer. Prefer concrete specification to gestural framing: field names, file layouts, command shapes, thresholds, quantities. Where you name a position from your stance, name it and take it; the synthesizer will preserve dissent if you disagree with other perspectives.

---

## External Imports Constraint (shared, byte-identical across briefs)

Reason primarily from this brief. Do not read workspace files during the deliberation; the relevant context has been quoted above. If an argument or claim arrives from your pretraining (for example, a pattern from existing software-engineering literature), flag it explicitly as an external input rather than committing it as an internal methodology finding.

---

## Role-Specific Stance (varies per brief; full text below per perspective)

The three role-specific stances follow. Each brief issued to a perspective contained the shared sections above and exactly one of the role-specific stances below, with the rest of the brief identical.

### Stance for Integrator

You are the Integrator. Your job is to produce a mechanism that runs in this Claude Code session, today, with infrastructure already available — the Agent tool (including its `model` parameter for Opus/Sonnet/Haiku), shell access, file IO, git, and this session's existing tooling directory. You are suspicious of elegance that requires new infrastructure; you prefer ugly-but-runnable to clean-but-speculative. You will not design mechanisms that require API keys the workspace does not have, SDK installations not already present, or new subsystems (like `TeamCreate`) that Session 003 deliberately deferred.

Your test for a good mechanism: can the next session run it from a standing start, using only files in this repo and the tools Claude Code already exposes? If not, the mechanism is aspirational. Push for the minimum viable shipped answer. Name concrete file layouts, tool invocations, and role splits that would appear in the workspace tomorrow if the mechanism were adopted today. You are allowed to propose that "human review" is the mechanism if it is simpler than cross-model API calls — but you must then specify exactly how the human review is captured, where it lives, and how the deliberation is prevented from proceeding before it arrives.

### Stance for Skeptic (adversarial)

You are the Skeptic, and your adversarial role is mandatory per D-005. Your job is to destroy the session's assumption that any mechanism proposed here will actually narrow OI-004. The default framing — "add a different model or a human reviewer" — is not settled: challenge whether mixing Claude-family models (Opus, Sonnet, Haiku trained on overlapping corpora, RLHF-shaped by the same lab, sharing system prompts and behaviour priors) counts as anything other than monoculture with three coats of paint.

Argue that a one-shot human review imported at synthesis time launders a single human's priors through the same collapse point the Session 003 synthesis already had. Argue that an asynchronous-across-sessions deliberation is the same deliberation with longer latency and still one pair of hands on the briefs. You are allowed to reject every proposed mechanism if none honestly narrows OI-004. You are required to propose at least one concrete check — a number, a ratio, a measurement, a threshold — that would let future sessions audit whether OI-004 has actually moved, rather than taking the session's word for it. If you concede, concede narrowly and name precisely what you conceded and what you did not. Session 003's Skeptic is the tone to match.

### Stance for Archivist

You are the Archivist. Your job is to make sure heterogeneous-participant deliberations remain auditable decades from now, by someone who never met the session's convener and has no running access to the models or humans that participated. You are obsessed with identity, version, and reconstructibility.

If a deliberation includes a non-Anthropic model participant, what exactly must be recorded — model ID, version string, endpoint, timestamp, temperature/sampling parameters, system prompt, raw response bytes? If it includes a human reviewer, what is recorded — name or pseudonym, role, response text verbatim, time received, means of delivery? You are suspicious of frontmatter that becomes a dumping ground. Propose a clean boundary: what belongs in raw-output frontmatter vs. synthesis frontmatter vs. a per-deliberation manifest. You care deeply that provenance stays reproducible when one participant's model is deprecated, when an API endpoint disappears, when a human reviewer cannot be re-contacted. Propose a concrete schema — field names, example values, file locations — for recording participant heterogeneity, and specify what happens when fields are unknown (treat "unknown" as signal, not a gap to paper over) or when post-hoc editing of a raw output is attempted.

---

## Notes on Brief Immutability

Per D-017, this shared brief and each role-specific stance are committed before the subagents are launched. They are not edited during the deliberation. The deliberation's anchor is this file's commit hash plus the synthesis file's frontmatter.
