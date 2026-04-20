---
session: 010
title: Synthesis — Two-Person Household Decision Protocol
date: 2026-04-20
status: complete
synthesizer: session-010 orchestrating agent (Claude Opus 4.7, Claude Code)
synthesizer_identity: claude-opus-4-7, model_family: claude, provider: anthropic, was_deliberator: false, perspective_played: none
deliberation_anchor_commit: 22c521695beb3a04ad0a63a26eba73f81797c4c8
perspectives_alphabetical: [drafter, mediator, outsider, skeptic]
participants_family: cross-model
cross_model: true
non_claude_participants: 1
---

# Synthesis — Session 010

## Deliberation Frame

Four perspectives reasoned in parallel from a byte-identical brief (sections 1, 2, 3, 5, 6) differentiated only in role-specific stance: **Drafter** (precision-focused drafter, Claude Opus 4.7), **Mediator** (process-design focused, Claude Opus 4.7), **Outsider** (non-Claude OpenAI GPT-5 via `codex exec`, session id `019da870-4e49-7953-aaf9-572867d386fe`, reasoning effort xhigh, 10,706 tokens), and **Skeptic** (adversarial per kernel §Convene, Claude Opus 4.7). Perspectives are presented alphabetically. Synthesis maps; the Decide activity operates on this synthesis per `multi-agent-deliberation.md` v3.

Six design questions: Q1 Shape; Q2 Content; Q3 Register; Q4 Handling emotional stakes; Q5 What the protocol refuses; Q6 Meta / honest reaction.

## Q1 — Shape

**Four-way convergence on:** short prose artefact (not diagrams, trees, matrices, or two-column layouts); approximately one page or less; named moves with brief gloss per move. All four reject corporate visual grammars (arrows, boxes, scoring tables).

**Divergence on move count and shape:**

- [Drafter, 01a, Q1]: "A one-page document with four or five named moves, laid out as short headed sections with a line or two of prose under each." Explicitly rejects numbered lists ("too procedural"), flow diagrams ("too engineered"), and cyclic sequences ("implies a repeating meta-practice the couple hasn't signed up for").
- [Mediator, 01b, Q1]: "A short list of named moves with a clear sequence, plus one explicit loop-back." 5–6 named steps. "Ritual set (unordered 'moves') abandons the failure mode the user named as active — the process drifts because no one owns the 'decide now' moment."
- [Outsider, 01c, Q1]: "A one-page conversation loop, not a full-bodied 'protocol' in the heavy sense. Five short moves, arranged as a loose cycle, with a narrow side-strip for 'if one of you cares more' and 'what this refuses.'" Proposes: **"A House Decision in Five Moves."** Also notes: "The loop should visibly allow a pause between moves 3 and 4. That is where real household decisions often live."
- [Skeptic, 01d, Q1]: "No protocol. Or if a protocol must ship, the smallest possible object: a single index card of prompts, not a procedure." 3–4 prompts. "The word 'protocol' should not appear in the artefact at all. Neither should 'step', 'phase', or 'stage.'"

**Shape resolution [synth]:** Three-of-four want 4–5 named moves; Skeptic wants 3–4 (and preferably zero). A 5-move structure honours the majority and is within Skeptic's "if a protocol must ship" acceptable range. Mediator's sequential-with-one-loop-back and Outsider's loose cycle are convergent in function (both accommodate the real household pattern of narrowing options, pausing for research, then returning) and can be reconciled: a visibly sequential spine with an explicit "pause here if you need to check facts" permission between moves 3 and 4. Drafter's "headed short sections" format is compatible with all three alternatives and is the simplest production target.

**Load-bearing shape claim:** the artefact's shape must read as prose, not procedure. All four perspectives agree structurally; the differences are in surface register, which is Q3.

## Q2 — Content

**Four-way convergence on three moves:**

1. **Name the decision (open it).** All four perspectives include some version of a first move that makes the decision explicit and bounds it.
   - [Drafter, 01a, Q2]: "Opening the question. One of us names that there's a decision worth sitting down for, and roughly what it's about."
   - [Mediator, 01b, Q2]: "Name the decision out loud, and who's bringing it up. One sentence: what are we deciding, and roughly what's the budget and timeframe."
   - [Outsider, 01c, Q2]: "Name the actual decision. Verbatim wording I would consider: *Keep the decision small enough to finish.*"
   - [Skeptic, 01d, Q2]: "What is this actually about?" — with the argument that "the shelving-versus-bookshelves decision is rarely only about shelving."

2. **Name uneven caring.** The strongest single cross-model convergence in this deliberation. All four perspectives independently arrived at this as a load-bearing move.
   - [Drafter, 01a, Q4]: "If one of us cares much more than the other, that usually settles it."
   - [Mediator, 01b, Q4]: "Decide who cares more, and whether that settles it."
   - [Outsider, 01c, Q4]: "If one of you cares a lot more, and the other can genuinely live with that option, that is usually enough."
   - [Skeptic, 01d, Q2]: "Who cares more about this one?"

3. **Close cleanly.** All four perspectives include some version of an explicit close-or-name-what's-pending move.
   - [Drafter, 01a, Q2]: implicit in "Deciding" — "we either keep talking or sleep on it. No other machinery."
   - [Mediator, 01b, Q2]: "Call it, or name what's still in the way."
   - [Outsider, 01c, Q2]: "Close it cleanly. Finish with either a decision or a clear next action."
   - [Skeptic, 01d, Q2]: "What are we doing, and who's doing it?"

**Three-of-four convergence on a "say what matters" move:**

- [Drafter, 01a, Q2]: "What we each care about" — "stakes ('I want the lounge to feel like a room we read in'), not positions ('I want the oak shelves')."
- [Mediator, 01b, Q2]: "Each person says what they want, uninterrupted." Plus a separate "Say the thing underneath, if there is one" move.
- [Outsider, 01c, Q2]: "Say what matters, including who cares more." Combines "what matters" with "uneven caring" in one move.
- [Skeptic, 01d, Q2]: folded into "What is this actually about?" — does not make it a separate move.

**Three-of-four convergence on a "narrow options" move:**

- [Drafter, 01a, Q2]: "What we're actually choosing between. We name two or three real options."
- [Mediator, 01b, Q2]: implicit; not a named step (Mediator's five steps do not include options-narrowing as a distinct move).
- [Outsider, 01c, Q2]: "Keep the options short and real. Only compare a few live options. Two or three is enough."
- [Skeptic, 01d, Q2]: explicitly rejects a research/information-gathering step as "patronising."

**Outsider-unique content contribution — the burden-cost asymmetry clause:**

[Outsider, 01c, Q2]: **"Caring more does not trump the other person's cost, work, or ongoing inconvenience."** "If one option means the other person pays more, maintains it, installs it, loses function, or resents it every day, that objection weighs heavily even if they are the lower-care party aesthetically."

No Claude perspective produced this clause. Drafter, Mediator, and Skeptic all named "uneven caring" as a legitimate decision shortcut; only Outsider added the limiting clause that ongoing burden on the other party can outweigh strong preference. This is a structural refinement the three Claude perspectives missed and is load-bearing: without it, "who cares more" becomes a preference-wins rule that predictably produces resentment in exactly the failure mode the Mediator named as real (*one party silently stockpiles disagreement*).

**Skeptic-unique content contribution — the regret-check move:**

[Skeptic, 01d, Q2]: "What would we regret in a year? A regret check is more honest than a benefits check because it forces both people to imagine the outcome they do not want, which is the side of the trade-off that optimism underweights." No other perspective produced this framing.

**Divergence on the optional check-in/after-note move:**

- [Drafter, 01a, Q2]: "(optional) Checking back in." In favour.
- [Mediator, 01b, Q2]: "Optional sixth: a short after-note, weeks later. I'm ambivalent." Qualified in-favour.
- [Outsider, 01c, Q2]: "Also must not reward the more verbally skilled person." No after-note in Outsider's 5 moves; explicitly "make the decision part of the house and move on" in Q5.
- [Skeptic, 01d, Q2]: "A 'revisit this decision in N weeks' step. Post-decision review is institutional machinery." Against.

**Two-two split** on after-note inclusion. The same split reappears in Q5 (post-decision review refused).

**Content resolution [synth]:** A 5-move structure that honours the full four-way convergence (name the decision; name uneven caring; close cleanly), the three-of-four convergences (say what matters; narrow options), and adopts the Outsider-unique burden-asymmetry clause inside the uneven-caring move:

1. Name the decision.
2. Say what each of us cares about.
3. Narrow to real options.
4. Look for the workable yes — including the burden clause.
5. Close it, or name what's next.

The Skeptic-unique "regret in a year" move is considered as a candidate but not adopted as a named move in the main sequence — it compresses into Move 2 (when "what each cares about" includes future-regret imagining) rather than standing alone. The synthesizer notes this preservation is partial; Skeptic's regret framing is a testable refinement if the artefact fails domain validation.

The optional check-in is adopted as a one-sentence footnote at the end of the artefact, not as a numbered move. This honours Drafter+Mediator's ambivalent-yes while respecting Outsider+Skeptic's concern that a numbered "revisit" step would import retrospective register. The footnote framing matches Mediator's minimal proposal [01b, Q2]: "A few weeks in, it's worth one sentence each on whether this still feels right. Not a scheduled review. Not a form. Just a named possibility." This resolution mirrors the Session 009 Q4 pattern of adopting a minimal form that honours both sides of a 2-2 split.

## Q3 — Register

**Four-way convergence on rejected register-markers:**

- Corporate/managerial: "stakeholders", "alignment", "action items", "decision-maker", "criteria", "stakeholder" — rejected by all four.
- Therapy/self-help: "hold space", "honour your perspectives", "check in with your feelings" — rejected by all four.
- Framework/best-practices language — rejected by all four.
- Any visual template aesthetic — rejected by all four.

**Four-way convergence on preferred voice:** short sentences; plain verbs; no Latinate jargon; reader-respecting (not chummy, not instructive).

**Two-two split on person:**

- [Drafter, 01a, Q3]: **first-person plural** ("we"/"us"/"our") throughout. "'We' positions the reader as already inside the couple the document is for; 'you' positions the document as coming from somewhere outside and instructing." Proposes "your person" as the couple-native term.
- [Skeptic, 01d, Q3]: **first-person plural** ("we"). "What is this actually about?" reads as something the two of them might say to each other. "What is the decision about?" reads as something a facilitator would ask them."
- [Mediator, 01b, Q3]: **second-person plural** ("you two"). "'You' addressed to the couple puts the document in the position of a friendly guide, not a participant."
- [Outsider, 01c, Q3]: **second-person plural** ("you two") for the instructions, **first-person** for the example lines. Hybrid.

**Person resolution [synth]:** The 2-2 split is genuine. Outsider's hybrid pattern — second-person addressing for the instructions ("Name the decision. Say what matters.") with first-person example lines ("I care more about the look of this than the price difference.") — is the only proposal that accommodates both positions: the document is a guide (not a participant) but the example lines model the couple's internal voice. The synthesizer adopts Outsider's hybrid as the resolution. This mirrors Session 009's pattern of adopting an Outsider-originated third way when Claude-only perspectives produce a 2-2 split.

Drafter's "we" dissent is preserved. If the hybrid reads awkwardly in use, the Skeptic+Drafter "we" voice is the preferred fallback. This is recorded as a watchpoint for domain validation.

**Four-way convergence on title style:** the artefact should not call itself a "protocol", "framework", or "process". Candidates named:

- [Drafter, 01a, Q3]: **"Deciding Together"** or **"A way of deciding, for two"**.
- [Mediator, 01b, Q3]: no specific proposal; defers to Drafter.
- [Outsider, 01c, Q1]: **"A House Decision in Five Moves"**.
- [Skeptic, 01d, Q3]: no candidate; rejects the available options without proposing.

**Title resolution [synth]:** Three proposals are in play. **"A House Decision in Five Moves"** (Outsider) is the most specific and least coy; **"Deciding Together"** (Drafter) is the most casual; **"A way of deciding, for two"** (Drafter) is the most distinctive. The synthesizer adopts **"A House Decision in Five Moves"** because (a) it names the thing by its form without inflating it, (b) it reads as descriptive rather than framework-like, (c) Outsider-originated title choices have cross-lineage support (cross-model signal), and (d) "Five Moves" echoes Morning Unfurl's precedent of naming the count without dramatising it. Drafter's "Deciding Together" is preserved as a secondary-position candidate if "A House Decision in Five Moves" reads as too declarative in domain validation.

## Q4 — Handling Emotional Stakes

**Four-way convergence** on every substantive point:

- Name uneven caring once, plainly, at the surface; trust the reader thereafter.
- Reject therapy-adjacent language ("hold space", "check in with feelings", reflective-listening mirroring).
- Reject corporate-diversity gestures ("honour both perspectives", "ensure both voices are heard").
- Reject equalising machinery (scoring-intensity scales, mandatory equal-airtime rules).
- Do not convert qualitative stakes into quantitative scores.

**Outsider-unique contribution 1 — burden-cost asymmetry clause.** Already captured in Q2 (see above).

**Outsider-unique contribution 2 — the verbally-skilled-partner failure mode:**

[Outsider, 01c, Q4]: "It also must not reward the more verbally skilled person. That is a quiet failure mode. If the artefact overvalues explanation, the more articulate spouse wins too often. Better to privilege clear statements of preference and burden over persuasive performance."

No Claude perspective produced this framing. It has a testable implication: the artefact's Move 2 (say what matters) should not invite explanation or justification — only statement of preference and burden. This is a structural constraint, not just a tonal one.

**Mediator-unique contribution — the "uneven-caring-is-granting-not-winning" reframe:**

[Mediator, 01b, Q4]: "This isn't the caring-more party 'winning' — it's the caring-less party granting the decision, which is a different gesture."

This reframing is load-bearing. It explicitly inverts the default reading of "who cares more wins" into "who cares less grants", which is more compatible with the brief's trust-assumed register.

**Skeptic-unique contribution — the "this one" de-escalator:**

[Skeptic, 01d, Q4]: "The prompt should be 'who cares more about this one?' with the trailing 'this one' doing important work. It frames unevenness as situational — *this* decision, not *decisions in general* — which de-escalates by implication."

Adopted: the artefact's caring-more question uses "this one" rather than a bare "who cares more".

**Resolution [synth]:** All four-way-convergent rejections become entries in the "not this" section (Q5). The Outsider's burden-cost asymmetry and verbally-skilled-partner concerns shape Move 4. The Mediator's "granting not winning" reframe is incorporated into Move 4's gloss. The Skeptic's "this one" phrasing is adopted. This is the densest single-question cross-model uptake in the deliberation.

## Q5 — What the Protocol Refuses

**Four-way convergence on refusing:**

- Weighted scoring matrices / decision matrices (all four).
- Written justifications (all four).
- Mandatory cool-off periods (all four; Mediator explicitly, Outsider explicitly, Drafter explicitly; Skeptic via "time-boxing emotional process is a patronising gesture").
- Third-party arbitration (Mediator, Outsider, Skeptic; Drafter silent but consistent with direction).

**Three-of-four converge on refusing voting thresholds:**

- [Drafter, 01a, Q5]: "Voting thresholds. There are two people. Voting is either 1–1 (deadlock, no mechanism) or 2–0 (consensus, no vote needed)."
- [Mediator, 01b, Q5]: "No voting thresholds or weighted scoring."
- [Outsider, 01c, Q5]: "Formal veto rights or voting rules. In a two-person household, 'each person gets a veto' sounds tidy and often works badly."
- [Skeptic, 01d, Q5]: notes that voting thresholds are "too obviously wrong for two people" and argues explicitly *against* listing them in the "not this" section — "including them would make the artefact look like it was designed with three-person groups in mind and then retrofitted."

**Skeptic-unique meta-refusal** — the "which refusals to actually name" question:

[Skeptic, 01d, Q5]: "The 'not this' section should list probably three items, chosen to be the ones most likely to sneak back in during revision. My candidates: weighted scoring, written justifications, third-party arbitration."

This is a sharp point. Naming a refusal draws attention to a possibility. Naming "no voting thresholds" signals that voting was considered. Naming "no post-decision review" signals that review was considered. The synthesizer takes this seriously: the "not this" section should list the refusals that (a) might plausibly sneak back in during revision and (b) are not so obvious that naming them implies they were considered.

**Resolution [synth]:** The "not this" section adopts Skeptic's three-item list (weighted scoring matrices, written justifications, third-party arbitration) as the primary refusals. Mandatory cool-off periods are added as a fourth because they are tonally seductive in the "give yourselves time" register that might otherwise creep in. Voting thresholds and explicit veto rights are deliberately *not* listed, per Skeptic's argument. Post-decision review is *not* listed — the optional after-note at the bottom of the artefact handles this dimension obliquely without inviting a review-meeting default.

**"Not this" section wording** (synthesis-proposed, candidate for D-057):

> **Not this**
>
> - Not a scoring matrix. If you want to make a spreadsheet, that is fine, but this is not one.
> - Not a written case. The one-line close is enough; no mini-briefs required.
> - Not a third-party call. Look up facts, not votes.
> - Not a cool-off rule. Sleep on it if you want to; don't if you don't.

The section heading is "Not this" (Skeptic's proposal) rather than "What this refuses" (Morning Unfurl's wording). Rationale: "refuses" has become methodology-vocabulary, and the artefact should not wear its methodology on its sleeve.

## Q6 — Meta / Honest Reaction

**Four-way convergence on the methodology-vocabulary-leakage risk:**

- [Drafter, 01a, Q6]: "The word 'protocol' itself. It's exactly the kind of word that will push the downstream writing in a corporate direction." Also: "decision-making" as a hyphenated compound.
- [Mediator, 01b, Q6]: "The risk is that the methodology's own register (rigorous, specified, iterative) leaks into the artefact. The artefact has to shed the methodology's voice entirely."
- [Outsider, 01c, Q6]: "The most Claude-like risk in the brief is not factual error; it is **over-civilized overdesign**. Phrases like 'Domain validation as a first-class activity,' 'emotionally intelligent and psychologically secure,' and the careful fencing-off of non-goals all make sense inside the methodology. But they can tempt the artefact toward self-conscious correctness."
- [Skeptic, 01d, Q6]: "The phrase 'decision-making protocol' primes every downstream design choice toward formality."

**Convergence on the validation-signal weakness:**

- [Mediator, 01b, Q6]: noted; did not push hard.
- [Outsider, 01c, Q6]: "Household decisions are not hard mainly because people lack decision frameworks. They are hard because taste, effort, money, and future annoyance are tacit and cumulative."
- [Skeptic, 01d, Q6]: "The user is also the person who commissioned the artefact, the person who will read the deliberation output before trying the artefact, and the methodology's primary author. The chain of motivated interpretation is long. The wife's reaction is the more signal-bearing half of the validation."

**Outsider-unique contribution 3 — asynchronous/fragmented use:**

[Outsider, 01c, Q6]: "This has to work asynchronously and in fragments. Real household decisions are often started by one person sending two links or a photo, continued in a quick chat, then finished later after a measurement or price check. If the artefact assumes a deliberate sit-down conversation, it may read beautifully and fail in practice. The structure should survive being used across messages, not just face to face."

No Claude perspective named this. It is a concrete structural implication for the artefact: the moves must be individually addressable (not just sequential-in-one-sitting) so they can be picked up across messages, days, or contexts.

**Outsider-unique contribution 4 — perfect-symmetry risk:**

[Outsider, 01c, Q6]: "Perfect symmetry may feel less natural than light asymmetry. The brief says the protocol should name the initiator and the other party but remain symmetric in principle. Fine. But the surface wording should not overperform that symmetry. In real couples, one person often brings the decision because they care more, noticed the problem, or will do the work. The artefact should let that be normal."

Resolved in the artefact: the opening framing allows natural asymmetry ("one of you is bringing this up; the other is joining") without formalising symmetric rights.

**Skeptic-unique contribution — aim at obsolescence:**

[Skeptic, 01d, Q6]: "Good is an artefact the couple tries once, finds mildly useful, and then internalises and no longer needs. The artefact should aim at its own obsolescence. A protocol that remains on the fridge after six months has failed."

This reframes the success criterion. It is not adopted as a directive in the artefact text (which would be self-undermining), but it is recorded as the success criterion for domain validation interpretation: a "worked" report from the couple that includes "we didn't need it the second time" is a stronger signal than a "worked" report that requires continued use.

**Mediator-unique contribution — honesty-in-the-moment floor:**

[Mediator, 01b, Q6]: "The protocol I've described does assume a baseline of honesty — step 2 ('say what you'd actually pick') and step 3 ('is there something underneath?') both depend on the two people telling each other the truth in a specific moment. That's not the same as emotional intelligence, but it's also not nothing."

Recorded as a limitation: the artefact works for couples with a minimum floor of in-the-moment honesty. A softer-lying couple is outside the intended use case. This limitation is not prominently displayed in the artefact (which would patronise the intended users) but is noted in provenance.

**Mediator-unique contribution — A$500 band calibration:**

[Mediator, 01b, Q6]: "The A$500 budget band is doing more work than the brief acknowledges. If the protocol were being designed for a $20,000 decision, I'd want different steps."

Recorded as a limitation: the artefact is calibrated for medium-stakes A$500 decisions, not renovations, vehicles, or life decisions. This is worth surfacing in the artefact's "not this" section as a scope-refusal.

## Cross-Model Observations and Honest Limitations

**Cross-model signal strength.** The Outsider contributed three load-bearing elements no Claude perspective produced:

1. **Burden-cost asymmetry clause** in Move 4 [01c, Q2]: "caring more does not automatically beat ongoing inconvenience." Shapes Move 4's content materially.
2. **Asynchronous/fragmented use** observation [01c, Q6]: shapes the artefact's structural requirement that moves be individually addressable.
3. **"Over-civilized overdesign"** diagnosis [01c, Q6]: names the specific Claude-family failure mode the artefact must avoid.

A fourth Outsider-original contribution — the title "A House Decision in Five Moves" — is adopted, extending the Session 008/009 pattern of Outsider-unique language being load-bearing in final artefact production. Cumulative Outsider influence on Session 010: four concrete outcome-shaping contributions.

The Outsider also converged strongly with the three Claude perspectives on the four-way consensus items (name the decision, name uneven caring, close cleanly, refuse scoring matrices, refuse therapy register). The convergence pattern is not Claude-vs-non-Claude on any dimension; the Outsider sided with different Claude perspectives on different questions (closer to Mediator on voice; closer to Skeptic on "over-civilized overdesign" diagnosis; closer to Drafter on title-naming form). This is what a genuine distinct-training participant should do; it is consistent with the Sessions 005–009 Outsider participation pattern.

**Brief-priming check.** The Session 010 brief deliberately avoided Session 009's distinctive vocabulary ("copy-plus-reference", "domain-actor", "mutable/immutable", "silent bypass", "external-legibility") and did not seed Session 007/008 vocabulary. Checking the four raw outputs for lexical echo from the brief:

- "Friendly household document" appears in the brief and in all four perspectives — brief-originated; expected.
- "Load-bearing" appears in three of four; from the brief's §5 response format; brief-originated; expected.
- "Corporate" / "corporate register" appears across all four — seeded by the brief's Q3 "corporate process" framing; the perspectives converge on specific corporate-register-markers (stakeholders, alignment, action items) from their own vocabulary, not the brief's.
- "Therapy" / "therapy register" appears in three of four — arrived independently from Q4 framing (the brief did not use the word "therapy"); genuine convergence.
- "Over-civilized overdesign" is **Outsider-unique** and novel — not in the brief.
- "Aim at its own obsolescence" is **Skeptic-unique** and novel.
- "Burden" / "burden-cost" framing is **Outsider-unique**.

**Session 010 is the third consecutive session without a brief-priming finding.** Sessions 008 and 009 established the discipline; Session 010 continues it. Worth carrying forward as confirmed technique.

**Required Limitations Note** (per `multi-agent-deliberation.md` v3 §Limitations):

- All three Claude subagent perspectives share the Opus 4.7 model family; consensus among them is weak evidence, not strong.
- Parallel isolation prevents conversational anchoring, not training-distribution anchoring.
- Brief-writing has no adversary; framing choices propagate identically.
- The synthesis step is the pattern's highest-risk single-agent re-entry point. The synthesizer is Claude Opus 4.7, same family as three of four deliberators (not the Outsider). Conventions applied: citations to `[perspective-file, section]`; `[synth]` marker on synthesizer-original claims; quote-over-paraphrase for load-bearing claims; majority/minority structure reported explicitly.
- One non-Claude participant (Outsider) narrows OI-004 less than its presence suggests; sustained-practice is a cumulative property across sessions.
- Non-Claude participation depends on convener fidelity; the `codex exec` output was committed verbatim including the CLI banner and the end-of-stream duplication, with a `transport_notes` entry in the Outsider perspective file frontmatter.

## Synthesis — Recommendations for the Decide Activity

1. **Adopt a 5-move sequential artefact** with visible permission to pause between Move 3 (narrowing) and Move 4 (workable yes). Named moves, headed short sections with brief prose; not numbered mandatory steps. One page or close to it.

2. **The five moves (content):**
   1. Name the decision.
   2. Say what each of us cares about.
   3. Narrow to real options.
   4. Look for the workable yes. (Includes the Outsider-originated burden-cost asymmetry clause.)
   5. Close it, or name what's next.

   Plus: an optional one-sentence after-note at the artefact's foot. Not a numbered move; a footnote.

3. **Voice:** Outsider's hybrid — second-person plural addressing the couple ("you two"), with first-person example lines modelling the couple's internal voice. Plain verbs. Invitational when possible; plain imperative is fine when not. Drafter's "we"-throughout position is preserved as a secondary fallback if the hybrid reads awkwardly in domain validation.

4. **Title:** **"A House Decision in Five Moves"** (Outsider's proposal). Drafter's "Deciding together" preserved as secondary candidate.

5. **"Not this" section** with four items: no scoring matrix; no written case; no third-party call; no cool-off rule. Heading: **"Not this"** (Skeptic's proposal), not "What this refuses" (which has become methodology-vocabulary).

6. **Scope-refusal note:** name that the artefact is calibrated for small-to-medium household decisions (roughly the A$500 band) and is not intended for renovations, vehicles, or life decisions. Mediator-sourced.

7. **Structural requirement from Outsider [01c, Q6]:** moves must be individually addressable so the artefact can be used across messages/days, not only in a sit-down conversation. This shapes the artefact's prose density: each move's text must stand alone enough that a reader arriving at Move 3 without just-having-read-Move-2 can still use it.

8. **Success criterion for domain validation** (Skeptic-framed, synthesis-adopted): the couple tries the artefact once, finds it mildly useful, and internalises the pattern such that the second similar decision doesn't require returning to the artefact. A report of "we needed it every time" is a softer signal than a report of "we used it once and then didn't need to."

9. **Preserve dissent:**
   - Skeptic's "no protocol at all / smallest possible object" minority position is preserved in decision record as the null-alternative against which the artefact's domain-validation report should be read.
   - Drafter's "we"-throughout voice preference is preserved as a fallback.
   - Mediator's dissent on optional-after-note (qualified in-favour) is honoured via the footnote form.

## Preserved Minority Positions (Dissent Register)

- **Skeptic: no protocol at all; ship only if shipping is mandatory.** Not adopted (three-of-four converge on producing a 5-move artefact). Preserved as the null-alternative benchmark for domain validation.

- **Drafter: "we"/"us"/"our" throughout; no second-person addressing of the couple.** Not adopted (2-2 split resolved via Outsider's hybrid). Preserved as fallback if the hybrid reads awkwardly.

- **Skeptic: "what would we regret in a year?" as a dedicated move.** Not adopted as a named move (compressed into Move 2's "what each cares about"). Preserved as a testable refinement if the artefact fails domain validation on "the couple didn't surface future-regret before deciding."

- **Skeptic + Outsider: no optional after-note / post-decision reflection.** Not adopted (footnote form instead). Preserved; if the footnote is ignored in use or reads as institutional, the artefact would be revised to remove it.

- **Mediator + Outsider + Skeptic: concern that the methodology's claim generalises to governance-domain work.** Recorded as a watchpoint (see D-058 below). Not treated as adopted-or-rejected; the Session 010 domain validation is the test.

End of synthesis.
