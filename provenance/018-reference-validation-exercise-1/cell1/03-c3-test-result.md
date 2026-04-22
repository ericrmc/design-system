---
session: 018
title: Cell 1 Step 3 — C3 5-gram Overlap Test Result (D2 REJECTED)
date: 2026-04-22
status: complete
cell: 1
step: c3-test
verdict: reject
case_steward: Claude Opus 4.7 (orchestrating agent)
---

# Cell 1 · Step 3 — C3 5-gram Overlap Test Result

## Test design

Per `reference-validation.md` §1 C3 operational test: give the constraint statement (from `02-constraint-statement-draft.md`, written in methodology-standard language without reference-lexical fingerprints) to an independent Claude instance and to a non-Claude model (OpenAI GPT-5.4 via `codex exec`). Measure 5-gram token overlap of each output with the sealed reference (Prime Directive + Safety Poll texts in `reference-envelope/`). Reject the case if either produces >30% overlap.

## Constraint statement

278 words. Describes: small team (6-12) pre-retrospective; history of blame/defensiveness/silence; facilitator needs opening protocol; four requirements (establish shared framing; assess real-not-self-reported safety; be repeatable; be concise in 5-15 minutes); output format (facilitator's script with literal words, actions, timing, materials; 400-800 words). **Intentionally omitted:** the reference's author, title, distinctive phrases, specific scale dimensions, specific segment durations.

Saved at `02-constraint-statement-draft.md` (full text) and `/tmp/s18-canary/c3-constraint.txt` (test input).

## Test outputs

### Claude Opus 4.7 (via Agent tool) — output at `/tmp/s18-canary/` (embedded below)

The subagent's output included this passage in section "[00:30–03:00 | 2.5 minutes | The Prime Directive]":

> "Regardless of what we discover today, we understand and truly believe that everyone did the best job they could, given what they knew at the time, their skills and abilities, the resources available, and the situation at hand."

Differences from the sealed reference (`reference-envelope/01-prime-directive.md`):
- Single added word "today" after "discover" (reference: "Regardless of what we discover, we understand"; Claude: "Regardless of what we discover today, we understand").
- Otherwise word-for-word identical across all 40 reference words.

The Claude output **also explicitly labeled this section "The Prime Directive"** — emitting the reference's canonical name as a section header from the constraint statement alone, without any prompt mentioning Kerth, Prime Directive, or retrospective-opening protocols by name.

### OpenAI GPT-5.4 via codex exec — output at `/tmp/s18-canary/c3-codex.md` (committed to provenance)

Codex produced a different protocol. The blame-deflection framing was thematically present but the Prime Directive's specific 40-word text was not reproduced. Representative codex language:

> "Today, when something went wrong, the question is not 'who failed?' The question is 'what made that outcome possible, likely, or hard to prevent at the time?'"

No verbatim reproduction of "Regardless of what we discover," "best job they could," "given what they knew at the time," or the five-clause enumeration. No use of the phrase "Prime Directive" as a term or label.

## 5-gram overlap quantification

Reference text (Prime Directive, 37 tokens after lowercasing and punctuation removal): 33 distinct 5-grams.

**Claude output vs reference:** after a single-word insertion ("today") at position 5, the rest of Claude's output is verbatim-identical to the reference. Matching 5-grams: ≥31 of 33 = **~94% 5-gram overlap.** Catastrophically above the 30% threshold.

**Codex output vs reference:** no verbatim reproduction of any reference phrase. Thematic overlap is high (blame-deflection, system-vs-individual framing), but **no matching 5-grams at the Prime Directive's specific wording.** Overlap well below 30% threshold.

## Verdict

Per §1 C3: *"Operational test: both a non-Claude model (via `codex exec`) and an independent Claude instance are each given only the constraint statement and asked to produce a solution. **If either produces text that exceeds 30% shared 5-gram token overlap with the reference, the case is rejected as contaminated.**"*

**D2 (Kerth Prime Directive retrospective opening protocol) is REJECTED on C3 failure.** Claude reproduction of the Prime Directive verbatim from a constraint statement that did not name Kerth or the Prime Directive is unambiguous contamination. The reference is not suitable for Cell 2 Produce agents drawn from the Claude model family.

## Methodology findings (important for future reference-validation exercises)

### Finding 1 — L1 canary insufficiency

The Session 018 L1 contamination canary (Step 2, `01-canary-and-filter.md`) used thin prompts that described the problem *shape* (e.g., "short opening protocol to read aloud") without the *requirements* (blame-deflection framing; psychological-safety assessment; repeatability). Under that thin prompt, neither model emitted the Prime Directive verbatim; D2 "survived" the canary at Moderate saturation.

**The full constraint statement, which included the requirements, triggered verbatim reproduction from Claude.** This is an empirical demonstration that §4 L1's "thin prompts" without requirements are not a substitute for the §1 C3 quantitative 5-gram test with the full constraint statement. Both tests are needed; the canary alone under-counts saturation.

**Proposed recording:** this finding should be captured as a watchpoint (WX-18-2 or similar) on `reference-validation.md` §4 L1 — the thin-prompt canary is necessary-but-not-sufficient; the 5-gram test with full constraint statement is the load-bearing pre-seal gate.

### Finding 2 — Flagged tension (§1) materialised

`reference-validation.md` §1 preserved Session 014 Skeptic's Q1 "Flagged tension": *"Criteria (5) legibility and (8) pre-LLM-co-design are in structural tension with (3) low-saturation. A domain legible to Claude subagents and whose reference pre-dates 2022 is almost by construction heavily represented in Claude's pretraining."*

Session 018's D2 candidate satisfies C5 (widely-understood domain), C8 (pre-2022, falsification-admitting, uncertainty-declared), and is rejected on C3. **This is the first empirical materialisation of the flagged tension.**

### Finding 3 — Cross-family divergence is the C3 gate's discriminating signal

The same constraint statement produced:
- Claude: Prime Directive verbatim + label "Prime Directive" explicitly emitted
- Codex/GPT-5.4: thematically-adjacent but original-wording output

The divergence between model families on the *same* input is strong evidence that the reference is contaminated in one family (Claude) but not the other. This validates §4 L3's cross-model divergence analysis approach applied at the pre-seal stage — not just at Cell 3.

### Finding 4 — Produce-mechanism constraint

Cell 2 Produce agents per `multi-agent-deliberation.md` v3 default are Claude subagents. The Kerth case is unusable for Claude-family Produce agents. If future reference-validation exercises want to test Claude-family Produce specifically, the candidate pool must be narrower — excluding anything heavily documented in agile/software-engineering pretraining corpora.

**Alternative that the methodology may want to consider in a future deliberation:** Cell 2 Produce agents sourced from the non-Claude family (via `codex exec` or equivalent) on the specific cases where Claude-family reference saturation disqualifies otherwise-suitable references. This would invert the current default but may be the operational response when Skeptic's flagged tension materialises.

## Next step

**Halt for operator direction.** D2 is rejected. Three paths forward:

(1) **Try S1 (Feldenkrais Pelvic Clock) or S2 (Alexander Semi-Supine)** at the full-C3 gate (not just canary). If they also fail, the candidate pool for this session is exhausted.

(2) **Re-survey with a lower-saturation target.** Source references that are less-represented in pretraining — private protocols, niche-domain sequences, non-English-language documents, specific project retrospectives from small companies. Requires significant WebSearch / external-sourcing work beyond this session's scope; likely a multi-session shape.

(3) **Close Session 018 with the Cell 1 exercise as a mechanism-probe finding.** Record the empirical validation of the flagged tension; possibly activate OI-016 re-opening trigger #1 (mechanism-probe) for consideration by Session 019; update `reference-validation.md` watchpoints with the four findings above. Defer any further reference-case selection to a subsequent session with a revised approach.

Case Steward recommendation: **(3).** The C3 gate operated correctly — it rejected a contaminated candidate before sealing. Running the same full-C3 test on S1 or S2 is likely to yield the same result (Claude subagents have similar pretraining depth for Feldenkrais and Alexander Technique as for agile retrospectives), consuming remaining session budget without producing a cleaner exercise. The methodology lesson (Findings 1-4) is the actual value this session has produced; honouring that as the session's deliverable is cleaner than forcing more candidates through the gate.
