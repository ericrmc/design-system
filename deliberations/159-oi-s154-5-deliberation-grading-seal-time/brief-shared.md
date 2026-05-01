# D-23 Shared Brief — Seal-time deliberation-grading clause

## Methodology context

You are participating as one perspective in a Selvedge cross-family deliberation. Selvedge is a methodology that produces durable provenance by running diverse perspectives against load-bearing decisions, preserving disagreement as first-class output, and evolving its own kernel through the same mechanic.

The substrate at `state/selvedge.sqlite` is the canonical record. Markdown in `provenance/` is a generated export. Specs (engine-manifest, methodology, prompt-development, prompt-application, workspace) are the active engine-definition file set; engine-v45 is current.

You are NOT to import ideas from outside the recorded record. Surface external insight as a hypothesis, not a commitment. Cite the workspace material you rely on.

## Problem statement

OI-S154-5 (MEDIUM, open since S154) names a discipline gap:

> "Deliberation-grading discipline — name single-frame counterfactual at seal time, not at retrospective time; sub-type verification at typed-observation closure."

The S155 cross-family deliberation D-21 explicitly excluded this gap when shipping the close-time interpretive-choice audit (DV-S155-1) on the grounds that seal-time grading has a different trigger (deliberation-seal vs session-close), a different actor (synthesizer vs close author), and different evidence (perspective-output vs plan-prose). All five S155 perspectives converged on excluding S154-5; OI-S154-5 was kept open as a sibling for separate treatment.

The session's task is to decide the **shape** of the seal-time clause that closes OI-S154-5.

## Design questions

1. **Two-clause or one?** OI-S154-5 bundles two concerns: (a) name a single-frame counterfactual at seal time, not retrospectively; (b) verify sub-type assignment at typed-observation closure (per DV-S152-1 conflict_kind/closure_kind opt-in atoms on reference_harness). Are these one discipline applied at two phases, or two distinct disciplines that should be spec'd separately?

2. **Authority — operator-policed or substrate-gated?** DV-S155-1 shipped the close-time audit operator-policed with a typed-observation→gate promotion trigger (calibration-EF naming an unlifted miss fires a substrate gate). Should the seal-time clause follow the same v1-operator-policed → v2-gate pattern, or should it differ given the synthesizer (an LLM) is the actor rather than the operator?

3. **Payload shape.** The close-time audit uses an `engine_feedback` row with prefix `audit-step:` and three dispositions per choice (lifted-to-A-NNN, deferred-to-FR, accepted-implicit). What is the equivalent for seal-time? Candidates:
   - An engine_feedback row with prefix `seal-grade:` enumerating counterfactuals named.
   - A new typed `synthesis_point` kind beyond existing `convergence | divergence | minority` (e.g. `counterfactual`).
   - A free-prose section in the synthesis_md body, no new substrate.

4. **Definition of single-frame counterfactual.** A "single-frame counterfactual" is a position no perspective took but that a future reader could surface as a load-bearing alternative reading the synthesis admits but did not address. Is this definition tight enough to be policeable? What exclusions belong (e.g. micro-naming, ordering)?

5. **Sub-type verification scope.** Sub-type verification only applies to deliberations using harness typed-observation closure (currently disaster-response arc only; per DV-S152-1 conflict_kind/closure_kind nullable opt-in atoms). Does the seal-time clause carry the verification, or is verification a separate harness-level concern that should remain with the harness substrate kind?

6. **Promotion trigger.** What is the trigger condition for graduating from operator/agent-policed to substrate-gated? Mirror DV-S155-1 (calibration-EF naming an unlifted miss), or different shape given different evidence?

7. **Scope limits.** Should the clause apply to every deliberation-seal, or only deliberations meeting some weight threshold (methodology-changing, kernel-touching, multi-arc)?

## Evidence base

Read these before authoring:

- `specifications/methodology.md` v10 §When-to-convene-multiple-agents and §Synthesis (current discipline).
- `prompts/development.md` §4 Convene perspectives (CLI surface) and §8.5 Close-time interpretive-choice audit (sibling pattern; cites DV-S155-1).
- `provenance/155-close-time-self-audit-step/01-deliberation.md` (D-21 five-perspective rationale for excluding S154-5).
- `provenance/155-close-time-self-audit-step/02-decisions.md` (DV-S155-1 shape + R-1.5 rejected fold-S154-5 alternative).
- The substrate: `bin/selvedge query "SELECT alias, name FROM objects WHERE alias LIKE 'OI-S154-%'"` (sibling OIs from same triage).
- DV-S152-1 typed-observation pathway at workspace-experimental layer (`provenance/152-typed-conflict-primitive-seam/`).

## Response format

Author `deliberations/159-oi-s154-5-deliberation-grading-seal-time/perspective-N.json` with:

```json
{
  "deliberation_id": 23,
  "label": "P-N",
  "family": "anthropic|openai|google|other-llm|human",
  "expected_disagreement_axis": "<short phrase>",
  "body_md": "<your full perspective>"
}
```

The body_md must contain:

- **Position.** (one paragraph distilling your single sentence answer to the design questions, suitable as `perspective-position`).
- **Schema sketch.** (bullets — substrate shape if any).
- **CLI surface.** (bullets — the bin/selvedge submit shape).
- **Migration path.** (bullets — what changes ship in this session vs deferred).
- **What not.** (bullets — alternatives explicitly rejected).
- **Open questions.** (bullets).
- **Risks.** (bullets).
- **What lost.** (bullets — what your shape forecloses relative to the strongest alternative).

Each bullet becomes one `perspective-claim` row at decomposition; keep each bullet 8–240 chars, single sentence, no newlines, no fenced code, no pipe tables.

## Constraint on external imports

Do not import ideas from training-distribution context outside the recorded Selvedge workspace. If you draw on a concept the substrate has not deliberated, name it as a hypothesis with explicit acknowledgment that it is unsourced. Cite the substrate material you rely on. "I don't know" is a valid output; fabrication is not.
