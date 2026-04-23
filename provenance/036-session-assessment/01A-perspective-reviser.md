---
session: 036
title: Perspective — Reviser (Path PD)
date: 2026-04-23
status: complete
perspective: Reviser
committed_at: 2026-04-23T00:00:00Z
---

## Q1 — Dispatcher revision

The dispatcher should be revised. The current `PROMPT.md` lines 18–26 encode a Session-001 signature for external-problem routing ("fresh / empty / near-empty") that structurally cannot survive Session 002. The self-development branch uses a semantic qualifier ("of self-development") that is not structurally verifiable from the workspace alone — an in-flight external application's `SESSION-LOG.md` is file-format-identical. The failure mode is benign (halt-and-ask rather than misroute), but the dispatcher is nonetheless under-specified and forces operator intervention on every post-Session-001 external load. That friction scales linearly with external-application session count and compounds across multiple concurrent applications.

The most coherent minimal revision is **Direction 2 (stable structural signature)** anchored on the presence or absence of `applications/NNN-<slug>/brief.md`. This is already how external applications are initialised per `engine-manifest.md` §6. The brief file exists from Session 001 onward and persists through steady-state. It is the cleanest available structural invariant.

I reject **Direction 1 (MODE.md marker file)** as over-engineered. A new top-level file adds an engine-definition surface, requires validator awareness, and introduces a new failure mode (marker present but stale/wrong). We already have `applications/` as the structural signal; adding MODE.md duplicates state.

I reject **Direction 4 (separate PROMPT files)** as worse over-engineering — it forces the operator to choose the prompt, pushing the dispatch decision out of the engine and into the human. The whole point of `PROMPT.md` is dispatch-at-load.

I reject **Direction 3 (SESSION-LOG frontmatter `mode:`)** because SESSION-LOG has not historically carried frontmatter in this workspace (based on the brief's descriptions; flag as inference) and adding it for dispatch purposes re-uses the wrong surface — SESSION-LOG is a record, not a configuration.

Proposed revised dispatch text for `PROMPT.md` lines 18–26 (the entire §Dispatch block):

> **§Dispatch.** At load, determine the workspace mode from its structural signature:
>
> - **External-problem application** — if the workspace contains the engine-definition files enumerated in `specifications/engine-manifest.md` §3 AND contains at least one `applications/NNN-<slug>/brief.md` file, load `prompts/application.md`. The external-problem branch applies regardless of `SESSION-LOG.md` contents; Session 001 and Session N both route here.
> - **Self-development application** — if the workspace contains the engine-definition files AND contains `provenance/001-genesis/` (or equivalent Session 001 self-development provenance marker) AND contains no `applications/NNN-<slug>/brief.md`, load `prompts/development.md`.
> - **Ambiguous or uninitialised** — if the workspace does not yet contain the engine-definition files, or if both signals are present (external `brief.md` AND self-development genesis provenance, which may occur in nested or migrated workspaces), or if neither signal is present, halt and seek clarification from the operator.

This revision closes the §2a gap cleanly: the external-problem branch no longer depends on a Session-001-only freshness property, and the self-development branch gains a positive structural signal (`provenance/001-genesis/`) rather than relying on the unverifiable "of self-development" qualifier. The fallback is preserved and narrowed.

The Skeptic-preserver will argue for no change on grounds that halt-and-ask is safe and that each dispatcher revision risks regression in a mature engine (engine-v6 preservation count 2, zero friction). My counter: the current dispatcher is provably incorrect for external-application steady-state — it cannot route without operator intervention. "Safe-but-wrong" is still wrong, and the cost of carrying the gap grows with external-application adoption. Preservation is warranted when the artefact works; here it does not, for a known-non-hypothetical use case we have explicitly designed toward. The revision text above is three-bullet, uses only existing structural elements, and introduces no new files. That is minimal.

## Q2 — Feedback pathway from external applications

The most coherent minimal pathway re-uses **open-issues (OIs) plus provenance**, with a single new convention: an OI raised in an external application's workspace may be tagged `scope: engine-feedback` in its frontmatter. At external-application session close, the operator collects any `scope: engine-feedback` OIs and carries them (verbatim, as copy-paste) into the self-development workspace as new OIs or as comments on existing OIs. No new directory. No new file type. No new tool.

Concretely, I propose a short addition to `specifications/workspace-structure.md` (or wherever OI conventions live — flag as inference from the brief's enumeration of specifications) defining the `scope:` field with two values: `application` (default, stays local) and `engine-feedback` (intended for return to self-development). And a short addition to `prompts/application.md` instructing external-application agents that when they surface methodology-level friction — unclear spec, kernel §7 gap, MAD v4 awkwardness, dispatcher ambiguity, reference-validation gap — they raise a `scope: engine-feedback` OI rather than attempting to self-modify the engine from inside the external application.

The intake convention on the self-development side: at Session N open in self-development, if the operator has queued `engine-feedback` OIs from external applications, they are introduced as operator-mediated OIs with a provenance pointer to the originating external workspace and session. They then follow normal OI disposition — activation warrants, preserved-minority discipline, all existing machinery applies.

**Retention:** the originating external-application OI stays in that workspace's `open-issues/` (it is part of that application's record). The self-development workspace gets a copy-with-pointer. Both records persist. No merge conflict, no authority conflict.

**Discipline:** the field `scope: engine-feedback` is an advisory tag. It does not authorise the external application to modify the engine. It signals "this belongs upstream." Operator retains ratification authority for whether/when the upstream OI is opened in self-development. This preserves the existing operator-ratification discipline while making the pathway structural rather than memory-dependent.

I considered and reject a dedicated `engine-feedback/` directory in external-application workspaces. That duplicates OI machinery for a rare case. I considered and reject a watchpoint-based pathway (WX entries); watchpoints are scoped to single-workspace recurring observations, not cross-workspace artefacts. OI re-use is the cleanest fit.

I considered a new `scope:` field versus overloading the existing OI-type taxonomy. Overloading would be cheaper still but risks conflation: an OI can be *about* the engine AND *about* the application simultaneously, and a type-taxonomy entry cannot cleanly express that. A frontmatter `scope:` field can.

External input flag: the term "scope" as a frontmatter convention is common in issue-tracking systems generally (external pretrained knowledge). I claim no specific prior-art precedent in the Selvedge engine.

## Q3 — Relationship between Q1 and Q2

Q1 (inbound dispatch) and Q2 (outbound feedback) are **related by theme but independent by mechanism**. They both concern the engine/application boundary but operate on different surfaces (`PROMPT.md` §Dispatch vs `open-issues/` + `prompts/application.md`). They can and should be solved by separate revisions in separate files. Bundling them into a single mechanism — e.g., a MODE.md that also carries feedback pointers — would over-engineer both.

They do share one implementation moment: both should be addressed in the same session (036) and the same engine-v bump, because both arrived on the engine's radar at the same time, both concern external-application steady-state, and deferring one while shipping the other leaves asymmetric readiness. But the *artefacts* are separate. This is independence of mechanism within co-scheduling of delivery.

## Q4 — Substantive revision scope

Files touched under my proposal:

1. `PROMPT.md` — replace §Dispatch block (lines 18–26) with the three-bullet revised text above. ~15 lines of text change.
2. `specifications/workspace-structure.md` — add `scope:` field definition for OI frontmatter, ~10 lines.
3. `prompts/application.md` — add short paragraph on raising `scope: engine-feedback` OIs when methodology-level friction arises in external application work, ~8 lines.
4. `specifications/engine-manifest.md` §6 — add one sentence noting that external-application OIs may be tagged for engine-feedback return. ~2 lines.
5. `specifications/engine-manifest.md` §7 — new engine-v7 entry documenting the Session 036 bump, rationale, substantive content.

OI-002 classification: **substantive** under the existing heuristic. The revision modifies dispatch behaviour (functional change to `PROMPT.md`) and introduces a new cross-workspace convention (`scope: engine-feedback`). Both affect engine behaviour observable to agents, not merely record-keeping.

Engine-v bump: **engine-v6 → engine-v7**. This would be the sixth engine-v bump and the third post-cadence-maturation content-driven bump. Preservation count for v6 would close at 2 (consistent with the v5 → v6 transition cadence; flag as inference).

Preserved-minority structure: if the Skeptic-preserver's no-change argument is rejected at decision, preserve it as a first-class minority in reference-validation.md §10.3 with activation warrant "If engine-v7 dispatcher revision causes a routing regression within 6 sessions post-adoption, re-evaluate rollback to engine-v6 dispatcher text." This mirrors the Session 014/032/033 end-to-end preservation-activation-adoption pattern.

## Q5 — First-class minority preservation

Rejected directions warranting preservation:

- **Direction 1 (MODE.md marker file)** — preserve with activation warrant: "If the `applications/NNN-<slug>/brief.md` structural signal proves ambiguous in practice (e.g., workspaces with brief.md but no intent to run as external application), reconsider explicit mode marker." 6-session evaluation window.
- **Direction 4 (separate PROMPT files)** — preserve with activation warrant: "If the unified PROMPT.md §Dispatch block grows beyond three routing cases or develops mode-specific logic exceeding 30 lines, reconsider split." Indefinite retention; activation on structural threshold rather than session count.
- **Dedicated `engine-feedback/` directory (rejected under Q2)** — preserve with activation warrant: "If `scope: engine-feedback` OI tagging proves insufficient for three or more cross-application feedback events (lost, conflated, or operator-burden exceeds tolerance), reconsider dedicated directory."

Each is preserved per §10.3 discipline with the activation-clock cadence established by the Session 014/032/033 lineage.

## Q6 — WX-35-1 disposition

Defer. WX-35-1 (the 13-session claimed-but-unexecuted OI-004 edit gap) is an orthogonal integrity concern about past sessions' commit fidelity. Bundling it into the Session 036 substantive engine revision would mix an audit-discipline fix with a dispatcher+feedback-pathway fix, reducing provenance legibility for both.

My recommendation among the three options: **(c) incremental catch-up**, but *not in Session 036*. Session 037 or 038 can dedicate a Path that addresses WX-35-1 specifically, with a short audit pass reconciling the 13 sessions of SESSION-LOG row narrative against actual OI-004.md commit history, writing a single consolidated edit that brings the file current and records in the session close that the 13-session gap is closed. Option (a) retroactive backfill is anti-laundering-adjacent (rewriting history to look like it happened as narrated); option (b) convention-change treats the gap as retrospectively-fine which cheapens future edit-claim discipline.

The default recommendation in the brief is "defer unless bundled." I concur: do not bundle. The Session 036 scope is already substantial (dispatcher revision + feedback pathway + engine-v7 bump). Adding WX-35-1 disposition risks scope-creep into a session that should demonstrate clean single-concern discipline given the breadth of its primary mandate.

---

**External input flags:** (1) "scope" as a frontmatter convention in issue trackers (general software-engineering prior art). (2) The preservation-window cadence of 6 sessions is cited from the brief's mention of the Session 014/032/033 lineage and §10.3; I rely on the brief's summary, not independent inspection of those session records.
