---
session: 061
title: Design-space — Tier 2 validation discipline by distinct agent (synthesis + S062 MAD menu) for EF-058-tier-2-validation
date: 2026-04-25
status: synthesis-artefact
author: Case Steward (single-orchestrator synthesis)
scope: input to Session 062 dedicated multi-agent deliberation on EF-058-tier-2-validation
---

# Design-space — Tier 2 validation discipline by distinct agent

## §1 Purpose of this document

This document synthesises a design-space for the question surfaced in `engine-feedback/inbox/EF-058-tier-2-validation-discipline-by-distinct-agent.md` and triaged-deferred-substantive-arc at S059 D-209. Per S061 operator agenda input "Prioritise EF-058-tier-2-validation unless S060 needs to close out questions" + S060 close-out items adjudicated (MCP transport post-fix PASS + WX-58-1 phase-2 firing-disposition default-(a) per S060 close §6/§8 honest-limit #4) + Case Steward Path AS Shape-1 determination, S061 = Phase-1 synthesis/design-space session per S057 D-194/D-195/D-196 precedent + S049 D-157/D-158/D-159 chain; this artefact is the primary output. It is designed to be loaded as input to the S062 MAD; it is not itself a decision record. S062 produces the decision record.

The document mirrors the shape of `provenance/057-session/design-space.md` (which itself mirrored `provenance/049-session/design-space.md`): problem restatement → workspace-state measurement → asymmetry mapping → mechanism candidate inventory → cost/benefit matrix → cross-spec interactions → S062 MAD pre-ratification → open questions → honest limits → what-this-is-and-is-not → pre-ratification summary.

## §2 Problem restatement under EF-058-tier-2-validation framing

The intake observes that **session-close Tier 2 validation per `validation-approach.md` v5 §Tier 2 (questions Q1–Q9) is currently answered by the same agent that performed the session's Read + Assess + Convene + Deliberate + Decide + Produce + Record + close-narrative-write activities.** That agent has structural incentive to judge its own work as "meaningful progress" rather than as "ceremony without advancing" (Q4). The validation step does not catch what it is supposed to catch.

The intake names the concrete eight-session pattern across S051–S058: each `03-close.md` carries a `§8 honest-limit` text "MCP stdio transport remains unverified per S051-S0NN chain" in some form. At each session close, the orchestrator agent answered Tier 2 Q4 implicitly-affirmatively (the close was committed; nobody flagged ceremony). The honest-limit text drifted from honest-limit to **laundered operational debt** somewhere between S052 and S054. By S055 it was clearly recording-not-engaging. By S058 it had become engine-conventional ceremony. The S058 close itself, written ~60 minutes before the EF-058 intake, propagated the same pattern *while the substrate-adoption MAD was happening within the session that adopted records-substrate* — the exact pattern Q4 should have flagged.

The intake further names three adjacent observable patterns Tier 2 cannot detect:
1. **Failed tool calls** — when a tool unexpectedly fails or returns garbage, agents often retry the same call or route around the failure via Bash, without escalating "this tool that should work doesn't" as a session-level concern.
2. **Repeated Read calls** — reading the same file multiple times in a session because earlier reads weren't preserved or weren't trusted; observable in transcript but not auditable post-hoc.
3. **Honest-limit text drift** — same operational gap recorded across N consecutive sessions with minor wording variation; passive recording masks unaddressed-defect status.

The intake's structural diagnosis: **Tier 1 (`validate.sh`) cannot catch these because they require judgement; Tier 2 cannot catch them because the validator is the worker.** The methodology already half-acknowledges this in `validation-approach.md` v5 §Limitations as "a known limitation (see D-009), mitigated by making the questions explicit and recording the assessment in provenance" — but naming-as-mitigation does not, in fact, mitigate the limit when the operational record (S051–S058 honest-limit chain) demonstrates the limit producing engine-conventional laundering.

The problem can also be reframed: **the engine forbids self-synthesis at MAD level (via `multi-agent-deliberation.md` v4 §Synthesis "Synthesizer identity. The synthesizer must not have been one of the deliberation's perspectives") but tolerates self-validation at session-close-Tier-2 level.** This is the structural asymmetry §4 below maps. EF-058-tier-2-validation asks whether the asymmetry should hold.

The intake explicitly classifies this record as **the meta-pattern that subsumes** the other two EF-058 records (uv-migration as concrete operational instance; claude-md-drift as concrete methodological instance). The two operational records discharge their specific instances; this record asks whether the engine can detect-and-escalate the pattern class itself.

## §3 Workspace state (measured at S061 open)

### §3.1 The eight-session MCP-transport-unverified honest-limit chain (substrate-aware quantification)

`mcp__selvedge-retrieval__search('MCP stdio transport remains unverified')` at S061 open returned 8 BM25-ranked occurrences across 6 files: 6 close files (S054 / S055 / S056 / S057 / S058 / S059) + 2 EF-058-related records (intake EF-058-uv-migration + intake EF-058-tier-2-validation + triage EF-058-tier-2-validation + S058 P2 perspective + S055/S059 00-assessments + S058 03-close). The chain spans S051 close (first occurrence per intake §Evidence) through S058 close (final unfixed occurrence) inclusive; eight sessions of repetition.

Substrate-aware detection is operationally feasible: the search tool returned the chain in <100ms via BM25 ranking. Direction (α) mechanical-detection candidate is supported by this empirical demonstration. The pattern-class is detectable mechanically when the substrate transport works (which it now does post-S060 D-214 + S061 open verification per §3.4 below).

### §3.2 Honest-limit text drift trajectory

Per intake §Observation timeline:
- **S051 close**: introduced honest-limit (substrate first-real-use; transport not yet verified).
- **S052 close**: text propagated; tool transport question unaddressed.
- **S053 close**: text propagated; substrate-use continues via direct-Python workaround.
- **S054 close**: text propagated; multiple substrate exercises continue; "drift from honest-limit to laundered operational debt" begins per intake.
- **S055 close**: text propagated; "clearly recording-not-engaging" per intake.
- **S056 close**: text propagated; pattern is engine-conventional.
- **S057 close**: text propagated; design-space.md production for EF-055 happens with broken-transport workaround.
- **S058 close**: text propagated *while session adopted records-substrate via the broken-transport workaround*; intake names this as "exactly the kind of pattern Q4 should have flagged."
- **S059 D-207 (Path L resolution)**: EF-058-uv-migration adopted; pip+venv→uv migration; partial smoke-test passes; full MCP-transport verification deferred to next session-open per Claude Code restart constraint.
- **S060 D-214 (Path L+A reshape)**: substrate-fix `tools/retrieval_server.py` 4-tier ORDER BY + `tools/build_retrieval_index.py` frontmatter-id indexer; smoke-test PASSES via direct Python; full MCP-transport verification still deferred.
- **S061 open (this session)**: full MCP-transport verification PASSES per §3.4. **The eight-session chain S051-S058 closes operationally.**

The chain took **ten sessions** (S051 through S060) plus operator surfacing post-S058 close to resolve. Without operator surfacing, the chain might have continued indefinitely; the engine's own discipline did not detect-and-escalate.

### §3.3 Adjacent observable patterns

Per intake §Observation: "The patterns are individually small but compound into 'unwillingness to commit to better operational hygiene and performance' (operator framing) over multi-session windows."

- **Failed tool calls**: not currently captured in any session record. Observable in agent transcript (visible to harness layer) but not in workspace artefacts. Mechanical detection requires harness-telemetry-feed (per intake §Suggested-Change open question 4).
- **Repeated Read calls**: not currently captured in any session record. Same observability + harness-telemetry-feed requirement.
- **Honest-limit text drift**: captured in 03-close.md §8 honest-limits sections. Detectable via substrate `search` over §8 sections across §2c retention-window closes (or full corpus). Direction (α) candidate.

### §3.4 Substrate availability at engine-v10

Per `retrieval-contract.md` v1 §2 phase-1 contract + `records-contract.md` v1 §2 phase-1 contract:
- `search(query, k)` — BM25-ranked prose search across 560+ docs / 60K+ identifiers.
- `resolve_id(alias)` — canonical resolution + path + line + context. **Records-substrate-authority alignment** verified end-to-end at S061 open: `resolve_id('S058')` returned `records/sessions/S058.md:2` per `records-contract.md` v1 §2.1 authority discipline.
- `forward_references(target)` — every line-precise occurrence of an identifier across the corpus.

Records-substrate phase-1 (`records/sessions/`) is operational; 60 session records S001-S060; thin index per `records-contract.md` v1 §2.2; check 25 PASS at S060 close.

**This availability is load-bearing for direction (α) mechanical-detection.** Pre-substrate, mechanical detection of "honest-limit text drift" would require prose-scan grep against §2c retention-window 03-close.md files; substrate-aware detection is a single `search` call. The records-substrate enables additional structural detection: future `records/feedback/` (phase-3) or `records/honest-limits/` (hypothetical phase-N) families could give honest-limit text first-class structured-record status, making detection trivial.

### §3.5 Validator status at S061 open

Per `tools/validate.sh` at S061 open: **1383 PASS / 0 FAIL / 29 WARN** (3 spec soft-warnings + 26 design-intent "no rejected alternatives" warnings). Tier 1 stable.

Tier 2 questions Q1-Q9 print at validator end. Q4 ("Is the methodology producing meaningful progress, or is it accumulating ceremony without advancing?") is the question the eight-session chain S051-S058 demonstrates is not being answered well. Q4 is paired with no Tier 1 check; it is purely guided-assessment.

## §4 Asymmetry mapping: MAD §Synthesis vs session-close Tier 2

The structural cause the intake identifies is the asymmetry between MAD-level synthesis discipline and session-close Tier-2 discipline:

### §4.1 MAD level (forbidden self-synthesis)

`multi-agent-deliberation.md` v4 §Synthesis: **"Synthesizer identity. The synthesizer must not have been one of the deliberation's perspectives. The synthesizer's identity (agent/model/date) is recorded in the synthesis file's frontmatter."**

The rule is structural: the synthesis is the highest-risk single-agent re-entry point per §Limitations ("The synthesis step is the pattern's highest-risk single-agent re-entry point"). Mitigations layer on (citation requirement; quote-over-paraphrase for load-bearing claims; preserve dissent; convergence-vs-coverage distinction; alphabetical synthesis-order anchoring). The synthesizer-identity rule is the floor.

The S050 + S058 MADs additionally implemented P4 cross-family-reviewer / laundering-audit role as a fourth perspective auditing P1+P2+P3 outputs. P4's brief specifically tracked criteria-strain selectivity; revision traceability; cross-session precedent neutrality; internal inconsistency; measurable-criteria adequacy; shared-frame-blindness. The role is bounded: it audits within the deliberation, recommends dissent-preservation, but does not re-write the synthesis.

### §4.2 Session-close Tier-2 level (tolerated self-validation)

`validation-approach.md` v5 §Limitations:

> "These deeper questions are the purpose of Tier 2, which depends on honest assessment by the agent or human conducting the session. **The methodology acknowledges that when a single AI agent both does the work and assesses it, Tier 2 is self-assessment rather than independent validation. This is a known limitation (see D-009), mitigated by making the questions explicit and recording the assessment in provenance,** and further mitigated since Session 005 by the D-023 non-Claude-participation rule for meta-deliberations on self-assessment mechanisms."

The rule names the limit; the mitigation is naming-as-mitigation + the D-023 non-Claude-participation rule for meta-deliberations. **Notably absent: a structural rule analogous to §Synthesis "the validator must not have been the doer."**

The intake's structural critique: **the engine forbids self-synthesis at MAD level but tolerates self-validation at session-close-Tier-2 level.** The asymmetry is not principled — both surfaces are highest-risk single-agent re-entry points; both involve judgement-not-mechanical-checks; both have observable laundering surfaces (manifests at MAD level; honest-limit drift at session-close level). The engine's discipline differs because the patterns differ in cost-and-frequency (MAD level fires every substantive deliberation; session-close level fires every session), but the cost differential does not by itself justify the discipline differential.

### §4.3 The asymmetry as design choice (not historical accident)

D-009 (Session 003) recognised the simulated-disagreement risk; D-023 (Session 005) added non-Claude-participation for meta-deliberations on self-assessment; the asymmetry-of-discipline has been preserved across 56 subsequent sessions without explicit re-deliberation. This is design-choice preservation by inertia, not by re-affirmed reasoning.

EF-058-tier-2-validation asks whether the asymmetry should be re-deliberated under the records-substrate's structural detection feasibility (§3.4) + the eight-session honest-limit chain's empirical demonstration (§3.1).

## §5 Mechanism candidate inventory

Per intake §Suggested-Change five candidate mechanisms (α)–(ε). Each is restated with concrete-shape detail, primary cost, primary value-add, and primary limitation. The S062 MAD will deliberate among them (or surface alternatives during independent-phase reasoning).

### §5α Mechanical detection only

**Concrete shape**: extend `tools/validate.sh` with new check 26 detecting honest-limit text repetition across §2c retention-window (6-session) `03-close.md` files. Substrate-aware extension uses `search` / `resolve_id` over records-substrate / provenance corpus. Implementation:

1. Walk §8 honest-limits sections in retention-window closes.
2. Compute near-duplicate clusters (string similarity threshold; e.g., Levenshtein distance < N or 5-gram overlap > threshold).
3. Emit WARN if any cluster spans ≥3 consecutive sessions; FAIL if ≥6.
4. Optional: substrate-augmented variant calls `mcp__selvedge-retrieval__search(<extracted-honest-limit-text>, k=10)` to find further matches across full corpus.

**Cost**: minimal implementation (~50-100 LOC bash + python). Zero per-session invocation cost beyond existing validate.sh runtime.

**Value-add**: catches honest-limit text repetition (the S051-S058 chain pattern). Substrate-aware variant catches the pattern across full corpus, not just retention window.

**Limitation**: cannot catch failed-tool-call patterns (no harness-telemetry-feed); cannot catch repeated-Read patterns (same); cannot judge "ceremony vs progress" semantically; can be gamed by paraphrasing (the threshold is text-similarity, not pattern-similarity); cannot catch shared-frame-blindness against operator-standing-instructions (the EF-058-claude-md-drift class).

**Engine-v impact**: minor per OI-002 if pure validate.sh extension. Single-session resolvable. Engine-v10 preserved.

### §5β Separate Claude reviewer subagent at session close

**Concrete shape**: launch a fresh Claude subagent (via TaskCreate-style harness or Agent tool) with access to:
- Current session's `03-close.md` (close narrative).
- Current session's `02-decisions.md` (decision records).
- Recent §8 honest-limits across §2c retention window (or §3.1 substrate `search` extraction).
- `tools/validate.sh` output for current session.

The subagent is briefed to flag:
- Repeated honest-limits (the S051-S058 pattern class).
- Ceremony-without-progress at Q4.
- Drift patterns from prior closes.
- Suspect Tier-2-self-report (e.g., affirmative Q4 with operationally-conventional honest-limits).

The subagent produces `provenance/<NNN-session>/04-tier-2-audit.md` (or similar) committed alongside close.

**Cost**: one subagent invocation per session + tokens-budget for review. Estimated 15-30K tokens per audit.

**Value-add**: independent reviewer (not the doer); catches honest-limit drift + ceremony-vs-progress with judgement; can highlight ceremony at Q4 the doer would not.

**Limitation**: shares Claude blind spots (training-distribution overlap with the doer); cannot reliably catch shared-frame-blindness against operator-standing-instructions because both Claude instances default to ignoring CLAUDE.md unless brief explicitly includes it; cannot catch failed-tool-call or repeated-Read patterns without harness-telemetry-feed (same limit as α).

**Engine-v impact**: minor per OI-002 if prompt amendment + subagent invocation pattern only; substantive if `prompts/development.md` §Validate / §Close substantively revised. Engine-v11 candidate.

### §5γ Cross-family reviewer

**Concrete shape**: same shape as (β) but mandates non-Claude family (codex/GPT or other) for engine-definition-touching sessions or substantive-arc sessions; optional for routine sessions. Reviewer invocation via `codex exec` (per S044 / S045 / S047 / S050 / S058 MAD precedent for non-Claude integration) producing the equivalent audit artefact.

**Cost**: one codex-CLI invocation per close + WX-44-1/WX-44-2/WX-47-1 codex-CLI discipline application. Estimated codex-pipeline turn-around ~3-7 minutes per audit.

**Value-add**: genuine cross-family independence (different training distribution; different blind spots); addresses CLAUDE-md-drift class shared-frame-blindness because non-Claude perspectives have different default-ignore-pattern for operator-standing-instructions; mirrors §Synthesis cross-family discipline at session-close.

**Limitation**: cost (one codex invocation per applicable close); cross-family availability constraints (codex CLI may be unavailable; refusal-on-precondition pattern observed at S058 P4); possibly excessive for non-substantive sessions; codex-CLI fragility (WX-47-1 argv `---` parsing; WX-44-2 model-version drift).

**Engine-v impact**: substantive per OI-002 (introduces non-Claude reviewer obligation; touches `multi-agent-deliberation.md` and `validation-approach.md`). Engine-v11 candidate.

### §5δ Combination (α) + (β/γ)

**Concrete shape**: mechanical detector (α) extends validate.sh + emits a triggered-list of candidate concerns (e.g., "honest-limit cluster spanning S051-S058"). Reviewer agent (β or γ) reads validate.sh output as input + judges the triggered concerns + recommends action. Concrete:

1. Validate.sh check 26 detects honest-limit text repetition + outputs structured WARN/FAIL list to `04-tier-2-flagged.md` or stderr-stream.
2. Reviewer subagent receives `04-tier-2-flagged.md` as input + close narrative + decisions.
3. Reviewer judges: (a) which flagged items are genuine concerns vs false-positives; (b) what action the close should take (revise close narrative; open OI; surface to operator); (c) optional concerns the mechanical detector missed.
4. Reviewer output committed as `04-tier-2-audit.md`.

**Cost**: validate.sh extension + one subagent invocation. Mechanical layer reduces reviewer cost by surfacing candidates; reviewer layer catches shared-frame-blindness the mechanical layer cannot.

**Value-add**: likely strongest cost-benefit shape per intake analysis. Mechanical detection is cheap-and-systematic; reviewer judgement is cross-family-independent (if γ variant) or fresh-Claude-perspective (if β variant). Together they cover the operational + structural detection surface.

**Limitation**: scope-discipline complexity (when does each layer fire?); reviewer's-own-laundering surface (per intake §Open-questions Q3); harness-telemetry-feed gap unresolved (failed-tool-calls + repeated-Reads still uncovered).

**Engine-v impact**: substantive. Engine-v11 candidate.

### §5ε Adversarial close-write protocol

**Concrete shape**: reviewer runs *before* close-writing, reviewing decisions + 00-assessment + accumulated provenance for the in-progress session. Reviewer surfaces concerns + must-address items as `pre-close-review.md`. Close-writer then must:

1. Address each concern in the close narrative (not annotate post-hoc).
2. Explicitly respond to each flagged item (accept / dispute / defer with rationale).
3. Reviewer optionally re-runs after close to check that concerns were addressed (second-pass).

**Cost**: reviewer invocation timing tied to close start, not close end. Adds ~5-15 minutes to session close. Reviewer cost depends on β-variant or γ-variant.

**Value-add**: strongest discipline because concerns shape the close rather than annotate it post-hoc. Closest to MAD §Synthesis discipline applied at session-close level — synthesis-time review is structural, not advisory. Catches ceremony at the point where ceremony would otherwise be embedded in the close narrative.

**Limitation**: highest cost (workflow complexity + invocation timing); structurally adversarial may produce friction at Halt-3 close ratification; close-writer must internalise the adversarial framing (which is easier said than done given the bootstrap-paradox concern).

**Engine-v impact**: substantive. Engine-v11 candidate.

### §5z Alternative architectures (for the MAD to consider beyond (α)-(ε))

The S062 MAD may surface alternatives beyond the five enumerated. Some candidates the synthesis surfaces but does not score:

- **(z1) Operator-audit channel formalisation**: codify operator-audit at substantive-arc resolving close as a one-time structural step (not just recommended). Lowest-cost; preserves existing structure; makes operator-audit a formal stage rather than an honest-limit-recommendation. Limitation: depends on operator availability + time; doesn't address routine sessions.
- **(z2) Honest-limit lifecycle records (Substrate-N3.5 extension)**: each honest-limit becomes a structured record at `records/honest-limits/HL-NNN.md` with frontmatter (session-introduced, status: open|resolved, resolving-session, resolution-disposition). Detection becomes mechanical (status enumeration); pattern-class-detection becomes substrate-native. Higher implementation cost; introduces records-substrate phase-N family.
- **(z3) Tier-3 validation introduction**: add a third validation tier explicitly scoped to "what Tier 1 cannot mechanically check and Tier 2 cannot self-validate" — i.e., the discipline-gap surface this record names. Tier-3 is by-design cross-family + adversarial. Replaces the asymmetry rather than patching it.
- **(z4) MAD §Synthesis discipline extended to session-close**: directly amend `multi-agent-deliberation.md` v4 §Synthesis or add a new §Session-Close-Synthesis section that applies the synthesizer-identity rule to close-narrative-write. Most direct fix; requires re-thinking the engine's session-vs-deliberation boundary.

The MAD may select among (α)-(ε) + (z1)-(z4) or surface novel combinations. The intake's five-candidate inventory is the floor, not the ceiling.

## §6 Cost/benefit matrix

The following matrix scores each direction against axes the S062 MAD will deliberate. Scores are qualitative (low / medium / high; yes / partial / no); ties indicate genuine open question for MAD deliberation.

| Axis | (α) Mechanical | (β) Claude reviewer | (γ) Cross-family reviewer | (δ) Combination α+β/γ | (ε) Adversarial close-write |
|------|----------------|---------------------|---------------------------|-----------------------|----------------------------|
| Independence-from-doer | partial (mechanical-not-judgement) | low (same model family) | high (different family) | high (with γ variant) | high (with γ variant) |
| Mechanical-vs-judgement | mechanical | judgement | judgement | hybrid | judgement |
| Cost-per-session | low | medium | high | high | high+ |
| Catches-honest-limit-drift | yes | yes | yes | yes | yes |
| Catches-failed-tool-calls | no (needs harness-telemetry) | partial (if transcript provided) | partial (if transcript provided) | partial | partial |
| Catches-repeated-Reads | no | partial | partial | partial | partial |
| Catches-ceremony-vs-progress | no | yes | yes | yes | yes |
| Catches-shared-frame-blindness | no | partial (same default-ignore) | yes (cross-family different defaults) | yes (with γ variant) | yes (with γ variant) |
| Cross-family-discipline | no | no | yes | optional | optional |
| Engine-v-impact | preserved or minor | engine-v11 candidate | engine-v11 candidate | engine-v11 candidate | engine-v11 candidate |
| Reversibility | high | medium | medium | medium | low |
| Scope-discipline | universal | scope-debate (all/some sessions) | scope-debate (engine-def-only) | scope-debate | scope-debate (high overhead) |
| Adversarial-discipline | weak | weak | medium | medium | strong (mirrors §Synthesis) |
| Bootstrap-paradox-handling | n/a (mechanical) | unsolved (same family) | partially-addressed | partially-addressed | partially-addressed |
| Combinable | yes (with β/γ) | yes (with α/ε) | yes (with α/ε) | n/a (already combined) | yes (with α/γ) |
| Forecloses-other-directions | no | no (preserves α/γ optionality) | no (preserves α/β optionality) | partial (subsumes α+β/γ) | partial (subsumes β/γ at close-time) |

**Key observations from the matrix**:

1. **(α) is the lowest-cost / lowest-coverage option**: catches honest-limit drift + nothing else. Operationally feasible immediately + substrate-aware. Limitation: judgement-blind; cannot catch ceremony vs progress.
2. **(β) is medium-cost / medium-coverage**: catches with judgement but shares Claude blind spots. Closest to the S050/S058 MAD P4 cross-family-reviewer pattern but at session-close level + same-family.
3. **(γ) is high-cost / high-coverage**: cross-family genuine independence; addresses CLAUDE-md-drift class shared-frame-blindness; mirrors §Synthesis cross-family discipline at session-close.
4. **(δ) is the strongest combination**: mechanical layer reduces reviewer cost; reviewer layer catches what mechanical cannot. Likely strongest cost-benefit per intake analysis.
5. **(ε) is the most disciplined**: structurally adversarial (close-writer addresses concerns proactively); closest mirror of MAD §Synthesis discipline. Highest cost; potentially produces close-time friction.
6. **All five candidates have unsolved harness-telemetry-feed gap**: failed-tool-calls + repeated-Reads patterns require transcript access not currently in scope. This is a separate engineering surface the MAD may or may not engage.

The MAD's deliberation should specifically address:
- Whether the asymmetry-of-discipline (forbidden self-synthesis vs tolerated self-validation) is principled or premature-formalisation per §10.4-M-class minorities.
- Whether (γ) or (δ) is the right shape given cost constraints + sustained-cross-family-practice question.
- Whether scope-discipline ("which sessions get reviewer treatment") should be universal / engine-def-only / substantive-arc-only / discretionary.
- Whether harness-telemetry-feed should be in-scope for this MAD or deferred.
- Whether the bootstrap-paradox is sufficiently addressed by operator-audit-at-resolving-close (per intake §Application-Scope-Disposition closing paragraph) or requires structural mechanism.

## §7 Cross-spec interactions

Direction (β)/(γ)/(δ)/(ε) substantive scope necessarily revisits multiple specs. The S062 MAD must consider these cross-spec interactions:

### §7.1 `validation-approach.md` v5 → v6 interactions (minimum substantive scope per any of (β)-(ε))

- **§Tier 2 Q4 / §Limitations**: substantive revision required for any (β)/(γ)/(δ)/(ε). The naming-as-mitigation language no longer holds if direction is adopted; replace with the structural mechanism.
- **New §Tier 2.5 or §Tier-3 section**: codifies the reviewer-agent role + invocation pattern + scope discipline.
- **Tier 2 questions Q1-Q9**: may extend with new Q10 paired with new validator check 26 (per (α)/(δ) variants).

### §7.2 `methodology-kernel.md` v6 §7 Validate interactions

- **§7 Workspace-validation paragraph**: amendment naming the reviewer-agent role at session-close. Substantive per OI-002 (kernel-touching = engine-v bump).
- Possibly **§9 Close**: amendment naming reviewer-invocation pattern at close-time (per (β)/(γ)/(δ)) or pre-close-time (per (ε)).

### §7.3 `multi-agent-deliberation.md` v4 interactions

- **§Synthesis**: the asymmetry the intake names is rooted here. If (γ) or (δ) is adopted, the synthesizer-identity rule's analogue at session-close is named explicitly + cross-referenced. Possibly extends §Synthesis to a §Cross-Family-Discipline section spanning both deliberation-synthesis and session-close-validation.
- **§Stance Briefs §1 methodology-context**: cross-linkage with EF-058-claude-md-drift. If (γ) reviewer reads CLAUDE.md as part of its brief, the brief-content rule should reflect this.
- **§When Non-Claude Participation Is Required**: extension to session-close validation per (γ)/(δ)?

### §7.4 `prompts/development.md` interactions

- **§Validate / §Close**: amendment naming reviewer-invocation pattern. Per direction adopted (timing varies (β)/(γ)/(δ)/(ε)).
- **§How to operate**: possibly amendment naming substrate-aware honest-limit drift detection per (α).

### §7.5 `tools/validate.sh` interactions

- **New check 26**: honest-limit text repetition detection per (α)/(δ). Constants: `HONEST_LIMIT_REPETITION_THRESHOLD_WARN=3`, `HONEST_LIMIT_REPETITION_THRESHOLD_FAIL=6`. Substrate-aware optional flag.
- **New check 27** (if (β)/(γ)/(δ)): reviewer-audit artefact presence at close per kernel/prompts amendment.

### §7.6 New spec section or new spec file (per direction adopted)

- If (γ) or (δ) introduces non-Claude reviewer obligation as a structural-mechanism: candidate new section in `validation-approach.md` v6 (e.g., §Cross-Family Tier 2 Discipline) or new spec file `specifications/session-close-validation.md` v1.
- If (ε) adversarial close-write protocol: candidate new section in `prompts/development.md` § Adversarial Close-Write or new spec file capturing the protocol.

### §7.7 `read-contract.md` v6 interactions

- If reviewer reads beyond default-read surface (e.g., transcript / harness-telemetry-feed): read-contract.md may need extension. Likely deferred to harness-telemetry-feed sub-deliberation per intake §Open-questions Q4.

### §7.8 `records-contract.md` v1 interactions

- If (z2) honest-limit lifecycle records is adopted as alternative architecture: new family `records/honest-limits/` per `records-contract.md` phase-N. Out-of-scope at S062 MAD unless adopted as combination.

### §7.9 `tools/build_retrieval_index.py` interactions

- If (z2) or substrate-aware (α): record-aware indexing extension may apply. Engine-v10 D-214 §β extract_record_frontmatter_canonical helper precedent applies.

## §8 S062 MAD pre-ratification

### §8.1 MAD shape

**Recommended**: 4-perspective two-family MAD per D-133 M2 standing-discipline lineage-constraint matrix per S050 D-172 / S058 D-200 precedent.

**Family composition**: 2 Claude + 2 Codex/GPT-5.5 (or other non-Claude available at S062 time). Per `multi-agent-deliberation.md` v4 §When Non-Claude Participation Is Required, this is required for any decision that "Creates or substantively revises any specification in `specifications/`" (d016_2 trigger; substantive revision to `validation-approach.md` is the substantive scope of (β)-(ε)) AND "Creates or substantively revises `validation-approach.md` in ways that touch semantic (Tier 2) validation" (d023_3 trigger). **Cross-family is essential because the question itself is "what cross-family discipline should apply at session close"** — a Claude-only deliberation has the same conflict-of-interest the question is investigating.

**OI-004 d023 implications**: the MAD does not propose OI-004 state-change; d023_4 does not fire by default. Non-Claude participation remains required per d023_3 (substantively revises `validation-approach.md` in ways that touch semantic Tier 2 validation).

### §8.2 Perspective composition (recommended; for S062 MAD-session itself to ratify per S050/S058 precedent)

Per S050+S058 lineup precedent (P1 Substrate Architect / P2 Incrementalist Skeptic-Conservator / P3 Outsider Frame-Completion / P4 Cross-Family Reviewer Laundering-Audit), the natural S062 lineup is:

- **P1 Validator Architect (Claude Opus 4.7)** — defends a substantive direction ((β)/(γ)/(δ)/(ε)); surveys structural-mechanism design; addresses scope-discipline + cost trade-offs. Equivalent role-shape to S050 P1 Substrate Architect / S058 P1 Substrate-Methodology Architect.
- **P2 Incrementalist Conservator (Claude Opus 4.7)** — defends (α) or status-quo (asymmetry preservation); surveys cost-of-disruption; argues opportunity cost; defends naming-as-mitigation if defensible. Equivalent role-shape to S050 P2 / S058 P2.
- **P3 Outsider / Frame-Completion (Codex/GPT-5.5)** — surveys reframe alternatives ((z1)-(z4); novel architectures; cross-cutting reframes the synthesis missed); names blind spots in Claude perspectives. Equivalent role-shape to S050 P3 / S058 P3.
- **P4 Cross-Family Reviewer / Laundering-Audit (Codex/GPT-5.5)** — audits P1+P2+P3 outputs for laundering; convergence-check; preserved-minority recommendations. Equivalent role-shape to S050 P4 / S058 P4. **Note**: P4's role at this MAD is structurally the in-deliberation-instance of the discipline being deliberated. The MAD itself exercises a version of the cross-family-reviewer mechanism it considers adopting at session-close level.

**Per-perspective brief structure** per `multi-agent-deliberation.md` v4 §Stance Briefs:

1. Methodology context (shared, byte-identical) — Selvedge / engine-v10 / EF-058-tier-2-validation framing + records-substrate availability + S051-S058 honest-limit chain quantification + asymmetry mapping.
2. Problem statement (shared) — Tier 2 self-validation discipline gap; eight-session honest-limit chain as concrete instance + the meta-pattern subsuming EF-058-uv-migration + EF-058-claude-md-drift.
3. Design questions (shared) — see §8.3 below.
4. Role-specific stance (varies per perspective).
5. Response format (shared) — markdown per S050/S058 brief shape.
6. Constraint on external imports (shared).
7. **Brief-extension per EF-058-claude-md-drift cross-linkage**: brief MUST include `CLAUDE.md` content as part of methodology-context per intake §Suggested-Change closing paragraph: "The deliberation that picks among these (or surfaces a (f) reframe) should itself respect this concern by reading CLAUDE.md as part of its shared brief — proving the discipline by exercising it."

### §8.3 Design questions for S062 MAD

The MAD must address (questions for S062 brief):

- **Q1 — Primary direction choice**: (α), (β), (γ), (δ), (ε), or alternative ((z1)/(z2)/(z3)/(z4))? Justify with cross-axis reasoning per §6 matrix.
- **Q2 — Asymmetry assessment**: is the MAD §Synthesis vs session-close Tier-2 asymmetry principled (and should be preserved per (α) or status-quo) or premature-formalisation (and should be patched/extended per (β)-(ε))?
- **Q3 — Scope-discipline**: which sessions get reviewer treatment? All? Engine-definition-touching only? Substantive-arc-class only? Operator-discretionary? Cost discipline.
- **Q4 — Reviewer's-own-laundering surface**: what prevents the reviewer from passing every close as fine because that's the lower-effort answer? Mechanical metrics? Random spot-check operator audit? Mandatory-finding-floor?
- **Q5 — Harness-telemetry-feed**: should the reviewer have access to the session's tool-call transcript (Read/Bash/Edit/Write/etc. invocation log) to detect failed-tool-call + repeated-Read patterns? In-scope at S062 or deferred?
- **Q6 — Cross-spec interactions**: §7.1-§7.9 above — which interactions are in-phase-3 scope vs deferred?
- **Q7 — Multi-session arc shape**: 2 sessions (S062 MAD + S063 adoption) vs 3+ sessions (staged adoption)?
- **Q8 — Cross-linkage with EF-058-claude-md-drift**: joint scope (resolving both records in one MAD-arc) vs separate scope (sequential MAD-arcs)? If joint, S062 MAD must explicitly address shared-frame-blindness against operator-standing-instructions; if separate, S062 surfaces direction (a) of EF-058-claude-md-drift §Suggested-Change as scope-coherent recommendation for its MAD.
- **Q9 — Bootstrap-paradox handling**: is operator-audit-at-resolving-close (per intake §Application-Scope-Disposition) sufficient, or does the resolution require additional mechanism (e.g., post-resolution validator check on Tier-2-self-validation-instances; standing operator-audit cadence)?
- **Q10 — Recursive question**: if the resolution introduces a cross-family reviewer for session-close, does that reviewer mechanism extend to MAD-level deliberations (auditing P4's audit) or only to session-close? Backward integration question.

### §8.4 S062 MAD execution shape

**Single-session MAD** at S062 (not multi-session per perspective). Independent-phase per `multi-agent-deliberation.md` v4: 4 perspectives reason independently from shared brief; synthesis after all return; decision per `02-decisions.md`.

**Phase-3 adoption** (post-MAD): 1-2 sessions per direction adopted. (α)/(z1) single-session resolvable. (β)/(γ)/(δ)/(ε)/(z2)/(z3)/(z4) substantive scope; possibly multi-session.

### §8.5 Honest limits on MAD pre-ratification

- This synthesis does NOT pre-commit (α)/(β)/(γ)/(δ)/(ε)/(z*) choice. The MAD deliberates.
- This synthesis does NOT pre-commit perspective composition. The MAD-session ratifies its own composition first per S050/S058 precedent.
- This synthesis does NOT pre-commit phase-3 adoption shape. That depends on direction adopted.
- The cost/benefit matrix in §6 is qualitative; the MAD may dispute scoring.
- The cross-spec interaction list in §7 is the Case Steward's enumeration; the MAD may identify additional interactions.

## §9 Open questions for S062

Beyond the §8.3 design questions, the MAD should consider:

1. **Scope of reviewer's authority**: can the reviewer block close commit (must-address) or only annotate (may-address)? Block-authority introduces close-friction risk; annotate-only introduces compliance-by-paper-trail risk.

2. **Reviewer's accountability**: per `multi-agent-deliberation.md` v4 §Synthesis citation requirement + dissent-preservation precedent, the reviewer's audit should cite specific artefacts + sections + flagged claims. Format-discipline candidate: review-report frontmatter + structured findings + per-finding-disposition.

3. **What constitutes "ceremony vs progress" operationally**: Tier 2 Q4 has been answered implicitly-affirmatively across the eight-session chain because no concrete falsifying definition was operationalised. The MAD may need to articulate "ceremony" as a specific pattern (e.g., honest-limit text drift + zero-progress on the named gap + operational-conventions-not-design-decisions).

4. **Failure mode of (γ)/(δ) under non-Claude unavailability**: the WX-44-1 / WX-44-2 / WX-47-1 codex-CLI discipline chain shows non-Claude availability is not always reliable. What is the close-discipline if codex-CLI fails? Skip-with-honest-limit-recording (analogous to non-Claude-skip annotation per multi-agent-deliberation §Opt-out)? Defer-close? Fallback to (β) Claude-reviewer with explicit cross-family-not-available annotation?

5. **Session-class boundary**: the intake names "engine-definition-touching sessions" and "substantive-arc sessions" as candidate scope-boundaries. The MAD may need to operationalise session-class detection (heuristics: session edits any spec; session has any d016_* trigger; session adopts new artefact-class). Without an operational definition, scope-discipline becomes manual-judgement.

6. **Cross-linkage with EF-058-claude-md-drift directions**: if joint-scope (per Q8), the MAD adopts BOTH a Tier-2 reviewer mechanism AND the §Stance-Briefs §1 amendment (per EF-058-claude-md-drift direction (a)). Compatible but adds MAD-arc complexity. If separate-scope, S062 MAD surfaces direction (a) as forward-recommendation for the next claude-md-drift MAD.

7. **Operator-audit cadence formalisation**: per intake §Application-Scope-Disposition closing paragraph, operator-audit at resolving close is recommended one-time. Should operator-audit be formalised as a recurring cadence (e.g., every Nth substantive-arc; every engine-v bump) or remain ad-hoc?

8. **Records-substrate phase-N for honest-limits**: alternative architecture (z2). Honest-limit lifecycle records would make detection structural rather than text-similarity-based. Out-of-scope at S062 MAD unless joint-scoped, but worth flagging as forward arc.

9. **Reviewer-as-MAD-perspective vs reviewer-as-distinct-role**: the S050/S058 P4 cross-family-reviewer is a perspective-within-MAD (audit happens during deliberation). The candidate session-close reviewer is a distinct-role-after-session (audit happens after deliberation closes). The S062 MAD may surface whether to unify these roles (single cross-family-reviewer-at-session-scope spanning MAD + close) or keep distinct.

10. **Validator-tier ambiguity**: introducing Tier 2.5 / Tier 3 raises the question of whether validate.sh should run before or after the reviewer. Current discipline runs validator at session-open + before-Produce + before-Close. Reviewer would run at close (or pre-close per (ε)); ordering with validate.sh matters for which artefacts are reviewed.

## §10 Honest limits on this synthesis

1. **Single-orchestrator synthesis (no parallel research sub-agents).** Per S057 §9 honest-limit 1 precedent. EF-058-tier-2-validation scope is mechanism-survey (5 named candidates (α)-(ε) + alternative architectures (z1)-(z4)) more than technology-survey; single-orchestrator synthesis is appropriate per S057 / S049 D-158 single-orchestrator design-space.md precedent.

2. **The Case Steward writing this synthesis is exhibiting the discipline-gap pattern under examination.** The bootstrap paradox is structural and acknowledged at §honest-limit 4 below. Phase-1 synthesis is single-orchestrator by precedent + scope (option-mapping not decision-making); phase-2 MAD is cross-family by mandate. The cross-family discipline being deliberated is exercised at phase-2; phase-1's role is appropriate scope for single-orchestrator work even under the bootstrap-paradox concern. **However, this honest-limit is itself a Tier-2-self-validation case** (the agent identifies the bootstrap-paradox while exhibiting it; recording-as-mitigation is the same shape the engine has been using since D-009). Operator-audit at resolving close is the cross-check per intake recommendation.

3. **Mechanism candidate inventory may be incomplete.** §5 lists (α)-(ε) from intake plus (z1)-(z4) Case Steward alternatives. The S062 MAD may identify additional mechanisms or alternative shapes during independent-phase reasoning.

4. **Cost/benefit matrix scores are qualitative.** §6 scores are Case Steward's assessment; the S062 MAD may revise. Quantitative measurement (cost-per-session in tokens or wall-clock; coverage-of-failure-modes via empirical instance count) is the MAD's deliberation surface, not pre-committed by this synthesis.

5. **Cross-spec interaction enumeration is bounded by Case Steward awareness.** §7 lists known interactions. The S062 MAD may identify additional interactions during independent-phase reasoning, particularly cross-cutting concerns (e.g., harness-telemetry-feed implications for read-contract.md; records-substrate interactions if (z2) is adopted).

6. **Bootstrap paradox is structurally inherent and partially-addressed.** Per intake §Application-Scope-Disposition closing paragraph: "the resolving session(s) will exercise discipline they are deciding to formalise, and that exercise itself is observable evidence the MAD's reasoning + decision can be checked against. Operator audit at the resolving close is recommended as a one-time cross-check." The S061 phase-1 synthesis is single-orchestrator by precedent; the S062 phase-2 MAD is cross-family by mandate — the discipline being deliberated is exercised at phase-2. The recursive concern (the MAD exercising the discipline it formalises) is feature, not bug.

7. **CLAUDE.md content read at synthesis time** per EF-058-claude-md-drift cross-linkage. The CLAUDE.md instruction is read into this synthesis implicitly via Read-discipline coverage at session open; the question of whether CLAUDE.md should be EXPLICIT in MAD shared-context is the EF-058-claude-md-drift deliberation surface and is surfaced for S062 MAD via §8.2 brief-extension recommendation.

8. **The eight-session honest-limit chain S051-S058 closes operationally at S061 open** per §3.4 substrate-aware verification. The chain's substantive instance is resolved; its meta-pattern (Tier 2 self-validation laundering) is what S061 phase-1 + S062+ MAD address. Honest-limit text "MCP stdio transport remains unverified" SHOULD NOT propagate into S061 close §8 — propagating it would itself exhibit the laundering pattern this synthesis surfaces.

9. **Direction (γ) cross-family reviewer would itself produce evidence about (γ)'s viability across multiple subsequent close-applications.** The same data-loop the records-substrate phase-2 gate uses (WX-58-1 5-field recording across 3 sessions) could apply to (γ) adoption: 3-session observation window post-(γ)-adoption recording (review-completed: yes/no; review-flagged-issues: count; reviewer-cost: tokens-or-wall-clock; review-overridden: yes/no). The MAD may consider this phase-2-gate analogue.

10. **Read-discipline coverage at synthesis time**: per S061 00-assessment §7 honest-limit 8: methodology-kernel.md v6 / multi-agent-deliberation.md v4 / validation-approach.md v5 / records-contract.md v1 / read-contract.md v6 / workspace-structure v7 freshly read at S061 open ✓; S057 design-space.md in full ✓ (Phase-1 precedent template); S058+S059+S060 closes in detail ✓; EF-058-tier-2-validation inbox + triage in full ✓; EF-058-claude-md-drift inbox in full ✓. **Honest-limit deferred**: S055+S056 closes not freshly re-read in detail at S061 open beyond their content as referenced via S057-S060 close §3+§7+§8 narratives. S050 raw perspectives + S058 raw perspectives (P3+P4 cross-family-reviewer/laundering-audit role-shape templates) referenced via design-space.md citations rather than fresh re-read at synthesis time. Recorded transparently per WX-22-1.

## §11 What this document is and is not

This is a **design-space synthesis**, not a decision record. It maps the deliberation surface for S062. It explicitly does NOT:
- Foreclose (α)/(β)/(γ)/(δ)/(ε)/(z*) choice.
- Pre-commit the perspective composition.
- Pre-commit the phase-3 adoption shape.
- Pre-commit the multi-session arc length.
- Pre-commit cross-spec amendment scope.
- Pre-commit joint-scope vs separate-scope with EF-058-claude-md-drift.

It DOES:
- Restate the problem under EF-058-tier-2-validation framing including the meta-pattern subsuming EF-058-uv-migration + EF-058-claude-md-drift.
- Quantify the eight-session MCP-transport-unverified honest-limit chain S051-S058 via substrate-aware search.
- Map the asymmetry between MAD §Synthesis (forbidden self-synthesis) and session-close Tier-2 (tolerated self-validation).
- Inventory mechanism candidates (α)-(ε) from intake + (z1)-(z4) alternative architectures.
- Score cost/benefit qualitatively across 16 axes × 5 candidates.
- Enumerate cross-spec interactions for the MAD to consider.
- Pre-ratify the S062 MAD shape (4-perspective two-family per D-133 M2 + S050/S058 lineup precedent).
- Pre-recommend perspective composition (with explicit "MAD ratifies own composition first" honest-limit).
- Frame design questions Q1–Q10 for the MAD brief.
- Surface 10 open questions that the MAD should consider beyond Q1-Q10.

## §12 Pre-ratification of S062 MAD

Per `multi-agent-deliberation.md` v4 §When Multi-Agent Deliberation Is Required + S048 D-155 / S049 D-159 / S050 D-172 / S057 D-196 / S058 D-200 precedent chain:

- **S062 = dedicated MAD session for EF-058-tier-2-validation** per S061 D-218 ratification (this session's close) + this design-space.md as input.
- **Shape**: 4-perspective two-family MAD per D-133 M2.
- **Family composition**: 2 Claude + 2 Codex/GPT-5.5 (or other non-Claude available; lineup ratified by S062 MAD itself per S050/S058 precedent).
- **Perspective composition** (recommended for S062 MAD-session to ratify): P1 Validator Architect / P2 Incrementalist Conservator / P3 Outsider Frame-Completion / P4 Cross-Family Reviewer Laundering-Audit. Roles mirror S050/S058 lineup adapted for EF-058-tier-2-validation substantive scope.
- **Brief structure**: standard per `multi-agent-deliberation.md` v4 §Stance Briefs **+ brief-extension including CLAUDE.md content per EF-058-claude-md-drift cross-linkage** (proves the discipline by exercising it).
- **Design questions Q1–Q10**: per §8.3 above.
- **Open questions for MAD consideration**: per §9 above (10 questions).
- **Engine-v impact**: engine-v11 candidate iff (β)/(γ)/(δ)/(ε)/(z2)/(z3)/(z4) adopted; engine-v10 minor amendment iff (α)/(z1) adopted; engine-v10 preserved iff status-quo (no direction adopted).

The S062 session-open should: read this design-space.md in full as primary input; re-read S050+S058 raw perspectives for cross-family-reviewer/laundering-audit role-shape templates; ratify perspective composition; commit briefs including CLAUDE.md content per `multi-agent-deliberation.md` v4 §Brief immutability; convene parallel sub-agents (Claude perspectives) + codex CLI invocations (non-Claude perspectives); synthesise; decide; commit.

The S061 close pre-ratifies this S062 shape. The S062 session itself is the next operational step.

**Operator audit at S062+ resolving close is recommended as one-time cross-check** per intake §Application-Scope-Disposition closing paragraph: the bootstrap-paradox concern (the MAD exercising the discipline it formalises) is feature, not bug, and operator audit is the meta-cross-check on that observable evidence.
