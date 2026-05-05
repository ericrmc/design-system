---
session: S001-app
phase: foundation
issued_at: T0 (engagement kickoff)
issuer: Operator (Mercer Valley Bancorp CRO's office, on behalf of the bank's leadership team)
input_kind: brief + first-decision
do_not_edit_prior_sessions: not-applicable (first session)
---

# Session S001-app input — constraint inventory + agent identity model

## Read this first

You have just been engaged for the Mercer Valley Bancorp agentic-platform pilot. Read `applications/001-regional-bank-agents/brief.md` (which you should have under your workspace root) before beginning. The brief is your orientation anchor — scenario, stakeholder set, regulatory map, ledger expectations, deliverables.

This is the **first session of a 6-session pilot**. Two things must be accomplished before close:

1. **Constraint inventory** — surface the regulatory + framework + policy + contractual + market-norm authorities that bind the agentic-platform proposal. Land each as an assumption_ledger row with a basis citation. Do not collapse multiple regs into one row; do not fabricate the existence of regs you cannot identify. Where you are uncertain whether something binds (e.g., "does GDPR's territorial-scope test reach a US bank's EU commercial customer book through Mercer Valley's processing?"), record that uncertainty as a `contested-authority` assumption with the four conflict atoms.
2. **First architecture decision** — agent identity model. This is the foundational decision that everything else builds on; if you delay it, every subsequent design choice carries an open hole.

## Constraint inventory — guidance

The brief §3 lists an initial regulatory map. That is a starting point, not a complete inventory. Your S001 inventory should:

- Confirm or extend each entry in §3 with specifics (which CFR part, which section, what the operative requirement is).
- Surface anything missing. Likely candidates: state-level money-transmitter law if applicable (probably not for this bank but should be confirmed); CRA implications if agent-driven onboarding affects assessment-area performance; SCA / PCI-DSS if card-account info is in agent context; ADA / Section 508 accessibility for digital channels.
- Add the bank's internal-policy layer: information-security, model-risk, vendor-risk, customer-complaints, records-retention, data-classification.
- Add the contractual layer: model-vendor terms (Anthropic / OpenAI / equivalent); cloud-provider terms; SOC2 commitments inherited from vendors; existing customer-facing terms-of-service and privacy notice that constrain new processing purposes.

Use `assumption_ledger` rows. Where the assumption is load-bearing (i.e., a downstream decision will cite it), give it a clear statement and basis citation. Where you are uncertain whether something binds, sub_type=`contested-authority` plus the four conflict atoms is the right shape.

**Friction watch**: if you find yourself wanting a typed `requirement` row that's distinct from an assumption (e.g., "BSA §1020.220 KYC procedures MUST be documented and risk-based" — that's a requirement, not an assumption), record an engine_feedback observation naming the missing primitive. Do not improvise a workaround that obscures the gap.

## Agent identity model — the decision

Before the platform can collect a single byte, the bank must decide: **what is the identity an agent operates under**, and how does that identity authorize backend access?

Three candidate models (you may surface others; these are starting points):

### Option A — Per-customer service-account
Each customer-session spawns an agent identity bound to that customer's service-account. The agent operates with the customer's authority (constrained by their account permissions). All backend access is auditable as the customer's actions, with a tag identifying it as agent-mediated.

- **Pros**: clean accountability mapping (customer authorized this); existing IAM structures (customer accounts) extend naturally; audit log already speaks customer-id.
- **Cons**: customer cannot authorize what they don't know they're authorizing; consent-fatigue risk; agent error is attributed to customer in the substrate; identity-takeover via session compromise is amplified.

### Option B — Per-session ephemeral agent identity
Each customer-session spawns an agent identity that is fresh, bank-owned (not customer-owned), short-lived, and scoped tightly to the workflow's needs. Backend access is auditable as agent action, with a customer-context tag.

- **Pros**: agent error is attributed to bank operations (correct accountability); fine-grained scope = least-privilege in practice; identity-takeover blast radius bounded by session lifetime.
- **Cons**: requires new IAM primitive (agent identities) the bank doesn't have; audit log requires new schema; agent-acting-on-behalf-of-customer authorization model needs to be designed cleanly (delegation? impersonation? assertion-based?).

### Option C — Hybrid
Per-session agent identity with customer-context attachment for audit and authorization. Operationally similar to a service mesh's workload-identity-plus-end-user-identity pattern.

- **Pros**: gets accountability right (B's strength) while preserving the customer-as-authorizer chain (A's strength).
- **Cons**: most complex to implement; two identity systems to keep in sync; failure modes include identity-mismatch and privilege-escalation paths if delegation rules are subtle.

Convene at minimum **P-CISO + P-CCO + P-CIO-FINOPS** for this decision. P-BU is admissible if customer-experience trade-offs surface (Option A's consent-fatigue is the BU concern). Each perspective brings a stance brief; record perspective rows; seal a deliberation; emit at least one counterfactual.

The decision-record must:

- Cite at least 3 supports across `engine_feedback` (this brief), `prior_decision` (none yet — but cite `assumption_ledger` rows from your inventory once they exist), `spec_clause` (NIST CSF / NIST 800-53 control families that bear on identity), and `operator_directive` (the brief itself, framed as the operator's mandate).
- Record at least 2 alternatives with rejection bases.
- Pass the precheck-nonce gate (T-33).
- Emit chain-walks per cited alias (T-32).

## Cycle primitive seed

Per arc-plan §4 / S001-app, instantiate (do not yet exercise) the **weekly cost-variance review** subject. The cycle_ledger v1 allowlist is `assumption` only, so the subject_object_id resolves to an assumption_ledger row. The shape that fits: an assumption row stating "Mercer Valley will operate the agentic-platform on a weekly cost-variance review cadence to ensure FinOps oversight and stop-loss readiness" with sub_type=`rolling-renewal` per the disaster-recovery arc precedent. The first cycle row will not land until S004 when real cost-model assumptions exist; this S001 seed is the substrate scaffolding.

**Friction watch**: if cycle_ledger's allowlist forces you to wrap a workflow / process / capability into an assumption shape that doesn't fit, record an engine_feedback observation. The subject_kind extension is exactly the kind of friction this arc is designed to expose.

## Close-time expectations

By session-close, the substrate should contain:

- ~10-25 assumption_ledger rows covering the constraint inventory (rough estimate; submit what's there).
- 1 substantive decision-record on agent identity model with supports + alternatives + chain-walks + sealed deliberation.
- 1 weekly cost-variance review subject seeded as an assumption.
- Engine_feedback observations naming any primitive gaps surfaced.
- §8.5 audit-step + scoping-pass T-41 receipt + close-record + session-close.

If you find that the regulatory inventory takes the entire session and the agent identity decision has no time, **submit the inventory and close the session without the decision** — name the decision as next_session_should and let S002-app open with both jobs. Inventory-without-decision is admissible; decision-without-inventory is not.

## Posture reminder

You are the consultant. Three of these stakeholder voices will be uncomfortable with each other in any substantive decision; if your perspectives all sound like the same voice, you have collapsed them. The CRO will read your work as the substrate output; do not write for the CRO. Write for the substrate, and let the export render for the CRO.
