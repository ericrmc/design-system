---
title: Workspace Structure
version: 5
status: active
created: 2026-04-17
last-updated: 2026-04-23
updated-by-session: 036
supersedes: workspace-structure-v4.md
---

# Workspace Structure

## Purpose

This specification defines how the workspace is organized: what directories and files exist, what each contains, and how they relate. It ensures that any agent or person reading the workspace can orient themselves quickly and knows where to find — and where to put — each kind of content.

Version 5 (Session 036, D-113 + D-116) adds the `MODE.md` workspace-identity-file convention, the `engine-feedback/` directory with mode-dependent outbox/inbox semantics, and the §10.4 first-class-minority block preserving six Session 036 Path PD minorities. v4 preserved as `workspace-structure-v4.md`.

Version 4 (Session 022, D-084) adds the `open-issues/` directory split (replacing the single `open-issues.md` file per the v3 §open-issues split-authorisation clause), adds cross-references to `specifications/read-contract.md` (new v1 specification governing default-read vs archive surface distinction), and adds the archive-surface subdirectory convention (`provenance/NNN-title/archive/`). v3 preserved as `workspace-structure-v3.md`.

Version 3 (Session 017, D-074) adds the three file-class distinction (engine-definition / development-provenance / application-scope) and documents `prompts/` as a new directory created by the PROMPT.md split. v2 preserved as `workspace-structure-v2.md`.

## Specification

### File classes (added v3, extended v5)

Under the three-layer denotation established in `identity.md` v2 (Selvedge methodology / Selvedge engine / application), workspace files fall into one of four classes (v5 adds the workspace-identity class).

- **Engine-definition files** — the loadable Selvedge engine. An external application workspace may (and should) clone this set without inheriting development-provenance. Enumerated canonically by `specifications/engine-manifest.md`. At `engine-v1`: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `specifications/*.md` (all active files in the `specifications/` directory), `tools/validate.sh`.
- **Workspace-identity files** (added v5) — per-workspace identity declarations created at initialisation time. Distinct from engine-definition because each workspace has its own content (not copied byte-identically from the engine). Includes `MODE.md` at workspace root (required from Session 001 of any new workspace per `PROMPT.md` §Session-001 obligation). See §MODE.md below.
- **Development-provenance files** — the self-development application's own accumulated history. Not part of the engine load; not inherited by external-application workspaces by default. Includes `SESSION-LOG.md`, `open-issues/`, and `provenance/`.
- **Application-scope files** — per-application content (inputs, outputs, application-specific briefs and notes). Mutable per the `applications/` directory rules below. Organised as `applications/NNN-<slug>/`.
- **Non-engine operator-managed content** — content that is neither engine-definition nor development-provenance nor application-scope but serves operator coordination. Includes `engine-feedback/` (added v5; see §engine-feedback below).

The normative rule: an external application workspace may load the engine-definition set as a read-only unit (or a cloned starting point) without inheriting development-provenance. The self-development application (this workspace) carries all four classes by construction (the engine is being developed here; the provenance is the development record; the applications are the by-products; the workspace-identity marker names what this workspace is).

### Top-level structure

The workspace has the following top-level structure:

```
/PROMPT.md
/MODE.md                       (workspace-identity; added v5)
/prompts/
  development.md
  application.md
/SESSION-LOG.md
/open-issues/
  index.md
  OI-NNN.md      (one file per open issue)
  resolved/
    OI-NNN.md    (one file per resolved issue)
/specifications/
/provenance/
  NNN-title/
    00-assessment.md
    01-brief-shared.md       (if preserved separately)
    01X-perspective-<role>.md
    01-deliberation.md
    02-decisions.md
    03-close.md
    manifests/
    participants.yaml
    archive/                 (if over-threshold raws were archive-packed per read-contract.md §4)
      <slug>/
        manifest.yaml
        0N-chunk.md
/tools/
/applications/
/engine-feedback/              (optional; added v5; mode-dependent semantics)
  INDEX.md                     (default-read in self-development mode when present)
  inbox/                       (self-development workspace: operator-deposited feedback from external workspaces)
  triage/                      (self-development workspace: per-feedback triage records)
  EF-<id>.md                   (external workspace: outbox feedback files)
```

### PROMPT.md

The bootstrap prompt. Under v3 (D-074, Session 017) `PROMPT.md` is a thin **dispatcher**: it names the three layers (methodology / engine / application), names the two operating modes (self-development and external-problem), and points to the two mode-specific executable prompts in `prompts/`. It is part of the engine-definition file class. It may be revised, but any revision is a significant event and recorded in provenance (as it was when the v3 split occurred in Session 017, and as it was in Session 036 D-113 when §Dispatch was revised to consult `MODE.md` as authoritative signal with structural-signature fallback).

The self-development application's executable content was moved to `prompts/development.md`; the template for external-problem applications lives at `prompts/application.md`.

### MODE.md (added v5)

`MODE.md` is a **workspace-identity file** at workspace root, required from Session 001 of any new workspace. It declares the workspace's operating mode to `PROMPT.md` §Dispatch.

Frontmatter schema:

```yaml
---
mode: self-development | external-problem
workspace_id: <short stable identifier>
created_session: 001
engine_version_at_creation: <e.g., engine-v7>
---
```

For external-problem workspaces, `MODE.md` additionally carries `application_brief: applications/NNN-<slug>/brief.md`.

For pre-existing workspaces that adopt `MODE.md` after Session 001 (the one-time retroactive-adoption case), the frontmatter additionally carries `marker_adopted_session: NNN` and `engine_version_at_marker_adoption: engine-vM`.

**Classification**: workspace-identity (not engine-definition). Each workspace has its own `MODE.md` with its own content; the file is not copied byte-identically across workspaces the way engine-definition files are. External application workspaces create their own `MODE.md` during Session 001 initialisation per `specifications/engine-manifest.md` §6 bootstrap contract.

**Validation**: `tools/validate.sh` check 23 (added engine-v7 per D-116) verifies `MODE.md` presence at workspace root and that its `mode:` frontmatter value is a recognised token (`self-development` | `external-problem`).

**Default-read discipline**: `MODE.md` is included in the default-read surface per `specifications/read-contract.md` v4 §1 item 0.

**Revision**: `MODE.md` is append-history-discipline but not immutable across the session boundary — an operator may legitimately correct a mis-declared mode or promote a workspace from one mode to another (though the latter is a load-bearing event warranting explicit decision record in the source workspace's provenance). The v-suffix supersession discipline (for specifications) does not apply to `MODE.md` because it is identity, not specification.

### prompts/

Contains the two mode-specific executable prompts created by the D-074 split. Part of the engine-definition file class.

- `prompts/development.md` — the self-development application's executable prompt. Carries the content that was in the pre-split `PROMPT.md` (minus the high-level framing moved up into the dispatcher), reframed as the engine's own self-development. This workspace's current application loads this file.
- `prompts/application.md` — the template for external-problem applications. Loads the engine by reference (engine-manifest), names the slots an external application fills (problem statement, constraints, stakeholders, success condition, initial state), and declares that development-provenance is NOT part of the application's context unless explicitly imported. An external application workspace copies this file (typically renamed to `PROMPT.md` in the new workspace, or loaded from its canonical location here) and fills in the slots.

Both files are revisable under the methodology's spec-revision discipline (significant revisions recorded in provenance; v-suffix preservation if substantive changes accumulate).

### SESSION-LOG.md

A thin one-line-per-session index for quick orientation. Each entry is one Markdown table row containing the session number, date, title, and a one-sentence summary of the decision surface. The canonical detail for each session lives in its provenance `03-close.md` file; the SESSION-LOG entry is an index over that detail, not a replacement.

SESSION-LOG.md is default-read surface per `specifications/read-contract.md` §1 and must satisfy the default-read per-file budget (currently 8,000 words hard ceiling, 6,000 words soft warning). A long-form per-session summary that would push SESSION-LOG.md over budget belongs in `03-close.md`, not in SESSION-LOG. This file is updated at the close of each session.

The post-Session-022 thin-index form replaces the pre-Session-022 variable-length-summary form per Session 022 R8a; the pre-Session-022 SESSION-LOG content is preserved in `provenance/022-workspace-scaling-trajectory/archive/pre-R8a-SESSION-LOG/` as an archive-pack witness.

### open-issues/

A directory containing the workspace's known questions, gaps, uncertainties, and unresolved disagreements. Each issue lives in its own file `OI-NNN.md` (where NNN is the OI number, zero-padded if necessary to sort correctly). A thin index `open-issues/index.md` lists all active OIs with one-line status summaries; `open-issues/resolved/` holds resolved issues with reference to the session that resolved them.

The `open-issues/` directory replaces the pre-Session-022 single `open-issues.md` file. The split was authorised by the v3 "unless the number of issues makes a single file unwieldy" clause and is exercised in Session 022 per D-084 R8b.

Per `specifications/read-contract.md` §1, `open-issues/index.md` is default-read surface; per-OI files (`OI-NNN.md`) are default-read when relevant to the session's work and archive-surface-accessed otherwise (the thin-index-plus-relevant-detail pattern).

Each `OI-NNN.md` carries:
- Frontmatter: `id`, `surfaced-in-session`, `status`.
- Brief description of the issue.
- Full historical annotation record (lossless preservation of prior `open-issues.md` content for each OI).

### specifications/

Contains the living specifications that describe the methodology's current state. Each specification is a Markdown file with YAML frontmatter:

```yaml
---
title: [what this specifies]
version: [integer, starting at 1]
status: draft | active | superseded | deprecated
created: [date]
last-updated: [date]
supersedes: [path to prior version, or "none"]
---
```

The body of each specification has three sections:

1. **Purpose** — What this specification governs and why it exists
2. **Specification** — The normative content
3. **Validation** — How to verify this specification still describes reality

When a specification undergoes substantive revision, the prior version is preserved with a version suffix (e.g., `workspace-structure-v1.md`) and the new version takes the canonical filename. Minor corrections are committed through git without file-level versioning.

Superseded-status specifications (those carrying frontmatter `status: superseded`) are archive-surface per `specifications/read-contract.md` §3; they are not default-read at session open but remain preserved verbatim and accessible by explicit reference via their `-vN.md` filenames.

Status lifecycle:
- **draft** — Proposed but not yet deliberated and accepted
- **active** — Deliberated, accepted, and governing
- **superseded** — Replaced by a newer version (the `supersedes` chain connects them)
- **deprecated** — No longer relevant because the thing it governed no longer exists

### provenance/

Contains the historical reasoning records. Organized by session:

```
/provenance/
  /001-genesis/
    00-survey.md
    01-deliberation.md
    02-decisions.md
  /002-[title]/
    ...
```

Each session's provenance is a numbered directory. Files within are numbered for reading order. All provenance files use Markdown with YAML frontmatter:

```yaml
---
session: [number]
title: [title]
date: [date]
status: complete | in-progress
---
```

Provenance records are **immutable** once the session closes. Errors or retractions are recorded in subsequent sessions, not by editing past records.

**Folder-name discipline** (added v4, Session 027 per D-094, minor amendment): at session open, the provenance folder is created as `NNN-session-assessment` (where NNN is the zero-padded session number). The folder name is **permanent**: it is not revised at session close and is not revised by subsequent sessions. Discoverability of session content is carried by `SESSION-LOG.md` (thin-index), which holds each session's descriptive title; the folder name is the container address, not the thin-index. Sessions 017-022 that received content-reflective folder names (`017-oi017-reframing-deliberation` through `022-workspace-scaling-trajectory`) are historical artefacts of an informal pre-Session-027 convention and are not retroactively altered (D-017 immutability). Session 015 and Sessions 023-026 retained the opening default and are likewise preserved as-is. This clause codifies operational behavior already in practice from Session 023 onward; it introduces no new close-step obligation and no new validator check. Minority positions preserved at Session 027 per D-094 (see `provenance/027-session-assessment/02-decisions.md`) include: a close-step rename-when-substantive discipline (Discoverer); a change of opening default from `NNN-session-assessment` to `NNN-session` (Minimalist); and an advisory-only placement in `prompts/development.md` (Archivist). Each minority has a documented activation warrant; none fires at Session 027 close.

**Archive-pack subdirectory** (added v4): when a session's raw perspective file or other provenance file exceeds the default-read per-file budget (`specifications/read-contract.md` §2), the file is archive-packed before session close per `read-contract.md` §9. Archive-packs live at `provenance/NNN-title/archive/<slug>/` with `manifest.yaml` + numbered chunks. Retroactive migration of a closed session's over-budget file uses the copy-plus-reference discipline (Session 009 D-054 precedent): the archive-pack is created in the migrating session's provenance directory, not the originating session's directory, preserving D-017 immutability.

### tools/

Contains tooling that supports the methodology's operations. Tools are executable scripts or programs that automate aspects of the methodology (e.g., validation, reporting). Each tool should have a corresponding specification in `specifications/`.

Current contents:
- `validate.sh` — Two-tier validation tool (see `specifications/validation-approach.md`)

### applications/

Contains **external artefacts** — work-products the methodology has produced for use outside the workspace (specifications, sequences, templates, design fragments, and the like). Organized by the session that originally produced the artefact:

```
/applications/
  /NNN-[slug]/
    [artefact-files]
```

`NNN` is the producing session's number; `[slug]` is a short descriptive name. Filenames within the directory are descriptive (not numbered for reading order) — the numbered-reading-order convention applies to provenance records only.

External artefacts are **mutable**: they may be revised by later sessions in response to domain validation (see `methodology-kernel.md` §7 Domain validation) or other feedback. Revisions update the artefact in place; the revising session's provenance records what changed and why. When an artefact is revised, any corresponding copies in the originating session's provenance directory and in prior revising sessions' provenance remain untouched (per the provenance immutability rule) and serve as historical witnesses to earlier versions.

Each external artefact file includes in its frontmatter the fields `originating_session` (the session that first produced the artefact) and, when applicable, `regularized_in_session` (the session that moved the artefact into `applications/` after the fact) and `provenance_witness_path` (the path to the frozen provenance copy, if one exists). Subsequent revisions update `last-revised-session` in the frontmatter.

**Regularization of pre-existing external artefacts.** When an external artefact was placed in a producing session's provenance directory before `applications/` existed as a defined top-level directory, the artefact is regularized into `applications/` by **copy-plus-reference**: a copy is made to `applications/NNN-[slug]/[filename]` with the frontmatter fields above; the provenance copy is not moved, modified, or deleted. The regularizing session's decision record is the authoritative cross-reference.

### engine-feedback/ (added v5)

An optional, mode-dependent top-level directory for operator-mediated engine/methodology feedback flowing from external-problem applications back to the self-development source workspace. Non-engine-definition; not copied when the engine is cloned.

**In external-problem workspaces**, the directory is an **outbox**: the operator places feedback files here when external-application practice surfaces methodology-level friction (unclear spec, kernel §7 gap, dispatcher ambiguity, MAD v4 awkwardness, reference-validation exercise gap, or equivalent). Feedback files should use the naming convention `EF-<external-session-number>-<short-slug>.md`.

**In the self-development source workspace**, the directory carries three subdirectories:

- `inbox/` — operator copies feedback files verbatim from external workspaces here. Preserved byte-identically per read-contract §3 (archive-surface preservation discipline extended to feedback).
- `triage/` — per-feedback triage records written by self-development sessions that triage inbox items. Separate file per feedback record. Triage state does not overwrite intake.
- `INDEX.md` — thin index with one line per feedback record and its current status.

Feedback file frontmatter schema:

```yaml
---
feedback_id: EF-NNN-<slug>
source_workspace_id: <workspace id>
source_session: NNN
created_at: <ISO-8601>
reported_by: operator | application-agent
target: engine | methodology | other
target_files: [<paths>]
severity: blocker | friction | observation
status: outbound | inbox | triaged | resolved | rejected
---
```

Feedback file body sections: `## Observation` (what happened in the external application), `## Why It Matters` (what engine/methodology behaviour was implicated), `## Suggested Change` (optional), `## Evidence` (links or copied snippets), `## Application-Scope Disposition` (why the external application did or did not resolve locally).

Triage file frontmatter schema:

```yaml
---
feedback_ref: engine-feedback/inbox/EF-<id>.md
triage_session: NNN
status: accepted | deferred | rejected
classification: substantive | minor | non-applicable
opened_issue: open-issues/OI-NNN.md  # optional; present when triage lifts feedback to OI
resolved_by: provenance/NNN-title/  # optional; present when resolution is complete
---
```

**Read-contract integration**: `engine-feedback/INDEX.md` is default-read in self-development mode when present (per `read-contract.md` v4 §1 item 9). Individual feedback files in `inbox/` and `triage/` are activation-read by reference when `INDEX.md` shows `status: new` or when an OI cross-references them.

**OI integration**: substantive feedback that warrants OI opening produces a new OI in `open-issues/` following existing conventions; the triage file's `opened_issue:` pointer cross-references the OI. Minor feedback can remain in triage-only.

**Retention**: feedback intake files preserved verbatim. Neither intake nor triage overwrite each other.

**Return semantics**: return of feedback from external workspace to self-development is **operator-mediated** — the operator carries the file by copy-paste or equivalent. The engine does not specify automated cross-workspace transport. External application workspaces are independent of each other and of the self-development workspace at the filesystem level; the operator is the transport.

### Additional directories

New top-level directories may be created by future sessions when the work demands them (e.g., `implementations/`, `examples/`). Any new directory should be documented by updating this specification. `applications/` was defined by Session 009 (D-054) for external artefacts and is no longer a hypothetical example. `engine-feedback/` was defined by Session 036 (D-116) for external-application engine/methodology feedback intake.

## §10.4 First-class minorities preserved Session 036 (Path PD deliberation)

Six minorities were preserved from the Session 036 Path PD deliberation per `multi-agent-deliberation.md` v4 §Preserve dissent. Activation warrants per each minority's evaluation window. See `provenance/036-session-assessment/01-deliberation.md` §6 for full synthesis and raw-perspective citation.

- **§10.4-M1 Skeptic-preserver no-revision-warranted on Q1 (Session 036).** Position: PROMPT.md §Dispatch does not warrant revision; the fallback at pre-v7 line 24 (halt and seek clarification) is correct behaviour, and every-session operator-halt for external-application Session-002+ is a cheap operational cost that does not justify specification surface expansion. Source: `[provenance/036-session-assessment/01B-perspective-skeptic-preserver.md, Q1]`. Activation warrant: if 10 sessions post-engine-v7 adoption the new MODE.md + structural-signature dispatcher has been exercised zero times beyond the Session 036 self-development adoption event (no new workspace initialised, no external application begun), no-revision position is retroactively vindicated; reconsider reverting PROMPT.md §Dispatch to pre-v7 form.

- **§10.4-M2 Skeptic-preserver premature-feedback-pathway on Q2 (Session 036).** Position: feedback pathway is premature; no external application has yet surfaced unaddressed engine/methodology feedback (Sessions 008 + 010 closed cleanly without feedback emerging), so formalising a mechanism in advance of demonstrated need risks specifying-ahead-of-evidence. Source: `[provenance/036-session-assessment/01B-perspective-skeptic-preserver.md, Q2]`. Activation warrant: if no feedback file flows into `engine-feedback/inbox/` for 10 consecutive sessions post-adoption with no external applications in flight during that window, premature-formalisation position is retroactively vindicated.

- **§10.4-M3 Reviser pure Direction 2 structural-signature dispatch (Session 036).** Position: the dispatcher should rely on structural signature alone (`applications/NNN-<slug>/brief.md` presence + `provenance/001-genesis/` absence) without introducing a MODE.md file; re-use existing workspace structure as the source of truth. Rejected in favour of the hybrid (MODE.md authoritative + structural-signature fallback) per Outsider's category-error critique. Source: `[provenance/036-session-assessment/01A-perspective-reviser.md, Q1]`. Activation warrant: if MODE.md adoption proves burdensome, frequently stale, or inconsistently created at Session 001 across 3 or more new workspace initialisations, consider collapsing to pure structural signature.

- **§10.4-M4 Outsider pure Direction 1 MODE.md-authoritative dispatch (Session 036).** Position: MODE.md should be the sole authoritative dispatch source; the structural-signature fallback encodes accidental layout as identity and will fail on future workspaces that carry both self-development material and application material for legitimate reasons. Rejected in favour of the hybrid (fallback retained for legacy workspaces). Source: `[provenance/036-session-assessment/01D-perspective-outsider.md, Q1]`. Activation warrant: if the structural-signature fallback produces ambiguous routing in practice (e.g., a self-development workspace with legitimate `applications/NNN-<slug>/brief.md` content, or a dispatcher fallback case that the operator has to adjudicate more than twice within 6 sessions), consider removing the fallback and requiring MODE.md unconditionally.

- **§10.4-M5 Reviser OI-tag-only feedback pathway (Session 036).** Position: feedback pathway should re-use existing OI machinery via a `scope: engine-feedback` frontmatter tag; no new directory, no new file type, no new tool. Rejected in favour of structured `engine-feedback/` directory per Outsider's upstream-intake framing. Source: `[provenance/036-session-assessment/01A-perspective-reviser.md, Q2]`. Activation warrant: if `engine-feedback/` in the self-development workspace accumulates fewer than 3 distinct feedback records over 10 sessions post-adoption, consider collapsing to OI-tag-only per Reviser's direction.

- **§10.4-M6 Outsider separate-prompt-files-operator-invoked (Session 036).** Position: the dispatcher should be eliminated; the operator invokes `PROMPT-development.md` or `PROMPT-external.md` directly; explicit entrypoints are common in mature tooling and avoid autodispatch ambiguity. Rejected in favour of preserving the single-entry-point abstraction. Source: `[provenance/036-session-assessment/01D-perspective-outsider.md, Q5]`. Activation warrant: if MODE.md + fallback continues to produce dispatcher ambiguity beyond the Session 036 revision over 6 sessions, reconsider explicit operator-invoked separate prompt files.

Note on minority count: these six Session 036 minorities, added to the 21 preserved at Session 035 close (consolidated in `provenance/036-session-assessment/01-deliberation.md` §6), bring engine-wide first-class minorities to **27** at Session 036 close.

## Validation

To validate this specification:

1. Check that all top-level elements listed above exist in the workspace
2. Check that each specification in `specifications/` has the required frontmatter fields and three body sections
3. Check that each provenance directory follows the naming convention `NNN-title/`
4. Check that `SESSION-LOG.md` has an entry for every provenance directory
5. Check that no provenance record dated before the current session has been modified since its session closed (immutability check via git)
6. Check that each directory in `applications/` corresponds to an external artefact produced or regularized in a session whose decision record in provenance authorises its presence
7. Check that every external artefact file in `applications/` carries the `originating_session` frontmatter field; for regularized artefacts, also `regularized_in_session` and `provenance_witness_path`
8. (Added v5) Check that `MODE.md` exists at workspace root with a recognised `mode:` value. Automated as `tools/validate.sh` check 23.
9. (Added v5) When `engine-feedback/` exists, check that any file named `engine-feedback/inbox/EF-*.md` carries the required feedback frontmatter schema per §engine-feedback, and that any file at `engine-feedback/triage/EF-*.md` carries the required triage frontmatter schema.
