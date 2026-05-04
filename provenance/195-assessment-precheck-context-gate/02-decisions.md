---
session: 195
title: assessment-precheck-context-gate — decisions
generated_by: selvedge export
---

# Decisions

## D-1. S195 ships T-38 assessment-precheck gate + bin/selvedge context CLI + migration 047 (assessment_prechecks) per operator-named-mandate at S194-close to relocate context-surfacing from orient to assessment-time substrate-enforced.

**Kind:** schema_migration.  **Outcome:** adopt migration `047-assessment-prechecks`.

**Why.**

- (engine_feedback) EF-S195-1 codex-shape-consult (gpt-5.5 xhigh) endorsed bootstrap-by-ordering + all-kinds-gate (no kind=meta exemption since triage-only meta still modifies durable state) + sha256-over-rendered-pack + atomic-consume. [EF-S195-1]
- (prior_decision) DV-S194-1 shipped engine_feedback_anchors typed-FK graph (option C) + relevant_history_anchored orient surfacing (option E); operator-named at S194-close that orient is wrong location and surfacing must move to assessment-time per substrate-presented-not-operator-curated principle. [DV-S194-1]
- (prior_decision) DV-S081-1 substrate-loss-defense-v1 substrate-canonical posture binds: substrate is canonical, agents avoid friction, ship the gate that forces context-load before deliberation. [DV-S081-1]
- (prior_decision) DV-S189-1 markdown-only-recovery binds zero-anchor-acceptable for harvested EFs; assessment-precheck pack queries engine_feedback_anchors via FK join not body_md substring match. [DV-S189-1]

**Effects.**

- adds_migration 047-assessment-prechecks table + role-capability inline
- creates process_rule: T-38 assessment-precheck gate + context CLI
- modifies orient.py remove relevant_history_anchored (S194 location-error)

**Rejected alternatives.**

- **R-1.1.** Keep S194 orient surfacing (relevant_history_anchored stays) and add the precheck-gate as ADDITIONAL surface.
  - (operator_override) Operator-named at S194-close orient is wrong place; agents skim under context pressure; relocate not duplicate.
- **R-1.2.** Wait for 3 calibration-EFs across N>=5 sessions naming missed-historical-context per FR-S194-9 watch-trigger M-2 minority before shipping the gate.
  - (operator_override) Operator-named at S194-close: wait-for-evidence approach no longer appropriate after 194 sessions of evidence agents avoid the substrate; ship the gate now.
- **R-1.3.** Operator-curated targets[] field in assessment payload (agent picks what context to load; no auto-generation default).
  - (inferior_tradeoff) Operator-named substrate-not-frictionless agents-avoid-substrate; substrate-presented auto-generation mandatory; named --target narrows but not required.
- **R-1.4.** kind=meta admit zero-precheck (mirror T-33 calibration/disposition/procedural admit) so triage-only meta sessions skip the gate.
  - (inferior_tradeoff) Codex shape-consult: triage-only meta still modifies durable state via FR/EF dispositions and substrate writes; gate ALL kinds with no admit-zero per operator substrate-friction-is-the-point.
- **R-1.5.** Hardcoded S195 session-id exemption in T-38 logic to avoid bootstrap chicken-and-egg.
  - (inferior_tradeoff) Codex caution avoid hardcoded session exemption; bootstrap-by-ordering works (S195 own assessment-submit happens before migration applies; gate fires from S196 onward).
