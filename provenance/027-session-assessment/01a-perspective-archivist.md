---
session: 027
title: Perspective — Archivist
date: 2026-04-23
status: complete
perspective: archivist
committed_at: session-027-independent-phase
---

# Perspective — Archivist

## Q1. Should the engine formalise a folder-naming discipline?

No. Or more precisely: not as a specification, not as a validator check, not as a new close-step activity, and not as a clause inside workspace-structure.md. The drift the operator observed is real, but the remedy the observation invites — formalise the rule, mechanise its enforcement, add a close-step — is disproportionate to the harm.

Begin with what actually went wrong. Across Sessions 023-026 the folder names did not get updated to reflect content. The content is fine. The decisions are recorded. The synthesis documents exist. The validator ran. The minority ledger was preserved. The read-contract was honoured. Every load-bearing machinery of the engine continued to function. What failed is a cosmetic labelling convention that was never specified in the first place. Calling this a "drift" elevates it to spec status; more accurate to call it a style regression — four sessions in a row adopted the opening-default filename and didn't rename at close.

Before we reach for a new rule, examine what the informal convention cost when it worked. From Sessions 017-022 the operator and the engine appear to have negotiated names through ordinary human judgement at either open or close. The names are good: `017-oi017-reframing-deliberation`, `018-reference-validation-exercise-1`, `022-workspace-scaling-trajectory`. No rule produced these; attention produced them. A person looked at the folder and thought "this should say what it is." That attention was available for six sessions and then drifted for four. The straightforward corrective is: restore the attention.

What is the cost of leaving it informal?

First candidate cost: future readers get confused when four folders share a placeholder name. I accept this. But the confusion is bounded. The SESSION-LOG.md (per workspace-structure.md v4) carries the real titles; each session's own synthesis and close files narrate content; the manifest.yaml inside each folder identifies the decisions. A reader navigating by folder name alone is already mis-using the workspace. Folder names are not the primary index; the SESSION-LOG is. Degrading the folder-name redundancy does not destroy navigability, it merely removes a convenience.

Second candidate cost: the drift is evidence of decay in the engine's self-observation. I accept this too, and I will speak to it in Q6. But the remedy for decayed self-observation is not to add more mechanism. More mechanism is what decayed. The engine has 9 activities, 13 active OIs, a 22-check validator, a read-contract, a minority-preservation ledger, an engine-manifest, OI-002's heuristic for substantive-vs-minor revisions, OI-007 itself tracking scaling pressure on workspace surfaces. Each one was defensible when added. Taken together they are a forest. Adding one more tree — "at close, verify folder name reflects content" — does not restore attention, it consumes attention. Attention spent verifying a naming check is attention not spent reading the synthesis.

Third candidate cost: without a rule, the same drift will recur. Probably. Drifts recur in every process. The question is whether the recurrence cost exceeds the formalisation cost. For folder names I do not think so. A folder named `025-session-assessment` when it could have been `025-path-a-r2-conversion-check` is ugly but not broken. A future reader who opens `025-session-assessment/synthesis.md` will find the actual content in the first paragraph. If they only read the folder name they were never going to understand the session anyway.

OI-007 is directly on point. OI-007 observes scaling pressure on workspace surfaces and asks whether additions pull their weight. A new close-step for folder naming fails the OI-007 test: it adds surface (a check), it adds process (run the check), it adds documentation (document the check), it adds enforcement (what happens when the check fires), and it solves a problem that is aesthetic rather than load-bearing. Scaling pressure is already pressing; this is exactly the kind of addition OI-007 was written to discourage.

What goes wrong if nothing changes? Four folders stay named as they are. The SESSION-LOG continues to carry the real titles. Future sessions either restore the informal convention (the human looks at the folder and renames it at close) or they do not. If they do, the problem was transient. If they do not, the cost is four more ugly folder names per four sessions, and eventually someone proposes the spec revision again with more evidence — at which point the case is stronger, not weaker. Waiting does not foreclose future rule-making; it just means we do not pay the rule-making cost until the harm is demonstrated.

My recommendation on Q1: do not formalise. If something must be done, make it a single sentence in prompts/development.md under "How to operate" — and make it advisory, not a spec clause. That note, and the operator's direct attention, are sufficient.

## Q2. When should the folder name be chosen or revised? Who has authority?

Assume for this question that some lightweight rule exists (see Q5) — the answer to "when" and "who" still needs to be consistent with D-017.

The only safe answer is: at open or during-session, never after close. Once a session closes, the folder name is part of the provenance artifact. D-017 states plainly: "Provenance records are immutable once the session closes. Errors or retractions are recorded in subsequent sessions, not by editing past records." The folder name is a property of the provenance record. A directory is not merely a container for files; it is itself a filesystem object with a name, a creation timestamp, a history. Git tracks it as part of the tree. The name appears in every commit message, every path-citation, every cross-reference. Mutating the name after close is mutating the record.

The operator's framing distinguishes "path-string updates only, no content mutation" from "edit closed-session content." I will argue in Q3 that this distinction is less clean than it looks. For Q2: if any rule is adopted, the window for choosing the folder name closes when the session closes. Current-session authority only.

Who decides? The session in progress. During Read/Assess the session may take the opening default. During Decide/Produce, once the content is clear, the session may rename. The rename operation is: change the directory name, update any internal references that were written in anticipation of the old name, and log the rename in the close file. This is current-session authority over current-session artefacts — unambiguously permitted.

Can the next session revise the previous session's name? No. That is D-017 violation. The next session can note in its own close that a prior folder was mis-named and recommend future readers consult SESSION-LOG for the true title. That note lives in the next session's record, not the previous one. This is the D-017 prescribed form: "errors or retractions are recorded in subsequent sessions, not by editing past records." Mis-naming is a class of error. The remedy is a note, not a mutation.

Interaction with D-017 is the whole question. The temptation the operator's framing invites is that a rename is so minor it deserves an exception. I want to name that temptation precisely. The exception would read: "D-017 applies to content, not to path-strings; path-strings may be updated retroactively to fix naming inconsistencies, provided no content is altered." That exception is corrosive for three reasons. First, it is a precedent. Once we say D-017 has a "narrow" class of permitted post-close edits, every future drift will reach for the same dispensation. Second, the boundary is not where it looks. Path-strings are cited inside content — the assessment files cite `provenance/025-session-assessment/...` as part of their narrative; renaming the folder without editing the citations creates broken paths, renaming it with editing the citations is content mutation. Third, git preserves the old path regardless; a rename produces a rename-commit that future readers must interpret, and they will ask "why did this rename happen" and the answer is "because a later session decided the old name was ugly" — which is exactly the post-hoc editorial authority D-017 exists to prevent.

So the authority rule is: current session only, before close. After close, the name is frozen. This is conservative. It is also the only rule consistent with D-017 as currently written.

## Q3. Should there be a retroactive rename of Sessions 023/024/025/026?

No. And I want to be specific about why each of the three options the brief enumerates is worse than inaction.

Option (a): leave text references stale. This means rename the folders but do not edit the citations inside them. The workspace becomes internally inconsistent — assessment files cite paths that no longer exist, commit messages point to renamed directories, archive-pack chunks reference containers with a different name. Anyone running a reference-validation pass (per reference-validation.md v2) will flag the broken citations. The fix for the broken citations is... to edit the closed-session content to update the citations, which is option (b). So (a) is either temporary inconsistency that forces (b) later, or it is permanent inconsistency that degrades the workspace's internal coherence indefinitely. Neither is acceptable.

Option (b): edit the text references inside closed-session folders. This is a direct D-017 violation. The operator's framing hedges "unless dispensed" — but a dispensation for four folders on aesthetic grounds is not a dispensation, it is a precedent. If we can dispense D-017 for "the folder name is ugly," we can dispense it for "the synthesis was imprecise," "the decision record had a typo," "the minority position was mis-characterised." Each of those has been raised in prior sessions and each time D-017 held. It holds because the rule is unconditional. Conditional D-017 is no D-017.

Option (c): narrower dispensation — path-string updates only, no content mutation, enumerated in a decision record. This is the option that looks reasonable. Let me dissect it.

The claim is that a path-string is mechanical enough that updating it is not really content mutation. I dispute the mechanicality. Consider a specific file: `provenance/025-session-assessment/05-close.md` contains (I infer from pattern) a line like "This session executed Path A at `provenance/025-session-assessment/path-a-execution.md`." If we rename the folder to `025-path-a-r2-conversion-check`, updating the self-reference requires editing the close file of a closed session. The edit is small but it is an edit. The file's git hash changes. The file's content — as a bytestream — is no longer what was written at close. Whatever a future reader pulls from git will have either the old name (if they pull the original commit) or the new name (if they pull the rename commit). The record bifurcates.

"Enumerated in a decision record" does not cure the bifurcation. The decision record documents what was done; it does not undo the fact that the files now read differently than they read at close. A future reader reconstructing Session 025's decisions must now read Session 025's files plus the Session 027 dispensation note to know what they are looking at. The provenance graph grows a new edge: "this file was edited post-close under dispensation D-XXX." That edge is exactly the thing D-017 was written to prevent from proliferating.

Further: the dispensation is not actually narrow. The brief says "path-string updates only, no content mutation." But a path-string inside a narrative sentence is content. "We executed Path A at `provenance/025-session-assessment/...`" contains a path-string; the sentence is a narrative claim about the session's trajectory; editing the path-string edits the sentence. The only fully mechanical path-strings are those in structured fields — the `originating_path` field in manifest.yaml, for instance. Editing a structured field is mechanical, yes, but it is also inside a file that carries other content, and the edit produces a hash change on the whole file. The boundary "path-string only" is a lexical distinction, not a semantic one. Semantically, any edit inside a closed-session file is a post-hoc edit.

I will also note the git-history asymmetry. Even if we edit the text references, git history points into the old paths. Every commit from Sessions 023-026 was made under the old names. A future reader doing `git log -- provenance/023-session-assessment/` sees the session's commits; a reader doing `git log -- provenance/023-<new-name>/` sees only the rename commit plus any post-rename edits. Which history is "true"? Both, in different senses. The rename creates a split: pre-rename history under old name, post-rename history under new name. Retroactive rename does not cleanly rewrite history; it adds confusion to history.

So my answer to Q3 is: do not rename. The cost of the four folders remaining as historical witnesses is the correct cost. They are exactly what D-017 predicts: honest artefacts of a period when the naming convention drifted. A future reader opening the workspace sees four folders with placeholder names, consults the SESSION-LOG, finds the real titles, and learns that the engine went through a naming drift. That learning is valuable. Scrubbing the folders hides the drift; keeping them documents it.

Analogy — and I flag this as `[pretrained-external]` since it is a rhetorical appeal rather than an engine-internal argument — archival practice in general holds that the job of an archive is to preserve the record, not to tidy it. Paper records with errors are annotated, not rewritten. Digital records are no different in principle.

The cost of keeping the four folders is bounded. Future readers will be mildly confused by the placeholder names; they will resolve the confusion by reading the synthesis or the SESSION-LOG; they will potentially observe the drift pattern and learn from it. The cost of renaming is unbounded: it sets a precedent for post-close edits that will be invoked every time a future session finds a prior session's artefacts aesthetically wanting.

## Q4. Should the opening default name change?

No strong opinion, leaning no. The current default `NNN-session-assessment` is a placeholder and placeholders have utility. Let me work through the candidates.

`NNN-opening`: cleaner, but still a placeholder, and it leaks a tiny amount of information (it says "this folder is an opening, not yet renamed") which could be a feature — a reader seeing `025-opening` immediately knows the session drifted without renaming. That is informative. But it also invites renaming-at-close as a standard expectation, which re-introduces the ceremony I argued against in Q1.

`NNN-<date-stamp>`: date is already in the provenance (session date is carried in file frontmatter per identity.md v2). Duplicating it in the folder name trades a placeholder for a timestamp that is both redundant and non-semantic. Worse than the current default.

`NNN-pending-title`: explicit, which is honest, but explicit-placeholder is a red flag that pressures every session to rename. That pressure is exactly what I'm arguing we should not mechanise.

`NNN-session-assessment`: the current default. "Session-assessment" is not meaningless — it literally describes activity 2 of the 9 (Assess), and every session does open with an assessment phase. The placeholder is semantically grounded in the methodology. A folder named `024-session-assessment` is honest: it says "this session did an assessment, and no substantive content warranted a rename." For Sessions 025 and 026, which produced no substantive decisions (D-090/D-091/D-092/D-093 all `[none]`), the placeholder is arguably correct. For Sessions 023 and 024, which did produce substantive content, the placeholder is a label regression, but the content is still there.

Is the current default a design bug? I do not think so. It is a useful placeholder that becomes a less-useful placeholder when the session content is substantive and no one renames. The alternative — a more-explicit placeholder that pressures renaming — trades a mild aesthetic cost (placeholder sticks when it should not have) for a mild process cost (placeholder screams "rename me" at every close). Neither is clearly better.

If forced to choose: leave the default alone. It has worked for sessions that remained genuinely assessment-only (015, 025, 026). It has failed to prompt rename for substantive sessions (023, 024). The failure is not in the default; it is in the informal convention that said "rename when substantive."

## Q5. Where should the rule live?

If a rule is adopted — and I repeat my Q1 position that it should not be — the lightest possible location is prompts/development.md under "How to operate." Not workspace-structure.md. Not the validator. Not a new OI.

Why prompts/development.md and not workspace-structure.md? The specifications in workspace-structure.md are load-bearing for the engine's correctness. A session that violates workspace-structure.md is broken in a structural sense — its files do not integrate with the rest of the workspace. A folder-naming convention is not structural in this sense. A session with a mis-named folder still integrates; the SESSION-LOG still carries the true title; the manifest.yaml still enumerates decisions; the read-contract still functions. The rule is operational, not structural. Operational guidance belongs in the operator's prompt.

Why prompts/development.md and not validation-approach.md? The 22-check validator enforces load-bearing invariants. Adding a 23rd check for folder-name-reflects-content requires defining what "reflects content" means, which is inherently editorial. Validator checks should be mechanical (e.g., "file exists," "frontmatter present," "decision record has required fields"). A "does this name reflect the content" check is aesthetic — it cannot be mechanised without either (a) a heuristic that will produce false positives and negatives, or (b) a human judgement call dressed in a checklist. Either degrades the validator's precision.

Why prompts/development.md and not a new OI? OIs accumulate. The engine has 13 active OIs already. Each OI imposes a continuing attention cost — the session must check whether the OI fires, document the check, and preserve the OI's invariant. A folder-naming OI would be one of the lowest-stakes OIs ever written, and it would sit alongside OIs that govern load-bearing concerns like minority preservation and substantive-vs-minor heuristics. The signal-to-noise ratio of the OI list degrades with every low-stakes addition. OI-007 is again on point: scaling pressure on governance surfaces.

So if a rule is written, it is a single sentence in prompts/development.md: "When producing the close file, if the session produced substantive output, consider renaming the session folder to reflect that output; if renaming, do so before the close commit so the folder name is part of the closed state." That is advisory, it is co-located with operator guidance, it does not create a validator check, and it does not create a new OI.

The tradeoff of prompts/development.md versus workspace-structure.md: prompts/development.md is advisory and can be ignored without breaking the engine; workspace-structure.md is normative and ignoring it creates a defect. The folder-naming rule is advisory in character. Putting it in a normative location creates a category error — a non-structural rule living in the structural spec.

The tradeoff of prompts/development.md versus nowhere: prompts/development.md gets read; nowhere does not. If the rule exists at all it needs a home that the operator consults. prompts/development.md is the natural location for operational conventions.

## Q6. Is this class of drift governable by the mechanism I propose?

No, and this is the most important observation the operator's flag surfaces.

The drift was that four consecutive session closes adopted the placeholder folder name despite Sessions 023 and 024 producing substantive output. Sessions 024, 025, and 026 each conducted their own Session N-1 synthesis-fidelity audit. None of those audits flagged the folder naming. The audit machinery looked past the drift for three successive opportunities.

This tells us something about the audit mechanism. The synthesis-fidelity audit checks whether the prior session's synthesis faithfully represents the deliberation's content. Folder names are not synthesis content. They are meta-data about the provenance container. The audit looked at the right thing and missed the thing it was not looking at. This is a feature of any audit mechanism: it sees what it is pointed at and is blind to everything else.

Propose a folder-naming check: we add a 23rd validator item, or a close-step, or an OI-fires-at-close. That check would catch this specific drift. It would not catch the next drift — the drift that happens in a surface nobody has added a check for. The pattern is: something drifts, a check is added, the next drift happens elsewhere, another check is added, and the check-count grows without bound.

This is the deeper limitation the operator's observation exposes. Single-session self-audits are structurally unable to see drifts in surfaces that the audit prompt does not name. The audit prompt for Session N-1 synthesis-fidelity does not name folder-naming; therefore the audit does not see folder-naming drift. The audit prompt for the validator does not name folder-naming; therefore the validator does not see folder-naming drift. No audit named folder-naming, so folder-naming drifted unobserved for four sessions.

The remedy is not to add folder-naming to every audit prompt. That solves this specific case and prepares to miss the next one. The remedy — and I offer this tentatively — is a periodic audit whose prompt is not "does X hold?" but "what has drifted?" That is an open-ended audit, an audit without a target. It is what the operator just performed at Session 027 open. The operator looked at the workspace, observed a pattern, and flagged it. That act is the mechanism. The mechanism is human attention applied openly, not mechanism-plus-mechanism-plus-mechanism applied narrowly.

If we formalise anything from Session 027, it should not be a folder-naming rule. It should be a note that periodic open-ended audit — "look at the workspace with fresh eyes; flag what looks off" — is itself an engine-level practice. That practice is what caught this drift. Mechanising the specific catch (folder names) would not have caught this drift at Session 023 or 024 or 025; only the open-ended attention at Session 027 caught it. Preserve the mechanism that worked. Do not replace it with a more specific mechanism that would not have worked.

I am aware this argument could be used to justify never adding any check. I am not arguing that. Checks have a place — for load-bearing invariants that must hold session-to-session. Folder names are not load-bearing. Minority preservation is. Reference validity is. Read-contract honouring is. The distinction is: check what must not fail, do not check what is merely nice to have.

OI-007 scaling pressure is the backstop for this argument. Every addition to the audit surface pulls attention from existing audit surface. The engine has finite attention per session. Adding a folder-name check makes it marginally more likely that a load-bearing check is performed less carefully. The marginal cost of a low-stakes check is a marginal degradation of high-stakes checks. For folder names, that trade is bad.

So the class of drift the operator surfaced — cosmetic-but-accumulating regression in a non-load-bearing surface — is governable only by periodic open-ended human attention. It is not governable by adding a new check. And the honest answer to "how do we prevent the next such drift?" is: we do not prevent it, we observe it and flag it when it accrues, the way the operator just did.

## Concluding summary

Do not formalise a folder-naming rule beyond a single advisory sentence in prompts/development.md; do not retroactively rename Sessions 023-026 under any dispensation, however narrowly framed, because "path-string only" is not a clean boundary and the precedent corrodes D-017; and acknowledge that the underlying class of drift — non-load-bearing surfaces accumulating cosmetic regressions — is governed by periodic open-ended human attention, not by adding more checks to an already-saturated audit surface.
