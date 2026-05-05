---
title: Arc-Plan v1 — regional-bank agentic-platform pilot (selvedge external-application trial #2)
authoring_session: 207
authoring_decision: DV-S207-1
date: 2026-05-05
status: active
external_workspace_pending: /Users/ericmccowan/Development/selvedge-regional-bank-agents (to be bootstrapped at S208 self-dev)
preceded_by: applications/106-disaster-response-arc/arc-plan.md (first external-application trial; closed at S162)
preceded_by_decision: DV-S206-1 (immediately prior; closes OI-S205-1 test-infra refactor)
visibility: operator-only — do NOT copy into external workspace default-read surface; brief.md is the external-visible orientation anchor
---

# Arc-Plan v1 — regional-bank agentic-platform pilot

## §1 Purpose

This is the authoritative arc-plan for executing the engine-v59 Selvedge engine against the **second external-problem trial**. The trial runs in a freshly-bootstrapped external workspace (path TBD at S208 self-dev). The arc commits to **6 sessions**, scoped per the S207 codex shape-consult (EF-S207-1) and DV-S207-1 supports.

This arc is **not** a domain-coverage exercise. The disaster-response arc (106-/S106-S162) tested *stakeholder events under uncertainty* against a single domain. This arc tests *constraint-density and contested decisions under adversarial review* against a domain whose authority structure is naturally multi-source: regulation + framework + contract + internal policy + market norm.

### §1.1 Hypothesis under test

Selvedge's typed primitives (assumption_ledger, decision_v2 with supports + alternatives, supersession_ledger, cycle_ledger, event_ledger, chain-walks) **are well-suited** to enterprise systems work where:

- Multiple authoritative sources bind a single decision.
- Decisions are revisited under audit pressure years later.
- Contested trade-offs benefit from multi-perspective deliberation.
- Constraints link in non-obvious ways the chain-walk surfaces.

The arc fails its purpose if it produces design artefacts but no friction signal — friction IS the load-bearing output. Specifically: the missing primitives identified pre-arc (typed `requirement_ledger`; stakeholder registry distinct from stakeholder *events*; traceability-export adapters) MUST be felt by S006-app for the pilot to count as informative.

### §1.2 Operator role

Operator is hands-off across the arc; the orchestrator (Claude Code, in the external workspace) plays all stakeholder roles via the perspective-convening machinery. Operator transports per-session inputs from this arc-plan into the external workspace and runs `bin/selvedge monitor-external harvest-ef` after each external session closes to ferry engine_feedback rows back to self-dev.

### §1.3 Friction-yield criteria

The arc IS informative if at least the following surface as engine_feedback during the external-side run:

- (F1) At least one calibration EF naming a primitive that *should exist but doesn't* (typed `requirement_ledger` is the most likely; alternatives: `stakeholder_registry`, `traceability_export`, `risk_register`).
- (F2) At least one calibration EF naming a refusal/CHECK/T-NN that fires usefully (catches a real footgun).
- (F3) At least one calibration EF naming a refusal/CHECK/T-NN that fires *harmfully* (blocks a sensible operation; pure ceremony).
- (F4) At least one calibration EF naming the `ledgerized-vagueness` failure mode in the wild (per AR-S207-1) — broad reg recorded as assumption with no concomitant typed decision.
- (F5) Per-session cost in CLI calls / token budget / wall time vs disaster-response arc baseline.

The arc is **uninformative** if it produces 6 sessions of clean substrate with zero (F1)-(F4) signals — that means perspectives collapsed to one narrator, regs got recorded as platitudes, and no one tested the engine against real adversarial trade-offs.

## §2 Scenario at T0 — what external S001 will see

### §2a Setting (canonicalized in brief.md §2)

**Mercer Valley Bancorp** (fictional), a US nationally-chartered commercial bank, ~$32B in assets, ~120 retail branches across four mid-atlantic states, plus a small commercial-banking arm serving regional manufacturers and a wealth-management subsidiary. Deposit-funded, no investment-bank arm. National Bank Act charter; OCC primary supervisor; FDIC insurance; FRB membership. CRA outstanding rating last cycle. Subject to:

- BSA/AML/KYC/CIP/OFAC for customer onboarding and ongoing monitoring
- Reg E for electronic-fund-transfer error/dispute handling (consumer accounts)
- Reg Z + ECOA + FCRA + UDAAP for any agent involvement in lending or adverse-action explanation
- GLBA Title V information-security standards (banking version, not FTC Safeguards)
- OCC Bulletin 2023-17 third-party risk management (model-vendor relationships)
- 12 CFR Part 53 (OCC) computer-security incident notification — 36-hour rule
- Bank Service Company Act (12 USC §1867) examination and notice rights for technology-service providers
- OCC SR 11-7 model risk management as historically applicable; OCC April-2026 update places **genAI/agentic AI outside SR 11-7 scope** — governance must be designed under the resulting ambiguity
- A small EU-domiciled commercial customer book invokes a GDPR-overlay obligation

### §2b The proposal at T0

Mercer Valley's CIO and Head of Retail Banking propose an **agentic-platform pilot** to deploy LLM-backed agents into three customer-facing workflows:

1. **Customer onboarding** — assist new-account applicants through KYC document collection, identity verification, product matching, account opening; agent collects narrative information and invokes specialist back-end systems (BSA/AML scoring, OFAC screening, credit bureau pull) but does not unilaterally adjudicate.
2. **Dispute resolution** — Reg E first-line intake for unauthorized-transfer disputes; agent collects timeline/evidence, opens claim, communicates outcome from human-determined adjudication. Agent does NOT determine merit.
3. **Account-servicing inquiry** — balance, transactions, statements, basic transfers, routing; the lowest-risk lane and the highest-volume one.

The proposal is **not yet approved**. The OCC has been informally notified per the 2023-17 supervisory-expectations posture. Internal stakeholders have raised concerns spanning security, model-risk, third-party risk, customer harm, audit-trail adequacy, and cost. The CRO has asked for a structured architecture-and-governance pilot before approval.

The 6-session pilot's deliverable is a **reference design + governance framework + cost model** that the bank's architecture-review board, model-risk committee, and CCO can collectively read and comment on. Implementation is out of scope.

### §2c What external S001 must NOT see

- This arc-plan (operator-only).
- Friction-yield criteria (F1)-(F5) above — they would bias the agent toward producing the named friction rather than encountering it organically.
- Codex consult content (EF-S207-1 in self-dev substrate, not external substrate).
- The fictional bank name: brief.md uses **Mercer Valley Bancorp** as an in-scenario fact, not as authoring metadata. The agent in S001-app encounters the bank as the world it is operating in.

## §3 Stakeholder perspectives (convening identities)

Per codex Q3 + AR-S207-1 (named persona discipline). Each perspective carries a stance brief sufficient for the orchestrator to convene as that perspective without persona collapse. Perspectives are NOT required for every session — only when a substantive deliberation opens.

| Code | Role | Stance brief (one-line summary; full briefs per-deliberation) |
|------|------|---------------------------------------------------------------|
| P-CISO | Chief Information Security Officer | Containment + auditability + incident-response readiness; pushes deny-by-default and aggressive logging |
| P-CCO | Chief Compliance Officer | Conformance to BSA/Reg E/UDAAP/ECOA; pushes documented control mappings and audit-trail completeness |
| P-CRO | Chief Risk Officer (operational risk) | Aggregate risk appetite + concentration risk + tail-event scenarios; pushes scenario analysis and stop-loss triggers |
| P-LEGAL | Privacy/legal counsel | GLBA + GDPR + state-AG exposure + customer-notice obligations; pushes data-minimization and retention discipline |
| P-MRM | Model-risk management lead | Validates models pre-deployment; navigates SR 11-7 scope ambiguity for genAI; pushes challenger-model and back-testing discipline |
| P-VRM | Third-party / vendor-risk owner | OCC 2023-17 + BSCA exam rights; pushes vendor-tier classification, exit-readiness, and SOC2/ISO contract terms |
| P-BU | BU owner (customer onboarding lead) | Customer experience + funnel conversion + speed-to-resolution; pushes capability and latency over containment |
| P-CIO-FINOPS | CIO / FinOps (combined per codex Q3) | Per-token cost, infra spend, capacity planning; pushes lower-cost paths and cost-attribution discipline |
| P-EXAMINER | OCC examiner (adversarial external; from S003-app onward) | Reads the substrate as a regulator would; pushes traceable supports for every control claim |

The external orchestrator MUST convene at least 3 perspectives per substantive decision, and MUST include P-EXAMINER in any session from S003-app forward that touches a controlled-function decision (KYC, BSA, Reg E, UDAAP).

## §4 Six-session arc plan

### S001-app — Constraint inventory + agent identity model
- **Phase**: foundation
- **Substantive deliverables**: (a) constraint inventory landed as `assumption_ledger` rows tagged with reg-source citation in `basis`; (b) one substantive decision-record on agent identity model (per-customer service-account vs per-session ephemeral identity vs hybrid; convene P-CISO + P-CCO + P-CIO-FINOPS).
- **Cycle subject inaugurated**: weekly cost-variance review (placeholder: zero rows yet, primitive seeded via assumption AR for the cost-attribution discipline itself).
- **Expected friction**: where do regulatory citations live? `basis` text-atom is 8-480 chars — what about a long quote? Is `assumption_ledger` the right table for a *requirement* (must be met) vs an *assumption* (taken on faith pending verification)? F1 candidate.

### S002-app — PII/NPPI redaction boundary + model routing
- **Phase**: contested-architecture
- **Substantive deliverable**: decision-record on the most contested decision (per codex Q2): can raw customer PII/NPPI reach a managed LLM endpoint, or must it stay inside bank-controlled infrastructure with deterministic redaction at the boundary? Convene P-CISO + P-CCO + P-LEGAL + P-CIO-FINOPS + P-BU (5 perspectives).
- **Cycle subject inaugurated**: per-deploy security review (placeholder).
- **Expected friction**: chain-walk on every cited regulation will surface whether `decision_supports.cite` machinery actually scales across 5+ supports per perspective. F4 candidate (ledgerized-vagueness if regs cited as supports without specifics).

### S003-app — Governance framework v1 + first SR 11-7 ambiguity test
- **Phase**: governance design
- **Substantive deliverables**: (a) governance framework v1 covering decision-rights map (who can approve what), audit-trail expectations, AI-incident-response playbook stub; (b) substantive decision on how to handle SR 11-7 scope ambiguity post-OCC-Apr-2026 (treat as in-scope by precaution, build genAI-specific framework, defer pending FFIEC/FRB/FDIC alignment). Convene P-CCO + P-CRO + P-MRM + P-EXAMINER (P-EXAMINER joins from this session).
- **Expected friction**: stakeholder voices may collapse here if the agent is tired (F4 ledgerized-vagueness watch).

### S004-app — Cost model v1 + first cycle_ledger rows
- **Phase**: cost / FinOps
- **Substantive deliverables**: (a) cost model v1 covering per-workflow per-customer unit economics, model-routing cost basis, audit/log storage cost line items, vendor-cost forecast; (b) first concrete `cycle_ledger` rows on the weekly cost-variance review subject — substantial and non-substantial cycles both, to exercise classification.
- **Expected friction**: cycle_ledger allowlist is `assumption` only at v1 — does cost-variance review fit? AR-S207-2 shoehorn applies; capture friction. F1 candidate (cost-variance review may want its own subject_kind).

### S005-app — Vendor-risk + 36-hr cyber incident integration
- **Phase**: third-party + incident response
- **Substantive deliverables**: (a) vendor-risk tier classification for the model-vendor relationship under OCC 2023-17 + BSCA; (b) 36-hour cyber incident notification process integrated with agent-platform telemetry. Convene P-VRM + P-CISO + P-LEGAL + P-EXAMINER.
- **Cycle exercise**: per-deploy security review subject — submit at least 2 cycle rows.
- **Expected friction**: stakeholder-event primitive (event_ledger, allowlist=assumption only at v1) — does an OCC examiner inquiry fit? AR-S207-2 shoehorn applies. F1 candidate.

### S006-app — Cross-pillar integration session + stakeholder-event simulation + arc retrospective
- **Phase**: integration + harvest-prep
- **Substantive deliverables**: (a) cross-pillar integration session — find the seams where security/cost/governance interact (e.g., model-routing decisions that have BOTH cost and security implications); (b) stakeholder-event simulation: inject 2-3 realistic events (audit finding, vendor TOS change, regulator inquiry) and watch how the substrate handles invalidation; (c) arc retrospective EF naming what surfaced (F1)-(F5).
- **Expected friction**: This is the harvest-quality session. The retrospective EF feeds the self-dev harvest session at S208+.

## §5 Bootstrap (next self-dev session, S208)

Before S001-app can run:

1. Self-dev S208 creates external workspace at `/Users/ericmccowan/Development/selvedge-regional-bank-agents/` (path subject to operator confirmation).
2. Bootstrap external workspace with `bin/selvedge init`, MODE.md (mode=external-problem, workspace_id, application_brief pointer), apply migrations.
3. Copy `applications/207-regional-bank-agents/brief.md` into external workspace at `applications/001-regional-bank-agents/brief.md`.
4. Copy `session-001-input.md` into external workspace at the same path or hand to operator for in-session paste.
5. Self-dev S208 closes; external S001-app opens via Claude Code in the external workspace, dispatched via prompts/application.md.

## §6 Harvest cadence

After each external session closes:

```sh
bin/selvedge monitor-external harvest-ef --workspace /Users/ericmccowan/Development/selvedge-regional-bank-agents
```

Harvest writes engine_feedback rows from external substrate into self-dev substrate with provenance preface and per-row ledger. After S006-app the operator runs the **harvest session** in self-dev (probably S214 or thereabouts) to triage the imported EFs into open-issues / decisions / spec amendments.

## §7 Arc-completion criteria

Arc is closed when:

- All 6 external sessions have closed-records in external substrate.
- All engine_feedback rows from external have been harvested into self-dev.
- A self-dev harvest session has triaged the (F1)-(F4) signals into open-issues or decisions.
- Arc-retrospective decision-record submitted in self-dev naming what the engine learned.

Arc is **halted early** if:

- 3 consecutive external sessions emit zero engine_feedback rows (signal: persona collapse or capture by routine).
- The orchestrator reports E_REFUSAL_T-NN repeatedly on the same shape (signal: substrate gate is fundamentally misaligned with enterprise work; harvest needed before continuing).
- Operator reads the substrate at any point and finds the (F4) ledgerized-vagueness pattern dominant (signal: convene-and-redirect before more sessions consolidate the pattern).

## §8 Out of scope

- Workflow orchestration pillar (deferred per S207 user direction).
- Building any executable platform code or running any actual agent.
- Engaging any actual bank, regulator, or vendor.
- Any decision that depends on jurisdictional specifics beyond the scenario sketch (e.g., specific state AG positions, specific FRB district interpretations).
- Resolution of the OCC-Apr-2026 SR 11-7 scope ambiguity by external substrate — arc DESIGNS under the ambiguity, does not resolve it.
