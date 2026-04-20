---
title: Methodology Identity
version: 1
status: active
created: 2026-04-20
last-updated: 2026-04-20
updated-by-session: 012
supersedes: none
---

# Methodology Identity

## Purpose

This specification records the methodology's canonical name and the reasoning behind it. Its scope is narrow by design: the name, its origin, its intended use, and the conditions under which reopening the naming question would be legitimate. It does not record mission statements, values, principles, or other identity content beyond the name itself.

Opened as the closure artefact for OI-001 (methodology naming), which was open from Session 001 through Session 012.

## Specification

### Canonical name

**Selvedge.**

The methodology is referred to as Selvedge.

### Origin of the name

The word *selvedge* is the self-finished edge of woven cloth — the edge that does not need hemming because the weave itself is closed there. In textile craft, the selvedge is what keeps cloth from unravelling at the margin.

Three properties of this methodology are named by that metaphor:

- **Self-hosting.** The methodology weaves its own edges. It evolves by running its own process on itself; its own specifications, its own kernel, its own validation approach are all produced and revised by the same mechanism the methodology teaches.
- **Multi-strand preservation.** Perspectives disagree, and the disagreement is preserved rather than melted into consensus. Specifications are versioned and superseded rather than overwritten. Decisions record rejected alternatives alongside what was adopted. The reasoning remains legible strand-by-strand to later readers.
- **Durability by construction.** The woven edge keeps the cloth from fraying. The methodology's preservation discipline — v1/v2/v3 files, explicit `supersedes`/`superseded-by` pointers, provenance as a first-class output — keeps prior reasoning from being lost even as the methodology evolves.

The metaphor names these three properties without privileging any of the nine core activities over the others. It does not commit the methodology to a specific domain of application.

### What the name does

The name is a **reference handle**. It gives the methodology something to be called when it is referred to from outside the workspace, and it resolves the awkwardness of the "the methodology" formulation in external artefacts and external discussion. It is not a brand, a slogan, or a claim of school.

The name changes reference, not structure. It does not alter the kernel's nine activities, the multi-agent-deliberation specification, the validation approach, or any other specification. The kernel file remains `methodology-kernel.md`; the kernel's title remains "Methodology Kernel"; specifications are not renamed. External artefacts and external communication may use the name; internal specifications may continue to use "the methodology" where that reads more naturally.

### Scope of this file

This file's scope is the name and its immediate reasoning. Expansion into a general identity document (mission statements, values, principles, manifestos) is not an intended use of this file. If identity content beyond the name is ever needed, it belongs in a separate specification produced by a distinct deliberation, not appended here.

### Reopening conditions

OI-001 closed in Session 012 via the deliberation preserved at `provenance/012-methodology-naming/`. The refuse-to-name minority position — that naming is premature; that identity accumulation is not the same as external standing; that a name creates attachment the methodology's disciplines have otherwise worked to avoid — is preserved as first-class dissent in that deliberation's raw perspective file (`01c-perspective-skeptic.md`) and in the decision record.

If any of the following conditions comes to hold, a future session may legitimately reopen the question of whether the name Selvedge was premature. These conditions are drawn from the deliberation's cross-model convergence on "evidence that would make naming clearly right rather than merely defensible":

1. **External adoption threshold.** A named practitioner outside this workspace uses the methodology for at least three months on their own work, with feedback that affects at least one kernel revision.
2. **Cross-domain artefact threshold.** At least three externally validated artefacts across materially different domains (not personal micro-guides of similar shape).
3. **Kernel-stability threshold.** At least five consecutive sessions without kernel revision, demonstrating that the nine-activity frame has stabilised under pressure rather than merely between pressures.
4. **External naming pushback.** An external reader or user reports that the name Selvedge blocks or distorts their engagement with the methodology (e.g., the textile metaphor misleads them about the methodology's scope, or the name collides with something in their context).

Reopening under any of these conditions would be legitimate methodology work. Reopening in their absence would bear the burden of showing why.

### Adoption and revisability

Adopted in Session 012 via D-063 with user ratification. The ratification selected:
- The name **Selvedge** from a shortlist of three (Selvedge, Sediment, Strata), with "the methodology" refusal preserved as the fourth option.
- This file (`specifications/identity.md`) as the canonical placement, per Outsider-primary and Skeptic-conditional convergence. Alternative placements considered were kernel frontmatter (Namer's preference) and broader placement including kernel title + PROMPT.md (Steward's preference).

The name is revisable under the methodology's normal specification-revision discipline: if a future session revises it, the current file is preserved as `identity-v1.md` with `status: superseded` and `superseded-by` pointer, and a new `identity.md` takes its place. Revision should be grounded in one of the reopening conditions above; a name that changes repeatedly is worse than no name.

## Validation

**Workspace validation** for this specification: the name Selvedge and its placement in this file do not contradict any other active specification. `methodology-kernel.md` is unchanged; `workspace-structure.md` is unchanged; `multi-agent-deliberation.md` is unchanged; `validation-approach.md` is unchanged. The `specifications/` directory now contains this additional file; the `tools/validate.sh` check for required frontmatter fields and required sections (Purpose, Specification, Validation) passes.

**Domain validation** for this specification is of a peculiar shape: the methodology's "domain-actor" for its own naming is the methodology's own practitioner, and the user has ratified the name at Session 012 close. For the broader question — whether the name works as an external reference handle for readers outside the workspace — domain validation will accumulate as external artefacts (`applications/NNN-*/`) reference the methodology by name. The first such reference will constitute initial domain evidence; sustained comfortable use across multiple external-artefact sessions will be stronger evidence; external-reader pushback (per reopening condition 4) would be adverse evidence.

This validation section should not be substantially edited by future sessions unless the name itself changes. If reopening conditions are met and the deliberation elects to revise or retire the name, the revision's validation logic belongs in the new version, not retrofitted here.
