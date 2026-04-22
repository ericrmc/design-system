---
session: 027
title: Perspective — Minimalist
date: 2026-04-23
status: complete
perspective: minimalist
committed_at: session-027-independent-phase
---

# Perspective — Minimalist

## Framing note before Q1

The operator surfaced an observation: four consecutive provenance folders share the same opening-default name. The deliberation wants to know whether to formalise a folder-naming rule, whether to retroactively rename, where the rule should live, and what this drift means for the engine's self-observability. My load-bearing concern is that the engine has been accreting surface for 27 sessions and that each new rule is a tax — small per-instance, compounding in aggregate — paid forward across every future session by writers, validators, and readers. Before I answer the six questions, I want to be explicit about what I think the operator's observation actually is, because the answers depend on it.

The four folders named `NNN-session-assessment` are not evidence of a lost convention. They are evidence that a convention which was already fraying before Session 023 (Session 015 did not rename; the rename practice was never specified) stopped being performed once the SESSION-LOG thin-index absorbed the function the folder name was serving. The operator is right that the pattern broke. What the operator has not yet concluded — and what is this perspective's job to argue — is that the break is not a defect to be repaired. It is a signal that a redundant channel has quietly gone silent, and the correct engine response is to notice the silence, accept it, and remove the channel from the spec. I will argue this across Q1-Q6 and in the closing summary.

## Q1. Should the engine formalise a folder-naming discipline?

No. The engine should not formalise a folder-naming discipline. It should go the other direction — standardise on the opening default as the permanent name and drop the informal rename-when-substantive practice.

The case for formalising looks reasonable on its face: four folders lost their descriptive names, the operator had to notice, and a rule would prevent recurrence. But each of those three clauses is weaker than it looks when examined.

First, "four folders lost their descriptive names." They did not lose descriptive names — they never had them, because the rename step at close was never part of the close checklist in any version of the methodology kernel or workspace-structure spec. Sessions 017-022 received content-reflective names through session-specific editorial judgment, not through a rule. Session 015 already broke the implied pattern (single-perspective planning session, no rename), and the engine did not flag it because there was no rule to flag against. The "drift" framing presumes a baseline discipline that was not specified. Retrofitting a rule to match the 017-022 pattern imports a convention we did not previously have.

Second, "the operator had to notice." The operator noticed on Session 027 open, at which point the workspace had absorbed four sessions under placeholder names and nothing was broken. No decision was lost. No reference went untraceable. The SESSION-LOG entries for Sessions 023, 024, 025, 026 carry descriptive titles (`Read-Contract Budget Recalibration; engine-v3 → engine-v4`; `MAD 6K-Soft-Warn Response — A.4 Carry-the-Warning`; `Path A Executed — Carry-the-Warning Continues`; `Path A Executed — D-086 R9 Cadence-Escalation Window Ages Out`). Discoverability is intact. The operator's observation was aesthetic, not functional. That matters when we are asked to pay a rule-tax to prevent its recurrence.

Third, "a rule would prevent recurrence." A rule is a forward promise. The engine's track record with informal conventions is the data we have about how well it keeps forward promises. The rename-when-substantive convention was observed 6 times out of 8 eligible sessions (017-022, counting 015 as the break) before it stopped being observed at 023. That is a 75% observance rate for a low-stakes editorial habit. The mechanism for preventing the next lapse — a specification clause plus a validator check plus a close-step obligation — has to hold for 27+ future sessions better than the informal version held for 10. Claiming that formalisation closes the gap requires demonstrating the mechanism, not asserting it. I will ask for that demonstration in Q6.

The cost of leaving it informal, if "informal" means "not specified and not practiced": zero, modulo the operator's aesthetic objection. The cost of leaving it informal while asserting there is a convention: confusion, because no one can tell when the convention applies. The cost of formalising: a line in workspace-structure.md, a close-step obligation, a validator clause, a decision per session about whether the current session's content warrants a new name, and the accretion of one more editorial judgment to every close-phase activity. OI-007 scaling pressure is the accumulated weight of those "small" taxes.

My recommendation for Q1: standardise on the opening-default form as the permanent name. Specify in workspace-structure.md that provenance folders are `NNN-session` (or `NNN-session-NNN` if we want redundant stability, which I discuss in Q4), and that the folder name is not the thin-index — SESSION-LOG.md is. No rename at close. No editorial judgment required. The discoverability function is fully carried by SESSION-LOG.

## Q2. When should the folder name be chosen, who can revise it, D-017 interaction?

If my Q1 recommendation holds, Q2 largely dissolves. The folder name is chosen at open, matches a deterministic template (`NNN-session` or similar), and is never revised. No authority question arises because no revision happens. No D-017 interaction because no content or address mutation occurs after close.

But the question is asked in the alternative — if we do formalise a discipline — and the answer there matters for completeness.

Choosing at open: infeasible. At open, the session does not know what it will produce. The six-path presentation is drafted but the decision is not made. Naming at open would either encode the expected content (which is wrong whenever the session takes a different path) or encode the input (which reproduces the `session-assessment` placeholder problem we are trying to solve).

Choosing at close: plausible, but creates the exact D-017 pressure we are trying to avoid. If the rule says "current session renames at close," the rename action itself is a close-session modification that the session records. That is not a D-017 violation — the session is still open when the rename is performed. But it establishes a pattern where close activities include workspace-structural edits, and every additional close-phase activity is another thing the engine has to remember and execute correctly. OI-007 debit.

Choosing in subsequent session: explicit D-017 violation unless dispensed. "Next session renames Session N-1's folder based on what N-1 actually produced" is editing a closed session's address. Even if we narrow the dispensation to "path-string touch only, no content mutation," we have introduced a mechanism whose sole purpose is to make folders look better in `ls`, at the cost of loosening D-017. The immutability principle is load-bearing for the engine's trust contract — session N can cite session N-2 knowing the citation will resolve. Opening the retroactive-rename door for folder-aesthetics reasons is a bad trade.

Never-after-close: this is the D-017-respecting variant of "choose at close." It forces the naming decision into a close-phase editorial judgment that, if not exercised, results in the placeholder surviving forever. That is what happened in Sessions 023-026. The informal version of this rule ran for five sessions (023-026 plus the earlier 015) and failed in four of them (023, 024, 025, 026 — 015 was correctly placeholder-retained because no substantive output occurred).

So the authority-and-timing question collapses to: either we accept that the current-session-at-close variant is what we are formalising, or we accept that the next-session variant requires a D-017 dispensation. I reject both. I recommend the no-rename policy from Q1 precisely because both formalisations have costs that exceed the problem they solve.

If I were forced to pick one: current-session-at-close, with explicit written permission in workspace-structure.md, and no retroactive-rename authority ever granted to subsequent sessions. This is the narrower option. It does not touch D-017. But I still argue against adopting it.

## Q3. Retroactive rename of 023/024/025/026?

No retroactive rename.

The three options the brief enumerates:

(a) Leave text references stale after rename. This is incoherent — the workspace is supposed to be internally consistent. A folder address that is referenced inside closed-session files as `023-session-assessment` and as filesystem path `023-read-contract-budget-recalibration` is a workspace in which grep produces misleading results. The operator will have to remember, every time, that the path strings don't match reality. This is worse than the current state, not better.

(b) Edit text references inside closed-session folders. D-017 violation. The brief acknowledges this.

(c) Narrow dispensation: path-string updates only, no content mutation, enumerated in a decision record. This is the option that the deliberation will find most tempting. Let me argue directly against it.

The dispensation sounds narrow, but it establishes that D-017 has exceptions when the cost of preserving immutability is "workspace internal inconsistency after a workspace-structural change." Once that exception exists, it is available for the next reorganisation. Session 022 already did a workspace-scaling reorg — imagine it had required path-string updates inside closed sessions. Session 030 might do a folder-hierarchy reorganisation and claim the same dispensation. Each one individually will be narrow. Cumulatively, D-017 becomes "immutability except when workspace-restructuring demands otherwise," which is materially weaker than "provenance records are immutable once the session closes."

There is a second argument. The four folders are historical witnesses to the drift. That is not a cost — that is a feature. A future session looking at provenance history can see that Sessions 023-026 share a placeholder name and that the pattern broke between 022 and 027. This is legible evidence of the engine's state at the time. Renaming them erases the evidence. We end up with a workspace that looks like it always followed a discipline, when in fact the discipline was not followed. That is a loss of historical fidelity in service of aesthetic uniformity.

Third: the git history points into old paths. Even a perfect rename does not fix the git log. Someone doing archaeology on the engine's development will see `git log -- provenance/023-session-assessment` works and `git log -- provenance/023-read-contract-budget-recalibration` also works (because the rename shows up as a move), but the commit messages still reference the old name. Retroactive renaming produces a workspace where the file tree says one thing, the commit messages say another, and the closed-session files either say the old thing (option a) or were illegally edited (option b/c).

The cost of leaving the four folders as historical witnesses: minor aesthetic inconsistency in `ls provenance/`, easily explained by a one-line note in SESSION-LOG.md or in the Session 027 close record ("Sessions 023-026 retained the opening-default folder name; Session 027 standardised on the default as the permanent form"). That is cheap and accurate. The cost of retroactive rename: D-017 dispensation precedent, historical fidelity loss, and the engine energy to execute and validate the rename. No.

## Q4. Should the opening-default name change?

Yes, but modestly. The current `NNN-session-assessment` default is a design bug, but the fix is small.

The bug: `session-assessment` is a session-shape classification. It implies every session is an "assessment" session, which is false. Some sessions are assessments of a prior session's state. Others execute a pre-authorised path (Sessions 025, 026 per the SESSION-LOG entries). Others deliberate on spec revisions. Others are single-perspective planning sessions (Session 015). The word "assessment" is wrong for the majority of sessions and quietly misleading for the minority.

The fix options the brief lists:
- `NNN-opening`: fine, but "opening" is also a session-activity term (per methodology-kernel.md v5's nine activities — Read, Assess, Convene, Deliberate, Decide, Produce, Validate, Record, Close). Using "opening" as the folder name conflates the folder with the first activity, which could confuse future readers.
- `NNN-<date-stamp>`: redundant with git commit timestamps, and date-stamps tie the folder to wall-clock time in a way that is brittle if a session spans multiple days.
- `NNN-pending-title`: accurate but verbose, and implies the title will arrive later, which contradicts my Q1 recommendation that no rename occur.

My preference: `NNN-session` (no tail). Three characters, semantically empty, deterministic. The folder name becomes the container address, nothing more. SESSION-LOG carries the title. This is the cleanest expression of the "folder name is not the thin-index" principle.

A weaker alternative: `NNN-session-NNN` (e.g., `023-session-023`). This is redundant but stable and makes the folder name harder to mistype. The redundancy is a minor tax — five extra characters per folder, one extra glance to realise the tail is not adding information. I do not prefer it, but I would accept it if the deliberation wants a belt-and-braces form.

I would reject any option that includes editorial-judgment text (e.g., `NNN-read-contract-budget-recalibration`). Those names require per-session authorship, which is exactly the close-step obligation I am trying to remove. The whole point of picking the default form is to make the folder name deterministic.

Whether this should be applied retroactively to Sessions 023-026 is the Q3 question — no. Whether it should be applied to Session 027 onward, and to the Session 015 folder — yes for 027 onward, no for 015 (Session 015 is a closed historical record and D-017 applies).

Two edge cases worth flagging:
1. Session 015's folder is `015-session-assessment` per the brief. Under my recommendation, it stays that way — D-017. Under any deliberation outcome that changes the default, Session 015's folder becomes the last artefact of the old default and is a historical witness to the policy change. Fine.
2. Sessions 017-022 have content-reflective names that are well-chosen and should not be renamed — D-017 again, plus they are genuinely more useful than default names would be. The engine does not need to retrofit uniformity onto the historical record. It needs to pick a forward default and hold.

## Q5. Where should the rule live?

If the rule is "the folder name is the opening-default form, permanently, no rename," it belongs in `workspace-structure.md` §provenance. That specification already defines the provenance directory pattern; adding one sentence that fixes the folder-name form is the smallest possible surface change.

The candidate locations:

**workspace-structure.md §provenance.** Best fit. This is where provenance directory structure is specified. The clause would read approximately: "Provenance folder names are `NNN-session` where NNN is the zero-padded session number. The folder name is stable from open through close and is not revised. Discoverability is carried by SESSION-LOG.md (thin-index)." One sentence, one clause, in the spec where a reader would look for it.

**prompts/development.md §How to operate.** Wrong location for a structural rule. development.md is operational guidance for agents running the engine; it can reference the workspace structure spec but should not redefine it. If we put the rule here and not in workspace-structure.md, the spec and the operational prompt diverge, which is a future-debt instrument.

**methodology-kernel.md.** Too high-level. The kernel specifies the nine activities and the session cycle, not the filesystem layout. Folder-naming is a workspace-structure concern.

**engine-manifest.md.** Wrong. The manifest enumerates active specs; it does not contain rules.

**A new file.** No. OI-007 scaling pressure. Adding a spec file for a folder-naming rule is the most expensive possible placement for the smallest possible rule.

Tradeoff note: workspace-structure.md is currently at v4. If the clause I propose is classified as substantive (OI-002 heuristic), it triggers a version bump. I think it is minor — it formalises a default that is already operationally in use (Sessions 023-026 used this default), and it removes an unstated informal practice rather than adding new behavior. Minor revision, no v-bump, no engine-v bump. Operator can adjudicate per OI-002.

If the deliberation disagrees with my Q1 recommendation and goes for a formalised rename-at-close rule, the placement question becomes harder. The rule has two components: the naming convention (workspace-structure.md) and the close-phase obligation to exercise it (prompts/development.md §close). Putting the rule in one place risks the other half being forgotten. Putting it in two places creates spec-duplication risk. This is a second argument against formalising — the placement is cleaner when the rule is "default is permanent" than when the rule is "rename at close when substantive."

## Q6. Is this class of drift governable by the proposed mechanism?

This is the sharpest question in the brief and deserves the sharpest answer.

The operator's observation — that four consecutive self-audits (Sessions 024/025/026, and we can add Session 023's own close to the count) missed the folder-name drift — is data about single-session self-audit's field of view. The synthesis-fidelity audit performed by Session N on Session N-1 is targeted at whether Session N-1's produced artefacts correspond to its deliberation inputs. It is not designed to notice that the folder the artefacts live in has a misleading name. The name-of-the-container is outside the audit's frame.

The question is whether a specification clause — wherever we put it — changes that. I argue it does not, and that the inference from "the drift went unflagged" to "we need a rule" is backwards.

Consider what a formalised rule would actually do. The clause in workspace-structure.md says "rename at close when substantive." The validator checks the clause. The validator, operating on Session N, reads Session N's close artefacts, confirms the folder was renamed if substantive output occurred, and passes or fails. This works for Session N. It does not work for Session N-1. The Session 023 close, under a hypothetical formalised rule, would have noticed its own placeholder and renamed. But the Session 023 close also noticed that it had produced an engine-v4 bump, and it still did not rename. The informal convention was known to the Session 023 author; the convention did not translate to action. That is the failure to diagnose.

If the Session 023 author, aware of the informal convention, did not rename, the formalised convention has to do one of three things:
1. Generate a validator that *fails* the close, forcing the rename before the session closes. This works, but it introduces a validator category ("workspace-aesthetic fails") that was not previously in scope.
2. Generate a validator that *warns* the close, like a lint. This is what the informal convention already was, minus the written-down part. We have evidence it is insufficient.
3. Generate a mandatory close-phase activity that the close step has to execute or explicitly defer. This adds a 10th activity to the nine-activity kernel, or a close-phase sub-step. Spec surface.

Option 1 is the only one that actually prevents recurrence, and it does so by promoting folder-naming to a blocking concern. That promotion is a substantive change to what the validator is for. The validator currently checks read-contract budgets, MAD escalations, immutability, reference resolution. Adding "and folder names look right" is a genre shift. I do not support the shift.

Option 2 is placebo. Option 3 is kernel modification — OI-007 debit.

Which means the formalisation response does not actually address the self-observability question. It either blocks on aesthetics (over-strong) or provides the same outcome the informal convention provided (equivalent, not improved).

The deeper question — whether single-session self-audit can surface this class of drift at all — I think the answer is no. Self-audit scopes to the session's own decisions and the prior session's artefacts-to-inputs correspondence. Workspace-global drift ("folder names have been drifting for 4 sessions") is cross-sectional; it is not visible from the inside of any single session's audit frame. The only mechanism that would reliably catch it is a periodic workspace-wide audit — which is itself an accretion of engine surface, and which has its own frequency and scope questions.

My position on Q6: the operator is the correct mechanism for this class of drift. External observation by someone who sees the workspace as a whole, not through the lens of a single session's scope, is the detection mechanism that actually worked here. The operator noticed on Session 027 open. The drift was surfaced. The self-audit not catching it is not a defect in the self-audit — it is the audit correctly operating within its scope. Adding a rule does not expand the scope. It adds a specific check that might or might not fire on the specific drift that triggered the rule's creation, while doing nothing for the next class of cross-sectional drift we have not yet imagined.

The right engine response is not to add a rule to catch the drift we just observed. It is to accept that operator observation is the layer at which workspace-global consistency is policed, and to keep the engine's self-audit scoped to its current frame. This is a statement about engine architecture, not about folder names.

## Concluding summary

Top-line recommendation: do not formalise a folder-naming rule, do not retroactively rename Sessions 023-026, change the opening-default from `NNN-session-assessment` to `NNN-session` in workspace-structure.md §provenance as a minor revision, and accept that cross-sectional drift is governed by operator observation rather than by additional single-session checks. This answer pays the smallest possible surface cost, preserves D-017 unbroken, and treats the operator's observation as the signal it is — that a redundant channel (folder-name-as-thin-index) has been superseded by SESSION-LOG.md and should be formally retired rather than formally revived.
