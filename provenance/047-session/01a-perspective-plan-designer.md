---
session: 047
title: P1 Plan Designer — five-session compound disaster-recovery arc with master plan in self-dev + per-session operator-injected reveals; exercises §7 void, D-017 retroactive-invalidation, MAD-v4 minority-under-invalidation, partial-view scope
date: 2026-04-24
status: raw
perspective: plan-designer
committed_at: <will be filled in by committer>
---

## Position summary

I propose a **five-session compound-incident disaster-recovery arc** in a fictional mid-size coastal city. The scenario is scaffolding selected for its ability to generate structural stress against four named engine surfaces, not for verisimilitude.

**Placement (§2.5): option (a).** The authoritative master plan lives in self-dev at `provenance/047-session/arc-plan-master.md` (single synthesised artefact produced from this deliberation). The external workspace receives **per-session reveal files** at each T0 (`applications/001-disaster-response/session-NNN-brief.md`), each delivered by the operator and containing only that session's scope plus any constraints invalidated at its boundary. This honours "no full view until arc completion" without requiring a new `.orchestrator/` directory convention in the external workspace.

**Feedback-yield thesis.** A clean disaster-response narrative produces little feedback; the engine chugs competently. An arc with **designated invalidation events at known boundaries (S003 and S004)** guarantees that retroactive-invalidation handling, D-017-compliance mechanics, MAD v4 minority-preservation under constraint churn, and §7's fallback behaviour when all three senses are under-specified or N/A are exercised at predictable points. The arc structure hits feedback surfaces per session rather than hoping they emerge; this is the inversion the brief's §2 calls for. I name five engine surfaces exercised and one deliberately skipped in Q5.

## Q1 — Scenario at T0 + arc structure

### Scenario at Session 001 T0

Fictional port city **"Wharncliffe"** (not mapped to any real place), population ~180K, on the southeastern coast of a fictional temperate continent. At T0, the hazard is a **compound event in progress**: (i) an offshore storm surge made landfall ~36h earlier with peak crest ~3.1m above mean high tide, inundating the low-lying port district (~22K residents) and compromising two substations; (ii) salt-water intrusion has taken the primary drinking-water treatment plant offline pending decontamination assessment (backup well capacity serves ~35K on rotation); (iii) road/rail access intact from the interior; sea and air degraded.

Population tail relevant to decisions: ~8% over 70 (~14.4K), ~3% dependent on powered medical equipment (~5.4K). Regional hospital 450 beds, 82% occupied. Two dialysis centres. ~18% non-native-speakers of the majority language.

**Why compound structure.** Compound hazards (surge + power + water) guarantee that assumptions about axis A (e.g., power restoration timeline) can be invalidated by developments on axis B (e.g., water contamination worse than reported) without narrative contrivance at per-session transitions. This is load-bearing for Q2's retroactive-invalidation exercise. I avoid exotic flavor (once-in-200-year events, specific breach mechanics) — narrative detail that does not feed invalidation mechanics is gold-plating; feedback-yield wins per §2 of the brief.

### Arc structure — five sessions

Five, not four, because five is the minimum count preserving a standalone retrospective session (S005) capable of synthesising across an evolving multi-session record. Four would collapse retrospective into recovery-planning and weaken the MAD v4-across-arc feedback surface.

- **S001** — System model v1 + assumptions v1 + risk register v1 + initial response plan v1. OI inventory opened for unresolved uncertainty.
- **S002** — Response plan elaborated (v2) under S001 assumptions; new decision-trees v1 for key branch-points (water-rationing thresholds; medical-evac triggers; comms cadence).
- **S003 (pivot)** — Operator reveals **invalidation event A**: two S001 assumptions + one S002 decision-tree branch invalidated by fictional +48h developments (axes: infrastructure + communications). Session records invalidation D-017-compliantly (P2's machinery), produces response-plan v3, risk-register v2, assumptions v2, and decides fate of S001-opened OIs whose premises no longer hold.
- **S004** — Pivot from acute-response to 4-12 week recovery. New axis (infrastructure reconstruction) enters scope. Absorbs smaller **invalidation event B** (an S002 risk entry revealed as understated; demand-axis census revision ~+40% on medical-equipment-dependent count). Produces recovery-plan v1, system-model v2.
- **S005** — Retrospective + lessons-learned + explicit engine-feedback synthesis emitting concrete records to `engine-feedback/outbox/`. Reads across full 4-prior-session evolving record.

**Structural dependencies (arc-level coherence I own per §5a):** S002 requires S001's system-model + assumptions. S003's invalidation needs specific S001 assumptions pre-committed in the arc-plan-master. S003+ must cite S001/S002 verbatim via `[archive: ...]` per read-contract §6 because those artefacts become archive-surface on S001/S002 close. S005 must read the full arc — the session where external-workspace `read-contract.md` §2b aggregate pressure peaks.

### §2.5 placement: option (a)

Authoritative master plan in `provenance/047-session/arc-plan-master.md` (self-dev). External workspace receives five reveal files `applications/001-disaster-response/session-NNN-brief.md` placed by operator at each session's T0, containing only that session's scope. The slot-template `applications/001-disaster-response/brief.md` records meta only: "This application is run over 5 sessions; each session's brief is supplied by operator at T0 as `session-NNN-brief.md`; no single master plan lives in this workspace."

Rejected alternatives: option (b) hidden file — requires new `.orchestrator/` directory convention (workspace-structure.md spec change in external workspace, unrelated ratification requirement); option (c) per-session files without named master — leaves ambiguous where the master lives; option (d) operator-held outside both — discards deliberation's provenance product. Option (a) preserves MAD v4 §Brief Immutability (each reveal sealed at T0), keeps external workspace's default-read clean, and matches `engine-feedback/` operator-mediated-transport pattern per workspace-structure.md v5 §engine-feedback.

## Q2 — Constraint-evolution mechanic + D-017-compliant retroactive-invalidation handling

I own arc-shape; P2 owns the between-session mechanics in detail. Arc-level answer:

**What changes per transition (arc-level):**
- S001→S002 clean — no invalidation, baseline.
- S002→S003 **invalidation event A** — two S001 assumptions + one S002 decision-tree branch invalidated (axes: infrastructure = water treatment contamination worse than S001 assumed; communications = cell-tower coverage loss on south shore worse and longer-duration than assumed).
- S003→S004 **invalidation event B** (smaller) — one S002 risk entry understated; demand axis revised upward ~+40% on medical-equipment-dependent census.
- S004→S005 — retrospective only, no new invalidations.

**Delivery (arc-level, detail to P2):** option (a) operator-injected constraint-update brief at S003 and S004 T0. I deliberately choose designated invalidation sessions over option (c) emergent-from-prior-session, because emergence makes the retroactive-invalidation surface unpredictable; predictability is needed for feedback-yield at known boundaries. Option (b) pre-scheduled-but-operator-withheld is what the §2.5 constraint actually forces given (a) placement: master plan declares invalidations at S003/S004; operator withholds delivery until those sessions.

Arc-level constraint on P2's format: constraint-update brief must allow S003's deliberation to cite S001/S002 artefacts verbatim via `[archive: ...]` per `read-contract.md` §6.

**D-017-compliant retroactive-invalidation (arc-level structural slot):** mechanism **(α)** — append to S003/S004 record, never edit closed S001/S002 files. Specifically:

1. S001/S002 provenance and `applications/` artefact versions (v1/v2) are immutable after their closing session (D-017; extended by §applications -v1 preservation per Session 013 D-066 precedent).
2. A new file `applications/001-disaster-response/invalidation-log.md` is created at S003 (appended at S004). Each entry: `(session-boundary, invalidated-artefact-path, invalidated-claim-text, invalidating-information, supersession-marker)`.
3. The S003 `response-plan-v3.md` carries `supersedes: response-plan-v2.md` in frontmatter + body cross-references via `[archive: applications/001-disaster-response/response-plan-v2.md]`.
4. Any S001-opened OI whose premise is invalidated at S003 receives a new annotation. If P2 proposes a new "constraint-invalidated" state on the OI state machine, that is a **substantive** OI-002 classification (new state transition = new normative content) and should route to self-dev deliberation, not be adopted in-arc.

I accept mechanisms (β)/(γ)/(δ) as P2-owned substitutes compatible with this arc shape; mechanism (δ) archive-pack-style is overkill for single-claim invalidations.

## Q3 — Artefact progression

| Session | Artefact | Path | State | Key frontmatter |
|---------|----------|------|-------|-----------------|
| 001 | System model v1 | `applications/001-disaster-response/system-model.md` | New | `originating_session: 001` |
| 001 | Assumptions v1 | `applications/001-disaster-response/assumptions.md` | New | `originating_session: 001` |
| 001 | Risk register v1 | `applications/001-disaster-response/risk-register.md` | New | `originating_session: 001` |
| 001 | Response plan v1 | `applications/001-disaster-response/response-plan.md` | New | `originating_session: 001` |
| 002 | Response plan v2 | (canonical revised) | Revised | `last-revised-session: 002` + -v1 preserved |
| 002 | Decision trees v1 | `applications/001-disaster-response/decision-trees.md` | New | `originating_session: 002` |
| 003 | Invalidation log | `applications/001-disaster-response/invalidation-log.md` | New | `originating_session: 003` |
| 003 | Assumptions v2 | (canonical revised) | Revised | `last-revised-session: 003` + -v1 preserved |
| 003 | Response plan v3 | (canonical revised) | Revised | `last-revised-session: 003` + -v2 preserved |
| 003 | Risk register v2 | (canonical revised) | Revised | `last-revised-session: 003` |
| 003 | Decision trees v2 | (canonical revised) | Revised | `last-revised-session: 003` |
| 004 | System model v2 | (canonical revised, recovery-horizon extension) | Revised | `last-revised-session: 004` |
| 004 | Recovery plan v1 | `applications/001-disaster-response/recovery-plan.md` | New | `originating_session: 004` |
| 004 | Risk register v3 | (canonical revised) | Revised | `last-revised-session: 004` |
| 004 | Invalidation log append | (canonical extended) | Revised | `last-revised-session: 004` |
| 005 | Retrospective | `applications/001-disaster-response/retrospective.md` | New | `originating_session: 005` |
| 005 | Engine-feedback synthesis | `applications/001-disaster-response/engine-feedback-synthesis.md` | New | `originating_session: 005` |
| 005 | Engine-feedback outbox files | `engine-feedback/EF-005-*.md` (multiple) | New | Per workspace-structure.md v5 §engine-feedback schema |

**Sealed at originating session (provenance-immutable per D-017):** each session's `00/01X/01/02/03-*.md`; the operator-delivered `session-NNN-brief.md` reveal (sealed once session opens).

**Mutable across sessions (`applications/` canonical-path-revised pattern per workspace-structure.md §applications + Session 013 D-066 precedent):** system-model, assumptions, risk-register, response-plan, decision-trees, invalidation-log, recovery-plan. Prior versions preserved as `-v1.md`, `-v2.md` in place next to canonical.

**Only-in-self-dev:** `arc-plan-master.md` (the deliberation's product); any operator notes about the intended invalidation sequence. The external workspace must not see these.

## Q4 — Validation approach per session

**Per-session shape:** three-perspective MAD by default.
- **Response Planner** (Claude subagent) — forward-looking plan content.
- **Stakeholder Stand-in** (Claude subagent with stance brief anchoring in affected-population constraints) — the arc's stakeholder-simulation per §2 of the brief.
- **Adversarial Skeptic** (Claude subagent) — challenges assumptions, red-teams plan.

**Non-Claude participation at S003 and S005** (adds Codex/GPT-5.5 via `codex exec`, bringing count to 4). S003 because invalidation-handling is high-stakes and cross-family reduces framing bias at the pivot; S005 because retrospective + engine-feedback synthesis benefits from outsider reframing on what surfaces were substantively vs. ceremonially exercised. S001/S002/S004 default 3-Claude unless an in-session d023_N trigger fires (none expected; external applications don't modify the kernel).

**Kernel §7 senses per session (v6):**
- **Workspace validation:** `validate.sh` per session (D-142 bootstrap provides infrastructure). Aggregate-budget monitoring per `read-contract.md` v4 §2b.
- **Domain validation:** **not available** — fictional scenario; no practitioner. Pre-declared scope.
- **Provisional reference substitute:** **N/A** — no public-domain reference matches this compound fictional scenario; three-cell protocol in `reference-validation.md` v3 cannot run. **This is a deliberate engine-surface exercise — see Q5 Surface 1.**

**Fallback qualitative-multi-agent criteria** (what fills the §7 void), recorded explicitly in each session's `02-decisions.md`:
1. **Internal coherence** — produced artefacts don't contradict each other within the session.
2. **Cross-artefact consistency** — session's artefacts consistent with un-invalidated prior-session artefacts; explicitly inconsistent (with invalidation-log cross-reference) with invalidated ones.
3. **Adversarial coverage** — standing MAD v4 requirement; one perspective argues against consensus; decisions record what was argued and why adopted-or-not.
4. **Stakeholder-simulation plausibility** — stand-in objections recorded verbatim; overridden objections name the tradeoff.

**Case Steward synthesiser placement:** separate Claude orchestrator per session, not a deliberation perspective. Performs factual checks independently, writes `01-deliberation.md`, authors `02-decisions.md`. S005 additionally authors `engine-feedback-synthesis.md` and drafts `engine-feedback/EF-NNN-*.md` outbox files. Matches self-dev S036-S046 pattern.

## Q5 — Feedback-yield optimisation (primary target)

### Five engine surfaces this arc deliberately exercises

**Surface 1 — Kernel §7 three-sense under-specification when Domain is unavailable and Reference is N/A.**
- Which Q1-Q4 exercises it: Q4's validation-approach. No domain-actor (fictional); three-cell reference protocol N/A (no public-domain reference for this scenario). Fallback qualitative-multi-agent criterion set is standing practice but not a codified §7 sense.
- Draft feedback file: `EF-005-kernel-section-7-fallback-sense-uncodified.md`. Summary: "Kernel §7 names three senses; when Domain unavailable and Provisional-reference-substitute N/A, fallback behaviour (qualitative multi-agent coherence) ran as standing practice across five external sessions without being a named §7 sense or carrying citation discipline."
- Engine property: **unclear spec + missing affordance.** Candidate for substantive kernel §7 revision (new named sense = new normative content; OI-002 substantive classification).

**Surface 2 — Retroactive invalidation + D-017 immutability under multi-session evolving artefact state.**
- Which Q1-Q4 exercises it: Q2's designated invalidation events at S003/S004 + Q3's canonical-path-revised-with-supersession mechanics + `invalidation-log.md` creation.
- Draft feedback file: `EF-003-d017-retroactive-invalidation-mechanism-underspecified.md`. Summary: "D-017 bars editing closed-session provenance; `workspace-structure.md` v5 §applications permits mutable-external-artefact revision with -v1 preservation; neither spec codifies how to record retroactive *claim-level* invalidation of a prior-session artefact with a standing cross-reference log. Ad-hoc pattern used in S003 (invalidation-log + supersession-marker) worked but is uncodified."
- Engine property: **missing affordance.** Candidate for minor workspace-structure.md amendment (codify invalidation-log) or substantive OI-state-machine amendment (new "constraint-invalidated" state) — classification depends on P2's specific mechanism.

**Surface 3 — MAD v4 minority-preservation across arc with constraint invalidation.**
- Which Q1-Q4 exercises it: Q4's per-session MAD + the guaranteed invalidation events.
- Specific scenario expected: At S002, Adversarial Skeptic raises concern that S002's plan assumes water-restoration ≤7 days. Concern preserved as first-class minority per MAD v4 §Preserve Dissent. At S003, operator reveals water contamination is worse than assumed (designated invalidation A). S003 faces: is the S002 minority (a) **vindicated** (concern proved right), (b) **obsoleted** (invalidation went further than minority warned, making specific claim moot), or (c) **preserved unchanged** (historical claim about S002 decisions stands even as constraint state shifts)?
- Draft feedback file: `EF-003-minority-preservation-under-constraint-invalidation.md`. Summary: "MAD v4 §Preserve Dissent specifies preservation with activation warrants but does not address how a minority's status evolves when an assumption underlying its warrant is invalidated by a subsequent session's constraint-update. Needs a third possible transition (invalidated) distinct from activated and preserved-unactivated."
- Engine property: **load-bearing gap.** Adjacent to OI-019 sub-question (b) activation-warrant expiration windows, but distinct — (b) is time-based, this is constraint-based.

**Surface 4 — Read-contract aggregate-budget dynamics in a fast-growing external workspace + engine-feedback outbox first live use.**
- Which Q1-Q4 exercises it: Q1's 5-session arc + Q3's accumulating artefact set + Q4's deliberation provenance growing each session.
- Expected pressure: by S005, external workspace aggregate = 5 session closes (no §2c rotation within the arc; 6-session window unfired) + ~7 active artefacts (~15-30K words at mid-arc) + 5 archive-surface `01-deliberation.md` frequently read-by-reference during S003-S005. Projected S005-open aggregate 40-65K words — within §2b soft (90K) but with observable trajectory. Arc also produces first live engine-feedback outbox records (bootstrapped at S046 D-142 but unused until this arc).
- Draft feedback file: `EF-005-external-workspace-aggregate-budget-trajectory.md`. Summary: "A 5-session arc grew external-workspace aggregate from ~5K at S001 open to ~[measured] at S005, with close-rotation unfired because all five closes remain within the 6-session window; per-session growth rate suggests 10+-session arcs would cross §2b soft before rotation begins."
- Engine property: **rigid-convention observation + first-use data point.** Not a demand for spec change from this observation alone (would be scope-creep per §7 of brief anti-laundering); feeds OI-019 sub-question (f) extended-baseline visibility and §10.4-M5 Reviser OI-tag-only feedback-pathway activation-pending watchpoint.

**Surface 5 — Hidden-scenario / partial-view scope handling per §2.5.**
- Which Q1-Q4 exercises it: Q1's placement option (a) — external sessions see only per-session reveals.
- Draft feedback file: `EF-001-or-EF-002-partial-view-session-done-ness-detection.md`. Summary: "Kernel §1 Read + `prompts/application.md` §Read assume session scope is fully readable at session-open; under partial-view the session cannot distinguish 'my scope is complete' from 'next session's reveal will include additional scope I don't yet see'; S001's close criteria became ambiguous. MAD-within-partial-view also stresses the question of whether strong convergence on assumptions invalidated in S003 is vindication-of-MAD-under-uncertainty or a signal that MAD's context assumptions are too strong."
- Engine property: **wrong abstraction + new-class observation.** Candidate for substantive kernel §1 or §9 Close amendment (changes normative closure criteria). Directly addresses §2.5.4 of the brief.

Five surfaces, exceeding the ≥3 threshold for P1 per §5a and §7.

### Engine surface deliberately NOT targeted

**Engine-v bump-trigger criteria / OI-018.** The arc does not exercise `engine-manifest.md` §5 bump-trigger logic. The external application loads the engine read-only per `prompts/application.md`; injecting synthetic self-dev-like kernel-revision decisions into the arc would distort its purpose. OI-018 is better exercised in a dedicated self-dev MAD session. I stay off this surface so the arc's 5-session scope remains focused.

Explicit secondary non-targets (not load-bearing): OI-004 closure machinery (closed at S041); `reference-validation.md` v3 three-cell protocol (no reference case available — that's the Surface 1 void, not a separate exercise); `validate.sh` check-23 MODE.md-presence stress-test (implicitly exercised, not stressed).

## Confidence and limits

**Confident:** 5-session shape; designated-invalidation structure at S003/S004; artefact progression table; placement option (a); five feedback surfaces identified with specific Q-answer sources.

**Less confident:**
1. **Scenario scaffolding specifics.** Compound storm+power+water is defensible but not uniquely determined. Alternative scaffolds (technological-disaster + social-unrest; pandemic-tail + infrastructure-degradation) might exercise the same surfaces equivalently. Defer to synthesis if P2/P3/P4 propose a better scaffold hitting the same surfaces.
2. **Session count 5 vs. 4.** I chose 5 to preserve standalone retrospective. If P2/P4 argue 4-with-folded-retrospective exercises the same surfaces, I accept 4.
3. **Mechanism (α) vs. (β)/(γ)/(δ) for D-017 invalidation.** I proposed (α) as the arc-level slot; P2 owns the mechanism in detail. Any of (β)/(γ)/(δ) substitutes into my arc shape without modification.
4. **Surface 4 strength.** Weakest of the five — produces a data point, not a gap-surfacing event. If P3/P4 argue for a stronger replacement, I accept.

**Assumed:** operator-injected T0 reveals are interpretable by external Case Stewards as session-briefs without additional engine support (MODE.md-routed `prompts/application.md` execution suffices); fictional-no-domain-actor clause is stable across all 5 sessions (operator does not introduce a domain-actor mid-arc, which would change validation-approach mid-arc).

**OI-002 classification for implied spec amendments my design forecasts (none proposed for adoption this session):**
- New "constraint-invalidated" OI state (if P2 proposes): **substantive** (new state transition = new rules + new required fields).
- `invalidation-log.md` pattern at workspace-structure.md §applications: **minor** (codifies operational pattern; no new rules/fields/triggers/artefacts beyond §applications).
- Fourth §7 sense for qualitative-multi-agent fallback (if Surface 1 feedback adopted): **substantive** (new named §7 sense = kernel expansion).

**§5.6 transparency:** both non-Claude seats this S047 are Codex/GPT-5.5 per operator S044 R2 standing preference; §5.6 GPT-family-concentration worst-case-side data point continues. Spirit-level sustained-exercise question remains open per S045 §6 carry-forward.

**WX-35-1 file-edit claim discipline:** My design names specific external-workspace files expected to be produced/edited by executing sessions: `applications/001-disaster-response/{system-model,assumptions,risk-register,response-plan,decision-trees,invalidation-log,recovery-plan,retrospective,engine-feedback-synthesis}.md`, plus multiple `engine-feedback/EF-NNN-*.md`. These claims are concrete and verifiable via `git log` after arc execution; if the executing sessions do not produce these files at these paths, WX-35-1 fires at self-dev review of arc outcomes.
