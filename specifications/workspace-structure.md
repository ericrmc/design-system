---
title: Workspace Structure
version: 4
status: active
created: 2026-04-17
last-updated: 2026-04-23
updated-by-session: 030
supersedes: workspace-structure-v3.md
---

# Workspace Structure

## Purpose

This specification defines how the workspace is organized: what directories and files exist, what each contains, and how they relate. It ensures that any agent or person reading the workspace can orient themselves quickly and knows where to find — and where to put — each kind of content.

Version 4 (Session 022, D-084) adds the `open-issues/` directory split (replacing the single `open-issues.md` file per the v3 §open-issues split-authorisation clause), adds cross-references to `specifications/read-contract.md` (new v1 specification governing default-read vs archive surface distinction), and adds the archive-surface subdirectory convention (`provenance/NNN-title/archive/`). v3 preserved as `workspace-structure-v3.md`.

Version 3 (Session 017, D-074) adds the three file-class distinction (engine-definition / development-provenance / application-scope) and documents `prompts/` as a new directory created by the PROMPT.md split. v2 preserved as `workspace-structure-v2.md`.

## Specification

### File classes (added v3)

Under the three-layer denotation established in `identity.md` v2 (Selvedge methodology / Selvedge engine / application), workspace files fall into one of three classes:

- **Engine-definition files** — the loadable Selvedge engine. An external application workspace may (and should) clone this set without inheriting development-provenance. Enumerated canonically by `specifications/engine-manifest.md`. At `engine-v1`: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `specifications/*.md` (all active files in the `specifications/` directory), `tools/validate.sh`.
- **Development-provenance files** — the self-development application's own accumulated history. Not part of the engine load; not inherited by external-application workspaces by default. Includes `SESSION-LOG.md`, `open-issues.md`, and `provenance/`.
- **Application-scope files** — per-application content (inputs, outputs, application-specific briefs and notes). Mutable per the `applications/` directory rules below. Organised as `applications/NNN-<slug>/`.

The normative rule: an external application workspace may load the engine-definition set as a read-only unit (or a cloned starting point) without inheriting development-provenance. The self-development application (this workspace) carries all three classes by construction (the engine is being developed here; the provenance is the development record; the applications are the by-products).

### Top-level structure

The workspace has the following top-level structure:

```
/PROMPT.md
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
```

### PROMPT.md

The bootstrap prompt. Under v3 (D-074, Session 017) `PROMPT.md` is a thin **dispatcher**: it names the three layers (methodology / engine / application), names the two operating modes (self-development and external-problem), and points to the two mode-specific executable prompts in `prompts/`. It is part of the engine-definition file class. It may be revised, but any revision is a significant event and recorded in provenance (as it was when the v3 split occurred in Session 017). The self-development application's executable content was moved to `prompts/development.md`; the template for external-problem applications lives at `prompts/application.md`.

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

### Additional directories

New top-level directories may be created by future sessions when the work demands them (e.g., `implementations/`, `examples/`). Any new directory should be documented by updating this specification. `applications/` was defined by Session 009 (D-054) for external artefacts and is no longer a hypothetical example.

## Validation

To validate this specification:

1. Check that all top-level elements listed above exist in the workspace
2. Check that each specification in `specifications/` has the required frontmatter fields and three body sections
3. Check that each provenance directory follows the naming convention `NNN-title/`
4. Check that `SESSION-LOG.md` has an entry for every provenance directory
5. Check that no provenance record dated before the current session has been modified since its session closed (immutability check via git)
6. Check that each directory in `applications/` corresponds to an external artefact produced or regularized in a session whose decision record in provenance authorises its presence
7. Check that every external artefact file in `applications/` carries the `originating_session` frontmatter field; for regularized artefacts, also `regularized_in_session` and `provenance_witness_path`
