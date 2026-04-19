---
session: 009
title: Reviser Perspective — Kernel Validate & Workspace-Structure Revisions
date: 2026-04-19
status: complete
perspective: reviser
committed_at: 2026-04-19
---

## Q1

I propose splitting the current §Validate into **two sub-activities under one heading**, with explicit named senses. The kernel's activity count stays at nine; the sequence stays intact. Replace the current §7 with the following verbatim text:

> #### 7. Validate
>
> Validate has two senses. Both apply when a session produces an external artefact; only the first applies when a session produces only self-infrastructure.
>
> **7a. Internal validation.** Check that the workspace is internally consistent:
>
> - New specifications don't contradict existing ones
> - Specifications describe the workspace as it actually is
> - Provenance records are complete and well-formed
> - Open issues reflect the actual state of uncertainty
>
> **7b. Domain validation.** When a session produces an external artefact, check that the artefact functions in its target domain: the party with the problem the artefact was designed for reports whether the design worked in use. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.
>
> If either validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.

**Why this over alternatives.**

*Rejected: two distinct numbered activities (e.g., 7. Validate-internal, 8. Validate-domain).* This inflates the kernel's activity list from nine to ten and implies equal weight in every session. Most sessions produce no external artefact; a tenth activity that is N/A by default is worse than a sub-activity marked conditional.

*Rejected: one activity with a pointer to an elaboration specification.* Hiding the disambiguation in a pointer defers the reader's problem. The kernel is the document a first-time reader consults; if two senses are in active use, the kernel should name both. Pointers are for depth, not for basic disambiguation.

*Rejected: minimal change (add one sentence: "Domain testing of external artefacts is also a form of validation").* This preserves ambiguity about whether the user-report in Session 009 was a separate activity or part of 7 as written. The Reviser's default is to eliminate ambiguity in normative text, not smooth it over.

*Rejected: leave kernel as-is, record distinction elsewhere.* The distinction was exercised in Session 009 and will be exercised again every time an external artefact issues. Recurring distinctions belong in the kernel.

**Consequence of the chosen form.** The kernel's activity-count remains nine, preserving references in `multi-agent-deliberation.md` and `validation-approach.md` that cite "the nine activities." The sub-activity notation (7a/7b) signals internally that the pair occupies one slot. The conditional phrasing ("When a session produces an external artefact") makes the asymmetry normative rather than accidental: self-infrastructure sessions skip 7b without apology; external-artefact sessions owe both.

## Q2

I propose a **new top-level `applications/` directory** as the canonical location for external artefacts, with a forward-pointer from the producing session's provenance directory. Replace the current `workspace-structure.md` §Additional directories with the following verbatim text, and insert a new §applications before it:

> ### applications/
>
> Contains external artefacts — specifications, sequences, templates, or other work-products the methodology has produced for use outside the workspace. Organized by session of origin:
>
> ```
> /applications/
>   /008-morning-unfurl/
>     artefact.md
>   /NNN-[slug]/
>     artefact.md
> ```
>
> Each external artefact lives in a directory named `NNN-[slug]` where NNN is the session of origin and slug is the artefact's short name. The artefact file itself is named `artefact.md` when there is one; multiple-file artefacts use descriptive filenames. The producing session's provenance directory contains a forward-pointer file `external-artefact.md` naming the path under `applications/`.
>
> External artefacts are **mutable** — they may be revised by subsequent sessions in response to domain validation (kernel §7b). Revisions are recorded in the revising session's provenance; the artefact file itself records its last-revised session in frontmatter.
>
> ### Additional directories
>
> New top-level directories may be created by future sessions when the work demands them. Any new directory should be documented by updating this specification.

**Handling the Session 008 artefact.** Move `provenance/008-first-external-application/artefact-morning-unfurl.md` to `applications/008-morning-unfurl/artefact.md`. Leave a forward-pointer file `provenance/008-first-external-application/external-artefact.md` with contents: `This session's external artefact is at applications/008-morning-unfurl/artefact.md. Moved in Session 009 per D-[N].` Do **not** symlink (symlinks cross-cut the workspace's Markdown/frontmatter model and are invisible in most rendering). Do **not** copy (two copies of a mutable artefact is a synchronisation hazard). Do **not** leave in place (the whole point of this revision is canonical location).

**Why this over alternatives.**

*Rejected: canonicalize session-provenance-embedded (what Session 008 did).* Provenance is immutable; external artefacts are mutable. Putting mutable artefacts inside immutable directories is a contradiction the workspace will pay for the first time an artefact is revised.

*Rejected: hybrid with artefact in provenance plus pointer elsewhere.* Ambiguity about canonical location is exactly what the Reviser's stance rejects. A hybrid asks every future reader which copy is authoritative.

*Rejected: no top-level directory, artefact path decided per-session.* This guarantees inconsistency. Session 008 put the artefact under provenance; Session 014 might put it under `outputs/`; neither knows of the other without coordination overhead.

## Q3

**Pair the tool update with the workspace-structure revision.** Update `tools/validate.sh` in Session 009 to replace hard-coded `02-decisions.md` with a pattern match. Proposed behaviour: the tool searches each session's provenance directory for any file whose filename matches `NN-decisions.md` (where NN is a two-digit number) and treats that as the decisions file. If zero or multiple matches are found, the tool fails with a descriptive error.

The fix is small, it closes the silent-bypass hazard Session 008 surfaced, and it belongs with the workspace-structure revision because the latter licenses non-`02` numbering implicitly by moving artefacts out of provenance (making provenance numbering more stable) and because the workspace-structure specification should govern the tool's search semantics, not the tool's bash.

**Proposed tool change (conceptual):**

> Checks 14 and 15 previously operated on the hard-coded path `02-decisions.md`. They now operate on the result of a glob matching `[0-9][0-9]-decisions.md` within the session directory. Zero matches or multiple matches cause validation failure with a descriptive error message.

**Why not defer.** The workaround (non-numbered artefact filenames) is load-bearing: it silently prevents future sessions from tripping the checks. A specification whose tool requires an unwritten filename convention to function is a specification with a hidden dependency. Hidden dependencies are where silent failures live. Fixing this in Session 009 costs maybe ten lines of bash. Deferring costs future-session cognitive tax every time a session considers its provenance layout.

**Why not a bigger fix.** I do not propose parameterising all hard-coded paths now. The sub-finding is about one specific path that was exercised in use. Wider tool redesign is a separate concern; Session 009 should narrow.

## Q4

**Interaction: Q1 (kernel §7b) and `validation-approach.md`.** The `validation-approach.md` specification describes how validation is *performed* — what the tool checks, what a reviewer does. Introducing sub-activity 7b means `validation-approach.md` now has a gap: it describes internal-consistency validation but not domain validation. This is a **coordinated change** — `validation-approach.md` should gain a section on domain validation in Session 009 (short, naming who does it, when, and what counts as a report), because leaving the kernel to reference a sense that the validation-approach spec omits creates exactly the ambiguity the Reviser's stance rejects. The section can be brief; it need not be comprehensive.

**Interaction: Q2 (applications/ directory) and `multi-agent-deliberation.md`.** Moving external artefacts out of provenance and making them mutable has no direct bearing on deliberation procedure. The deliberation spec governs how perspectives convene and how synthesis produces decisions; it is indifferent to where the synthesised artefacts subsequently live. **Benign** — no change needed. Naming this explicitly matters because a future reader might wonder whether D-023 categories need updating to cover applications/-touching revisions; they do not, because D-023 is about what triggers non-Claude participation, not about file locations.

**Interaction: Q1 sub-activity 7b and open issues.** A domain-validation report can be negative ("artefact did not work") as easily as positive. The kernel text I proposed says "the receiving session records the report and decides whether it triggers revision." This implies a decision-branch that does not currently exist in any open issue or procedure. This creates a **new watchpoint** for a later session: "How does a session triage a domain-validation report that requests revision to an external artefact — is the revision in-session or does it trigger a new session?" I recommend logging this as a Session 009 watchpoint rather than resolving it now; Session 009 has no negative report to test against, and writing procedure for a case we have not encountered is how specifications drift.

**Interaction: Q3 tool update and existing provenance.** Session 001–008 provenance all use `02-decisions.md`. The glob pattern matches `02-decisions.md` exactly, so existing provenance passes unchanged. **Benign**, but worth stating: the tool change is non-breaking for all prior sessions.

## Q5

**Applying G/O/K/S.**

**Q1 (kernel §7b).** Satisfies **G** and **K**. The increment's need can be stated externally: "the methodology produces external artefacts; the kernel must name the check that asks whether the artefact worked." The weakness is visible to an external reader, who reads the current §Validate and cannot tell whether asking a user "did it work?" is a kernel activity or something else. Satisfies **S** — the specific obstacle is Session 009's own difficulty classifying the user's out-of-session Validate report against a kernel activity that nominally covers only internal consistency. **Keep.**

**Q2 (applications/ directory).** Satisfies **G**, **O**, and **K**. External frame: the methodology produces external artefacts; a specification silent about where they live is a gap a first-time external reader sees immediately. Narrows next-action decision-space: a named Session 010 action ("produce the next external artefact") has a canonical destination. External-reader visibility: the current §Additional directories mentions `implementations/` and `examples/` as hypothetical but has no slot for what Session 008 actually produced. **Keep.**

**Q3 (tool update).** Satisfies **S**. The specific obstacle is the silent-bypass hazard Session 008 worked around with an unwritten filename convention. Does not satisfy G (hard to state in purely external terms) or K (external readers do not read tools/). Satisfies S alone, which is enough. **Keep, narrowed.** Do not expand to general tool refactor.

**Q4 (validation-approach.md coordinated change).** Satisfies **K** — the gap would be visible to an external reader who followed the kernel's §7b reference into validation-approach.md and found no corresponding treatment. **Keep, minimal.** Write the short domain-validation section; do not rewrite validation-approach.md.

**Extension I would cut.** I am not proposing one, which is itself worth stating: the temptation in Q4 would be to also revise `multi-agent-deliberation.md` to reference 7b-triggering sessions; I argued against it above because the interaction is benign. Hold that line. The watchpoint on negative-report triage (Q4) is **not** an extension — it is a deferral, which is the opposite of scope-inflation.

**Honest scope check.** Session 009's ratified direction is W2 + W4. My proposals touch W2 (Q2, Q3), W4 (Q1), and one coordinated spec (Q4 → validation-approach.md domain-validation section). The coordinated spec is in-scope because leaving it unwritten would make W4's kernel change reference a sense the validation specification omits. No other extensions.

## Meta-note

**(a) Position likely to differ from others.** I expect the Critic to argue against pairing the tool update (Q3) with Session 009 on scope-narrowing grounds, and the Integrator to argue for a more cautious workspace-structure revision that preserves the embedded-in-provenance pattern. I hold the opposite of both: the tool fix is small and load-bearing, and the embedded pattern contradicts provenance immutability once artefacts become mutable. I expect the Originator may propose a different top-level directory name (`external/`, `outputs/`); `applications/` is defensible but not uniquely correct — I will not die on that hill.

**(b) Suspect assumption.** The brief assumes domain validation is always out-of-session. It may sometimes be in-session (same human, sitting in the chair); the kernel text I proposed allows both but does not name in-session explicitly. Minor.

**(c) Framing concern.** W2 and W4 were ratified as separate watchpoints but are entangled through mutability — naming that entanglement now, rather than treating them as independent, costs little and prevents later unwinding.
