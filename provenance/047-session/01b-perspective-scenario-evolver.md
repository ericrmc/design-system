---
session: 047
title: P2 Scenario Evolver — emergent-pressure-plus-operator-injection evolution mechanic with supersession-marker spec amendment preserving D-017 immutability via forward-reference ledger
date: 2026-04-24
status: raw
perspective: scenario-evolver
committed_at: pending
---

# P2 Scenario Evolver — raw perspective

## 1. Position summary

My feedback-yield thesis: the between-session machinery should **force the engine to confront retroactive invalidation as a first-class event** rather than letting executing sessions treat constraint change as "a fact that happened to change." Three choices follow. (a) The evolution mechanic is **emergent-with-injection** — per transition, axis + magnitude are pre-declared in the self-dev arc-plan; the operator selects the specific prior-session assumption to invalidate based on what the session actually committed to, and delivers the constraint-update brief at the next session's T0. This ties invalidation causally to executing-session choice so it cannot be dismissed as arbitrary. (b) Retroactive invalidation is recorded via a concrete **supersession-marker mechanism** (β from brief Q2) — prior-session files remain byte-identical; the marker is a new `open-issues/OI-NNN.md` with `supersedes-assumption-in:` frontmatter plus an appended row in an application-scope `supersession_ledger.md`. D-017 is preserved because no closed-session file is edited. (c) Four transitions rotate through coordination / infrastructure+comms / demand / validation-approach, the fourth being an engine-internal meta-axis that makes E-005 the yield-harvest session where the arc's qualitative-multi-agent validation gaps become explicit feedback. The design exercises retroactive-invalidation recording, OI state-machine under invalidation, minority preservation under invalidated assumption, validation-label vocabulary gap, and hidden-scenario session-done-ness.

## 2. Q1 — Scenario at T0 + arc structure

### 2.1 Scenario at T0

**Setting:** the **Kaelor coastal corridor** in the fictional Republic of Ostrava — 400 km of littoral plain with three estuary cities (Meristem, Tarsal, Vell-by-the-Sound); population affected ~**1.4 million** (~820 k urban + 580 k distributed).

**Disaster class: compound slow-onset** — a multi-week storm-surge sequence has saturated coastal aquifers, collapsed one of three east-west rail trunks, and disabled two of four coastal telecomms exchanges. Mortality low-hundreds-stable; the operational problem is **sustainment** of 1.4 million with 40-70 % infrastructure degraded, second surge forecast in 5-9 days. Slow-onset chosen deliberately: rapid-onset front-loads decisions into T0 and compresses the arc; slow-onset forces sustained multi-session planning where mid-arc constraint changes are organically motivated.

**Key T0 constraints:** Meristem has ~2,400 dialysis-dependent patients; Tarsal holds the regional neonatal unit; Vell-by-the-Sound depends on the fishing fleet. One intact rail trunk; one intact highway bridge (24 t post-surge); one grid substation degraded 40 %. Central government pledged 2,000 responders + 400 vehicles over 14 days; neighbouring states offered-not-committed. **Plausibly-researchable-but-fictional** — no real coastline to anchor on.

### 2.2 Arc structure

**Five sessions** (the upper bound of operator scope; the extra session is needed because the feedback-yield-optimal design requires a dedicated session on retroactive invalidation rather than bundling it).

| Session | Broad objective | What has changed since prior session |
|---|---|---|
| E-001 | **System model + explicit assumptions** for the Kaelor corridor; first draft response plan covering weeks 1-2 | n/a (T0) |
| E-002 | **Coordination-axis shift:** regional authority structure changes; response plan revised | Coordination axis (central-command → distributed-municipal; or the inverse) |
| E-003 | **Infrastructure-axis shift:** the comms partial-collapse deepens into near-total-outage over affected population for 36-72 hours; response-plan revision | Communications + infrastructure axes coupled |
| E-004 | **Demand-axis shift:** the second storm surge arrives sooner and worse than forecast; demand surges across water, shelter, medical | Demand axis (the substrate) |
| E-005 | **Validation-axis meta-shift** (see §Q2.3 below): the arc reveals to the executing session that several sessions' qualitative-multi-agent validation missed something that a different validation shape would have caught; the session's job is to document this rather than to plan further | "Validation-approach" — the engine-internal axis added by me beyond the operator's four |

The arc leans into stress-tests of the engine's validation and invalidation machinery. Sessions E-001 through E-004 rotate through infrastructure / communications / coordination / demand per operator scope (with coupling between infrastructure and comms in E-003 because pretending they are independent would launder the scenario into implausibility). E-005 is the **yield-harvest** session — its whole purpose is to make the engine confront what the preceding four sessions' qualitative-multi-agent validation could not see from within themselves.

### 2.3 Placement approach (§2.5 amendment Q1)

**Approach (a): authoritative arc-plan lives in self-dev.** The operator reads it at each external session's open and delivers only the relevant per-session constraint-update brief into the external workspace. Rationale: simplest against the "no full view until arc completion" constraint; requires no spec amendment in the external workspace (its `read-contract.md` §1 enumeration is unchanged); self-dev copy is version-controlled for vindication-criteria assessment at arc-end.

Rejected (b) hidden-file-in-external (requires external read-contract amendment); rejected (c) split-into-per-session-reveal-files (file-proliferation in external workspace needs its own governance); rejected (d) operator-held (not version-controlled; too fragile for arc-end assessment).

## 3. Q2 — Constraint-evolution mechanic + D-017-compliant retroactive-invalidation handling

### 3.1 What changes (per-axis specification)

**E-001 → E-002 (Coordination):** a constitutional ambiguity between federal and provincial authority over coastal-zone response is invoked by the provincial governor of Ostrava-East, who claims local authority over Meristem and Tarsal. **Two parallel command structures** now exist. E-001's single-command response plan is not executable as-written.

**E-002 → E-003 (Communications + Infrastructure, coupled):** solar activity plus storm-surge damage to the remaining two coastal telecomms exchanges drops the region into near-total comms outage for 36-72 hours. The intact rail trunk's signalling is comms-dependent; freight planning in E-002 that assumed rail-trunk availability is invalidated (daylight sight-line traffic only, reduced capacity). I couple comms + infrastructure here because pretending they are independent would launder the scenario into implausibility.

**E-003 → E-004 (Demand):** the forecast second surge arrives 3 days earlier and 1.4 m higher than prior forecasts. Water-supply demand doubles against a half-degraded network; shelter demand triples in Tarsal as the Old Harbour district inundates. E-003's demand envelope is invalidated.

**E-004 → E-005 (Validation-approach axis, added by me):** at E-005 open the operator reveals to the executing session that several prior-session assumptions their multi-agent validation converged on (≥ 3-of-4) have turned out to be wrong in ways the validation shape could not have caught — they were plausibility-constrained rather than consequence-constrained. Not a scenario-axis change in the operator-four-axis sense; an engine-axis change. E-005's job is not re-planning but documenting engine-feedback: what about the reference-validation-void fill-in produced false confidence.

### 3.2 How the change is delivered (delivery mechanism)

**Mechanic: emergent-with-injection** — hybrid of Q2 options (b) pre-scheduled and (c) emergent-from-prior-outputs.

- **Pre-declared in the self-dev arc-plan:** the four axes and magnitude ranges above are fixed in the authoritative plan. Operator latitude at each transition is bounded.
- **Injected by operator at session-open:** the operator reads the prior external session's outputs, selects the most load-bearing assumption intersecting the pre-declared axis, and drafts a constraint-update brief invalidating *that specific assumption*. The brief is placed in the external workspace at session T0 (e.g., `applications/001-disaster-response/session-input-002.md`).

Delivery is operator-transport-compatible per §2.5 amendment. The hybrid avoids two failure modes: pre-scheduled-only invites "constraint change irrelevant to what the session actually committed to"; pure-emergent invites "operator retcons whatever at each transition." Operator latitude is bounded to which specific assumption within the fixed axis.

### 3.3 D-017-compliant retroactive-invalidation recording

I propose **mechanism β** (supersession-marker spec clause) with a concrete two-part schema:

#### 3.3.1 Per-session marker in the current session's OI

Each external session that invalidates a prior session's assumption opens a new `open-issues/OI-NNN.md` in the *external workspace's* `open-issues/` directory with frontmatter:

```yaml
---
id: OI-NNN
status: open-invalidated-assumption
surfaced-in-session: <current-session>
supersedes-assumption-in:
  - path: applications/001-disaster-response/<artefact>.md
    section: <heading or line-range>
    session-of-origin: <prior-session>
supersession-reason: <one sentence>
---
```

Body includes: (a) verbatim quote of the superseded assumption, (b) the constraint-update brief content that invalidated it, (c) what the current session's revised artefact proposes instead, (d) explicit note that the prior-session provenance file **remains unchanged** per D-017.

This is D-017-compliant because no closed-session file is edited. The OI is a new file in the current session's (mutable) scope.

#### 3.3.2 Arc-level ledger in application-scope

A single `applications/001-disaster-response/supersession_ledger.md` in the external workspace: flat chronological ledger, one row per supersession event, columns `event-id | session | superseded-artefact | superseded-assumption | superseding-artefact | OI-reference`. It is a **mutable application-scope file** per `workspace-structure.md` §applications; appending is allowed without violating D-017; prior content is never edited. Prior artefact versions remain at their original paths as historical witnesses.

#### 3.3.3 Implied spec amendment

The ledger itself requires no amendment (existing §applications mutability covers it). What requires amendment is `workspace-structure.md` §provenance's D-017 clause to **explicitly name** the supersession-marker mechanism. D-017 currently reads "Errors or retractions are recorded in subsequent sessions, not by editing past records" — correct but under-specified. Proposed added paragraph:

> When a session invalidates a prior session's assumption, the invalidating session records the invalidation via (a) a new OI-NNN.md file with frontmatter field `supersedes-assumption-in:`, and (b) if part of a multi-session arc, an appended row in application-scope `supersession_ledger.md`. Neither edits any prior-session provenance file.

**OI-002 classification: minor.** The amendment operates entirely within existing D-017 immutability (no new rule that contradicts or expands D-017's scope); it elaborates rather than adds new rules; no new validator check; adds one frontmatter field to an existing file class (OI-NNN.md) consistent with Session 021 D-082's pattern. Trigger per OI-002 heuristic: "annotates existing candidate entries with descriptive metadata within the section's stated purpose." Engine-v bump NOT required (engine-manifest.md §5 non-bump list). If synthesis reclassifies substantive (trigger "new required frontmatter field"), engine-v bump would follow. I flag the ambiguity.

### 3.4 Minority-preservation under constraint invalidation

Brief §2 named this. My proposal: **minorities are not auto-invalidated.** A preserved minority's activation warrant typically references the substance of its position, not the scenario-state that induced it. When constraint change invalidates the scenario-state, the invalidating session's deliberation re-evaluates: (i) the minority's position is now moot (recorded with forward-reference, preserved verbatim), or (ii) the minority is vindicated under new constraints (vindication event). Neither edits the original minority-preservation record. Mirrors the self-dev §5.3-vindicated-at-S027 pattern.

## 4. Q3 — Artefact progression

All artefacts live at `applications/001-disaster-response/` in the external workspace unless noted.

### 4.1 Artefact set per session

| Artefact | E-001 | E-002 | E-003 | E-004 | E-005 |
|---|---|---|---|---|---|
| `system-model.md` | v1 | v2 | v3 | v4 | frozen |
| `assumptions.md` | v1 | v2 | v3 | v4 | frozen |
| `response-plan.md` | v1 | v2 | v3 | v4 | frozen |
| `risks.md` | v1 | v2 | v3 | v4 | frozen |
| `decision-tree.md` | v1 | — | v2 | v3 | frozen |
| `supersession_ledger.md` | — | new row | append | append | final row |
| `session-input-NNN.md` | (T0 is brief.md) | operator-delivered T0 | same | same | same |
| `engine-feedback/EF-NNN-*.md` | — | candidate | candidate | candidate | **mandatory** (≥1) |

Each artefact carries frontmatter with `originating_session`, `last-revised-session`, `supersedes` (path to -v(N-1).md if versioned), and `validation: qualitative-multi-agent` (new value; see §5.3). Revised versions use the `-v1.md`/`-v2.md` preservation pattern per S013 D-066 (external-artefact revision pattern); canonical path holds the current version; the ledger references specific version-to-version supersessions.

### 4.2 Which live in external vs self-dev

Per §2.5 (placement a): **external only** — all artefacts in the table above. **Self-dev only** — the authoritative arc-plan and self-dev-side engine-feedback triage. **Both (via operator transport)** — `session-input-NNN.md` drafted in self-dev, placed in external; engine-feedback records produced in external, copied to self-dev inbox.

### 4.3 Sealed vs mutable

Per workspace-structure.md §applications: **mutable across sessions** — `system-model.md`, `assumptions.md`, `response-plan.md`, `risks.md`, `decision-tree.md` (revision uses -v1/-v2 preservation per S013 D-066; no silent overwrites). **Append-only** — `supersession_ledger.md`. **Sealed at origin** — each external session's provenance (01/02/03 files) per kernel §Record + workspace-structure §provenance D-017.

## 5. Q4 — Validation approach per session

### 5.1 Per-session validation shape

Reference-validation is explicitly N/A (fictional; kernel §7 Provisional reference substitute cannot run without a pre-selected documented proven solution). Domain-validation has no domain-actor. What remains: qualitative-multi-agent plus workspace-validation.

**E-001 through E-004 (same shape each):** 3-perspective MAD — Plan Builder (Claude) + Assumption Prober (Claude, adversarial, satisfies kernel §Convene requirement) + Stakeholder Simulator (Codex/GPT-5.5, speaking from a specific stakeholder position: E-001 Meristem hospital administrator; E-002 Ostrava-East provincial governor's office; E-003 fishing fleet captain; E-004 central-government logistics officer). Convergence threshold 2-of-3 (MAD v4 does not fix a threshold below 4-participant); minority preservation applies. Case Steward synthesises per MAD v4 §Synthesis.

**E-005 differs:** meta-reflective — 4-perspective two-family (2 Claude + 2 Codex/GPT-5.5) mirroring S047 shape, because "what did the arc's validation not see?" is itself a reference-validation-void exercise.

### 5.2 Validation-criteria in the reference-validation void

Non-reference / non-domain-actor criteria, checkable by the Case Steward synthesiser at each session's close:

- **Internal coherence:** session artefacts don't contradict each other or prior non-superseded artefacts.
- **Cross-artefact consistency:** `assumptions.md` lists every load-bearing premise used in `response-plan.md` and `decision-tree.md`; reverse-check passes.
- **Adversarial-probe outcome:** the Assumption Prober surfaces ≥1 premise not explicit in the plan; resolved by adding to `assumptions.md` or revising plan.
- **Stakeholder-simulation outcome:** the Simulator surfaces ≥1 operational constraint the Plan Builder had not represented; resolved by model adjustment or explicit mismatch flag.
- **Engine-feedback candidate check:** Close explicitly asks "did execution surface engine-level friction?" — records `EF-NNN-*.md` candidate or explicitly declines with reason.

### 5.3 New validation-label proposal

Introduce frontmatter value `validation: qualitative-multi-agent` for external-application artefacts under the above shape. Distinct from `reference-provisional` (sealed three-cell protocol per reference-validation.md) and `domain-validated` (domain-actor receipt).

**OI-002 classification: substantive.** Adds a new label value to kernel v6's normative label vocabulary (trigger: new normative content). Requires kernel §7 Validate revision to enumerate the label alongside `reference-provisional` and `domain-validated`, with a clause stating `qualitative-multi-agent` applies when both (a) no domain-actor available and (b) fictional/unstageable scenario precludes reference-exercise. Kernel v6 → v7 bump; engine-v7 → engine-v8 bump.

Flagged as **feedback-yield candidate**: surfacing that the current label vocabulary has a gap is itself high-value E-005 engine-feedback, arguably its primary output.

### 5.4 Case Steward placement

Case Steward sits at synthesis per MAD v4 §Synthesis. In this arc, the Case Steward is the single continuous orchestrator across all five external sessions (S046 D-142 single-orchestrator pattern). This creates continuity-of-memory risk (anchoring on E-001 framing across E-002-E-005); itself an engine-feedback candidate if observed. Recommend E-005 deliberately convenes with lineage-distinct orchestration attempt (operator as reviewer, perhaps) to test.

## 6. Q5 — Feedback-yield optimisation (primary target)

### 6.1 Engine surfaces the evolution mechanic deliberately exercises

**Surface 1 — Retroactive invalidation under D-017 (brief §2 primary).** Exercised by §3.3 two-part marker. Expected feedback: **EF-003-retroactive-invalidation-handling.md** — "workspace-structure.md §provenance D-017 is under-specified for multi-session applications; the invalidating-session's handling of superseded assumptions required a mechanism this arc had to invent." Property: **unclear spec + missing affordance** — D-017 is correct but leaves sessions to invent the mechanism, creating inter-session inconsistency risk.

**Surface 2 — OI state-machine under constraint invalidation (brief §2).** Exercised by the `status: open-invalidated-assumption` value in §3.3.1, absent from the existing OI state enumeration. Expected feedback: **EF-004-oi-state-constraint-invalidated.md** — "OI states (open/resolved/deferred) have no state for 'surfaced by constraint invalidation, closed-by-mooting later'; sessions misuse `resolved` or invent unofficial states." Property: **missing affordance** — OI state-machine gap.

**Surface 3 — Minority preservation under invalidated scenario-state (brief §2).** Exercised by §3.4 — the arc will produce a minority at E-002 whose scenario-grounding is invalidated at E-003. Expected feedback: **EF-005-minority-under-invalidation.md** — "MAD v4 §Preserve Dissent is silent on how a preserved minority's warrant reads when its scenario-state is invalidated; the operator decided ad hoc between lift / re-word / preserve-with-forward-reference." Property: **missing affordance** — MAD v4 scaling gap across evolving state.

**Surface 4 — Validation-label vocabulary gap (kernel §7).** Exercised by §5.3 — `qualitative-multi-agent` doesn't exist in kernel v6's label enumeration. Expected feedback: **EF-006-validation-label-vocabulary-gap.md** — "kernel §7 has no label for legitimately-qualitative-only validation when both domain-actor absence and fictionality preclude reference-substitute; this class has no correct frontmatter label." Property: **rigid convention** — fiction-without-domain-actor is a third legitimate path the enumeration doesn't name.

**Surface 5 — Hidden-scenario non-visible-scope handling (brief §2.5).** Exercised by operator-transport delivery + placement (a). Expected feedback: **EF-007-non-visible-scope-session-done-ness.md** — "kernel §1 Read and §9 Close assume the session determines done-ness from its own scope; the hidden-scenario constraint forced sessions to reason about stopping mid-deliverable because a later session will reveal shape-changing content. §9 Close needs a partial-view-execution clause." Property: **load-bearing gap** — done-ness criterion assumes full-view.

### 6.2 Compliance note

Role requires ≥2 surfaces; I provide 5. Surface 1 is retroactive-invalidation handling (explicitly required); Surface 3 engages MAD-scaling-across-arc; Surface 5 engages the §2.5 hidden-scenario constraint.

### 6.3 Engine surface deliberately NOT targeted

**Engine-v bump trigger criteria (OI-018).** The arc does not attempt to surface OI-018 feedback on engine-manifest §5 bump-trigger calibration. OI-018's domain is internal spec-revision cadence, not external-application exercise; conflating risks laundering OI-018 feedback from data not designed to measure it. If arc-induced revisions to kernel §7 (Surface 4) or workspace-structure §provenance (Surface 1) trigger engine-v bumps, that is adjacent data for OI-018 but not primary feedback. Also deliberately not targeted: **§5.6 GPT-family concentration** — the two non-Claude seats are Codex/GPT-5.5 per S044 R2; the arc continues §5.6 worst-case-side data rather than mitigating it, but §5.6 is not the arc's target.

## 7. Confidence and limits

**High confidence:** (a) the supersession-marker mechanism (§3.3) is D-017-compliant; (b) emergent-with-injection is operator-transport-compatible per §2.5; (c) Surfaces 1 and 5 will be exercised almost regardless of executing-session choice.

**Medium confidence:** (a) OI-002 classification of my §3.3.3 amendment as minor — I argued minor but concede the "new required frontmatter field" framing could justify substantive; defer to synthesis. (b) that 5 sessions is correct — 4 sessions with E-005 bundled into E-004 was considered and rejected because bundling reduces meta-reflection's feedback-yield (a session focused on demand-surge re-planning is not positioned to step back to methodology-level observation).

**Low confidence:** (a) whether the Kaelor-corridor specifics resist executing-session real-world anchoring (Katrina, Idai) — chose plausibly-researchable-but-fictional to mitigate but not eliminate. (b) whether `qualitative-multi-agent` (§5.3) is the right label token; alternatives include `multi-agent-unfalsifiable`, `scenario-qualitative`. Bikeshed-prone; cross-family input useful.

**Independence compliance:** read the shared brief, workspace-structure.md v5, methodology-kernel.md v6, read-contract.md v4, open-issues/index.md, OI-019.md, OI-002.md. Did NOT read other perspectives' outputs, self-dev S046 deliberation, or any content in `/selvedge-disaster-response/` (top-level `ls` only, no file reads).

**§5.6 transparency:** both non-Claude seats in any 4-perspective shape convened under this arc are Codex/GPT-5.5 per S044 R2 standing preference. Arc continues the §5.6 worst-case-side data point.

## 8. Independent-claim evidence pointer

Not required for Claude subagent (P2) per §6.
