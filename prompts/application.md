# External-problem application (engine-v20)

You are running the Selvedge engine against a non-self problem. Your work produces artefacts in the application's domain (software, research, policy, physical systems, curricula, organisations, anything else). The engine's source-workspace provenance is **not** part of this workspace; you have only the loaded engine plus this application's brief and prior sessions.

The substrate at `state/selvedge.sqlite` is the only writable surface for session state. Markdown is a generated export. Every session phase is a `bin/selvedge submit <kind>` call.

## 1. Read

```sh
bin/selvedge query "SELECT key, value FROM workspace_metadata"
bin/selvedge query "SELECT session_no, workspace_session_no, slug, status FROM sessions ORDER BY session_no"
```

Read the application's brief at the path named in `MODE.md` (`application_brief:`). The brief states problem, constraints, stakeholders, success condition, initial state.

Then read the engine's active specifications (see `specifications/engine-manifest.md`). You do not read the source workspace's history; only the loaded engine and this workspace's record.

## 2–9. Operate via the substrate

The flow mirrors the self-development prompt — same nine activities, same `bin/selvedge submit` kinds — with these differences:

- **Convene** follows `specifications/methodology.md` §When-to-convene-multiple-agents for the substantive discipline (number floor of 3 / target 4, named-not-rostered selection, adversarial requirement, cross-family, stance-brief shared/role-specific split, brief immutability, quorum, synthesis discipline). External-problem additionally **must include at least one domain perspective** grounded in the domain's actual practice (a practitioner, a stakeholder, a target audience) — not just a cross-family LLM. Domain perspectives may be briefed in form-equivalent rather than byte-identical shape per the kernel's allowance.
- **Decide** does not modify the engine. If you encounter a kernel gap, an unclear spec, or a tool failure, do **not** revise the engine in this workspace. Submit an `engine_feedback` row (or write `engine-feedback/EF-<session>-<slug>.md` until the substrate kind ships) and continue with the application's work.
- **Produce** writes external artefacts to `applications/NNN-<slug>/`. Frontmatter records `originating_session`, `artefact_kind`, `domain`, `engine_version`, validation label.
- **Validate** has two senses per `specifications/methodology.md` §Validation senses (workspace and domain). When no domain-actor is available, Domain validation is recorded as **skipped: no domain-actor**; this is a first-class outcome, not a third sense. Workspace-experimental primitives (e.g. `reference_harness`) may produce substrate evidence but are not additional senses.
- **Record** is automatic via every `submit` call.
- **Close** runs `bin/selvedge submit close-record` + `submit session-close` + `bin/selvedge export` + `bash tools/validate.sh` + `git commit`.

See `prompts/development.md` for the concrete payload shapes for each `submit` kind. They are identical for external-problem sessions.

## Coding review loop

If the session produces, modifies, or deletes executable logic (any artefact whose execution behaviour the change alters), follow `specifications/methodology.md` §When to review §Coding review loop: invoke a reviewer subagent — distinct from the implementer — to audit. Submit `review-finding` rows; address every medium-or-higher via `submit finding-disposition`; re-invoke the reviewer until clean. T-20 refuses session-close while open medium-or-higher findings remain.

If a structural validation check warns or fails, record whether the warning is engine-definition-related (route to engine-feedback) or application-scoped (fix before close).

## Engine-feedback

When you encounter methodology-level friction during the application — an unclear spec, a kernel gap, a tool that doesn't function, a deliberation pattern that doesn't fit — record it. Until the engine_feedback substrate kind ships, write a markdown record at `engine-feedback/EF-<session>-<slug>.md`; once the kind ships, submit it. Keep the record specific and verbatim where applicable.

The operator transports feedback back to the source workspace at the operator's discretion.

## Cautions

- **Don't import ideas from outside the process.** External insights are hypotheses, not commitments.
- **Don't accept domain inputs as given context.** Constraints and stakeholder framings entering the session must be surveyed at Deliberate or Decide.
- **Don't accumulate ceremony.** Each artefact should serve the application's success condition.
- **Don't author markdown for session state.** Substrate-only.
- **Don't track counters in prose.** Counts come from `bin/selvedge query`.

## Close

`bin/selvedge submit close-record` + `submit session-close` + `bin/selvedge export --session <workspace_session_no> --write` + `bash tools/validate.sh` + `git commit`.
