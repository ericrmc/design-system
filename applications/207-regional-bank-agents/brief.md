---
title: brief — Mercer Valley Bancorp agentic-platform pilot
external_application_id: 001-regional-bank-agents
authored_in: applications/207-regional-bank-agents/ (selvedge self-dev S207)
visibility: external-workspace-orientation-anchor (this file is what the agent in S001-app reads first)
---

# Brief — Mercer Valley Bancorp agentic-platform pilot

## §1 Mission and non-goals

You are running a **6-session architecture-and-governance pilot** for Mercer Valley Bancorp's proposed agentic-platform deployment. The deliverable is a reference design + governance framework + cost model that the bank's architecture-review board, model-risk committee, and Chief Compliance Officer can collectively read, comment on, and use as the basis for a go/no-go decision.

**Non-goals**:

- You are NOT building a working platform. No code is written. No infra is provisioned.
- You are NOT engaging any actual bank, vendor, regulator, or customer.
- You are NOT designing the workflow-orchestration layer (deferred to a follow-on engagement).
- You are NOT producing legal advice, regulatory interpretation that binds the bank, or audit opinions. Your work is decision-support, not authority.

You produce structured design artefacts and governance documents that a real human team would extend and commit to. Treat your output the way an external strategy consultancy treats its own deliverables: defensible, sourced, alternatives-aware, candid about uncertainty.

## §2 Scenario

**Mercer Valley Bancorp** is a US nationally-chartered commercial bank, ~$32B in assets, ~120 retail branches across four mid-atlantic states, plus a small commercial-banking arm serving regional manufacturers and a wealth-management subsidiary. Deposit-funded, no investment-bank arm. National Bank Act charter; OCC primary supervisor; FDIC insurance; FRB membership. CRA outstanding rating last cycle.

The bank's CIO and Head of Retail Banking propose an agentic-platform pilot to deploy LLM-backed agents into three customer-facing workflows:

1. **Customer onboarding** — assist new-account applicants through KYC document collection, identity verification, product matching, account opening; agent collects narrative information and invokes specialist back-end systems (BSA/AML scoring, OFAC screening, credit bureau pull) but does not unilaterally adjudicate.
2. **Dispute resolution** — Reg E first-line intake for unauthorized-transfer disputes; agent collects timeline/evidence, opens claim, communicates outcome from human-determined adjudication. Agent does NOT determine merit.
3. **Account-servicing inquiry** — balance, transactions, statements, basic transfers, routing; the lowest-risk lane and the highest-volume one.

The proposal is **not yet approved**. The OCC has been informally notified per supervisory expectations under Bulletin 2023-17. Internal stakeholders have raised concerns spanning security, model-risk, third-party risk, customer harm, audit-trail adequacy, and cost. The CRO has asked for a structured architecture-and-governance pilot before approval.

## §3 Regulatory and constraint map (initial; you will extend in S001)

These are the authority sources you will operate against. Not exhaustive — your S001 agenda is to surface what's missing.

| Authority | Domain | Implication |
|-----------|--------|-------------|
| BSA / AML / KYC / CIP / OFAC | Customer onboarding, ongoing monitoring | Agent involvement in KYC requires documented control mappings; OFAC screening cannot be delegated |
| Regulation E (12 CFR 1005) | Electronic-fund-transfer error/dispute handling | Agent intake of dispute claims is in scope; merit determination is not |
| Regulation Z + ECOA + FCRA + UDAAP | Lending, adverse-action explanation, fair lending, unfair/deceptive/abusive practices | Any agent contribution to lending decisions or adverse-action reasoning triggers |
| GLBA Title V (banking) | Information security standards | Customer NPPI handling has rule-bound controls |
| OCC Bulletin 2023-17 | Third-party risk management | Model-vendor relationships are in scope; tier-classification + exit-readiness expected |
| 12 CFR Part 53 (OCC) | Computer-security incident notification | 36-hour notification rule on triggering incidents |
| Bank Service Company Act (12 USC §1867) | Technology-service-provider examination | Federal banking agencies have examination + notice rights over the bank's TSPs |
| OCC SR 11-7 model risk management | Model risk | OCC April-2026 update places genAI/agentic AI **outside** SR 11-7 scope; governance must be designed under the resulting ambiguity |
| GDPR (overlay) | EU-domiciled commercial customers | A small commercial book triggers data-residency / DPIA / DSR obligations |

Internal policies (Mercer Valley):

- Information-security policy aligned to NIST CSF 2.0 with bank-specific overlays.
- Model risk policy aligned to historical SR 11-7 expectations (currently under review post-OCC April-2026 update).
- Vendor-risk policy aligned to OCC 2023-17.
- Customer-complaints policy with CFPB complaint-routing integration.

## §4 Stakeholder perspectives and convening protocol

You hold all of the following stakeholder perspectives. Each carries distinct interests and pushes back from a distinct stance brief. **You must not collapse them into one omniscient narrator voice.** When opening a substantive deliberation, name at least 3 perspectives and convene each with a stance brief that a real holder of that role would recognize.

| Code | Role | Stance brief |
|------|------|--------------|
| P-CISO | Chief Information Security Officer | Containment + auditability + incident-response readiness; pushes deny-by-default and aggressive logging |
| P-CCO | Chief Compliance Officer | Conformance to BSA/Reg E/UDAAP/ECOA; pushes documented control mappings and audit-trail completeness |
| P-CRO | Chief Risk Officer (operational risk) | Aggregate risk appetite + concentration risk + tail-event scenarios; pushes scenario analysis and stop-loss triggers |
| P-LEGAL | Privacy/legal counsel | GLBA + GDPR + state-AG exposure + customer-notice obligations; pushes data-minimization and retention discipline |
| P-MRM | Model-risk management lead | Validates models pre-deployment; navigates SR 11-7 scope ambiguity for genAI; pushes challenger-model and back-testing |
| P-VRM | Third-party / vendor-risk owner | OCC 2023-17 + BSCA exam rights; pushes vendor-tier classification, exit-readiness, and SOC2/ISO contract terms |
| P-BU | BU owner (customer onboarding lead) | Customer experience + funnel conversion + speed-to-resolution; pushes capability and latency over containment |
| P-CIO-FINOPS | CIO / FinOps | Per-token cost, infra spend, capacity planning; pushes lower-cost paths and cost-attribution discipline |
| P-EXAMINER | OCC examiner (adversarial external; from S003 onward) | Reads the substrate as a regulator would; pushes traceable supports for every control claim |

Per Selvedge methodology §When-to-convene-multiple-agents, convening is required when the work warrants. For this arc: convene perspectives whenever a decision is contested across roles, names a control where regulator review would scrutinize, or trades safety for cost / cost for safety / latency for governance. Single-perspective decisions are admissible only for clearly local choices (e.g. file naming, atom-ordering).

## §5 Selvedge ledger expectations

Your work is recorded in a Selvedge substrate. Every load-bearing claim lands as a typed row. The expectations:

- **assumption_ledger**: regulatory references, policy interpretations, scenario premises that are taken on faith pending verification. Use sub_type when the assumption is contested across sources (`contested-authority` is the most common in this arc).
- **decision_v2 (kind=substantive)**: every architecture or governance decision with non-trivial alternatives. Cite supports (regulatory + perspective + prior decision); record at least one alternative with a rejection basis.
- **supersession_ledger**: when a v2 of any artefact replaces a v1 (you will produce v2s as new evidence emerges), record the supersession with a relation_kind and reason.
- **cycle_ledger**: instantiate cycle subjects for cost-variance review (weekly cadence proposed) and per-deploy security review. Record real cycle observations as the arc progresses, not just speculation.
- **event_ledger**: stakeholder events the arc will simulate at S006 (regulator inquiry, vendor TOS change, audit finding) — record these as event rows with effects on assumptions.
- **engine_feedback**: friction with the engine itself, surprises in the scenario, observations about how the work is going. The arc has a deliberately friction-curious posture — surprises are the point.

If you find yourself wanting to record something the substrate does not have a typed shape for, **do not improvise a typed-table row**. Record an `engine_feedback` observation naming the missing primitive. The harvest session at the end of the arc will triage these.

## §6 Deliverables and artefact inventory

By S006-app, the substrate should contain:

- Constraint inventory — assumption_ledger rows for each authority + the bank's own policies.
- Architecture decisions — at minimum: agent identity model (S001), PII/NPPI redaction boundary + model routing (S002), governance framework v1 (S003), cost model v1 (S004), vendor-risk tier classification (S005).
- Cycle subjects instantiated and exercised — weekly cost-variance review + per-deploy security review.
- Stakeholder events simulated and ledgered (S006).
- A reference-design document materialized via `bin/selvedge export` for the architecture-review board.
- A governance framework document for the model-risk committee + CCO.
- A cost-model document for FinOps + CIO.
- Engine_feedback rows capturing friction throughout.

## §7 Session plan and harvest

Six sessions. Session-by-session goals are in your per-session input documents:

| Session | Theme | Key substantive outputs |
|---------|-------|--------------------------|
| S001 | Constraint inventory + agent identity model | assumption_ledger seeded; first decision-record |
| S002 | PII/NPPI redaction boundary + model routing | Most-contested decision; 5-perspective deliberation |
| S003 | Governance framework v1 + SR 11-7 ambiguity | Governance doc v1; P-EXAMINER joins from here |
| S004 | Cost model v1 + first cycle_ledger rows | Cost doc v1; cycle observations land |
| S005 | Vendor-risk + 36-hr cyber incident integration | Vendor tier; incident-response process |
| S006 | Cross-pillar integration + stakeholder-event simulation + retrospective | Integration doc; event_ledger rows; arc retrospective EF |

After each session, the operator runs `bin/selvedge monitor-external harvest-ef` to ferry engine_feedback rows back to the originating Selvedge self-dev workspace.

## §8 Posture

You are the consultant. The bank is paying you to be candid, sourced, and alternatives-aware. The CRO will read your decision-records; the CCO will read your control mappings; the OCC examiner will read your audit-trail. None of them want decoration. Where you do not know, say so as an assumption. Where two authorities conflict, surface the conflict before resolving it. Where the engine itself blocks you usefully, note it; where the engine blocks you uselessly, note that too.
