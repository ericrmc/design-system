---
session: 077
perspective: architect
family: Anthropic
date: 2026-04-27
---

# architect — blind position

## Frame

The brief commits to two things — a database for structured state, and a multi-agent shape — and asks me to make those concrete. I read the deliberation as a question of *coupling*: what mediates between agents, and what does the substrate refuse on their behalf. Selvedge's seventy-five-session failure was not that the agent was bad; it was that there was no medium between agents (because there was only one agent) and no medium between the agent and its prior state (because the substrate held everything as prose and refused nothing). The successor's defining choice is therefore the substrate's *interface* — the set of operations agents can perform on it, what each operation is forced to declare, and what each operation refuses. The agents fall out of that interface; the orchestrator becomes its enforcer; the human reviewer and the subtractor become operators of distinguished interface paths. I will name two candidate architectures (a minimal and a fuller) and pick the minimal.

## Position

### The substrate as a contract, not just a database

The substrate is SQLite (a single file, transactional, no daemon, recoverable by `cp`) holding a small, opinionated schema. It is not a free-form key-value store. The substrate refuses writes that violate any of: identifier format, foreign-key resolution, lifecycle-state legality, or required-field presence. This is the operationalisation of `constraints.md` §2 ("models treat failure as cheap") — the substrate is the friction.

Tables (named, not exhaustive — devops's perspective will go deeper at the column level):

- `sessions(session_id PK, slug, opened_at, closed_at, engine_version, mode)` — one row per session.
- `decisions(decision_id PK, session_id FK, local_ord, body_md, status)` where `decision_id` is a globally-stable opaque ID and `local_ord` gives the in-session `D-N` rendering. The `body_md` is the prose; the cross-references inside it are checked via a separate `decision_refs(decision_id, target_kind, target_id)` table populated by the validator on commit. The substrate refuses a decision whose declared refs do not resolve.
- `rejected_alternatives(rej_id PK, decision_id FK, body_md, reason_md)` — the brief preserves rejected options as first-class; the schema does too.
- `specifications(spec_id PK, name, version, status, body_md, supersedes_spec_id FK NULL)` — Markdown-bodied, schema-policed lifecycle. `status ∈ {active, superseded, retired}`. Two `active` rows for the same `name` are refused.
- `commitments(commitment_id PK, source_decision_id FK, body_md, status)` where status moves through `open → met | abandoned | superseded`. Selvedge had commitments-as-prose-claims; here a commitment is a row whose state machine the substrate enforces.
- `references(ref_id PK, source_kind, source_id, target_kind, target_id, kind)` — the cross-reference index. Derived on write, not narrated.
- `perspectives(perspective_id PK, session_id FK, role, family, body_md)` — one row per blind position. Synthesis reads rows; it does not re-author them.
- `subtraction_log(action_id PK, session_id FK, target_kind, target_id, action, rationale_md)` — every subtraction is a row. The subtractor cannot remove without writing here.
- `engine_feedback(ef_id PK, raised_in_session FK, body_md, status, disposition_session FK NULL)` — preserves the operator's diagnostic-substrate channel from `methodology.md` §Engine-feedback.

What the substrate refuses, structurally: a decision body containing `[D-7]` whose target row does not exist; a `specifications` write that creates a second `active` row for the same name; a commitment transition that skips a state; a session close whose required artefacts are not registered; a perspective row added to a session whose deliberation is already closed.

What the substrate does *not* hold: the design intent. Specification bodies and decision bodies remain Markdown. Markdown is the right substrate for design intent (`constraints.md` §1 implication). The database's job is the *envelope* — identifiers, references, lifecycle, counters — not the prose inside it.

### The agent set (minimal candidate, A1)

Five agents. The brief enumerates seven; I argue two are roles a single process plays.

1. **Orchestrator** — opens the session, routes work, never holds the workspace. Its context at any moment is: the session's assessment, the agenda item being executed, and the substrate handles needed for that item. It does not read prior provenance directly; it queries.

2. **Worker** — a generic role that executes scoped tasks (read a record and extract X; revise a specification; draft a decision body). The worker is the merger of `reader`, `specifier`, and `assembler` from the brief. Selvedge accumulated three nominal roles around what is really one capability: a small-context process that loads what its tool tells it to load and writes back through the substrate. Splitting them by name produces role-confusion (`constraints.md` §Risks: "the inevitable temptation to keep adding agents"). One worker, parameterised by task, is enough.

3. **Deliberator (n-of)** — the multi-perspective pattern preserved (`constraints.md` §"What the methodology preserved"). Each deliberator instance is a worker bound to a single perspective in a single deliberation. At least one is from a different model family per `methodology.md`. Deliberators write to `perspectives` rows; they do not see one another's rows until after writing their own (substrate enforces this via a `sealed_until` timestamp on the deliberation).

4. **Validator** — runs as a process on the substrate, not as an LLM. It is `tools/validate.sh`'s descendant: a deterministic checker that runs on every write and at session close. The validator is the only agent that is not a model. This is deliberate: the brief's friction-at-write-time prescription (`constraints.md` §"What this means for the engine's design") fails if the friction is itself an LLM that retries when the validation prose looks plausible.

5. **Reviewer** — a separate model instance (different conversation, fresh context) that audits structured constraints, not full session prose. The reviewer queries the substrate for findings the validator could not encode (close-correctness narrative, mechanism adequacy, trajectory discipline per `methodology.md` §When to review at close) and writes a `reviews` row. The reviewer does not fix; the next session does.

What I dropped from the brief's roster:
- **`decider`** — the orchestrator records the decision once deliberation closes; a separate "decider" is precedent-from-Selvedge dressing.
- **`assembler`** — assembly is a query over the substrate. The session artefact (`03-close.md`) is *generated* from the rows, not authored. A view, not an agent.

### The coordination protocol

Agents talk to the substrate. They do not message each other. This is the brief's commitment ("Coordination through the substrate, not through agent-to-agent messaging") taken seriously.

Concretely: every agent invocation receives (a) a *task envelope* (a row in `tasks(task_id, session_id, kind, payload, status)`), (b) read-only handles to the substrate scoped to what the task declares, and (c) a write capability scoped to a single output kind. The agent emits a write; the substrate either accepts or refuses with a structured reason; the orchestrator routes the next task. There is no shared scratch. There is no agent-to-agent channel. If two pieces of work need to coordinate, they coordinate through a substrate row that one writes and the other reads.

A session's record is produced by querying the substrate at close. The "assemble" step is `sqlite3` plus a template; it is not a creative act.

### The human review role

Cadence: every Nth session, where N is set per workspace (default: every fifth self-development session, every tenth external-application session). Cadence is enforced by the substrate — the session refuses to open if a review is overdue.

Scope: the human reads a *generated dossier* (rows-to-Markdown), not the raw provenance. The dossier includes: decisions made since the last review with their rejected alternatives; subtraction actions; engine-feedback rows raised and not yet dispositioned; specifications that became `active` or `superseded`; the validator's warning history. The dossier is small by construction.

Authority: the human can write three kinds of row directly: an `engine_feedback` entry; a `specifications` revision (next session is forced to read it); a `subtraction_log` action with `actor=human`. Crucially, the human can *reframe* — write a row that flags the current agenda as wrongly framed, which the orchestrator must surface in the next assessment.

Why deliberately built: `constraints.md` notes the operator-as-diagnostic-substrate pattern was structural-but-undeclared. Declaring it here means it shows up in the schema, which means a successor reading the substrate sees it as part of the system, not as outside intervention.

### The subtraction role

The subtractor runs on a fixed cadence (per N sessions, like the human reviewer, possibly the same session). It is a model agent with one capability: it can mark `specifications`, `commitments`, `engine_feedback`, and `tasks`-class rows for retirement, and it must write a `subtraction_log` row giving the rule that justified it.

The rules are *declared in the schema*, not invented per-run:

- A specification is eligible for retirement if no `active` decision in the last K sessions cited it.
- A commitment is eligible if it has been `open` for more than M sessions with no progress row.
- An engine-feedback record is eligible if it has been `triaged` for more than P sessions with no disposition.

The subtractor cannot remove on judgment alone; it must point at a rule. This is the structural feature that prevents the role from "being captured by the same accretion logic" (`constraints.md` §Risks). If the subtractor wants to remove something no rule covers, it must propose a rule (raising an engine-feedback row), and the next session decides. This makes the subtractor's job *removing-by-rule* rather than *judgment-as-authority*; an LLM agent can do removing-by-rule consistently.

The human, by contrast, retains *unrestricted* subtraction authority. The subtractor is a rule-following automaton; the human is the exogenous pressure (`constraints.md` §"What this means": "External pressure as a methodology requirement").

### Why the minimal architecture (A1) over a fuller one (A2)

A2 would split the worker into the brief's three roles, add a separate decider, add a separate assembler, and route everything through a message bus. A2 is what Selvedge would have built had it not failed. It is the architecture that re-enacts the accretion the brief diagnoses. A1 picks the smallest set that runs the methodology and forces the substrate to do the integrity work; if A1 proves insufficient, sessions 078+ split a role only when a specific failure justifies it. The default is *fewer agents*, not more.

## Where you would not commit

1. **The five-agent count is a guess, not a derivation.** I cannot prove from the brief that worker-as-three-roles is collapsible without role-confusion of its own. If the worker's task envelope grows per-kind prompting until each kind is effectively a separate prompt, the collapse was wrong. A session-078 prototype where one worker prompt handles read/specify/assemble without per-task branching becoming dominant would confirm A1; the opposite would push toward the brief's roster.

2. **SQLite specifically is a low-confidence pick.** A single-file, transactional, recoverable store is what I want; SQLite is one realisation. Devops should override me on the store. What I am committed to is *one* substrate, transactional, strong-schema, holding only envelope state.

3. **The subtractor's rules-only mechanism may be too rigid.** A rule-bound subtractor cannot remove novel ceremony no existing rule anticipates. If the system accumulates a *new kind* of weight, the subtractor will be silent until the human acts. This may be the right division (human as catch) or it may mean the subtractor adds little — a sequence of human subtractions over things the rule-set could not see would be the negative signal.

4. **Generated session artefacts may lose something.** If `03-close.md` is generated from rows, the close stops being a place where the agent narrates what it learned. That narration may have been load-bearing for the next session's read, or it may have been ceremony. I do not know which.

5. **Cross-family coverage at the worker level is unspecified.** The deliberator is multi-family by design; the worker is not. If worker-class tasks (e.g., drafting a kernel revision) inherit single-family bias, `constraints.md` §1.3 reappears at smaller scale.

## What you think the other perspectives will miss

The adversary will likely attack the database direction at the level of category (substrate change as misdiagnosis) but may miss that the *interface* of the substrate, not its existence, is what carries the load. A non-refusing database is just prose-state in different clothes; the structural commitment is *what writes are refused*, which lives in schema design, not in the choice of store.

The subtractor will likely cut the agent count further — toward "one worker plus the validator." That cut sacrifices the deliberator's multi-perspective pattern, which is the brief's most-validated finding (`constraints.md` §"What the methodology preserved"). The correct cuts are in the fuller architecture A2 implies; cutting below A1 abandons the foundation.

Both Anthropic perspectives may underweight schema *evolution*. The schema will be wrong somewhere within twenty sessions; the friction-at-write-time substrate must itself be evolvable without breaking historical rows. Devops is the likely surface for this.

The cross-family voices may notice that "agents talk to the substrate, not to each other" is a Claude-vocabulary-loaded resolution to LLM coordination — other traditions (message-passing, blackboard, actor) resolve it differently. My architecture is one shape drawn from a substrate-centric framing the brief itself prefers; whether that framing is the only sensible one is exactly the §1.3 pretraining-shape question.
