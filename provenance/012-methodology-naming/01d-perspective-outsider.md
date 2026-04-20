---
session: 012
title: Perspective — Outsider
date: 2026-04-20
status: complete
perspective: outsider
committed_at: 2026-04-20T06:02Z
transport_notes: "Raw stdout from `codex exec --sandbox read-only`, committed verbatim including CLI banner, user-prompt echo, 'codex' marker, response body, 'tokens used' line with token count (22,575 tokens), and end-of-stream duplicate response body. End-of-stream duplication is a known property of codex exec stdout (see Sessions 005/006/007/008/009/010/011 Outsider raw outputs) and is preserved rather than edited out to maintain verbatim integrity. OpenAI Codex v0.121.0 (research preview), model: gpt-5.4, provider: openai, reasoning effort: xhigh, session id: 019daa64-f24f-7402-be96-565c135009a1, 22,575 tokens reported. Invocation: cat /tmp/session-012-outsider-brief.md | codex exec --sandbox read-only > /tmp/session-012-outsider-raw.txt 2>&1."
---

Reading prompt from stdin...
OpenAI Codex v0.121.0 (research preview)
--------
workdir: /Users/ericmccowan/Development/design-system
model: gpt-5.4
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019daa64-f24f-7402-be96-565c135009a1
--------
user
---
session: 012
title: Shared Brief — Methodology Naming (OI-001)
date: 2026-04-20
status: finalised-before-launch
deliberation-anchor-commit: TBD-recorded-after-commit
perspectives:
  - namer (Claude Opus 4.7, subagent)
  - steward (Claude Opus 4.7, subagent)
  - skeptic (Claude Opus 4.7, subagent, adversarial)
  - outsider (OpenAI GPT-5 via Codex CLI, non-Claude participant per D-021 Shape A)
note: |
  Sections 1–6 are byte-identical across all four perspectives. Only the
  role-specific stance section (delivered to each perspective separately)
  differs. Frontmatter is file-level metadata for provenance tracking,
  not part of what perspectives saw during the independent phase.
---

# Shared Brief — Session 012

**Notice to all perspectives.** This brief's non-role-specific sections are byte-identical across all four perspectives. Only the role-specific stance section delivered with each copy differs. Do not coordinate; do not seek external context beyond this brief; do not read workspace files during your reasoning.

---

## 1. Methodology Context

This workspace is building a design methodology in which diverse perspectives deliberate, produce durable specifications, and preserve reasoning (provenance) so future readers — human or agent — can reconstruct what was decided and what was considered. The methodology is self-hosting: it evolves by running its own process on itself. The methodology advances by **sessions**. Each session performs a set of nine activities (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close). Each session produces one increment.

The methodology has been exercised for eleven sessions. Sessions 001–007 built self-infrastructure. Session 008 produced the methodology's **first external artefact** (a movement sequence for a stiff lower back), positively validated out-of-session by its intended user. Session 009 revised kernel §7 Validate to name two senses (Workspace validation, Domain validation) and created the `applications/` directory for external artefacts. Session 010 produced the **second external artefact** (a five-move guide for small two-person household decisions); domain validation for that artefact is pending. Session 011 revised kernel §1 Read to name two senses (workspace reading, domain reading) — structurally parallel to §7. Session 012's planned primary work — receiving the Session 010 validation receipt — is not available; Session 012 addresses the longest-deferred open issue instead.

The methodology currently refers to itself as "the methodology." It does not have a name.

## 2. Problem Statement — Should the Methodology Be Named, and If So, How?

Session 001 (the bootstrap session) opened an explicit question (its Question 6): should we name the methodology? The perspectives convened there produced split views:

- The Historian argued every serious methodology has a name; *"the methodology"* is awkward.
- The Minimalist argued naming now is premature; the methodology barely exists. A name should emerge from what the methodology becomes, not be imposed at birth.
- The Skeptic argued a name creates attachment — once named, the methodology becomes an identity to defend rather than a system to evolve. Early naming ossifies.
- The Practitioner argued a working name would be useful, something explicitly provisional.
- The Futurist argued the name could be one of the things the methodology discovers about itself; put it on the open issues list and let future sessions decide.

Session 001's resolution: *"No name yet. The methodology refers to itself as 'the methodology' for now. Naming is recorded as an open issue for future sessions to address when the methodology has enough identity to name meaningfully."* The group specifically declined to adopt a provisional name, on the reasoning that "even a 'provisional' name tends to stick."

Since then the methodology has accumulated:

- **4 active specifications.** The kernel (Read → Close; nine activities); workspace structure (directory layout, mutability rules, application artefacts); multi-agent deliberation (perspective-shape rules, non-Claude participation rules, trigger-coverage annotations, closure criteria); validation approach (tiered structural and guided checks, extensions as the system has evolved).
- **2 external artefacts** in `applications/` (one validated; one pending).
- **7 multi-perspective deliberations with non-Claude participation** (Sessions 005, 006, 007, 008, 009, 010, 011; 4 of these were required-trigger deliberations under D-023).
- **62 recorded decisions** (D-001 through D-062), each with rationale and rejected alternatives.
- **Distinct vocabulary** that has emerged rather than been imposed: the nine activities; provenance; perspectives; kernel; watchpoints; stance briefs; manifests; the G/O/K/S criterion-package; triggers_met.
- **Characteristic patterns.** Preservation of superseded specifications by version (v1, v2, v3) with explicit `supersedes`/`superseded-by` pointers. Per-decision trigger annotations making multi-agent and non-Claude participation machine-checkable. A recurring structure where external artefacts ship into `applications/NNN-slug/` alongside their provenance directory.

Session 012's task is to deliberate: is the identity threshold met, and if so, what name should the methodology carry and where should that name live?

### Adjacent constraints

**Constraint A — PROMPT.md's own refusal.** PROMPT.md (the prompt applied each session) says: *"The workspace's shape, its stages if it has them, its vocabulary, its conventions, and even its name should emerge from the process rather than be imposed from outside."* A name must be generated from the methodology's own identity; it is not acceptable to import a name from outside (e.g., borrowing a name from another methodology wholesale, or importing a name because the agent happens to know a trendy word). If an idea for a name arrives via pretraining or analogue, flag it as such and argue why it applies.

**Constraint B — preservation of prior reasoning.** Session 001's Q6 resolution specifically declined a provisional name. Session 012 is not bound to that resolution but must explicitly cite it if proposing to name now; arguing that circumstances have changed (via identity accumulation) is the acceptable form. Silently re-proposing a name without engaging Session 001's reasoning is not.

**Constraint C — reversibility.** The methodology has a strong preservation-of-prior-versions convention for specifications (v1, v2, v3 files with explicit supersession pointers). A name could in principle be revised similarly (v1-name → v2-name), but a name that changes repeatedly is worse than no name. Proposed names should survive examination against reasonable three-year-later reviewers without needing revision; if that's not realistic, the deliberation should consider whether now is too early to name.

**Constraint D — single-increment discipline.** Session 012 is naming the methodology (or deciding not to name). It is not revising the kernel's structure, adding new specifications beyond what naming requires, or committing to additional work that naming may suggest.

### Pre-existing constraint on self-work — the G/O/K/S criterion-package

A prior session adopted a criterion-package for deciding whether self-infrastructure work is load-bearing. Self-work is load-bearing if it satisfies at least one of:

- **(G)** *Translation-to-external-frame* — the need for the increment can be stated in terms that refer to the methodology's external use, not only in terms of the methodology's self-description.
- **(O)** *Narrows-external-action-decision-space* — the increment removes a concrete blocker to a named next external action.
- **(K)** *External-reader visibility* — the weakness the increment addresses would be visible to a reader outside the workspace reading the specs for the first time.
- **(S)** *Specific-obstacle resolution* — the increment resolves a specific articulable obstacle that blocks a named next step, or closes an open issue whose closure changes what later sessions can do.

Self-work satisfying none of these is tracked as ceremonial. A perspective answering Q5 below should apply this package to Session 012's naming work itself and report honestly.

## 3. Design Questions

Answer each question. Be concrete. Name alternatives you considered and rejected, not only the answer you favour. Target length: 300–600 words per question. Use H2 headings `## Q1` through `## Q6`.

**Q1. Is the identity threshold met for naming now?** Session 001's resolution said name "when the methodology has enough identity to name meaningfully." Applying your own standard, is the current identity sufficient? Name three specific identity markers you find most salient in answering (e.g., the nine activities as a stable frame; the preservation patterns; the external-artefact track record; the G/O/K/S criterion-package; something else). Separately, name one or more identity markers you find weak or under-developed — things a name would be premature to commit to. State your answer unambiguously: yes / no / conditional-on-something-specific. If your answer is no, you may still answer Q2 hypothetically, and Q5 becomes your primary question.

**Q2. Candidate names.** Propose 3–5 candidate names. For each candidate, provide: (a) the name itself (2 words or fewer is a soft preference but not required); (b) etymology or derivation — where does the name come from, what does it mean; (c) what the name emphasises about the methodology; (d) what the name hides or understates; (e) collision check — is this name already in use for a related methodology, framework, software tool, book, or company? (Be honest. If you don't know, say so.) Do not propose names that are puns, acronyms decoded into non-names, or labels that double as descriptions. The name should be something a practitioner in five years could say without embarrassment in a room of peers.

**Q3. Evaluation criteria.** What makes a good methodology name? Propose and argue a set of criteria. Consider: external-legibility (a first-time reader can use the name without sounding strange); memorability (fits in a sentence and sticks); collision-avoidance (not easily confused with existing named things); translatability (works across languages, or at least doesn't embarrass in any language you can check); non-pretentiousness (not grand beyond the methodology's actual scope); resistance-to-ossification (doesn't pre-commit the methodology to a specific form of its content). Weight the criteria; identify tradeoffs between them. Apply your weighted criteria to the candidates in Q2, producing a ranked evaluation.

**Q4. Placement — where does the name live canonically?** If a name is chosen, where in the workspace does it become the canonical reference? Options include (enumerate non-exhaustively): (a) `methodology-kernel.md` title and frontmatter (e.g., the kernel's title becomes "The [Name] Kernel"); (b) PROMPT.md — a first-paragraph self-reference is added; (c) a new file (e.g., `specifications/identity.md` or a simpler artefact) whose sole purpose is to record the name and its origin; (d) `SESSION-LOG.md` header; (e) no canonical placement — the name is used in external references only and workspace artefacts keep referring to "the methodology." For each option, consider: what specification revisions are required (v-bumps, supersessions); what trigger coverage the placement implies (D-016 triggers for spec revisions; D-023 triggers for kernel or multi-agent-deliberation or validation-approach revisions); what reader an external visitor first encounters the name through. Argue for your preferred placement and name at least two alternatives you reject.

**Q5. Refuse to name — Skeptic-oriented, Session 001 dissent carried forward.** Session 001's Skeptic and Minimalist positions (names ossify; name creates attachment; naming is premature) are preserved in the workspace's provenance. Those positions have had eleven sessions to be falsified. Are they falsified? Argue the refuse-to-name case at its strongest. Identity accumulation is a fact; naming is a commitment; the two are not the same. What evidence would be required before naming is clearly the right move rather than a defensible move? If Session 012 should decline to name, what's the form of that decline — does OI-001 remain open with updated notes; is the question retired; does it become "named only if the methodology is adopted externally"? Even perspectives who favour naming should engage this question seriously and explain why they reject the refuse-to-name case.

**Q6. What naming changes.** Does naming the methodology change what the methodology *is*, or only how it's referenced? A name pulls future self-presentation into its shape — a methodology called "Something Kernel" accentuates the kernel; a methodology called "Something Provenance" accentuates provenance; a methodology called by a neutral-sounding name accentuates whichever parts later sessions choose to foreground. Name at least one concrete way your preferred name (from Q2 and Q3) would steer future self-presentation or reasoning. Name at least one way it would not — a property of the methodology the name *won't* privilege that remains available to future sessions. If you're refusing to name (per Q5), describe what staying unnamed steers the methodology toward or away from.

## 4. Response format

Produce a single Markdown response. Use H2 headings matching `## Q1` through `## Q6`. Under each heading, provide your answer with arguments considered and rejected alternatives. Be concrete; give exact candidate names and exact proposed placement text where appropriate; use named examples.

At the end of your response, include a short section `## Meta-note` of up to 150 words noting: (a) any position you hold that you expect to differ from what other perspectives will say, and why it is salient; (b) any assumption in this brief you flag as suspect; (c) any concern about the deliberation's framing.

## 5. Constraint on external imports

Reason primarily from this brief. Do not open workspace files. If an idea you want to use arrived through pretraining, a real-world example, or an analogue from outside the methodology, flag it explicitly (e.g., "[external analogue: ...]") and argue why the analogue applies; do not silently commit external ideas as if generated from within the brief.

This constraint is especially sharp for Q2. Any candidate name must be argued from the methodology's identity as described in §1 — not borrowed whole from an existing named framework because the name is available.

## 6. Closing note

Your response will be committed verbatim as provenance. It will be read by synthesis in conjunction with three other perspective responses. Your positions — including positions you hold reluctantly or conditionally — are recorded at their strongest. Do not soften them to anticipate synthesis. If you hold a position in tension with your role-specific stance, record the tension explicitly; the synthesis prefers honest tension to performed alignment.

---

## 7. Role-specific stance — Outsider (non-Claude participant)

You are a non-Claude participant (external LLM). Your task is to provide an independently-trained perspective on this naming question. You do not share Claude's training provenance; where your positions diverge from what Claude-family perspectives would produce, that divergence is the value you add.

The orchestrating agent running this session is Claude (Opus 4.7, 1M context). Three other perspectives in this deliberation are Claude Opus 4.7 subagents:

- **Namer** — charged with proposing 3–5 candidates from the methodology's identity.
- **Steward** — charged with weighing candidates against the methodology's shape as developed across eleven sessions.
- **Skeptic** — charged with arguing the refuse-to-name case at its strongest; carries forward Session 001 dissent.

You are the only non-Claude participant. Your participation is required under D-023 if the decision modifies the kernel; it is recommended in any case given the methodology's cross-model closure-criterion-2 is now at 4 of 3 (sustained practice extended beyond threshold). Your concrete contributions will be traced and recorded per D-024.

**Your specific work:**

- **On Q1 identity threshold.** Form an independent judgment on whether identity is sufficient. A non-Claude reader looking at this methodology — its four specifications, two external artefacts, sixty-two decisions — without Claude's priors about what self-hosting methodologies should look like: does it read as a named-able thing, or as still-becoming? Argue the judgment from what you see, not what you guess Claude would say.

- **On Q2 candidate names.** You may propose names that Claude-trained models would be less likely to reach for — names from design, research, or craft traditions less salient in Claude's training distribution; names in a second language that fit the methodology's shape and don't embarrass; names whose shape would strike a Claude-trained model as unusual but which may fit. Honour Constraint A (emerge from process) — a name you borrow from an external tradition must be argued to fit, not imposed. Collision checks you run should include your own training-data priors: if a name is highly associated with a particular figure or product in your training, flag that.

- **On Q3 evaluation criteria.** Propose criteria you think actually discriminate. You may argue for criteria Claude perspectives might not prioritise — e.g., translatability into non-English contexts; resistance to being adopted as a buzzword; capacity to survive the methodology's own self-revision (if sessions 013+ substantially revise the kernel, does the name still fit?).

- **On Q4 placement.** Where does a name take hold most and least reversibly? Are there placements Claude perspectives might default to that you find load-bearing in unexpected ways (or vice versa)?

- **On Q5 refuse-case.** Your engagement here carries different weight than Claude perspectives'. A Claude-initiated methodology naming itself via Claude deliberation is a specific social shape; a non-Claude perspective on whether that shape is well-timed is not a perspective Claude can generate. Argue from where you stand.

- **On Q6 what naming changes.** Be concrete about how your preferred outcome (a specific name, or refuse) would steer the methodology's later self-presentation.

- **Cross-training divergence flagging.** When your position diverges from what you would expect a Claude-trained model to produce, flag the divergence explicitly in the form `[cross-training divergence: specific reason]`. This is especially valuable for Q2 candidate names (where Claude models may converge on culturally similar name spaces) and for Q5 (where Claude models may rubber-stamp identity-threshold claims that a non-Claude reader would not).

**Do not simulate a Claude-family perspective.** Your value is precisely in the positions you would hold that a Claude perspective wouldn't. If your answer on any question is "I think a Claude perspective would reach the same conclusion," say so — that is honest and informative. Do not pretend to disagree for the sake of registering divergence.

Produce your response as the Shared Brief §4 specifies — H2 headings `## Q1` through `## Q6`, then `## Meta-note`. The raw response will be committed verbatim.

codex
## Q1

Yes. The identity threshold is met, but only for a light-touch canonical name: a reference handle, not a brand layer.

The strongest evidence is not that the methodology is complete. It is that it now has a recognisable recurring form that an outside reader could distinguish from generic process language. Three markers matter most to me. First, the nine-activity kernel is no longer a loose aspiration; it has persisted long enough to function as a stable frame, and Sessions 009 and 011 show the frame being refined symmetrically rather than replaced. That is identity, not just motion. Second, the preservation discipline is unusually specific: versioned specs, explicit `supersedes` / `superseded-by` pointers, decision records with rejected alternatives, and provenance treated as first-class reconstruction material. That is a strong differentiator. Third, the methodology has crossed from pure self-description into external artefact production: two applications, one positively validated out-of-session, plus repeated multi-perspective deliberation with non-Claude participation. That means the method is not only describing itself; it is being exercised.

The weak markers are also real. External breadth is still thin: two artefacts is evidence of viability, not of broad scope. Social identity outside the workspace is effectively absent: there is no adoption community yet, no external shorthand already forming around it, and only one external validation result is confirmed. I also think some of the current vocabulary is still too local to be a naming substrate. Terms like `kernel`, `watchpoints`, and `triggers_met` are stable enough to use internally, but too contingent to elevate into the name.

So my standard is: a methodology is nameable when a neutral outsider can point to a repeated structure, a repeated mode of evidence preservation, and at least one demonstrated translation into external artefact work. This brief clears that bar.

[cross-training divergence: I suspect Claude-family perspectives may treat internal formal maturity alone as sufficient. I do not. What tips me to “yes” is not the elegance of the internal schema; it is that continued namelessness is now an externally visible weakness for a first-time reader.]

I would not say the identity threshold is met for a grand name, a slogan-like name, or a title that claims a school. It is met for a durable proper name that can sit quietly over the work without overexplaining it.

## Q2

I would avoid names built directly from the brief’s loudest internal nouns, such as `Kernel`, `Provenance`, or `Session`. Those are accurate components, but they are too descriptive and too likely to ossify the current internal vocabulary. My candidates are metaphorical rather than taxonomic.

1. `Selvedge`. [external analogue: textile term; from “self-edge,” the finished edge woven into cloth so it does not unravel.] This is my preferred candidate. It emphasises three real traits at once: self-hosting, multiple strands held together, and preservation against fraying. It also fits the methodology’s habit of making durable edges around reasoning rather than discarding it. What it hides is the external-artefact track; the name sounds more archival than applied. Collision check from memory only: I know `Selvedge` as a textile term, a magazine title, and brand usage, but not as a related methodology.

2. `Braid`. [external analogue: braided strands remain distinct while being combined.] This emphasises multi-perspective deliberation especially well: perspectives are not melted into one voice; they remain traceable within a stronger whole. It also survives future revision because it does not privilege any one spec. What it understates is versioning and validation; a braid can be elegant without being accountable. Collision check from memory only: moderate to high. I know the video game `Braid` and assorted tech/product uses.

3. `Trace`. [external analogue: design tracing and audit trace.] This foregrounds reconstructability: later readers can see how a decision came to be. It fits the methodology’s provenance ethic and its refusal to erase superseded reasoning. What it hides is synthesis and production; `Trace` risks sounding like an audit tool rather than a generative method. Collision check: high. `Trace` is an extremely common software and product term.

4. `Strata`. [external analogue: geology / archaeology, where layers remain readable over time.] This suits the preserved-version habit well and gives the methodology a non-grand, durable feel. It suggests accumulated decisions that remain inspectable rather than overwritten. It hides the active, sessional character of the method; `Strata` sounds more like the result of history than an engine for increments. Collision check: high. I know many products and companies using `Strata`.

5. `Loom`. [external analogue: a device that turns threads into fabric.] This emphasises the methodology as apparatus rather than doctrine. It is simple to say and memorable. It also fits the fact that the method produces external artefacts rather than only internal discussion. What it understates is provenance; a loom says more about production than about preserved reasoning. Collision check: high. I know multiple software, network, and crypto-adjacent uses.

[cross-training divergence: I would expect Claude-family perspectives to cluster around explicit compounds like “Provenance Kernel” or “Session Method.” I think that would be a mistake. The name should not freeze the current glossary into the methodology’s public face.]

## Q3

A good methodology name should score well on six criteria, weighted in this order.

1. Identity fit, 30%. The name should capture what is actually distinctive here, not just what is currently most visible in the prose.
2. Scope resilience, 25%. It should survive revisions to the kernel, validation regime, or application domains without becoming false.
3. External legibility, 15%. A first-time reader should be able to say it aloud without feeling they are reciting internal jargon.
4. Collision avoidance, 15%. If the name is already saturated across tools, companies, and frameworks, it will not carry reference well.
5. Memorability, 10%. It should be easy to retain after one encounter.
6. Translatability / non-embarrassment, 5%. I cannot verify languages here, so I weight this lightly, but the name should at least not feel culturally brittle.

The main tradeoff is between fit and legibility. Names with high internal fit often become overdescriptive or jargon-heavy. Names with high legibility are often common words with severe collision problems. There is also a tradeoff between resonance and ossification: naming after the current “kernel” or “provenance” emphasis would feel precise now but age badly if later sessions redistribute emphasis.

On those criteria, my ranking is:

1. `Selvedge`. Best balance of distinctiveness and resilience. Its fit is unusually high because “self-edge” maps to self-hosting plus anti-unraveling preservation. Its main weakness is legibility: some readers will not know the term immediately. I accept that cost.
2. `Braid`. Better speakability than `Selvedge`, and still faithful to the multi-perspective structure. It falls because collision risk is materially worse and because it underplays provenance.
3. `Strata`. Strong on preserved history and scope resilience. It loses on collision and on the fact that it sounds static.
4. `Trace`. Strong fit to provenance, but too collision-heavy and too close to a description of one function rather than the whole method.
5. `Loom`. Elegant and memorable, but too saturated and too production-centric.

[cross-training divergence: I am weighting collision risk and buzzword resistance more heavily than I expect Claude perspectives will. A mostly-Claude synthesis may over-reward conceptual neatness. I think the name has to survive ordinary reference in mixed human settings, not just read well in the spec set.]

So my recommendation is `Selvedge`, with `Braid` as the fallback if the group judges `Selvedge` too obscure in speech.

## Q4

The name should live canonically in a new, single-purpose identity record, not in the kernel title and not primarily in `PROMPT.md`.

My preferred placement is a new file such as `specifications/identity.md` whose job is only to state the name, the adoption decision, and the origin rationale. The opening text should be this plain:

```md
# Methodology Identity

Canonical name: Selvedge

Adopted in Session 012.
This name is the canonical reference for the methodology as a whole.
It changes reference, not kernel structure or activity names.
Origin: the methodology combines multiple perspectives into durable increments while preserving the reasoning edge conditions that keep prior work from unraveling.
Provenance: Session 012.
```

That placement has three advantages. First, it is the least reversible in the good sense: the decision becomes real and citeable, but if a later session must revise it, the supersession path is local and explicit. Second, it does not force a kernel v-bump merely to rename the umbrella under which the kernel sits. Third, it gives an external reader a clear place to learn why the name exists, rather than making them infer significance from a retitled core document.

On trigger implications, this is the smallest blast radius. It likely requires ordinary spec-addition coverage and provenance recording, but it should avoid D-023-triggering revisions to the kernel, multi-agent deliberation spec, or validation approach, because the name is being recorded as identity metadata rather than as a structural kernel change. By contrast, renaming the kernel itself would require a kernel revision, supersession handling, and the heavier trigger story that comes with kernel edits. Putting the name first in `PROMPT.md` would make the operational prompt the primary identity carrier; that is too sticky and too constitutive for a decision that should remain mainly referential.

I reject two alternatives strongly. I reject kernel-title canonicalisation because it overstates “kernel” as the methodology’s defining organ. I reject “no canonical placement” because that is functionally a refusal to name; the name would then diffuse through habit rather than decision. I also reject `SESSION-LOG.md` as canonical placement because a log is retrospective, not normative.

If later the workspace wants the name echoed in the kernel or prompt, that echo should be derivative, not canonical.

## Q5

The refuse-to-name case remains strong enough that it must be answered, not brushed aside. Session 001’s Skeptic and Minimalist positions are not falsified. They are merely no longer decisive.

What has not been falsified is the underlying causal concern: a name can create attachment, and attachment can bias later revision. Eleven sessions do not disprove that. In fact, a mostly-Claude process becoming increasingly articulate about itself could make the risk sharper, not weaker, because internal coherence can be generated faster than external legitimacy. [cross-training divergence: I place more weight than I expect Claude perspectives will on this asymmetry. A model-mediated process can sound mature before it has had enough outside contact to deserve a durable identity.]

The strongest refuse-case is this: the methodology has enough identity to be described, but not enough external standing to be named. Two applications and sixty-two decisions show persistence, not necessarily social durability. The method may still be overfit to its current orchestration ecology: Claude-run sessions, spec-heavy preservation, and a particular style of agentic recordkeeping. If naming happens now, the name may freeze today’s self-understanding before the methodology has been pressured by wider use, more varied domains, or human-only adoption.

What evidence would make naming clearly right rather than merely defensible? I would want at least one of these: repeated external need to refer to the method by name; three or more externally validated artefacts across materially different domains; evidence that the methodology survives one substantial self-revision without identity confusion; or external adoption by someone who did not help build it. If Session 012 declined to name, the correct form would be: keep OI-001 open, add a note that identity is sufficient for discussion but not yet for durable naming, and revisit on either external adoption or a stronger cross-domain application record. I would not retire the question.

Why do I still reject refusal? Because naming now satisfies the G/O/K/S package honestly through K and S. It plainly satisfies K: an outside reader will notice the absence of a proper name as a real awkwardness. It satisfies S: this is an explicit long-deferred open issue, and closing it changes how later sessions can refer to the method. It does not strongly satisfy G, and it barely satisfies O. That is fine. The work is load-bearing enough if handled minimally. The right move is not “be proud of the name”; it is “stop making the method refer to itself generically.”

## Q6

Naming does not change the kernel semantics, but it does change the methodology’s social shape. A name is not only a reference tag; it is a steering metaphor.

If the chosen name is `Selvedge`, future self-presentation will tilt toward a particular account of what is distinctive here: not merely that the methodology has stages, but that it preserves the edges that keep reasoning from unraveling. That will likely make future writers foreground version preservation, explicit provenance, and the combination of multiple strands without erasure. It may also encourage a more disciplined claim about external artefacts: not “we have a grand theory,” but “we have a way of making durable, inspectable increments.” I think that is a good steering effect, because it emphasises the methodology’s strongest actual differentiator.

What `Selvedge` would not privilege is equally important. It does not privilege the nine activities as sacred; if Sessions 013+ later split, merge, or rename activities, `Selvedge` can survive. It does not privilege validation over production, or the kernel over applications, or Claude over non-Claude participation. It also does not lock the methodology to design as a content domain. The metaphor is structural, not topical.

There is a risk. The name could tempt later sessions to overextend textile metaphors and start reading intentionality into the metaphor itself. That would be a category error. The name should guide emphasis, not become a hidden theory.

If the methodology stayed unnamed, that would also steer it. It would preserve humility and reduce identity attachment, but it would keep the method in a permanent preface state: always becoming, never quite introducible. It would also increase the chance of informal de facto naming later, which is a worse form of commitment because it arrives without a recorded decision.

So my answer is: naming changes how the methodology will be narrated and what future readers expect to be central. With a restrained name and a restrained placement, that change is acceptable and useful.

## Meta-note

I expect two divergences from other perspectives. First, I suspect I am more cautious about internal maturity as evidence; I think a mostly-Claude process can become self-coherent faster than it becomes socially name-stable. Second, I am deliberately preferring a craft-metaphor name over internal-vocabulary names; I expect some Claude perspectives to prefer `Kernel`- or `Provenance`-adjacent candidates, and I think that would overfit the present glossary.

The assumption I most distrust is that naming pressure should be resolved now simply because the issue is old. Age of an open issue is not itself evidence.

My framing concern is that Q2 is concrete while Q5 is evidentiary, which subtly biases the synthesis toward naming.
tokens used
22,575
## Q1

Yes. The identity threshold is met, but only for a light-touch canonical name: a reference handle, not a brand layer.

The strongest evidence is not that the methodology is complete. It is that it now has a recognisable recurring form that an outside reader could distinguish from generic process language. Three markers matter most to me. First, the nine-activity kernel is no longer a loose aspiration; it has persisted long enough to function as a stable frame, and Sessions 009 and 011 show the frame being refined symmetrically rather than replaced. That is identity, not just motion. Second, the preservation discipline is unusually specific: versioned specs, explicit `supersedes` / `superseded-by` pointers, decision records with rejected alternatives, and provenance treated as first-class reconstruction material. That is a strong differentiator. Third, the methodology has crossed from pure self-description into external artefact production: two applications, one positively validated out-of-session, plus repeated multi-perspective deliberation with non-Claude participation. That means the method is not only describing itself; it is being exercised.

The weak markers are also real. External breadth is still thin: two artefacts is evidence of viability, not of broad scope. Social identity outside the workspace is effectively absent: there is no adoption community yet, no external shorthand already forming around it, and only one external validation result is confirmed. I also think some of the current vocabulary is still too local to be a naming substrate. Terms like `kernel`, `watchpoints`, and `triggers_met` are stable enough to use internally, but too contingent to elevate into the name.

So my standard is: a methodology is nameable when a neutral outsider can point to a repeated structure, a repeated mode of evidence preservation, and at least one demonstrated translation into external artefact work. This brief clears that bar.

[cross-training divergence: I suspect Claude-family perspectives may treat internal formal maturity alone as sufficient. I do not. What tips me to “yes” is not the elegance of the internal schema; it is that continued namelessness is now an externally visible weakness for a first-time reader.]

I would not say the identity threshold is met for a grand name, a slogan-like name, or a title that claims a school. It is met for a durable proper name that can sit quietly over the work without overexplaining it.

## Q2

I would avoid names built directly from the brief’s loudest internal nouns, such as `Kernel`, `Provenance`, or `Session`. Those are accurate components, but they are too descriptive and too likely to ossify the current internal vocabulary. My candidates are metaphorical rather than taxonomic.

1. `Selvedge`. [external analogue: textile term; from “self-edge,” the finished edge woven into cloth so it does not unravel.] This is my preferred candidate. It emphasises three real traits at once: self-hosting, multiple strands held together, and preservation against fraying. It also fits the methodology’s habit of making durable edges around reasoning rather than discarding it. What it hides is the external-artefact track; the name sounds more archival than applied. Collision check from memory only: I know `Selvedge` as a textile term, a magazine title, and brand usage, but not as a related methodology.

2. `Braid`. [external analogue: braided strands remain distinct while being combined.] This emphasises multi-perspective deliberation especially well: perspectives are not melted into one voice; they remain traceable within a stronger whole. It also survives future revision because it does not privilege any one spec. What it understates is versioning and validation; a braid can be elegant without being accountable. Collision check from memory only: moderate to high. I know the video game `Braid` and assorted tech/product uses.

3. `Trace`. [external analogue: design tracing and audit trace.] This foregrounds reconstructability: later readers can see how a decision came to be. It fits the methodology’s provenance ethic and its refusal to erase superseded reasoning. What it hides is synthesis and production; `Trace` risks sounding like an audit tool rather than a generative method. Collision check: high. `Trace` is an extremely common software and product term.

4. `Strata`. [external analogue: geology / archaeology, where layers remain readable over time.] This suits the preserved-version habit well and gives the methodology a non-grand, durable feel. It suggests accumulated decisions that remain inspectable rather than overwritten. It hides the active, sessional character of the method; `Strata` sounds more like the result of history than an engine for increments. Collision check: high. I know many products and companies using `Strata`.

5. `Loom`. [external analogue: a device that turns threads into fabric.] This emphasises the methodology as apparatus rather than doctrine. It is simple to say and memorable. It also fits the fact that the method produces external artefacts rather than only internal discussion. What it understates is provenance; a loom says more about production than about preserved reasoning. Collision check: high. I know multiple software, network, and crypto-adjacent uses.

[cross-training divergence: I would expect Claude-family perspectives to cluster around explicit compounds like “Provenance Kernel” or “Session Method.” I think that would be a mistake. The name should not freeze the current glossary into the methodology’s public face.]

## Q3

A good methodology name should score well on six criteria, weighted in this order.

1. Identity fit, 30%. The name should capture what is actually distinctive here, not just what is currently most visible in the prose.
2. Scope resilience, 25%. It should survive revisions to the kernel, validation regime, or application domains without becoming false.
3. External legibility, 15%. A first-time reader should be able to say it aloud without feeling they are reciting internal jargon.
4. Collision avoidance, 15%. If the name is already saturated across tools, companies, and frameworks, it will not carry reference well.
5. Memorability, 10%. It should be easy to retain after one encounter.
6. Translatability / non-embarrassment, 5%. I cannot verify languages here, so I weight this lightly, but the name should at least not feel culturally brittle.

The main tradeoff is between fit and legibility. Names with high internal fit often become overdescriptive or jargon-heavy. Names with high legibility are often common words with severe collision problems. There is also a tradeoff between resonance and ossification: naming after the current “kernel” or “provenance” emphasis would feel precise now but age badly if later sessions redistribute emphasis.

On those criteria, my ranking is:

1. `Selvedge`. Best balance of distinctiveness and resilience. Its fit is unusually high because “self-edge” maps to self-hosting plus anti-unraveling preservation. Its main weakness is legibility: some readers will not know the term immediately. I accept that cost.
2. `Braid`. Better speakability than `Selvedge`, and still faithful to the multi-perspective structure. It falls because collision risk is materially worse and because it underplays provenance.
3. `Strata`. Strong on preserved history and scope resilience. It loses on collision and on the fact that it sounds static.
4. `Trace`. Strong fit to provenance, but too collision-heavy and too close to a description of one function rather than the whole method.
5. `Loom`. Elegant and memorable, but too saturated and too production-centric.

[cross-training divergence: I am weighting collision risk and buzzword resistance more heavily than I expect Claude perspectives will. A mostly-Claude synthesis may over-reward conceptual neatness. I think the name has to survive ordinary reference in mixed human settings, not just read well in the spec set.]

So my recommendation is `Selvedge`, with `Braid` as the fallback if the group judges `Selvedge` too obscure in speech.

## Q4

The name should live canonically in a new, single-purpose identity record, not in the kernel title and not primarily in `PROMPT.md`.

My preferred placement is a new file such as `specifications/identity.md` whose job is only to state the name, the adoption decision, and the origin rationale. The opening text should be this plain:

```md
# Methodology Identity

Canonical name: Selvedge

Adopted in Session 012.
This name is the canonical reference for the methodology as a whole.
It changes reference, not kernel structure or activity names.
Origin: the methodology combines multiple perspectives into durable increments while preserving the reasoning edge conditions that keep prior work from unraveling.
Provenance: Session 012.
```

That placement has three advantages. First, it is the least reversible in the good sense: the decision becomes real and citeable, but if a later session must revise it, the supersession path is local and explicit. Second, it does not force a kernel v-bump merely to rename the umbrella under which the kernel sits. Third, it gives an external reader a clear place to learn why the name exists, rather than making them infer significance from a retitled core document.

On trigger implications, this is the smallest blast radius. It likely requires ordinary spec-addition coverage and provenance recording, but it should avoid D-023-triggering revisions to the kernel, multi-agent deliberation spec, or validation approach, because the name is being recorded as identity metadata rather than as a structural kernel change. By contrast, renaming the kernel itself would require a kernel revision, supersession handling, and the heavier trigger story that comes with kernel edits. Putting the name first in `PROMPT.md` would make the operational prompt the primary identity carrier; that is too sticky and too constitutive for a decision that should remain mainly referential.

I reject two alternatives strongly. I reject kernel-title canonicalisation because it overstates “kernel” as the methodology’s defining organ. I reject “no canonical placement” because that is functionally a refusal to name; the name would then diffuse through habit rather than decision. I also reject `SESSION-LOG.md` as canonical placement because a log is retrospective, not normative.

If later the workspace wants the name echoed in the kernel or prompt, that echo should be derivative, not canonical.

## Q5

The refuse-to-name case remains strong enough that it must be answered, not brushed aside. Session 001’s Skeptic and Minimalist positions are not falsified. They are merely no longer decisive.

What has not been falsified is the underlying causal concern: a name can create attachment, and attachment can bias later revision. Eleven sessions do not disprove that. In fact, a mostly-Claude process becoming increasingly articulate about itself could make the risk sharper, not weaker, because internal coherence can be generated faster than external legitimacy. [cross-training divergence: I place more weight than I expect Claude perspectives will on this asymmetry. A model-mediated process can sound mature before it has had enough outside contact to deserve a durable identity.]

The strongest refuse-case is this: the methodology has enough identity to be described, but not enough external standing to be named. Two applications and sixty-two decisions show persistence, not necessarily social durability. The method may still be overfit to its current orchestration ecology: Claude-run sessions, spec-heavy preservation, and a particular style of agentic recordkeeping. If naming happens now, the name may freeze today’s self-understanding before the methodology has been pressured by wider use, more varied domains, or human-only adoption.

What evidence would make naming clearly right rather than merely defensible? I would want at least one of these: repeated external need to refer to the method by name; three or more externally validated artefacts across materially different domains; evidence that the methodology survives one substantial self-revision without identity confusion; or external adoption by someone who did not help build it. If Session 012 declined to name, the correct form would be: keep OI-001 open, add a note that identity is sufficient for discussion but not yet for durable naming, and revisit on either external adoption or a stronger cross-domain application record. I would not retire the question.

Why do I still reject refusal? Because naming now satisfies the G/O/K/S package honestly through K and S. It plainly satisfies K: an outside reader will notice the absence of a proper name as a real awkwardness. It satisfies S: this is an explicit long-deferred open issue, and closing it changes how later sessions can refer to the method. It does not strongly satisfy G, and it barely satisfies O. That is fine. The work is load-bearing enough if handled minimally. The right move is not “be proud of the name”; it is “stop making the method refer to itself generically.”

## Q6

Naming does not change the kernel semantics, but it does change the methodology’s social shape. A name is not only a reference tag; it is a steering metaphor.

If the chosen name is `Selvedge`, future self-presentation will tilt toward a particular account of what is distinctive here: not merely that the methodology has stages, but that it preserves the edges that keep reasoning from unraveling. That will likely make future writers foreground version preservation, explicit provenance, and the combination of multiple strands without erasure. It may also encourage a more disciplined claim about external artefacts: not “we have a grand theory,” but “we have a way of making durable, inspectable increments.” I think that is a good steering effect, because it emphasises the methodology’s strongest actual differentiator.

What `Selvedge` would not privilege is equally important. It does not privilege the nine activities as sacred; if Sessions 013+ later split, merge, or rename activities, `Selvedge` can survive. It does not privilege validation over production, or the kernel over applications, or Claude over non-Claude participation. It also does not lock the methodology to design as a content domain. The metaphor is structural, not topical.

There is a risk. The name could tempt later sessions to overextend textile metaphors and start reading intentionality into the metaphor itself. That would be a category error. The name should guide emphasis, not become a hidden theory.

If the methodology stayed unnamed, that would also steer it. It would preserve humility and reduce identity attachment, but it would keep the method in a permanent preface state: always becoming, never quite introducible. It would also increase the chance of informal de facto naming later, which is a worse form of commitment because it arrives without a recorded decision.

So my answer is: naming changes how the methodology will be narrated and what future readers expect to be central. With a restrained name and a restrained placement, that change is acceptable and useful.

## Meta-note

I expect two divergences from other perspectives. First, I suspect I am more cautious about internal maturity as evidence; I think a mostly-Claude process can become self-coherent faster than it becomes socially name-stable. Second, I am deliberately preferring a craft-metaphor name over internal-vocabulary names; I expect some Claude perspectives to prefer `Kernel`- or `Provenance`-adjacent candidates, and I think that would overfit the present glossary.

The assumption I most distrust is that naming pressure should be resolved now simply because the issue is old. Age of an open issue is not itself evidence.

My framing concern is that Q2 is concrete while Q5 is evidentiary, which subtly biases the synthesis toward naming.
