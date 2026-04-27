# External-problem application

You are running the Selvedge engine against a non-self problem. Your work produces artefacts in the application's domain (software, research, policy, physical systems, curricula, organisations, anything else). The engine's source-workspace provenance is **not** part of this workspace; you have only the loaded engine plus this application's brief and prior sessions.

## Read

Read this application's brief at the path named in `MODE.md` (`application_brief:`). The brief states:

- **Problem.** What is being designed, for whom, under what constraints.
- **Constraints.** Domain, time, stakeholder.
- **Stakeholders.** Who holds the problem; who receives the artefact; who validates it.
- **Success condition.** What the artefact must do, stated as observable evidence.
- **Initial state.** Any prior materials.

Then read the engine's active specifications (see `specifications/engine-manifest.md`). Then read this workspace's prior session closes by querying the substrate (`bin/selvedge query "SELECT session_no, slug, status FROM sessions ORDER BY session_no"` and reading the exported markdown). You do not read the source workspace's history; only the loaded engine and this workspace's record.

## Operate via the substrate (engine-v20+)

**The substrate is the only writable surface for session state.** Markdown files are exports; agents and operators read them, but no one authors them by hand. The flow:

1. `bin/selvedge submit session-open` — record the session.
2. `bin/selvedge submit assessment` — state and agenda as typed atoms.
3. `bin/selvedge submit deliberation-open` + `submit perspective` per perspective + `submit deliberation-seal` + `submit synthesis-point` — when convening multiple perspectives. At least one **domain perspective** grounded in the domain's actual practice.
4. `bin/selvedge submit decision-record` — typed decisions with supports, effects, alternatives, and rejections (all atoms; no prose).
5. `bin/selvedge submit review-finding` + `submit finding-disposition` — for any code-producing work, the coding review loop applies and T-20 blocks close on open medium-or-higher findings.
6. `bin/selvedge submit close-record` + `submit session-close` — close the session.
7. `bin/selvedge export --session <N> --write` — regenerate the provenance markdown view.
8. `bash tools/validate.sh` and `git commit` — durable cross-machine record.

You do **not** author markdown files for session phases. The substrate enforces that prose cannot hide in rows: atoms are 8–240 characters (16–480 for spec clauses), no newlines, no fenced code, no pipe tables. Multi-paragraph reasoning decomposes into typed `decision_supports`, `decision_effects`, `alternative_rejections`, and `perspective_claim` rows with closed-enum bases.

When the decision touches the methodology itself (you encountered a kernel gap, a spec is unclear, a tool failed), do **not** revise the engine in this workspace. Submit an engine-feedback row (TODO: engine-feedback submit kind extension) and continue with the application's work. Engine-feedback is transported by the operator back to the source workspace.

## Validate

Three senses apply per `specifications/methodology.md`:

- **Workspace validation** — always. The session's artefacts are internally consistent and the substrate's `selvedge validate --precommit` passes.
- **Domain validation** — when a domain-actor (named in §Stakeholders) is available. Get evidence the artefact functioned for its intended use. Record who validated, what was tried, what happened — as typed substrate rows, not prose.
- **Provisional reference substitute** — when no domain-actor is available, the session may compare its artefact to a sealed reference under blind conditions. The artefact carries the label `validation: reference-provisional`; this is a provisional substitute, not an equal third sense.

## Review

If the session produces, modifies, or deletes executable logic (any artefact whose execution behaviour the change alters), follow `specifications/methodology.md` §When to review §Coding review loop: invoke a reviewer subagent — distinct from the implementer — to audit the change. Address every medium-or-higher finding (fix or explicitly adjudicate via `submit finding-disposition` with a substantive reason). Re-invoke the reviewer. Repeat until no medium-or-higher findings remain or the loop halts at the four-iteration deadlock threshold (per the methodology spec). The Agent tool with `subagent_type=Explore` and an adversarial prompt is the default invocation.

If a structural validation check warns or fails, record whether the warning is engine-definition-related (engine-feedback) or application-scoped (fix before close).

## Produce

External artefacts live in `applications/NNN-<slug>/`. Frontmatter on produced artefacts records `originating_session`, `artefact_kind`, `domain`, `engine_version`, and the validation label. The artefacts themselves can be authored prose; only the *session-state* rows (assessment, decisions, review, close) must go through the substrate.

## Engine-feedback

When you encounter methodology-level friction during the application — an unclear spec, a kernel gap, a tool that doesn't function, a deliberation pattern that doesn't fit — record it. Until the engine-feedback substrate kind ships, write a markdown record at `engine-feedback/EF-<session>-<slug>.md`; once the kind ships, submit it. Keep the record specific and verbatim where applicable.

The operator transports feedback back to the source workspace at the operator's discretion. The engine does not specify automated cross-workspace transport.

## Cautions

- **Don't import ideas from outside the process.** External insights are hypotheses to be surveyed, not commitments.
- **Don't accept domain inputs as given context.** Constraints, stakeholder framings, and domain knowledge entering the session must be surveyed as options at Deliberate or Decide, not absorbed and re-examined silently.
- **Don't accumulate ceremony.** Each artefact should serve the application's success condition.
- **Don't author markdown for session state.** Substrate-only.
- **Don't track counters in prose.** Counts come from `bin/selvedge query`.

## Close

Submit `close-record` and `session-close`. Run `bin/selvedge export --session <N> --write` and `bash tools/validate.sh`. If a piece of work cannot complete, submit what was produced, record the blocker, and close cleanly. The session's close states what the next session should address as `next_session_should` close-state items.
