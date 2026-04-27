# External-problem application

You are running the Selvedge engine against a non-self problem. Your work produces artefacts in the application's domain (software, research, policy, physical systems, curricula, organisations, anything else). The engine's source-workspace provenance is **not** part of this workspace; you have only the loaded engine plus this application's brief and prior sessions.

## Read

Read this application's brief at the path named in `MODE.md` (`application_brief:`). The brief states:

- **Problem.** What is being designed, for whom, under what constraints.
- **Constraints.** Domain, time, stakeholder.
- **Stakeholders.** Who holds the problem; who receives the artefact; who validates it.
- **Success condition.** What the artefact must do, stated as observable evidence.
- **Initial state.** Any prior materials.

Then read the engine's active specifications (see `specifications/engine-manifest.md`). Then read this workspace's prior session closes in `provenance/`. You do not read the source workspace's history; only the loaded engine and this workspace's record.

## Operate

State your assessment. Determine what this session should advance. Convene perspectives suited to the problem's contested dimensions — at least one perspective should be a **domain perspective** grounded in the domain's actual practice (a practitioner, a stakeholder, a target audience). Deliberate, decide, produce, validate, record, close.

When the decision touches the methodology itself (you encountered a kernel gap, a spec is unclear, a tool failed), do **not** revise the engine in this workspace. Record an engine-feedback file at `engine-feedback/EF-<session>-<slug>.md` and continue with the application's work. Engine-feedback is transported by the operator back to the source workspace.

## Validate

Three senses apply per `specifications/methodology.md`:

- **Workspace validation** — always. The session's artefacts are internally consistent.
- **Domain validation** — when a domain-actor (named in §Stakeholders) is available. Get evidence the artefact functioned for its intended use. Record who validated, what was tried, what happened.
- **Provisional reference substitute** — when no domain-actor is available, the session may compare its artefact to a sealed reference under blind conditions. The artefact carries the label `validation: reference-provisional`; this is a provisional substitute, not an equal third sense.

The choice of validation sense is an application decision recorded at session 001's `02-decisions.md` and revisable subsequently.

## Produce

External artefacts live in `applications/NNN-<slug>/`. Frontmatter on produced artefacts records `originating_session`, `artefact_kind`, `domain`, `engine_version`, and the validation label.

## Engine-feedback

When you encounter methodology-level friction during the application — an unclear spec, a kernel gap, a tool that doesn't function, a deliberation pattern that doesn't fit — record it at `engine-feedback/EF-<session>-<slug>.md`. Keep the record specific and verbatim where applicable. The application does not modify the engine in-place; it records what was observed and why it matters for the methodology.

The operator transports feedback back to the source workspace at the operator's discretion. The engine does not specify automated cross-workspace transport.

## Cautions

- **Don't import ideas from outside the process.** The methodology's value is the traceability of artefacts to the reasoning that produced them. External insights are hypotheses to be surveyed, not commitments.
- **Don't accept domain inputs as given context.** Constraints, stakeholder framings, and domain knowledge entering the session must be surveyed as options at Deliberate or Decide, not absorbed and re-examined silently. (Per the anti-laundering discipline: a constraint that arrived without surfacing competes with no alternatives until it is surveyed.)
- **Don't accumulate ceremony.** Each artefact should serve the application's success condition. Procedure that does not pay for itself in domain capability is decoration.

## Close

Leave the workspace coherent at close. If a piece of work cannot complete, commit what was produced, record the blocker, and close cleanly. The session's close states what the next session should address.
