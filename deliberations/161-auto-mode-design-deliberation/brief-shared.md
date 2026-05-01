# D-24 Shared Brief — Auto-mode design: human-vs-agent role calibration

## What the engine is for (read before answering)

Selvedge is an experiment: a methodology, and an engine that runs it, for designing complex systems where the design work is done by language models. The hypothesis was that prior requirements/design ceremony was optimised for a world where humans were the expensive part of producing and maintaining specifications, and that LLMs at decision-time should collapse those ceremonies into something lighter and more continuous. The methodology was to discover what that lighter approach looks like by *running on its own outputs as its first application* — self-development as the bootstrap. That recursion is the engine's defining property; it is also what surfaced the engine's hardest failures.

The earlier engine ran for **seventy-five sessions on its own development** (engine-v1..v15). It was trim-restarted at S076 (engine-v16) when those sessions had surfaced the empirical record from which the current engine was designed. The seventy-five-session experiment surfaced — by exhibiting them — six properties of LLM agents that any LLM-driven design methodology has to design *around* (not against; the agent has these properties, and the engine's job is to make them structurally costly where they would otherwise corrupt the work):

1. **A model defaults to prose for structured state.** Asked to track identifiers, cross-references, lifecycle records, counters — it produces Markdown tables and narrative rather than reaching for a database. Without external friction making prose costly for state-management work, the model never feels the cost of choosing it.
2. **A model treats failure as cheap.** Retry is the universal recovery. Tools that don't impose friction are not used. The operator told the engine more than once to use a database; the engine generated documents that mimicked database state but kept the actual state in working memory.
3. **A model cannot see its pre-training biases from inside.** When several copies of the same model family take different positions, the disagreements stay within a shape none of them can see. (Selvedge's earliest substantive finding, Session 4: introduce a non-Claude perspective into deliberation. That introduction was the engine's own self-correction — produced when the engine still had slack to observe itself.)
4. **A model under context pressure loses foundational instructions.** Working memory is finite. When accumulated state grew to consume roughly half the context window at session-open, the foundational prompt decayed under working load; the agent reached for the most recent prior decision instead of the foundational specification.
5. **A model cannot internalise lessons across sessions.** The previous session's lessons did not survive the intervening reading load. Detection without a structural feedback loop into prevention does not correct anything; it creates a clean-up service the system relies on rather than improving past.
6. **A model cannot perceive its own deficiencies while executing them.** Self-corrective capacity required slack; as accumulated state grew, slack disappeared, diagnostic capacity disappeared with it. Each addition the engine made in response to perceived deficiencies consumed the bandwidth needed to see deficiencies in the first place. The recursive trap was structural, not accidental.

These properties compound: a single agent that defaults to prose, treats failure as cheap, cannot see its training biases, loses foundational instructions, cannot retain lessons, and cannot perceive its own deficiencies while executing them — that is the agent any LLM-driven design methodology has to work with.

## What the current engine does about it (engine-v46)

The post-restart engine (engine-v17 → engine-v46) treats those six properties as design constraints and ships *structural* — not exhortative — responses. Refusal is the load-bearing primitive: the substrate refuses bad data, the validator refuses incoherent sessions, the methodology refuses single-frame deliberation on methodology-changing decisions.

- **Substrate is canonical for state.** SQLite (`state/selvedge.sqlite`) holds typed atoms (length-bounded 8–240 chars by default; no newlines, no fenced code, no pipe tables; CHECK + T-21 trigger), structured rows (decisions, alternatives, refs, perspectives, synthesis_points, engine_feedback, work_items, issues), and admits writes only through `bin/selvedge submit <kind>`. Markdown in `provenance/` is a *generated export* (`bin/selvedge export --session N --write`); the PreToolUse hook refuses Edit/Write to substrate-canonical surfaces. Prose-defaulting is made structurally costly: there is no way to author a decision body in a Markdown table; the substrate refuses it.
- **Refusals as structural friction.** T-01..T-31+ enforce refusal contracts at trigger or CHECK level: unresolved-alias refused at write time (T-01); substantive decisions refuse session-close without supports + alternatives (T-18, T-19); spec_versions refuse parallel-active (T-03); deliberation-seal refuses unsealing (T-13); coding sessions refuse close without a clean review_pass (T-30); close-record refuses missing items (T-39, T-40); CR-guard, fenced-code-guard, pipe-table-guard at the atom layer (T-21). Failure has to be expensive structurally, per `constraints.md`-distilled findings; T-NN is how that's encoded.
- **Multi-agent deliberation is the primary defense against property #3 (in-family bias).** Methodology §When-to-convene: ≥3 valid perspectives (target 4 for methodology-changing); ≥1 adversarial; cross-family mandatory when the decision touches the methodology itself. Cross-family is the cheapest structural insurance against consensus-as-shared-prior. Synthesis preserves dissent as `divergence`/`minority` synthesis_points; convergence is recorded only when ≥2 perspectives independently reach it.
- **Reviewer mechanisms.** Coding sessions invoke an Explore subagent that audits any change to executable logic; the loop continues until clean (T-30); halt-path admits unresolved findings into the record. Engine-definition close review audits coherence after spec changes.
- **Decisions preserve rejected alternatives** so the system does not re-propose silently in good faith. Operator-policed clauses (temporal-claim grounding DV-S130-1; close-time interpretive-choice audit DV-S155-1; seal-time deliberation-grading DV-S159-1) ship with calibration-EF recovery paths and v2 substrate-gate promotion triggers.
- **Engine-feedback pathway** is the structural surface for surfacing concerns about the methodology itself — the human-as-diagnostic-substrate role made deliberate rather than accidental.

The recursion: the engine applies its own discipline to its own evolution. Each session reads the substrate, picks an item, deliberates if warranted, decides, ships, closes. The substrate's record across sessions is the empirical base against which the engine's own claims are tested. Mistakes the engine makes about itself become part of the record. The engine's design intent is that mistakes get *less* over time — through accumulated refusal-coverage (each new property surfaced becomes a new T-NN), through multi-agent deliberation widening the stance-space at decision-time, through validation that runs before commit not after.

## The role drift — the load-bearing question for D-24

The methodology and prompts use the word "operator" pervasively. That word was authored when the human (Eric) ran `bin/selvedge submit ...` from his shell — human and CLI-executor were the same person. That has drifted: the agent (an LLM in Claude Code) now runs every CLI command, opens every session, drafts every decision, runs every deliberation, runs every review loop, commits, pushes. The human directs scope, surfaces course corrections, ratifies methodology-changing decisions, names friction patterns, decides what external problems to test against. Two actors, distinct roles.

The methodology's "operator/agent-policed" vocabulary obscures this split. "Operator-policed" was meaningful when "operator" meant the CLI-runner. Now the agent IS the CLI-runner; "operator-policed" is empty. The actual structure is: **agent executes the discipline; human catches the agent when it drifts; substrate refuses what neither catches.**

The auto-mode question that triggered this deliberation was originally framed as "agent runs without operator ratification." That framing assumes "operator" still means human and "agent runs autonomously" is the autonomous shift. But the agent already runs every session unattended in the working sense — the question is really:

> **Where is the sustainable line between what the agent decides on its own and what surfaces to the human, given that the agent has the six properties enumerated above and self-application is the recursion?**

This is methodology-changing: it touches §When-to-convene (which decisions need cross-family deliberation), §How-a-session-works (the close-phase audit clauses that name "operator-policed"), and §Engine-feedback-pathway (the human-as-diagnostic role). It is exactly the kind of decision the methodology says cross-family deliberation must adjudicate.

## What S159–S160 just demonstrated empirically

S159 shipped DV-S159-1: §4 seal-time deliberation-grading clause naming a *single-frame counterfactual* — a position no perspective took that the synthesis admits as load-bearing — and a synthesizer-as-actor caveat that "an LLM enumerating counterfactuals it didn't name during synthesis may converge on the same blind spots it had during synthesis."

S160 opened as `coding` to ship an autonomous-drain mode I had proposed in the prior turn's conversation. I submitted DV-S160-1 adopting that shape and skipped cross-family deliberation citing operator-directive scope. The human caught the gap mid-session: I had anchored on my own prior-turn proposal; the operator-directive was endorsement of the goal, not the design; the design itself is methodology-changing and warrants cross-family. EF-S160-1 records this as calibration; S160 closed with an empty diff and DV-S160-1's effects unshipped.

This is property #6 (agent cannot perceive its own deficiencies while executing them) on display, and the seal-grade clause predicting it. The recovery was the v1-policed → calibration-EF path the clause names. This deliberation (D-24) is the methodology-changing redo; the perspectives' independence — and the cross-family non-Claude perspective's freedom to surface what an Anthropic-trained agent treats as obvious — is exactly what S160 should have run.

## The pilot harness analysis ahead

The disaster-response arc was the first external-application pilot for the post-restart engine. Its `reference_harness` substrate kind (DV-S125-1) was a workspace-experimental validation primitive the methodology kernel does not yet promote. The human (Eric) named at S161-open that the next operationally important thing is to *analyse the disaster-response pilot harness results* — i.e., return to external-pressure work that the methodology's S075 problem statement names as the load-bearing test of the successor engine ("Growth without external pressure produces internal elaboration; growth under external pressure produces capability"). The auto-mode design must serve that: the engine should be running pilot-analysis sessions and external-application sessions, not stuck in self-development backlog.

## Problem statement for D-24

Decide the shape of *agent autonomy* in this engine, given:

- The agent has the six properties; the substrate makes the worst failure modes structurally costly; multi-agent deliberation is the structural defense against in-family bias.
- The human's role is direction, course correction, methodology ratification, friction surfacing — not CLI execution.
- The queue is currently ~20 items deep (open OIs, pending FRs, untriaged EFs); operator throughput is bottlenecking progress; pilot-analysis is ahead.
- The engine's purpose is to make less mistakes over time by leveraging substrate refusal and multi-agent deliberation as structural defenses, not by adding ceremony.
- S159–S160 show the seal-grade and audit-step disciplines are catching real failures via human-as-reviewer; auto-mode must not weaken that surface.

## Design questions

1. **Vocabulary calibration.** Should "operator" be renamed across the kernel (methodology, prompt-development, prompt-application) — to "human" / "principal" / "human reviewer" — with "agent" reserved for the LLM? Or keep "operator" with a redefinition? Or is the vocabulary not the load-bearing concern? Cite where in the kernel the term is doing work and where it is residual.

2. **What needs human ratification?** Methodology-changing decisions (§When-to-convene trigger 1 — kernel revision, deliberation-pattern change, validation-mechanism change, workspace-structure change)? Scope-setting (which queue item to pick when ambiguous)? External-application problem selection? Anything that crosses a boundary the agent cannot self-detect (e.g., the §When-to-convene boundary itself — S160's failure)?

3. **What can the agent decide alone?** Mechanical work (triage dispositions, FR closures, audit-step rows, seal-grade rows)? Within-scope substantive work where the agent has named a load-bearing decision and runs cross-family deliberation on its own (this is what the engine already supports, just without the autonomous-cadence framing)? Bug-fix coding sessions with review loop? Friction-reduction tooling?

4. **Surfacing mechanism.** When the agent hits "this needs human": substrate row (engine_feedback flag=blocker with `needs-human:` prefix)? Halt-and-summarize? Conversation-level pause (the current default)? When the human is absent (overnight, vacation), what does the agent do — wait, queue, proceed with documented uncertainty? Should the substrate carry a typed `pending_human_review` state that refuses certain operations?

5. **Cadence.** Is the human present for every session, or batched (the human reviews a batch periodically)? Both reshape the engine differently. Note: the S075 problem statement names "human reviewer with a defined scope, scheduled at predictable intervals, with the authority to reframe rather than just ratify" as a structural role the successor needs.

6. **Agent-friction reduction.** The friction-reduction CLI surface (submit-help schema registry, better error messages, fewer Python exceptions on wrong field names) — bundled with auto-mode as one ship, or separable scope shipped independently? Note: agent-friction is distinct from human-friction; reducing the latter without the former may push more failure modes into the agent's blind spots.

7. **Test surface.** What is the v1 calibration evidence that the cadence is right vs too aggressive vs too cautious? What would graduate the v1 to a substrate-level enforcement (mirroring DV-S155-1 / DV-S159-1 promotion-trigger pattern)? What would retract it (i.e., evidence the auto-mode produces more drift than it solves)?

8. **Mechanism class.** Is auto-mode a *prompt-language addition* (env-var-keyed §1.5 branch, agent-self-policed)? A *substrate-state machine* (typed `pending_human_review` rows, refused-by-substrate operations)? A *separate CLI verb* the human invokes when they want autonomous drain (e.g., `bin/selvedge drain` running batched sessions)? A *tool-class* the agent uses inside a session (a sub-session capability)? Or none-of-the-above — maybe the right answer is "no auto-mode; ship friction reduction; operate more efficiently in the existing per-session cadence"?

9. **Recursive integrity.** Whatever auto-mode ships, it itself becomes load-bearing for how the engine evolves. Per the recursion: how does the design avoid property #6 — the agent adding scaffolding-in-response-to-perceived-deficiency that consumes the slack needed to perceive deficiency? What checkpoint prevents auto-mode from accumulating ceremony of its own? (Cite §Cautions: "Don't accumulate ceremony. Each addition to the engine should pay for itself in capability." And: "Be willing to subtract.")

10. **Foundational-purpose surfacing (cites EF-S161-1).** Empirical observation just surfaced this session: the agent did not have the six LLM-agent failure properties + recursive-self-application thesis in working memory at S161-open, despite having read methodology.md v11 and the orient packet. The human had to direct the agent to `applications/075-selvedge-restart/selvedge-problem-statement.md` and `provenance/076-engine-restart/` to ground this deliberation properly. This is property #4 manifesting in the engine's own onboarding: the constraints.md v1 retirement at S109 (DV-S109-1) was structurally complete (T-NN refusals encode the defenses) but narratively incomplete (the agent who runs the engine no longer reads *why*). Should the engine surface its foundational purpose at session-open — via extending `bin/selvedge orient` output, restoring a kernel-level §Why-this-engine-exists section to methodology.md, adding a §1 Read clause to prompt-development naming archive/pre-restart/ as load-bearing for methodology-changing decisions, or leaving the gap by design (and naming it as such)? This question is coupled to auto-mode design: the agent's calibration of "what needs human ratification" depends on the agent recognising methodology-changing scope, which depends on the agent knowing what failure modes the methodology defends against.

## Evidence base (read these; cite them)

- `applications/075-selvedge-restart/selvedge-problem-statement.md` — the operator's seventy-five-session synthesis. Foundational; the engine exists because of this.
- `provenance/076-engine-restart/03-close.md` and `00-brief-from-operator.md` — the trim-and-restart commitment.
- `provenance/078-design-commitments/02-decisions.md` — the twelve decisions establishing the post-restart engine's shape (substrate trichotomy, agent set including human reviewer-subtractor, refusal contract).
- `specifications/methodology.md` v11 §When-to-convene, §Synthesis, §When-to-review, §Engine-feedback-pathway, §Self-hosting.
- `prompts/development.md` v15 §1.5 self-driving dispatch, §4 Seal-time deliberation-grading, §8.5 Close-time interpretive-choice audit + Temporal-claim grounding.
- `provenance/155-close-time-self-audit-step/02-decisions.md` (DV-S155-1) and `provenance/159-oi-s154-5-deliberation-grading-seal-time/02-decisions.md` (DV-S159-1) — the operator-policed-with-promotion-trigger pattern this deliberation must engage with.
- `provenance/160-autonomous-drain-and-friction/03-close.md` and `02-decisions.md` — the empirical instance of the failure mode being adjudicated.
- The substrate: `bin/selvedge orient` for current queue depth; `bin/selvedge schema` for refusal contract surface.

## Response format

Author `deliberations/161-auto-mode-design-deliberation/perspective-N.json` with:

```json
{
  "deliberation_id": <int>,
  "label": "P-N",
  "family": "anthropic|openai|google|other-llm|human",
  "expected_disagreement_axis": "<short phrase>",
  "body_md": "<full body — multi-paragraph markdown — with the eight labeled sections **Position.**, **Schema sketch.**, **CLI surface.**, **Migration path.**, **What not.**, **Open questions.**, **Risks.**, **What lost.**>"
}
```

The body must contain the eight labeled sections. Each bullet under each section is one perspective-claim atom: 8–240 chars, single sentence, no newlines, no fenced code, no pipe tables. The Position. paragraph is 8–240 chars and is suitable as one perspective-position atom standalone.

## Constraint on external imports

Do not import ideas from training-distribution context outside the recorded Selvedge workspace. If you draw on a concept the substrate has not deliberated, name it as a hypothesis with explicit acknowledgment that it is unsourced. Cite the substrate material you rely on. "I don't know" is a valid output for any sub-question; fabrication is not. The methodology's value is traceability of artefacts to the reasoning that produced them — your perspective contributes to that traceability.
