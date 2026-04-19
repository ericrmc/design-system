---
session: 009
title: Minimalist Perspective — Kernel Validate & Workspace-Structure Revisions
date: 2026-04-19
status: complete
perspective: minimalist
committed_at: 2026-04-19
---

## Q1

**Proposal: amend the existing §Validate with one added bullet. No new sub-activities, no new activities, no vocabulary additions.**

Replacement text:

> #### 7. Validate
>
> Check that the workspace is internally consistent:
>
> - New specifications don't contradict existing ones
> - Specifications describe the workspace as it actually is
> - Provenance records are complete and well-formed
> - Open issues reflect the actual state of uncertainty
> - If the session produced an artefact intended for use outside the workspace, check whether it functioned for the person who has the problem it was made for
>
> If validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.

The frame "check that the workspace is internally consistent" still governs the first four bullets. The fifth bullet is *also* a check; it just checks a different thing — whether the artefact, when used, did what it was supposed to do. The added bullet uses existing kernel words: "session," "artefact," "outside the workspace," "use," "problem." It introduces no new term.

**Rejected: two distinct activities (e.g., 7a Validate-Internal, 7b Validate-External).** This expands the activity list from nine to ten and forces every session — including ones with no external artefact — to explicitly dispose of the new activity ("N/A this session"). That is administrative weight for a case that will not always apply. The kernel's nine activities earn their slots by applying *every* session; a tenth that applies only sometimes weakens the pattern.

**Rejected: new vocabulary like "domain-native validation" or "in-use validation."** These terms are accurate and read well in prose; they are heavy in a kernel. Once named, every later session must decide whether to use the term. The bullet above communicates the same content without coining anything: readers understand "check whether it functioned for the person who has the problem" without needing a label for the check.

**Rejected: pointer to an elaboration spec.** Pointing out ("see `validation-approach.md` for external-artefact case") drags a second file into every read of the kernel. The observation is one sentence long; it fits in the kernel directly.

Activity-list consequence: none. Count remains nine. Sequence unchanged. Existing `tools/validate.sh` behaviour is unaffected — it continues to check the first four bullets, which are the mechanical ones. The fifth bullet is a human check and was always going to be, regardless of how it is named.

Residual ambiguity I accept: the added bullet does not specify *who* performs the check (author? user? agent?) or *when* (before Close? after?). Session 008 answered both in practice — the user did it, out-of-session, and Session 009 opened on the receipt. That pattern is one data point; writing it into the kernel would overspecify. Let the next external-artefact session either repeat Session 008's pattern or name a reason to deviate; if a stable pattern emerges over three or four cases, record *that*.

## Q2

**Proposal: one-sentence addition to §Additional directories. Keep the Session 008 artefact where it is. Do not create `applications/`.**

Added sentence to §Additional directories:

> Artefacts produced by a session for use outside the workspace are placed in that session's provenance directory alongside its deliberation and decisions, unless a future session names a reason to do otherwise.

Session 008's artefact at `provenance/008-first-external-application/artefact-morning-unfurl.md` stays where it is. No move, no copy, no symlink, no forward pointer.

**Rejected: new top-level `applications/` directory.** One artefact is one data point. Creating `applications/` from one case makes a pattern claim the evidence does not support. If Sessions 010, 012, and 015 each produce external artefacts, and the provenance-embedded placement starts to strain — e.g., artefacts get referenced across sessions, or users want to find them without knowing which session produced them — *then* `applications/` earns its slot. Premature top-level directories are expensive to retract: once specified, later sessions defer to them even when the fit is poor.

**Rejected: hybrid (artefact in provenance + forward-pointer stub in a top-level location).** A stub file in a directory that does not yet exist is worse than no stub — it creates a directory whose only function is to hold pointers, which is a structural commitment disguised as minimalism. If `applications/` is not worth creating, its stub-precursor is not worth creating either.

**Rejected: rename or move the Session 008 artefact.** Session 008's provenance is closed; moving files out of a closed session violates the "immutable once the session closes" property spelled out in the current workspace-structure text. Even if the move were technically allowed, it would be churn for no gain. The Session 008 artefact is findable by anyone who reads Session 008's session-log entry, which is where external readers will land.

The added sentence names a distinction without coining vocabulary: "artefacts produced by a session for use outside the workspace." No new term ("external artefact," "application," "work-product") is required. The phrase describes the artefact by what it is for, which is the simplest possible definition.

Residual ambiguity I accept: the sentence does not say what filename format the artefact should use, whether it should be numbered, or how it should be indexed. Session 008 chose `artefact-morning-unfurl.md` (non-numbered); that is fine. Later sessions can do the same or something else; if a naming convention is worth canonicalizing, that will be evident after several cases.

## Q3

**Proposal: leave `tools/validate.sh` as-is for Session 009. Record the hard-coded path as an open issue; do not fix it now.**

The hard-coded `02-decisions.md` path in checks 14 and 15 is a real defect — Session 008 discovered it by hitting it. But Session 008 also found a workaround (non-numbered filenames for non-decisions-file artefacts) and the workaround is compatible with the Q2 proposal: external artefacts keep non-numbered filenames like `artefact-morning-unfurl.md` and the decisions file keeps its `02-` prefix. Under that pattern, the tool continues to work correctly.

**Rejected: parameterise the decisions-file path per session.** Adds configuration surface for a problem that is already solved by convention. Once parameterised, future sessions must either specify the parameter (noise) or default it (same as hard-coding, but with more code).

**Rejected: expand the tool to search for a file matching a pattern (e.g., `*-decisions.md`).** A file-pattern search is a small change in LOC but a meaningful change in the tool's contract: it moves from "the decisions file is at a known path" to "the decisions file is whatever matches this pattern." The looser contract has to be specified and maintained. The current contract is rigid but simple.

**Rejected: pair the tool update with Q2 so the workspace-structure spec governs search semantics.** Coupling the tool to the spec makes the spec heavier (it now has to describe search semantics) and the tool more abstract. The tool's job is narrow: check that each closed session has a well-formed decisions file. The narrow form is fine.

Open issue wording (brief): *The hard-coded `02-decisions.md` path in checks 14–15 of `tools/validate.sh` constrains session provenance file numbering. Workaround: non-decisions artefacts use non-numbered filenames. Revisit if numbering pressure becomes a recurring issue.*

This is the minimal acknowledgment that the defect exists, paired with the minimal action — none — that the current evidence warrants. The trigger for picking it up is concrete: a session where the workaround cannot be applied, or a third external artefact whose natural place in the numbering would collide.

## Q4

**Interaction: Q1's added Validate bullet vs. `validation-approach.md`.**

`validation-approach.md` describes the Tier-1/Tier-2 structure of validation and is what `tools/validate.sh` implements. The Q1 bullet adds a fifth check to §Validate that is neither Tier-1 (mechanical, tool-checkable) nor easily Tier-2 (whatever Tier-2 currently specifies). It is a human check, performed by the user of the artefact, possibly out-of-session.

**Assessment: benign for Session 009. Watchpoint for later.** The Q1 bullet does not contradict `validation-approach.md`; it adds a kind of check the existing document does not yet describe. The bullet stands on its own in the kernel. `validation-approach.md` can be updated in a later session (e.g., when a second external artefact goes through the same receipt pattern) to name the new check's tier, if tiering turns out to matter for it. Bundling this update into Session 009 would expand scope past W2+W4.

**Interaction: Q2's added sentence vs. `multi-agent-deliberation.md`.**

`multi-agent-deliberation.md` governs when deliberation is needed and who participates. The Q2 sentence changes placement of artefacts; it does not change who deliberates or when. The brief's own §2 notes that workspace-structure revisions trigger D-016 (multi-agent deliberation) but not D-023 (non-Claude participation). Session 009 is already running multi-agent deliberation because W4 is in scope. Q2 comes along for the ride. **Assessment: benign; no coordinated change needed.**

**Interaction: Q1 and Q2 with each other.**

Q1's added bullet refers to "an artefact intended for use outside the workspace." Q2's added sentence refers to "artefacts produced by a session for use outside the workspace." The phrases agree without either defining a term. If Q1 and Q2 are both adopted, a later reader encounters the same description twice in two specs — this is slight duplication, not inconsistency. The duplication is acceptable: it lets each spec stand alone. **Assessment: benign; no coordinated change needed.**

**Interaction with Session 008's W1 (Read) and W3 (self-referential phrasing), currently deferred.**

Q1 and Q2 do not touch the Read activity or the self-referential phrasing. They do not foreclose future work on W1 or W3. **Assessment: benign; no new watchpoint.**

**Interaction with OI-004 and OI-009.**

The brief instructs to consider interactions *other than* OI-004 and OI-009, but I note for completeness that nothing in Q1 or Q2 changes the state of either. **Assessment: benign.**

**New watchpoint I would record:** *If a second external artefact produces a receipt that does not fit the pattern assumed by Q1's added bullet (e.g., the artefact has no single "person who has the problem" — it is for broad use; or its use is long-run and does not produce a timely receipt), revisit the bullet's wording.* This is the honest cost of the minimal Q1 wording: it assumes a specific-user-receipt shape that Session 008 exhibited. One data point supports the shape; a second may not.

## Q5

Applying G/O/K/S honestly.

**Q1 (kernel Validate bullet):**

- **G — Translation-to-external-frame.** Yes. The need is stated in external-frame terms: *"the methodology produced an artefact for use outside itself; the check that the artefact worked is not currently described."* Does not require self-description to motivate.
- **O — Narrows-external-action-decision-space.** Weakly. It does not remove a concrete blocker to a named next external action; Session 008's artefact was already produced and validated without the bullet. The bullet helps the *next* external artefact's session be clearer about what Validate covers, which is closer to K than O.
- **K — External-reader visibility.** Yes. A reader picking up the kernel and asking "how would I know this method worked?" will find the current Validate silent on the use-case they probably care about. The added bullet answers them.
- **S — Specific-obstacle resolution.** Yes. The obstacle is specific: two senses of Validate were active in Session 008 and the kernel named only one. The bullet closes that.

**Q1 verdict: load-bearing. G + K + S.**

**Q2 (workspace-structure sentence):**

- **G — Translation-to-external-frame.** Yes. "Where does the movement sequence live?" is stateable without reference to the methodology's self-description.
- **O — Narrows-external-action-decision-space.** Yes, minimally. The next session that produces an external artefact is spared the placement decision Session 008 had to make.
- **K — External-reader visibility.** Weakly. An external reader is unlikely to notice the absence of a placement rule until they look for the artefacts and cannot find where they live. With one artefact, findability is adequate via the session log.
- **S — Specific-obstacle resolution.** Yes. The obstacle is the Session 008 placement ambiguity itself.

**Q2 verdict: load-bearing. G + O + S.**

**Q3 (tool, leave as-is + open issue):**

- **S — Specific-obstacle resolution.** Partial. Recording the open issue closes the "this was noticed and then lost" problem; it does not close the defect itself.
- **G/O/K.** None. Not an external-frame concern, not blocking external action, not externally visible.

**Q3 verdict: ceremonial if taken as action, load-bearing only as recording. The "leave as-is" choice *is* the minimal action; it is not an extension to drop — it is the absence of an extension.**

**Extensions I would drop if they had been proposed:**

- Canonical filename format for external artefacts (overspecifies from one case).
- Elaboration spec for external-artefact Validate (Q1 bullet handles it; elaboration is for pattern-across-cases).
- `applications/` directory creation (fails G through S; pattern claim from one case).
- Parameterising `tools/validate.sh` (fails G/O/K; S is speculative).

**Session 009 scope under this proposal:** two one-sentence additions (kernel §Validate; workspace-structure §Additional directories) and one open-issue record (tool hard-coded path). Three small things. Each maps to a named weakness in the brief. No new section, no new directory, no new vocabulary.

## Meta-note

(a) **Position I expect to differ from others:** I expect the Architect or the Methodology-Fit perspectives to propose `applications/` or an elaboration spec for external-artefact Validate. I hold, reluctantly, that both are premature. One data point is one data point; every additional spec-surface will itself need to be validated. If synthesis adopts a larger structure, I want the provenance to show that the minimal alternative was on the table and defensible, not absent. (b) **Suspect assumption:** the brief treats "the user reported back" as the prototype of domain-native Validate. Session 008's artefact had a user whose stiffness was in scope that morning. Other external artefacts may not have such a timely, specific, single-user receipt loop. The Q1 bullet I propose inherits this assumption; I flagged the watchpoint in Q4. (c) **Framing concern:** the brief's ratified scope is narrow, but each question invites a proposal; inviting proposals pulls against narrowness. I have tried to answer each Q with the minimum, including "do not do this" where warranted.
