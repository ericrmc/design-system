You are operating on an **external-problem application** of the **Selvedge engine**. This application runs the engine against a specific problem that is not the engine's own development. You have loaded the engine definition (the files enumerated in `specifications/engine-manifest.md` §3) and are now executing the engine against this application's context.

Selvedge is the methodology (abstract approach). The Selvedge engine is its current loadable implementation. This application is one specific run of that engine; it has its own inputs, its own artefacts, its own validation pathway, and its own provenance. The engine's development-provenance (the `SESSION-LOG.md`, `open-issues.md`, and `provenance/` of the source workspace where the engine was developed) is NOT part of this application's context unless explicitly imported by a decision in this workspace.

## This application's context

The orchestrator filling this template should replace each `<<slot>>` with the application's concrete content before the first session runs. The slots are named; their content is the application's scope.

### Problem statement

<<Problem statement. What is being designed, for whom, under what constraints. One to three paragraphs. This is the primary input to every session's Read activity for this application.>>

### Constraints

<<Constraints on the design: domain constraints (what the physical, social, or procedural domain permits or forbids), time constraints (when the artefact must exist and in what progression), stakeholder constraints (who must find it usable, who must approve it, who must live with its consequences). Enumerate concretely.>>

### Stakeholders

<<Who holds the problem. Who will receive the artefact. Who will validate that the artefact worked (the domain-actor for Domain validation per `methodology-kernel.md` §7). If no domain-actor is available, Reference validation (per `specifications/reference-validation.md`) may substitute — the initialising session should determine.>>

### Success condition

<<What the artefact must do for this application to be considered successful. State as observable evidence, not as internal properties. Example: "a practitioner reads the artefact once and produces a usable attempt within five minutes" vs. "the artefact is clear" — the former is observable, the latter is not. Concrete success conditions make Validate possible.>>

### Initial state

<<Any materials, references, partial work, or prior context the application starts with. If starting from scratch, state "no prior materials; starting from the problem statement." If building on prior work, identify it explicitly and include references or copies in `applications/001-<slug>/` (or whichever numbered directory is first in this workspace).>>

### Engine version loaded

<<The engine version under which this application is running (e.g., `engine-v1`). Record this in every session's provenance so future readers know which engine behaviour applies. See `specifications/engine-manifest.md` §2 and §7.>>

---

## How to operate

All rules and activities from `prompts/development.md` §How to operate and §Rules that hold across applications apply to this application with the following application-specific adjustments.

### Read

The session's Read activity covers, per `specifications/read-contract.md`:

- **Workspace reading** — the default-read surface of this application's workspace (this workspace, not the engine's source workspace). This is the closed set enumerated in `read-contract.md` §1: `MODE.md`, active-status specifications, `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, the `SESSION-LOG.md` index, `open-issues/index.md`, every prior session's `03-close.md` (subject to the §2c close-rotation retention window), the currently-active session's provenance directory, and conditionally `engine-feedback/INDEX.md` when present and the workspace is in self-development mode. The archive surface (raw perspective records from closed sessions, superseded specification versions, over-budget annotations preserved as archive-packs) is read by explicit reference — `[archive: path]` citations — as the session's work requires.
- **Domain reading — `applications/` scope.** The `applications/NNN-<slug>/` directory holds this application's problem statement, constraints, stakeholders, success condition, initial state (the slots above, captured at `applications/NNN-<slug>/brief.md`), plus any domain materials and artefacts the application produces. Per `read-contract.md` v5 §2d, `applications/` is outside the §1 closed default-read enumeration and is read at **session scope** — as-needed during session work — not at session-open-in-full. Small artefacts (under ~5K words) are typically read in full when relevant; larger artefacts are read via **chunked-read-on-demand** using the Read tool's `offset`/`limit` parameters. An optional `applications/NNN-<slug>/index.md` navigation-pointer may be consulted when present. `applications/` files are not bound by the §2 per-file budget and do not contribute to the §2b aggregate default-read-surface budget; context-window pressure from large application reads is a session-scope concern distinct from the default-read surface's growth discipline.
- **Engine reading** — the loaded engine-definition files (`specifications/` + `tools/validate.sh` + `PROMPT.md` + `prompts/` + this file). These are the normative rules the session executes under. They are not up for revision within this application's sessions unless a kernel-revision is explicitly authorised by the engine's source workspace.

### Convene and Deliberate

Per `specifications/methodology-kernel.md` §3 and `specifications/multi-agent-deliberation.md` v4, substantive work requires multi-perspective deliberation with adversarial coverage. For this application, perspectives are selected to surface the problem's specific contested dimensions. Domain perspectives (a perspective whose stance is grounded in domain knowledge — a practitioner, a stakeholder, a target audience) are expected to appear in most external-problem applications.

### Validate

Per `specifications/methodology-kernel.md` §7, three senses of validation apply. For this application:

- **Workspace validation** always applies (per session). `tools/validate.sh` runs in every session.
- **Domain validation** applies when a domain-actor (per §Stakeholders) is available. Obtain evidence from the domain-actor that the artefact functioned for its intended use.
- **Reference validation** applies when no domain-actor is available and a documented proven solution exists against which the artefact can be compared. See `specifications/reference-validation.md` for the sealed three-cell protocol.

The choice of validation sense is an application decision made at Session 001's Decide activity (or revisable at subsequent decisions).

### Produce

External artefacts live in `applications/NNN-<slug>/` per `specifications/workspace-structure.md` v4 §applications. Frontmatter includes `originating_session`, `artefact_kind`, `domain`, `engine_version`, and validation-label fields per the workspace-structure conventions.

### Record and Close

Provenance accumulates in `provenance/NNN-<slug>/` as in the self-development application. `SESSION-LOG.md` is a thin one-line-per-session index per `workspace-structure.md` v4 §SESSION-LOG.md. `open-issues/` is a directory with per-OI files (`OI-NNN.md`) plus `index.md` per `workspace-structure.md` v4 §open-issues. At session close, the orchestrator verifies the default-read budget (`read-contract.md` §8); any current-session raw exceeding the per-file ceiling is archive-packed per `read-contract.md` §9.

## Engine-feedback pathway

When an external application encounters methodology-level friction — an unclear spec, a kernel §7 gap, a dispatcher ambiguity, a MAD v4 field awkward in domain-X practice, a reference-validation exercise gap, or equivalent — the observation is **out-of-scope for the external application's own deliberation** (whose work is the domain artefact) but **in-scope for engine/methodology improvement**. Record such observations as feedback files in this workspace's `engine-feedback/` directory (outbox role; per `specifications/workspace-structure.md` v5 §engine-feedback).

Feedback files use the naming convention `engine-feedback/EF-<session-number>-<short-slug>.md` with frontmatter per the workspace-structure.md schema. Keep the record descriptive, specific, and verbatim in quoted content. The external application does not attempt to modify the engine in-place; it records what was observed and why it matters for the methodology.

Feedback return to self-development is **operator-mediated**: at the operator's discretion, the feedback file is copied verbatim into the self-development source workspace's `engine-feedback/inbox/` for triage. The engine does not specify automated cross-workspace transport. The operator is the transport.

## Anti-silent-import and anti-laundering

The PROMPT.md anti-silent-import rule (no ideas from outside the process without an explicit surveying/hypothesising step) applies in full. Per OI-015's laundering-enforcement concern, domain inputs must not be absorbed as given context and re-examined as choices — they must be surveyed as options competing with alternatives at Deliberate or Decide.

## Now begin

Read the workspace (including this application's scope slots above). Determine what state the application is in and what Session 001 (or the current session) should address. Convene perspectives. Deliberate. Decide. Produce. Validate. Record. Close. Report what was done, what state the workspace is now in, and what the next application of this prompt should address.
