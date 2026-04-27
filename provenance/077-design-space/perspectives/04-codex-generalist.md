---
session: 077
perspective: cross-family-generalist
family: OpenAI
date: 2026-04-27
---

# cross-family-generalist — blind position

## Frame
I read this less as “Selvedge needs more machinery” and more as “Selvedge discovered that an LLM design methodology must externalise memory, authority, and error before the agent is overloaded.” The brief’s diagnosis is credible, but I would separate two layers: constraints that look general to LLM-driven work, such as prose-default, cheap failure, and context decay (`specifications/constraints.md` §The six properties), and constraints amplified by Selvedge’s early choices, especially Markdown-only state, mostly self-developmental use, and an expanding default read surface (`specifications/engine-manifest.md` §Engine-version history; `provenance/076-engine-restart/03-close.md` §State at close). A different methodology might not have failed at the same point, but it would still need to design against the same class of failure: the agent cannot be the integrity boundary.

## Position

The multi-agent plus database direction is right, but I would make it narrower and more tool-like than the brief’s language may invite. The danger is building a parliament of agents around the same weak center. The successor should instead have a small typed substrate, deterministic gates, and scoped agents that are replaceable workers, not holders of system truth.

The database should be the canonical home for structured state, with Markdown retained for design intent. That follows directly from “models default to prose” and the observed identifier/reference/counter drift (`specifications/constraints.md` §1). My concrete candidate is a local relational store, with SQLite as an implementation hypothesis rather than a methodological commitment. The schema should start with only the integrity surfaces the brief already says failed:

- `sessions(id, slug, mode, engine_version_open, engine_version_close, status, opened_at, closed_at)`
- `artifacts(id, session_id, path, file_class, status, content_hash, supersedes_artifact_id)`
- `spec_versions(id, spec_name, version, status, canonical_path, content_hash, supersedes_id)`
- `decisions(id, session_id, local_id, title, body_md, status)`
- `rejected_alternatives(id, decision_id, alternative_md, reason_md)`
- `references(id, source_kind, source_id, target_kind, target_id, locator, required, validation_status)`
- `read_events(id, session_id, actor, object_kind, object_id, purpose)`
- `engine_feedback(id, origin_session_id, status, body_md, disposition_decision_id)`
- `human_reviews(id, session_id, scope, finding_md, required_action, disposition_decision_id)`

The key is not the table list; it is where refusal happens. A decision cannot close if its references do not resolve. A reference to a superseded spec requires an explicit superseded-reference reason. Session counters are queries, not text. Generated close files are views over rows, with prose sections allowed only where the row type calls for prose. This addresses the brief’s “failure is cheap” property by moving correction from audit-time to write-time (`specifications/constraints.md` §2 and §5).

I would also distinguish “agent” from “role.” Several proposed roles should be tools first and LLM agents only where judgment is needed. A validator should be deterministic. An assembler should be mostly deterministic. A reader should be a constrained query-and-excerpt service that records `read_events`, not a free agent summarising the universe. The LLM roles should be: deliberator perspectives, specifier, decider, reviewer, and subtractor. This keeps the orchestrator from becoming the overloaded single agent under a new name, the failure mode identified in `specifications/constraints.md` §4.

Coordination should happen through the substrate, as the brief suggests (`specifications/constraints.md` §What this means for the engine's design), but that needs a hard rule: no agent-to-agent handoff counts as state until written to the store. The orchestrator may schedule work, but it should not carry unresolved obligations in working memory. If a specifier needs a prior decision, it asks the substrate. If a reviewer finds a gap, it writes a finding row. If the assembler creates `03-close.md`, it renders from stored decisions, produced artifacts, validation results, and open findings.

The subtraction role should be designed as a veto-bearing maintenance role, not a reflective essay. It should run before any net-new engine role, active specification, persistent table, or default read obligation is added. Its write authority should include retiring active engine files, collapsing roles, deleting non-load-bearing schema, and marking proposed additions as rejected. Its decision surface should include a read-budget ledger: for each role, what objects it must load by default and why. The prior failure was not just too many lines; it was that additions were locally reasonable while globally consuming diagnostic slack (`specifications/constraints.md` §6; `applications/075-selvedge-restart/selvedge-problem-statement.md` “The growth has to be incremental…”). The subtractor’s test should be: does this addition reduce future required context or merely explain why more context is necessary?

The human review role should be explicit and asymmetric. The brief says the operator caught limitations the engine did not, and that operator interventions became structural through engine-feedback (`specifications/methodology.md` §Engine-feedback; `specifications/constraints.md` §What the methodology preserved). Therefore human review should not be modeled as just another perspective. It should be allowed to reframe the problem, reject the session’s premise, or require an external application before more self-development. I would store human review as structured findings with dispositions, and require a disposition decision before a blocking finding is considered closed.

Finally, the successor should make external pressure a release gate. The methodology already says self-development is bootstrap, not destination (`specifications/methodology.md` §Self-hosting). I would require every candidate architecture in session 077 to name the smallest external-problem trial that could falsify it. Session 078 should not only design an engine; it should design the first test where the engine must produce value outside itself.

## Where you would not commit

I would not yet commit to the exact database technology. A local relational database is my preferred candidate because the failure modes are referential integrity, counters, lifecycle state, and queryability, but evidence that the engine needs distributed concurrent writes or richer document search would change that.

I would not commit to seven or more named agents. The roles in `provenance/076-engine-restart/03-close.md` §What session 077 should address are useful as a design prompt, but the implementation should collapse any role that does not need independent judgment. Evidence from a prototype showing role confusion or orchestration overhead would push me toward fewer LLM agents and more deterministic tools.

I would not commit to generated Markdown as the only human-facing record until tested. `specifications/methodology.md` §Preservation requires durable provenance and rejected alternatives; generated views can satisfy that only if humans can still read and trust them. If generated records become opaque or lossy, the design should keep authored Markdown for reasoning while indexing its structure in the database.

I would not commit to a fixed cadence for human review or subtraction. The need is clear; the interval is empirical. If every session triggers review, review becomes ceremony. If review is rare, the old accumulation returns. The evidence needed is session throughput and defect recurrence under the successor.

## What you think the other perspectives will miss

I expect Claude-family perspectives may treat “preservation,” “self-hosting,” and “dissent as first-class” as intrinsically virtuous rather than as costly mechanisms that must keep earning their place. The brief itself says much of the late trajectory became ceremony (`specifications/constraints.md` §What the methodology preserved), so the successor should preserve less by default and preserve more only where retrieval, replay, or accountability require it.

I also expect under-specification at the refusal boundary. Many designs will say “use a database” or “coordinate through the substrate” but leave the agent free to narrate around failed writes. The central design question is what the system refuses to accept.

The other likely miss is making the subtraction role another deliberative voice. If it cannot block additions and remove cherished machinery, it will become the exact kind of ceremony it was created to prevent.
