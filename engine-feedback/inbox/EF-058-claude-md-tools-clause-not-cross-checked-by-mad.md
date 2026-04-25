---
feedback_id: EF-058-claude-md-tools-clause-not-cross-checked-by-mad
source_workspace_id: selvedge-self-development
source_session: 058
created_at: 2026-04-25T18:00:00Z
reported_by: operator
target: methodology
target_files:
  - specifications/multi-agent-deliberation.md
  - specifications/methodology-kernel.md
  - CLAUDE.md
severity: observation
status: inbox
---

# EF-058 — CLAUDE.md tools clause not cross-checked by S050 MAD (methodology observation; shared-frame-blindness data point)

## Observation

CLAUDE.md §Tools (added by D-144 Session 046, content present at workspace root since at least S046 close) states:

> "This contains usage instructions for tools you have requested. If you decide more are needed, you can install them using `uv tool` or ask the user to ratify your tool decision and install something on your behalf."

The S050 4-perspective two-family MAD on EF-047-retrieval-discipline (P1 Substrate Architect + P2 Incrementalist Skeptic Claude + P3 Outsider Frame-Completion + P4 Cross-Family Reviewer Codex/GPT-5.5) deliberated phase-1 substrate adoption + bootstrap contract + external-application portability across Q1-Q8 + cross-family laundering audit. The synthesis (`provenance/050-session/01-deliberation.md` §2.7 + §1 Q7) landed on **pip + venv** for runtime install + bootstrap (`tools/bootstrap-external-workspace.sh` prints `pip install 'mcp[cli]' pyyaml` instructions; `.mcp.json` declares `"command": "python3"` system invocation; `.cache/venv/` built at S051 D-178 substrate-first-real-use). **`uv` was not surfaced as the alternative anywhere in the deliberation surface or in P4's audit.** Per the laundering-audit role's brief at `provenance/050-session/01d-perspective-cross-family-reviewer.md`, P4 audited P1+P2 for: criteria-strain selectivity, revision traceability, cross-session precedent neutrality, internal inconsistency, measurable-criteria adequacy, shared-frame-blindness — **but did not check the decision against operator standing instructions in CLAUDE.md.**

This is engine-conventional behaviour: the MAD perspectives' shared brief (`multi-agent-deliberation.md` v4 §Stance Briefs §1 methodology-context) names `methodology-kernel.md` + `engine-manifest.md` + `identity.md` etc. as load-bearing context, but does NOT name CLAUDE.md as load-bearing context. Operator standing instructions live in CLAUDE.md as a per-workspace identity-class file (workspace-structure.md v7 §file classes); they are not engine-definition; they were not part of the MAD's reading discipline.

The result: pretraining-dominant pip+venv pattern overrode the operator's specified `uv` direction. The drift was not malicious; it was unaudited. This is what `EF-058-substrate-runtime-uv-migration-recommended-path.md` (filed separately as the operational fix) tracks at the implementation layer; this record tracks the methodological observation about the discipline gap that allowed the drift.

## Why It Matters

1. **CLAUDE.md is load-bearing operator guidance, currently treated as advisory.** Operator standing instructions affect tooling, conventions, anti-patterns, and per-workspace policies. They sit between methodology-kernel (engine-definition) and per-session decisions (provenance). The engine has been treating them as a kind of decoration the harness consults, rather than as input the methodology's deliberation discipline must respect.

2. **Shared-frame-blindness expansion.** P4's role-stance brief at S050 specifically tracked "shared assumptions across P1+P2+P3 perspectives." But the operator's instructions are a different shared-frame layer — one that ALL Claude perspectives default to ignoring because they emerge from harness-time instruction-injection rather than from in-conversation deliberation. The S058 post-session discussion's identification of the drift is operationally a Cause-3 corroborating-evidence data point: cross-family contribution surfaced what Claude perspectives missed not because perspectives were wrong about substrate engineering but because *no perspective read the operator's standing instructions before reasoning*. The blind spot is the methodology's, not P1/P2/P3/P4's individually.

3. **§10.4-M13 (P3+P4 shallow-Direction-A warning) is adjacent to this concern.** That minority watches whether structured-records-as-source-of-truth discipline holds in practice. The deeper question — whether the methodology's discipline genuinely respects operator authority — is structurally similar: the engine can ratify discipline-shaped artefacts without verifying the discipline holds against the standing instructions the operator wrote.

4. **Future MAD substrate-adjacent decisions risk the same drift.** Next session's mirrored-minority migration (phase-2 per `records-contract.md` v1 §6 phase-2 gate) is a substrate-adjacent implementation decision. If S059's MAD (or single-orchestrator implementation) doesn't cross-check against CLAUDE.md, the same pattern recurs at smaller scale. n=1 is observation; n=2 in close adjacency is a methodology hole.

## Suggested Change

**Defer scoping to a future deliberation; do not resolve at S059.** This is observation-class; substantive resolution requires a MAD or operator-directed-resolution. Possible directions for that future deliberation:

(a) **MAD §Stance Briefs §1 methodology-context amendment** — extend the shared-context enumeration to include CLAUDE.md (workspace-identity class) when the workspace has one. Concrete: add to `multi-agent-deliberation.md` v4 §Stance Briefs §1 a clause "Briefs include the workspace's CLAUDE.md content as part of methodology context, treated as operator standing instructions of decision-relevant standing." Minor per OI-002 if no kernel touch; substantive if extends to kernel §Convene.

(b) **Kernel §Convene amendment** — add a Convene-time obligation to surface operator standing instructions that bear on the deliberation surface. Concrete: amend `methodology-kernel.md` v6 §3 Convene with text like "Convening identifies any operator standing instructions in CLAUDE.md that bear on the deliberation's scope and ensures they enter the perspectives' shared brief." Substantive per OI-002; engine-v bump.

(c) **Workspace-structure.md operator-instruction class enumeration** — formalise CLAUDE.md as workspace-identity class with operator-standing-instructions sub-classification (currently it's classified as "Workspace-identity files" alongside MODE.md per workspace-structure.md v7 §file classes, but no machinery treats CLAUDE.md content as deliberation input). Substantive; engine-v bump.

(d) **Defer until n=2 instances surface** — adopt observation-only stance; if a second clear instance of CLAUDE.md drift surfaces in S059-S064, escalate to substantive deliberation. Anti-laundering: the threshold should be "drift caused operational damage at substantive deliberation," not "drift was identified post-hoc"; without that threshold, the watchpoint becomes unfalsifiable.

(e) **Combination (a)+(d)** — adopt minor (a) preemptively; defer substantive (b)/(c) until evidence accumulates.

The deliberation that picks among these (or surfaces a (f) reframe) should itself respect this concern by reading CLAUDE.md as part of its shared brief — proving the discipline by exercising it.

## Evidence

- **CLAUDE.md §Tools clause** (workspace root; per D-144 Session 046 + standing through S058): specifies `uv tool` as install mechanism.
- **S050 deliberation `provenance/050-session/01-deliberation.md` §1 Q5-Q7 + §2.7**: pip+venv adopted; uv not mentioned anywhere in synthesis or perspectives.
- **`provenance/050-session/01a-perspective-substrate-architect.md`** through **`01d-perspective-cross-family-reviewer.md`**: full search of perspective files reveals zero `uv` mentions. Pretraining-default pattern.
- **P4 laundering-audit role brief** (`provenance/050-session/01d-perspective-cross-family-reviewer.md`): audited cross-session precedent + criteria-strain selectivity + measurable-criteria adequacy + shared-frame-blindness. Did not include CLAUDE.md cross-check in audit scope.
- **`multi-agent-deliberation.md` v4 §Stance Briefs §1 Methodology context**: enumerates `methodology-kernel.md`, `engine-manifest.md`, `identity.md` as shared-context spec sources; does NOT enumerate CLAUDE.md or operator-standing-instructions as a separate context category.
- **S058 post-session discussion** (operator-identified drift): "I think at some point python3 started to be used instead of uv, which is specified in the CLAUDE.md file. Using that first might have avoided all this venv mess." Post-S058-close.

## Application-Scope Disposition

Self-dev-originated. Operator-surfaced post-session intake (S058-post-session discussion). Direct-to-inbox per `engine-feedback/INDEX.md` Note-on-direct-to-inbox-placement convention. `source_workspace_id: selvedge-self-development` accurately reflects self-dev origin. `reported_by: operator` reflects operator-surfacing channel.

Severity `observation` (not friction; not blocker): the operational symptom is tracked separately at `EF-058-substrate-runtime-uv-migration-recommended-path.md`. This record tracks the methodological pattern that allowed the operational symptom to emerge unaudited. The pattern is a discipline gap; resolving the operational symptom does not resolve the pattern; future MAD-class decisions could reproduce the drift in different shapes.

Triage scheduled S059+, but **NOT recommended for same-session resolution**. Substantive scoping (which of (a)-(e) directions, or surfacing (f)) requires a MAD with cross-family adversarial coverage; per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required, this falls under d016_2 (creates or substantively revises specifications) if direction (b) or (c); under d016_3 (reasonable-disagreement) regardless. Recommended path-shape: **classify substantive at triage; defer to dedicated MAD session per S048 D-155 / S049 D-159 / S050 D-172 / S057 D-196 substantive-arc deliberation pattern chain.** OR: classify observation-with-deferred-substantive-scope; let evidence accumulate before scheduling.

If S059 default-agent state encounters this record + EF-058-uv-migration record, the recommended sequence is:
1. Triage EF-058-uv-migration as defect-fix-shape Path T+L; resolve same session.
2. Triage EF-058-claude-md-drift as substantive-arc-shape; defer to dedicated future MAD or apply (d)/(e) hybrid evidence-accumulation discipline.

If the operator surfaces preference for direction (a)+(d) hybrid at S059, the (a) minor amendment to `multi-agent-deliberation.md` v4 §Stance Briefs is single-orchestrator-tractable per S048 D-153 precedent (operator-directed-resolution); engine-v10 → v10.minor or v11 candidate per OI-002 heuristic.

Forward observation: the broader question — whether engine-conventional MAD discipline should cross-check operator standing instructions — likely surfaces additional adjacent observations as the workspace continues to operate. This record opens the inquiry rather than closing it.
