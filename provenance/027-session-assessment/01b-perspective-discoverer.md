---
session: 027
title: Perspective — Discoverer
date: 2026-04-23
status: complete
perspective: discoverer
committed_at: session-027-independent-phase
---

# Perspective — Discoverer

## Q1. Should the engine formalise a folder-naming discipline?

Yes. The engine should formalise a folder-naming discipline, and my reasoning starts from what folder names actually do in this workspace.

Folder names in `provenance/` are addresses. They are the primary index by which a future reader — operator, Claude in session N+k, or an external reviewer — finds prior work. A future reader does not start by grepping the full content of every session; they scan the folder listing. The folder name is the answer to "what happened here?" before any file is opened. This is not aesthetic. It is load-bearing for discoverability, which is itself load-bearing for the engine's compounding property: later sessions build on earlier ones by finding and reading them, and the cheaper finding is, the more reliably the compounding works.

The current state has four consecutive folders named `session-assessment`. Two of them (023, 024) contain substantive engine work — the engine-v4 bump with read-contract.md v1→v2, and D-088 A.4 carry-the-warning with R6 cleanup. A reader scanning `provenance/` today sees four identical-looking bins and must open each to discover which contains the engine-v4 transition. This is exactly the regression the operator surfaced. It compounds: the longer it persists, the more the workspace's self-index degrades, and the more each future session spends on orientation rather than work.

**The rule I propose:**

At session close, if the session produced **any** substantive output — a decision record containing non-`[none]` reductions, a new or revised specification (OI-002 substantive-revision threshold), a new deliberation or explicit recognition of new structure, a pattern that will be referenced by future sessions — then the folder MUST be renamed from the `NNN-session-assessment` default to a descriptive slug reflecting the session's load-bearing content. The slug follows the form `NNN-<kebab-case-descriptor>` and should be short enough to scan in a folder listing (target ≤ 6 tokens after the session number) and specific enough that a reader can guess the content without opening anything.

If the session produced no substantive output — Path A execution with all reductions `[none]`, or pure assessment with no artefacts beyond the assessment itself — then the folder MAY remain `NNN-session-assessment`, following Session 015 precedent. This is the placeholder's legitimate use case: signalling "this session generated no addressable work."

**What goes wrong if nothing changes:**

Three things go wrong, each of which I can name concretely.

First, the self-index degrades monotonically. Every future session where substantive work lands in a placeholder-named folder adds another opaque bin to the workspace. Discoverability is a function of the whole folder listing, not individual folders, so the damage is cumulative and non-local.

Second, audits fail silently. Sessions 024, 025, and 026 each ran a synthesis-fidelity audit on their predecessor and none surfaced this drift. That is itself diagnostic data about what single-session audits can and cannot see. Without a rule, the class of "ran correctly, produced no flag" covers both "everything was fine" and "the auditor's attention was shaped by the same drift pattern." An explicit rule gives audits a thing to check.

Third, the engine's ability to reference prior sessions by semantic address weakens. When someone writes "see the engine-v4 bump in 023-session-assessment" the reference is correct but unhelpful; the reader needs a map between session numbers and content that the folder listing should be providing for free.

So formalise it.

## Q2. When should the folder name be chosen or revised, and who has authority?

**When:** At session close, as part of the Close activity.

The open-step default remains `NNN-session-assessment` because at open we genuinely do not know what the session will contain — the assessment itself is one of the first activities. Forcing a name at open would either require renaming mid-session anyway (the current state) or would encourage premature commitment to a framing that the assessment might overturn. The default is appropriate for open; the drift is that we never update it at close.

**Who:** The current session, as the final step of Close. Specifically: after the close-log is drafted and decision records are written, before the commit, the operator (or Claude, instructed by the operator) renames the folder if the session produced substantive output. The rename is part of the same commit that records the close.

**Interaction with D-017:** This is where I want to be careful and precise, because D-017 is the load-bearing constraint, and my view is that it has been over-read.

D-017 says: "Provenance records are immutable once the session closes. Errors or retractions are recorded in subsequent sessions, not by editing past records." The phrase "provenance records" refers to **content** — what was written, what decisions were recorded, what reasoning was preserved. The purpose of D-017 is to prevent history rewriting: you cannot silently fix a past mistake by editing its record; you must record the correction in a subsequent session.

A folder name is not content. It is the address at which content is located. Renaming a folder changes where the content is found; it does not change what the content says. The distinction matters because:

1. **No information is lost by rename.** Git history preserves the old path; `git log --follow` recovers it. The mv operation is tracked.
2. **No decision is silently overturned.** The content of decision records inside the folder is unchanged.
3. **The close-step rename happens *before* session close.** If we specify that rename is part of Close, it occurs while the session is still live. D-017's "once the session closes" clause has not yet triggered.

For forward discipline, this is clean. Close-step rename operates under the authority of the current session; the session is not yet closed at rename time; D-017 does not apply.

**For the previously-closed sessions (023, 024, 025, 026):** D-017 *does* apply because those sessions are closed. But I argue the relevant question is whether renaming a closed folder constitutes "editing a past record." I contend it does not — for the reasons above — but I acknowledge this is a reading that the engine should make explicit rather than assume.

The cleanest path: Session 027 issues a narrow dispensation (see Q3) that enumerates exactly what retroactive edits are permitted, the dispensation itself is a permanent decision record, and from that point forward the close-step rename rule makes the problem self-correcting.

**Authority for retroactive rename:** The session that flags the drift (here, Session 027). Not the drifted session (which cannot edit itself after close), not an arbitrary future session (which weakens the principle that corrections are recorded promptly), but the session that identifies the problem and issues the dispensation in the same session.

## Q3. Retroactive rename for Sessions 023/024/025/026?

**Yes for 023 and 024. Yes, probably, for 025 and 026 — for symmetry and clarity.**

Sessions 023 and 024 produced substantive output. A reader looking for the engine-v4 transition or the D-088 A.4 carry-the-warning work currently finds folders whose names reveal nothing. This is the core regression. Rename is the repair.

Sessions 025 and 026 executed Path A with all reductions `[none]`. Under the Session 015 precedent, the placeholder name is legitimate for sessions that produced no substantive output. I am genuinely torn here. Two considerations pull different directions:

- **Keep 025/026 as `NNN-session-assessment`:** This preserves the signal that "this session generated no addressable work." A reader scanning the listing sees two `session-assessment` folders and correctly infers they contain only assessments. This aligns with Session 015 precedent and treats the placeholder as a meaningful marker rather than a bug.

- **Rename 025/026 to something descriptive:** The SESSION-LOG titles for 025 and 026 are actually informative — "Path A Executed — Carry-the-Warning Continues" and "Path A Executed — D-086 R9 Cadence-Escalation Window Ages Out". A rename to `025-path-a-execution-carry-the-warning-continues` and `026-path-a-d086-r9-ages-out` would preserve information that is currently only in the close-log title. The cost: four `session-assessment` folders becomes zero, which loses the "no substantive output" signal.

I lean toward renaming 025 and 026 too, for these reasons:

1. The SESSION-LOG title already carries distinguishing information; the folder name should reflect that rather than collapse it.
2. The rule "placeholder means no substantive output" is fragile — it requires every future reader to know the convention. An explicit marker (e.g., `025-path-a-no-reduction` or a metadata tag) is more robust than relying on folder-name absence-as-signal.
3. Symmetry simplifies the rule: "at close, rename to reflect content" with no fork based on substantive/non-substantive is easier to follow and audit.

But I am willing to be argued out of this by the Archivist or Minimalist if they hold that Session 015 precedent should govern. My stronger claim is the retroactive rename for 023/024; the 025/026 question is secondary.

**The dispensation — scoped and specific:**

I propose a decision record in Session 027 with the following form:

> **D-NNN: Retroactive folder-name correction for Sessions 023/024 [025/026].**
>
> Scope: Rename the following folders in the `provenance/` tree:
> - `023-session-assessment/` → `023-read-contract-engine-v4-bump/`
> - `024-session-assessment/` → `024-mad-6k-soft-warn-a4-carry-warning/`
> - [Optionally: `025-session-assessment/` → `025-path-a-carry-warning-continues/`]
> - [Optionally: `026-session-assessment/` → `026-path-a-d086-r9-ages-out/`]
>
> Permitted edits during this rename:
> 1. `git mv` of the folder itself.
> 2. Update of path strings *inside the renamed folder* where those strings are self-references to the folder's own path. Specifically: manifest.yaml `path` fields; assessment files' self-citations; archive-pack container references; close-log commit-path statements. The enumeration is closed: only these four categories.
> 3. Update of path strings in SESSION-LOG.md and any active specification that references the renamed folders, to point to the new paths.
>
> Forbidden edits:
> 1. Any mutation of decision-record content (D-NNN text, reductions, reasoning).
> 2. Any mutation of deliberation content (perspectives, synthesis, judgment).
> 3. Any mutation of commit messages (git history is not rewritten).
> 4. Any mutation of files outside the enumerated categories.
>
> Authority: Session 027 operator authorises; Claude executes under operator supervision.
>
> Validation: After rename, `grep -r "023-session-assessment"` (and the other three old names) over the workspace should return zero matches except in this decision record and in git log output. A follow-up session MAY audit this.
>
> Rationale: D-017 protects content immutability. Folder names are addresses, not content. Path strings inside content that are self-references are tracking metadata, not reasoning or conclusions; updating them to match the new address is a coherence repair, not a content mutation. The enumeration closes the dispensation so it cannot be quietly widened by future sessions.

This is the dispensation I would argue for. Note the features:

- It is specific about what may and may not be edited.
- It is enumerated — four categories of permitted edit, four categories of forbidden edit, closed lists.
- It is auditable — a grep either confirms coherence or reveals a miss.
- It is permanent — the decision record itself cannot be edited, so the dispensation's scope is locked.
- It does not generalise — future retroactive renames require their own decision records.

**Cost of doing nothing (leaving 023/024 as historical witnesses to the drift):**

The operator's framing "historical witnesses" has aesthetic appeal — the workspace preserves its own mistakes as memento mori, and this is a kind of honesty. But I think this trades too much discoverability for too little pedagogy. The lesson ("we drifted for four sessions; here is the rule that fixes it") is fully captured by the Session 027 decision records themselves. The folder names do not need to bear that pedagogical load. Keeping them stale is a form of monument-building that future readers pay for in search cost.

Also: "historical witness" framing works once. If the engine drifts again — and it might — we cannot leave *every* drift as a monument. The workspace would accumulate these. The principle should be: record drift explicitly in decision records; repair the addresses so discoverability is preserved; let the monument live in the decision record, not in the folder tree.

## Q4. Should the opening default name change?

I lean toward **keeping `NNN-session-assessment` as the opening default**, with one caveat.

The placeholder has a job: mark a folder whose content is not yet known because the session is still in Assess. Alternatives have problems:

- `NNN-opening`: Loses the signal that Assess is the primary opening activity. Less informative.
- `NNN-<date-stamp>`: Redundant with commit timestamps; adds noise to the folder listing.
- `NNN-pending-title`: More honest about the placeholder status but longer and uglier.
- `NNN-tbd`: Short, but cryptic to external readers.

`NNN-session-assessment` actually describes what is happening at open — the session starts with assessment — and transitions naturally once the close-step rename rule is in force: the folder begins as a literal description of its opening activity and is renamed at close if substantive output justifies it.

**The caveat:** If the close-step rename rule is *not* adopted (Q1 answered no), then the current default is a design bug: it silently becomes a permanent name when the rename step is skipped. The placeholder is only acceptable because it is temporary. If we cannot guarantee the rename step happens, the placeholder becomes misleading and we should switch to something that reads more obviously as "to be named" — perhaps `NNN-pending-title` or `NNN-open`.

In short: the current default is a useful placeholder *conditional on a reliable rename mechanism*. Without the mechanism, it is a design bug.

## Q5. Where should the rule live?

**Primary location: `workspace-structure.md` §provenance.**

The rule is about workspace layout — how the provenance directory tree is organised — which is exactly what `workspace-structure.md` governs. It fits naturally as an extension of existing text about folder structure.

I would add a subsection along these lines:

> **§provenance.folder-names**
>
> Provenance folders follow the pattern `provenance/NNN-<descriptor>/` where NNN is the zero-padded session number and `<descriptor>` is a kebab-case slug describing the session's load-bearing content. At session open, the default descriptor is `session-assessment`. At session close, if the session produced substantive output (per OI-002 substantive-revision threshold applied broadly to any non-`[none]` decision, specification change, or recognised pattern), the folder MUST be renamed to a descriptive slug reflecting content. If the session produced no substantive output, the folder MAY remain `NNN-session-assessment` per Session 015 precedent.
>
> The close-step rename is performed before the close commit. Validation: the close-log commit message references the final folder name; no path strings inside the folder reference an old name.

**Secondary location: `prompts/development.md` §How to operate.**

A brief reference to the rule in the operational prompt, pointing to `workspace-structure.md` for the full statement. Something like: "At Close, rename the provenance folder to reflect content if substantive output was produced (see workspace-structure.md §provenance.folder-names)."

**Why not only in development.md?**

Because operational prompts change more frequently than specifications, and a rule that defines workspace structure should live where structure is defined. Putting it only in development.md makes it feel procedural rather than structural; putting it only in workspace-structure.md makes it easy to miss during session execution. Both locations, with the canonical statement in the spec, is the pattern the engine already uses for other structure-touching rules.

**Tradeoff against single-location:** Two locations is mild duplication. But the duplication is pointer-style (development.md references the spec), which is the right pattern for rules that span structural and operational concerns.

**This is a substantive spec revision**, triggering OI-002 and an engine-v bump to engine-v5. I think the rule is substantive enough to warrant that — it changes a previously-informal practice into a specified one, and it authorises retroactive edits (via the dispensation mechanism) that were previously unprecedented. A version bump signals to future sessions that a structural rule changed.

## Q6. Self-observability and the class of drift

This is the question that most concerns me, and I want to give it real weight.

The operator's observation is data about the engine's self-observability — specifically about what single-session audits can and cannot see. The drift ran for four sessions. Three of those sessions (024, 025, 026) ran synthesis-fidelity audits on their predecessor. None flagged the folder-name drift. The operator flagged it on casual inspection at Session 027 open.

What does this tell us?

**One thing it tells us:** The audits were looking at the right level for their scope. A synthesis-fidelity audit checks whether Session N-1's close-log faithfully represented what happened during the session — it reads the deliberation, the decision records, the commits, and verifies the close narrative matches. This is a *content* audit. The folder name is not in scope for a content audit, because the audit looks inside the folder, not at the folder. The audit operates at the wrong altitude to see its own container's name.

**A second thing it tells us:** Drift that affects the index (folder names, file organisation, cross-reference paths) is systematically invisible to audits that read the index. An audit that opens `provenance/024-session-assessment/close.md` is not surprised by the folder name; it treats the folder name as given. The drift is in the frame, not in the picture.

**A third thing it tells us:** Casual external inspection — the operator glancing at the folder listing — can catch drift that structured internal audits miss. This is not a failure of the audits; it is a property of the class of drift. Index-level drift needs index-level audit, which means looking at the listing *as a listing*, not at the contents of individual folders.

**Can the mechanism I propose govern this class of drift?**

Partly. The close-step rename rule prevents new instances of this specific drift (folder-name misalignment with content). But it does not prevent the broader class — index-level drift in general. Future drift might be in file naming conventions, in manifest.yaml field conventions, in archive-pack organisation, in cross-reference patterns. Each would be invisible to content-audits for the same reason.

**What I think the deeper finding is:**

The engine needs a distinct audit altitude: an **index audit** that periodically examines the workspace as a listing, without opening individual files. This would catch:

- Folder-name drift (the current instance).
- File-naming inconsistency across folders.
- Missing manifest.yaml files or drifted manifest structure.
- Path-reference drift (references to moved or renamed files).
- Unlinked files (files that exist but are not referenced from any index).

An index audit is cheap — it is mostly `ls`, `grep`, and pattern-check — and it operates at the altitude that content-audits cannot. I would propose it as a periodic activity (every N sessions, or at version bumps) rather than every-session, because index drift is typically slow.

**But I do not want to propose the full audit mechanism in this session.** The immediate task is to fix the folder-name drift and specify the discipline. The audit mechanism is a follow-on that Session 027's close-log could flag as an Open Item for a future session to take up.

**Is this a deeper limitation of single-session self-audits?**

Yes, partially. Single-session self-audits are constrained by scope — they look at what they are pointed at. They cannot spontaneously broaden their attention to notice things outside their frame. The mechanism proposed (close-step rename; retroactive dispensation) governs the specific drift but does not address the audit-altitude gap.

The honest framing: the rule I propose prevents recurrence of *this* drift pattern. It does not generalise. A second rule — index audits at version bumps, or whenever a session notices "a lot of self-referential folder names" or similar heuristics — would be the complementary governance. I gesture at this but do not propose it fully here, because Session 027's load-bearing decisions are about the immediate problem, and adding a second rule risks overloading this session's output.

So: governable in part by my proposed rule; the deeper limitation is real and deserves its own session.

---

## Concluding summary

**Top-line recommendation:** Formalise a close-step folder-rename rule in `workspace-structure.md` (engine-v5 bump under OI-002), and issue a scoped dispensation in Session 027 to retroactively rename Sessions 023 and 024 (and probably 025/026) with a closed enumeration of permitted path-string updates — because D-017 protects content immutability, not address immutability, and the workspace's discoverability is load-bearing enough to justify both the forward discipline and the bounded retroactive repair.
