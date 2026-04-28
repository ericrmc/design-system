---
title: Methodology Identity
version: 2
status: active
created: 2026-04-20
last-updated: 2026-04-22
updated-by-session: 017
supersedes: identity-v1.md
---

# Methodology Identity

## Purpose

This specification records the methodology's canonical name and the reasoning behind it, and establishes the denotation layering between the methodology, its current engine, and the applications of that engine. Its scope is narrow by design: the name, its origin, its intended use, the three-layer denotation, and the conditions under which reopening the naming question would be legitimate. It does not record mission statements, values, principles, or other identity content beyond the name itself.

Opened as the closure artefact for OI-001 (methodology naming), which was open from Session 001 through Session 012. Revised v1 → v2 in Session 017 per D-074 to add the three-layer denotation; v1 preserved as `identity-v1.md`.

## Specification

### Canonical name

**Selvedge.**

The methodology is referred to as Selvedge.

### Layered denotation (added v2, Session 017)

The word "Selvedge" operates across three layers:

- **Selvedge** (unqualified) — names **the methodology**: the abstract-approach, domain-general mechanic of diverse perspectives reasoning together, producing durable artefacts, preserving reasoning, and evolving the system by running the same mechanic on its own outputs.
- **Selvedge engine** (qualified phrase) — denotes **the current executable implementation** of the Selvedge methodology: the loadable file set enumerated in `specifications/engine-manifest.md` at any given engine version. The engine is a concrete thing (files + prompt); the methodology is the abstract approach the engine realises.
- **Application of the Selvedge engine** — any specific run of the engine against a problem. Two kinds of application are recognised:
  - **Self-development application** — the engine evolves its own specifications by running on its own outputs. This workspace (sessions 001–017+) is the foundational self-development application. Driven by `prompts/development.md` per D-074.
  - **External-problem application** — the engine runs against a non-self problem, using the same engine definition plus application-specific context. Driven by `prompts/application.md` per D-074. No external application had been launched at the time of this revision.

The unqualified name points to the broader thing (methodology). The qualified phrase ("Selvedge engine") points to the concrete, loadable thing. The application layer names specific runs. This three-layer denotation resolves the two-sense ambiguity surveyed in Session 016 and elaborated through the OI-017 deliberation in Session 017.

Internal specifications may use "the methodology," "the engine," or "the application" where that reads more naturally; external communication should prefer "Selvedge" for the methodology, "Selvedge engine" for the implementation, and "an application of Selvedge" or similar for a specific run.

### Origin of the name

The word *selvedge* is the self-finished edge of woven cloth — the edge that does not need hemming because the weave itself is closed there. In textile craft, the selvedge is what keeps cloth from unravelling at the margin.

Three properties of this methodology are named by that metaphor:

- **Self-hosting.** The methodology weaves its own edges. It evolves by running its own process on itself; its own specifications, its own kernel, its own validation approach are all produced and revised by the same mechanism the methodology teaches.
- **Multi-strand preservation.** Perspectives disagree, and the disagreement is preserved rather than melted into consensus. Specifications are versioned and superseded rather than overwritten. Decisions record rejected alternatives alongside what was adopted. The reasoning remains legible strand-by-strand to later readers.
- **Durability by construction.** The woven edge keeps the cloth from fraying. The methodology's preservation discipline — v1/v2/v3 files, explicit `supersedes`/`superseded-by` pointers, provenance as a first-class output — keeps prior reasoning from being lost even as the methodology evolves.

The metaphor names these three properties without privileging any of the nine core activities over the others. It does not commit the methodology to a specific domain of application.

### What the name does

The name is a **reference handle**. It gives the methodology something to be called when it is referred to from outside the workspace, and it resolves the awkwardness of the "the methodology" formulation in external artefacts and external discussion. It is not a brand, a slogan, or a claim of school.

The name changes reference, not structure. It does not alter the kernel's nine activities, the multi-agent-deliberation specification, the validation approach, or any other specification. The `methodology-kernel.md` filename remains unchanged per D-074 Session 017 three-of-four cross-model convergence against rename; the kernel's title remains "Methodology Kernel." Specifications are not renamed. External artefacts and external communication may use the name; internal specifications may continue to use "the methodology," "the engine," or "the application" where that reads more naturally.

### Scope of this file

This file's scope is the name, its immediate reasoning, and the three-layer denotation. Expansion into a general identity document (mission statements, values, principles, manifestos) is not an intended use of this file. If identity content beyond the name and layered denotation is ever needed, it belongs in a separate specification produced by a distinct deliberation, not appended here.

### Reopening conditions

OI-001 closed in Session 012 via the deliberation preserved at `provenance/012-methodology-naming/`. The refuse-to-name minority position — that naming is premature; that identity accumulation is not the same as external standing; that a name creates attachment the methodology's disciplines have otherwise worked to avoid — is preserved as first-class dissent in that deliberation's raw perspective file (`01c-perspective-skeptic.md`) and in the decision record.

Session 017's D-074 adds the layered denotation without reopening the name itself. The Reopening conditions below are preserved verbatim from v1.

If any of the following conditions comes to hold, a future session may legitimately reopen the question of whether the name Selvedge was premature. These conditions are drawn from the deliberation's cross-model convergence on "evidence that would make naming clearly right rather than merely defensible":

1. **External adoption threshold.** A named practitioner outside this workspace uses the methodology for at least three months on their own work, with feedback that affects at least one kernel revision.
2. **Cross-domain artefact threshold.** At least three externally validated artefacts across materially different domains (not personal micro-guides of similar shape).
3. **Kernel-stability threshold.** At least five consecutive sessions without kernel revision, demonstrating that the nine-activity frame has stabilised under pressure rather than merely between pressures.
4. **External naming pushback.** An external reader or user reports that the name Selvedge blocks or distorts their engagement with the methodology (e.g., the textile metaphor misleads them about the methodology's scope, or the name collides with something in their context).

Reopening under any of these conditions would be legitimate methodology work. Reopening in their absence would bear the burden of showing why.

Session 017's Skeptic-perspective warrant [`provenance/017-oi017-reframing-deliberation/01c-perspective-skeptic.md` Q5] preserved as first-class minority: Reopening condition 1 (external adoption threshold) remained unmet at Session 017 open, and Skeptic argued H4 adoption "de facto triggers" the condition without satisfying it. The synthesis adopted H4 anyway on cross-model-weighted grounds [`provenance/017-oi017-reframing-deliberation/01-deliberation.md` §2.3, §6]. The Skeptic's warrant stands: if three consecutive Sessions 018+ revise H4's adopted shape without external-adoption evidence, the Skeptic's preservation-discipline argument becomes the preferred revision direction toward H1 (no reframing).

### Adoption and revisability

Adopted in Session 012 via D-063 with user ratification. The ratification selected:
- The name **Selvedge** from a shortlist of three (Selvedge, Sediment, Strata), with "the methodology" refusal preserved as the fourth option.
- This file (`specifications/identity.md`) as the canonical placement, per Outsider-primary and Skeptic-conditional convergence. Alternative placements considered were kernel frontmatter (Namer's preference) and broader placement including kernel title + PROMPT.md (Steward's preference).

Revised Session 017 via D-074 to add the three-layer denotation (Selvedge / Selvedge engine / application of the Selvedge engine). v1 preserved as `identity-v1.md` with `status: superseded` and `superseded-by: identity.md`.

The name is revisable under the methodology's normal specification-revision discipline: if a future session revises it, the current file is preserved as `identity-v2.md` (or the next v-integer) with `status: superseded` and `superseded-by` pointer, and a new `identity.md` takes its place. Revision should be grounded in one of the Reopening conditions above; a name that changes repeatedly is worse than no name.

## Validation

**Workspace validation** for this specification: the name Selvedge, the three-layer denotation, and the placement in this file do not contradict any other active specification. `methodology-kernel.md` was minor-edited in Session 017 with a scope-clarification sentence referencing this file and `engine-manifest.md`; `workspace-structure.md` was revised v2 → v3 in Session 017 adding the three file-class distinction consistent with the denotation layering; `multi-agent-deliberation.md` and `validation-approach.md` received minor scope clarifications stating their rules apply to both application kinds; `reference-validation.md` is unchanged. The `specifications/` directory now contains `engine-manifest.md` v1 (new) and `identity-v1.md` (preserved superseded) alongside this v2 active file; the `tools/validate.sh` check for required frontmatter fields and required sections passes.

**Domain validation** for this specification is of a peculiar shape: the methodology's "domain-actor" for its own naming and layered denotation is the methodology's own practitioner, and the user has ratified the name at Session 012 close and the reframing direction at Session 017 open. For the broader question — whether the layered denotation works as an external reference handle for readers outside the workspace — domain validation will accumulate as external artefacts (`applications/NNN-*/`) reference Selvedge, the Selvedge engine, or applications of the engine. The first such reference after v2 will constitute initial domain evidence for the denotation layering; sustained comfortable use across multiple external-artefact sessions will be stronger evidence; external-reader pushback (per Reopening condition 4 or any clarity concern specific to the three layers) would be adverse evidence.

This validation section should not be substantially edited by future sessions unless the name itself or the denotation layering changes. If Reopening conditions are met and the deliberation elects to revise or retire the name or the layering, the revision's validation logic belongs in the new version, not retrofitted here.
