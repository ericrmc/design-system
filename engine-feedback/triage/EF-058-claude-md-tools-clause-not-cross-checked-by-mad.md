---
triage_id: EF-058-claude-md-drift-triage
feedback_ref: ../inbox/EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md
triaged_in_session: 059
triaged_at: 2026-04-25
status: triaged
classification: substantive-arc
opened_issue: null
resolved_by: null
disposition: Classified substantive-arc-shape; deferred to dedicated future MAD session per intake disposition; operator-stated "NOT recommended for same-session resolution" honoured. Substantive resolution requires deliberation between candidate directions (a)-(e) which include MAD §Stance Briefs §1 amendment / kernel §Convene amendment / workspace-structure operator-instruction class enumeration / defer-until-n=2 evidence-accumulation / combination (a)+(d). The deliberation that picks among these (or surfaces a (f) reframe) should itself respect this concern by reading CLAUDE.md as part of its shared brief.
decision_records:
  - D-208
engine_version_impact: deferred (engine-v10 preserved at S059 triage; future substantive-arc resolution may produce engine-v11 candidate per direction adopted)
direction_selected: deferred
alternative_directions_deferred:
  - direction: (a) MAD §Stance Briefs §1 methodology-context amendment (extend shared-context enumeration to include CLAUDE.md when workspace has one) — minor per OI-002 if no kernel touch; substantive if extends to kernel §Convene
  - direction: (b) Kernel §Convene amendment (add Convene-time obligation to surface operator standing instructions that bear on deliberation surface) — substantive per OI-002; engine-v bump
  - direction: (c) Workspace-structure.md operator-instruction class enumeration (formalise CLAUDE.md as workspace-identity class with operator-standing-instructions sub-classification) — substantive; engine-v bump
  - direction: (d) Defer until n=2 instances surface (observation-only stance; if a second clear instance of CLAUDE.md drift surfaces in S059-S064, escalate to substantive deliberation)
  - direction: (e) Combination (a)+(d) — adopt minor (a) preemptively; defer substantive (b)/(c) until evidence accumulates
---

# Triage — EF-058 CLAUDE.md tools clause not cross-checked by S050 MAD

## Classification

**Target**: methodology (MAD shared-frame discipline; kernel §Convene; workspace-structure operator-instruction class). **Severity on inbox record**: observation (not friction; not blocker; the operational symptom is tracked separately at EF-058-uv-migration; this record tracks the methodological pattern that allowed the operational symptom to emerge unaudited). **Source**: `selvedge-self-development` Session 058 post-session operator-surfaced observation (`reported_by: operator`); recorded as direct-to-inbox per S054/S055 self-dev-originated convention.

**Disposition**: **triaged-deferred** at S059. Substantive-arc-shape per intake disposition; defer to dedicated future MAD session per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required (d016_2 if direction (b) or (c) adopted; d016_3 reasonable-disagreement applies regardless). Operator-stated at intake: "NOT recommended for same-session resolution."

## Pattern summary (from inbox record)

CLAUDE.md §Tools (added by D-144 Session 046) states: "If you decide more are needed, you can install them using `uv tool` or ask the user to ratify your tool decision and install something on your behalf." The S050 4-perspective two-family MAD on EF-047-retrieval-discipline (P1 Substrate Architect + P2 Incrementalist Skeptic Claude + P3 Outsider Frame-Completion + P4 Cross-Family Reviewer Codex/GPT-5.5) deliberated phase-1 substrate adoption + bootstrap contract + external-application portability + cross-family laundering audit. The synthesis (`provenance/050-session/01-deliberation.md` §2.7 + §1 Q7) landed on **pip + venv** for runtime install + bootstrap. **`uv` was not surfaced as the alternative anywhere in the deliberation surface or in P4's audit.** Per the laundering-audit role's brief at `provenance/050-session/01d-perspective-cross-family-reviewer.md`, P4 audited P1+P2 for: criteria-strain selectivity, revision traceability, cross-session precedent neutrality, internal inconsistency, measurable-criteria adequacy, shared-frame-blindness — **but did not check the decision against operator standing instructions in CLAUDE.md.**

This is engine-conventional behaviour: the MAD perspectives' shared brief (`multi-agent-deliberation.md` v4 §Stance Briefs §1 methodology-context) names `methodology-kernel.md` + `engine-manifest.md` + `identity.md` etc. as load-bearing context, but does NOT name CLAUDE.md as load-bearing context. Operator standing instructions live in CLAUDE.md as a per-workspace identity-class file (workspace-structure.md v7 §file classes); they are not engine-definition; they were not part of the MAD's reading discipline.

The result: pretraining-dominant pip+venv pattern overrode the operator's specified `uv` direction. The drift was not malicious; it was unaudited. The operational fix is at `EF-058-substrate-runtime-uv-migration-recommended-path.md` (resolved S059 D-207); this record tracks the methodological observation about the discipline gap.

## Deferral rationale

The intake explicitly recommends NOT same-session resolution; classification substantive-arc-shape. Rationale per intake §Suggested Change:

1. **Substantive scoping requires a MAD with cross-family adversarial coverage.** The substantive directions (b)/(c) extend kernel §Convene or workspace-structure file-class definitions; per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required, this falls under d016_2 (substantive spec revisions). Direction (a) alone may be minor per OI-002; combined with (b)/(c) is substantive.

2. **Reasonable-disagreement on direction.** Five candidate directions (a)-(e) range from minor amendment to engine-v bump. Cross-family deliberation is appropriate to surface which is right; single-orchestrator forecloses without cross-family cover. Per d016_3 (reasonable-disagreement) trigger.

3. **Bootstrap-paradox feature.** Per intake §Suggested Change closing paragraph: "The deliberation that picks among these (or surfaces a (f) reframe) should itself respect this concern by reading CLAUDE.md as part of its shared brief — proving the discipline by exercising it." S059's resolving session triage cannot itself exercise the discipline being deliberated; the dedicated MAD must.

4. **Cross-linkage with EF-058-tier-2-validation.** Per EF-058-tier-2-validation §Why It Matters point 3: "EF-058-claude-md-drift class — Tier 2 / MAD shared-frame-blindness against operator-standing-instructions" is one of the concrete instances the meta-pattern subsumes. The substantive-arc resolutions for both records may be co-scheduled (single design-space.md surfaces joint scope) per EF-058-tier-2-validation §Suggested Change open-question 6: "Cross-linkage to EF-058-claude-md-drift: both records concern shared-frame-blindness against operator-standing-instructions. Should the MAD's shared brief read CLAUDE.md as part of methodology-context (per EF-058-claude-md-drift suggested change (a)+(b))? If yes, the reviewer's brief should also."

## Scope and arc shape (planned; for the dedicated session(s) to ratify)

The intake names five candidate directions (a)-(e). Concrete planned shape (subject to operator agenda + dedicated MAD's own ratification):

- **Phase 1 — synthesis / design-space session** (Path AS Shape-1 per S057 EF-055 precedent). Surveys directions (a)-(e) + alternative architectures + combination shapes + interaction with EF-058-tier-2-validation directions (α)-(ε). Possible joint design-space.md covering both records' substantive arcs if scope-coherent. Engine-v preserved (synthesis-only is non-bumping per S057 / S049 D-157 precedent).
- **Phase 2 — MAD session** (Path AS-MAD-execution per S050 / S058 4-perspective two-family lineup precedent). Likely 2 Claude + 2 Codex/GPT-5.5 per D-133 M2 lineage-constraint matrix. Cross-family essential because the question is "what cross-family discipline should apply at MAD shared-brief level" — Claude-only deliberation has the same shared-frame-blindness the question investigates. Composition candidates: Substrate / Conservator / Outsider non-Claude / Cross-Family Reviewer non-Claude (mirroring S058 lineup). Adopts a direction; engine-v11 candidate if direction (b) or (c) adopted; minor if direction (a) alone; no engine-v change if direction (d) defer adopted.
- **Phase 3 — adoption** (substantive spec edits per direction adopted). Possible touches: `multi-agent-deliberation.md` v4 §Stance Briefs (extend §1 methodology-context enumeration); `methodology-kernel.md` v6 §Convene (add operator-standing-instruction obligation); `workspace-structure.md` v7 §file classes (formalise operator-standing-instruction sub-class).

## Direction-specific scheduling notes

- **Direction (a) MAD §Stance Briefs §1 amendment alone**: minor per OI-002 if no kernel touch. Single-orchestrator-tractable per S048 D-153 precedent (operator-directed-resolution). Engine-v10 preserved.
- **Direction (b) Kernel §Convene amendment**: substantive per OI-002. Engine-v11 candidate. MAD-required per d016_2.
- **Direction (c) Workspace-structure.md operator-instruction class enumeration**: substantive. Engine-v11 candidate. Compatible with (a) and (b) as super-set or as paired adoption.
- **Direction (d) Defer until n=2**: no spec edit; observation-only stance; activation warrant fires at n=2 instances of CLAUDE.md drift in S059-S064 window.
- **Direction (e) Combination (a)+(d)**: minor (a) preemptive + substantive (b)/(c) deferred to evidence-accumulation. Compromise direction; preserves operator-stated standing while leaving room for stronger evidence-driven resolution.

## Forward-dependency observations

- **n=1 currently surfaced** (the S050 MAD pip+venv vs CLAUDE.md uv drift). Direction (d) defer-until-n=2 stance is internally consistent with engine's preserved-minority-activation discipline; cumulative-evidence threshold is an engine-conventional shape.
- **Joint scope with EF-058-tier-2-validation likely**: both records concern shared-frame-blindness against operator-standing-instructions. The dedicated phase-1 synthesis session may produce a joint design-space.md if scope-coherence is judged adequate.
- **§10.4-M13 (P3+P4 shallow-Direction-A warning) is adjacent**: per intake §Why It Matters point 3, the question of whether discipline genuinely respects operator authority is structurally similar to whether structured-records-as-source-of-truth holds in practice. The dedicated MAD may consider whether direction (a)-(c) and §10.4-M13 share resolution paths.
- **EF-058-tier-2-validation operator-stated MAD preference**: Per EF-058-tier-2-validation `reported_by: operator` + intake §Application-Scope Disposition: "NOT recommended for same-session resolution per operator preference at intake ('should go through MAD')." That MAD preference may also apply to this EF-058-claude-md-drift record (the operator's filing-context is shared); explicit MAD preference for this record is implicit per cross-linkage (open-question 6 in EF-058-tier-2-validation intake) but not literally stated for this record.

## Cross-references

- **Inbox record**: `engine-feedback/inbox/EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` (preserved verbatim).
- **Decision authorising this triage**: `provenance/059-session/02-decisions.md` D-208.
- **Operational-fix-pair**: `engine-feedback/inbox/EF-058-substrate-runtime-uv-migration-recommended-path.md` (resolved S059 D-207).
- **Meta-pattern record**: `engine-feedback/inbox/EF-058-tier-2-validation-discipline-by-distinct-agent.md` (substantive-arc-deferred per S059 D-209; subsumes both this record and EF-058-uv-migration as concrete instances).
- **CLAUDE.md §Tools operator standing instruction**: workspace root; per D-144 Session 046.
- **Pattern-arc precedent (substantive arc class)**: EF-047-retrieval-discipline → S049 design-space (D-157/D-158/D-159) → S050 4-perspective MAD → engine-v9 + retrieval-contract.md v1; EF-055-substrate-aware-format-and-archive-rethink → S057 design-space (D-194/D-195/D-196) → S058 4-perspective MAD → engine-v10 + records-contract.md v1.
- **Origin-source S050 deliberation**: `provenance/050-session/01-deliberation.md` §1 Q5-Q7 + §2.7 (pip+venv adoption); `01d-perspective-cross-family-reviewer.md` (P4 laundering-audit role; did not include CLAUDE.md cross-check).

## OI impact

No OI opened at S059 triage. The substantive-arc resolution may open OI for tracking the discipline-gap-resolution if direction (d) (defer-until-n=2) is adopted alone, or may be subsumed within direction (a)/(b)/(c) spec edits.

## Subsumed deferred candidates

None. S047 D-150 three remaining deferred candidates (i)/(ii)/(iii) unchanged.
