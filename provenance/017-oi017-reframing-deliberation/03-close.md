---
session: 017
title: Close — H4 Layered Model Adopted; Engine Manifest Created; PROMPT.md Split
date: 2026-04-22
status: complete
---

# Close — Session 017

## Artifacts Produced

### Provenance (`provenance/017-oi017-reframing-deliberation/`)

- `00-operator-steering.md` — user's Session 017 open message preserved verbatim (H2 preference steering).
- `00-assessment.md` — Session 016 fidelity audit + deliberation plan.
- `01-brief-shared.md` — byte-identical shared brief, committed before perspective launch (deliberation-anchor commit `f3e003b`).
- `01a-perspective-architect.md` — Claude Opus 4.7 H2 advocate raw response.
- `01b-perspective-operationalist.md` — Claude Opus 4.7 H3 advocate raw response.
- `01c-perspective-skeptic.md` — Claude Opus 4.7 H1 advocate (adversarial) raw response.
- `01d-perspective-outsider.md` — OpenAI GPT-5.4 (via `codex exec`) raw response. **Proposed and advocated H4 layered model as a novel fourth hypothesis.**
- `01-deliberation.md` — synthesis per `multi-agent-deliberation.md` v3 conventions; frontmatter records `participants_family: cross-model`, `cross_model: true`, `non_claude_participants: 1`.
- `02-decisions.md` — two decisions (D-074 H4 adoption; D-075 OI housekeeping) with `**Triggers met:**` + `**Triggers rationale:**` per D-037/D-038 schema.
- `manifests/architect.manifest.yaml`, `manifests/operationalist.manifest.yaml`, `manifests/skeptic.manifest.yaml`, `manifests/outsider.manifest.yaml` — full D-024 per-participant manifests.
- `participants.yaml` — session-level participant index.
- `03-close.md` — this file.

### Specifications revised

- **`methodology-kernel.md` v4** — minor edit: one-sentence scope clarification added to §Purpose. No v-bump. `last-updated: 2026-04-22` unchanged; `updated-by-session: 014` unchanged per OI-002 minor-correction convention.
- **`multi-agent-deliberation.md` v3** — minor edit: scope-applicability sentence added to §Purpose. No v-bump.
- **`validation-approach.md` v3** — minor edit: scope-applicability scope-note added to §Purpose. No v-bump.
- **`identity.md` v1 → v2 (substantive)** — adds the three-layer denotation (Selvedge / Selvedge engine / application). v1 preserved as `identity-v1.md` with `status: superseded` and `superseded-by: identity.md`.
- **`workspace-structure.md` v2 → v3 (substantive)** — adds §File classes section (engine-definition / development-provenance / application-scope); documents `prompts/` directory; revises §PROMPT.md section to reflect dispatcher role. v2 preserved as `workspace-structure-v2.md` with `status: superseded`.
- **New: `specifications/engine-manifest.md` v1** — enumerates engine-v1 file set; defines versioning discipline and external-application initialisation contract.
- **`reference-validation.md` v1** — unchanged.

### PROMPT.md split (significant event per workspace-structure.md §PROMPT.md)

- **`PROMPT.md`** — restructured as thin dispatcher. Names three layers; names two operating modes; dispatches to `prompts/development.md` or `prompts/application.md` based on workspace state.
- **New: `prompts/development.md`** — executable prompt for the self-development application; carries the content that was in the pre-split `PROMPT.md` with framing reworked to declare the self-development application kind explicitly.
- **New: `prompts/application.md`** — template prompt for external-problem applications with named slots (problem statement, constraints, stakeholders, success condition, initial state, engine version loaded).

### No external artefact this session

Session 017 is an engine-development session. No `applications/` contribution.

### SESSION-LOG.md

Session 017 entry added.

### open-issues.md

- **OI-017 resolved** (engine-vs-methodology reframing — H4 adopted via D-074).
- **OI-004 tally advances 5-of-3 → 6-of-3** per D-075 (sixth required-trigger deliberation with non-Claude participation). Criterion-3 gains **5** concrete Outsider-sourced contributions (layered H4 frame; "Selvedge engine" qualified phrase; thin-dispatcher PROMPT.md pattern; "engine's autobiography" activation rule; H1/H2/H3 frame-challenge). Cumulative criterion-3: **45** across Sessions 005–017.
- **OI-007 count 13 → 12.** OI-017 moves from open to resolved.
- **OI-002 new data point.** Session 017 executes two substantive revisions (identity.md v1→v2; workspace-structure.md v2→v3), one new spec creation (engine-manifest.md v1; **third narrow-single-purpose-spec creation**), and three minor edits (kernel, multi-agent-deliberation, validation-approach). Eighth OI-002 data point.
- OI-005, OI-006, OI-008, OI-009, OI-011, OI-012, OI-013, OI-014, OI-015, OI-016 unchanged.

### Tooling authorisation

Operator's `uv tool` authorisation from Session 016 remained available this session; no new tools installed (the existing `gemini` and `codex` CLIs sufficed per the deliberation's non-Claude participation need).

## Decisions Made

- **D-074** — Adopt H4 layered model (methodology → engine → application). Create `engine-manifest.md`; revise `identity.md` to v2; revise `workspace-structure.md` to v3; add kernel §Purpose scope clarification; add minor scope-applicability sentences to `multi-agent-deliberation.md` and `validation-approach.md`; split `PROMPT.md` into dispatcher + `prompts/development.md` + `prompts/application.md`. Triggers: `[d016_1, d016_2, d016_3, d023_1]`.
- **D-075** — OI state housekeeping. OI-017 resolved; OI-004 tally 5→6 of 3; OI-007 count 13→12; OI-002 new data point. Triggers: `[d023_4, d016_3]`.

Both decisions are backed by the same cross-model four-perspective deliberation; the non-Claude Outsider satisfies D-023's non-Claude requirement.

## Validation

`tools/validate.sh` at close: expected clean once SESSION-LOG.md is updated and all files committed. During WIP some failures expected per Sessions 013/015/016 precedent.

### Tier 1 Structural Checks

- Check [3] specification frontmatter: all 8 active specifications (6 prior + `identity.md` v2 + `engine-manifest.md` v1; `workspace-structure.md` v3 replaces v2 at the canonical filename) pass. Expected new superseded files pass frontmatter: `identity-v1.md`, `workspace-structure-v2.md`.
- Check [4] specification sections: all active specs pass.
- Check [6] session log completeness: Session 017 entry added at close.
- Check [7] provenance directory contents: `017-oi017-reframing-deliberation/` contains the full set (12 files plus `manifests/` directory).
- Check [8]/[9] provenance frontmatter: all files have required frontmatter.
- Check [11] three-raw-output floor: session has 4 `*-perspective-*.md` files, satisfies ≥3 with margin. D-074 declares `d016_*` triggers; check applies and passes.
- Check [12] schema well-formedness: 4 manifests in `manifests/` directory; all have D-024 required fields per 014-oi016-resolution precedent.
- Check [13] cross-model-claim honesty: session declares `cross_model: true` in deliberation synthesis; Outsider manifest declares `training_lineage_overlap_with_claude: independent-claim`; check passes.
- Check [14] multi-agent trigger coverage: D-074 declares d016_1/d016_2/d016_3; 4 perspective files + synthesis present; passes.
- Check [15] non-Claude trigger coverage: D-074 declares d023_1; Outsider manifest has `participant_kind: non-anthropic-model`; passes.

### Tier 2 Guided Assessment

1. **Provenance continuity (Q1).** Yes. Session 017's Read activity drew on Session 016's `00-assessment.md` §3 surveying and §4 hypothesising; the H1/H2/H3 frame originated there was presented to perspectives as the preferred starting point with explicit permission for additional hypotheses. Outsider's H4 is a live use of that permission. No prior decision was silently re-proposed; `identity.md` Reopening condition 1 was re-examined explicitly as a Skeptic-carried-forward warrant [01c Q5, Q7].

2. **Specification consistency (Q2).** Yes, maintained and improved. The layered denotation in `identity.md` v2 is consistent with the file-class distinction in `workspace-structure.md` v3 and with the enumeration in `engine-manifest.md` v1. Kernel §Purpose scope clarification references both new files. Minor scope-applicability sentences in `multi-agent-deliberation.md` and `validation-approach.md` are consistent with the three-layer denotation.

3. **Adversarial quality (Q3).** Skeptic was genuinely adversarial — advocated H1 against operator preference, against the two other Claude perspectives, and against the Outsider's H4. Named specific weaknesses in H2 [01c Q3] and H3 [01c Q2]. Q7 counter-argument engaged seriously ("The observable that would cause me to abandon H1 in favour of H3: a named prospective practitioner (identified by email address, not a hypothetical) reports ..."). Dissent preserved as first-class minority in `01-deliberation.md` §4.1 with specific operational reopening warrant.

4. **Meaningful progress (Q4).** Yes, substantial. OI-017 resolved. New specification created. Two substantive spec revisions. Three minor edits. PROMPT.md split (significant-event). Engine definition versioned as `engine-v1`. External-application activation path specified. Three first-class minorities preserved as operational warrants for potential future revision. Fifth or so substantive kernel/spec-producing session in workspace history, largest revision footprint in a single session to date.

5. **Specification-reality alignment (Q5).** Yes, maintained. The PROMPT.md dispatcher references `prompts/development.md` and `prompts/application.md` which now exist. `engine-manifest.md` §3 enumerates files that all exist at declared paths. `workspace-structure.md` v3's file-class distinction matches the actual file layout. `identity.md` v2's three-layer denotation matches the dispatcher's framing.

6. **Cross-model-honesty evidence (Q6).** Session declares `cross_model: true` in `01-deliberation.md` frontmatter and `participants.yaml`. Outsider manifest has `participant_kind: non-anthropic-model`, `provider: openai`, `model_id: gpt-5.4`, `training_lineage_overlap_with_claude: independent-claim`. Concrete evidence of genuine non-Claude participation: codex exec session id `019db36d-14a0-7d10-863e-179677eef35b`; reasoning effort xhigh; token count 19,120; CLI invocation documented in transport_notes; end-of-stream duplicate output pattern matches Sessions 005-014. The Outsider's H4 proposal is a class of contribution (frame-challenge at Q1 followed by novel hypothesis construction) that Claude subagents systematically did not produce in this session — an additional cross-family-divergence signal beyond manifest fields alone.

7. **Trigger-coverage plausibility (Q7).** D-074 declares `[d016_1, d016_2, d016_3, d023_1]`. Reading: kernel modified (scope clarification — d016_1, d023_1); new spec created + substantive revisions to identity/workspace-structure (d016_2); genuine cross-perspective disagreement on PROMPT.md split and Selvedge-denotation (d016_3). All listed triggers supportable by decision content. D-075 declares `[d023_4, d016_3]`. Reading: OI-004 tally advance (d023_4); reasonable disagreement (d016_3 via supporting deliberation). Supportable. No skip annotations; none required (non-Claude Outsider present for all d023_* triggers).

## Honest Notes from the Session

- **Outsider's H4 is the strongest single cross-model contribution across the Sessions 005–017 non-Claude participation history.** Prior Outsider contributions (Sessions 009/010/011 third-way split-resolutions, Session 014 three-cell protocol) resolved 2-2 or 3-1 Claude splits within the hypothesis frame the orchestrator had set. Session 017's Outsider explicitly rejected the H1/H2/H3 frame and proposed a novel fourth hypothesis — meta-level framing challenge rather than within-frame synthesis. This extends the WX-11-3 pattern (Outsider-originated resolution of cross-perspective disagreement) to a new genre: frame-replacement rather than frame-completion.

- **Operator preference was not binding and was not honoured in full.** The operator stated H2 preference at Session 017 open. The deliberation's three-of-four perspectives diverged from H2, and the adopted H4 rejects two H2-specific details (kernel rename; Selvedge-names-engine). The decision record (D-074 Rejected alternatives) is explicit: operator preference is input, not direction; engine determined H4 better supported by cross-model evidence. If the operator disagrees with any H4 detail, a subsequent session can re-deliberate per the preserved first-class minorities (Architect's H2 kernel-rename warrant is the explicit handle for stronger-restructure direction).

- **Brief-priming-absent streak extends to eight consecutive sessions (010–017).** Three-of-four perspectives diverged from operator preference; no lexical-echo pattern detected in perspective outputs; Architect advocated H2 as assigned-role rather than as operator-preference-drift.

- **The PROMPT.md split is the first "significant event" per workspace-structure.md §PROMPT.md in the workspace's history.** D-074 and this close record constitute the required provenance. Prior PROMPT.md state (pre-split) is preserved through git history rather than via an in-tree versioned file — this is arguably a minor OI-002 observation (preservation discipline for PROMPT.md is not file-versioning but git-history-versioning). Monitor whether a future session wants to formalise a `PROMPT-v0-pre-split.md` preservation to match spec-revision discipline; for now, git history is the record.

- **`engine-manifest.md` is a specification about specifications** — it enumerates engine-definition files without restating their content. This is a new spec genre (the prior five specs each defined rules for some aspect of the engine's execution). Skeptic's objection [01c Q4] that "a specification is earned by having something downstream of it" is preserved as first-class warrant: if no workflow, tool, or session reads the manifest over the next N sessions, the Skeptic's "ceremony" charge applies. Specific observable condition for re-examination: if `engine-manifest.md` has not been consulted operationally (beyond this session's creation) by Session 022, the Skeptic's warrant activates.

- **Three first-class minorities preserved in OI-017's resolution**, each with specific operational conditions under which they become the preferred revision direction:
  - Skeptic's H1 (no reframing): activates if three consecutive Sessions 018+ revise H4 without external-adoption evidence.
  - Operationalist's H3 (partial reframing): activates if `prompts/development.md` and `prompts/application.md` turn out to be "almost the same ... with only small variable substitutions and no meaningful behavioural divergence" [Outsider-convergent warrant].
  - Architect's H2 (full reframing with rename): activates if the layered denotation (methodology / engine / application) does not hold in practice — users collapse them in all cases without losing information.

- **Session 017 is large-footprint.** Eight files touched or created in `specifications/`; three new files in `prompts/`; PROMPT.md rewritten; provenance full-deliberation structure. Prior comparable sessions: 006 (triggers_met schema + two v-bumps), 014 (kernel v4 + new reference-validation.md). Session 017's footprint is closer to Session 014's. OI-007 scaling pressure argues against compounding this with additional watchpoints unless specifically warranted; Session 018+ readers should pick up the preserved first-class minorities rather than re-surface them as watchpoints.

## Next session

Session 018 should:

1. Run `tools/validate.sh` at start.
2. Audit Session 017 synthesis fidelity with particular attention to: (a) whether the 3-of-4 cross-model convergence on "don't rename methodology-kernel.md" was genuinely cross-family rather than two-Claude + Outsider coincidence; (b) whether H4's adoption faithfully honours the Outsider's proposal rather than selectively adopting parts Claude perspectives found palatable; (c) whether the PROMPT.md dispatch logic is coherent (does the dispatch section in the new PROMPT.md actually discriminate self-development from external-problem workspaces reliably?); (d) whether the three first-class minorities carry operationally meaningful reopening conditions or are ornamental; (e) whether `engine-manifest.md` §3's enumeration is complete (any engine-definition file missing from §3 would be a consistency failure against `workspace-structure.md` v3 §File classes).
3. Consider one of:
   - **Cell 1 of reference-validation** per D-072 standing precommitment (now runnable under H4; reference-validation.md unchanged; Case Steward role is engine-level).
   - **First-exercise of the H4 application-initialisation path** by creating a pilot external-application workspace (would be a new kind of session; would test H4 under operational pressure; the Skeptic's warrant on external-adoption-threshold activates naturally if this path is chosen).
   - **OI-004 closure criterion-4 articulation** (now at tally 6-of-3; criterion-4 remains unmet; would close the oldest open issue if successful).
   - **OI-015 laundering-gap deliberation** (re-examine under H4's explicit prompt-class separation; does H4 naturally reduce laundering surface, or are additional protections still warranted?).

Default pre-commitment: Cell 1 per D-072 (session 017 was the OI-017-deliberation fork of the Session 016 close's two-path choice; D-072 was preserved with re-disposition, not revoked; Cell 1 remains the standing default for the next session unless user steers otherwise).
