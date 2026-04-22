Reading prompt from stdin...
OpenAI Codex v0.121.0 (research preview)
--------
workdir: /Users/ericmccowan/Development/complex-systems-engine
model: gpt-5.4
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019db6a2-ba9d-7b01-881a-75975c9c2700
--------
user
You are participating as the Outsider perspective in a multi-perspective deliberation for the Selvedge methodology, Session 023. You are invoked via codex exec as a non-Anthropic model; your training lineage is independent of Claude's. This is the shared brief. All four perspectives receive §1 through §6, their own §7 stance, and §8 through §10. You are §7.D (Outsider). Do not read the other perspectives' §7 stances.

Your raw output will be committed verbatim to provenance/023-session-assessment/01d-perspective-outsider.md. Produce your raw output addressing Q1 through Q6 per §8 response format, with Honest Limits + Meta-note at end per §8. You may consult workspace files via your sandbox read-only access; if you do, declare which files in Honest Limits.

---

# Shared Brief — Session 023

## 1. Methodology context

You are participating in a deliberation for the Selvedge methodology's self-development application, Session 023. The methodology has been running for 22 closed sessions; this is the 12th multi-perspective deliberation to convene with non-Claude participation. The engine version loaded is `engine-v3` (adopted Session 022 per D-084).

The Selvedge engine is the current loadable implementation of the Selvedge methodology. Eight active specifications define the engine; the ones directly relevant to this deliberation are:
- `specifications/read-contract.md` v1 — defines the default-read surface and archive surface access discipline (the spec under revision in this session).
- `specifications/engine-manifest.md` — defines engine versioning and enumerates engine-definition files.
- `specifications/validation-approach.md` v5 — defines Tier 1 structural checks including check 20 which enforces the default-read budget.
- `tools/validate.sh` — holds the budget constants as variables.

Your job: reason independently from this brief toward a position on Q1–Q6 below, producing a raw output that the synthesis step will read alongside three other perspectives' outputs. Your output will be committed verbatim to the workspace. Preserve honesty about uncertainty; refuse the premise if you must; distinguish your substantive positions from the brief's framing.

## 2. Problem statement

Session 022 adopted `read-contract.md` v1 per D-084. §2 set a hard ceiling of **15,000 words** for default-read files and a soft warning at **10,000 words**. The §2 Rationale cited: *"The current single-Read-tool ceiling at the time of adoption is approximately 25,000 tokens (≈ 19,250 words at a 1.3× words-to-tokens approximation). A 15,000-word hard ceiling leaves headroom below the single-read ceiling."*

Session 022's own Honest Notes, written at close, flagged that the Rationale's 1.3× ratio was empirically wrong for workspace files:

> My brief §2.2 and operator §3 cite token counts (SESSION-LOG 33,227 tokens; open-issues 27,437 tokens). The new check 20 measures words not tokens. Word counts for the same files: SESSION-LOG 10,405 words; open-issues 9,783 words. Ratio ~3.0× tokens-per-word for these prose-with-markdown files, not the 1.3× my synthesis §2.3 D2 calculation assumed. The 15,000-word hard ceiling therefore translates to ~45,000 tokens in Read-tool terms (far above the 25,000-token single-Read ceiling), not the ~19,500 tokens I stated. This is the Outsider's §5.3 minority concern materialised — the 15K-word budget is more permissive than my synthesis assumed.

The Session 022 Outsider §5.3 minority position (preserved in `read-contract.md` §2 and in the Session 022 synthesis) argued:

> 8,000-word per-file budget is the conservative-preferable value; 15,000 may be permissive. Activation warrant: if any default-read file exceeds 10,000 words (soft warning) within 5 sessions of adoption without subsequent restructure, the 8,000-word ceiling becomes the preferred revision direction.

The Session 022 Outsider also proposed [archive: provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04, Q6]:

> My recommendation is 8,000 words per default-read file. I would also add an aggregate report, and likely a warning threshold, for the total development-provenance default-read surface. Per-file control alone is not sufficient if the default-read set keeps growing by accretion.

The operator ratified Path (C) from Session 022's close at Session 023 open: "Tighten read-contract §2 budget to 8,000 words per Outsider §5.3 minority." This deliberation determines the specific values, engine-version implications, and side-effects of that direction. Operator direction is ratification of path, not binding on values.

## 3. Current state facts

Validator run at Session 023 open: **574 pass, 0 fail, 0 warn**. Default-read surface currently measures 33 files. The five largest default-read files:

| File | Words | Fraction of 8K budget | Fraction of 15K budget |
|------|-------|-----------------------|------------------------|
| `specifications/multi-agent-deliberation.md` | 4,800 (est) | 60% | 32% |
| `specifications/validation-approach.md` | 4,647 | 58% | 31% |
| `provenance/021-oi004-criterion4-articulation/03-close.md` | 4,499 | 56% | 30% |
| `provenance/013-artefact-revision/03-close.md` | 4,454 | 56% | 30% |
| `provenance/022-workspace-scaling-trajectory/03-close.md` | 3,796 | 47% | 25% |

No file exceeds 5,000 words. The Outsider §5.3 activation warrant (any file exceeds 10K soft within 5 sessions) has not fired one session in.

Word-to-token empirical ratio for workspace prose: ~3.0× tokens-per-word (Session 022 Honest Notes).

Single-Read-tool ceiling at Session 023: ~25,000 tokens (unchanged since Session 022).

Derived budgets at 3.0× ratio:
- 8,000 words ≈ 24,000 tokens — within single-Read ceiling.
- 10,000 words ≈ 30,000 tokens — above single-Read ceiling (paginated Read required).
- 15,000 words ≈ 45,000 tokens — ~1.8× single-Read ceiling.

Engine-version history (engine-manifest.md §7):
- `engine-v1` established Session 017 (D-074).
- `engine-v2` established Session 021 (D-082 — OI-004 criterion-4 articulation; multi-agent-deliberation v3→v4; validation-approach v3→v4; validate.sh +checks 16-19).
- `engine-v3` established Session 022 (D-084 — new read-contract.md; methodology-kernel v4→v5; workspace-structure v3→v4; validation-approach v4→v5; validate.sh +checks 20-22).

If Session 023 adopts a substantive revision to `read-contract.md`, this would be `engine-v4` — **three engine-v-bumps in four sessions**.

Session 022 §5.4 Skeptic engine-version-cadence minority (preserved in `provenance/022-workspace-scaling-trajectory/01-deliberation.md` §5 per D-084):

> Activation warrant: three engine-v-bumps in four adjacent sessions OR external-application portability confusion.

## 4. Current spec text (verbatim excerpts)

`specifications/read-contract.md` §2 in full:

> ### 2. Default-read budget
>
> Per-file constraints:
>
> - **Hard ceiling: 15,000 words.** Any file in the §1 enumeration exceeding 15,000 words of body content (frontmatter excluded) is a validation failure at `tools/validate.sh` check 20. The session that produces such a file must either reduce it or restructure it (e.g., split into multiple files each under the ceiling; relocate detail to archive surface with reference from the default-read file).
> - **Soft warning: 10,000 words.** Any file in the §1 enumeration between 10,000 and 15,000 words triggers a validator warning (not a failure). The warning is signal that the file is approaching the ceiling; the next session should consider restructuring.
>
> Measurement: word count via `wc -w` on body content after the closing YAML frontmatter delimiter. The word-count metric is chosen for stability across tokenisers (per Session 022 Outsider [01d-Q6] + Conservator [01b-Q6] convergence).
>
> **Rationale for the chosen values.** The current single-Read-tool ceiling at the time of adoption is approximately 25,000 tokens (≈ 19,250 words at a 1.3× words-to-tokens approximation). A 15,000-word hard ceiling leaves headroom below the single-read ceiling. The 10,000-word soft warning provides early signal before files approach the hard ceiling.
>
> **Outsider minority position** (§5.3 of `provenance/022-workspace-scaling-trajectory/01-deliberation.md`): 8,000-word per-file budget is the conservative-preferable value; 15,000 may be permissive. Activation warrant: if any default-read file exceeds 10,000 words (soft warning) within 5 sessions of adoption without subsequent restructure, the 8,000-word ceiling becomes the preferred revision direction.

`tools/validate.sh` constants:

```
DEFAULT_READ_HARD_WORD_CEILING=15000
DEFAULT_READ_SOFT_WORD_CEILING=10000
READ_CONTRACT_ADOPTION_SESSION=22
```

`specifications/engine-manifest.md` §5 (versioning discipline):

> The engine version (`engine-v1`, `engine-v2`, ...) increments when any file in §3 changes in substance. "In substance" means:
>
> - A new engine-definition file is added to §3.
> - An existing engine-definition file receives a substantive revision (v-bump per the spec-revision discipline in `workspace-structure.md`).
> - An engine-definition file is removed or superseded.
>
> The engine version does not increment on:
> - Typo corrections or formatting adjustments.
> - Minor elaborations within an existing spec's scope (per the OI-002 substantive-vs-minor heuristic).
> - Updates to development-provenance or application-scope files.

`specifications/read-contract.md` §10 Versioning:

> **Substantive:** any change to the §1 enumeration, §2 budget values, §4 archive-pack structure, §5 manifest fields, §6 reference convention, or §7 integrity mechanism. Engine-version bump per `engine-manifest.md` §5.

The §10 text pre-declares that a §2 budget-value change is substantive. This determines v-bump classification mechanically; the deliberation may still challenge whether the classification is correct.

## 5. Survey

Three traditions bear on this problem without importing their conclusions:

1. **Working-set theory (computer architecture, Denning 1968).** A "working set" is the set of pages a process actively uses over a given time window. Working-set theorists distinguish per-page cost (how expensive it is to keep any one page in memory) from aggregate cost (the total cost of the working set). The Outsider §5.3(b) proposal maps to the aggregate side of this distinction.

2. **Document-design constraints in published style guides (e.g., NASA SP-7084, ISO/IEC technical writing standards).** These treat document-length ceilings as a reading-contract between author and reader. Ceilings are not absolute but are calibrated against the reader's expected single-read effort. A ceiling set 1.8× above the single-read effort is, by this discipline, not a ceiling but a soft suggestion.

3. **Budget-as-commitment discipline (procurement / government finance).** Budget values that are set substantially above actual consumption rate become ceremonial rather than binding; when consumption approaches the ceiling, the ceiling is typically revised upward rather than triggering restructure. This is the Outsider §5.3 concern materialised as an analogy: a 15K ceiling when largest file is 4,800 (32%) is well-clear of binding; a 8K ceiling when largest file is 4,800 (60%) binds meaningfully.

Do not import any conclusion from these traditions without flagging it explicitly per the anti-silent-import rule in §10.

## 6. Design questions

You are asked to reason about the following six questions. Your raw output should address each explicitly, in order. Distinguish cases where you take a strong position from cases where you note uncertainty.

### Q1. Hard ceiling value

What should the per-file hard ceiling be? Engage the empirical calibration data in §3 and the single-Read ceiling anchor. Options surveyed (you may propose others):
- 8,000 words (Outsider §5.3 position).
- 10,000 words (compromise; matches current soft warning).
- 12,000 words (modest tightening from 15K).
- 15,000 words (retain current; correct §2 Rationale text only).
- Other.

### Q2. Soft warning value

If the hard ceiling is changed, what should the soft warning be? Options surveyed (you may propose others):
- 6,000 words (75% of 8K hard).
- 5,000 words (63% of 8K hard; more headroom for early signal).
- Remove soft warning entirely (one clean value).
- Tie to a percentage formula rather than a fixed value.
- Other.

### Q3. Aggregate default-read surface budget

The Outsider §5.3(b) proposal at Session 022 was not adopted: "I would also add an aggregate report, and likely a warning threshold, for the total development-provenance default-read surface." Current aggregate is ~81,500 words across 33 default-read files. Session 022 did not adopt; Session 023 may revisit. Options:
- Adopt aggregate budget this session (name value and threshold).
- Do not adopt; add as watchpoint only.
- Reject; argue per-file budget is sufficient.
- Other.

### Q4. Engine-version classification

Read-contract §10 pre-declares §2 budget-value changes as substantive. Per engine-manifest §5, substantive revision to an engine-definition file triggers an engine-version bump. If Q1 adopts a value other than 15K, is this `engine-v4`, or is there a narrow interpretation that avoids the bump (e.g., "constant-tuning within an existing spec's scope" as a minor per OI-002)? Argue on the spec-revision discipline merits; do not argue on cadence-concern grounds (that is Q5's territory).

### Q5. Engine-version cadence (§5.4 minority response)

If Q4 adopts engine-v4, this is three engine-v-bumps in four sessions (engine-v2 Session 021; engine-v3 Session 022; engine-v4 Session 023). The Session 022 §5.4 Skeptic cadence minority activation warrant fires: "three engine-v-bumps in four adjacent sessions OR external-application portability confusion." How should the deliberation respond to the activated warrant?
- Treat as informational signal; proceed with engine-v4 on merits.
- Elevate to substantive concern; re-examine Q1/Q4 under cadence pressure.
- Revise engine-version-bump criteria in engine-manifest §5 to narrow the bump conditions.
- Other.

The §5.4 minority text should be engaged directly per the first-class-minority-preservation discipline.

### Q6. Watchpoints and minorities

What minorities should this deliberation preserve as first-class? What watchpoints should Session 024+ monitor? Name activation triggers concretely.

## 7. Role-specific stance — OUTSIDER (non-Claude; non-Anthropic model family)

You are the Outsider, a non-Anthropic model participating via `codex exec`. Your training lineage is independent of Claude's. Your presence is voluntary for this session per multi-agent-deliberation.md v4 §When Non-Claude Participation Is Required clause 2 (this deliberation substantively revises read-contract.md, which is not in D-023's enumerated list, so non-Claude participation is recommended but not required; your inclusion is voluntary per Sessions 007/008/010/012/013/020/022 precedent).

At Session 022, an Outsider (same model family) produced the §5.3 minority position (8K word per-file budget + aggregate budget proposal) preserved in read-contract.md §2 and in the Session 022 synthesis. Your current stance is not bound to that prior position; reason fresh from this brief's §2 / §3 / §4 / §5 / §6 content.

Engage in Q1: produce your own considered answer. The prior Outsider's 8K position is preserved verbatim in §2 of the brief; you may adopt, refine, or argue against it. Engage in Q2–Q6 per your independent reading. If you find the Pacer 10K or Skeptic defer positions more defensible, adopt them. If you find a position none of the Claude stances anticipates, propose it. Your value to the deliberation is the possibility that your training-distribution-difference produces a contribution Claude perspectives cannot generate (this possibility is open every session; whether it materialises depends on your reading here, not on your prior).

You may consult workspace files if your tooling supports read access; if you do, preserve the Session 021/022 honest-limit pattern of declaring which files you read and what you relied on. You may not import conclusions from outside the workspace without flagging them per §10.

Engage in all six questions. Produce a Meta-note at the end on what you believe your strongest divergence from likely Claude-majority positions is, if any.

## 8. Response format

- Address Q1 through Q6 in order, each with its own `## Q1.` / `## Q2.` etc. heading.
- Target length: 1,500–3,500 words total. Shorter is acceptable if your position is direct; longer is acceptable if you need to preserve reasoning. Do not pad.
- Cite spec text by spec name and section (e.g., `read-contract.md §2`) and session provenance by path + question number where applicable (e.g., `[Session 022 01c-Q9]`). Use the `[archive: path]` convention for archive-surface citations.
- Close with a `## Honest Limits` section naming: what you did not read; what you are uncertain about; where your position rests on assumptions rather than evidence.
- For the Outsider (§7.D only): close with `## Meta-note` in addition to Honest Limits, naming what you expect your strongest cross-model divergence to be.

## 9. Constraint on external imports

Per `PROMPT.md` rule: do not import ideas from outside the process. Reason primarily from this brief's content and the spec text it cites. If a pretrained pattern or analogy arrives (from working-set theory, document-design practice, budget discipline, or anywhere else), flag it as an external input, attribute it, and frame it as hypothesis rather than commit. The §5 survey is the designated on-ramp for pretrained content; use it.

## 10. Closure

Your output will be committed verbatim. Dissent is preserved; minority positions become first-class record; your honest position is more valuable than consensus.

When ready, produce your raw output.

codex
I’m treating this as a written deliberation artifact, not a code-edit task. I’ll verify the cited spec text and versioning clauses in the workspace, then draft a direct Q1–Q6 position with explicit uncertainties and no dependence on the other perspectives’ current §7 stances.
exec
/bin/zsh -lc "sed -n '1,220p' specifications/read-contract.md" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "sed -n '1,220p' specifications/engine-manifest.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
---
title: Engine Manifest
version: 1
status: active
created: 2026-04-22
last-updated: 2026-04-22
updated-by-session: 022
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

**`engine-v3`** (established Session 022 per D-084).

Subsequent engine versions (`engine-v4`, `engine-v5`, ...) increment per the versioning discipline in §5. The current engine version is always named by this §2.

### 3. Engine-definition files at `engine-v3`

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

 succeeded in 0ms:
---
title: Read Contract
version: 1
status: active
created: 2026-04-22
last-updated: 2026-04-22
updated-by-session: 022
supersedes: none
---

# Read Contract

## Purpose

This specification defines the **access discipline** governing what the methodology reads in full at every session open versus what it preserves verbatim and accesses by explicit reference. It repairs a divergence observed at Session 022 between the methodology's normative read obligation (`methodology-kernel.md` §1 Read: "every file, every specification, every provenance record") and the operational read mechanism (paginated `Read --offset`, targeted `Grep`, harness-layer routing around oversized files).

The access discipline is a dimension separate from — and cutting across — the existing file-class ontology in `workspace-structure.md` (engine-definition / development-provenance / application-scope). A file may be engine-definition AND default-read (an active specification); development-provenance AND archive surface (a historical raw perspective).

Created Session 022 per D-084 as the resolution of the workspace-scaling trajectory. The read-contract articulates an engine-v3 repair of what Session 022 diagnosed as an OI-015 laundering pattern materialised at the harness layer.

This specification applies equally to the self-development application and to external-problem applications of the Selvedge engine. Its default-read and archive enumerations are engine-definition content; external-application workspaces inherit them at engine-v3.

## Specification

### 1. Default-read surface

The default-read surface is the bounded set of files read in full at every session open. Every session's Read activity must read every file enumerated below in full before any substantive work proceeds.

**The default-read surface enumeration at engine-v3:**

1. Every active-status `.md` file in `specifications/`. "Active-status" means frontmatter `status: active`. Superseded-status files (`*-v1.md`, `*-v2.md`, etc., carrying `status: superseded`) are archive surface by exclusion (§3).
2. `PROMPT.md` (top-level dispatcher).
3. `prompts/development.md` (self-development executable prompt).
4. `prompts/application.md` (external-application executable prompt).
5. `SESSION-LOG.md` (thin one-line-per-session index; full per-session detail lives in `03-close.md`).
6. `open-issues/index.md` (thin overview; full per-OI detail lives in `open-issues/OI-NNN.md` files).
7. Every `provenance/NNN-title/03-close.md` across all closed sessions.
8. Every file in the currently-active session's provenance directory (`provenance/NNN-title/` where NNN is the current session). While the session is open, current-session provenance is default-read; on close, it becomes archive surface by exclusion (§3) unless it is a `03-close.md` (which stays default-read by §7 above).

The enumeration is closed. A file not enumerated here is archive surface by §3.

### 2. Default-read budget

Per-file constraints:

- **Hard ceiling: 15,000 words.** Any file in the §1 enumeration exceeding 15,000 words of body content (frontmatter excluded) is a validation failure at `tools/validate.sh` check 20. The session that produces such a file must either reduce it or restructure it (e.g., split into multiple files each under the ceiling; relocate detail to archive surface with reference from the default-read file).
- **Soft warning: 10,000 words.** Any file in the §1 enumeration between 10,000 and 15,000 words triggers a validator warning (not a failure). The warning is signal that the file is approaching the ceiling; the next session should consider restructuring.

Measurement: word count via `wc -w` on body content after the closing YAML frontmatter delimiter. The word-count metric is chosen for stability across tokenisers (per Session 022 Outsider [01d-Q6] + Conservator [01b-Q6] convergence).

**Rationale for the chosen values.** The current single-Read-tool ceiling at the time of adoption is approximately 25,000 tokens (≈ 19,250 words at a 1.3× words-to-tokens approximation). A 15,000-word hard ceiling leaves headroom below the single-read ceiling. The 10,000-word soft warning provides early signal before files approach the hard ceiling.

**Outsider minority position** (§5.3 of `provenance/022-workspace-scaling-trajectory/01-deliberation.md`): 8,000-word per-file budget is the conservative-preferable value; 15,000 may be permissive. Activation warrant: if any default-read file exceeds 10,000 words (soft warning) within 5 sessions of adoption without subsequent restructure, the 8,000-word ceiling becomes the preferred revision direction.

### 3. Archive surface

By exclusion: anything preserved in the workspace but not on the §1 enumeration. This includes:

- Raw perspective files (`provenance/NNN-title/01X-perspective-<role>.md`) from closed sessions.
- Superseded specification versions (`specifications/*-v1.md`, `*-v2.md`, etc., carrying `status: superseded`).
- Deliberation synthesis files (`provenance/NNN-title/01-deliberation.md`) from closed sessions.
- Decision files (`provenance/NNN-title/02-decisions.md`) from closed sessions.
- Assessment files (`provenance/NNN-title/00-assessment.md`) from closed sessions.
- Manifests (`provenance/NNN-title/manifests/`) from closed sessions.
- Participant indexes (`provenance/NNN-title/participants.yaml`) from closed sessions.
- Any per-OI historical annotation files that predate the Session 022 `open-issues/` directory split.

Archive surface records are **preserved verbatim.** Summarisation, silent compression, content-aware truncation, or edit-in-place are forbidden. The preservation-vs-summarisation distinction is the load-bearing property that prevents this specification from becoming an on-ramp for information loss.

Archive surface records are **accessed by explicit reference.** A session reading an archive record must cite it per §6 below; silent non-reads of relevant archive records are a validation concern (check 22 and Tier 2 Q9 in `validation-approach.md` v5).

### 4. Archive-pack structure

When an archive-surface record exceeds the default-read per-file budget (§2 hard ceiling), or when the archive record is produced within a current session that will otherwise push the current-session provenance directory over budget at close, the record must be structured as an **archive-pack**: a directory with a manifest plus numbered chunks, preserving byte-identical content via line-range splits only.

Archive-pack layout:

```
provenance/NNN-title/archive/<slug>/
  manifest.yaml        # frontmatter + chunk table + integrity fields
  00-source.md         # byte-identical single file if under per-chunk budget
  OR
  01-chunk.md          # numbered chunks with line-range boundaries only
  02-chunk.md
  ...
```

Chunk size target: each chunk ≤ 10,000 words (matching the §2 soft warning) so that reading any individual chunk never exceeds comfortable read budget.

Boundary rule: **mechanical only** — either line-range or byte-range boundaries. Content-aware boundaries (e.g., "end at a paragraph break," "split at a heading") are forbidden because they introduce chunking judgment that can silently edit content over time. Line-range and byte-range boundaries are both mechanical and auditable; the manifest declares which rule was used via `chunk_boundary_rule: line-range | byte-range | single-file`. Line-range is preferred where the file's line-length distribution is bounded; byte-range is the fallback when the file contains very long lines that would otherwise produce oversized chunks (the Session 014 Outsider file exemplifies this: a 96,651-word file with individual lines of up to 3,328 words; line-range chunking produced chunks over 36,000 words that would themselves breach the default-read budget, so byte-range splitting into 50,000-byte chunks was used).

### 5. Archive-pack manifest fields

The `manifest.yaml` file in every archive-pack carries the following required fields:

```yaml
---
archive_id: <stable identifier, typically <originating-NNN>-<slug>>
originating_session: <session number>
originating_path: <workspace-relative path of the source file>
migrated_in_session: <session number that created the archive-pack>
kind: raw-perspective | over-budget-annotation | superseded-spec | other-named
total_bytes: <integer; bytes of concatenated chunks in canonical order>
total_words: <integer; words of concatenated chunks>
chunk_count: <integer>
chunk_boundary_rule: line-range | single-file
source_hash_sha256: <SHA-256 hash of full concatenation of chunks in ordinal order>
chunks:
  - ordinal: 1
    file: 01-chunk.md
    line_range: "1-500"
    chunk_hash_sha256: <SHA-256 hash of this chunk's contents>
  - ordinal: 2
    file: 02-chunk.md
    line_range: "501-1000"
    chunk_hash_sha256: <SHA-256 hash>
  ...
readers_note: <1-3 sentences; what the archive preserves; when to consult it>
---
```

The manifest is pointer-only. Narrative content beyond the `readers_note` field is forbidden — `readers_note` is at most three sentences. The manifest exists to resolve references, not to summarise the archived content.

### 6. Reference conventions

Default-read surface files cite archive-surface records using a stable reference string:

```
[archive: provenance/NNN-title/archive/<slug>/]
```

With optional chunk-level precision:

```
[archive: provenance/NNN-title/archive/<slug>/#chunk-02]
```

Readers resolving the reference read `manifest.yaml` first, consult the `readers_note`, and then read specific chunks as the current work requires. A citing session that relies on archive content for a load-bearing claim must either read the cited chunk(s) in full, or declare in its honest-limits section that the claim rests on prior-session vetting of the archive content rather than fresh re-reading.

The reference convention is load-bearing for validator check 22 (archive-pack citation consistency): every `[archive: path]` reference in a default-read file must resolve to an existing archive-pack path.

### 7. Integrity guarantee

The `source_hash_sha256` field in each archive-pack manifest is computed against the canonical concatenation of chunks in numerical order. `tools/validate.sh` check 21 verifies this hash on every run; any mismatch is a hard-fail.

Per D-017 immutability (`workspace-structure.md` §provenance), once the migrating session closes, archive-pack files are immutable. Any revision to an archive-pack's content requires a new migrating session with its own decision record; the revision creates a new archive-pack and a supersession reference, not an edit of the prior pack.

Archive-packs created by retroactive migration (migrating a closed session's file into archive form) use the **copy-plus-reference** discipline per Session 009 D-054 precedent: the original file at its original path is **not modified**; the archive-pack is created alongside, typically in the migrating session's own provenance directory (`provenance/<migrating-NNN>/archive/<slug>/`). The original remains at its original path as the byte-identical witness; the archive-pack provides structured access.

Archive-packs created for the current session's own raws (per §9 close-time obligation) move the original content into the archive-pack structure directly (the original path becomes the archive-pack path; no duplication). Because the session is still open at the time of packing, moving is not an edit of a closed-session file.

### 8. Default-read surface budget at session close

At every session close, the orchestrator verifies that every file in the §1 enumeration satisfies the §2 per-file budget. `tools/validate.sh` check 20 enforces this; a hard-fail at session close blocks the session from closing cleanly.

Remediation when a default-read file exceeds the budget: reduce the file in place; or split the file into multiple default-read files (each under budget) with the original split-file designated archive-surface (its content preserved as an archive-pack); or relocate detail to archive-pack form with references from a thinner default-read replacement.

Remediation must not summarise or silently compress; the archive-pack discipline preserves content verbatim.

### 9. Close-time obligation for current-session raws

At every session close, the orchestrator measures each raw perspective file and each provenance file in the current session directory. Any file exceeding the default-read per-file hard ceiling (§2: 15,000 words) is archive-packed before session close.

Mechanism for current-session raw-to-archive-pack migration:

1. Create `provenance/NNN-title/archive/<slug>/` where `<slug>` is a short descriptive identifier (typically matching the perspective role and question theme).
2. Split the file into line-range chunks each ≤ 10,000 words. Preserve byte-identical content.
3. Write `manifest.yaml` with the required fields (§5), computing all hashes.
4. **Remove the original file** from the provenance root. The original content now lives in the archive-pack chunks (byte-identical); there is no duplication. (This removal is permissible during session close because D-017 immutability binds only on closed sessions.)
5. Update any in-session references (e.g., from `01-deliberation.md`) to use the `[archive: path]` convention.

The SESSION-LOG entry for the session records archive-pack presence with a one-phrase note (e.g., "archive-packs: 1 (outsider)").

### 10. Versioning

Version 1 established Session 022 per D-084. Subsequent revisions to this specification follow OI-002 substantive-vs-minor heuristic (`open-issues/OI-002.md`):
- **Substantive:** any change to the §1 enumeration, §2 budget values, §4 archive-pack structure, §5 manifest fields, §6 reference convention, or §7 integrity mechanism. Engine-version bump per `engine-manifest.md` §5.
- **Minor:** clarifying text edits, cross-reference updates, examples within existing scope.

## Validation

To validate this specification:

1. Confirm every file in the §1 enumeration exists at its declared path and carries the required frontmatter (for specifications) or is a well-formed index/close.md (for SESSION-LOG and open-issues).
2. Confirm every file in the §1 enumeration satisfies the §2 per-file budget. `tools/validate.sh` check 20 automates this verification.
3. Confirm that files not in the §1 enumeration but present in the workspace are either (a) explicitly archive surface (per §3), or (b) out-of-scope top-level files (e.g., `.git`, `.gitignore`, `.claude`, `.serena`, `applications/`), or (c) session-scratch files outside the read-contract scope.
4. For every archive-pack in `provenance/*/archive/*/`: confirm `manifest.yaml` is well-formed with all §5 required fields; confirm `source_hash_sha256` matches the actual hash of concatenated chunks in canonical order. `tools/validate.sh` check 21 automates this.
5. For every `[archive: path]` reference in a default-read surface file: confirm the reference resolves (path exists; chunk ordinals exist if specified). `tools/validate.sh` check 22 automates this.
6. Confirm that `methodology-kernel.md` §1 Read references this specification as the authority on default-read vs archive distinction.
7. Confirm that `prompts/development.md` and `prompts/application.md` read-activity instructions reference this specification as the authority.
8. Confirm that `workspace-structure.md` v4 §SESSION-LOG.md, §open-issues, and §specifications point at this specification for the access-discipline rules.

exec
/bin/zsh -lc 'rg -n "check 20|DEFAULT_READ_HARD_WORD_CEILING|DEFAULT_READ_SOFT_WORD_CEILING|READ_CONTRACT_ADOPTION_SESSION" tools/validate.sh specifications/validation-approach.md' in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
specifications/validation-approach.md:64:| 20 | Default-read surface per-file budget: every file in `read-contract.md` §1 default-read enumeration has body-word-count ≤ `DEFAULT_READ_HARD_WORD_CEILING` (Fail) or ≤ `DEFAULT_READ_SOFT_WORD_CEILING` (Warn) | read-contract §2 | Fail/Warn | session ≥ 022 |
specifications/validation-approach.md:102:**Session-number-gating (check 20).** Check 20 applies only to sessions numbered ≥ 022 (the session that adopted `specifications/read-contract.md` v1). The gate is encoded as an explicit constant `READ_CONTRACT_ADOPTION_SESSION=22` near the top of `validate.sh`. Out-of-scope sessions (001 through 021) produce no output from check 20 — pre-adoption SESSION-LOG.md / open-issues.md sizes are preserved as-is until the R8a / R8b migrations complete in Session 022.
specifications/validation-approach.md:111:DEFAULT_READ_HARD_WORD_CEILING=15000
specifications/validation-approach.md:112:DEFAULT_READ_SOFT_WORD_CEILING=10000
specifications/validation-approach.md:113:READ_CONTRACT_ADOPTION_SESSION=22
specifications/validation-approach.md:128:Archive-pack files and superseded-status specifications are excluded from check 20 scope.
specifications/validation-approach.md:246:- Default-read budgets (check 20) measure file size, not file relevance to the session's work. A file under the budget may still be effectively not-read; a file over the budget has failed even if its content was fully read in segments.
tools/validate.sh:28:readonly READ_CONTRACT_ADOPTION_SESSION=22
tools/validate.sh:29:readonly DEFAULT_READ_HARD_WORD_CEILING=15000
tools/validate.sh:30:readonly DEFAULT_READ_SOFT_WORD_CEILING=10000
tools/validate.sh:727:# A file can pass check 20 while being effectively unreadable (e.g., an opaque
tools/validate.sh:730:# Gate: session number >= READ_CONTRACT_ADOPTION_SESSION (=22).
tools/validate.sh:741:  if [[ $last_session_int -ge $READ_CONTRACT_ADOPTION_SESSION ]]; then
tools/validate.sh:746:  echo "  (pre-adoption; check 20 out-of-scope)"
tools/validate.sh:801:    if [[ $word_count -gt $DEFAULT_READ_HARD_WORD_CEILING ]]; then
tools/validate.sh:802:      fail "$rel — $word_count words exceeds hard ceiling ($DEFAULT_READ_HARD_WORD_CEILING). Restructure per read-contract.md §8 (sp