---
session: 009
title: Shared Brief — Kernel Validate & Workspace-Structure Revisions (W4 + W2)
date: 2026-04-19
status: finalised-before-launch
deliberation-anchor-commit: 3260f0bf08b96c806cef3ef5dd618781988d27f0
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

# Shared Brief — Session 009

**Notice to all perspectives.** This brief's non-role-specific sections are byte-identical across all four perspectives. Only the role-specific stance section delivered with each copy differs. Do not coordinate; do not seek external context beyond this brief; do not read workspace files during your reasoning.

---

## 1. Methodology Context

This workspace is building a design methodology in which diverse perspectives deliberate, produce durable specifications, and preserve reasoning (provenance) so future readers — human or agent — can reconstruct what was decided and what was considered. The methodology is self-hosting: it evolves by running its own process on itself. The methodology advances by **sessions**. Each session performs a set of nine activities (Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close). Each session produces one increment.

The methodology has been exercised for eight sessions. Sessions 001–007 built self-infrastructure. Session 008 produced the methodology's **first external artefact** (a movement sequence for a stiff lower back), executed by Branch B of a selection mechanism (user-ratified agent proposal). Session 009 opened with the user's out-of-session Validate report on that artefact — strongly positive, no modifications requested.

Session 008's Produce activity recorded four stress-test watchpoints (W1–W4) observing where specification text strained when applied outside the workspace's native domain. These were recorded, not acted upon, per a prior decision (D-047) committing Session 008 to no mid-session spec revisions.

**The current session is Session 009. Its ratified work-product is a deliberation on two of those watchpoint findings.** The user has ratified a narrowed scope: W2 and W4 only. W1 (Read activity) and W3 (self-referential phrasing) are deferred.

## 2. Problem Statement — Revise Kernel §Validate (W4) and Workspace-Structure (W2)

Two observations from Session 008's external application are in scope. Each is stated here in plain-language terms, followed by the verbatim current specification text the perspective is reasoning about.

### W4 — Kernel Validate activity has two senses in active use

The methodology-kernel's Validate activity, as currently written, describes internal consistency checking: that specifications do not contradict each other, that the workspace matches its specifications, that provenance is well-formed. This is the sense in which `tools/validate.sh` operates.

Session 008's external artefact required a **different** sense of Validate: asking the user, who has the actual problem the artefact was designed for, whether the design functioned in use. The user reported back at Session 009 open ("stiffness lifted immediately; all moves do-able; phrase-like recall; no modifications"). This was a **domain-native test** of the artefact in its target domain, not an internal-consistency check of how the artefact sits within the workspace. Both happened; the kernel currently names only the first.

**Current kernel §Validate (verbatim):**

> #### 7. Validate
>
> Check that the workspace is internally consistent:
>
> - New specifications don't contradict existing ones
> - Specifications describe the workspace as it actually is
> - Provenance records are complete and well-formed
> - Open issues reflect the actual state of uncertainty
>
> If validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.

The question is whether this text needs to distinguish the two senses, combine them, add a second activity, or do something else.

### W2 — Workspace structure does not name external work-products

Session 008's external artefact — the movement sequence — was placed at `provenance/008-first-external-application/artefact-morning-unfurl.md`. Placement choices:

1. *External artefacts live inside their producing session's provenance directory,* alongside deliberation files, decisions, and manifests. This is what Session 008 did.
2. *External artefacts live in a separate top-level directory* (e.g., `applications/`) referenced from the session that produced them.
3. Some other arrangement.

Additionally, Session 008 surfaced a **tooling sub-finding**: `tools/validate.sh` hard-codes the path `02-decisions.md` for checks 14 and 15. Session 008's initial attempt to number the artefact file (e.g., `02-artefact-morning-unfurl.md` with decisions shifting to `03-decisions.md`) would have silently bypassed those checks. The artefact was renamed to a non-numbered filename as a workaround. The workaround is recorded in provenance but is not a clean solution.

**Current workspace-structure §provenance (verbatim, partial):**

> ### provenance/
>
> Contains the historical reasoning records. Organized by session:
>
> ```
> /provenance/
>   /001-genesis/
>     00-survey.md
>     01-deliberation.md
>     02-decisions.md
>   /002-[title]/
>     ...
> ```
>
> Each session's provenance is a numbered directory. Files within are numbered for reading order. All provenance files use Markdown with YAML frontmatter:
> [frontmatter block]
> Provenance records are **immutable** once the session closes. Errors or retractions are recorded in subsequent sessions, not by editing past records.

**Current workspace-structure §Additional directories (verbatim):**

> ### Additional directories
>
> New top-level directories may be created by future sessions when the work demands them (e.g., `implementations/`, `examples/`). Any new directory should be documented by updating this specification.

The question is how external artefacts should be located and how (if at all) the tool should be updated.

### Scope note on D-023 classification

A prior session's close (Session 008) described both revisions as "D-023-triggering" requiring non-Claude participation. This was imprecise. D-023 (in `multi-agent-deliberation.md` v3) covers four categories: kernel modification, multi-agent-deliberation revision, validation-approach revision (Tier-2-touching), and OI-004 state change. Workspace-structure revisions are **not** in that list — they trigger multi-agent deliberation under D-016 but do not require non-Claude participation under D-023. W4 (kernel) is correctly D-023.1; W2 (workspace-structure) is not D-023. Because W4 is in scope, the whole deliberation gets non-Claude participation, and this brief records the correction for future reference.

### Pre-existing constraint on self-work — the G/O/K/S criterion-package

A prior session adopted a criterion-package for deciding whether self-infrastructure work is load-bearing. Self-work is load-bearing iff it satisfies at least one of:

- **(G)** *Translation-to-external-frame* — the need for the increment can be stated in terms that refer to the methodology's external use, not only in terms of the methodology's self-description.
- **(O)** *Narrows-external-action-decision-space* — the increment removes a concrete blocker to a named next external action.
- **(K)** *External-reader visibility* — the weakness the increment addresses would be visible to a reader outside the workspace reading the specs for the first time.
- **(S)** *Specific-obstacle resolution* — the increment resolves a specific articulable obstacle that blocks a named next step, or closes an open issue whose closure changes what later sessions can do.

Self-work satisfying none of these is tracked as ceremonial. A perspective answering Q5 below should apply this package to the Session 009 work itself and report honestly.

## 3. Design Questions

Answer each question. Be concrete. Name alternatives you considered and rejected, not only the answer you favour. Target length: 300–600 words per question. Use H2 headings `## Q1` through `## Q5`.

**Q1. Kernel Validate revision (W4).** Propose specific text to replace or amend the current kernel §Validate. Your proposal should address the two-senses observation: how should the text treat internal-consistency checking and domain-native testing of external artefacts? Options include (but are not limited to): two sub-activities under one Validate; two distinct activities in the kernel's activity list; one activity with explicit sense-disambiguation; minimal change with a pointer to an elaboration specification; leave kernel as-is and record the distinction elsewhere. Argue for your preferred option and against at least two alternatives. If your preferred option changes the kernel's activity list length or sequence, say so explicitly and argue the consequence.

**Q2. Workspace-structure revision (W2).** Propose specific text (new section, revised section, or additions to existing sections) for `workspace-structure.md`. Your proposal should name where external artefacts live, how they are referenced, and what — if anything — distinguishes them from session-internal provenance artefacts. Options include (but are not limited to): new top-level `applications/` directory; canonicalize the session-provenance-embedded pattern Session 008 used; a hybrid with a reference-from-provenance pointer. Argue for your preferred option and against at least two alternatives. If your proposal creates or relocates files that already exist (the Session 008 artefact is one such), explicitly address what happens to those files: move, copy, symlink, leave in place with a forward pointer, or something else.

**Q3. Tooling sub-finding.** Propose how (or whether) `tools/validate.sh` should be updated to address the hard-coded `02-decisions.md` path. Options include: leave tool as-is (the non-numbered-filename workaround is acceptable); parameterise the decisions-file path per session; expand the tool to search for a file matching a naming pattern; pair the tool update with the workspace-structure revision so the workspace-structure specification governs the tool's search semantics. Argue your preferred option. If the tool update is out-of-scope for Session 009 entirely, argue why, and name the session that should take it up and its trigger.

**Q4. Integration.** The two proposed revisions interact with other specifications. Identify at least one interaction — between Q1 and Q2, between either revision and `multi-agent-deliberation.md`, between either revision and `validation-approach.md`, or between either revision and open issues other than OI-004 and OI-009. For each interaction you name, state whether it requires a coordinated change (bundled in Session 009) or creates a new watchpoint for a later session. An interaction you believe is benign should still be named — "benign" is a conclusion, not an absence of content.

**Q5. Necessity and scope.** Apply the G/O/K/S criterion-package (brief §2) to the Session 009 work as you are proposing it. Does your proposal satisfy any of G, O, K, S? Which? Honestly. If your proposal satisfies none, recommend which parts to drop. If your proposal satisfies some criteria but contains extensions that satisfy none of the four, recommend which extensions to drop. The purpose of this question is to prevent Session 009 from inflating beyond its warranted scope; the session's ratified direction is narrow (W2 + W4 only), and scope-drift is the most likely failure mode.

## 4. Response format

Produce a single Markdown response. Use H2 headings matching `## Q1` through `## Q5`. Under each heading, provide your answer with arguments considered and rejected alternatives. Be concrete; quote proposed specification text where you are proposing text; use named examples.

At the end of your response, include a short section `## Meta-note` of up to 150 words noting: (a) any position you hold that you expect to differ from what other perspectives will say, and why it is salient; (b) any assumption in this brief you flag as suspect; (c) any concern about the deliberation's framing.

## 5. Constraint on external imports

Reason primarily from this brief. Do not open workspace files. If an idea you want to use arrived through pretraining, a real-world example, or an analogue from outside the methodology, flag it explicitly (e.g., "[external analogue: ...]") and argue why the analogue applies; do not silently commit external ideas as if generated from within the brief.

## 6. Closing note

Your response will be committed verbatim as provenance. It will be read by synthesis in conjunction with three other perspective responses. Your positions — including positions you hold reluctantly or conditionally — are recorded at their strongest. Do not soften them to anticipate synthesis. If you hold a position in tension with your role-specific stance, record the tension explicitly; the synthesis prefers honest tension to performed alignment.
