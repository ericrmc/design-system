---
title: Workspace Structure
version: 9
status: active
created: 2026-04-17
last-updated: 2026-04-26
updated-by-session: 074
supersedes: workspace-structure-v8.md
---

# Workspace Structure

## Purpose

This specification defines how the workspace is organized: what directories and files exist, what each contains, and how they relate. It ensures that any agent or person reading the workspace can orient themselves quickly and knows where to find — and where to put — each kind of content.

Version 9 (Session 064 per D-234) extends §10.4 with five new first-class minorities §10.4-M21 through §10.4-M25 (S064 MAD on operator audit findings; minority count 45 → 50). Minor per OI-002 (additions only; no removals; no revisions to existing text); engine-v bump driven by `validation-approach.md` v7 substantive revision per `engine-manifest.md` engine-v12 entry, not by this file. v8 preserved as `workspace-structure-v8.md`.

Version 8 (Session 063 per D-228) extended §10.4 with five new first-class minorities §10.4-M16 through §10.4-M20 (S062 EF-058-tier-2-validation MAD dissent-preservation; minority count 40 → 45). Added `validation-debt/` directory to top-level structure as engine-adjacent lightweight ledger per `validation-approach.md` v6 §(z5) Validation-Debt Lifecycle.

Version 7 (Session 058 per D-202a + D-204) added the records-substrate file-class extension (`structured-source-record` + `markdown-witness` + reaffirms `human-provenance`), added `records/` directory to top-level structure, and extended §10.4 with four new first-class minorities §10.4-M12 through §10.4-M15 (S058 records-substrate MAD dissent-preservation; minority count 36 → 40). v6 preserved as `workspace-structure-v6.md`.

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
/validation-debt/              (added v8; engine-adjacent lightweight (z5) lifecycle ledger per validation-approach.md v6)
  index.md                     (markdown-table lifecycle ledger; rows per (z5) item; checked by validate.sh check 28)
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

Note on minority count: the five S062 minorities §10.4-M16 through §10.4-M20 below add to the 40 preserved at S058 close, bringing engine-wide first-class minorities to **45** at S062 close. Mirrored cross-reference at `specifications/validation-approach.md` v6 §10.

- **§10.4-M16 P2 minimum-viable-response (Session 062).** Position: per `reference-validation.md` v3 §10.3 Skeptic-preserver minimal-revision precedent, the minimum-viable response to EF-058-tier-2-validation activation is (α) mechanical detection + (z1) operator-audit channel formalisation + `validation-approach.md` v6 minor-correction articulating the principled-asymmetry basis (alias-prevention vs noticing-failure). Larger structural mechanism ((β)/(γ)/(δ)/(ε)) is reserved for n≥3 sustained-pattern evidence. Engine-v10 preserved. Source: `[provenance/062-session/01b-perspective-incrementalist-conservator.md, Q1+Q2]`. Activation warrant: synthesis adopted (δ-γ + α + z5-lightweight + z6-deferred-spec) over P2's minimum-viable response; preserve as standing reopen-warrant if the adopted direction's cost-evidence balance proves unfavourable across S063+ observation window. Reopen warrants: (a) sustained-pattern threshold n=3 (third operationally-distinct laundering pattern beyond MCP-transport-honest-limit-chain + EF-058-claude-md-drift); (b) adopted-direction operational insufficiency vs (α)+(z1) (cross-family reviewer mechanism (γ) misses a laundering pattern that operator-audit catches where post-hoc analysis demonstrates (α)+(z1)-only would have been operationally equivalent); (c) operator-audit cadence drift (cadence recorded as performed in fewer than 80% of qualifying sessions across a 10-session window); (d) records-substrate phase-N maturity (records-substrate phase-2 mirrored-minorities + phase-3 feedback adoption + 6-session stabilisation completes — estimated S068+ — and (z5) records-family promotion becomes operationally tractable). Mirrored in `specifications/validation-approach.md` v6 §10.

- **§10.4-M17 P2 principled-asymmetry-articulation (Session 062).** Position: regardless of which direction is adopted, `validation-approach.md` v6 MUST explicitly articulate the principled basis for the MAD §Synthesis vs session-close Tier-2 asymmetry (alias-prevention vs noticing-failure per P2 [`01b`, Q2]). Failure to articulate is itself the deeper laundering surface than the eight-session chain, because un-articulated discipline is preserved by inertia. Source: `[provenance/062-session/01b-perspective-incrementalist-conservator.md, Q2]`. Status at S063 close: **adopted** — `validation-approach.md` v6 §Principled Asymmetry incorporates the articulation requirement directly. Preserved as minority-not-as-alternative-direction but as durable-articulation-discipline carrying forward. Reopen warrant: (a) articulation absence in any future Tier-2-validation-discipline-EF-resolving session (concrete trigger: any future `engine-feedback/inbox/EF-NNN` naming Tier-2-self-validation as the structural concern reopens this minority for explicit articulation in that resolving session). Mirrored in `specifications/validation-approach.md` v6 §10.

- **§10.4-M18 P3 z5 lifecycle-ledger as required (Session 062; P4 endorsed).** Position: EF-058 is fundamentally a validation-debt liveness problem; a mechanism without lifecycle tracking leaves recording-not-engaging structurally unresolved. (z5) validation-debt lifecycle ledger is required as part of first adoption, not later embellishment. Lightweight-vs-records-family scope is implementation question; presence is required. Source: `[provenance/062-session/01c-perspective-outsider-frame-completion.md, Frame critique + Q1]` + `[provenance/062-session/01d-perspective-cross-family-reviewer.md, Q1 + Per-perspective audit > P3]`. Status at S063 close: **adopted** as Layer 4 of the layer composition (lightweight implementation at `validation-debt/index.md` per `validation-approach.md` v6 §(z5) Validation-Debt Lifecycle; records-family promotion deferred). Preserved against future-arc rollback. Reopen warrants: (a) repeated honest-limit recurrence (any repeated honest-limit or equivalent debt persists across three sessions without lifecycle-status update or escalation); (b) lifecycle item dispositioned-without-rationale (any (z5) item deferred past `review_by_session` without escalation or substantive-progress rationale); (c) reviewer-cannot-identify-debt (a reviewer (γ) cannot identify active unresolved validation debt from the review packet — lifecycle table absent, stale, or ambiguous). Mirrored in `specifications/validation-approach.md` v6 §10.

- **§10.4-M19 P3 z6 harness-telemetry-digest (Session 062; P4 endorsed).** Position: harness telemetry should first be implemented as a structured digest (failed tool calls, retries, repeated reads, fallback events, anomalous patterns) before raw transcript review becomes a reviewer obligation. Cheaper, less noisy, more reviewable than full transcript inspection. Source: `[provenance/062-session/01c-perspective-outsider-frame-completion.md, Frame critique + Q5]` + `[provenance/062-session/01d-perspective-cross-family-reviewer.md, Q5 + counter-frames]`. Status at S063 close: **specified, deferred-implementation** via Layer 5 of the layer composition + EF-059 filing per S062 D-225 (`engine-feedback/inbox/EF-059-harness-telemetry-feed-for-tier-2-reviewer.md`). Preserved against future raw-transcript-first adoption. Reopen warrants: (a) failed-tool/repeated-Read operator-surface (failed tool calls or repeated Reads operator-surfaced post hoc as discipline-gap events vindicate "specify the requirement now"); (b) reviewer-cost from raw-transcript noise (if EF-059 implementation arc proposes raw-transcript-first approach and reviewer cost rises measurably from transcript noise); (c) anomalous-pattern absence in workspace artefacts (two sessions contain unavailable-tool or retry clusters not visible in workspace artefacts, only in transcript). Mirrored in `specifications/validation-approach.md` v6 §10.

- **§10.4-M20 P1 δ-γ tiered routing required if narrower path adopted (Session 062).** Position: δ-γ with tiered routing (Layer 1 universal mechanical + Layer 2 triggered cross-family + Layer 6 operator-audit) is the operationally-justified scope; if a narrower direction is adopted (α-only, α+z1, or δ-γ without z5), the structural-prevention surface is incomplete relative to the eight-session honest-limit chain pattern. Source: `[provenance/062-session/01a-perspective-validator-architect.md, Q1+Q2+Q3]` + `[provenance/062-session/01d-perspective-cross-family-reviewer.md, Dissent-preservation 4]`. Status at S063 close: **substantively adopted** as v6 direction; preserved as durable warrant if S064+ implementation narrows scope or rolls back any layer. Reopen warrants: (a) honest-limit text drift recurs in any 3-session window post-S062 close (laundering-pattern operationally re-confirmed); (b) operator-surfaced Q4-laundering instance recurs (status-quo-or-(α)-only adoption is empirically inadequate); (c) cross-family availability becomes structurally reliable (if WX-44/WX-47 codex-CLI discipline gets resolved — direct API path; reliability stabilises across N sessions — universal R2 every-session γ should be reconsidered rather than left at engine-def-only-and-substantive-arc-only routing). Mirrored in `specifications/validation-approach.md` v6 §10.

Note on minority count: the five S064 minorities §10.4-M21 through §10.4-M25 below add to the 45 preserved at S063 close, bringing engine-wide first-class minorities to **50** at S064 close. Mirrored cross-reference at `specifications/validation-approach.md` v7 §10.

- **§10.4-M21 P2 prompt-template-first / defer-spec-revision-to-S067+ (Session 064).** Position: per `reference-validation.md` v3 §10.3 Skeptic-preserver minimal-revision precedent + S062 §10.4-M16 P2 minimum-viable-response precedent: minimum-viable response to S063 first-instance reviewer findings is reviewer-prompt-template extension at S064 (operational-level fix; not engine-definition spec revision) + observation across WX-62-1 window (S064-S066 triggered applications). Substantive spec revision at S064 is precipitate against §10.4-M16 reopen warrant (b) sustained-pattern threshold (n≥3); S067+ resolution preferred when WX-62-1 closes with empirical data. Source: `[provenance/064-session/01b-perspective-conservator.md, Q1+Q4+Q6+Q7+Q8 + Frame critique 1-5 + Dissent-preservation 1-5]`. Status at S064: rejected per cross-family weighted convergence; preserved as standing reopen-warrant. Reopen warrants: (a) sustained-pattern threshold n≥3 misses across S065-S067; (b) compact engine-v12 entry laundering (truncation omits class-classification or first-of-record events); (c) bootstrap recurrence (S065/S066 close audit produces another operator audit finding requiring same-or-similar revision direction); (d) (z10-trigger) differential-trigger-set vindication (high-cost-low-value findings at sessions where simpler differential-trigger routing would have sufficed). **Status update at S074 D-290**: reopen warrant (a) sustained-pattern threshold n≥3 **EMPIRICALLY VINDICATED at n=4** per S063+S067+S071+S073 Gemini findings_count=0 + S073 codex cross-check on identical input produced findings_count=2 (see `engine-feedback/inbox/EF-073-gemini-excluded-and-reviewer-family-rule-relaxation.md`). Operator-directive at S074 (§10.4-M10 clause (c) n=11) excludes google + removes family-distinctness per D-288 v7→v8; template v3 revision deferred to future Path-AS / Path-PD scope per (z7) lock-in-after-n=2. Mirrored in `specifications/validation-approach.md` v8 §10.

- **§10.4-M22 P1 two-session arc preferred (Session 064).** Position: same-session adoption at S064 violates perspective-independence preservation per S062 deliberation §1.7 + S062+S063 reified two-session arc pattern (n=2). Two-session arc shape is engine-conventional for substantive-arc resolutions where perspective-independence is load-bearing. S064 = MAD; S065 = phase-3 implementation + first triggered application of revised audit shape. Reifies pattern at n=2. Source: `[provenance/064-session/01a-perspective-reviewer-mechanism-architect.md, Q7 + Dissent-preservation 2]`. Status at S064: rejected per cross-family weighted convergence (P3+P4 same-session bounded over P1 two-session); preserved as standing reopen-warrant. Reopen warrants: (a) spec-text drift (S065 retrospective check finds v7 spec drifted from S064 deliberation's adopted direction); (b) synthesizer-framing absorption (any load-bearing P3 reframe was paraphrased into Claude-preferred shapes during synthesis or implementation); (c) phase-3 implementation flaw (same-session implementation introduces operational defects detected at S065+ first triggered application of revised audit shape). Mirrored in `specifications/validation-approach.md` v7 §10.

- **§10.4-M23 P3 substrate-led reviewer-judged frame (Session 064; P4 endorsed).** Position: Tier 2.5 is not "get a cross-family reviewer"; it is "force an independent-enough agent to inspect the right substrate surfaces against known failure modes." A different family reading a thin packet can still rubber-stamp; a same-family but temporally separated reviewer with a strong evidence checklist can sometimes catch more. The mechanism's load-bearing structure is **substrate-led, reviewer-judged**: substrate surfaces accumulated debt + watchpoints + inbox + open-issues + recent Path A defaults; reviewer judges flagged-vs-not-flagged states. Reviewer identity is secondary to evidence-surface activation. Source: `[provenance/064-session/01c-perspective-outsider-frame-completion.md, Frame critique + Q1 + Q2 + Q4 + Dissent-preservation 1]` + `[provenance/064-session/01d-perspective-cross-family-reviewer-laundering-audit.md, Per-perspective audit P3 + Synthesis warnings 3 + Dissent-preservation 3]`. Status at S064: **substantively adopted** as v7 audit-shape direction (per §1.2 + §1.4 of synthesis). Preserved against future-arc rollback or narrowing into "use retrieval" framing. Reopen warrants: (a) reviewer-judges-without-substrate-input (a future reviewer audit produces findings without engaging substrate-state-surfaces — lifecycle ledger / watchpoints / inbox / open-issues — substrate-led framing operationally re-confirmed as primary discipline); (b) substrate-tooling gap blocks discipline (substrate state-surface queries insufficient to support audit-shape requirements; substrate-tooling expansion prioritised at next deliberation); (c) reviewer-identity-magic recurrence (synthesis or implementation drifts toward "cross-family reviewer is sufficient" framing without substrate-led discipline). Mirrored in `specifications/validation-approach.md` v7 §10.

- **§10.4-M24 P3 (z11) (z5) authoritative-not-witness + (z12) explicit-Path-justification (Session 064; P4 endorsed).** Position: (z5) validation-debt lifecycle ledger should be authoritative (source-of-truth) not witness (also-read), per S058 records-substrate Substrate-N3.5 framing applied to (z5). Reviewer treats ledger-vs-narrative mismatch as a finding unless close explains why ledger is stale or superseded. Separately, (z12) explicit Path-justification at every session close prevents defaults hiding inside familiar labels. Source: `[provenance/064-session/01c-perspective-outsider-frame-completion.md, Q4 z11 + z12 + Dissent-preservation 2]` + `[provenance/064-session/01d-perspective-cross-family-reviewer-laundering-audit.md, Per-perspective audit P3 + Dissent-preservation]`. Status at S064: **adopted** in v7 (z11 incorporated into §(z5) Validation-Debt Lifecycle authoritative semantics with `authoritative: true` frontmatter declaration; z12 incorporated into prompts/development.md). Preserved against future relaxation. Reopen warrants: (a) ledger-as-witness drift (close-narrative claims about debt diverge from ledger state without explicit reconciliation); (b) records-family promotion blocked by ledger maturity (lightweight markdown-table ledger's authoritative semantics produce edit-conflicts or staleness across multi-session use; records-family promotion per S062 §10.4-M18 reopen warrants becomes preferred); (c) Path-justification omitted (a future close omits Path justification despite (z12) requirement; prompt-discipline must be tightened — e.g., validator check enforcing presence). Mirrored in `specifications/validation-approach.md` v7 §10.

- **§10.4-M25 P2 cadence-depth + P1 audit-cost-budget co-preservation (Session 064).** Position (cadence-depth, P2): engine-v11 → engine-v12 at adjacent sessions (S063 + S064) with engine-v11 preservation depth 0 is **first-of-record depth-0 preservation event** in workspace history, approaching §5.4 cadence-runaway signal threshold. Future engine-v13 at S065 (if engine-manifest restructure or other substantive revision) would create 2-bump-in-3-sessions pattern requiring §5.4 reopen. Position (audit-cost-budget, P1): revised audit shape with full scope significantly increases reviewer cost; quality-laundering by budget-pressure (reviewer truncates scope under cost constraint without disclosure) is a structural risk requiring (z10-cost) audit-cost-budget discipline at session-close. Source: `[provenance/064-session/01b-perspective-conservator.md, Frame critique 2 + Q5 + Q8 + Dissent-preservation 2]` + `[provenance/064-session/01a-perspective-reviewer-mechanism-architect.md, Q4 (z10-P1) + Dissent-preservation 3]`. Status at S064: **preserved as forward-observation discipline**. Cadence-depth: §5.4 reopen warrant tracking active. Audit-cost-budget: not spec-encoded but recorded in v7 §Tier 2.5 implementation note as forward-observation. Reopen warrants: (a) engine-v13 at S065 creates first-of-record 3-bump-in-3-sessions pattern; §5.4 fully activates (status update at S071: engine-v13 ratified at S071 close per S071 D-265, NOT at S065; engine-v12 preserved depth-6 across S065-S070 = engine-conventional cadence; reopen warrant (a) does NOT fire at engine-v13-at-S071); (b) reviewer-cost growth >2× over S063 baseline (~25 wall-clock minutes / ~45,000 tokens) per audit; audit-cost-budget discipline operationally required (status update at S071: per S071 D-264 the §10.4-M25 P1 audit-cost-budget threshold arithmetic on self-reported values is suspended pending harness-measurement availability per (γ) phase-3 (z6) digest arc); (c) quality-laundering by budget-pressure (reviewer audit at S065+ shows scope-truncation without explicit `skip_rationale:`); P1's audit-cost-budget framing vindicated as required spec-encoded discipline. Mirrored in `specifications/validation-approach.md` v7 §10.

Note on minority count: the four S071 minorities §10.4-M26 through §10.4-M29 below add to the 50 preserved at S064 close, bringing engine-wide first-class minorities to **54** at S071 close. Mirrored cross-reference at `specifications/validation-approach.md` v7 §10.

- **§10.4-M26 P1 full-(γ)-immediate position (Session 071).** Position: per `[provenance/071-session/01a-perspective-harness-discipline-architect.md, Q1+Q2+Q8+Cross-product candidate position+Dissent-preservation]`: full (γ) digest implementation as the structural-correctness response per cross-session-state-claim discipline framing (design-space §4.2); multi-session phase-3 arc per S062 D-220 precedent; engine-v13 at S072+ phase-3 close. Hybrid (ε) defers γ commitment; the empirical evidence chain at design-space §3.1 (n=5 substrate non-use) + §3.2 (n=3 reviewer self-report propagation) is operationally sufficient for γ commitment now per cross-session-state-claim verifiability requirement. Status at S071: rejected per cross-family weighted convergence (P2 Claude + P3+P4 codex on (ε) hybrid over P1 full (γ)); preserved as standing reopen-warrant. Reopen warrants: (a) sustained substrate non-use post-β (after β lands at S071 close, if substrate non-use recurs at orchestrator self-report across ≥3 consecutive sessions despite spec-side requirement promotion, full (γ) is reopened); (b) reviewer-cost-trajectory laundering recurrence (after β lands with Direction C, if a future operator audit surfaces a reviewer-cost-trajectory inaccuracy, Direction B subsumption is reopened); (c) operational tractability shift (if Claude Code hook surface stabilises or harness-telemetry capture mechanism becomes trivial, full (γ) is reopened on cost-side rather than evidence-side). Mirrored in `specifications/validation-approach.md` v7 §10.

- **§10.4-M27 P2 (γ)-deferral-criteria position (Session 071; partly absorbed).** Position: per `[provenance/071-session/01b-perspective-incrementalist-conservator.md, Q2+Q4+Q8+Cross-product candidate position+Dissent-preservation]`: (γ) scope is precipitate per S062 §10.4-M16 P2 reopen warrant criteria. The (z6)-specific surfaces (failed-tool-call + repeated-Read at concrete sessions) lack n≥3 evidence at present; n≥3 evidence-floor on (z6)-specific surfaces should gate phase-3 (γ) activation; records-substrate phase-2/3 stabilisation is natural pacing constraint per EF-059 §Why It Matters point 4. Status at S071: **partly absorbed** by (ε) hybrid synthesis at S071 D-263 (the same-session-bounded β-phase preference is honored; the (γ)-deferral-with-named-gating is honored). The minority preserves the **threshold for activating phase-3 (γ) at S072+**, not the phase-1 (β) adoption-direction question (which (ε) accommodates). Reopen warrants: (a) (γ) phase-3 implementation introduces operational complexity that displaces operator-audit-as-laundering-detection without equivalent verification (operator-audit cadence drops below 80% across 10-session window per §10.4-M16 reopen warrant (c) pattern); (b) (γ) capture mechanism (CM1/CM2) portability friction blocks external-application engine load; (c) (z6) digest produces n≥3 sessions of measured behavior that diverges from spec-side expectation in ways that β would have caught — vindicating γ adoption-direction; (d) records-substrate phase-2 mirrored-minorities + phase-3 feedback-records-family adoption stalled because (γ) phase-3 implementation absorbed substantive-arc capacity (cadence-runaway via scope-expansion-stacking per §5.4 cadence-depth concern preservation per §10.4-M25 P2). Mirrored in `specifications/validation-approach.md` v7 §10.

- **§10.4-M28 P3 measurement-authority-separation-as-load-bearing position (Session 071; substantively adopted; P4 endorsed).** Position: per `[provenance/071-session/01c-perspective-outsider-frame-completion.md, Q4+Q5+Frame critique+Dissent-preservation]` + `[provenance/071-session/01d-perspective-cross-family-reviewer-laundering-audit.md, Q4+Q5]` cross-family endorsement: digest records MUST distinguish `producer_kind: harness-measured | post-hoc-reconstructed | agent-declared` + `authority_level` semantic distinction. Same field name carries different evidentiary weight per producer_kind. Without that distinction, future sessions can launder CM4 (in-session emission) into γ via YAML shape alone (P3 explicit at `[01c, Q5]`: "That prevents a future session from laundering CM4 into γ merely because the YAML shape exists"). Status at S071: **substantively adopted** at synthesis §5.1 of `provenance/071-session/01-deliberation.md`. Phase-3 (γ) digest schema specification at S072+ MUST incorporate per VD-003 lifecycle row gating. Preserved against future-arc rollback or narrowing into "schema-only-without-producer-kind" framing. Reopen warrants: (a) phase-3 (γ) digest spec adopted without producer_kind/authority_level fields; reframe operationally re-confirmed as primary discipline; (b) CM4 in-session emission entries treated as harness-measured-equivalent in any session's audit; (c) future MAD on related arc surfaces measurement-authority concern independently. Mirrored in `specifications/validation-approach.md` v7 §10. Cross-family-originated-and-adopted-at-MAD-execution reframe-architecture pattern reified at n=4 (S058 Substrate-N3.5 + S062 z5+z6 + S064 substrate-led + z11 + z12 + S071 measurement-authority separation).

- **§10.4-M29 P4 bundling-by-laundering audit position (Session 071; substantively adopted).** Position: per `[provenance/071-session/01d-perspective-cross-family-reviewer-laundering-audit.md, Frame critique+Cross-product candidate position+Dissent-preservation]`: separate dispositions per direction prevents bundling-by-laundering; (γ) bundle risks combined cost looking inevitable because each part points at "harness measurement" but each part has independent merit and independent cost. The synthesis should preserve separate disposition for each: first-phase substrate habit correction (β-phase), immediate reviewer-cost caveat (Direction C now), and separately scoped digest implementation (γ phase-3 arc). Status at S071: **substantively adopted** at synthesis §5.2 of `provenance/071-session/01-deliberation.md`. The (ε) hybrid composition reflects this framing. Preserved against future-arc bundling pressure. Reopen warrants: (a) phase-3 (γ) implementation adopts bundled-direction shape that obscures per-direction cost; (b) future MAD bundles related arcs without explicit per-direction cost analysis; (c) operator-audit at phase-3 close surfaces bundling-by-laundering finding. Mirrored in `specifications/validation-approach.md` v7 §10.

Note on minority count: the six S073 minorities §10.4-M30 through §10.4-M35 below add to the 54 preserved at S071/S072 close, bringing engine-wide first-class minorities to **60** at S073 close. Mirrored cross-reference at `specifications/validation-approach.md` v7 §10.

- **§10.4-M30 P1 (γ-1)/(γ-2) maximalist position dissent (Session 073).** Position: maximal-scope γ phase-3 (CMD-4+SCD-3+RAD-1+REVD-3+CHKD-1+EVD-1) per §10.4-M28+M29 structural-honest response; partial-shift accrues durable agent-declared records. Source: `[provenance/073-session/01a-perspective-capture-mechanism-maximalist-architect.md, Cross-product candidate+Dissent-preservation]`. Rejected per cross-family weighted convergence on (γ-6); preserved as reopen-warrant. Reopen warrants: (a) substrate non-use post-γ; (b) reviewer-cost-trajectory laundering recurrence; (c) operational tractability shift; (d) γ phase-3 reviewer surfaces partial-schema laundering. Lineage §10.4-M26 evolved. Mirrored in `validation-approach.md` v7 §10.

- **§10.4-M31 P2 (γ-3) minimum-viable position dissent (Session 073).** Position: smallest-scope γ phase-3 (CMD-3+SCD-2+RAD-2+REVD-2+CHKD-3+EVD-2-smaller) discharging VD-003; pacing-claim under n=2 observation. Source: `[provenance/073-session/01b-perspective-minimum-viable-conservator.md, Cross-product candidate+Dissent-preservation]`. Rejected per cross-family weighted convergence; preserved. Reopen warrants: (a) (γ-6) implementation cost at S074-S075 exceeds (γ-3) baseline by >50%; (b) records-substrate phase-2 stalled per §10.4-M27 (d); (c) aggregate-budget at S076 exceeds 92K. Mirrored in `validation-approach.md` v7 §10.

- **§10.4-M32 P3 z8 portable-capture-adapter-contract reframe (Session 073; substantively adopted).** Position: capture-adapter contract over CM1/CM2/CM3 producer implementations is portable engine design surface; CM1 first adapter; CM2 portable end-state; evidence contract should survive migration to codex/gemini CLI, OpenAI Agents SDK, custom MCP agents. Source: `[provenance/073-session/01c-perspective-outsider-frame-completion.md, Frame critique+Q1]`. Adopted per S073 D-275 (γ-6) + D-276 capture stack. Preserved against future-arc Claude-only-capture rollback. Reopen warrants: (a) engine under non-Claude harness; CM1 hook-only fails; (b) digest production fails outside Claude Code; (c) reviewer treats CM1 as generally authoritative; (d) external-application CM1-portability friction. **Cross-family-originated-and-adopted-at-MAD reframe pattern reified at n=5** (S058+S062+S064+S071+S073). Mirrored in `validation-approach.md` v7 §10.

- **§10.4-M33 P3 z9 validator-as-evidence-consumer reframe (Session 073; substantively adopted).** Position: validate.sh validates declared evidence + digest shape; does NOT require live MCP substrate access; may run outside Claude Code's MCP context (CI, terminal, different harness). Source: `[provenance/073-session/01c-perspective-outsider-frame-completion.md, Frame critique+Q5]`. Adopted per S073 D-280 CHKD-2 evidence-consuming. Preserved against future-arc live-substrate-required-validation. Reopen warrants: (a) future MAD adopts CHKD-1 substrate-required without evidence-consumer discipline; (b) check 26 substrate-aware at S074 introduces live-MCP-runtime-dependency breaking CI; (c) evidence-declaration shape gaps in implementation. Mirrored in `validation-approach.md` v7 §10.

- **§10.4-M34 P4 z-laundering-1 measurement-authority-not-inherited-from-YAML-container reframe (Session 073; substantively adopted).** Position: authority attaches per record/section, not file-level; harness-emitted file containing agent-declared workaround text does not inherit primary status; agent-declared cannot promote to harness-measured via digest shape alone. Source: `[provenance/073-session/01d-perspective-cross-family-reviewer-laundering-audit.md, Frame critique+Q2]`. Adopted per S073 D-277 SCD-3 field-level authority + REVD-2 quarantine extension at validation-approach.md v7 §Tier 2.5. Preserved against future-arc file-level-only-authority rollback. Reopen warrants: (a) future MAD adopts file-level-authority without per-section discipline; (b) digest at S074-S077+ contains mixed-origin fields without per-field annotations; (c) reviewer treats CM1 file wholesale primary. Mirrored in `validation-approach.md` v7 §10.

- **§10.4-M35 P3 z10 + P4 z-laundering-2 staging-must-be-per-direction reframe (Session 073; P3+P4 dual-originated; substantively adopted).** Position: staged rollout requires per-direction disposition for CM/SCD/RAD/REVD/CHKD/EVD/Q7/Q8/Q9/Q10; "staged" without per-direction launders delay into prudence or maximal-scope into inevitability. Reopen-warrant-activation ≠ implementation-bundling. Source: `[provenance/073-session/01c-perspective-outsider-frame-completion.md, Frame critique+Q8]` + `[provenance/073-session/01d-perspective-cross-family-reviewer-laundering-audit.md, Frame critique+Cross-product candidate]`. Adopted per S073 D-275 (γ-6) per-direction disposition + D-282 reopen-warrant-activation-not-bundling. Preserved against future-arc bundling/staged-collapse. Reopen warrants: (a) γ phase-3 stage at S074-S076 collapses per-direction into one ratification; (b) future MAD bundles arcs without per-direction cost analysis; (c) operator-audit at γ close finds bundling-by-laundering; (d) reopen-warrant activation drifts into implementation-bundling at S074+. Mirrored in `validation-approach.md` v7 §10.

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
