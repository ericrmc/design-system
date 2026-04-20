---
session: 011
title: Synthesis — W1 Kernel §1 Read Revision
date: 2026-04-20
status: complete
synthesizer: session-011 orchestrating agent (Claude Opus 4.7, Claude Code)
synthesizer_identity: claude-opus-4-7, model_family: claude, provider: anthropic, was_deliberator: false, perspective_played: none
deliberation_anchor_commit: f263aaa1ba8bf86a24d076908bc7ed5655150370
perspectives_alphabetical: [minimalist, outsider, reviser, skeptic]
participants_family: cross-model
cross_model: true
non_claude_participants: 1
---

# Synthesis — Session 011

## Deliberation Frame

Four perspectives reasoned in parallel from a byte-identical brief (sections 1–6) differentiated only in role-specific stance: **Minimalist** (smallest-defensible-change, Claude Opus 4.7), **Outsider** (non-Claude OpenAI GPT-5 via `codex exec`, session id `019da943-2c45-7f30-bab8-ce303aba09db`, reasoning effort xhigh, 13,820 tokens), **Reviser** (precision-drafter, Claude Opus 4.7), and **Skeptic** (adversarial per kernel §Convene, Claude Opus 4.7). Perspectives are presented alphabetically. Synthesis maps; the Decide activity operates on this synthesis per `multi-agent-deliberation.md` v3.

Five design questions: Q1 revised text and naming of senses; Q2 structural placement; Q3 scope of domain reading; Q4 PROMPT.md reconciliation; Q5 G/O/K/S necessity and refuse-the-revision case.

## Q1 — Revised text for kernel §1 Read, and naming of senses

**Four distinct text proposals.** Each perspective quotes specific text. All four distinguish the workspace-reading sense from a second (domain) sense; they differ on structural form and on whether the senses carry explicit named labels.

- [Reviser, 01a, Q1]: **Parallel sub-sections with bolded sense-names.** ~175 words. "**Workspace reading** applies to every session... **Domain reading** applies when a session produces or revises an artefact intended for use outside the workspace..." Argues from §7 Validate precedent.
- [Minimalist, 01b, Q1]: **In-paragraph elaboration, senses named only implicitly.** ~98 words. Preserves current first sentence; adds "When a session's work concerns a domain outside this workspace's self-hosting scope, Read additionally includes absorbing the domain constraints the session operates under and the domain knowledge available to the orchestrating agent and perspectives; such domain inputs must be surfaced in the session record, not silently applied." Argues against coining named terms-of-art.
- [Skeptic, 01c, Q1]: **In-paragraph elaboration, no sub-headings, minimum-damage.** ~90 words. Under-protest. Preserves current first sentence; adds a paragraph naming the two senses without sub-headings or labels. "The two activities are structurally asymmetric... Treating them as parallel sub-senses implies a symmetry that doesn't exist."
- [Outsider, 01d, Q1]: **In-paragraph elaboration with inline bolded names, reordered first sentence.** ~150 words. "Absorb the current basis of the session before changing anything. In every session this includes **workspace reading**... When the session produces or revises an artifact for use outside the workspace, it also includes **domain reading**..." Argues current first sentence hardcodes self-hosting frame.

**Structural split (sub-sections vs inline):** three-of-four against sub-sections (Minimalist, Skeptic, Outsider). Reviser lone supporter.

**Naming split (explicit named senses vs senses-named-only-implicitly):** two-for explicit naming (Reviser, Outsider); two-against (Minimalist, Skeptic). **This is a 2-2 split that crosses the model-family axis** — Claude perspectives are 1-2 against explicit naming; the Outsider tips the balance by joining the naming position, but with a structurally distinct proposal (inline bolded names) that no Claude perspective produced.

**First-sentence reorder:** two-for reorder (Reviser, Outsider; different wordings); two-for keep (Minimalist, Skeptic). Another 2-2 split that crosses the model-family axis. Outsider's reorder ("Absorb the current basis of the session") is more neutral in register than Reviser's ("Absorb what the session will reason from"); the Outsider argues the current first sentence "hardcodes a self-hosting frame; that frame is exactly what Session 011 is meant to repair" [01d, Q1].

**Shape resolution [synth].** Three-of-four against sub-sections is load-bearing. Inline prose. On naming: the Outsider's proposal — **inline bolded names without sub-sections** — is a structurally distinct third-way that honours the two Claude perspectives' anti-sub-section concerns (no false structural parallelism with §7; no precedent pressure for §2–§9 sub-sections) while preserving the Reviser's and Outsider's concern for explicit sense-names that future readers can refer to. This is the **second consecutive session where an Outsider-originated proposal resolves a 2-2 split** (WX-10-5 pattern continued — see Session 010 D-058 WX-10-5 and Q2 voice resolution). The pattern is recorded as WX-11-3-confirmed (see Assessment). Adopted: inline bolded names "workspace reading" and "domain reading"; no sub-sections. First-sentence reorder: adopt Outsider's "Absorb what the session will reason from" or equivalent that removes self-hosting-first framing — **Decide-step chooses specific wording**; the reorder honours the Outsider's external-legibility concern which is Session 008's four-way Q5 convergence.

**Load-bearing content for the revised text (four-way agreement):**

1. Both senses are distinguished.
2. Domain reading is bounded — it absorbs domain constraints (user-stated) and domain knowledge (inputs entering at session convening); it does not authorise silent import.
3. A PROMPT.md reconciliation clause is present in §1 or adjacent.
4. §1's receptive-activity character is preserved — "Its output is understanding, not artefacts."

## Q2 — Structural placement

**Three-of-four converge: in-paragraph elaboration (option a).**

- [Minimalist, 01b, Q2]: "§7 Validate was forced to split because Workspace validation and Domain validation are genuinely distinct activities... §1 Read does not bifurcate that way. Reading the workspace and reading domain knowledge are the same receptive activity targeting different sources."
- [Skeptic, 01c, Q2]: "§7 Validate was *forced* — workspace validation (no-contradictions, well-formed provenance) and domain validation (did the artefact work for its user) are genuinely different activities producing different kinds of evidence. §1 Read faces a weaker forcing function."
- [Outsider, 01d, Q2]: "In §7, the two senses are genuinely different validation operations... Sub-sections make sense there because the activity itself branches. Read is not like that. Read remains one receptive act with two objects of attention."

Three independent perspectives (one crossing the model-family axis) converge on the structural argument: §7 Validate's sub-section structure was forced by genuine activity-bifurcation; §1 Read faces a different, weaker forcing that warrants prose elaboration, not structural parallelism.

**Reviser minority [01a, Q2]:** "Treating equivalent asymmetries with equivalent structure is how readers build reliable intuitions about the kernel... The §1 length objection dissolves once domain reading is actually described."

**Load-bearing concern raised by three perspectives:** precedent-pressure risk. If §1 and §7 both carry sub-sections, §2–§9 come under implicit pressure to acquire sub-sections when any later session identifies "a second sense." [Minimalist, 01b, Q2]: "Several activities... do not obviously bifurcate into workspace/domain senses, and the kernel would be worse if each acquired sub-sections to match §1 and §7." [Skeptic, 01c, Q2]: "The kernel becomes a Russian doll." [Outsider, 01d, Q2]: "A kernel can become a graveyard of once-reasonable watchpoint fixes that were never abstract enough to deserve permanence."

**Structural resolution [synth].** Adopt in-paragraph elaboration. Reviser's parallelism concern is addressed by the inline bolded names (see Q1) — the two senses are visibly named in §1 matching the two senses visibly named in §7, without imposing parallel structural machinery. Reviser's minority dissent preserved.

## Q3 — Scope of domain reading

**Mapping to the brief's (a)–(f):**

| Sub-kind | Reviser | Minimalist | Skeptic | Outsider | Count IN |
|---|---|---|---|---|---|
| (a) User-stated constraints | IN | IN | IN | IN | 4/4 |
| (b) Agent pretrained knowledge | IN (conditional) | IN | IN (strong provenance) | OUT | 3/4 |
| (c) Perspective pretrained knowledge | IN (with channel) | IN (via brief) | OUT (category error) | OUT | 2/4 |
| (d) Explicit in-session research | IN (conditional) | OUT (not §1) | IN | IN | 3/4 |
| (e) Cited external materials | IN | IN | IN | IN | 4/4 |

**Convergences:** four-way on (a) user-stated constraints and (e) cited external materials. Three-way on (d) explicit research (Minimalist dissents — places research in a separate surveying step, not §1).

**Divergences:**

- **(c) perspective pretraining:** Three-of-four position *against* treating perspective pretraining as part of §1 Read's domain reading. The cleanest argument is the Skeptic's [01c, Q3]: "Treating perspective pretraining as 'domain reading' conflates the orchestrating agent's reading activity (before convening) with the perspectives' reasoning activity (during deliberation). These are different activities at different points in the process." Outsider independently: "Under the stance-brief rule, perspectives reason from the brief during the independent phase. So their pretraining cannot be treated as additional reading performed by those perspectives" [01d, Q3]. Minimalist positions perspective pretraining as entering via the brief, not via §1 Read [01b, Q3]: "'Domain reading' as performed by perspectives is: the brief author curated domain knowledge into the brief, and perspectives absorb it as brief content." The three positions converge: perspective pretraining is not a §1-Read activity; it enters the session through the brief (where it is already provenance-preserved).

- **(b) agent pretraining:** Three-of-four include; Outsider excludes. [Outsider, 01d, Q3]: "I do not count the orchestrating agent's pretrained knowledge as domain reading. It was not read during the session. More importantly, calling it reading would collapse two very different epistemic statuses: explicit source intake and latent model priors." This is a precision position — the Outsider wants "reading" reserved for explicit external inputs. The three Claude perspectives treat agent pretraining as something that *is* in use and therefore should be named and surfaced. Honest tension; the synthesis accepts the majority position (include) but records the Outsider's precision concern as a load-bearing dissent.

**Scope resolution [synth].** Domain reading includes:

- User-stated constraints passed in-session (four-way).
- Cited external materials the user or operator introduces (four-way).
- Explicit research the session undertakes (three-of-four; Minimalist's narrower position recorded).
- Orchestrating agent's pretrained knowledge *when it is surfaced explicitly as input* (three-of-four; Outsider's precision dissent recorded).

Domain reading does NOT include (three-of-four):

- Perspective pretraining — this is reasoning, not reading, per `multi-agent-deliberation.md` v3 §Stance Briefs. Where perspectives bring domain knowledge, they do so through the brief (which is authored at Convene-time and provenance-preserved as part of the session record).

The kernel text does not need to enumerate the (a)–(e) sub-kinds; the synthesis level enumeration is reference material for future sessions. The kernel text needs to name the two senses and require surfacing. Granular boundary decisions are better handled case-by-case by the orchestrating agent at Read/Convene, with session-record discipline.

## Q4 — Interaction with PROMPT.md's "do not import ideas" rule and `multi-agent-deliberation.md` §Stance Briefs

**Four-way convergence: reconciliation text is required in §1 or adjacent.** All four perspectives identify the tension and propose reconciliation language. The specific phrasings differ; the substance is the same.

- [Reviser, 01a, Q4]: "Naming an input as 'domain reading' IS the explicit handling. The rule isn't 'no outside inputs'; the rule is 'no silent outside inputs.'"
- [Minimalist, 01b, Q4]: "The tension is real but structural, not logical. PROMPT.md's rule targets **silent commitment**... The W1 revision is consistent with PROMPT.md as long as domain reading is **surfaced** (recorded, made visible) rather than **silently applied**."
- [Skeptic, 01c, Q4]: "Domain reading surfaces domain knowledge as an *input*: it is named, bounded, and recorded in the session brief or session record. Domain reading does not authorise the orchestrating agent or deliberation perspectives to incorporate pretrained knowledge silently into produced artefacts."
- [Outsider, 01d, Q4]: "Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step and recorded as such."

**Four-way convergence on the separation of "intake" from "commitment"** — clearest in Outsider's formulation [01d, Q4]: "Domain reading enlarges what the session may legitimately absorb before acting. It does not enlarge what the session may treat as already justified. Outside material can enter Read if it is explicit. It can shape Produce or Decide only through the recorded reasoning of the session." The Reviser, Minimalist, and Skeptic all articulate the same structure — domain reading populates inputs; workspace decisions still route through Deliberate/Decide.

**Four-way convergence on the laundering failure mode.** Each perspective names a variant of the same concrete risk: orchestrating agent encodes a pretrained intuition into the brief as "domain reading," then the deliberation treats it as given context rather than proposed option, and the decision is smuggled rather than surveyed.

- [Reviser, 01a, Q4]: "A perspective... wants a workspace-level revision... They rationalise it as emerging from 'domain reading'... But what actually happened is the perspective imported a methodology idea from pretraining."
- [Minimalist, 01b, Q4]: "The orchestrating agent has, from pretraining, a strong intuition about the answer. Rather than running an explicit surveying step that would force the intuition to compete with alternatives, the agent labels the intuition 'domain reading' and absorbs it as Read-activity context."
- [Skeptic, 01c, Q4]: "The conclusion — 'use BATNA' — was smuggled in at Read, then validated by the subsequent steps treating it as environment rather than choice." The Skeptic names this sharply as "the natural shape of the failure mode once domain reading is legitimised."
- [Outsider, 01d, Q4]: "The orchestrating agent knows, from pretraining, a standard movement or facilitation pattern. It writes a brief that already encodes that pattern, labels it 'domain reading,' and then lets perspectives deliberate over a pre-shaped solution."

**Four-way laundering convergence is the strongest single cross-model finding in this deliberation.** Four perspectives, crossing the model-family axis, independently name the same failure mode with the same structure. The revision must include reconciliation text AND the failure mode must be recorded as a new watchpoint or open issue for future sessions (Skeptic-proposed; Outsider-echoed).

**Reconciliation resolution [synth].** The revised §1 includes a clause that:

1. Surfaces domain inputs as named/recorded, not silently applied.
2. Preserves PROMPT.md's rule against silent import — the revision is consistent with PROMPT.md, not an exemption from it.
3. Separates intake from commitment — domain reading enlarges what is absorbed; it does not authorise skipping Deliberate/Decide for conclusions.

The Outsider's two-sentence formulation [01d, Q1] is the most compressed: "Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step and recorded as such." Adopted with minor tightening for kernel compression. **Decide-step finalises specific wording.**

**New open issue (proposed):** the laundering enforcement gap. Three-of-four perspectives argue that reconciliation text in §1 Read is necessary but not sufficient — enforcement requires Deliberate/Decide to re-examine domain inputs as choices rather than environment. Session 011 does not revise Deliberate or Decide; the gap is recorded as an open issue for a future session to address. See Decide-step D-062 for OI proposal.

## Q5 — G/O/K/S and the refuse-the-revision case

**G/O/K/S scoring (four-perspective):**

| Criterion | Reviser | Minimalist | Skeptic | Outsider |
|---|---|---|---|---|
| (G) Translation-to-external-frame | ✓ | ✓ | weak | ✓ |
| (O) Narrows-external-action-decision-space | partial | weak | ✗ | weak |
| (K) External-reader visibility | ✓ | ✓ | weak | ✓ |
| (S) Specific-obstacle resolution | ✓ | ✓ | marginal | ✓ |

Three-of-four score G/K/S as clearly satisfied; Skeptic scores them weakly-but-present. Four-of-four score O as weakly satisfied or unsatisfied. Under the strict "at least one criterion satisfied" reading, the revision passes four-of-four. Under a "load-bearing?" reading, three-of-four say yes; the Skeptic says no.

**Refuse-the-revision case.** All four perspectives engage it seriously. Two endorse variants (Skeptic primary; Minimalist partial); two reject (Reviser; Outsider — both with explicit engagement of the strongest form).

- [Skeptic, 01c, Q5] **primary refuse position:** "The methodology worked without it. Two external artefacts... were produced successfully... Revising to close a gap that hasn't failed is the methodology worrying about itself." Five specific arguments: methodology-worked-without-it; ratchet-to-ossification pattern; external-application-guidance belongs in separate document; §7 precedent weaker than it looks; session's choice of W1 is self-work-expanding-to-fill-external-work-gap. Includes a **falsifiability condition**: "A session attempting an external artefact is *blocked* by §1's lack of domain-reading naming — not merely slowed, but unable to proceed or producing a demonstrably worse artefact — *and* the W1-style revision would have prevented that block. If this happens, record it in that session's Assess and re-open W1 with real forcing."

- [Minimalist, 01b, Q5] **partial endorsement:** "The refuse-case is right in principle about premature crystallisation, but wrong in the specific here for three reasons. First, W1 is an *already-open* watchpoint from Session 008, deferred once, deferred again... Second, my proposed revision is 58 words, not a re-architecture... Third, the G/O/K/S check comes out three-of-four." Minimalist's position: refuse against fuller revision (sub-sections + new terminology); accept minimal revision. "The refuse-case **wins against the fuller revision** even while it loses against the minimal one."

- [Outsider, 01d, Q5] **reject-but-take-seriously:** "I take that case seriously. If the current kernel had been written abstractly enough, I would probably accept refusal. But it was not. It does not say 'understand the current basis of the work.' It says 'absorb the full current state of the workspace.' That is not neutral minimality; it is a concrete claim, and for external-domain sessions it is wrong. Refusing revision therefore means either tolerating a known falsehood at kernel level or retreating the methodology's domain-general ambition until later."

- [Reviser, 01a, Q5] **reject:** "The asymmetry is in the kernel activity itself, not in an application's elaboration. 'What does Read consume' is a first-order question about what the activity *is*. Moving that to an applications-layer document says '§1 Read means one thing, and sometimes in some applications it means a different thing that we describe elsewhere' — which is a worse read than '§1 Read has two senses, named.'"

**Necessity resolution [synth].** Adopt the revision in minimal form. Three-of-four support revision; Skeptic's refuse position is preserved as first-class dissent with its falsifiability condition recorded verbatim in Decide-step and open-issues. The Minimalist's partial-endorsement — refuse the fuller revision — is operative: the synthesis's adopted shape is closer to the minimal pole than the maximal pole (no sub-sections; inline named senses; PROMPT.md reconciliation; two paragraphs). The Reviser's fuller proposal is rejected on three-of-four structural grounds (no sub-sections); the Reviser's naming position is accommodated via inline bolded names.

## Synthesis Recommendations for Decide

1. **Adopt a kernel §1 Read revision in the form described below** (in-paragraph elaboration, inline bolded sense-names, first-sentence reorder, two paragraphs including PROMPT.md reconciliation clause). Proposed text (Decide may refine):

   > #### 1. Read
   >
   > Absorb what the session will reason from before changing anything. In every session this includes **workspace reading**: the full current state of the workspace — every file, every specification, every provenance record, and, where relevant, recent version-control history. Build a complete picture of the workspace's own state.
   >
   > When the session produces or revises an artefact intended for use outside the workspace, it also includes **domain reading**: the domain constraints the session operates under (stated by the user or operator in-session), cited external materials introduced into the session, and domain knowledge that the orchestrating agent surfaces explicitly as input to the work. Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step (per PROMPT.md). Perspective pretraining enters the session via stance briefs and perspective responses, not via §1 Read.
   >
   > This is a receptive activity. Its output is understanding, not artefacts.

   Approximately 170 words (up from ~40). Two paragraphs. Inline bolded sense-names. No sub-sections. First sentence reorders to remove the self-hosting-first framing. Includes the PROMPT.md reconciliation and the perspective-pretraining-routed-via-briefs clarification.

2. **Preserve Skeptic's refuse-the-revision position and falsifiability condition** verbatim in the decision record's Rejected Alternatives section. Skeptic's position is the null-alternative benchmark against which the revision will be read over subsequent sessions. If no external-artefact session ever surfaces a §1-silence-caused blocker, the Skeptic's position becomes the warrant for reviewing the revision's earned place.

3. **Open a new issue (OI-015) for the laundering enforcement gap.** Four-of-four convergence: reconciliation text in §1 is necessary but not sufficient; enforcement requires Deliberate/Decide to re-examine domain inputs. Session 011 does not revise Deliberate or Decide; a future session's deliberation on that gap would be kernel-revision-triggering again. Activation trigger: first post-Session-011 external-artefact session where a laundering pattern (domain input accepted as given rather than surveyed) is observed and recorded.

4. **Preserve minority positions that may become activation triggers:**
   - Outsider's strict-boundary position on agent pretraining: excluded from domain reading because "calling it reading would collapse two very different epistemic statuses." If the adopted text produces confusion in practice about what agent pretraining is within §1, the Outsider's precision becomes the revision warrant.
   - Minimalist's no-research-in-§1 position: research belongs in a surveying step, not domain reading. If the adopted text makes it unclear where mid-session research should be recorded, the Minimalist's position becomes the revision warrant.
   - Reviser's sub-section structural position: if future kernel work surfaces that the inline-names treatment is insufficient for reader comprehension across §1/§7, the Reviser's parallel-structure proposal becomes the revision warrant.

5. **Record the WX-11-3-confirmed pattern.** Second consecutive session with an Outsider-originated resolution to a 2-2 split (Session 009 Q2 applications/; Session 010 Q3 voice; Session 011 Q1 naming + first-sentence reorder). This session adds two instances rather than one: the inline-bolded-names proposal for the naming 2-2; the first-sentence reorder for the reorder 2-2. WX-10-5 monitoring continues; the pattern is load-bearing for OI-004 closure criterion 3's cross-model influence evidence base.

6. **OI-004 closure criterion status update.** Session 011 is a D-023_1-triggering deliberation (kernel modification) with non-Claude participation present. This is the **fourth required-trigger deliberation with non-Claude participation** across Sessions 005, 006, 009, and 011. Sustained-practice criterion 2 is already satisfied (3/3 from Session 009); Session 011 extends the evidence beyond the threshold. Criterion-3 data points accumulate materially: at minimum five concrete Outsider-sourced influences on adopted Session 011 content (inline-bolded-names third-way; first-sentence reorder; intake-vs-commitment framing; strict-boundary dissent preserved; kernel-level-vs-procedural reconciliation-text placement). Cumulative criterion-3 data points across Sessions 005–011: **approximately twenty-four** (nineteen through Session 010 per D-059; five added in Session 011 from synthesis count; exact figure fixed by Decide).

## Limitations (required content)

Per `multi-agent-deliberation.md` v3 Limitations, the following hold:

- Three Claude-subagent perspectives share a model family; shared training produces shared blind spots; the four-way laundering convergence at Q4 is therefore strong evidence but should be treated as convergence across three correlated perspectives plus one cross-model perspective, not as four fully-independent data points.
- Intra-Claude-family perspective mixing was not used; all three Claude subagents are Claude Opus 4.7. Capability-band differences did not surface as a factor.
- The synthesis step is single-agent (Claude Opus 4.7 orchestrator). Synthesizer conventions (citation, `[synth]` markers, dissent preservation, quote-over-paraphrase for load-bearing claims) are applied but not externally audited in-session. Session 012's audit will examine fidelity.
- The Outsider's participation depends on convener fidelity for verbatim reproduction of `codex exec` output; the end-of-stream duplicate in `01d-perspective-outsider.md` is preserved as characteristic of codex exec stdout (matches Sessions 005–010 pattern) rather than edited out.
- One Outsider in one session is less evidence for OI-004 narrowing than its presence suggests; the cross-lineage influence accumulates over sustained practice, as specified in v3 Closure Criteria. The fourth required-trigger deliberation with non-Claude participation extends the sustained-practice record beyond criterion 2's threshold.

## Cross-Model Honesty Notes (for Q6 of Tier 2)

`cross_model: true` stands for this session. Evidence:

- **Invocation transcript.** The Outsider's raw output is committed verbatim from `codex exec` stdout, including CLI banner: `OpenAI Codex v0.121.0 (research preview)`, `model: gpt-5.4`, `provider: openai`, `approval: never`, `sandbox: read-only`, `reasoning effort: xhigh`, `reasoning summaries: none`, OpenAI session id `019da943-2c45-7f30-bab8-ce303aba09db`. The banner is not producible by a Claude subagent.
- **CLI invocation.** `cat /tmp/session-011-outsider-brief.md | codex exec --sandbox read-only > /tmp/session-011-outsider-raw.txt 2>&1`, executed in the same parallel Bash/Agent batch as the three Claude subagent launches.
- **Output character.** The Outsider produced four concrete Outsider-unique positions: (1) the first-sentence reorder ("Absorb the current basis of the session") that no Claude perspective produced; (2) the inline-bolded-names proposal that is a structurally distinct third-way to the sub-sections-vs-inline-prose axis; (3) the strict-boundary position on agent pretraining (exclude); (4) the "intake vs commitment" framing — "Domain reading enlarges what the session may legitimately absorb before acting. It does not enlarge what the session may treat as already justified." These are not synthesizer-inducible lexical echoes.
- **End-of-stream duplicate.** Preserved verbatim; consistent with Sessions 005–010 codex exec output pattern.
- **Convergence-divergence pattern.** The Outsider aligns with Minimalist+Skeptic on no-sub-sections; with Reviser on explicit naming; against all three Claude perspectives on agent-pretraining inclusion; convergent with all three on the laundering failure mode. The convergence pattern is not along a Claude-vs-non-Claude axis; the Outsider sides with different subsets of Claude perspectives on different questions — the signature of a genuinely distinct-training participant.

End of synthesis.
