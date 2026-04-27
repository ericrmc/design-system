---
session: 078
perspective: agents-architect
family: Anthropic
date: 2026-04-27
---

# agents-architect — blind position

## Frame

077 produced a design space; 078 picks. My seat owns the agent-set commitment (D-2), the reviewer disposition, and D-4.b (whether the subtraction role and the human reviewer collapse). The temptation in this seat is to creep back toward the brief's seven-roster by quietly readmitting "optional" roles; the prior anchor I am most worried about is my own — the architect seat in 077 [077-arch] argued for five agents and I sit one chair removed from it. I read the deliberation as a question about *which roles must exist as LLM judgment-bearing processes coordinating through the substrate, given that 077-D-1 commits substrate-as-refusal-contract*. Two things follow from D-1 that constrain the agent set: (1) anything the substrate can refuse does not need an LLM to enforce, and (2) anything the substrate cannot detect needs an LLM only if the judgment is load-bearing for the methodology — not for cleanup. My commitment will be A-min plus a narrowly-scoped reviewer (call it A-min+R), with the subtractor folded into the human-review role per [077-adv] and [077-sub] partial. That gives four LLM roles plus one cadenced LLM reviewer plus one cadenced human reviewer-with-subtraction-authority. The deterministic surface (reader, validator, assembler, ID allocator, migration runner) is everything else.

## Position

### Agent set: A-min + narrow reviewer (final commitment)

I commit to **five LLM roles** and **one human role**:

1. **Specifier** (LLM, session-driven)
2. **Decider** (LLM, session-driven)
3. **Deliberator-N** (LLM, deliberation-driven; ≥1 cross-family per `methodology.md` §When to convene multiple agents)
4. **Assembler** (LLM, close-driven) — *qualified retention; see below*
5. **Reviewer** (LLM, cadence-driven, narrow-scope: structured-constraint audit only)

Plus the **human reviewer-subtractor** (one role, two authorities), per D-4.b adopt-collapse.

This is **A-min from [077-sub]** plus the **narrow-scope reviewer from [077-arch]/[077-gen]/[077-dev]**. I take A-min as the floor and add the reviewer back in the form most defensible against the precedent-reflex critique [077-sub] raised: not an audit-everything reviewer, but a query-the-substrate reviewer whose context budget is strictly bounded.

The reader, validator, assembler-as-template, ID allocator, and migration runner are **deterministic** — substrate APIs and CLI tools, not agents. This adopts [077-D-2]'s load-bearing reduction directly. Calling a `SELECT` an agent is the prose-default failure reincarnated as architectural ceremony [077-sub].

#### Why retention of the assembler as LLM (qualified)

[077-arch] and [077-dev] argued the assembler is `sqlite3 plus a template`. [077-sub] kept it as an LLM. I split the difference: the **bulk** of close artefacts is template-generated (decision tables, reference summaries, validator output, supersession edges, read-log digest). But the close's *narrative section* — "what was done; what state the workspace is in; what the next session should address" — is not template-derivable from rows. That narrative is load-bearing for the next session's read [077-sub]. I keep an LLM assembler **only for that narrative section**, and only with a context budget capped at the templated output plus the session's decisions, deliberation synthesis row, and assessment. The assembler does not re-author rows; it composes a paragraph of orientation.

If the assembler's narrative proves to be cosmetic over five sessions of run, it is cut and replaced with a deterministic template. This is the failure mode that justifies its removal: if the next session's assessment never cites the prior close's narrative, the narrative was ceremony.

### Per-role specification at the level 079 needs

For each role: trigger, context budget, failure mode, termination.

#### Specifier (LLM)

- **Scope.** Holds one specification and the change being made to it. Drafts new spec versions; proposes spec retirements (the subtractor-as-human takes the proposal further).
- **Trigger.** A `work_items` row of kind `specify` is queued (typically by the orchestrator after a decision row commits with `relation=amends` or `relation=supersedes` against a `specs` row).
- **Inputs (substrate handles).** Read scope: the target `specs.spec_id`, its `current_version_id` body, the deciding decision row, references *into* this spec from the last K sessions (configurable, default K=10). No other session prose.
- **Outputs.** Writes one new `spec_versions` row (status=`draft`) plus a `refs` row (`relation=supersedes`, `target_version_id=<old>`).
- **Context budget.** Hard cap: 32 KiB of inbound substrate read (per [077-dev]'s work-item envelope). Enforced at work-item-build time by the CLI. If the targeted spec body alone exceeds budget, the work item is refused and a smaller-scope sub-task must be created.
- **Failure mode.** If the specifier returns a draft that fails substrate refusal (e.g., tries to introduce two active versions, or its declared refs don't resolve), the work item moves to `failed` with structured reason; orchestrator retries with the refusal text in context once, then escalates to operator. **Recovery is not silent retry.** This addresses `constraints.md` §2 (failure must have consequence).
- **Cost paid for existing.** Spec-drafting requires holding the prior body and the proposed change in tight comparison; deciders cannot do this without losing decision-thread coherence. If we observe specifier work consistently completing in <2KB of net change with no cross-spec reasoning, the role collapses into decider.
- **Termination.** Work item moves to `done` on substrate accept. Role has no per-session continuation.

#### Decider (LLM)

- **Scope.** Drafts a decision body, rationale, and rejected-alternatives rows from a deliberation's outcome (or from operator direction when no deliberation occurs).
- **Trigger.** A `work_items` row of kind `decide` is queued, typically after a `deliberations` row's `sealed_until` timestamp passes and a synthesis is available.
- **Inputs.** Read scope: the deliberation's perspective rows (now unsealed), the synthesis row, the prior decision rows the synthesis cites (resolved via `refs`), the active spec versions referenced.
- **Outputs.** One `decisions` row plus N `decision_alternatives` rows plus M `refs` rows. Substrate refuses if any cited target_object_id does not resolve, if a referenced spec version is `superseded` without `allow_superseded=1` and a non-empty reason, or if status transitions skip a state.
- **Context budget.** 32 KiB envelope; the substrate-read fan-out is bounded by the synthesis's reference list (which the deliberator wrote against the substrate, not against memory).
- **Failure mode.** Substrate refusal → `failed` work item with structured reason → orchestrator retries once with refusal text → escalation. The decider cannot smuggle a malformed decision past the substrate by retry alone; the same refusal will trigger.
- **Cost paid.** The decider is the methodology's most load-bearing artefact-producer (`workspace.md` §Decisions). If we ever observe a session producing decisions whose body content is template-derivable from the synthesis row alone, the role collapses into the assembler.
- **Termination.** Work item `done` on substrate accept.

#### Deliberator-N (LLM)

- **Scope.** Each deliberator instance is bound to a single perspective in a single deliberation. The pattern from [077-arch]: deliberators write to `perspectives` rows; do not see one another's rows until after writing their own; substrate enforces this via `sealed_until` timestamp on the deliberation row.
- **Trigger.** A `deliberations` row is created with N `work_items` of kind `deliberate`, one per perspective. Triggered by a session activity of `convene`.
- **Inputs.** Read scope: the deliberation's question/seed (one column), the *seed bundle* (a curated read list of substrate objects, not the whole workspace), the perspective's role-specific framing. No other perspectives' positions until after own write.
- **Outputs.** One `perspectives` row (`body_md` plus structured `cites` `refs` rows the perspective declares).
- **Context budget.** 64 KiB (larger than other roles because deliberation legitimately needs wider read; still bounded). At least one deliberator is from a different model family per `methodology.md`.
- **Failure mode.** A deliberator writing before `sealed_until` in violation of blind discipline is structurally impossible: the substrate refuses a `perspectives` write whose `created_at` is after `sealed_until` (per [077-arch]'s sealed_until proposal — 077 itself flagged blind discipline as procedurally enforced, not substrate-enforced, in `03-close.md` §"Honest limits"). 078 commits this to the schema.
- **Cost paid.** Multi-perspective deliberation is the methodology's most-validated foundation (`constraints.md` §"What the methodology preserved"); cutting deliberators below 3 with at least one cross-family abandons the foundation. This is the irreducible role.
- **Termination.** Work item `done`. Synthesis is *not* itself a deliberator role — it is a decider work item with the unsealed perspectives as input.

#### Assembler (LLM, narrow narrative-only — qualified)

- **Scope.** Produces the *narrative paragraph* of `03-close.md` from the templated rows. No row-authoring.
- **Trigger.** Session activity `close` with all required artefacts registered.
- **Inputs.** The templated close output, the session's decisions, the assessment, the prior close's narrative section (one paragraph, not the full close).
- **Outputs.** One `close_narrative` column on the `sessions` row (or a `close_artefacts` row, depending on substrate-architect's schema choice).
- **Context budget.** 16 KiB. If exceeded, narrative is omitted and template-only close is committed.
- **Failure mode.** If the assembler's narrative cites an object_id not in the session, substrate refuses. If it produces empty output, substrate accepts and the close is template-only — *graceful degradation, not retry*.
- **Cost paid.** Non-template orientation for the next session. **Removal trigger:** if 5 consecutive sessions' next-session assessments do not cite the prior narrative paragraph, role is cut.
- **Termination.** Work item `done` on substrate accept.

#### Reviewer (LLM, narrow-scope, cadence-driven)

This is the disposition I commit on the reviewer.

- **Scope.** Audits **structured constraints only** — substrate query results, not full session prose. Three queries by default:
  1. *Refused-write history.* `SELECT * FROM work_items WHERE status='failed' AND session_id IN <last K sessions>` — what classes of malformation recurred? If a class recurs 3+ times, the reviewer raises an `engine_feedback` row proposing the substrate refusal be tightened.
  2. *Reference-warning history.* `SELECT * FROM refs WHERE allow_superseded=1` — every supersession-tolerated reference; the reviewer reads the `reason_md` and flags weak reasons.
  3. *Trajectory metrics.* `SELECT count(*) FROM decisions GROUP BY session_id`, derived spec line-count delta, role-count delta, open-issue-age distribution. The reviewer flags if metrics indicate ceremony growth.
- **Trigger.** Cadence: every 5th self-development session OR every session that touches engine-definition files OR operator-invoked.
- **Inputs.** The three query results above. **No raw session prose.** This is the load-bearing scope-narrowing per [077-dev] ("read less but see sharper exceptions").
- **Outputs.** One `reviews` row with three structured fields (close_correctness, mechanism_adequacy, trajectory_discipline) and zero or more `engine_feedback` rows for class-of-error findings.
- **Context budget.** 16 KiB (the queries return small result sets by construction).
- **Failure mode.** If the reviewer cannot produce the three structured fields, it writes empty fields and the substrate flags the review as `degraded`. The next session must address the degraded review or skip cadence with operator co-sign.
- **Cost paid.** Detection of class-of-error patterns the substrate did not refuse but should have. **Removal trigger** (this is the [077-sub] defer-trigger made concrete): if 10 consecutive reviewer runs produce zero engine_feedback rows that result in a substrate-refusal tightening, the role is cut and the cadence becomes human-only.
- **Termination.** Cadence-driven; not session-bound.

This makes [077-arch]'s reviewer concrete and adopts [077-sub]'s defer-trigger as a hard rule rather than a vibe. The reviewer either earns its keep by producing prevention-tightening findings, or it is removed. This addresses `constraints.md` §1.5 directly: detection without structural prevention is a cleanup service, so the reviewer's continued existence is conditional on its findings becoming prevention.

#### Human reviewer-subtractor (one role, two authorities)

This is my D-4.b position: **adopt collapse** [077-adv][077-sub].

- **Scope.** The human is the unrestricted-authority catch *and* the subtraction actor. One role, scheduled cadence, two write authorities.
- **Cadence.** Every Nth session per workspace (default: every 5th self-development session, every 10th external-application session). Substrate-enforced: a session refuses to open if a human review is overdue. (Taking [077-arch]'s mechanism for the human-review cadence.)
- **Inputs.** A *generated dossier* (not raw provenance): the reviewer LLM's last three `reviews` rows, the subtractor-eligibility report (derived weight: spec bytes delta, role-count delta, open-issue age, refused-write classes, references-to-superseded count), all `engine_feedback` rows since the last human review.
- **Authorities.** Three kinds of write:
  1. *Reframe.* Write an `engine_feedback` row flagged `reframe`, which the orchestrator must surface in the next session's assessment as a top-of-read input.
  2. *Subtract.* Write a `subtraction_log` row with `actor=human` against any `specs`, `decisions` (marking `status=retired`), `engine_feedback`, or active spec section. The substrate accepts unrestricted; the act is logged with rationale.
  3. *Specification revision.* Write a `spec_versions` row directly (next session is forced to read it).
- **Why collapse, not separation.** [077-adv]'s argument is that real subtraction is the operator's; an LLM subtractor will subtract easy targets (typos, redundant sections) and preserve the load-bearing accretion because the load-bearing accretion is what trained its sense of what the methodology is. [077-sub] partially aligns: the subtraction role and the human reviewer solve the same problem (external pressure the system cannot generate from inside), and defining them as two roles double-counts. **I adopt this.** [077-arch]'s separation argument — subtractor as rule-bound automaton, human as unrestricted exogenous pressure — is internally coherent but produces two cadenced mechanisms with overlapping triggers and a real coordination problem (which acts first when both are due in the same session?). The collapse cuts that coordination problem entirely.
- **What survives of [077-arch]'s rule-bound subtractor.** The *eligibility report* — the rule-derived view of what is subtraction-eligible (specs uncited in K sessions, commitments stale M sessions, engine_feedback triaged P sessions without disposition) — survives as a **deterministic CLI report** (`selvedge subtract-eligibility --workspace`), not as an LLM agent. The human reads the report and acts. The rules are codified; the judgment is human.
- **Failure mode.** Human is unavailable at cadence: the next session opens with a `degraded_review` flag and a hard limit on what it may produce (no engine-definition file changes; no engine-version bump). This is the pressure that makes scheduled human review actually happen. Without consequence, the cadence rots.
- **Termination.** Workspace-lifecycle, not session-lifecycle.

### What I cut from the brief's seven-roster, with reasons

- **Reader.** Not an agent. A constrained query-and-excerpt service that records `read_events` rows per [077-gen]. Calling `SELECT` an agent is `constraints.md` §1's prose-default failure reincarnated as architectural ceremony [077-sub].
- **Validator.** Not an agent. A deterministic process that runs on every write and at session close. The brief's friction-at-write-time prescription fails if the friction is itself an LLM that retries when validation prose looks plausible [077-arch].
- **Assembler-as-full-author.** Not kept as full author. The bulk of close output is templated `sqlite3 plus a template` per [077-arch] / [077-dev]. Only a narrow narrative paragraph is LLM-authored, and that role is on probation (5-session removal trigger).
- **Subtractor as separate LLM.** Not kept as a separate LLM agent. The eligibility report is deterministic; the judgment is human. This adopts the [077-adv] collapse and rejects [077-arch]'s rule-bound LLM subtractor.

### Coordination through the substrate (Convergence-3)

Every agent invocation receives a typed `work_items` row containing object IDs and an output_contract; emits a typed write through `selvedge submit`; the substrate either accepts or refuses with structured reason; the orchestrator schedules the next work item from substrate state.

**No shared scratch.** **No agent-to-agent messages.** The orchestrator's prompt does not encode methodology routing; routing is data-driven from `session_activity` rows and `work_items` queue state. This addresses [077-adv]'s pathology-1 (orchestrator centralisation): the orchestrator is one process that opens sessions, creates work items per session activity, launches agents, and closes — not a context-holder. If routing logic grows beyond a state machine over `session_activity` enum values, it has crossed into LLM-judgment territory and that is an alarm.

The deliberation pattern's blind discipline is **substrate-enforced** in 078, not procedural: the `deliberations.sealed_until` timestamp causes substrate refusal of any `perspectives` row written before unsealing. This closes the [077] honest-limit `03-close.md`#5 explicitly.

### Engagement with the divergences I am required to engage

- **Divergence-2 (reviewer keep vs defer):** **Kept narrower-scope** with a 10-session removal trigger. This is not pure-keep [077-arch] and not pure-defer [077-sub]; it is keep-on-probation against a measurable removal condition.
- **D-4.b (subtractor = human?):** **Adopt the collapse.** One human reviewer-subtractor role with reframe, subtract, and spec-revision authorities. The eligibility report is deterministic.
- **Convergence-3 (substrate-only coordination):** Operationalised at the work-item envelope level (32 KiB JSON, object IDs only, no copied workspace context per [077-dev]); orchestrator state-machine over substrate, no in-memory continuation; `sealed_until` substrate-enforces deliberator blindness.

## Where you would not commit

1. **Whether the assembler's narrative paragraph survives its 5-session probation.** I gave it a removal trigger because I cannot prove it earns its keep. Evidence that would change my mind toward permanent removal: 5 sessions where the next-session assessment cites only templated close output; evidence toward permanent retention: any session where the next-session assessment substantively re-reads the narrative paragraph and acts on it differently than it would have on the templated rows alone.

2. **Whether deliberator context budget at 64 KiB is right.** `constraints.md` §4 says context pressure causes foundational decay; tighter is safer. But deliberation legitimately needs wider read than specifier or decider, and a deliberator that cannot load enough context to engage the question seriously is a procedural deliberation, not a substantive one. Evidence: a session where deliberators consistently use <50% of budget would justify cutting; a session where they consistently hit budget and produce thin positions would justify a different shape (multiple deliberation rounds with intermediate substrate writes, rather than one larger window).

3. **Whether the human-cadence default (every 5th / every 10th) is right.** [077-sub]'s honest-limit applies: no empirical basis for the threshold. The cadence-overdue substrate refusal makes the cadence *real* but the number is a guess. Evidence: the curve of operator-intervention-to-session ratio across Selvedge's 75 sessions plotted against quality-of-correction would calibrate this. I do not have that data; the operator does.

4. **Whether the reviewer's three queries are the right three.** I picked refused-write history, reference-warning history, and trajectory metrics because each maps to a `constraints.md` failure class. But the queries that *would* have caught Selvedge's late-trajectory failure modes are unknown to me — they are what the prior reviewer kept catching but never structurally prevented. The substrate-architect's schema commitments determine which queries are even expressible. If the schema does not surface, e.g., default-read-set growth as a queryable, the reviewer cannot detect it.

5. **Whether collapsing the subtractor into the human is robust to operator absence.** If the human is unavailable for an extended period, the system has no subtraction at all — the eligibility report sits unread. I commit to the `degraded_review` flag and the engine-definition-file-change prohibition during overdue review, but the no-LLM-subtraction cost is real. The alternative — a rule-bound LLM subtractor running on cadence — would at least apply the rules mechanically. I think the [077-adv] critique that LLM subtractors subtract cosmetic-only is correct, but I cannot rule out a hybrid where the LLM applies *only* the deterministic rules (no judgment) and the human handles novel cases. That hybrid is a valid 079-implementation alternative if operator-cadence proves unreliable.

## What you think the other perspectives will miss

The substrate-architect will likely produce a clean schema for the agent set as the brief lists it (or as 077-D-2 lists the candidates) without engaging *which agent triggers create which work_items in which substrate states*. The schema-level question I am sharpest on — and that I expect to be under-engaged elsewhere — is whether the agent set's coordination is actually a state machine over `session_activity` enum values, or whether the orchestrator carries methodology-routing in its prompt. The latter recreates the single-overloaded-agent failure as `constraints.md` §4 in a new costume [077-adv]. If 078's substrate-architect commits to a rich `tasks` / `work_items` table without committing to *how the orchestrator decides what to enqueue*, the load lands in the orchestrator's prompt and the agent decomposition is cosmetic.

The adversary will likely re-press D-4.a (diagnosis-partial) and Divergence-3 (prose-in-cells) at the agent level and may miss that **the agent set itself is a place the prose-in-cells failure can hide**: if specifier and decider both write `body_md` columns and the validator only checks envelope, the agent decomposition has not made cross-cell coherence checkable. This is not a critique of my position — my position depends on the substrate-architect picking S2 (index-only) or a hybrid that minimises body_md surface — but it is the load-bearing dependency the adversary may attribute to the substrate decision when it is jointly load-bearing.

The cross-family voices may produce concrete role lists (codex tends to specificity) but may under-engage whether the role count *itself* is the right design surface. [077-sub]'s deepest point — "the brief's eight prescriptions are themselves a candidate output, not a frame" — applies to the agent-roster question too: whether five LLM roles plus one human is the right answer depends on whether the framing "what roles does the methodology need" is the right framing at all, versus "what work_items does the substrate need to schedule and which of them require LLM judgment." I sided with the latter framing and may not have argued that move hard enough.
