---
title: Workspace Structure
version: 2
status: superseded
created: 2026-04-17
last-updated: 2026-04-19
updated-by-session: 009
supersedes: workspace-structure-v1.md
superseded-by: workspace-structure.md
---

# Workspace Structure

## Purpose

This specification defines how the workspace is organized: what directories and files exist, what each contains, and how they relate. It ensures that any agent or person reading the workspace can orient themselves quickly and knows where to find — and where to put — each kind of content.

## Specification

The workspace has the following top-level structure:

```
/PROMPT.md
/SESSION-LOG.md
/open-issues.md
/specifications/
/provenance/
/tools/
/applications/
```

### PROMPT.md

The bootstrap prompt that drives the methodology. This file precedes the methodology — it is not produced by the process, it initiates the process. It may be revised, but any revision should be treated as a significant event and recorded in provenance.

### SESSION-LOG.md

A running index of sessions for quick orientation. Each entry is one line containing the session number, date, title, and a brief note on what was accomplished. This file is updated at the close of each session.

### open-issues.md

A list of known questions, gaps, uncertainties, and unresolved disagreements. Each entry has a brief description, the session that identified it, and its current status. Issues are removed when resolved (with a reference to the session that resolved them). This is a single file, not a directory, unless the number of issues makes a single file unwieldy.

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
