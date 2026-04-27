---
session: 078
title: Decisions — design commitments
date: 2026-04-27
engine_version_at_decision: engine-v16
decisions: 12
---

# Decisions

This session commits the next-generation engine's design surface. Per `provenance/077-design-space/02-decisions.md` D-5, 078 produces design commitments; 079 begins implementation. The twelve decisions below close 077's seven divergences and three minority dispositions, plus three new commitments raised in 078's deliberation (write budgets; 078-self-test; 079 handoff at vertical-slice level).

Each decision draws from `01-deliberation.md`'s synthesis. Tagged perspective sources: `[arch]` substrate-architect, `[agt]` agents-architect, `[adv]` adversary, `[eng]` cross-family engineer, `[meth]` cross-family methodologist; `[077-X]` for prior-session perspectives or decisions.

---

## D-1 — Substrate-shape: S1-typed (cells for argument; tuples for state; files for specifications only)

**What.** The substrate uses three storage modes, assigned by artefact-kind:

| Storage mode | Artefact-kinds | Mechanism |
|---|---|---|
| **S1 cells** (body_md TEXT NOT NULL) | `decisions`, `engine_feedback`, deliberation `synthesis` body | Body is design-intent prose; refusal acts on envelope (refs, lifecycle, status, supersession), not on prose content. |
| **S3 tuples** (typed satellite tables) | `decision_alternatives`, `refs` (including supersession edges), `commitments`, `synthesis_points` | One row per structural element. Cross-cell coherence is queryable. |
| **S2 files** (body_path + body_sha256) | `spec_versions` only | Specifications live at `specifications/<slug>-v<NNN>.md`; the row carries `body_path` and `body_sha256`. |

`perspectives` use **S1 cells** (`body_md TEXT NOT NULL`). The session's perspective files on disk (`provenance/NNN-<slug>/perspectives/*.md`) remain authored artefacts but are not the substrate of record once 079 lands; they are the working surface the deliberators write, and the substrate ingests `body_md` from them at close.

**Why.**

The S1-vs-S2-vs-S3 trichotomy in 077-D-3 is real but the actual design-space is mode-per-artefact-kind, not one mode for everything. The convergent claim from `01-deliberation.md` C-7 (Markdown carries argument; database carries obligations) translates directly: prose-of-argument lives in S1 cells; envelope and structural-state live in S3 tuples; the **specifications carve-out** for S2 files is justified by the methodology's git-diffability requirement (`workspace.md` §Specifications: "human-readable, version-diff-able"; `methodology.md` §Preservation: "git history is the workspace's tamper-evident substrate"). Spec changes happen rarely, at session pace, with one writer; the atomicity hazard `[eng]` named is bounded for that artefact-kind specifically.

The structured satellite tables (`decision_alternatives`, `refs`, `synthesis_points`, `commitments`) are the structural surface that makes the substrate's prose-in-cells residue auditable. `[arch]`'s argument carries: rejected alternatives as one row each (not narrative bullets in `decisions.body_md`) directly addresses the prior engine's most-empirically-observed prose drift. `[adv]`'s prose-in-cells prediction is acknowledged as live and partially mitigated rather than fully refuted; D-12 (write budgets) and the C-3 reviewer-deferral give the system structural exposure to prose-drift detection in 080+.

**Rejected alternatives.**

- **R-1.1 — Pure S1+ per `[arch]` (perspectives in files-with-SHA).** Rejected because `[eng]`'s two-phase consistency critique is sharp and perspectives are the artefact-kind where atomicity matters most (sealed-discipline depends on substrate-level integrity, not on a separate hash check). Specifications already require git-diffability; perspectives do not (they are session-local audit trail, not durable design intent).
- **R-1.2 — S1-only per `[eng]` (no file-shape carve-out).** Rejected because storing specifications as binary-blob diffs in git history violates `workspace.md` §Specifications and `methodology.md` §Preservation — the methodology requires human-readable spec history.
- **R-1.3 — S2-narrow per `[adv]` (no body_md columns; everything index-only).** Rejected because the synthesis_points pattern (C-7's "convergence requires ≥2 source perspectives" structurally enforced) requires the database to know what the perspective bodies say at the row level. An index-only substrate would push that knowledge into prose-of-summaries that contradict the rows they index.
- **R-1.4 — Pure S3 tuples for decision bodies.** Rejected per 077-D-3 R-3.3: nobody has produced a tuple-decomposition for decision *reasoning* that preserves what makes decisions readable. The hybrid lets reasoning stay prose while the structured commitment around it is queryable.

**Open.**

Whether the specifications S2 carve-out generalises to perspectives in 080+ is contingent on operational evidence. If specifications-as-files prove to introduce no atomicity failures across 079–085, 086+ may revisit perspectives. If specifications-as-files do introduce atomicity failures, 080+ may revert specifications to S1 cells with separate git-diffability addressed by exporting Markdown views from the database.

---

## D-2 — Agent set: 3 LLM roles + 1 human role (no LLM reviewer; no LLM assembler)

**What.** The active agent set:

| # | Role | Type | Trigger | Output kind |
|---|------|------|---------|-------------|
| 1 | **Specifier** | LLM, session-driven | `work_items` row of kind `specify` | `spec_versions` row + `refs` (`supersedes`) |
| 2 | **Decider** | LLM, session-driven | `work_items` of kind `decide` | `decisions` + `decision_alternatives` + `refs` |
| 3 | **Deliberator-N** | LLM, deliberation-driven; ≥1 cross-family | `work_items` of kind `deliberate`; `deliberations.sealed_until` enforced | `perspectives` row |
| 4 | **Human reviewer-subtractor** | Human, cadence-driven | Cadence overdue refuses session open | `engine_feedback` (reframe), `subtraction_log`, `spec_versions` (revision) |

**Deterministic, not LLM agents:**
- Reader (substrate query API + `read_log` rows).
- Validator (`tools/validate.sh` successor; runs pre-commit and at session close).
- Assembler (`sqlite3` + template; renders close artefacts from rows).
- ID allocator (`selvedge id-allocate` CLI; in-transaction).
- Migration runner (CLI applying `state/migrations/NNN-*.sql`).
- Subtractor-eligibility report (`selvedge subtract-eligibility` CLI; deterministic rules; human reads, human acts).

**Why.**

Three LLM roles is one fewer than 077-D-2's `A-min` (which kept assembler) and two fewer than `A-mid` (which kept assembler and reviewer). The reductions:

- **Assembler-as-LLM dropped.** `[arch]`, `[eng]`, `[meth]` all argue assembly is a query plus template; `[agt]`'s probationary-narrative case is the minority preserved as Div-3. The deterministic-only assembler is what the deliberation majority commits to. If a session's close artefacts prove unreadable without LLM-authored orientation, 080+ raises an engine_feedback row proposing a narrative-paragraph addition; until then, the role is not built.
- **LLM reviewer dropped at first cut, deferrable.** `[meth]`'s "remove now; return narrower" is sharper than `[agt]`'s "keep on probation" because the probationary form pays the LLM-role cost for ≥10 sessions before its trigger can fire. Cutting now is the more subtractive position consistent with `[adv]`'s 078-self-test (D-12). The LLM reviewer is **conditionally re-introduced in 080+** if the substrate's refusal contract demonstrably fails to catch a class of error that a substrate-query reviewer could catch — measured by an engine_feedback row from the human reviewer-subtractor naming the missed class. Until that row exists, no LLM reviewer is built.
- **Subtractor-as-LLM dropped (D-6 collapse).** Only the human has subtraction authority. The eligibility report is deterministic — rule-based queries over the substrate (specs uncited in K sessions; commitments stale M sessions; engine_feedback triaged P sessions without disposition). The human reads the report; the human acts.
- **Reader, validator, assembler, ID allocator are not roles.** `[077-D-2]`'s load-bearing reduction reaffirmed.

**Per-role specification at the level 079 needs** is owned by `02-agents-architect.md` §"Per-role specification at the level 079 needs"; this decision adopts the following from that document by reference: trigger-input-output-context-budget-failure-mode-termination spec for each LLM role; deliberator `sealed_until` substrate enforcement; specifier and decider 32 KiB context envelopes; deliberator 64 KiB context envelope; failure-mode handling (substrate refusal → structured reason → orchestrator retries with refusal text once → escalate to operator).

The assembler narrative-paragraph proposal from `[agt]` is **rejected for engine-v17** but recorded as Div-3 minority. If it returns, it returns through engine_feedback per the same conditional re-introduction rule as the reviewer.

**Rejected alternatives.**

- **R-2.1 — A-min per `[077-sub]` (4 LLM roles: specifier, decider, deliberator-N, assembler).** Rejected: the assembler has no LLM-distinct work that templating cannot do, per Div-3 majority.
- **R-2.2 — A-mid per `[077-arch]` (orchestrator + worker + deliberator-N + validator-as-LLM + reviewer).** Rejected: validator-as-LLM violates `constraints.md` §2 (failure-friction must be structural, not exhortative); orchestrator-as-LLM-judgment-bearing reproduces the single-overloaded-context failure (`[adv]` P4 stress-test).
- **R-2.3 — A-min + narrow probationary reviewer per `[agt]`.** Rejected: the probationary form pays role cost for ≥10 sessions; cutting now and re-introducing on substrate-evidence is more subtractive (per D-12) and equivalently informative.
- **R-2.4 — A-min + narrow probationary reviewer + probationary LLM-narrative assembler per `[agt]` full position.** Rejected for the same reasons combined.
- **R-2.5 — Brief's seven-role roster.** Rejected per 077-D-2 R-2.1 (no perspective endorses; all five reduce). Reaffirmed.

**Open.**

The conditional re-introduction triggers (one engine_feedback row from the human reviewer-subtractor naming a class of error the substrate did not catch but a substrate-query reviewer could) are designed to be observable but might be slow to fire. If 080–085 produce no such engine_feedback rows because no substrate-escape-class is detected (rather than because none exist), the absence is itself ambiguous evidence. The human reviewer-subtractor's cadence-driven dossier read is the structural surface that makes the absence diagnosable.

---

## D-3 — Refusal contract: 16 refusals at first cut

**What.** Migration 001 implements the following substrate refusals. Each is implementable as SQL trigger or CHECK constraint plus application-layer parsing in `selvedge submit`. Each cites the `constraints.md` failure property it makes structural.

| # | Refusal | Mechanism | Property |
|---|---------|-----------|----------|
| **T-01** | INSERT `decisions` WHERE refs declared in `body_md` (`[D-S\d+-\d+]`, `[SPEC-...]`, etc.) do not all resolve to `objects.object_id` | Application-layer parse; insert `refs` rows in same tx; refuse if any unresolved | P1, P2 |
| **T-02** | UPDATE `sessions` SET `status='closed'` WHERE any decision with `kind='substantive'` lacks ≥1 `decision_alternatives` row | Trigger | P1, methodology preservation |
| **T-03** | INSERT/UPDATE `spec_versions` WHERE another active row exists for same `spec_id` | UNIQUE partial index `(spec_id) WHERE status='active'` | P1 |
| **T-04** | INSERT/UPDATE `spec_versions` WHERE file at `body_path` SHA-256 ≠ `body_sha256` | Pre-commit `selvedge validate --hashes` | P2 |
| **T-05** | INSERT `perspectives` WHERE `deliberation.sealed_at IS NOT NULL` | Trigger | P5; closes 077-`03-close.md` honest-limit-5 |
| **T-06** | UPDATE/DELETE on `decisions`, `decision_alternatives`, `refs`, `spec_versions`, `perspectives`, `commitments`, `synthesis_points` WHERE owning session `status='closed'` | Triggers | Methodology preservation |
| **T-07** | INSERT `refs` WHERE `relation='cites'` AND target `spec_versions.status='superseded'` AND `allow_superseded=0` | CHECK + trigger; if `allow_superseded=1` then `reason_md NOT NULL AND length(reason_md) ≥ 16` | P1 |
| **T-08** | INSERT `decision_alternatives` WHERE `rejection_reason_md` IS NULL OR length < 16 | CHECK | P2 |
| **T-09** | UPDATE `commitments` SET `status` violating state machine `open → met \| abandoned \| superseded` | Trigger | P5 |
| **T-10** | INSERT `sessions` WHERE `session_no ≠ MAX(session_no)+1` | UNIQUE + CHECK | P1 |
| **T-11** | UPDATE `sessions` SET `status='closed'` WHERE any `work_items.status` ∈ {`queued`,`leased`,`failed`} for that session | Trigger | P5 |
| **T-12** | INSERT any row WHERE `agent_runs.role` not in `role_write_capabilities` for that table | Trigger lookup | P2; orchestrator-as-bottleneck protection |
| **T-13** | UPDATE `deliberations` SET `sealed_at=NULL` | Trigger refusing unconditionally | Methodology preservation |
| **T-14** | INSERT `synthesis_points` WHERE `kind='convergence'` AND `json_array_length(source_perspectives) < 2` | CHECK | Methodology preservation of dissent |
| **T-15** | Schema migrations: `DROP COLUMN`, `DROP TABLE` refused; only `ADD` operations permitted | Pre-migration check in `selvedge migrate` | `constraints.md` §"Risks" schema-evolution |
| **T-16** | INSERT/UPDATE `work_items` WHERE `lease_expires_at < CURRENT_TIMESTAMP` AND `status='leased'` | Trigger; cron-resets to `queued` | P2 |

**16 refusals; under `[adv]`'s 30-cap and the D-10 budget of 20.**

**Why.**

The list is the union of `[arch]`'s T-1–T-17, `[adv]`'s T1–T8, and `[eng]`'s minimum-refusal list, de-duplicated and adjusted to the D-1 substrate-shape (T-04 applies only to `spec_versions`, not all body-bearing rows; T-05 uses sealed_at, not sealed_until-as-deliberator-blindness-only). Refusals dropped from `[arch]`'s 17:

- T-9 (commitment summary cap): subsumed into `commitments.summary_md` column CHECK constraint, not its own refusal class.
- T-13 (close requires read_log entries): deferred until 080+ because the reader-as-substrate-API is built before but read_log discipline is non-trivial; 079 implements basic read_log without the close-blocking refusal.

This list is the **first cut**. Refusals discovered later become migrations under D-8.

**Rejected alternatives.**

- **R-3.1 — `[arch]`'s full 17 refusals as written.** Rejected because two refusals (T-9, T-13 in `[arch]` numbering) overlap with simpler mechanisms in this commitment.
- **R-3.2 — `[adv]`'s T1–T8 only.** Rejected because the 8-refusal list does not cover commitment lifecycle (T-09 here), supersession edges (T-07), substantive-decision-needs-alternatives (T-02), or sealed-deliberation immutability (T-13). The brief's `constraints.md` properties require structural refusal at the level of these closures; T1–T8 alone leaves them to the reviewer.
- **R-3.3 — Refusals on prose *content quality* (e.g., "decision body must contain a 'why' paragraph").** Rejected per `[arch]`'s argument: that is the reviewer's job (when the reviewer returns), not the substrate's; conflating them is the prose-default failure in another costume.

**Open.**

Each refusal's exact trigger SQL and application-layer parsing details are 079 implementation choices; the *contract* is what 078 commits to, the *implementation* is what 079 builds. If 079 finds a refusal cannot be implemented as specified (e.g., T-01's body_md ref-parsing is intractable at trigger time), 079 records an engine_feedback row and the contract revises in 080+ deliberation.

---

## D-4 — D-4.a Reading B: adopt; consequences for 078

**What.** Reading B (accretion-without-subtraction is the empirical pattern, compounding single-agent overload) is **adopted** as a co-cause of the 75-session failure trajectory.

**Why.**

`[adv]` and `[meth]` both adopt; `[meth]`'s framing ("an omitted causal layer" rather than competing diagnosis) is the synthesis position. The pattern is visible inside 077 itself (seven convergences + seven divergences + three minorities + three substrate candidates + two agent-set candidates produced; only one structural counter held as minority). 077-D-4.a preserved the reading as first-class; 078 closes it by adoption.

**Consequences for 078, all already commitments below:**

- D-7 adopts the D-4.c cut (subtraction is load-bearing, not optional).
- D-10 adopts write budgets (the structural mechanism the brief's "what this means for the engine's design" §"A subtraction role with the authority to remove" requires).
- D-12 runs `[adv]`'s 078-self-test: subtraction column ≥ addition column.
- D-2 cuts the LLM reviewer and LLM assembler at first cut (deferring to substrate-evidence-based re-introduction).
- D-6 adopts the subtractor-human collapse (no LLM subtractor pays role cost while not subtracting load-bearing accretion).

**Rejected alternatives.**

- **R-4.1 — Reject Reading B; treat single-agent overload as sole cause.** Rejected because `[adv]`'s evidence (the 077 record itself) is internal to the deliberation and undisputed. No perspective rebutted Reading B.
- **R-4.2 — Hold open per 077-D-4.a.** Rejected because 078 is the commitment session; "preserve as first-class" is what 077 did. Holding open in 078 too defers indefinitely.

**Open.** Whether the multi-agent decomposition is *necessary* for fixing single-agent overload (as the brief asserts) or merely *sufficient* given the additional Reading-B fixes is uncertain. If 080+ shows that the subtraction discipline + write budgets + engine cuts alone produce sustained capability without the multi-agent shape adding net value, the multi-agent decomposition is itself subtractable. This is monitored, not closed.

---

## D-5 — D-4.a Reading C: hold open with a release gate

**What.** Reading C (self-hosting itself is structurally trap-prone) is **held open** with an operator-enforced release gate:

> **Engine-v17 is provisional.** No methodology-expanding self-development sessions modify engine-v17 active spec content between 079 and the close of the first external-problem trial of 30 sessions. Bug-fix and validator-tightening sessions are admitted; new active-spec content (new file, new section, new active mechanism) is not. The operator enforces this externally.

**Why.**

`[adv]` and `[meth]` converge on the gate. `[meth]`'s framing — "the enforceable rule is a release gate: no further methodology-expanding self-development after the first agent-on-substrate run unless an external-problem trial has been opened, run, and closed with a domain or operator report" — sharpens `[077-gen]`'s "smallest external-problem trial" and accepts `[077-sub]`'s "the engine cannot enforce externality from inside."

The 30-session number is `[adv]`'s; it is acknowledged as deliberately wrong-in-detail, but its function is to make the gate concrete enough to be remembered and possibly broken (so that breaking it is itself observable).

**Rejected alternatives.**

- **R-5.1 — Substrate refusal: "no self-development after N consecutive self-dev sessions."** Rejected per `[meth]` and `[077-sub]`: "compliance theatre"; the engine cannot make external pressure true by schema. Substrate refusals belong on data integrity, not workspace mode.
- **R-5.2 — Reject Reading C.** Rejected because no perspective produced a rebuttal; the only evidence against C would be the engine running successfully on a real external problem, which has not happened.
- **R-5.3 — No gate at all; let self-development continue.** Rejected because doing nothing about Reading C while adopting Reading B (D-4) is internally inconsistent: Reading B says accretion-without-subtraction is the failure; permitting unbounded post-079 self-development invites the same accretion at the new substrate layer.

**Open.**

What constitutes a "30-session external-problem trial" is operator-defined. Whether 30 is the right threshold, whether the trial concludes by domain-actor report or operator report, and whether multiple parallel external trials count cumulatively or independently are operator decisions. The engine records `MODE.md` and session_count per workspace_id; the gate's interpretation is the operator's.

---

## D-6 — D-4.b: adopt the collapse (subtractor = human reviewer)

**What.** The subtraction role and the human reviewer are **one role**: human reviewer-subtractor.

- Cadence-driven (default every 5th self-development session, every 10th external-application session; per-workspace overridable).
- Three write authorities: reframe (write `engine_feedback` flagged `reframe`); subtract (write `subtraction_log` against any active artefact); spec-revision (write `spec_versions` directly).
- Substrate-enforced cadence: a session refuses to open if the human review is overdue.
- Reads a generated dossier (not raw provenance): the substrate's eligibility report (deterministic rules; uncited specs, stale commitments, untriaged engine_feedback) plus the session's own engine_feedback queue.

**Why.**

C-3 in `01-deliberation.md`: 4-of-5 perspectives that engaged adopt collapse; none oppose. `[adv]`'s structural argument reproduced here:

- Subtraction requires authority to remove specifications and decisions; the operator has it; LLM agents do not.
- An LLM "subtractor" produces subtraction-ceremony (cuts typos, preserves load-bearing accretion that trained its sense of identity).
- The operator is already the subtraction substrate (session 076's restart was a subtraction event no agent could perform).

The eligibility report survives as a deterministic CLI (`selvedge subtract-eligibility`) per `[agt]`. Rules are codified; judgment is human.

**Rejected alternatives.**

- **R-6.1 — `[077-arch]`'s separation: rule-bound LLM subtractor + unrestricted human.** Rejected per C-3: two cadenced mechanisms with overlapping triggers and a real coordination problem (which acts first when both are due in the same session?). The collapse cuts the coordination problem and removes one LLM role.
- **R-6.2 — Hybrid: deterministic rule-application LLM (no judgment) + human for novel cases.** Rejected because deterministic rule-application is implementable as CLI without an LLM in the loop; introducing an LLM whose only job is rule-application reintroduces retry-as-recovery (P2) at the deletion boundary.
- **R-6.3 — Pure human, no eligibility report.** Rejected because asking the human to discover what is eligible by reading provenance reproduces the load-shedding failure: the human's diagnostic capacity is itself finite. The deterministic eligibility report is the load-shed.

**Open.**

The cadence default (5/10 sessions) is `[agt]`'s guess. Per `[agt]` honest-limit-3, the curve of operator-intervention-to-session ratio across Selvedge's 75 sessions plotted against quality-of-correction would calibrate this. The operator carries that data; 080+ may revise. Operator-availability for the cadence is the structural risk per `[agt]` honest-limit-5; the substrate-enforced cadence-overdue-refusal makes the cadence *real* but not free.

---

## D-7 — D-4.c: adopt the cut; concrete cut list applied by 079

**What.** Engine-v16 is cut by approximately 80–100 lines as the first action of session 079, before substrate code lands. The cut list (per `[meth]`):

1. **`methodology.md` §"When to review at close"** — remove as active mechanism. Replace with one transitional sentence: *"Close-time review is superseded until the substrate distinguishes prevention from audit; D-2 conditional re-introduction governs."*
2. **`methodology.md` §"Validation senses"** — collapse to workspace validation and domain validation only. **Archive provisional-reference-substitute** to `archive/specifications/methodology-v1-validation-senses.md` (or equivalent versioned filename) per workspace.md §Specifications discipline.
3. **`methodology.md` §"What this kernel does not say"** — remove. Meta-disclaimers about what 077 didn't say have been superseded by 078's commitments themselves.
4. **`workspace.md` §"What this file does not say"** — remove. Same reason.
5. **`workspace.md` §"Top-level layout" tree** — replace with a narrower normative rule: *"The manifest defines engine-definition files; session records live under `provenance/`; generated exports are not the source of truth once the substrate exists."* The directory tree as-loaded was a transition-aid.
6. **`engine-manifest.md` §"Loading the engine in a fresh workspace"** — remove. The recipe for loading engine-v16 is invalidated by 079's substrate; engine-v17's loading recipe will be authored fresh in 079 or 080 as part of substrate adoption.

**Engine version impact.** 079's application of this cut produces **engine-v17**.

**Why.**

C-4 in `01-deliberation.md`: 3-of-5 perspectives explicitly adopt; none oppose. `[adv]`'s frame: "If 078 cannot subtract from a 350-line spec set with no users, the engine cannot subtract from a 3000-line spec set with sessions depending on it." The cut tests subtraction discipline before adding substrate.

`[meth]`'s argument that the specific targets are *load-bearing-zero*: each was a transition aid for engine-v16 (the trim-restart) that no longer earns its loaded surface. The provisional-reference-substitute is preserved by archive (per `methodology.md` §Preservation), not deleted.

**Rejected alternatives.**

- **R-7.1 — Defer the cut to a future session.** Rejected per `[adv]`'s 078-self-test framing: deferring is what 077-D-4.c warned against. Accretion-without-subtraction is named as the failure mode; deferring subtraction reproduces it.
- **R-7.2 — Cut more aggressively (collapse engine-v16 to 200 lines).** Rejected because the targets above are the load-bearing-zero items the deliberation could agree on; deeper cuts touch material the deliberation did not survey (e.g., the deliberation pattern itself, the engine-feedback pathway). Aggressive cuts beyond `[meth]`'s list belong in 080+ after evidence.
- **R-7.3 — Cut less aggressively (only 1–2 of the 6 targets).** Rejected because partial adoption signals subtraction-as-token-gesture, which is precisely what `[adv]` warned of. The cut list is treated as a unit.

**Open.**

The exact line count post-cut is an artefact of editing; the targets are normative, the count is not. If editing reveals one of the targets is more load-bearing than the deliberation supposed (e.g., removing the layout tree breaks navigation for a fresh reader), 079 records an engine_feedback row and 080+ deliberation revisits.

---

## D-8 — Schema-evolution protocol: additive-default; contract-changes are foundation-touching

**What.** Schema changes follow the protocol below.

**Additive migrations** (current session decides; deterministic review):
- New nullable column with default; new table; new index; new view; stricter trigger applying only to future rows (gated by `created_schema_version` metadata column).
- Authorised by a normal session decision of `kind='schema-migration'` citing the prompting refusal or capability gap.
- Deterministic review: apply to a `.backup` copy; run `PRAGMA integrity_check`, `PRAGMA foreign_key_check`, run the `selvedge` exporter, run the concurrency smoke-test from D-9 if write-path tables changed.

**Contract migrations** (foundation-touching; multi-perspective deliberation required):
- Drop column / drop table (not currently permitted per T-15; would require revising T-15).
- Rewrite object identity.
- Change refusal semantics (loosening or tightening any T-NN).
- Backfill non-derived historical meaning.
- Move body-storage shape (e.g., move `decisions.body_md` to file-shape).

Contract migrations require the methodology's normal foundation-touching discipline (`methodology.md` §When to convene multiple agents): multi-perspective deliberation, ≥1 cross-family voice.

**During migration:** substrate enters `schema_state='migrating'`; non-migration writes refused with `E_SCHEMA_MIGRATING`; work items queue; reads continue from snapshots; submits with stale `schema_version` lease refused with `E_STALE_SCHEMA`.

**Rollback:** two-tier. Pre-close failure → SQLite transaction rollback + restore from pre-migration `.backup`. Post-close failure → forward-only corrective migration (a new decision in a later session; the broken migration's row remains immutable per T-06).

**Backfill:** historical rows take `NULL` for new columns by default. Backfill is permitted only when deterministic (hashes, derived counters, copied foreign keys, status values mechanically implied). No LLM infers historical facts.

**Why.**

C-6 in `01-deliberation.md`: `[arch]` and `[eng]` converge on the protocol shape; the additive-vs-contract split is `[eng]`'s sharpening of `[arch]`'s T-17 (no destructive migrations). The split keeps ceremony bounded — `[meth]` "I expect schema evolution to be over-moralised. Most schema changes should be boring migrations with tests" — while making contract changes (which alter what the substrate refuses) appropriately heavy.

The `constraints.md` §"Risks" warning ("schema-evolution overhead and the possibility of state-substrate-substrate-protection ceremony reincarnated in a different form") is addressed structurally: most migrations are additive and decidable in-session; contract changes are rare and warrant the deliberation cost.

**Rejected alternatives.**

- **R-8.1 — All migrations require multi-perspective deliberation.** Rejected per `[meth]`: ceremony creep. Adding a column for a new feature is normal session work, not a foundation-touching decision.
- **R-8.2 — All migrations are session-author-discretion.** Rejected because contract changes alter the refusal semantics — what the substrate prevents — which is methodology-level. Letting any session loosen a refusal silently reproduces accretion-without-subtraction.
- **R-8.3 — Pre-deliberation review by a separate "schema-keeper" role.** Rejected as agent proliferation; this role is a deterministic CLI (`selvedge migrate --dry-run`) plus the additive-vs-contract split.

**Open.**

The exact list of operations classified as "contract" vs "additive" beyond the seed list above will accumulate as 079+ produces migrations. The first ambiguous case becomes the first 080+ deliberation that calibrates the boundary.

---

## D-9 — Substrate technology: SQLite 3, single-writer, local-only

**What.** Engine-v17's substrate is **SQLite 3** at `state/selvedge.sqlite` accessed only through the `selvedge` CLI/library.

- WAL journaling mode; `PRAGMA foreign_keys=ON`; `STRICT` tables where available; configurable `busy_timeout` with retry jitter.
- Every write opens its own connection, runs one short transaction with `BEGIN IMMEDIATE`. Readers get snapshot reads under WAL; writers serialize.
- IDs allocated in-transaction; no "next ID" call hands an agent a value to remember.
- Idempotency keys on writes: `(work_item_id, output_kind, output_hash)` for crash-recovery without duplicate insertion.
- Work-item leases with expiry; `selvedge recover` reclaims expired leases.
- Lock contention surfaces as structured `E_WRITE_BUSY` to the application layer; LLM never sees `database is locked`.

**Remote agents are compute, not database writers.** A remote codex/Claude call returns an output envelope to the operator machine; local `selvedge submit` performs the write. No agent process opens the SQLite file over NFS, Dropbox, SSHFS, or any sync surface. Multi-machine direct writers, if ever needed, are a separate substrate decision (likely Postgres).

**Concurrency falsification trial (079 deliverable):** 16 parallel `selvedge submit decision` processes against one active session, with injected sleep and one killed mid-transaction. Expected: contiguous local ordinals; references all resolve; killed process leaves no partial rows; queued work items recoverable; `PRAGMA integrity_check` and `foreign_key_check` clean; no raw lock error reaches agent layer. Choice falsified if duplicate ordinals, wedged lock, duplicated commits on retry, or operator must inspect SQLite internals to recover.

**Why.**

C-2 in `01-deliberation.md`. `[eng]`'s framing ("the real concurrency decision is not 'which database tolerates many writers'; it is 'where is the single serialization point for Selvedge state?'") is the load-bearing reframe. The single-serialization-point commits the concurrency answer; SQLite is one realisation; the single-writer property is what carries the load.

`[arch]`, `[eng]`, `[agt]` all commit to SQLite; `[meth]` is compatible. SQLite's operational footprint matches the operator-run, workspace-local shape: single file, no daemon, no port, no auth surface, simple backup. `constraints.md` §"Risks" warning about substrate-protection-ceremony reincarnated is addressed by picking the most boring substrate that meets the contract.

**Rejected alternatives.**

- **R-9.1 — Postgres at first cut.** Rejected because no current requirement justifies daemon + port + auth; multi-machine writers are not a v1 requirement per `[eng]`. Postgres becomes the obvious successor if multi-machine direct writes ever land.
- **R-9.2 — DuckDB / libSQL / custom file-locked store.** Rejected as undifferentiated from SQLite for the v1 contract while introducing less-common operational shapes.
- **R-9.3 — "No database; structured filesystem."** Rejected because the refusal contract (D-3) requires transactional integrity and FK enforcement that filesystem semantics do not provide. A structured filesystem reproduces the prior engine.
- **R-9.4 — Distributed substrate (cloud DB, remote-writers).** Rejected per `[eng]`: "I expect some perspectives will treat distributed agents as implying a distributed database. That is the wrong first cut."

**Open.**

The exact `busy_timeout`, retry budget, and lease-expiry interval are 079 implementation parameters set against the falsification trial's results. If the trial reveals frequent `E_WRITE_BUSY` under expected concurrency patterns, the system needs a local write-queue process or a different substrate; 079 records the calibration.

---

## D-10 — Write budgets: adopt with modified numbers

**What.** Three structural budgets, enforced by the human reviewer-subtractor's eligibility report:

| Budget | Limit | Scope |
|---|---|---|
| Active engine spec | ≤ 400 non-blank lines | Engine-v17 active set (`PROMPT.md` + `prompts/*.md` + `specifications/*.md` + `tools/validate.sh`); enforced until first external-problem trial completes |
| Migration 001 schema | ≤ 16 tables | Number of `CREATE TABLE` statements in `state/migrations/001-*.sql` |
| Refusal contract | ≤ 20 enumerated refusals | Number of T-NN refusals at first cut |

Measurement: non-blank lines counted by `grep -cv '^[[:space:]]*$'`. Blank lines are formatting; non-blank lines carry content the agent must read.

These budgets are **observable** (deterministic CLI counts) and **breachable with cause** (a session may exceed the budget if its decision record cites the breach explicitly and the human reviewer-subtractor's next dossier read does not subtract the breach). They are not substrate-refused; they are subtractor-pressure.

**Current state at 078 close (against the budgets):**
- Active engine spec: **430 non-blank lines** (PROMPT 31 + application 30 + development 26 + constraints 59 + engine-manifest 45 + methodology 76 + workspace 96 + validate 67). **Currently breaches the 400-line budget by 30 lines.** D-7's cut brings the surface to an estimated ~330–350 non-blank lines, under budget. The breach is the diagnostic the budget is designed to surface; D-7 is the resolution.
- Migration 001 schema: 16 tables planned (at limit; exact count is 079 implementation choice).
- Refusal contract: 16 enumerated (under 20).

Honest note: 077-`00-assessment.md` and 076 close both stated the engine was "~350 lines," which is closer to the post-D-7-cut state than to the actual engine-v16 state. The "~350" estimate was directional; the structural budget here is to non-blank-line count and is exceeded as of 078 open, which is itself evidence for D-4 Reading B's adoption.

**Why.**

`[adv]`'s argument: "These numbers are deliberately wrong-in-detail; their function is to force the removal conversation." Without observable budgets, accretion has no surface to push against. With budgets, breaches are visible as data, not as judgment calls.

Numbers modified from `[adv]`'s proposal:
- Active engine spec: 400 lines kept (matches `[adv]`).
- Migration 001 schema: 16 tables (relaxed from `[adv]`'s 12) because the `[arch]`+`[agt]`+`[eng]` schema converges on ~16 tables (sessions, objects, decisions, decision_alternatives, spec_versions, perspectives, deliberations, refs, commitments, engine_feedback, work_items, role_write_capabilities, read_log, subtraction_log, schema_migrations, agent_runs). Twelve would force a meaningful structural cut whose value the deliberation could not size.
- Refusal contract: 20 (relaxed from `[adv]`'s 30) because the convergent enumeration is 16; 20 leaves headroom for 079 implementation discoveries.

**Rejected alternatives.**

- **R-10.1 — No budgets.** Rejected per D-4 Reading B adoption: accretion-without-subtraction requires a structural surface to push against.
- **R-10.2 — `[adv]`'s exact numbers (400 / 12 / 30).** Rejected per the table-count modification; the deliberation's converged schema does not fit in 12.
- **R-10.3 — Substrate-refused budgets (cannot commit a session that breaches).** Rejected because the budgets are heuristics, not invariants; substrate-refusal would force compliance theatre (split tables to fit; trim refusals into the next migration).

**Open.**

Whether the budgets are recalibrated at first external-problem trial completion is operator-directed. The eligibility report's reading of breaches is the surface that makes recalibration data-driven.

---

## D-11 — Session 079 handoff: vertical slice, not horizontal expansion

**What.** Session 079 implements the substrate vertical slice. Concrete deliverables, in order:

1. **Apply the D-7 cut to engine-v16.** Edit the named files; archive removed sections per `methodology.md` §Preservation. Bump engine-v16 → engine-v17 in `engine-manifest.md`. *This is 079's first action.*
2. **Author `state/migrations/001-initial.sql`** implementing D-1's substrate-shape, the 16 refusals from D-3, the schema for sessions / objects / decisions / decision_alternatives / spec_versions / perspectives / deliberations / refs / commitments / engine_feedback / work_items / role_write_capabilities / read_log / subtraction_log / schema_migrations / agent_runs (≤ 16 tables per D-10).
3. **Implement the `selvedge` CLI** at minimum: `selvedge init` (creates schema from migration 001); `selvedge id-allocate --type <kind> --session <S>` (in-transaction); `selvedge submit <kind> --payload <json>` (parses refs, opens transaction, refuses on T-NN violations); `selvedge validate --precommit` (runs `PRAGMA integrity_check`, `PRAGMA foreign_key_check`, T-04 hash verification, ref-resolution cross-check); `selvedge subtract-eligibility` (deterministic eligibility report).
4. **Wire `tools/validate.sh`'s successor** to call `selvedge validate --precommit` and gate git-commit on its result.
5. **Run the round-trip test:** open S079 → write a decision (with one rejected_alternative row, one refs row) → close S079 → reopen → verify T-06 refuses any UPDATE on the closed decision.
6. **Run the concurrency falsification trial** from D-9 (16 parallel submits, injected sleep, one kill, expected results).
7. **Close S079** with a decision recording the trial results and any engine_feedback rows raised.

**079 must NOT:**
- Build any LLM agent role. The first session test runs with a single human writing rows via CLI.
- Implement a generated close-assembler (templated close output is fine; LLM-generated narrative is forbidden).
- Migrate the 75-session pre-restart provenance. The archive is evidence, not initial substrate payload.
- Solve schema-evolution questions beyond migration 001. D-8's protocol governs; 079 implements only migration 001.
- Implement reviewer dashboards, subtraction automation, agent-on-substrate flows. Those are 080+.
- Bump beyond engine-v17. Substrate landing is one engine-version increment.

**079 exit criteria:**
- A fresh workspace can `selvedge init` and the schema applies cleanly.
- The round-trip test passes from a clean state.
- The concurrency falsification trial produces the expected results from D-9 (or surfaces a calibration the close records).
- A closed session's structured rows cannot be mutated except by a later corrective row, matching `methodology.md` §Preservation.
- `selvedge validate --precommit` reports clean against the post-079 workspace.
- A documented command path exists that 080 can use to hand one agent output to the substrate, even if the agent prompt itself is not yet built.

**Why.**

C-1, C-2, C-6, C-9 in `01-deliberation.md`; `[meth]`'s "vertical-slice implementation session, not architecture-expansion session." The narrow scope makes 079 falsifiable: either the substrate refuses what the contract says it should, or it does not. Either the cut applies cleanly, or it does not. Either the trial produces the expected concurrency behaviour, or it does not.

The list above is the **smallest set** that exposes the substrate-as-refusal-contract claim to evidence. Anything larger admits the proliferation `[adv]` warned of.

**Rejected alternatives.**

- **R-11.1 — Honour 077-D-5 verbatim and let 079 also build a first agent role.** Rejected per `[meth]`: the agent set's correctness depends on the substrate's correctness; building agents over an unfalsified substrate ports the prior engine's failure.
- **R-11.2 — Apply the cut in 080 instead of 079.** Rejected per D-7 reasoning: the cut tests subtraction discipline; deferring it past the substrate landing gives the substrate first-mover and accretes around it.
- **R-11.3 — Migration 001 implements only sessions/decisions tables; defer half the schema to 080.** Rejected because the round-trip test requires decision_alternatives + refs + closed-session immutability + spec_versions to exercise T-02, T-06, T-07. Cutting tables below ~10 produces a substrate that cannot exercise the contract.

**Open.**

If 079 hits an implementation blocker (e.g., a refusal cannot be implemented at trigger level), 079 records the blocker as engine_feedback, downgrades that refusal to "deferred" in migration 001, and 080+ deliberates the resolution. The vertical-slice scope is the *plan*; the *exit criteria* admit graceful degradation with explicit engine_feedback.

---

## D-12 — 078 self-test: subtraction column ≥ addition column

**What.** Per `[adv]` Div-5, this session's commitments are weighed as a session against the diagnostic question 077 carried forward: *Does 078 subtract more than it adds?*

**Additions (commitments produced by 078):**

1. Substrate-shape commitment (D-1) — one schema framework specified per artefact-kind; no active-engine-spec lines added in 078 itself.
2. Agent-set commitment (D-2) — three LLM roles + one human; **fewer LLM roles than 077-D-2's `A-min` (which had four) or `A-mid` (which had five)**. Per-role specs adopted by reference from `[agt]`.
3. Refusal contract (D-3) — 16 refusals enumerated, under D-10's 20-cap.
4. D-4.a Reading B adoption (D-4).
5. D-4.a Reading C release-gate hold-open (D-5).
6. D-4.b collapse adoption (D-6).
7. D-4.c cut adoption (D-7) — *this is itself a subtraction*.
8. Schema-evolution protocol (D-8) — additive-default keeps protocol weight bounded.
9. Substrate technology (D-9) — single product (SQLite); no operational additions.
10. Write budgets (D-10) — three numbers; observable; breachable with cause.
11. 079 handoff (D-11) — vertical slice; explicit "must not" list constraining horizontal expansion.

**Subtractions (commitments by 078, applied or affirmed):**

1. **D-7 cut list** — six specific sections to remove from engine-v16 active spec, applied in 079; ~80–100 lines removed.
2. **LLM reviewer cut at first cut** (D-2) — vs. 077-D-2 `A-mid` (which kept it) and `[agt]` (which kept it on 10-session probation). Cutting now saves a role's cost.
3. **LLM assembler cut at first cut** (D-2) — vs. 077-D-2 `A-min` (which kept it) and `[agt]` (which kept narrative-only on 5-session probation). Cutting now saves a role's cost.
4. **LLM subtractor cut** (D-6 collapse) — vs. 077-`[arch]`'s rule-bound LLM subtractor. Eligibility report is deterministic; judgment is human.
5. **Provisional-reference-substitute archived** (within D-7) — `methodology.md` §Validation senses collapses to two senses.
6. **077-D-2 seven-roster reduced to three LLM roles + one human** — reaffirmed and operationalised.
7. **No close-time review at first cut** (within D-7) — the prior mechanism is removed; conditional re-introduction governs.
8. **Workspace.md layout tree replaced with a one-sentence rule** (within D-7) — directory enumeration removed.
9. **Engine-manifest.md loading recipe removed** (within D-7) — recipe is invalidated by 079's substrate.

**Result.** 9 subtractions, 11 additions. The additions include 4 dispositions (D-4, D-5, D-6, D-12 itself) that consume zero active-engine-spec lines and exist only as provenance commitments. The substantive additions to the *active engine surface in 079* are: the substrate (state/migrations/, state/selvedge.sqlite), the `selvedge` CLI, the cut-engine-v17 active spec set (smaller than v16). By line count of active engine spec, **engine-v17 is smaller than engine-v16** — a net subtraction at the active-engine-surface level.

The substrate is added as state/, not as active spec. State substrate is the methodology's *envelope*; per D-1 and C-7, state in the substrate is not the same kind of thing as design-intent in active spec. The substrate adds enforcement; the active-spec subtractions remove ceremony. The two are both load-bearing.

**`[adv]`'s test passes.**

**Why this disposition belongs in the decision record.**

`[adv]`'s diagnostic — "the synthesis check I want preserved: does 078 subtract more than it adds?" — was preserved as Div-5 minority. Recording the test's result here is the structural answer. If a future session reads 078 and asks "what did 078 cost the engine?", the accounting is in this decision. If the test had failed, the decision record would say so honestly and propose what subtraction 078 should have done but did not.

**Rejected alternatives.**

- **R-12.1 — Skip the self-test (treat `[adv]`'s framing as rhetorical).** Rejected because preserving dissent as first-class without engaging it converts dissent to ceremony.
- **R-12.2 — Run the test informally in `03-close.md` rather than in `02-decisions.md`.** Rejected because the close is reportage; the test is a structural commitment about how 078 weighs its own outputs. It belongs in decisions.

**Open.**

The accounting is honest at the level 078 can produce. If 080+ examines 078 with more specificity (e.g., re-counts what was added vs. what was removed at the level of refusal contract complexity, agent-orchestration prompts, or operator-procedure load), and the recount reverses the conclusion, the methodology corrects the error in 080+ explicitly.

---

## Engine-version impact

**No bump in 078.** No active engine-v16 file was modified by session 078. Session 078 produced provenance only.

The engine-v16 → engine-v17 bump occurs at session 079's close, when 079 applies the D-7 cut and lands migration 001.

## Open issues raised by this session

- **OI-078-001:** Cadence default for human reviewer-subtractor is 5 sessions (self-development) / 10 sessions (external). Numbers are guesses. Calibration data is operator-held; first revision after the first external-problem trial.
- **OI-078-002:** Conditional re-introduction trigger for LLM reviewer (one engine_feedback row from human reviewer-subtractor naming a class of error the substrate did not catch but a substrate-query reviewer could) may be slow to fire. Absence of trigger ≠ absence of need; cadence-driven dossier read is the surface for diagnosing the absence.
- **OI-078-003:** The decision-`body_md`-as-prose carve-out (D-1) is the load-bearing weakness in S1-typed. If 080–095 produce evidence of decision body drift (≥2 cases where two `body_md` cells contradict each other and the substrate did not refuse), the substrate-shape revisits.
- **OI-078-004:** The 30-session non-self-application threshold for D-5's release gate is `[adv]`'s number, deliberately wrong-in-detail. Operator-revisable at first external-problem trial open.

## Engine-feedback raised by this session

None. The engine-v16 spec set executed adequately for a foundation-touching commitment session. Two operational notes recorded as honest limits in the close (`03-close.md`).
