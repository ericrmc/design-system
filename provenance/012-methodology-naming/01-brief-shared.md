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
