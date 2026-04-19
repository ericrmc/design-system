---
session: 009
title: Skeptic Perspective — Kernel Validate & Workspace-Structure Revisions
date: 2026-04-19
status: complete
perspective: skeptic
committed_at: 2026-04-19
---

## Q1

My preferred option is **minimal change**: leave the kernel §Validate as written, append one clarifying sentence that scopes it, and refuse to encode domain-native testing anywhere in the kernel until it has been seen more than once.

Proposed appended sentence:

> Validate as described here covers the workspace's internal consistency. Testing an external artefact in its target domain is a separate activity handled by whoever holds the external problem; its relationship to the methodology is not yet specified.

That's it. No sub-activities, no renaming, no second kernel slot.

**Argument for.** The kernel is a nine-step description of how the methodology moves itself forward, session to session. Its Validate activity was written to answer "is this workspace internally coherent after this session's changes?" That question is real and repeats every session. The question "did the movement sequence work for the user's back?" is categorically different: it has one participant (the user), happens outside session time, and has no relation to workspace consistency. Mashing both into one kernel activity — or adding a tenth activity for the second sense — treats a single external-artefact episode as sufficient evidence that the kernel needs to accommodate external testing as a structural feature. It doesn't. Session 008 is n=1.

**Rejected: two sub-activities under one Validate.** This locks the kernel into a bi-modal shape on the basis of one application. If Session 010 produces an external artefact whose "domain test" is twelve conversations with twelve strangers over six weeks, the sub-activity structure will cramp that shape or require immediate revision. Better to stay silent now and let the shape emerge.

**Rejected: two distinct kernel activities.** Same objection, stronger. Expanding the kernel's canonical activity list from nine to ten is a bigger commitment than the observation warrants. The nine-step structure is referenced elsewhere; lengthening it creates ripple edits for a change whose load-bearing necessity has not been demonstrated.

**Rejected: pointer to an elaboration specification.** Still worse: it requires creating the elaboration specification. Session 009 is not scoped to do that, and promising a forward reference to a file that does not yet exist adds debt.

**Consequence of minimal change.** The kernel stays nine activities. The W4 observation is honoured by the scoping sentence without being prematurely theorised. When a second external artefact surfaces, synthesis will have two data points and can decide structurally. The cost of waiting is one sentence of ambiguity for one session.

**Tension I hold.** I concede the two-senses observation is real. But "real observation" ≠ "kernel-level response." The role-specific stance invites me to ask what goes wrong if the kernel stays silent; my answer is *nothing goes wrong* — the user still tests artefacts, the workspace still validates internally, and no session is blocked. That is the honest adversarial answer.

## Q2

My preferred option is **canonicalize what Session 008 did, with a one-line addition** to workspace-structure.md under the provenance section, and make zero changes elsewhere. No `applications/` directory. No relocation of the existing artefact.

Proposed addition to the §provenance section:

> Where a session produces an artefact intended for use outside the workspace (an "external artefact"), the artefact is placed in that session's provenance directory alongside the session's reasoning files. The artefact's filename begins with a non-numeric prefix (e.g., `artefact-*.md`) to distinguish it from the numbered reading-order files.

That is the entire revision.

**Argument for.** The methodology has produced one external artefact. It lives in Session 008's provenance directory and is working fine there. The "problem" is not that the placement failed — it is that the placement was unnamed. Naming the practice that already works costs one paragraph; creating an `applications/` directory and relocating files costs a migration, a new top-level concept, and an implicit claim that future external artefacts will be numerous enough to warrant their own address. That claim is not yet supported.

**Rejected: new top-level `applications/` directory.** This is n=1 architecture. We do not know whether future external artefacts will be one-off files, directories with sub-structure, or something else entirely. Committing now to a flat top-level bucket pre-shapes the answer. Worse, it severs the artefact from its producing session, which is exactly where its provenance lives. An external reader curious about *why* the Morning Unfurl has the moves it has would have to navigate from `applications/` back to `provenance/008-*/` — the embedded placement avoids this.

**Rejected: hybrid (artefact in session provenance, forward pointer from `applications/`).** This is the worst of both. It creates the `applications/` directory (the expensive part) while also keeping the embedded placement (the cheap part). The only thing it adds is a second address for each artefact to fall out of sync with. Index files tend to rot; forwards tend to rot harder.

**What happens to the existing artefact.** Nothing. It stays at `provenance/008-first-external-application/artefact-morning-unfurl.md`. The proposed revision names the pattern that it already instantiates. This is the cheapest possible resolution and the one most honest about the evidence.

**On filename convention.** The non-numeric prefix is the one detail I do lift to specification, because it is the one detail Session 008's tooling sub-finding made concrete. Without it, the artefact collides with the numbering scheme used by validate.sh. With it, the collision is structurally avoided. This is not speculation; it is documenting a known-good workaround.

**Tension.** Canonicalizing n=1 also encodes assumptions about future external artefacts — specifically, that they will be files that fit inside a session directory. A future artefact that is a running service, a physical object, or a multi-file bundle would strain this. But that strain will be legible when it happens and I would rather strain-and-revise than over-architect on speculation.

## Q3

**Leave `tools/validate.sh` alone this session.** Record a watchpoint that fires the next time the hard-coded path bites. Do not pair the tool update with the workspace-structure revision.

**Argument for leaving the tool alone.** The hard-coded `02-decisions.md` path worked for seven sessions and produced a workaround on the eighth — a workaround that is recorded, reversible, and imposes exactly one discipline (don't number external artefacts into the reading-order sequence). That discipline is the same one the Q2 revision proposes to canonicalize. So the tool and the spec converge on the same shape without the tool being touched. Touching a validator in a session that isn't going to stress-test the change is how validators acquire bugs.

**Arguments against alternatives.**

**Parameterise the decisions-file path per session.** Introduces per-session configuration, which means a config file or frontmatter convention that doesn't yet exist. Building configuration surface for a problem that has occurred once is premature generalisation. Parameterisation also defers the question rather than answering it: what path-resolution rule is correct? We don't know yet.

**Expand the tool to search for a file matching a pattern (e.g., `*-decisions.md`).** This is the tempting option and I want to argue against it specifically. Pattern-matching makes the tool more permissive, which sounds like robustness. But validate.sh's value is that it catches deviations from the expected shape. A tool that accepts `02-decisions.md`, `03-decisions.md`, `99-decisions.md` because they all match `*-decisions.md` has weaker guarantees than a tool that insists on a single path. Before relaxing the assertion, we should know what variance the tool is supposed to tolerate — and we don't, from one data point.

**Pair the tool update with the workspace-structure revision so the spec governs the tool's search semantics.** This sounds principled — spec-first, tool-implements-spec — but it is actually the most expensive option and the one most likely to produce a new bug. The workspace-structure revision I'm proposing in Q2 is one paragraph. Coupling it to tool-search-semantics means Session 009 is also deciding the search-semantics contract, which is a separate concern and deserves its own deliberation when the need is concrete.

**What the watchpoint should say.** Something like: *If a second session places files that confuse validate.sh's path assumptions, or if a session has reason to re-number decisions, open the tool question then with two data points rather than one.* This is the "do nothing; record a watchpoint that fires at the second bite" recommendation the role stance invites, and I endorse it directly.

**Net position.** The cheapest correct thing for Session 009 is: tool untouched, workaround discipline promoted to a single sentence in workspace-structure.md, watchpoint filed. Session 009 should resist the temptation to clean up tooling while the cleaning is cheap — cleaning is only cheap when you know what the right shape is, and on one data point you don't.

## Q4

I will name three interactions. Two I judge benign; one I flag as a genuine coordination cost.

**Interaction 1: Q1 (kernel Validate scope) × `validation-approach.md`.** The validation-approach specification presumably describes the tier structure that validate.sh implements — i.e., the *internal-consistency* sense of Validate. My Q1 proposal (append a scoping sentence to the kernel) leaves validation-approach untouched: the kernel sentence says "domain-native testing is a separate activity not yet specified," and validation-approach continues to describe the internal-consistency approach it already describes. No change needed. **Benign, but not absent** — the benign conclusion depends on the minimal-change Q1 option. A richer Q1 (two sub-activities, or a second kernel activity) would cascade into validation-approach revisions, which is a cost the richer options silently carry. Flagging this is part of why minimal Q1 is my recommendation.

**Interaction 2: Q2 (workspace-structure) × `multi-agent-deliberation.md`.** The brief's §2 notes that prior close-records described Q2 as D-023-triggering and corrects that to D-016-triggering only. This is a specification-text issue in whatever session's close-record made the imprecise claim, not an active interaction for Session 009 to resolve. Recording the correction in this session's provenance (as the brief does) is sufficient. **Benign, resolved-by-recording.**

**Interaction 3: Q2 × future open issues about external artefacts that are not files.** This is the interaction I want to flag as non-benign. My Q2 proposal says external artefacts live in their producing session's provenance directory. This works for a Markdown file. It strains for: a software implementation (where does the code live — in `provenance/NNN-*/code/`? Unlikely), a physical object (documentation in provenance; object in the world), a service (running infrastructure has a lifecycle provenance doesn't model). My Q2 proposal does not address these cases, and canonicalizing the file-in-provenance pattern makes it implicitly harder to adopt different patterns later because precedent will push toward the canonical form.

**Coordinated change or watchpoint?** Watchpoint, not coordinated change. Session 009 should not attempt to pre-specify placement rules for artefact types that don't yet exist — that is exactly the n=1 generalisation error I argued against in Q2. But the session should record, explicitly, that the Q2 revision is correct for file-shaped external artefacts and that non-file external artefacts will trigger a fresh deliberation. Framing: the Q2 revision is scoped to its evidence, not extended to cases we haven't seen.

**One interaction I expect other perspectives to name that I judge less significant:** interactions between Q2 and OI-009 (if OI-009 concerns artefact indexing or cross-referencing). If OI-009 tracks "we should have an index of external artefacts," then a single-artefact workspace doesn't need an index — the provenance directory structure *is* the index. The interaction is "the revision delays OI-009's pressure until artefact count justifies it," which is the correct behaviour, not a coordination cost.

## Q5

Applying G/O/K/S honestly to my proposal — which is the minimal-change set: one sentence to kernel, one paragraph to workspace-structure, zero tool changes, one watchpoint.

**(G) Translation-to-external-frame.** *Partially satisfied.* The need for the Q2 revision can be stated externally: "external readers of the workspace looking at where Morning Unfurl lives should find its placement documented, not emergent." The need for the Q1 revision is harder — "external readers reading the kernel and noticing Validate is described only in the internal-consistency sense" is plausible but thin. I would grade the Q2 revision as G-satisfying and the Q1 revision as G-weak.

**(O) Narrows-external-action-decision-space.** *Not satisfied by either revision.* Neither the kernel sentence nor the workspace-structure paragraph removes a concrete blocker to a named next external action. There is no named second external artefact waiting for these revisions. If there were — say, "the user has asked for a second artefact about sleep and we need to know where to put it" — O would be satisfied. Without such a named next step, O is absent. This is the criterion I am most uncomfortable about.

**(K) External-reader visibility.** *Satisfied by Q2, probably not by Q1.* A reader outside the workspace reading workspace-structure.md for the first time, and then seeing Session 008's provenance directory with a non-numbered artefact file in it, would notice the discontinuity between spec and workspace. That is a K-satisfying gap: the spec does not describe what the workspace is. Q1 is harder to claim K on — the kernel's silence about domain-native testing is visible to a reader only if the reader also has access to Session 008's external context, which most readers won't.

**(S) Specific-obstacle resolution.** *Weakly satisfied.* The specific obstacle is the filename collision between external artefacts and validate.sh's path assumptions. My Q2 proposal (non-numeric prefix) closes that obstacle by making the workaround canonical. That is a real S-satisfaction. The kernel revision (Q1) does not resolve a specific obstacle; it merely scopes a description.

**Honest recommendation.** The Q2 revision earns its place on K and S. The Q1 revision is weaker: it satisfies G weakly and nothing else. **Consider dropping Q1 entirely.** Leave the kernel alone, record the two-senses observation as a watchpoint (alongside the tooling watchpoint and the non-file-artefact watchpoint), and revisit when either (a) a second external artefact surfaces, or (b) a reader confuses the two senses in a way that causes an actual miscommunication. This is the minority position I most want preserved: Session 009 may be warranted on Q2 but not on Q1, and the cheapest honest version of the session ships Q2 alone.

If Q1 is retained over this objection, my proposed minimal-change sentence is the form I would defend. But the adversarial position is: drop Q1.

## Meta-note

(a) I expect other perspectives — particularly any architect-role voice — to argue for richer kernel revisions (sub-activities, a second activity, or elaboration-spec pointers). My position that Q1 should be dropped entirely, or reduced to one appended sentence, is the minority view I most want preserved. The asymmetry matters because richer Q1 options cascade into validation-approach edits and lengthen the kernel's canonical activity list, both on one data point.

(b) Suspect assumption: the brief treats W2 and W4 as comparably ripe for revision. They are not. W2 has tooling evidence (the filename collision); W4 has only the observation that two senses were in play. I accept the scoping but record the asymmetry.

(c) Concern about framing: the G/O/K/S question arrives last. A perspective that has already proposed revisions in Q1–Q4 faces sunk-cost pressure in Q5. Future sessions might apply G/O/K/S before proposal-drafting, not after.

