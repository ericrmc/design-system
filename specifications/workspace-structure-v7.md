---
title: Workspace Structure
version: 7
status: superseded
created: 2026-04-17
last-updated: 2026-04-25
updated-by-session: 058
supersedes: workspace-structure-v6.md
superseded-by: workspace-structure.md (v8)
superseded-in-session: 063
---

# Workspace Structure

## Purpose

This specification defines how the workspace is organized: what directories and files exist, what each contains, and how they relate. It ensures that any agent or person reading the workspace can orient themselves quickly and knows where to find — and where to put — each kind of content.

Version 7 (Session 058 per D-202a + D-204) adds the records-substrate file-class extension (`structured-source-record` + `markdown-witness` + reaffirms `human-provenance`), adds `records/` directory to top-level structure, and extends §10.4 with four new first-class minorities §10.4-M12 through §10.4-M15 (S058 records-substrate MAD dissent-preservation; minority count 36 → 40). v6 preserved as `workspace-structure-v6.md`.

Version 6 (Session 050 per D-172) added §10.4-M7 through §10.4-M11 five new first-class minorities preserved from S050 retrieval-substrate MAD. Minority count 27 → 36. v5 preserved as `workspace-structure-v5.md`.

Version 5 (Session 036, D-113 + D-116) adds the `MODE.md` workspace-identity-file convention, the `engine-feedback/` directory with mode-dependent outbox/inbox semantics, and the §10.4 first-class-minority block preserving six Session 036 Path PD minorities. v4 preserved as `workspace-structure-v4.md`.

Version 4 (Session 022, D-084) adds the `open-issues/` directory split (replacing the single `open-issues.md` file per the v3 §open-issues split-authorisation clause), adds cross-references to `specifications/read-contract.md` (new v1 specification governing default-read vs archive surface distinction), and adds the archive-surface subdirectory convention (`provenance/NNN-title/archive/`). v3 preserved as `workspace-structure-v3.md`.

Version 3 (Session 017, D-074) adds the three file-class distinction (engine-definition / development-provenance / application-scope) and documents `prompts/` as a new directory created by the PROMPT.md split. v2 preserved as `workspace-structure-v2.md`.

## Specification

### File classes (added v3, extended v5, extended v7)

Under the three-layer denotation established in `identity.md` v2 (Selvedge methodology / Selvedge engine / application), workspace files fall into one of seven classes (v7 adds three records-substrate classes).

- **Engine-definition files** — the loadable Selvedge engine. An external application workspace may (and should) clone this set without inheriting development-provenance. Enumerated canonically by `specifications/engine-manifest.md`. At `engine-v1`: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `specifications/*.md` (all active files in the `specifications/` directory), `tools/validate.sh`.
- **Workspace-identity files** (added v5) — per-workspace identity declarations created at initialisation time. Distinct from engine-definition because each workspace has its own content (not copied byte-identically from the engine). Includes `MODE.md` at workspace root (required from Session 001 of any new workspace per `PROMPT.md` §Session-001 obligation). See §MODE.md below.
- **Development-provenance files** — the self-development application's own accumulated history. Not part of the engine load; not inherited by external-application workspaces by default. Includes `open-issues/`, and `provenance/`. (Pre-v7 also included `SESSION-LOG.md`; at v7 this is migrated to records-substrate per §records-substrate; SESSION-LOG.md is archive-pack at `provenance/058-session/archive/pre-records-SESSION-LOG/`.)
- **Application-scope files** — per-application content (inputs, outputs, application-specific briefs and notes). Mutable per the `applications/` directory rules below. Organised as `applications/NNN-<slug>/`.
- **Non-engine operator-managed content** — content that is neither engine-definition nor development-provenance nor application-scope but serves operator coordination. Includes `engine-feedback/` (added v5; see §engine-feedback below).
- **Structured source records** (added v7) — authoritative per-fact-family records under `records/<family>/<id>.md`. Frontmatter is source-of-truth; body is optional witness/expansion. Schema and discipline per `specifications/records-contract.md` v1. Phase-1 family: `records/sessions/`. See §records-substrate below.
- **Markdown witnesses** (added v7) — projection or generated-or-validator-checked witness files derived from structured source records. Per-family `records/<family>/index.md` is default-read surface entry per `read-contract.md` v6 §1; per-record markdown bodies (if any expansion content exists) are session-scope read-as-needed. Witnesses are NOT authoritative; if witness and record disagree, the record wins per `records-contract.md` v1 §3 + check 25.

The normative rule: an external application workspace may load the engine-definition set as a read-only unit (or a cloned starting point) without inheriting development-provenance. The self-development application (this workspace) carries all classes by construction (the engine is being developed here; the provenance is the development record; the applications are the by-products; the workspace-identity marker names what this workspace is; the records-substrate is the source-of-truth layer for migrated fact families).

### Top-level structure

The workspace has the following top-level structure:

```
/PROMPT.md
/MODE.md                       (workspace-identity; added v5)
/prompts/
  development.md
  application.md
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
/records/                      (added v7; structured-source-record substrate per records-contract.md v1)
  sessions/                    (phase-1; per-session records replacing pre-v7 SESSION-LOG.md)
    index.md                   (default-read; thin pointer-only)
    S<NNN>.md                  (one record per session; structured frontmatter authoritative)
  minorities/                  (phase-2 candidate; per-minority canonical records)
  engine-versions/             (phase-3 candidate)
  feedback/                    (phase-3 candidate)
/engine-feedback/              (optional; added v5; mode-dependent semantics)
  INDEX.md                     (default-read in self-development mode when present)
  inbox/                       (self-development workspace: operator-deposited feedback from external workspaces)
  triage/                      (self-development workspace: per-feedback triage records)
  EF-<id>.md                   (external workspace: outbox feedback files)
```

Pre-v7 also included `/SESSION-LOG.md` at workspace root; at v7 this file is migrated to `records/sessions/` per D-203 + records-contract.md v1; pre-migration SESSION-LOG.md preserved verbatim as archive-pack at `provenance/058-session/archive/pre-records-SESSION-LOG/`.

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

### records-substrate (added v7)

Per `specifications/records-contract.md` v1 (engine-v10 adoption), structured records under `records/<family>/<id>.md` are authoritative for selected fact families. At engine-v10 phase-1, the only family is `records/sessions/` (per-session records replacing the pre-v7 `SESSION-LOG.md`).

Per-family `index.md` is the default-read surface entry (per `specifications/read-contract.md` v6 §1). It is a thin pointer-only file with one row per record. Authority discipline: source record (frontmatter) > index row; on disagreement, the record wins and `tools/validate.sh` check 25 emits FAIL.

Per-record files (`records/<family>/<id>.md`) are NOT default-read surface; they are read at session-scope-as-needed (similar pattern to `applications/` per `read-contract.md` v5 §2d carve-out).

### SESSION-LOG.md (pre-v7; migrated)

Pre-v7, `SESSION-LOG.md` at workspace root was a thin one-line-per-session index for quick orientation, default-read surface entry. At v7 (engine-v10 adoption Session 058 per D-203), this file is **migrated to `records/sessions/`**: each row becomes one structured record `records/sessions/S<NNN>.md`; `records/sessions/index.md` replaces SESSION-LOG.md as the default-read entry per `read-contract.md` v6 §1 item 5.

Pre-migration `SESSION-LOG.md` content is preserved verbatim as archive-pack witness at `provenance/058-session/archive/pre-records-SESSION-LOG/` per `read-contract.md` v6 §4-§7 archive-pack discipline + S022 R8a / S040 D-123 / S051 D-178 archive-pack precedent chain.

Pre-migration archive-pack chain at workspace history:
- `provenance/022-workspace-scaling-trajectory/archive/pre-R8a-SESSION-LOG/` (pre-Session-022 variable-length-summary form per S022 R8a thin-index restoration).
- `provenance/040-session-log-preemptive-restructure/archive/pre-L-SESSION-LOG/` (pre-Session-040 verbose multi-cell rows per S040 D-123 thin-index restoration).
- `provenance/051-session/archive/pre-L-SESSION-LOG/` (pre-Session-051 hard-ceiling-breach forced-restructure per S051 D-178).
- `provenance/058-session/archive/pre-records-SESSION-LOG/` (pre-engine-v10 SESSION-LOG.md migrated to records/sessions/ per S058 D-203).

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

**Folder-name discipline** (added v4, Session 027 per D-094, minor amendment; default-literal amended v5 Session 045 per D-138, minor amendment): at session open, the provenance folder is created as `NNN-session` (where NNN is the zero-padded session number). The folder name is **permanent**: it is not revised at session close and is not revised by subsequent sessions. Discoverability of session content is carried by `SESSION-LOG.md` (thin-index), which holds each session's descriptive title; the folder name is the container address, not the thin-index. Sessions 017-022 that received content-reflective folder names (`017-oi017-reframing-deliberation` through `022-workspace-scaling-trajectory`) are historical artefacts of an informal pre-Session-027 convention and are not retroactively altered (D-017 immutability). Sessions 015 and 023-045 retained the Session 027 D-094 opening default `NNN-session-assessment` and are likewise preserved as-is; Session 040 received a content-reflective name (`040-session-log-preemptive-restructure`) and is preserved. Session 045 D-138 activated S027 §B Minimalist minority (3-of-4 cross-family convergence including both non-Claude) to change the forward-only opening default from `NNN-session-assessment` to `NNN-session`, dropping the `-assessment` suffix that increasingly mislabelled broader-than-assessment sessions (S041 OI-004 closure, S043 Path PSD, S044 Path OC, S045 Path OS). This clause introduces no new close-step obligation and no new validator check. Minority positions preserved at Session 027 per D-094 (see `provenance/027-session-assessment/02-decisions.md`): close-step rename-when-substantive (Discoverer §A); advisory-only placement in `prompts/development.md` (Archivist §C). The Minimalist §B default-change minority was activated at Session 045 per D-138. New minority preserved at Session 045 per D-140: §5.14 Folder-Name Reviewer preserve-D-094 position (1-of-4 Claude-only dissent; three operational reopen warrants; see `provenance/045-session-assessment/02-decisions.md` §D-140).

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

Note on minority count: these six Session 036 minorities, added to the 21 preserved at Session 035 close (consolidated in `provenance/036-session-assessment/01-deliberation.md` §6), bring engine-wide first-class minorities to **27** at Session 036 close. Sessions 037–049 added minorities inline bringing the count to 31 at Session 049 close. Session 050's retrieval-substrate MAD adds five more minorities (§10.4-M7 through §10.4-M11 below), bringing engine-wide first-class minorities to **36** at Session 050 close.

- **§10.4-M7 P2 minimum-adoption / defer-with-instrumentation (Session 050).** Position: adoption should earn expansion through measured use, not anticipated architecture. If phase-1 proves unused, phase-1 should not have shipped. Source: `[provenance/050-session/01b-perspective-incrementalist-skeptic.md, §1.3]`. Activation warrant: if the WX-50-1 gate (retrieval-contract.md §6) fails to fire across S050–S053 AND zero use recorded for phase-1 tools in ≥3 consecutive sessions, revisit whether phase-1 should have shipped at all. Reopen warrants: (a) WX-50-1 non-firing + zero-use across 3+ consecutive sessions; (b) phase-1 tool maintenance becomes operationally burdensome relative to evidence of value. Mirrored in `specifications/retrieval-contract.md` v1 §7.1.

- **§10.4-M8 DuckDB structured-first substrate (Session 050).** Position: if structured filters and graph traversal prove dominant, SQLite FTS5 may be the wrong long-term substrate despite winning phase-1. Source: `[provenance/050-session/01a-perspective-substrate-architect.md, §1.2 + §2 counter-frames]` + `[provenance/050-session/01d-perspective-cross-family-reviewer.md, §7 dissent-rec 2]`. Activation warrant: any session in which phase-1 tool use shows structured-filter + graph-traversal queries dominate prose-search queries by ≥3× count over a 5-session window. Reopen warrants: (a) query-class data demonstrates structured-first dominance; (b) SQLite FTS5 ecosystem churn that DuckDB-FTS does not share. Mirrored in `specifications/retrieval-contract.md` v1 §7.2.

- **§10.4-M9 P1 engine-definition-at-adoption (Session 050).** Position: the retrieval-substrate capability is important enough that it warrants engine-definition classification now, not deferred; the current contract adopted engine-adjacent per D-170 but this minority preserves the opposite position for evidence-triggered reconsideration. Source: `[provenance/050-session/01a-perspective-substrate-architect.md, §4.1]` + `[provenance/050-session/01d-perspective-cross-family-reviewer.md, §7 dissent-rec 3]`. Activation warrant: if an external-workspace adoption exposes inconsistent inheritance (workspace A and workspace B have divergent substrate implementations producing different answers on equivalent queries), re-enter the engine-definition case. Reopen warrants: (a) inconsistent-inheritance signal; (b) ≥3 stable substrate versions + ≥1 successful external-workspace adoption + operator surfacing promotion. Mirrored in `specifications/retrieval-contract.md` v1 §7.3.

- **§10.4-M10 Substrate-N2 structured-artefacts-as-source-of-truth reframe (Session 050).** Position: the shared markdown-plus-index frame should not be mistaken for the only scalable answer; decisions, OIs, minorities, watchpoints, etc. may eventually become structured records with markdown as witness. Source: `[provenance/050-session/01c-perspective-outsider-frame-completion.md, §2 Substrate-N2]`. Activation warrant: if substrate phase-2+ maintenance cost exceeds projections by ≥2× OR multi-hop cross-reference queries become the dominant operational burden, revisit Substrate-N2 as a multi-session arc. Reopen warrants: (a) cumulative phase-2+ maintenance time exceeds projection 2× across 3 consecutive sessions; (b) multi-hop cross-reference query class dominates ≥5× prose-search over a 5-session window. Mirrored in `specifications/retrieval-contract.md` v1 §7.4.

- **§10.4-M11 `syncs_with:` declaration-of-intent distinction (Session 050).** Position: extracted edges may not replace explicit co-evolution commitments; edges answer "what is cited"; `syncs_with:` would answer "what must co-evolve"; the distinction is load-bearing; phase-2 deliberation on edges MUST explicitly deliberate whether to preserve or fold `syncs_with:`. Source: `[provenance/050-session/01c-perspective-outsider-frame-completion.md, Q6]` + `[provenance/050-session/01d-perspective-cross-family-reviewer.md, §7 dissent-rec 5]`. Activation warrant: at phase-2 deliberation on the `edges` table, the fold-vs-preserve question on `syncs_with:` is explicitly on the agenda; auto-fold is not permitted. Reopen warrants: (a) cross-spec drift that an `edges` table did not catch; (b) declared co-evolution relationships that are not citation-observable. Mirrored in `specifications/retrieval-contract.md` v1 §7.5.

**§10.4-M10 written warrants update (Session 058 per D-204 Part A)**: §10.4-M10 activation warrants are extended with new clause (c) operator-surfacing channel formalisation. Existing warrants (a) maintenance-cost-2× and (b) multi-hop-dominance-5× preserved. New warrant (c): operator-surfacing of §10.4-M-N-activation per S036/S043/S044/S045/S047 Path PD/OS minority-activation pathway — operationally exercised at S057 D-194-D-196 (the dedicated MAD scheduling) + S058 D-198-D-205 (the substantive deliberation). **First-of-record minority-warrant-amendment via operator-surfacing-channel-formalisation event** in workspace history.

Note on minority count: the four S058 minorities §10.4-M12 through §10.4-M15 below add to the 36 preserved at S057 close, bringing engine-wide first-class minorities to **40** at S058 close. Mirrored cross-reference at `specifications/records-contract.md` v1 §7.1 through §7.4.

- **§10.4-M12 P2 warrant-gated deferral / Direction C with B fallback (Session 058).** Position: "Direction C (defer until §10.4-M10 written warrants empirically fire), with Direction B held as a contingent fallback if SESSION-LOG.md ceiling pressure forces a tactical local action before either warrant fires." Source: `[provenance/058-session/01b-perspective-incrementalist-conservator.md, Q1]`. Activation warrant: if no §10.4-M10 telemetry exists by S060, OR phase-1 cost exceeds projected maintenance savings across S058+S059, the Conservator's deferral position is vindicated and the substantive arc may be rolled back via archive-pack restoration. Reopen warrants: (a) check 25 noisy or expensive (high false-positive rate); (b) record-witness drift detected within two sessions; (c) phase-1 default-read load reduction <7K words. Mirrored in `specifications/records-contract.md` v1 §7.1.

- **§10.4-M13 P3+P4 shallow-Direction-A warning / records-must-be-source-of-truth (Session 058).** Position: "Per-record Markdown plus thin indexes ... is not necessarily Substrate-N2." Source: `[provenance/058-session/01c-perspective-outsider-frame-completion.md, Frame Critique + Q1]` + `[provenance/058-session/01d-perspective-cross-family-reviewer.md, Counter-Frames]`. Activation warrant: if migrated `records/sessions/*.md` lack structured authoritative frontmatter, OR Markdown witnesses become manually authoritative, OR phase-2+ migration produces sharded-Markdown without strict source-of-truth discipline, this minority's substantive direction (true Substrate-N2 with structured records authoritative) becomes preferred revision direction. Reopen warrants: (a) phase-1 SESSION-LOG.md migration retains Markdown-as-source-of-truth in practice (operators edit body content rather than frontmatter); (b) phase-2 mirrored-minority migration creates duplicate source files; (c) bootstrap contract does not propagate record-schema discipline to external workspaces. Mirrored in `specifications/records-contract.md` v1 §7.2.

- **§10.4-M14 P1 broader-phase-1 / SESSION-LOG.md + workspace-structure.md §10.4 in single phase (Session 058).** Position: "Phase-1 (S058 MAD adoption + first migration): SESSION-LOG.md migration to `provenance/sessions/S<NNN>.md` per-session files, plus workspace-structure.md §10.4 migration to `specifications/minorities/M-NNN.md` per-record files." Source: `[provenance/058-session/01a-perspective-substrate-methodology-architect.md, Q1+Q2]`. Activation warrant: if SESSION-LOG.md phase-1 pilot earns trust at S059 (check 25 clean; no drift; ≥95% resolution) AND default-read aggregate reduction is less than projected because §10.4 minority block continues accreting, the broader-phase-1 position is preferred for accelerated phase-2 (mirror minorities migrated at S059 in single-session rather than 2-session staging). Reopen warrants: (a) phase-1 soak shows pattern is robust enough to migrate two blocks per phase rather than one; (b) §10.4 minority block crosses 1,500 words (currently ~1,800 with M12-M15 added). Mirrored in `specifications/records-contract.md` v1 §7.3.

- **§10.4-M15 P2 spec-local distributed minority directories (Session 058).** Position: "specifications/<spec-name>/minorities/M-NNN.md (distributed-across-spec-source-directories) over a centralised specifications/minorities/ directory. Rationale: minorities are spec-local artefacts that derive context from their parent spec." Source: `[provenance/058-session/01b-perspective-incrementalist-conservator.md, Q3]`. Activation warrant: if any cross-spec mirrored minority's status or text diverges across specs after migration to canonical `records/minorities/M-NNN.md`, the spec-local distribution position is vindicated as preferred direction. Reopen warrants: (a) `applies_to:` or equivalent metadata fails to scale; (b) external-workspaces inherit dependencies without context; (c) substrate cannot reliably distinguish mirrored-fact references from spec-local references. Mirrored in `specifications/records-contract.md` v1 §7.4.

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
