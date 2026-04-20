---
session: 011
title: Shared Brief — Kernel §Read Revision (W1)
date: 2026-04-20
status: finalised-before-launch
deliberation-anchor-commit: TBD-recorded-after-commit
perspectives:
  - reviser (Claude Opus 4.7, subagent)
  - minimalist (Claude Opus 4.7, subagent)
  - skeptic (Claude Opus 4.7, subagent, adversarial)
  - outsider (OpenAI GPT-5 via Codex CLI, non-Claude participant per D-021 Shape A)
note: |
  Sections 1–6 are byte-identical across all four perspectives. Only the
  role-specific stance section (delivered to each perspective separately)
  differs. Frontmatter is file-level metadata for provenance tracking,
  not part of what perspectives saw during the independent phase.
---

# Shared Brief — Session 011

**Notice to all perspectives.** This brief's non-role-specific sections are byte-identical across all four perspectives. Only the role-specific stance section delivered with each copy differs. Do not coordinate; do not seek external context beyond this brief; do not read workspace files during your reasoning.

---

## 1. Methodology Context

This workspace is building a design methodology in which diverse perspectives deliberate, produce durable specifications, and preserve reasoning (provenance) so future readers — human or agent — can reconstruct what was decided and what was considered. The methodology is self-hosting: it evolves by running its own process on itself. The methodology advances by **sessions**. Each session performs a set of nine activities (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close). Each session produces one increment.

The methodology has been exercised for ten sessions. Sessions 001–007 built self-infrastructure. Session 008 produced the methodology's **first external artefact** (a movement sequence for a stiff lower back), positively validated out-of-session by the user at Session 009 open. Session 009 revised two of Session 008's four stress-test watchpoint findings (W2 workspace structure — created the `applications/` directory — and W4 kernel Validate — named two senses, Workspace and Domain validation). Session 010 produced the **second external artefact** (a five-move guide for small two-person household decisions). Session 011's planned primary work — receiving the domain-validation receipt on Session 010's artefact — is not available; Session 011's substantive increment instead addresses Session 008's remaining open watchpoint, **W1: kernel Read activity for external domains.**

## 2. Problem Statement — Revise Kernel §1 Read (W1)

The methodology-kernel's §1 Read activity, as currently written, describes absorbing the workspace's state: every file, every specification, every provenance record. This works for the self-hosting case, where the thing a session is reasoning about is the methodology's own artefacts.

Sessions 008 and 010 produced artefacts for external domains (movement sequence; household decision process). In each, the Read activity drew on **two** distinct sources:

1. The **workspace state** in the sense the kernel currently names — existing specifications, prior provenance, open issues, tools, SESSION-LOG. The methodology's self-knowledge.
2. **Domain knowledge** not held in the workspace — user-stated constraints passed in-session, and pretrained knowledge the orchestrating agent or the deliberation's perspectives brought to the problem. For movement, that was yoga/physio/mobility knowledge. For household decisions, that was decision-theory and relationship-communication knowledge. None of this is in the workspace; none of it is the workspace's own self-knowledge.

The kernel names only the first source. A reader applying the kernel to an external domain would need to reinterpret §1 Read to include the second source. Session 008 (D-051 W1 finding) proposed a candidate revision:

> "For work outside this workspace's self-hosting scope, Read also includes absorbing the domain constraints the session operates under and the domain knowledge available to the perspectives."

The proposal was deferred to a future session. This session is that future session.

**Current kernel §1 Read (verbatim):**

> #### 1. Read
>
> Absorb the full current state of the workspace. Every file, every specification, every provenance record. If the workspace is under version control, understand the recent history. Build a complete picture before changing anything.
>
> This is a receptive activity. Its output is understanding, not artifacts.

The kernel's §7 Validate section, revised in Session 009 (D-053) as a structural precedent, now names two senses (Workspace validation, Domain validation) using a parallel-subsection pattern. The precedent is directly adjacent. It is not binding on §1 Read.

### Session 009 §7 Validate precedent (verbatim, for reference)

> #### 7. Validate
>
> Validate the session's output at each level on which it makes claims. Two senses apply.
>
> **Workspace validation** applies to every session. Check that:
> - New specifications don't contradict existing ones
> - Specifications describe the workspace as it actually is
> - Provenance records are complete and well-formed
> - Open issues reflect the actual state of uncertainty
>
> **Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.
>
> If either validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.

### Adjacent constraint — brief-contained reasoning for deliberation perspectives

`multi-agent-deliberation.md` v3 §Stance Briefs specifies: "Perspectives reason from the brief; they do not read workspace files or use other tools during the independent phase. This keeps the deliberation reproducible and prevents spurious disagreement from divergent reading."

This is a strong constraint on when and how *perspectives* Read. It implies a distinction between **session-level Read** (performed by the orchestrating agent before convening) and **perspective-level Read** (what each perspective does during the independent phase, which is strictly what the brief contains). Any revision to kernel §1 Read must be consistent with this constraint or explicitly alter it.

### Adjacent constraint — PROMPT.md §Rules that hold across applications

> Do not import ideas from outside the process. If an insight arrived through reading something unrelated, a conversation with a human, or your own pretraining, introduce it as an input to an explicit surveying or hypothesising step rather than committing it directly. The value of this methodology is that its artefacts are traceable to the reasoning that produced them.

This rule forbids silent import of outside ideas into workspace decisions. Domain knowledge that informs an external artefact is by construction from outside the workspace. Any revision to kernel §1 Read must be consistent with this rule — or must explicitly carve an exception for external-artefact domain knowledge with reasoning.

### Scope of this brief

This brief's scope is **W1 only**. Session 011 is not revising any other kernel activity, any other specification, or any other watchpoint. Single-increment discipline per D-058. A perspective may note interactions with other specifications, but proposing additional revisions is out-of-scope.

### Pre-existing constraint on self-work — the G/O/K/S criterion-package

A prior session (D-048, Session 007) adopted a criterion-package for deciding whether self-infrastructure work is load-bearing. Self-work is load-bearing iff it satisfies at least one of:

- **(G)** *Translation-to-external-frame* — the need for the increment can be stated in terms that refer to the methodology's external use, not only in terms of the methodology's self-description.
- **(O)** *Narrows-external-action-decision-space* — the increment removes a concrete blocker to a named next external action.
- **(K)** *External-reader visibility* — the weakness the increment addresses would be visible to a reader outside the workspace reading the specs for the first time.
- **(S)** *Specific-obstacle resolution* — the increment resolves a specific articulable obstacle that blocks a named next step, or closes an open issue whose closure changes what later sessions can do.

Self-work satisfying none of these is tracked as ceremonial. A perspective answering Q5 below should apply this package to the Session 011 work itself and report honestly.

## 3. Design Questions

Answer each question. Be concrete. Name alternatives you considered and rejected, not only the answer you favour. Target length: 300–600 words per question. Use H2 headings `## Q1` through `## Q5`.

**Q1. Revised text for kernel §1 Read, and naming of senses.** Propose the specific text that should replace or amend the current kernel §1 Read. Quote your proposal in full. Your proposal should address the two-senses observation: how should the text treat the workspace-reading sense (already named) and the domain-reading sense (not named)? Also: how are the two senses named? Options include (but are not limited to): "Workspace reading" and "Domain reading" (parallel to §7 Validate's "Workspace validation" and "Domain validation"); inline prose that distinguishes them without sub-headings; a single unified sense with enlarged scope; some other naming. Argue for your preferred option and against at least two alternatives. If your proposal changes the kernel's §1 length materially or reorders its existing sentences, say so explicitly.

**Q2. Structural placement.** Within §1 Read, should the two-sense treatment be (a) an in-paragraph elaboration in the existing §1 prose; (b) two parallel sub-sections under §1 (mirroring Session 009's §7 Validate treatment); (c) a pointer from §1 to an elaboration specification; (d) some other structure? The Session 009 §7 Validate precedent is adjacent but not binding. Argue the precedent-following case AND the precedent-departing case, then state your preferred option. Attend to: length of §1 relative to other activities (currently the shortest at ~40 words); whether §1 adding sub-sections sets an implicit precedent for other activities adding sub-sections; whether the external/self-hosting asymmetry should be visible or de-emphasised in the kernel.

**Q3. Scope of "domain reading."** What exactly is domain reading? Possibilities include: (a) user-stated constraints passed in the session's opening messages; (b) pretrained knowledge the orchestrating agent brings; (c) pretrained knowledge the deliberation perspectives bring (which is delivered via the brief, not read from anywhere); (d) explicit research during the session (web searches, document lookup); (e) external reference materials the user or operator cites; (f) all of the above. Where are the boundaries? For each inclusion you propose, name how the methodology keeps provenance of what was read — PROMPT.md's "do not silently import" rule forbids unflagged external inputs. If you propose that perspective pretraining counts as domain reading, explain how that reconciles with `multi-agent-deliberation.md` v3's "perspectives reason from the brief" constraint.

**Q4. Interaction with PROMPT.md's "do not import ideas from outside the process" rule and with `multi-agent-deliberation.md` §Stance Briefs.** PROMPT.md requires that outside ideas be introduced as explicit surveying/hypothesising steps, not silently committed. The Stance Briefs section requires perspectives to reason from the brief. Taken together, the methodology's existing text expresses a strong preference: **outside inputs are suspicious by default and must be surfaced.** The W1 revision proposes to name domain reading as a legitimate Read activity — which introduces external inputs at an earlier, broader step. Does this reconcile with PROMPT.md's rule cleanly, does it create tension, or does it require a carve-out? Propose the explicit reconciliation text (either within §1 Read or by pointer elsewhere). Name at least one concrete failure mode the carve-out could produce (e.g., a session uses "domain reading" to launder a conclusion that should have gone through a surveying step).

**Q5. Necessity and scope — G/O/K/S, and the refuse-the-revision case.** Apply the G/O/K/S criterion-package (brief §2) to the Session 011 revision as you are proposing it in Q1–Q4. Which criteria does it satisfy? Be honest. Second part: argue the **refuse-the-revision case.** What's the strongest argument that W1 should not be addressed by kernel revision at all — that it belongs in a separate external-application-guidance document, or that the kernel should remain minimal and external-domain methodology is a subsequent work the methodology hasn't committed to? A perspective whose role is adversarial should lean into this; other perspectives should engage it seriously and explain why they reject it (if they do).

## 4. Response format

Produce a single Markdown response. Use H2 headings matching `## Q1` through `## Q5`. Under each heading, provide your answer with arguments considered and rejected alternatives. Be concrete; quote proposed specification text where you are proposing text; use named examples.

At the end of your response, include a short section `## Meta-note` of up to 150 words noting: (a) any position you hold that you expect to differ from what other perspectives will say, and why it is salient; (b) any assumption in this brief you flag as suspect; (c) any concern about the deliberation's framing.

## 5. Constraint on external imports

Reason primarily from this brief. Do not open workspace files. If an idea you want to use arrived through pretraining, a real-world example, or an analogue from outside the methodology, flag it explicitly (e.g., "[external analogue: ...]") and argue why the analogue applies; do not silently commit external ideas as if generated from within the brief.

## 6. Closing note

Your response will be committed verbatim as provenance. It will be read by synthesis in conjunction with three other perspective responses. Your positions — including positions you hold reluctantly or conditionally — are recorded at their strongest. Do not soften them to anticipate synthesis. If you hold a position in tension with your role-specific stance, record the tension explicitly; the synthesis prefers honest tension to performed alignment.
