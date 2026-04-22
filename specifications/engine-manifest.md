---
title: Engine Manifest
version: 1
status: active
created: 2026-04-22
last-updated: 2026-04-23
updated-by-session: 023
supersedes: none
---

# Engine Manifest

## Purpose

This specification names what constitutes the **Selvedge engine** at any given engine version. The engine is the current loadable implementation of the Selvedge methodology (per `identity.md` v2 layered denotation): a file set that, when loaded together, executes the methodology's nine-activity process against an application's context. The manifest makes the engine pointable-at, versionable, and cleanly separable from the workspace's own development-provenance.

Created Session 017 per D-074 as the resolution of OI-017 (engine-vs-methodology reframing). Its minimal scope is deliberate: the manifest enumerates and declares invariants, but does not restate the content of the specifications it enumerates.

## Specification

### 1. Engine definition

The **Selvedge engine** is the current loadable implementation of the Selvedge methodology, consisting of the file set enumerated in §3 at the engine version named in §2. Loading the engine means having these files available and treating them as a closed unit for the purposes of executing a session.

The engine is distinct from:
- The **methodology** — the abstract-approach, domain-general mechanic that the engine realises (named "Selvedge" per `identity.md` v2).
- The **development-provenance** — the self-development application's own accumulated reasoning trail (`SESSION-LOG.md`, `open-issues.md`, `provenance/`).
- Any **specific application** — a particular run of the engine against a problem (self-development or external-problem).

### 2. Current engine version

**`engine-v4`** (established Session 023 per D-086).

Subsequent engine versions (`engine-v5`, `engine-v6`, ...) increment per the versioning discipline in §5. The current engine version is always named by this §2.

### 3. Engine-definition files at `engine-v4`

The following files constitute the engine at the current version:

| File | Role |
|------|------|
| `PROMPT.md` | Thin dispatcher: names the three layers and two operating modes; points to `prompts/development.md` and `prompts/application.md`. |
| `prompts/development.md` | Executable prompt for the self-development application (this workspace's entry point). |
| `prompts/application.md` | Template prompt for external-problem applications (loads the engine by reference to this manifest; specifies application-context slots). |
| `specifications/methodology-kernel.md` | Kernel: defines the nine-activity execution semantics. |
| `specifications/multi-agent-deliberation.md` | Defines multi-perspective deliberation triggers, non-Claude participation, recording schema. |
| `specifications/validation-approach.md` | Two-tier validation: structural checks and guided-assessment questions. |
| `specifications/workspace-structure.md` | Defines file classes, top-level structure, provenance conventions. |
| `specifications/identity.md` | Records the name Selvedge and the three-layer denotation. |
| `specifications/reference-validation.md` | Defines reference-validation as the third sense of validation. |
| `specifications/read-contract.md` | Defines the access discipline: default-read surface vs archive surface (v1, added engine-v3). |
| `specifications/engine-manifest.md` | **This file.** |
| `tools/validate.sh` | Executable: runs the Tier 1 structural checks from `validation-approach.md`. |

An external-application workspace that clones the engine should copy (or reference) these files and nothing else from the source workspace.

### 4. What is explicitly NOT part of the engine

The following are development-provenance or application-scope; they are **not** loaded when an external application initialises:

- `SESSION-LOG.md` (development-provenance)
- `open-issues.md` (development-provenance)
- `provenance/` (development-provenance: all session records)
- `applications/NNN-*/` (application-scope: prior application outputs, not reusable as engine load)
- `specifications/*-v1.md`, `*-v2.md`, `*-v3.md` (superseded spec versions: preserved in the workspace but not active engine definition)

This manifest's own version history is also not part of the engine load; the current `engine-manifest.md` is what counts.

### 5. Versioning discipline

The engine version (`engine-v1`, `engine-v2`, ...) increments when any file in §3 changes in substance. "In substance" means:

- A new engine-definition file is added to §3.
- An existing engine-definition file receives a substantive revision (v-bump per the spec-revision discipline in `workspace-structure.md`).
- An engine-definition file is removed or superseded.

The engine version does **not** increment on:
- Typo corrections or formatting adjustments.
- Minor elaborations within an existing spec's scope (per the OI-002 substantive-vs-minor heuristic).
- Updates to development-provenance or application-scope files.
- Changes to `SESSION-LOG.md`, `open-issues.md`, or `provenance/`.

Engine-version increments are declared by a decision record in the session that executes the increment. The decision names the file(s) changed and the new engine version.

### 6. Loading the engine / minimal external-application initialisation contract

An external application workspace is initialised by:

1. **Copy the engine-definition file set** (§3) into a fresh directory (or reference them from a canonical engine repository). The copy is flat: maintain the same paths (`PROMPT.md`, `prompts/`, `specifications/`, `tools/`).
2. **Create fresh development-provenance files** in the new workspace:
   - Empty `SESSION-LOG.md` (header only).
   - Empty `open-issues.md` (header only).
   - Empty `provenance/` directory.
3. **Create the first application directory** `applications/001-<slug>/` containing at minimum a `brief.md` carrying:
   - The problem statement.
   - Constraints (domain constraints; time constraints; stakeholder constraints).
   - Stakeholders (who holds the problem; who will receive the artefact; who validates).
   - Success condition (what the artefact must do for the application to be considered successful).
4. **Select the execution prompt.** For an external-problem application, copy `prompts/application.md` to the workspace's `PROMPT.md` (or reference it), then fill in the template slots with the application-specific content from `brief.md`. For a self-development application (like this workspace), use `prompts/development.md`.
5. **Record the engine version loaded.** The first session's provenance (e.g., `provenance/001-*/00-assessment.md`) should name the engine version (`engine-v1` or later) the workspace was initialised from.
6. **Run Session 001** per the loaded execution prompt. The session Reads the application's initial state (the `brief.md` + the engine specifications), Assesses what the application's first increment should be, Convenes perspectives, Deliberates, Decides, Produces the first artefact or design fragment, Validates, Records, and Closes.

The critical rule per Outsider [Session 017 01d Q6]: **external application workspaces inherit the engine, not the engine's autobiography.** The development-provenance of the Selvedge engine's own development is preserved in this source workspace; it does not travel with the engine to an external application.

### 7. Engine version history

- **`engine-v1`** — established Session 017 via D-074. First versioned engine definition. File set per §3. Corresponds to the post-Session-017 state of the workspace: `methodology-kernel.md` v4 + scope-clarification sentence; `multi-agent-deliberation.md` v3 + minor scope-applicability sentence; `validation-approach.md` v3 + minor scope-applicability sentence; `workspace-structure.md` v3; `identity.md` v2; `reference-validation.md` v1; `tools/validate.sh` as of Session 005/006 last substantive change; `PROMPT.md` as thin dispatcher; `prompts/development.md` and `prompts/application.md` as created by D-074. Subsequent intra-engine-v1 changes (Session 019: `reference-validation.md` v1 → v2; Session 020: `workspace-structure.md` v3 minor amendment) did not bump the engine version because v3 minor amendments do not trigger §5 bump per OI-002 heuristic.

- **`engine-v2`** — established Session 021 via D-082. Substantive revisions to three engine-definition files: `multi-agent-deliberation.md` v3 → v4 (added §Criterion-4 Articulation for OI-004; §Acceptable Participant Kinds for OI-004; six new Layer 2 manifest fields; one new synthesis frontmatter field; one new session-level participants.yaml block; four-state OI-004 lifecycle with §Closure Procedure for OI-004); `validation-approach.md` v3 → v4 (added §Tier 2 Q8; documented gating conventions for new checks 16-19); `tools/validate.sh` substantive update (added checks 16, 17, 18, 19; added CRITERION4_ARTICULATION_SESSION constant; added PARTICIPANT_ORGANISATION_CLOSED_SET constant; added Tier 2 Q8 print-out). v3 of the two specs preserved as `multi-agent-deliberation-v3.md` and `validation-approach-v3.md` (both `status: superseded`). All other engine-definition files unchanged at engine-v2 boundary: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `methodology-kernel.md` v4, `workspace-structure.md` v3, `identity.md` v2, `reference-validation.md` v2, `engine-manifest.md` (this file, frontmatter `last-updated: 2026-04-22` + `updated-by-session: 021`).

- **`engine-v3`** — established Session 022 via D-084. First engine-v-bump to add a new engine-definition file: `specifications/read-contract.md` v1 (new; defines default-read surface vs archive surface access discipline). Substantive revisions to multiple engine-definition files: `methodology-kernel.md` v4 → v5 (§1 Read revised to name default-read vs archive distinction); `workspace-structure.md` v3 → v4 (substantive — adds `open-issues/` directory replacing `open-issues.md` file per v3 split-authorisation clause; adds archive-pack subdirectory convention; cross-references to read-contract.md; SESSION-LOG.md text restored to thin-index form); `validation-approach.md` v4 → v5 (added §Tier 2 Q9 for read-contract adherence; documented gating conventions for new checks 20, 21, 22); `tools/validate.sh` substantive update (added checks 20, 21, 22; added READ_CONTRACT_ADOPTION_SESSION, DEFAULT_READ_HARD_WORD_CEILING, DEFAULT_READ_SOFT_WORD_CEILING constants; added Tier 2 Q9 print-out). Substantive revisions to prompts: `prompts/development.md` lines 19, 25, 43 revised for read-contract discipline; `prompts/application.md` analogous Read-section revision for external-application consistency. v4 of the two revised specs preserved as `methodology-kernel-v4.md`, `workspace-structure-v3.md`, `validation-approach-v4.md` (all `status: superseded`). All other engine-definition files unchanged at engine-v3 boundary: `PROMPT.md` (thin dispatcher unchanged), `multi-agent-deliberation.md` v4 (unchanged; cross-referenced from workspace-structure.md v4 and read-contract.md for provenance layout continuity), `identity.md` v2, `reference-validation.md` v2. Session 022 additionally performed retroactive migrations under the new read-contract: R8a SESSION-LOG.md restored to thin one-liner index; R8b `open-issues.md` split into `open-issues/` directory with per-OI files; R8c Session 014 Outsider perspective (96,651 words) archive-packed at `provenance/022-workspace-scaling-trajectory/archive/014-oi016-outsider/`; R8c' Session 022's own Outsider raw (22,611 words) archive-packed at session close. Mempalace R3 `CLAUDE.md` paragraph removed per E.1 (Session 020 §5.4 warrant trigger 1 satisfied; not engine-definition). Engine-v3 is the first engine-v-bump to introduce a new engine-definition spec file (beyond the original eleven at v1).

- **`engine-v4`** — established Session 023 via D-086. Substantive revision to one engine-definition file + substantive update to `tools/validate.sh`: `read-contract.md` v1 → v2 (§2 budget values recalibrated 15,000 → 8,000 hard and 10,000 → 6,000 soft per empirical 3.0× tokens-per-word ratio correcting v1's 1.3× assumption; §2 Rationale rewritten; §2a aggregate default-read surface report added with advisory threshold ≥90,000 and activation threshold ≥100,000; §5.1/§5.2/§5.3/§5.5 minorities added; §10 versioning updated); `tools/validate.sh` constants `DEFAULT_READ_HARD_WORD_CEILING` 15000 → 8000 and `DEFAULT_READ_SOFT_WORD_CEILING` 10000 → 6000; new aggregate reporter constants `DEFAULT_READ_AGGREGATE_ADVISORY=90000` and `DEFAULT_READ_AGGREGATE_ACTIVATION=100000`; check 20 output extended with aggregate report per §2a (informational not pass/fail/warn). v1 of read-contract.md preserved as `read-contract-v1.md` with `status: superseded`. All other engine-definition files unchanged at engine-v4 boundary: `PROMPT.md`; `prompts/development.md`; `prompts/application.md`; `methodology-kernel.md` v5; `multi-agent-deliberation.md` v4; `validation-approach.md` v5; `workspace-structure.md` v4; `identity.md` v2; `reference-validation.md` v2; `engine-manifest.md` (this file, documentary update per Session 021 sub-pattern). Engine-v4 is the second engine-v-bump in adjacent sessions (engine-v3 Session 022; engine-v4 Session 023) and the third in four sessions (engine-v2 Session 021; engine-v3 Session 022; engine-v4 Session 023). **Session 022 §5.4 Skeptic engine-version-cadence minority warrant activates at engine-v4 adoption:** "three engine-v-bumps in four adjacent sessions OR external-application portability confusion." Post-activation escalation trigger per Session 023 D-086 R9: any further engine-v-bump in Sessions 024/025/026 elevates §5.4 to substantive and forces a dedicated engine-manifest §5 revision deliberation in that session. OI-018 tracks this as an open issue for Session 024+. Known consequence of v4 adoption: `specifications/multi-agent-deliberation.md` at 6,403 words exceeds new 6,000-word soft warning and fires on adoption; this is designed soft-warning function per read-contract.md v2 §2; Session 024 responds per §8 remediation options.

Future engine-version increments will extend this history in this section.

## Validation

To validate this specification:

1. Confirm the files enumerated in §3 all exist at the declared paths.
2. Confirm that any file NOT enumerated in §3 but present in the workspace is either (a) in §4's explicit exclusion list, or (b) a superseded spec version, or (c) clearly out-of-scope (e.g., `.git`, `.gitignore`, `.claude`, `.serena`).
3. Confirm that `identity.md` v2 references this manifest as the definition of the engine at the current version.
4. Confirm that `workspace-structure.md` v3 references the same three file-class distinction this manifest implies (engine-definition / development-provenance / application-scope).
5. When a session executes a substantive revision to an engine-definition file, confirm the session's decision record declares a new engine version in this manifest's §2 and §7.
6. When an external application workspace is first initialised, confirm its Session 001 provenance records the engine version loaded per §6.5.
7. Confirm that no engine-version increment has occurred without a decision record authorising it (guard against silent engine-version drift).
