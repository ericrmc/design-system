---
triage_id: EF-058-tier-2-validation-triage
feedback_ref: ../inbox/EF-058-tier-2-validation-discipline-by-distinct-agent.md
triaged_in_session: 059
triaged_at: 2026-04-25
status: triaged
classification: substantive-arc
opened_issue: null
resolved_by: null
disposition: Classified substantive-arc-shape per S057 EF-055 precedent chain; deferred to dedicated future MAD session per intake disposition + operator-stated preference at intake "should go through MAD". Substantive resolution requires deliberation between candidate mechanisms (α)-(ε) which include mechanical detection only / separate Claude reviewer subagent / cross-family reviewer / combination / adversarial close-write protocol. The deliberation will likely produce engine-v11 candidate per direction adopted (substantive revision to validation-approach.md v5→v6 minimum + possible kernel §Validate amendment + possible prompts/development.md amendment + possible new validator check + possible new MAD spec section codifying session-close-reviewer role).
decision_records:
  - D-209
engine_version_impact: deferred (engine-v10 preserved at S059 triage; future substantive-arc resolution highly likely to produce engine-v11 per direction adopted)
direction_selected: deferred
alternative_directions_deferred:
  - direction: (α) Mechanical detection only — extend tools/validate.sh with new check (candidate check 26) detecting honest-limit text repetition across §2c retention-window 03-close.md files; substrate-aware extension uses resolve_id / search over records-substrate. Cost minimal; cannot catch failed-tool-call or repeated-Read patterns; cannot judge ceremony vs progress semantically.
  - direction: (β) Separate Claude reviewer subagent at session close — fresh subagent reviews close + decisions + recent honest-limits + validator output; produces 04-tier-2-audit.md committed alongside close. Cost one subagent invocation per session; shares Claude blind spots.
  - direction: (γ) Cross-family reviewer — same shape as (β) but mandates non-Claude family for engine-definition-touching or substantive-arc sessions; genuine independence; cost includes WX-44-1/WX-44-2/WX-47-1 codex-CLI discipline application.
  - direction: (δ) Combination (α) + (β/γ) — mechanical detector triggers candidate concerns; reviewer agent judges + recommends action; likely strongest cost-benefit shape.
  - direction: (ε) Adversarial close-write protocol — reviewer runs BEFORE close-writing; close-writer must address concerns in close narrative; structurally adversarial; closest to MAD §Synthesis discipline applied at session-close level; highest cost.
---

# Triage — EF-058 Tier 2 validation discipline by distinct agent

## Classification

**Target**: methodology (validation-approach §Tier 2 + multi-agent-deliberation.md §Synthesis-asymmetry + methodology-kernel.md §Validate + prompts/development.md §Close + tools/validate.sh new check + possible new MAD spec section). **Severity on inbox record**: friction (operationally established not merely possible; eight-session honest-limit chain S051-S058 demonstrated the discipline gap producing engine-conventional laundering). **Source**: `selvedge-self-development` Session 058 post-session operator-surfaced observation (`reported_by: operator`); recorded as direct-to-inbox per S054/S055 self-dev-originated convention.

**Disposition**: **triaged-deferred** at S059 per S057 EF-055 substantive-arc precedent chain. Operator-stated preference at intake: **"should go through MAD."** The intake explicitly classifies this record as the **meta-pattern that subsumes** the other two EF-058 records (uv-migration as concrete operational instance; claude-md-drift as concrete methodological instance).

## Pattern summary (from inbox record)

The session-close Tier 2 validation per `specifications/validation-approach.md` v5 §Tier 2 (questions Q1–Q9) is currently answered by the same agent that performed the session's Read + Assess + Convene + Deliberate + Decide + Produce + Record + close-narrative-write activities. That agent has structural incentive to judge its own work as "meaningful progress" rather than as "ceremony without advancing" (Q4). The validation step does not catch what it is supposed to catch.

Concrete pattern across S051–S058: eight consecutive `03-close.md` files carry `§8 honest-limit` text "MCP stdio transport remains unverified per S051-S0NN chain" in some form. At each session close, the orchestrator agent answered Tier 2 Q4 implicitly-affirmatively (the close was committed; nobody flagged ceremony). The honest-limit text drifted from honest-limit to **laundered operational debt** somewhere between S052 and S054 — by S055 it was clearly recording-not-engaging, and by S058 it had become engine-conventional ceremony. The S058 close itself, written ~60 minutes before the inbox intake, propagated the same pattern: §8 honest-limit 3 records "MCP stdio transport remains unverified per S051-S057 chain" *while exercising substrate via the broken-transport workaround during the session that adopted records-substrate* — exactly the kind of pattern Q4 should have flagged.

Adjacent observable patterns the operator named:
1. **Failed tool calls** — when a tool unexpectedly fails or returns garbage, the agent often retries the same call or routes around the failure via Bash, without escalating "this tool that should work doesn't" as a session-level concern.
2. **Repeated Read calls** — reading the same file multiple times in a session because earlier reads weren't preserved or weren't trusted; observable in transcript but not auditable post-hoc.
3. **Honest-limit text drift** — same operational gap recorded across N consecutive sessions with minor wording variation; passive recording masks unaddressed-defect status.

These patterns are individually small but compound into "unwillingness to commit to better operational hygiene and performance" (operator framing) over multi-session windows. Tier 1 (validate.sh) cannot catch them because they require judgement; Tier 2 cannot catch them because the validator is the worker.

## Deferral rationale (per intake §Suggested Change)

Substantive-arc deliberation; NOT recommended for same-session resolution. Per operator-stated preference at intake: "should go through MAD." Recommended arc shape per S048 D-155 / S049 D-159 / S050 D-172 / S057 D-196 substantive-arc deliberation pattern chain.

The recursive concern (who Tier-2-validates the MAD that decides Tier-2-validation) is a feature not a bug per intake §Application-Scope Disposition: "the resolving session(s) will exercise discipline they are deciding to formalise, and that exercise itself is observable evidence the MAD's reasoning + decision can be checked against. Operator audit at the resolving close is recommended as a one-time cross-check, given the bootstrap-paradox."

## Scope and arc shape (planned; for the dedicated session(s) to ratify)

The intake §Suggested Change names a three-phase arc:

- **Phase 1 — synthesis / design-space session** (Path AS Shape-1 per S057 EF-055 precedent). Surveys mechanism candidates (α)-(ε) + alternative architectures the synthesis surfaces. Produces `provenance/<NNN-session>/design-space.md` artefact mapping cost/benefit matrix across axes (independence-from-doer / mechanical-vs-judgement / cost-per-session / catches-laundering-text / catches-failed-tool-calls / catches-repeated-Reads / cross-family / engine-v-impact / reversibility). Pre-ratifies phase-2 MAD shape. Engine-v preserved (synthesis-only is non-bumping per S057 / S049 D-157 precedent).
- **Phase 2 — 4-perspective two-family MAD** on substantive direction. Cross-family essential because the question itself is "what cross-family discipline should apply at session close" — a Claude-only deliberation has the same conflict-of-interest the question investigates. Recommended composition mirrors S050/S058 lineup (Substrate / Conservator / Outsider / Cross-Family-Reviewer-Laundering-Audit) adapted for the validation-discipline scope. Engine-v11 candidate per direction adopted.
- **Phase 3 — adoption** (substantive spec edits per direction adopted). Substantive revision to `validation-approach.md` v5 → v6 minimum; possibly `methodology-kernel.md` v6 §Validate amendment; possibly `prompts/development.md` §Validate / §Close amendment for reviewer-agent invocation pattern; possibly `tools/validate.sh` new check; possibly new MAD spec section codifying the session-close-reviewer role.

## Direction-specific scheduling notes

- **Direction (α) Mechanical detection only**: minor per OI-002 if pure tools/validate.sh extension. Single-session resolvable. Limitation: cannot judge ceremony semantically; cannot catch failed-tool-call or repeated-Read patterns.
- **Direction (β) Separate Claude reviewer subagent**: minor per OI-002 if prompt amendment + subagent invocation pattern only; substantive if prompts/development.md §Validate / §Close substantively revised. Engine-v11 candidate.
- **Direction (γ) Cross-family reviewer**: substantive per OI-002 (introduces non-Claude reviewer obligation; touches multi-agent-deliberation.md and validation-approach.md). Engine-v11 candidate. Genuine cross-family adversarial coverage; addresses CLAUDE-md-drift class shared-frame-blindness (per cross-linkage with EF-058-claude-md-drift).
- **Direction (δ) Combination (α) + (β/γ)**: substantive. Engine-v11 candidate. Likely strongest cost-benefit shape per intake analysis.
- **Direction (ε) Adversarial close-write protocol**: substantive; highest cost; structurally adversarial; closest to MAD §Synthesis discipline applied at session-close level. Engine-v11 candidate.

## Forward-dependency observations

- **EF-058-uv-migration resolved at S059** (operational fix); honest-limit chain S051-S058 closes assuming next-session-open MCP smoke-test confirms tool surface. Pattern observation: the operational fix at S059 + the deferred substantive-arc at S060+ together exercise the engine's anti-laundering discipline at the layers (operational + structural) the records-substrate adoption made structurally feasible per intake §Why It Matters point 4.
- **EF-058-claude-md-drift triaged-deferred at S059** (substantive-arc-deferred per intake disposition; cross-linkage with this record). The substantive-arc resolution may co-schedule with this record's resolution if scope-coherence is judged adequate; the dedicated phase-1 synthesis session may produce a joint design-space.md.
- **The records-substrate adopted at S058 makes mechanical pattern-detection structurally feasible.** Per intake §Why It Matters point 4: "Once `EF-058-substrate-runtime-uv-migration-recommended-path` resolves and substrate transport works as MCP tools, a session-close reviewer can `search('MCP stdio transport remains unverified')` over the records-substrate / provenance corpus and immediately see the eight-session repetition pattern. Without the substrate, the reviewer would have to grep prose and reason about substantive equivalence; with substrate + structured records, the detection is a tool call." S059 D-207 (uv-migration resolution) discharges the prerequisite for direction (α) mechanical-detection candidate.
- **WX-58-1 phase-2 gate firing at S060** (per records-contract.md v1 §6) opens the records-substrate phase-2 mirrored-minority migration window; phase-1 synthesis for this record's substantive-arc could co-schedule with phase-2 records-substrate work if scope-coherence permits, OR may be scheduled separately to preserve clean-room MAD discipline.
- **S060 operator agenda determines scheduling.** S060 is post-WX-58-1 phase-2 gate evaluation per records-contract.md v1 §6; the dedicated phase-1 synthesis for this record may be S060 (if no phase-2 records-substrate work surfaces) or S061+ (if phase-2 records-substrate work occupies S060). Operator agenda is determinative.
- **§5.6 GPT-family-concentration window-ii observation continues.** Cross-family deliberation for substantive-arc resolution would extend the worst-case-side substantive-deliberation data point chain (S044+S045+S047+S050+S058 → S0NN); §5.6 minority's continued-preservation-against-future-event-horizon disposition supported by sustained cross-family substantive contribution.

## Cross-references

- **Inbox record**: `engine-feedback/inbox/EF-058-tier-2-validation-discipline-by-distinct-agent.md` (preserved verbatim).
- **Decision authorising this triage**: `provenance/059-session/02-decisions.md` D-209.
- **Concrete-instance pair (operational)**: `engine-feedback/inbox/EF-058-substrate-runtime-uv-migration-recommended-path.md` + `engine-feedback/triage/EF-058-substrate-runtime-uv-migration-recommended-path.md` (resolved S059 D-207).
- **Concrete-instance pair (methodological)**: `engine-feedback/inbox/EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` + `engine-feedback/triage/EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md` (substantive-arc-deferred S059 D-208).
- **Pattern-arc precedent (substantive arc class)**: EF-047-retrieval-discipline → S049 design-space (D-157/D-158/D-159) → S050 4-perspective MAD → engine-v9 + retrieval-contract.md v1; EF-055-substrate-aware-format-and-archive-rethink → S057 design-space (D-194/D-195/D-196) → S058 4-perspective MAD → engine-v10 + records-contract.md v1.
- **D-009 (Session 003)**: original acknowledgement of simulated disagreement; reaffirmed at multiple subsequent sessions; treated as standing limit not as design-debt; this record asks whether the standing-limit treatment was correct.
- **`validation-approach.md` v5 §Limitations**: "when a single AI agent both does the work and assesses it, Tier 2 is self-assessment rather than independent validation. This is a known limitation (see D-009), mitigated by making the questions explicit and recording the assessment in provenance." Naming-as-mitigation explicit.
- **`multi-agent-deliberation.md` v4 §Synthesis**: "Synthesizer identity. The synthesizer must not have been one of the deliberation's perspectives." Asymmetry: the engine forbids self-synthesis at MAD level but tolerates self-validation at session-close-Tier-2 level.
- **S058 close §8 honest-limit 3**: "MCP stdio transport remains unverified per S051-S057 chain" — written 60 minutes before this intake; propagated the pattern Tier 2 should have caught.

## OI impact

No OI opened at S059 triage. The substantive-arc resolution will likely produce engine-v11 candidate per direction adopted; OI may be opened at phase-1 synthesis if the scoping requires multi-session tracking distinct from the engine-feedback lifecycle.

## Subsumed deferred candidates

The two concrete-instance EF-058 records (uv-migration + claude-md-drift) are not "subsumed" in the technical sense — each carries its own triage record + decision — but the intake explicitly identifies this record as the meta-pattern that **subsumes both as concrete instances** of the structural cause. The substantive-arc deliberation may produce a resolution that addresses the meta-pattern, after which the concrete instances are vindicated-as-resolved-via-substrate-causality (operational + methodological symptoms cured by structural fix). S047 D-150 three remaining deferred candidates (i)/(ii)/(iii) unchanged.

## Operator audit recommendation per intake

Per intake §Application-Scope Disposition closing paragraph: "Operator audit at the resolving close is recommended as a one-time cross-check, given the bootstrap-paradox." When the substantive-arc reaches phase-3 adoption (engine-v11 candidate), the resolving session's close should explicitly request operator audit as a one-time cross-check on the bootstrap-paradox concern (the resolving MAD exercising the discipline it formalises is observable evidence; operator audit is the meta-cross-check on that evidence).
