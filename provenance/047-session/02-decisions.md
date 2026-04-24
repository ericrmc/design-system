---
session: 047
title: Decisions — S047 Path OS operator-directed MAD design of arc-plan for selvedge-disaster-response external application; D-147 adopt arc-plan (5-session arc / placement (a) self-dev authoritative / 70-30 hybrid evolution / three-part D-017-compliant invalidation mechanism / 4-perspective per-session MAD with Laundering Auditor / 7 targeted feedback surfaces / measurable anti-laundering guards adopted as first-class from P4); D-148 produce arc-plan artefact at provenance/047-session/arc-plan.md; D-149 OI-019 cross-linkage; D-150 defer three spec-amendment candidates to post-arc self-dev review; D-151 housekeeping (D-133 M2 second-of-3 vindication-side; WX-44-1 n=3 OI-promotion evaluation → forward convention candidate not OI; §5.6 worst-case-side continues; engine-v7 preservation window count 11 new longest extended further)
date: 2026-04-24
status: complete
---

# Decisions — Session 047

## D-147: Adopt arc-plan design from MAD synthesis for selvedge-disaster-response external application

**Triggers met:** [none]

**Triggers rationale:** No engine-definition specification file is edited by this decision. The adopted arc-plan is an application-scope artefact for an external-problem application; it lives in the self-dev S047 provenance but prescribes work for a different workspace. Three implied spec-amendment candidates are identified but explicitly **deferred** to post-arc self-dev review (D-150), not adopted in-session. MAD v4 triggers 3 + 4 (reasonable disagreement + load-bearing) applied to convene the deliberation itself; no d016_*/d023_* triggers fire on adoption of the design product.

**Decision:**

Adopt the synthesised arc-plan design for the 4-5 session disaster-response external application per §2 + §3 of `01-deliberation.md`. Core parameters:

1. **Session count: 5.** S001 baseline → S002 invalidation 1 (coordination) → S003 invalidation 2 (infrastructure+communications) → S004 invalidation 3 (demand) → S005 recovery + engine-feedback synthesis.

2. **Scenario**: fictional compound coastal-hazard event in a synthesised fictional geography (named in the arc-plan artefact per D-148). Compound (surge + power + water + coordination) because compound hazards produce organic per-session constraint invalidations without narrative contrivance.

3. **Placement per §2.5**: **option (a) strict** — authoritative arc-plan lives in self-dev at `provenance/047-session/arc-plan.md`. External workspace receives operator-transported per-session reveal files at each T0 (`applications/001-disaster-response/session-inputs/session-00N-input.md`, sealed on delivery). External workspace does NOT receive the full arc-plan until arc completion (S005 close or later).

4. **Constraint-evolution mechanic**: 70/30 hybrid per §2b of `01-deliberation.md`. Pre-declared per-transition axis in the arc-plan (coordination / infrastructure+comms / demand / validation-meta-via-retrospective); emergent per-transition specific-assumption selection by operator based on prior-session load-bearing commitments.

5. **D-017-compliant retroactive-invalidation handling**: three-part mechanism — (i) mutable `applications/001-disaster-response/assumption-ledger.md` with stable assumption IDs (`A-001`/`A-002`/...), status values `{active, superseded, invalidated, unresolved}`, fields `originating_session` / `invalidated_by_session` / `invalidating_input` / `affected_artefacts` / `prior_provenance_witness`; (ii) append-only `applications/001-disaster-response/supersession-ledger.md` with chronological rows; (iii) new OI-NNN.md in external workspace's `open-issues/` for invalidated assumptions creating unresolved application work, frontmatter `supersedes-assumption-in:` pointer. No closed-session provenance file is ever edited.

6. **Artefact set** at `applications/001-disaster-response/` (external workspace): `system-model.md`, `assumption-ledger.md` (central), `response-plan.md`, `risk-register.md`, `decision-trees.md`, `supersession-ledger.md`, `recovery-plan.md`, plus accumulating `session-inputs/session-00N-input.md` reveal files. Frontmatter per artefact includes `originating_session`, `last-revised-session`, `supersedes` (path to prior version if revised), `validation: qualitative-multi-agent` (new value — feedback candidate per D-150). Mutable artefacts preserve prior versions as `-v(N-1).md` per S013 D-066 pattern.

7. **Per-session validation**: **4-perspective MAD every session**, one role being explicitly **Engine Friction Recorder / Laundering Auditor** (making anti-laundering first-class per P4). The other three per session: Operations Planner / Constraint Skeptic / Stakeholder Simulator (stakeholder varies per session). At least one perspective should be non-Claude when feasible. Convergence threshold 3-of-4 for substantive decisions; minority preservation per MAD v4.

8. **Fallback validation criteria in kernel §7 void** (no reference case available; no domain-actor): internal coherence, cross-artefact consistency (assumption IDs cross-link), adversarial-probe sufficiency (≥1 surfaced hidden premise per session), stakeholder-simulation plausibility, constraint-impact accounting (each reveal names affected assumptions + sections), engine-feedback candidate check (session either produces ≥1 EF outbox record or close-notes explicit justification of non-production).

9. **Measurable anti-laundering guards adopted as first-class** (P4 contribution). Each guard is a close-criterion; absence blocks clean close:
   - Every session-close must list FAILED or STRAINED validation criteria, not only passed. A close with zero strains across 5 sessions is evidence of laundering, not success.
   - Every mutable artefact revision after S001 must update `last-revised-session` and include a `supersedes` OR `change_reason` entry naming the triggering `session-input.md` file.
   - Every session after S001 must name ≥1 prior assumption/artefact-section/OI/minority/validation-claim that was preserved/revised/superseded/invalidated. If no such object is touched, the session did not exercise the intended engine surface.
   - Every reveal session must mark ≥2 assumption IDs as `superseded`/`invalidated`/`still-active-after-review` AND name ≥1 artefact section changed because of the classification.
   - Every session must produce ≥1 EF outbox record OR a close-note explicitly justifying non-production.
   - Each EF record must contain ≥1 concrete evidence pointer (session-input path, artefact diff, OI reference, close-section claim) + application-scope disposition statement; minimum useful body length 250 words; shorter records need close-note justification.

10. **Targeted engine-feedback surfaces (7)**: (1) hidden-scenario partial-view session-done-ness; (2) kernel §7 validation-label vocabulary void; (3) D-017 retroactive-invalidation mechanism; (4) OI state-machine under constraint invalidation; (5) MAD minority preservation under invalidated premises; (6) read-contract `applications/` closed-enumeration ambiguity (P3 unique finding; direct spec contradiction); (7) engine-feedback outbox first-use operability.

11. **Deliberately NOT targeted**: real disaster-response domain competence (no practitioner, no standards); OI-018 engine-v cadence calibration.

**Single-agent reason:** N/A — this decision is made by Case Steward synthesis from a 4-perspective two-family MAD per MAD v4 §Synthesis with 3-of-4 or 4-of-4 cross-family convergence on every substantive design point. Per-perspective raw outputs committed verbatim at `01a-`/`01b-`/`01c-`/`01d-perspective-*.md`. Synthesis cites convergence by perspective number throughout `01-deliberation.md` §2.

---

## D-148: Produce arc-plan artefact at `provenance/047-session/arc-plan.md`

**Triggers met:** [none]

**Triggers rationale:** Writing the artefact operationalises D-147; no additional engine-definition content is created. The arc-plan is self-dev application-scope content for an external-problem application.

**Decision:**

Write the authoritative arc-plan to `provenance/047-session/arc-plan.md` per placement (a). File contents:
- §1 Arc summary + feedback-yield thesis
- §2 Scenario at T0 + setting + named fictional geography + population/vulnerability details
- §3 Arc structure — one subsection per session (S001-S005), each containing: (a) session broad objective; (b) pre-declared axis for any invalidation at its T0; (c) operator-facing stub — what the operator drafts as `session-inputs/session-00N-input.md` and transports into the external workspace at this session's T0; (d) expected artefacts; (e) per-session measurable close criteria
- §4 Evolution mechanic detail (70/30 hybrid; per-axis constraint-update format)
- §5 D-017-compliant three-part invalidation mechanism (assumption-ledger schema; supersession-ledger schema; OI-supersedes-assumption-in frontmatter)
- §6 Per-session validation approach (4-perspective MAD; role definitions; fallback criteria)
- §7 Measurable anti-laundering guards (all six close-criteria from D-147 §9)
- §8 Targeted feedback surfaces + draft EF record templates (7 surfaces from D-147 §10)
- §9 Vindication/refutation criteria for the arc (P4 adopted; observable at arc-end)
- §10 Deferred spec-amendment candidates explicitly named but not adopted this session
- §11 Operator transport instructions — step-by-step for injecting session-NNN-input.md into external workspace at each T0

**Single-agent reason:** Production of the deliverable from D-147 synthesis; no independent design decisions remain.

**File-edit claim per WX-35-1**: `provenance/047-session/arc-plan.md` will be created this session and verified via `git log` at close.

---

## D-149: OI-019 cross-linkage — first operator-directed MAD design of external-application arc with feedback-yield-primary optimisation target

**Triggers met:** [d009_1]

**Triggers rationale:** d009_1 is the OI cross-linkage / per-OI amendment trigger. OI-019 (path-selection work-channel and warrant-surface diversity, opened S043) sub-questions (d) operator-frame-observation input class and (f) extended-baseline visibility mechanism both receive direct data points from this session.

**Decision:**

`open-issues/OI-019.md` §Cross-linkage gains a Session 047 entry + §Session 043+ activation triggers gains a S047 new-class-signal bullet recording:

- S047 is the sixth operator-surfaced-agenda session (S036/S043/S044/S045/S046/S047) and the second operator-directed MAD (S044 Path OC + S047 Path OS-MAD-design). This operationalises sub-question (d) "operator-frame-observation input class" by demonstrating that a Case-Steward-discretion-routed operator directive can specify a particular MAD shape (4-perspective two-family, specific role functions) without spec-level formal input-class articulation.
- S047 provides data for sub-question (f) "extended-baseline visibility mechanism": the arc-plan artefact represents 5-session-planning-at-once, which is a different shape than both the §2c 6-session retention-window retrospective visibility and the self-dev's per-session operator-surfaced agenda. If the 5-session arc executes cleanly and the arc-plan proves accurate forward-scaffold, that is a data point for sub-question (f) favouring the "pre-planned design artefact" mechanism over retention-based or watchpoint-triggered alternatives.
- S047 establishes operator-directed MAD as a recurrent Path OS-MAD-design class within the operator-surfaced super-class. If this pattern recurs at S048+/S049+ with similar design-artefact-producing structure, sub-class discrimination becomes warranted per S046 §4 forward observation.
- The arc-plan's measurable anti-laundering guards (D-147 §9) are a concrete operationalisation of what sub-question (a) "P1 channel-diversity vs P4 warrant-surface-closure" might look like in a different form: P4 warrant-surface-closure was about operator-frame observations; S047's guards are about executing-session operational discipline. Not directly OI-019-resolving, but adjacent data for future deliberation venue.

---

## D-150: Defer three-plus-one spec-amendment candidates to post-arc self-dev review (anti-laundering)

**Triggers met:** [d009_1]

**Triggers rationale:** d009_1 per recording of forward-facing OI-adjacent commitments. Each candidate is a potential OI-018 bump-trigger input or direct spec-revision candidate; formal deliberation is deferred per the same-session-causing-and-revising prohibition.

**Decision:**

The arc-plan execution (S001-S005 of selvedge-disaster-response) will generate `engine-feedback/outbox/EF-NNN-*.md` records targeting up to four spec-amendment candidates. **None is adopted this session.** Candidates are named for operator visibility and for the post-arc self-dev triage session:

**(i) Kernel §7 validation-label vocabulary extension with `qualitative-multi-agent`.** Fictional-plus-no-domain-actor applications have no codified §7 sense; current enumeration is {Workspace validation / Domain validation / Provisional reference substitute}. Adding a fourth sense = new normative content = **substantive** per OI-002 heuristic. If adopted: kernel v6 → v7 + engine-v7 → v8 bump. Post-arc self-dev review decides.

**(ii) `workspace-structure.md` §provenance D-017 supersession-marker codification.** D-017 reads "errors or retractions are recorded in subsequent sessions, not by editing past records" — correct but under-specified for multi-session external applications. Amendment would add a clause naming the three-part mechanism (assumption-ledger + supersession-ledger + OI-supersedes-assumption-in frontmatter). **Minor per OI-002** (elaborates existing rule rather than adding new rules; no new validator check).

**(iii) OI state-machine extension with `constraint-invalidated` / `open-invalidated-assumption` transition.** Current OI states `{open, resolved, deferred}` have no state for "surfaced by later-session constraint invalidation, premise moot." Sessions during arc will open OIs with ad-hoc `status: open-invalidated-assumption`; if the pattern proves operationally valuable, codification is **substantive** per OI-002 (new state = new normative state-machine content; likely new required fields).

**(iv) `read-contract.md` §1 closed-enumeration + `applications/` ambiguity clarification** (P3 unique finding per §2f of deliberation). Current `read-contract.md` v4 §1 enumeration items 0-9 do NOT include `applications/`, implying application-scope is archive-surface by §3 default. But `prompts/application.md` §Read instructs external sessions to read `applications/` as domain scope. Direct spec contradiction latent until the §2.5 hidden-arc constraint makes it operational. Either `read-contract.md` §1 adds `applications/` (minor) or `prompts/application.md` §Read clarifies that it refers to session-scope content selected by the session-open Read activity not the default-read §1 enumeration (minor). Classification depends on which path is chosen.

**Post-arc self-dev review obligation**: after selvedge-disaster-response Session 005 closes, self-dev session N (candidate) should read `engine-feedback/inbox/EF-*.md` records and triage. Candidates above are named in advance for provenance discoverability. If any is adopted, the standard MAD-v4-and-engine-v-bump disciplines apply.

---

## D-151: Housekeeping — verification-window advancements, watchpoint status, engine-v preservation, WX-44-1 threshold evaluation

**Triggers met:** [none]

**Triggers rationale:** No specification change; no OI state transition; no minority preservation. Housekeeping consolidates verification-window data, watchpoint status, preservation-window disposition, and the WX-44-1 OI-promotion evaluation.

**Decision:**

### §D-151a Engine-v disposition

**engine-v7 preserved**. Preservation window count at S047 close: **11** — new longest engine-v preservation window extended further (exceeds S046's 10). First engine-v to reach preservation depth 11 for any content class. Sixth substantive-content session at engine-v7 after S041 / S043 / S044 / S045 / S046.

§5.4 Session 022 engine-v-cadence minority does NOT re-escalate per content-driven-bump precedent chain: S047 produces substantive MAD synthesis but no engine-definition-file change; three implied spec-amendment candidates deferred per D-150.

### §D-151b D-133 M2 Convene-time role/lineage matrix — second-of-3 verification window vindication-side

S047 is the second-of-3 verification-window exercise for D-133 M2 (S044 adopted; S045 was first-of-3 vindication-side; S046 was single-orchestrator and did not fire; S047 is second). §5c of `00-assessment.md` populated the 7-column matrix pre-convene. Compliance verified at synthesis: lineage-constraint honored (Outsider = non-Claude Codex per 21-for-21 convention; 23rd post-operator-correction exercise); synonym-drift guard confirmed (P3 and P4 produced distinct deliverables per §2/§2f of deliberation); departure discipline not triggered; function-audit independent on both P3 (frame-completion + reframe) and P4 (laundering-audit + measurable-guards).

**Second-of-2 verification exercises vindication-side**. Third-of-3 at next self-dev MAD session (sequential-by-MAD-firing, not session-sequential).

### §D-151c D-129 — now standing discipline

D-129 graduated to standing discipline at S046 close per §D-146b (third-of-3 vindication-side). S047 §5b of 00-assessment.md surfaced four non-Path-A alternatives with non-vacuous rationales per standing practice. No verification-window status; applies normally going forward.

### §D-151d Close-rotation

**Seventeenth close-rotation** at S047 close: S041 close (`provenance/041-session-assessment/03-close.md`) rotates OUT of the default-read §2c 6-session retention window; S047 close enters. Post-rotation window: S042/S043/S044/S045/S046/S047. WX-28-1 nineteenth-of-N zero-retention-exceptions sustains vindicated pattern (nineteen consecutive rotations S029-S047 all zero).

### §D-151e Watchpoint and minority status

- **WX-24-1** (MAD word count) stable — no MAD spec amendment this session. 6,637 words unchanged. Sixth-of-N post-S042 reset observation; no-growth streak 20 sessions (new record).
- **WX-24-3** (reference-validation label discipline) n=8 stable.
- **WX-27-1** fourteenth post-repair boundary holds.
- **WX-28-1** 19-of-19 zero retention-exceptions (see §D-151d).
- **WX-33-2** stable at reference-validation.md v3 7,160 words.
- **WX-34-1** standing discipline applied (substantive-row appropriate this session).
- **WX-35-1** standing discipline applied cleanly; explicit retractions in `03-close.md` §1e.
- **WX-43-1** subagent self-commit — P1 and P2 Claude subagents did NOT self-commit this session (Agent tool prompts explicitly instructed no-commit). Cumulative 6-of-N unchanged; new observation window begins from S047 against the explicit-instruction variant.
- **WX-44-1** codex-CLI independence-phase breach — P3 self-disclosed repository-wide-search snippet-surfacing of P2 raw output (not relied on). **n=3 cumulative across S044+S045+S047 — OI-promotion threshold met per S045 close §D-141d.** See §D-151f below.
- **WX-44-2** codex CLI model-version-drift discipline applied (P3 + P4 both gpt-5.5 verified from CLI startup metadata per manifest `transport_notes`; not pattern-copied).
- **WX-47-1 candidate** — codex CLI prompt-leading-`---` argv parsing fragility. First-session observation. Not yet pattern; record for recurrence watch.
- **First-class minorities engine-wide**: 31 at S047 close (unchanged from S046; no new minority preserved this session per §5 of deliberation).

### §D-151f WX-44-1 OI-promotion evaluation (n=3 threshold met)

**Decision: do NOT promote to OI this session.** Forward-convention candidate recorded instead.

Reasoning:

- **Pattern consistency**: all three observations (S044 P4 / S045 P4 / S047 P3) follow the same pattern — codex-CLI perspective during independent phase executes broad repository-wide search (`rg`, broad file-tree-enumeration) which surfaces snippets of other perspectives' outputs in tool output.
- **Operational impact**: low. All three observations were self-disclosed; none influenced the perspective's substantive position (verified by synthesis checking reframes against known P-other content in S047 case).
- **Spec-level vs practice-level**: practice-level. The MAD v4 §Independence discipline is clear; the breach is in execution mechanics (broad search in a shared workspace surfaces neighbor content).
- **Anti-laundering bar for OI promotion from n=3 single-pattern observations**: not met. The forward-convention pathway is more appropriate and less ceremonial than opening a full OI.

**Forward-convention candidate** (to be adopted at a future self-dev MAD session, not this session):

> Codex-CLI prompts during MAD independent phase should explicitly exclude repository-wide search operations (`rg` / `find` / broad `ls` / `grep -r`) over the session's provenance directory. Narrow per-file reads only when the perspective needs to cite a specific engine-definition file for technical accuracy. Deliberations producing a session's provenance directory should add a per-session `.codex-scope-exclusion` marker-file naming the paths off-limits during the independent phase.

**Next action**: at the next self-dev MAD session (where D-133 M2 verification third-of-3 also fires), evaluate whether to adopt this convention as a minor amendment to `multi-agent-deliberation.md` §Non-Claude Participation Mechanism Shape A or to the D-133 M2 matrix's function-audit column. If at that session WX-44-1 has n=4 or if a substantive breach (synthesis-shaping content leaked) has occurred, OI-promotion is reconsidered.

### §D-151g §10.4 observational windows

- **§10.4-M1** (Skeptic-preserver no-revision-warranted on dispatcher): discharged-not-vindicated at S046; status unchanged.
- **§10.4-M2** (Skeptic-preserver premature-feedback-pathway): S047 still pre-arc for the external application. Continued preservation against future-event horizon per S033 §10.3 precedent. First live outbox exercise happens during selvedge-disaster-response Session 001+.
- **§10.4-M5** (Reviser OI-tag-only feedback pathway): **activation-pending on selvedge-disaster-response arc outcome** per S046 D-146 §D-146f. Status unchanged. If arc produces zero feedback-outbox records, activation fires at arc close.
- **§10.4-M3/M4/M6**: continuing preserved-against-future-event-horizon status.

### §D-151h Forward observations consolidated

- P3 epistemic-partition reframe — candidate for future kernel/identity extension; not urgent.
- P4 measurable-anti-laundering-as-first-class adopted into arc-plan §7 — if arc-execution proves these guards effective, candidate for extension to self-dev MAD practice at a future session.
- Three-plus-one spec-amendment candidates explicitly deferred (D-150) — post-arc self-dev review obligation.
- WX-44-1 forward-convention candidate — codex-prompt independence discipline.
- WX-47-1 candidate — codex-CLI `---` argv fragility; single observation so far.

### §D-151i OI-002 data point count

No spec-revision classification triggered this session (all candidates deferred per D-150). OI-002 data-point count unchanged at 15 from S046.
