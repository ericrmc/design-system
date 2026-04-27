---
title: Workspace Structure
version: 1
status: superseded
created: 2026-04-17
last-updated: 2026-04-17
updated-by-session: 002
supersedes: none
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

### Additional directories

New top-level directories may be created by future sessions when the work demands them (e.g., `implementations/`, `examples/`). Any new directory should be documented by updating this specification.

## Validation

To validate this specification:

1. Check that all top-level elements listed above exist in the workspace
2. Check that each specification in `specifications/` has the required frontmatter fields and three body sections
3. Check that each provenance directory follows the naming convention `NNN-title/`
4. Check that `SESSION-LOG.md` has an entry for every provenance directory
5. Check that no provenance record dated before the current session has been modified since its session closed (immutability check via git)
