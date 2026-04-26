---
session: 072
title: Design-space — phase-3 (γ) harness-telemetry digest implementation arc per S071 D-268 VD-003 lifecycle row + S071 D-263 (ε) hybrid composition; surveys (z6) digest schema + capture mechanism selection (CM1/CM2/CM3) + producer_kind/authority_level field semantics + cross-spec interactions for validation-approach.md v7 → v8 + reviewer-prompt-template extension scope + Q1-Q10 design questions; pre-ratifies S073 phase-2 MAD shape per S057 D-196 + S061 D-219 + S068 D-251 + S070 D-260 phase-1-pre-ratifies-phase-2 precedent
date: 2026-04-26
status: complete
---

# Design-space — Session 072 (phase-3 (γ) harness-telemetry digest implementation arc)

## §1 Purpose of this document

This design-space surveys the choice surface for the **γ phase-3 implementation arc** activated at S071 D-268 + VD-003 lifecycle row (status: open; review_by_session: S076; introduced_session: S071). The arc was deferred from S071 phase-2 MAD adoption to S072+ multi-session per S062 D-220 phase-3-arc precedent + S071 D-263 (ε) hybrid bounded-then-extended composition (β-phase same-session-bounded at S071 close + γ-phase multi-session at S072+).

The document does not pre-decide direction. Per S057 D-196 + S061 D-219 + S068 D-251 + S070 D-260 phase-1-pre-ratifies-phase-2 precedent extended to phase-3-arc scope, phase-1 design-space synthesizes choice surface; phase-2 MAD at S073 deliberates direction across cross-family-weighted-convergence; phase-3 implementation at S074+ adopts and ships per direction selected.

The intended consumers are: (a) the S073 phase-2 MAD's perspectives — each receives this design-space as brief-extension, with stance-brief slots referencing its §3-§7 surveys; (b) the operator, who may amend scope or direction via §10.4-M10 written-warrant clause (c) at any time before S073 MAD execution; (c) future readers reconstructing the γ phase-3 arc's design-space as it stood at S072.

## §2 Problem restatement under γ-specific scope

S071 phase-2 MAD adopted (ε) hybrid bounded-then-extended composition per cross-family weighted convergence (3-of-4 across families: P2 Claude + P3 codex + P4 codex; P1 Claude dissent on full (γ)-immediate preserved as §10.4-M26). The β-phase Direction 1 (a)+(b)+(c)+(d) adopted at S071 close codifies substrate-use-required at session-open in `prompts/development.md` engine-v13 substantive revision + structured-declaration requirement + check 29 WARN-only enforcement. The γ-phase deferred elements are:

1. **EF-068-substrate-load-bearing Direction 1 (e)**: implement `tools/validate.sh` check 26 substrate-aware branch — replaces inline-comment placeholder with operational substrate call.

2. **EF-068-substrate-load-bearing Direction 2 (D2.1 vs D2.2)**: extend EF-059 (z6) digest scope to orchestrator-side read-discipline telemetry; make digest Tier 2.5 reviewer input always-available-always-read (D2.1) vs available-at-best-effort (D2.2).

3. **EF-059 full (z6) harness-telemetry digest implementation**: capture mechanism + digest schema + reviewer-prompt-template extension + `validation-approach.md` v7 → v8 substantive revision codifying digest specification + §Tier 2.5 audit-shape extension making digest reviewer-input.

4. **EF-067 Direction B subsumption into EF-059 (z6) digest scope**: deprecate `duration_minutes` + `reviewer_cost` self-report fields in favor of harness-measured `reviewer_invocation_wall_clock_seconds` + `reviewer_invocation_token_count` per VD-003 phase-3 gating.

5. **Measurement-authority separation reframe (substantively adopted at S071 D-263 §5.1; preserved at §10.4-M28)**: digest records MUST distinguish `producer_kind: harness-measured | post-hoc-reconstructed | agent-declared` + `authority_level`. Without distinction, future sessions launder CM4 into γ via YAML shape alone.

The γ phase-3 arc resolves these elements jointly per S071 D-263 (ε) hybrid composition. The phase-3 design-space at S072 surveys the choice surface within this scope; the phase-2 MAD at S073 deliberates direction.

## §3 Workspace state at S072 design-space production

### §3.1 β-phase substrate-use observation window state (n=2 evidence at S072)

| Session | Substrate calls at session-open | β-phase compliance | Hawthorne-effect / durable-behavior distinction |
|---------|----------------------------------|---------------------|--------------------------------------------------|
| S071 | non-zero (forward_references + 3 resolve_id) | adoption session; codification at close | adoption-time exercise; awareness-driven by definition |
| S072 | non-zero (forward_references('S072') = 117 hits at session-open per 00-assessment §3b) | first observation point post-codification | n=1 in observation window; cannot distinguish |

Pattern at S072: n=2 substrate-exercise sessions (S071 + S072); the n=5 substrate-non-use chain S067-S070 BROKEN at S071 is sustained at S072. Per VD-003 phase-3 gating condition (b): observation window data on β-phase substrate-use across S072-S076 inclusive distinguishes durable behavior change from design-space-salience compliance. n=2 is insufficient for adjudication; n=4-5 across S073-S076 will provide first triangulation.

The empirical question is testable: if S073-S076 sustain substrate-exercise pattern across heterogeneous Path-shapes (Path-AS phase-2 MAD at S073 + likely Path L or Path-AS phase-3 implementation at S074+ + Path A or Path T at S075-S076 per typical post-arc cadence), then the β-phase codification is empirically sufficient for the substrate-use-at-session-open discipline. If the pattern decays (e.g., n=0 at S074-S076 post-novelty-fade), then γ harness-side-enforcement-or-measurement is structurally required.

Per the §10.4-M27 P2 (γ)-deferral-criteria reopen warrant (c): "(z6) digest produces n≥3 sessions of measured behavior that diverges from spec-side expectation in ways β would have caught". The criterion is testable post-γ implementation; the pre-γ observation window (S072-S076) tests the converse: does β-phase succeed without γ?

### §3.2 Reviewer self-report propagation surface post-S071 D-264 §Tier 2.5 honest-limit subsection

Per `validation-approach.md` v7 §Tier 2.5 reviewer self-report honest-limit subsection (added per S071 D-264 + EF-067 Direction C from cross-family weighted convergence):

The §10.4-M25 P1 audit-cost-budget threshold arithmetic on self-reported values is suspended at S071 D-264 pending harness-measurement availability per the (γ) phase-3 (z6) digest arc per VD-003 lifecycle row + S072+ phase-3 design-space. Direction B subsumption per EF-067 cross-linkage with EF-059 (z6) extended scope is the targeted resolution: phase-3 (γ) digest fields will carry `producer_kind: harness-measured` distinguished from current `producer_kind: agent-declared` semantics per measurement-authority separation reframe substantively adopted at S071 D-263 §5.1 of synthesis (P3-originated; P4-endorsed; cross-family-originated-and-adopted-at-MAD-execution reframe-architecture pattern reified at n=4 — S058 + S062 + S064 + S071).

The cost-observation surface remains preserved with explicit caveat for cross-session pattern observation only (e.g., reviewer-cost trajectory may surface cadence-of-passivity signal even with imprecise absolute values; the §10.4-M25 P1 reopen-warrant text remains preserved as forward-observation discipline; the threshold arithmetic ("reviewer-cost growth >2× over S063 baseline") is suspended at S071 D-264 with the v7 amendment).

The phase-3 (γ) digest implementation arc resolves this surface: harness-measured reviewer invocation wall-clock + token count replace self-report for the threshold arithmetic surface; the §10.4-M25 P1 reopen-warrant becomes operationally meaningful again post-γ.

### §3.3 (z6) digest activation precondition state at S072

Per S062 D-225 + EF-059 intake §Suggested Change activation preconditions (all three required):

- **(a) Reviewer mechanism (Layer 2 (γ)) adopted at S063** per S062 D-221 phase-3 adoption. ✓ at S063 close (engine-v11 ratified).
- **(b) Reviewer operating across ≥3 sessions** per WX-62-1 observation window completion. ✓ at S067 close (3-of-3); extended at S071 close (4-of-4 with Gemini reviewer audit per Layer 2 trigger (a)+(b)+(d) multiple-fires).
- **(c) ≥1 instance documented where harness-telemetry digest (z6) would have caught failed-tool-call or repeated-Read pattern** given digest access. ✓ at S067 (extended per EF-067 to "harness-measured duration would have caught reviewer self-report inaccuracy").

**Plus VD-003 phase-3 activation gating conditions per S071 D-268** (must be discharged at phase-3 implementation):

- **(a) Capture mechanism selection** (CM1 vs CM2 vs CM3 with appropriate `producer_kind`); operationally tractable selection. **Status at S072**: design-space surveys CM1/CM2/CM3 trade-offs (this document §5); selection deferred to S073 phase-2 MAD per design-space-then-decide discipline.
- **(b) Observation window data on β-phase substrate-use** distinguishes durable behavior change from design-space-salience compliance. **Status at S072**: n=2 observation evidence per §3.1; window continues through S076 review.
- **(c) Digest schema specification with `producer_kind` + `authority_level` finalisation** per measurement-authority separation reframe. **Status at S072**: design-space surveys schema (this document §5.4 + §6); finalisation deferred to S073 phase-2 MAD + S074+ phase-3 implementation.

### §3.4 Cross-spec landscape at S072

| Spec | Version | (γ)-phase-3 impact |
|------|---------|---------------------|
| `validation-approach.md` | v7 | substantive v7→v8 candidate per (γ) digest spec addition + §Tier 2.5 audit-shape extension |
| `prompts/development.md` | engine-v13 | already substantively revised per S071 D-264 (β-phase); minor revision possible per (γ) digest cross-reference |
| `tools/validate.sh` | engine-v13 | check 29 already added per S071 D-264 (β-phase WARN-only); check 26 substrate-aware branch implementation per (γ) candidate; potentially new check 30 for (z6) digest record presence |
| `read-contract.md` | v6 | potentially v6→v7 candidate per §1 enumeration extension to add `harness-telemetry-digest.yaml` as required per-session-provenance file |
| `retrieval-contract.md` | v1 | scope unchanged per (γ) substrate primitives; substrate availability already required-precondition per β-phase |
| `records-contract.md` | v1 | scope unchanged per (γ); records-substrate phase-2/3 promotion of digest record deferred per S062 §10.4-M18 reopen warrant |
| `methodology-kernel.md` | v6 | scope unchanged per (γ); §7 Validate scope is harness-side-supplemented, not redefined |
| `multi-agent-deliberation.md` | v4 | scope unchanged per (γ); §Stance Briefs + §Graceful Degradation already cross-referenced from prompts/development.md per β-phase |
| `workspace-structure.md` | v9 | minor amendment candidate per (γ): §10.4-M26 through §10.4-M29 status updates per phase-3 outcome; new minorities possible per S073 phase-2 MAD |
| `engine-manifest.md` | engine-v13 | new engine-version entry per (γ) phase-3 adoption (engine-v14 candidate at S074+ phase-3 implementation close) |

### §3.5 Validator state at S072 open

Pre-session validator (final at S071 close): 1668 PASS / 0 FAIL / 39 WARN. Aggregate 90,309 / 90K soft (309 over). Check 26 PASS; check 27 BLOCKED (no Layer 2 trigger fired at session-open); check 28 PASS (3 lifecycle rows VD-001+VD-002 resolved + VD-003 open well-formed); check 29 PASS expected at S072 close per structured substrate declaration in 00-assessment + close.md mirror.

## §4 The γ scope's structural surface

### §4.1 Measurement-authority separation as the load-bearing schema decision

Per S071 D-263 §5.1 of synthesis (P3-originated; P4-endorsed; substantively adopted): digest records MUST distinguish `producer_kind` field with three values:

- **`harness-measured`**: produced by harness-side instrumentation (CM1 PreToolUse/PostToolUse hooks; CM2 external wrapper). Authority: primary. Verifiability: high (harness layer is opaque to agent self-report; agent cannot edit).

- **`post-hoc-reconstructed`**: produced by post-session analysis of harness-recorded transcript (CM3). Authority: secondary. Verifiability: medium (transcript is harness-recorded; reconstruction-script behavior is agent-mediated and may diverge from transcript ground-truth).

- **`agent-declared`**: produced by agent self-report at decision-time emission (CM4; explicitly rejected per S071 D-263 + §10.4-M29 P4 bundling-by-laundering audit) OR by orchestrator self-report in prose (the S071 D-264 β-phase structured declaration is currently `agent-declared` until backed by harness telemetry per check 29 honest-limit). Authority: tertiary. Verifiability: low (reflective self-report subject to laundering surface that EF-067 + EF-068 surface).

**Plus `authority_level` field**: numeric ordinal (1=primary, 2=secondary, 3=tertiary) OR enum (`primary | secondary | tertiary`) explicit in schema. The field is structurally redundant with `producer_kind` at first iteration; the question for the design-space is whether redundancy is desirable for reviewer-readability or compactness preferred.

### §4.2 Capture mechanism is the operational choice

Three remaining capture mechanism candidates per S071 D-263 framing (CM4 explicitly rejected):

- **CM1: Claude Code hook surface** (PreToolUse + PostToolUse hooks emit structured records to `provenance/<NNN-session>/harness-telemetry-digest.yaml`). Mechanism: native Claude Code hook configuration in `.claude/settings.json` per `update-config` skill scope. Authority: primary (harness-emitted). Portability: cross-Claude-Code-workspace; not cross-harness-tool (e.g., not portable to OpenAI Codex CLI without hook-equivalent).

- **CM2: External telemetry capture wrapper**. Mechanism: shell script wraps the Claude Code session; intercepts tool invocations via stdio multiplex or process-tree introspection; emits digest. Authority: primary (external-process-emitted; harness-layer-equivalent). Portability: cross-harness-tool (any CLI agent wrapping is feasible); not cross-IDE (Claude Code IDE extension does not expose stdio for wrapper).

- **CM3: Substrate-augmented post-session analysis**. Mechanism: extension to `tools/build_retrieval_index.py` parses Claude Code transcript file; reconstructs digest post-hoc. Authority: secondary (post-hoc-reconstructed). Portability: highest (transcript format is stable across Claude Code versions; reconstruction is offline).

Trade-off summary:

| Mechanism | Authority | Portability | Implementation cost | Cross-workspace deployment |
|-----------|-----------|-------------|----------------------|------------------------------|
| CM1 | primary | medium (Claude Code only) | low (hook config + emit-to-yaml) | per-workspace `.claude/settings.json` setup |
| CM2 | primary | high (cross-harness-tool) | medium (wrapper script + protocol) | per-workspace wrapper invocation discipline |
| CM3 | secondary | highest (offline reconstruction) | medium-high (transcript parsing + reconstruction script) | per-workspace tool-script setup |

Per S071 D-263 framing: **CM1 preferred** / CM2 acceptable / CM3 acceptable as bridge. The S073 phase-2 MAD's central capture-mechanism question is whether to pre-commit CM1 (preferred direction) or whether CM2 + CM3 deserve substantive consideration as primary implementations; the design-space surveys all three.

### §4.3 Schema scope: original EF-059 (z6) + EF-068 Direction 2 extension

Per S070 design-space §5.4 schema candidate (preserved as starting-point for S072 phase-3 design-space):

```yaml
session: <NNN>
captured_at: <ISO-8601>
producer_kind: harness-measured | post-hoc-reconstructed | agent-declared  # NEW per §10.4-M28
authority_level: primary | secondary | tertiary  # NEW per §10.4-M28
tool_calls:
  - tool: <name>
    invocations: <integer>
    failures: <integer>
    failure_modes: [<reason1>, <reason2>, ...]
    routed_around_via: [<alternative-tool>, ...]
read_invocations:
  - path: <workspace-relative-path>
    count: <integer>
    cached_after_first: true | false
unavailable_tools:
  - tool: <name>
    workaround: <description>
anomalous_patterns:
  - pattern: <description>
    instances: <count>
substrate_calls:
  - tool: <mcp__selvedge-retrieval__forward_references | resolve_id | search>
    invocations: <integer>
    arguments_summary: <string>
    invoked_at_session_open: true | false
files_read_at_session_open:
  - path: <workspace-relative-path>
    bytes_read: <integer>
    full_or_partial: full | partial
decision_claims_with_evidence_pointers:
  - decision_id: <D-NNN>
    evidence_pointer: <spec-section | ledger-row-id | minority-warrant | archive-pack>
reviewer_invocation_wall_clock_seconds: <integer>
reviewer_invocation_token_count: <integer>
```

Schema scope questions for the phase-2 MAD:

- **Q4a**: Original-EF-059-only vs original + EF-068 Direction 2 extension. Original-only is narrower (failed-tool-call + reviewer-cost surfaces); extended scope adds substrate_calls + files_read_at_session_open + decision_claims_with_evidence_pointers.

- **Q4b**: D2.1 (always-available-always-read) vs D2.2 (available-at-best-effort). D2.1 makes digest-or-no-reviewer hard precondition; D2.2 preserves reviewer operability with degraded coverage.

- **Q4c**: Per-tool granularity vs aggregated counters. Per-tool granularity is reviewer-readable but verbose; aggregated counters are compact but lose tool-specific signal.

### §4.4 Reviewer-prompt-template extension scope

Per (z7) lock-in-after-n=2 discipline (S067 D-246): templates lock-in after n=2 successful applications; subsequent revision requires explicit deliberation surface. Template v2 was lock-in at S067 close (S064 + S067 = 2 successful applications). The phase-3 (γ) implementation requires template extension to incorporate digest input — this is "subsequent revision" per (z7) and triggers explicit deliberation surface (Path PD or Path AS-MAD-execution depending on scope).

The S073 phase-2 MAD at γ phase-3 implementation execution scope is the structural deliberation surface for template v3 adoption. Template v3 extends v2 with: (a) digest-availability check at audit-time; (b) digest-required-section in audit-shape for §3 substantive evidence; (c) reviewer instruction to read digest before §3 evaluation; (d) reviewer instruction to flag digest-vs-narrative inconsistencies as §4 disposition findings.

Lock-in after n=2: template v3 locks-in after n=2 successful applications post-(γ) phase-3 close (forecast: S074+ phase-3 implementation close + first triggered (γ) reviewer post-implementation).

## §5 Direction inventory

### §5.1 Capture mechanism direction-set

- **CMD-1 (CM1 only)**: Claude Code hook-based capture. Engine-v impact: minor harness-config + new tools/digest_emitter.sh + minor `.claude/settings.json` template addition. Cross-workspace portability: per-workspace `.claude/settings.json` setup required at external-application bootstrap per S062 §10.4-M18 records-substrate-pacing-constraint analog.

- **CMD-2 (CM2 only)**: External wrapper-based capture. Engine-v impact: new tools/session_wrapper.sh + protocol spec + cross-harness-tool deployment discipline. Cross-workspace portability: wrapper invocation discipline (operator runs `selvedge-session-wrap claude-code` instead of bare `claude-code`); friction surface non-trivial.

- **CMD-3 (CM3 only)**: Post-hoc transcript-reconstruction capture. Engine-v impact: extension to tools/build_retrieval_index.py + transcript-format spec + reconstruction-script. Cross-workspace portability: tool-script-only; no per-session operator action required (post-session offline reconstruction).

- **CMD-4 (CM1 + CM3 hybrid)**: CM1 preferred for live sessions; CM3 fallback for sessions where CM1 hook setup is unavailable (e.g., legacy workspaces, Claude Code IDE extension contexts). Engine-v impact: CMD-1 + CMD-3 bundled; producer_kind field distinguishes which fired.

- **CMD-5 (CM2 + CM3 hybrid)**: CM2 preferred for cross-harness-tool deployment; CM3 fallback for harness-tool contexts where wrapper invocation is impractical. Engine-v impact: CMD-2 + CMD-3 bundled; producer_kind field distinguishes.

### §5.2 Schema scope direction-set

- **SCD-1 (Original EF-059 only)**: failed-tool-call + repeated-Read pattern + reviewer-cost only. Producer_kind/authority_level still required per §10.4-M28. Smallest scope.

- **SCD-2 (EF-059 + EF-068 Direction 2 substrate_calls only)**: extends with substrate_calls field per orchestrator-side substrate-discipline observability. Cross-linkage with VD-003 gating condition (b) observation window.

- **SCD-3 (Full EF-068 Direction 2 extension)**: extends with substrate_calls + files_read_at_session_open + decision_claims_with_evidence_pointers + reviewer_invocation_* harness-measured. Largest scope; addresses EF-067 Direction B subsumption fully.

- **SCD-4 (SCD-3 + records-substrate phase-2 promotion)**: SCD-3 + digest record promoted to records-substrate per records-contract.md v1 §6 records-family promotion discipline. Per S062 §10.4-M18 P3 z5+z6 lifecycle-required minority + records-substrate phase-2/3 stabilisation pacing constraint: deferred per phase-2/3 maturity gate; not phase-3 scope at γ adoption.

### §5.3 Reviewer-availability scope direction-set

- **RAD-1 (D2.1 always-available-always-read)**: digest is hard precondition for Layer 2 (γ) reviewer invocation. If digest unavailable at trigger-fire, reviewer audit deferred (or explicit honest-limit recording). §Tier 2.5 audit-shape extends frontmatter with required `digest_path:` field.

- **RAD-2 (D2.2 available-at-best-effort)**: digest is reviewer input when available; absent-digest sessions fall back to current Layer 2 audit shape (close artefacts only). §Tier 2.5 audit-shape extends with optional `digest_path:` field; absence triggers lighter-touch audit.

- **RAD-3 (D2.1 with bridged-D2.2 transition window)**: D2.1 is target end-state; D2.2 is deployment-window default during (γ) rollout (e.g., S074-S078 inclusive); D2.1 hard-precondition activates at named gating session (e.g., S079 first-triggered-reviewer-with-digest-required).

### §5.4 EF-067 reviewer self-report disposition direction-set (post-S071 D-264)

- **REVD-1 (Direction B full subsumption now)**: deprecate `duration_minutes` + `reviewer_cost` self-report fields entirely; replace with harness-measured `reviewer_invocation_wall_clock_seconds` + `reviewer_invocation_token_count` per (γ) digest schema; §10.4-M25 P1 audit-cost-budget threshold arithmetic re-activates against harness-measured values.

- **REVD-2 (Direction B partial-deprecation)**: preserve self-report fields with explicit `producer_kind: agent-declared` annotation; harness-measured fields added as parallel; reviewers may compare; cross-session pattern observation continues against harness-measured trajectory; §10.4-M25 P1 threshold arithmetic re-activates against harness-measured per (γ).

- **REVD-3 (Direction B + retrospective re-baseline)**: REVD-1 + retrospective re-baseline against post-(γ) harness-measured value (e.g., S074+ first-triggered-reviewer with digest = new baseline); §10.4-M25 P1 threshold arithmetic re-activates with new baseline (current S063 self-report baseline 25min retired).

### §5.5 EF-068 Direction 1 (e) check 26 substrate-aware branch direction-set

- **CHKD-1 (Implement substrate-aware branch with substrate-required precondition)**: replace inline-comment placeholder with operational `mcp__selvedge-retrieval__search` call; if substrate unavailable, fall back to grep-based n-gram (current implementation); if neither available, check 26 BLOCKED.

- **CHKD-2 (Implement substrate-aware branch with substrate-preferred-but-fallback discipline)**: substrate-aware call preferred when available; grep-based fallback when not; both produce equivalent output format; reviewer reads either.

- **CHKD-3 (Defer to post-γ)**: maintain current grep-fallback-only implementation; defer substrate-aware branch to post-(γ) when CM1/CM2/CM3 capture mechanism deployed (substrate-availability primitive becomes harness-mediated).

### §5.6 Engine-v impact direction-set

- **EVD-1 (Single substantive bump at S074+)**: engine-v13 → engine-v14 at phase-3 implementation close per substantive `validation-approach.md` v7 → v8 + new `tools/validate.sh` checks + minor amendments to bundled specs.

- **EVD-2 (Two-step bump: minor at S073 phase-2 MAD close + substantive at S074+ phase-3 implementation close)**: minor v7 amendment at S073 close codifying digest-spec direction adopted; substantive v7 → v8 at S074+ close per implementation. Per S062+S063 two-session-arc precedent (S062 D-221 + D-228 deliberation; S063 D-228 phase-3 implementation).

- **EVD-3 (Multi-step bump across phase-3 implementation arc)**: minor at S073 + minor at S074 (capture mechanism spec) + substantive at S075+ (full digest spec + audit-shape extension). Most fine-grained; engine-v depth concern per §10.4-M25 P2 cadence-depth.

## §6 Cross-product implementation candidates

Each candidate composes choices from §5 into a deployable bundle. Listed in decreasing scope (mirrors S070 design-space §6 structure but applied to γ-only):

- **(γ-1) Maximal scope**: CMD-4 (CM1+CM3 hybrid) + SCD-3 (full extended schema) + RAD-3 (D2.1 with bridged transition) + REVD-3 (full Direction B + retrospective re-baseline) + CHKD-1 (substrate-aware with required precondition) + EVD-1 (single substantive bump). Engine-v impact: substantive v7 → v8; new check 30 (digest record presence); engine-v14 ratification at S074+ phase-3 implementation close. Cross-spec touching: validation-approach.md v7 → v8 + tools/validate.sh + read-contract.md (v6 → v7 if digest record added to default-read enumeration) + retrieval-contract.md (substrate-availability cross-reference). Resolution time: ~3-4 sessions (S073 MAD + S074 implementation + S075 first-triggered-reviewer-with-digest + S076 VD-003 review). Risk profile: medium-high.

- **(γ-2) Default scope per S071 (ε) hybrid framing**: CMD-1 (CM1 only) + SCD-3 (full extended schema) + RAD-2 (D2.2 available-at-best-effort) + REVD-2 (Direction B partial-deprecation) + CHKD-2 (substrate-aware with fallback discipline) + EVD-2 (two-step bump: minor at S073 + substantive at S074). Engine-v impact: minor amendment at S073 phase-2 MAD close codifying direction; substantive v7 → v8 at S074+ phase-3 implementation close. Cross-spec touching: validation-approach.md v7 → v8 + tools/validate.sh + minor amendment to read-contract.md (digest record in §1 enumeration) + minor amendment to records-contract.md (digest record promotion deferred). Resolution time: ~2-3 sessions (S073 MAD + S074 implementation + S075 first-triggered-reviewer-with-digest). Risk profile: medium.

- **(γ-3) Minimum-viable γ scope per §10.4-M27 P2 deferral-criteria position partly absorbed**: CMD-3 (CM3 post-hoc-reconstructed only; bridge per S071 D-263 framing) + SCD-2 (substrate_calls extension only; defers full extended schema) + RAD-2 (available-at-best-effort) + REVD-2 (Direction B partial-deprecation) + CHKD-3 (defer substrate-aware branch) + EVD-2 (two-step bump with smaller scope at substantive). Engine-v impact: minor at S073 + substantive (smaller) at S074+. Cross-spec touching: validation-approach.md v7 → v8 (smaller) + tools/validate.sh (minor); read-contract.md unchanged. Resolution time: ~2 sessions. Risk profile: low-medium. Honors §10.4-M27 P2 minimum-viable-response framing within (γ) scope.

- **(γ-4) Capture-mechanism-first staged rollout**: phase-3.1 at S074 = CMD-1 (CM1 hook deployment) + minor schema; phase-3.2 at S075+ = SCD-3 + RAD-2 + REVD-2 (full schema + reviewer integration) per CM1 deployment validation. Engine-v: minor at S073 + minor at S074 (CM1) + substantive at S075 (full). Per §10.4-M22 P1 two-session-arc minority preserved-with-honor-by-multi-session-arc framing extended to γ; perspective-independence preservation across phase-3.1 and phase-3.2 deliberation. Resolution time: ~3-4 sessions. Risk profile: medium.

- **(γ-5) Hybrid CMD-4 + staged EVD-3**: CMD-4 (CM1+CM3 hybrid) + SCD-2 → SCD-3 staged across phase-3.1 + phase-3.2 + RAD-3 (transition window) + REVD-2 → REVD-3 staged + CHKD-2. Engine-v: minor at S073 + minor at S074 (CM1+CM3 deployment + SCD-2 schema) + substantive at S075 (SCD-3 expansion + RAD-3 D2.1 activation gating). Most fine-grained; preserves §10.4-M22 P1 multi-step-arc + §10.4-M25 P2 cadence-depth concern simultaneously. Resolution time: ~4 sessions. Risk profile: medium.

Comparison matrix (cost / benefit / risk):

| Candidate | Engine-v bumps | Spec-files touched | Tools touched | Resolution sessions | Producer_kind coverage | Risk profile |
|-----------|----------------|--------------------|--------------|----------------------|---------------------------|--------------|
| (γ-1)     | 1 substantive | validation-approach.md + read-contract.md + retrieval-contract.md (cross-ref) | tools/validate.sh + new harness-integration | 3-4 | harness-measured + post-hoc + agent-declared | medium-high |
| (γ-2)     | 1 minor + 1 substantive | validation-approach.md + minor read-contract.md | tools/validate.sh + new harness-integration | 2-3 | harness-measured + agent-declared | medium |
| (γ-3)     | 1 minor + 1 substantive (smaller) | validation-approach.md (smaller) | tools/validate.sh (minor) | 2 | post-hoc-reconstructed + agent-declared | low-medium |
| (γ-4)     | 1 minor + 1 minor + 1 substantive | validation-approach.md (staged) | tools/validate.sh (staged) + new harness-integration | 3-4 | harness-measured + agent-declared | medium |
| (γ-5)     | 1 minor + 1 minor + 1 substantive | validation-approach.md (staged) + read-contract.md | tools/validate.sh (staged) + new harness-integration | 4 | harness-measured + post-hoc + agent-declared | medium |

Per S062 §10.4-M16 P2 minimum-viable-response precedent: (γ-3) is structurally favored if the phase-2 MAD prefers minimum-viable framing within γ scope. Per S071 D-263 (ε) hybrid framing: (γ-2) is the default scope per the synthesis-articulated direction. Per §10.4-M22 P1 two-session-arc minority + §10.4-M25 P2 cadence-depth concern: (γ-4) and (γ-5) honor multi-step-arc framing. Per §10.4-M26 P1 full-(γ)-immediate dissent preservation: (γ-1) is the maximal-scope direction (P1 reopen warrant (a) sustained substrate non-use post-β would activate per (γ-1) framing).

## §7 Q1-Q10 design questions

- **Q1**: Capture mechanism preferred end-state — CM1 preferred (per S071 D-263 framing) vs CM2 (cross-harness-tool portability) vs CM3 (post-hoc offline reconstruction; bridge) vs CMD-4 hybrid (CM1+CM3) vs CMD-5 hybrid (CM2+CM3)? The choice has portability implications: CM1 binds engine to Claude Code; CM2 cross-harness-tool but adds wrapper-invocation friction; CM3 most-portable but secondary-authority. The phase-2 MAD's cross-family perspective inputs (P3+P4 codex/GPT-5.5 family) are particularly informative for portability evaluation.

- **Q2**: Schema scope — SCD-1 (original EF-059 only) vs SCD-2 (substrate_calls extension) vs SCD-3 (full EF-068 Direction 2 + EF-067 Direction B subsumption) vs SCD-4 (SCD-3 + records-substrate promotion)? SCD-3 subsumes the three-record joint-scope's full surface; SCD-4 anticipates phase-2/3 records-substrate maturity (deferred per S062 §10.4-M18). The phase-2 MAD's Q2 + Q4 evaluation affects Q4a/Q4b/Q4c sub-questions per §4.3.

- **Q3**: Reviewer availability discipline — RAD-1 (D2.1 always-available-always-read; hard precondition) vs RAD-2 (D2.2 available-at-best-effort) vs RAD-3 (D2.1 with bridged-D2.2 transition window)? The choice affects rollout shape: RAD-1 is structurally cleanest but blocks reviewer-audits for digest-unavailable sessions; RAD-2 preserves reviewer operability with degraded coverage; RAD-3 stages the transition.

- **Q4**: Reviewer self-report disposition (EF-067 Direction B execution) — REVD-1 (full subsumption now; deprecate self-report) vs REVD-2 (partial-deprecation; preserve with producer_kind annotation) vs REVD-3 (REVD-1 + retrospective re-baseline)? §10.4-M25 P1 audit-cost-budget threshold arithmetic re-activation depends on baseline choice: REVD-1/REVD-3 use post-(γ) baseline; REVD-2 preserves self-report baseline-comparison surface.

- **Q5**: Check 26 substrate-aware branch direction — CHKD-1 (substrate-required) vs CHKD-2 (substrate-preferred-but-fallback) vs CHKD-3 (defer to post-γ)? The choice depends on whether substrate-availability becomes harness-mediated post-γ (CM1 hook deployment makes substrate calls observable to validate.sh runtime context) or remains validate.sh-runtime-isolated.

- **Q6**: Engine-v cadence — EVD-1 (single substantive bump at S074+) vs EVD-2 (two-step: minor at S073 + substantive at S074+) vs EVD-3 (multi-step across phase-3 sub-phases)? §10.4-M25 P2 cadence-depth concern: depth-0 reset at engine-v13 (S071); depth-1 forecast at S072 close; depth-2 forecast at S073 close (per minor amendment if EVD-2/EVD-3); depth-0 reset at S074 close (per substantive); next reset depends on candidate. Per content-driven-bump precedent chain: cadence concern not violated regardless of candidate.

- **Q7**: Reviewer-prompt-template extension scope (template v3 candidate) — minimum-viable extension (digest-availability check + digest-required-section + reviewer-instruction) vs full extension (digest cross-check disposition findings + digest-vs-narrative inconsistency flagging)? Per (z7) lock-in-after-n=2: template v3 locks-in after n=2 successful applications; the phase-3 design-space surveys minimum-vs-full extension trade-off.

- **Q8**: Bundle-vs-defer for EF-068-read-write-rebalance per S069 D-255 operator-discretionary reopen warrant — should the four-record bundle be opened at S073 phase-2 MAD execution per aggregate-budget pressure surfacing at S071 close? Per S069 D-255: separate-scope at S070++ default; operator-discretionary four-record-bundle reopen preserved. The S072 design-space's Q8 evaluation determines whether to absorb EF-068-read-write-rebalance Direction 3 (default-read surface demote / query-driven read promote) + Direction 4 (forced-write rate reduction) into the γ joint-scope at S073 OR preserve separate-scope per intake-deferral discipline.

- **Q9**: Implementation-locus session-shape — Path L (single-orchestrator) vs Path-AS (design-space + MAD + implementation) for phase-3 implementation at S074+? Per S063 phase-3 precedent: Path L is single-orchestrator implementation per phase-2 MAD output adoption. Per S071 D-263 (ε) hybrid framing: phase-3 is structurally Path-L-class (implementation per direction adopted at phase-2 MAD); the design-space at S072 is the design-space for the phase-2 MAD at S073, which produces direction for the phase-3 implementation at S074+.

- **Q10**: Cross-spec interaction depth — minor amendments (engine-v13 cadence-recovery candidate) vs substantive bump (engine-v14 candidate at γ phase-3 close) vs new spec class (e.g., new `harness-telemetry-contract.md` candidate)? Per `engine-manifest.md` §5: any substantive revision to engine-definition file or any new engine-definition file added bumps engine-v. (γ-1)/(γ-2) bump per substantive validation-approach.md v7 → v8; (γ-3) smaller substantive scope; (γ-4)/(γ-5) staged bumps. New spec class (e.g., separate harness-telemetry-contract.md) is structurally available but would add to engine-definition file count; trade-off vs §10.4-M25 P2 cadence-depth concern.

## §8 Cross-spec interactions

### §8.1 `validation-approach.md` v7 interactions

- §Tier 2.5 audit-shape frontmatter: per §4.4 reviewer-prompt-template extension, RAD-1 adds required `digest_path:` field; RAD-2 adds optional; RAD-3 stages.
- §Tier 2.5 audit-shape required sections: §3 substantive evidence extends with §3d "Digest cross-check" sub-evaluation per RAD-1/RAD-2 adoption.
- §(z6) Harness-Telemetry Digest section: substantive replacement of current "specified-deferred" placeholder with full digest schema specification per (γ-1)/(γ-2)/(γ-3).
- §10 First-Class Minorities: §10.4-M26 reopen warrants tracked at phase-3 implementation close (sustained substrate non-use post-β; reviewer-cost-trajectory laundering recurrence; operational tractability shift). §10.4-M27 reopen warrants tracked similarly. §10.4-M28 substantively adopted via producer_kind/authority_level schema fields. §10.4-M29 substantively adopted via per-direction disposition discipline at phase-3 deliberation.

### §8.2 `prompts/development.md` interactions

- §How to operate paragraph: minor revision candidate per (γ) digest cross-reference (e.g., "the (γ) reviewer at session close incorporates harness-telemetry-digest input per `validation-approach.md` v8 §(z6)" if v8 adopted).
- File-edit claim discipline section: scope unchanged at γ scope.
- Substrate-availability-as-required-precondition clause (per S071 D-264): scope unchanged at γ scope; substrate availability already required-precondition per β-phase.

### §8.3 `tools/validate.sh` interactions

- Check 26 substrate-aware branch (CHKD-1/CHKD-2/CHKD-3 per Q5): scope per direction adopted.
- Check 29 (β-phase WARN-only): potentially upgraded to FAIL post-γ when harness-measured digest replaces agent-declared self-report.
- New check 30 candidate: digest record presence at `provenance/<NNN-session>/harness-telemetry-digest.yaml` per (γ-1)/(γ-2)/(γ-4) adoption; check 30 verifies presence + producer_kind/authority_level field well-formedness + schema-compliance per chosen schema spec.
- Check 27 sub-clause for reviewer-prompt-template v3 (post-(z7) extension): verifies template version recorded in audit frontmatter `reviewer_prompt_template_version: 3` post-γ adoption.

### §8.4 `read-contract.md` v6 interactions

- §1 default-read enumeration: potentially v6 → v7 candidate per (γ-1)/(γ-5) adoption — adds `provenance/<NNN-session>/harness-telemetry-digest.yaml` as required per-session-provenance file (engine-definition spec change → engine-v bump bundled with γ substantive). Per §8 alternative: digest record stays at session-scope per applications-directory carve-out analog (read-as-needed by reviewer; not default-read at session-open of subsequent sessions).
- §2 per-file budget: digest record forecast small (~500-1,500 words per session); under per-file budget; not aggregate-impact concern.
- §2c close-rotation: digest record rotates with session per close-rotation; same retention-window discipline as 03-close.md.

### §8.5 `retrieval-contract.md` v1 interactions

- §1 substrate primitives: scope unchanged per (γ); substrate-availability already required-precondition per β-phase.
- §2 portability: capture-mechanism choice per Q1 affects portability per §4.2; CM1 binds Claude Code; CM2 cross-harness-tool; CM3 most-portable.

### §8.6 `records-contract.md` v1 interactions

- Records-substrate phase-2/3 stabilisation pacing: per S062 §10.4-M18 P3 z5+z6 lifecycle-required minority — digest record promotion to records-substrate (records/harness-telemetry-digest/) deferred per phase-2/3 maturity gate. Not γ-phase-3 scope; future arc.

### §8.7 `methodology-kernel.md` v6 interactions

- §7 Validate scope: harness-side-supplemented per γ adoption; not redefined. The three senses (Workspace, Domain, Reference) are framing-stable; γ adds harness-measured-evidence-channel within Workspace sense.

### §8.8 `multi-agent-deliberation.md` v4 interactions

- §Stance Briefs: scope unchanged per γ; brief-extension content for S073 phase-2 MAD per §9 below.
- §Graceful Degradation: cross-referenced from RAD-1/RAD-3 hard-precondition discipline (digest unavailable → reviewer audit deferred per §Graceful Degradation honest-limit recording).

### §8.9 `workspace-structure.md` v9 interactions

- §10.4-M26 through §10.4-M29 status updates per phase-3 implementation outcome (additions only at phase-3 close per direction adopted; preservation against future-arc rollback maintained).
- New first-class minorities possible per S073 phase-2 MAD synthesis (e.g., P1 + P2 + P3 + P4 perspectives may surface §10.4-M30+ candidates per direction-not-adopted preservation discipline).

### §8.10 `engine-manifest.md` interactions

- §2 current engine version: engine-v13 → engine-v14 candidate at γ phase-3 implementation close per substantive bump.
- §7 engine version history: new engine-v14 entry at S074+ ratification close per phase-3 adoption.

## §9 Pre-ratification of S073 phase-2 MAD shape

Per S057 D-196 + S061 D-219 + S068 D-251 + S070 D-260 phase-1-pre-ratifies-phase-2 precedent extended to phase-3-arc design-space scope: phase-1 design-space pre-ratifies phase-2 MAD shape. The pre-ratification is conditional on no operator amendment at S073 open.

**Phase-2 MAD lineup (4-perspective two-family per S058 + S062 + S064 + S071 precedent)**:

- **P1 — Capture-Mechanism-Maximalist Architect (Claude family)**. Stance brief slot: Q1 capture-mechanism preferred end-state (defends CMD-4 CM1+CM3 hybrid for cross-context primary-authority coverage); Q2 schema scope (defends SCD-3 full extended schema); Q3 reviewer-availability discipline (defends RAD-1 D2.1 always-available-always-read for structural cleanliness); Q4 reviewer self-report (defends REVD-3 full subsumption + retrospective re-baseline); Q6 engine-v cadence (defends EVD-1 single substantive bump). Brief-extension cites this design-space §3-§7. Position aligns with §10.4-M26 P1 full-(γ)-immediate preservation.

- **P2 — Minimum-Viable Conservator (Claude family)**. Stance brief slot: defends (γ-3) minimum-viable γ scope per §10.4-M27 P2 deferral-criteria position partly absorbed framing; Q1 (defends CMD-3 post-hoc-reconstructed bridge); Q2 (defends SCD-2 substrate_calls extension only); Q3 (defends RAD-2 available-at-best-effort); Q4 (defends REVD-2 partial-deprecation); Q5 (defends CHKD-3 defer substrate-aware branch); Q6 (defends EVD-2 two-step bump with smaller substantive scope). Position preserves portability + harness-config simplicity + records-substrate phase-2/3 pacing constraint per S062 §10.4-M18 + S071 §10.4-M27 reopen warrant (d).

- **P3 — Outsider Frame-Completion (codex/GPT-5.5 family)**. Stance brief slot: Q1 capture-mechanism portability evaluation from outside Claude-family framing (CM2 cross-harness-tool surface + CM3 post-hoc-reconstruction surface); Q5 check 26 substrate-aware branch from outside-Claude-Code-runtime-context; Q8 bundle-vs-defer EF-068-read-write-rebalance evaluation as scope-question independent of intake-deferral discipline; frame-completion check on whether design-space §5-§6 candidate inventory covers choice surface adequately. May surface reframes (z-prefix per S058 + S062 + S064 + S071 precedent) not in this design-space's §5-§6 inventory (e.g., (z) capture-mechanism-as-substrate-extension; (z) digest-as-records-substrate-row-from-day-1; (z) reviewer-prompt-template-versioning-as-engine-feedback-arc).

- **P4 — Cross-Family Reviewer Laundering-Audit (codex/GPT-5.5 family)**. Stance brief slot: laundering-audit per S058 + S062 + S064 + S071 P4 precedent; specifically audits whether (γ-1)/(γ-2)/(γ-3)/(γ-4)/(γ-5) candidate selection at S073 MAD is operationally consistent with §10.4-M29 P4 bundling-by-laundering audit framing (separate dispositions per direction, not bundled inevitability); cross-family reviewer family rule per `validation-approach.md` v7 §Tier 2.5 satisfied (Claude family at orchestrator + P1/P2; codex family at P3/P4). Counter-frame check on (γ-1) maximal-scope vs (γ-3) minimum-viable-scope bundling pressure; verify producer_kind/authority_level schema field semantics per §10.4-M28 substantive adoption.

**Decision-procedure pre-ratification**: 4-perspective two-family weighted convergence per S058 + S062 + S064 + S071 precedent. Cross-family weighted-convergence threshold: 3-of-4 across families adoption signal triggers same-session-bounded direction-adoption per S071 D-263 (ε) hybrid same-session-bounded β-phase precedent OR phase-3 adoption deferred to S074+ per S062 D-220 multi-session phase-3 precedent depending on direction adopted; below threshold preserves design-space + names follow-on phase-2 MAD or phase-3 shape.

**Brief-extension content per perspective**: this design-space §3 (workspace state) + §4 (γ scope's structural surface) + §5 (direction inventory) + §6 (cross-product implementation candidates) + §7 (Q1-Q10 design questions) + §8 (cross-spec interactions). Per-perspective stance briefs assigned per perspective above.

**Reviewer prompt template version at S073 phase-2 MAD close**: v2 per S067 D-246 (z7) lock-in-after-n=2 (S064 + S067 = 2 successful applications; S071 fourth application sustained lock-in). Template v3 candidate scope per (γ) phase-3 adoption; adoption shape per direction selected at S073 phase-2 MAD synthesis; lock-in-after-n=2 discipline preserved (template v3 locks-in after n=2 successful applications post-γ phase-3 close per established (z7) framing).

**Cross-family reviewer family rule satisfaction check** (per `validation-approach.md` v7 §Tier 2.5 reviewer-family rule): orchestrator at S073 = Claude family (assumed per workspace convention; operator may amend); P3+P4 = codex family; family non-overlap satisfied. Substrate-led discipline per §10.4-M23: P3 codex independently surfaces frames not pre-encoded by orchestrator; reviewer-judged frame status preserved.

**Reviewer at S073 close**: required per Layer 2 trigger forecast (b) substantive-arc-class fires at phase-2 MAD execution scope. Reviewer family non-overlap with orchestrator + P3/P4 codex perspectives: prefer Google Gemini per §5.6 GPT-family-concentration window-ii consideration (cumulative count at S072 close = eight-consecutive; S073 advance to nine-consecutive at phase-2 MAD execution; Gemini interrupts streak per S063 + S067 + S071 reviewer family precedent); codex acceptable fallback with reviewer overlap disclosure per `validation-approach.md` v7 §Tier 2.5 reviewer-family rule revision.

**§5.6 GPT-family-concentration window-ii**: would advance at S073 phase-2 MAD execution per cross-family reviewer participation. Cumulative count would advance to nine-consecutive (S072 preserves at eight-consecutive per phase-1-design-space scope; S073 advances to nine per phase-2 MAD execution); window-ii observation continues per §5.6 minority preservation.

## §10 Open observations + cross-linkages + honest limits

### §10.1 Cross-linkages with preserved minorities

- **§10.4-M16 P2 minimum-viable-response precedent** (S062) — informs (γ-3) minimum-viable γ scope candidate selection per §6. Phase-2 MAD's Q2 + Q6 evaluation references this precedent.

- **§10.4-M22 P1 two-session-arc minority** (S064) — honored by multi-session phase-3 arc shape (S072 design-space + S073 MAD + S074+ implementation = three-session arc; structurally exceeds two-session-arc minimum). Reopen warrants (a) spec-text drift + (b) synthesizer-framing absorption + (c) phase-3 implementation flaw tracked at S074+ phase-3 implementation close.

- **§10.4-M23 P3 substrate-led reviewer-judged frame** (S064; substantively adopted at v7 audit-shape direction) — preserved at S064 + applied at S067 + S071 (Gemini reviewers; Layer 2 trigger fires). Phase-2 MAD's P3 + P4 cross-family substrate-led frame preserved at S073+; reviewer audit at S073 close incorporates substrate-led discipline.

- **§10.4-M25 P1 audit-cost-budget reopen-warrant** (S064; S071 D-264 amendment suspending threshold arithmetic on self-reported values pending harness-measurement availability) — disposition follows Q4 choice (REVD-1/REVD-3 re-activates threshold arithmetic against harness-measured baseline; REVD-2 preserves with parallel evidence channel).

- **§10.4-M25 P2 cadence-depth concern** (S064) — engine-v13 ratified at S071 (depth-0 reset); depth-1 forecast at S072 close. Engine-v14 candidate at S074+ phase-3 implementation close per (γ) substantive bump; preservation depth resets to 0 at engine-v14 ratification. §10.4-M25 P2 reopen warrant (a) "engine-v13 at S065 fully activates §5.4" status: NOT FIRED at S071 D-265 (engine-v13 ratified at S071 not S065; depth-6 path at engine-v12); not violated.

- **§10.4-M26 P1 full-(γ)-immediate position** (S071) — preserved at S071 + tracked at S072+ observation window. Reopen warrants per §10.4-M26: (a) sustained substrate non-use post-β; (b) reviewer-cost-trajectory laundering recurrence; (c) operational tractability shift. **Status at S072**: substrate-exercise sustained at S072 (n=2); (a) NOT FIRED yet (n=2 insufficient evidence); (b) NOT FIRED at S072 design-space scope (no reviewer at S072 close); (c) NOT FIRED at design-space-production scope. Tracking continues across S073-S076 retention window.

- **§10.4-M27 P2 (γ)-deferral-criteria position** (S071; partly absorbed) — informs (γ-3) minimum-viable γ scope candidate selection. Reopen warrants per §10.4-M27: (a) operator-audit cadence drops below 80% across 10-session window post-(γ); (b) (γ) capture mechanism portability friction blocks external-application engine load; (c) (z6) digest produces n≥3 sessions of measured behavior that diverges from spec-side expectation; (d) records-substrate phase-2/3 stalled because (γ) absorbed substantive-arc capacity. (b) is the load-bearing portability-friction surface for Q1 capture-mechanism evaluation.

- **§10.4-M28 P3 measurement-authority-separation position** (S071; substantively adopted) — load-bearing for §4.1 schema design + producer_kind/authority_level field semantics. Preserved against future-arc rollback: phase-3 implementation MUST include producer_kind/authority_level fields per §10.4-M28; reopen warrants (a) phase-3 (γ) digest spec adopted without producer_kind/authority_level fields + (b) CM4 entries treated as harness-measured-equivalent + (c) future MAD on related arc surfaces measurement-authority concern independently.

- **§10.4-M29 P4 bundling-by-laundering audit position** (S071; substantively adopted) — informs §6 cross-product candidate evaluation: separate per-direction disposition prevents (γ-1) maximal-scope from being adopted as bundled-inevitability framing without explicit per-direction cost analysis. Phase-2 MAD's P4 stance preserves this audit framing.

- **§10.4-M10 written-warrant clause (c) operator-surfacing channel** (S050+) — cumulative count advanced n=9 → n=10 at S072 open (Path-AS direction-setting surface). Pattern continues.

- **§10.4-M14 P1 broader-phase-1 minority** (S058) — reopen warrant fired empirically per EF-068-read-write-rebalance Evidence (§10.4 minority block crosses 1,500 words; currently ~1,800). Cross-reference preserved for S073+ phase-2 MAD design-space input; bundle-vs-defer Q8 evaluation references this minority.

### §10.2 Open observations

1. **The phase-3 design-space at S072 is structurally narrower than phase-1 design-spaces at S057/S061/S070**. Prior phase-1 design-spaces surveyed full substantive-arc scope ahead of phase-2 MAD adoption; the S072 phase-3 design-space surveys only the (γ) implementation-arc residual choice surface within the (ε) hybrid composition pre-decided at S071 phase-2 MAD. The narrowness is engine-conventional per multi-session phase-3 arc shape; the design-space's shape reflects the downstream-of-pre-decided-direction position.

2. **Substrate-exercise pattern at S072 (n=2) is single observation point**. The Hawthorne-effect-vs-durable-behavior-change distinction per §10.4-M26 reopen warrant (a) is testable empirically only at sustained pattern observation across S073-S076 retention window. The S072 design-space cannot adjudicate; the (γ) phase-3 implementation timing depends on whether β-phase succeeds in achieving sustained substrate-use without harness-side enforcement OR whether γ harness-side measurement-or-enforcement is structurally required.

3. **Capture-mechanism portability question is the load-bearing cross-family inquiry**. Claude-family perspectives (P1+P2) may default to CM1 (Claude Code hooks) per native-context familiarity; codex/GPT-5.5 perspectives (P3+P4) may surface CM2 + CM3 as substantive alternatives per cross-context portability concern. The phase-2 MAD's Q1 evaluation depends on this cross-family input; design-space surveys all three but does not pre-decide.

4. **Reviewer self-report disposition (Q4) is operationally orthogonal to capture mechanism (Q1)**. REVD-1/REVD-2/REVD-3 choices are per-(γ)-implementation-direction independent of CMD-1/CMD-2/CMD-3 choice. The phase-2 MAD may decompose these as independent dispositions per §10.4-M29 P4 bundling-by-laundering audit framing.

5. **Records-substrate phase-2/3 promotion deferred per §10.4-M18 + §10.4-M27 (d)**. Digest record promotion to records/harness-telemetry-digest/ is structurally available per records-contract.md v1 §6 records-family promotion discipline but deferred per records-substrate phase-2/3 maturity gate. Promotion is post-γ-phase-3-close future arc; not γ-phase-3 scope.

6. **The recursive tension at S070 (design-space-for-harness-side-enforcement-executed-under-existing-read-discipline-gap) is partially resolved at S071+S072 (orchestrator substrate-exercise non-zero at session-open)**. The recursive tension is not dissolved (β-phase is spec-side codification; γ-phase is the harness-side test of whether spec-side suffices); the resolution shape is empirically testable across S073-S076 observation window per VD-003 gating condition (b).

7. **Aggregate-budget pressure at S071 close (90,309 / 90K soft)** is engaged at S072 close per close-rotation S066 OUT (mechanical aggregate-reducing action). The structural restructure scope (EF-068-read-write-rebalance four-record-bundle reopen warrant per S069 D-255) remains preserved as standing operator-discretionary surface; activation at S073+ phase-2 MAD scope is structurally available per Q8 bundle-vs-defer evaluation.

8. **The §10.4-M22 P1 two-session-arc minority is structurally honored by multi-session phase-3 arc shape**. S072 design-space + S073 MAD + S074+ implementation = three-session arc; perspective-independence preservation across phase-3.1 design-space + phase-3.2 deliberation + phase-3.3 implementation is structurally available per (γ-4)/(γ-5) staged-rollout direction OR collapsed at (γ-1)/(γ-2)/(γ-3) single-substantive-bump direction. The phase-2 MAD's Q6 evaluation determines arc-shape extension.

### §10.3 Honest limits at design-space production

1. **Single-orchestrator phase-3 design-space session scope**. This document is produced by single-orchestrator at S072. The design-space's perspective-coverage is bounded by the orchestrator's framing; phase-2 MAD's 4-perspective two-family deliberation at S073 is the structural mechanism for perspective-diversity. Q1-Q10 (§7) and direction-inventory (§5-§6) reflect orchestrator framing; perspectives at S073 may surface choice-axes not pre-encoded.

2. **Substrate exercise at S072 session-open (n=2 in β-phase post-S071 D-264 window) does not yet adjudicate Hawthorne-effect-vs-durable-behavior distinction** per VD-003 gating condition (b). The pattern reified at n=2 is a single observation point; n=4-5 across S073-S076 retention window will provide first triangulation.

3. **Capture-mechanism technical feasibility evaluation is bounded by orchestrator's familiarity**. Claude Code hook surface (CM1) is concretely understood per native-context experience (PreToolUse + PostToolUse hooks per `update-config` skill scope); CM2 external wrapper feasibility is partly understood (stdio multiplex + process-tree introspection are concretely feasible but workspace-portability friction is non-trivial); CM3 transcript-reconstruction feasibility depends on Claude Code transcript format stability (stable across recent versions per workspace operator-experience but not externally-validated). The S073 phase-2 MAD's P3+P4 cross-family perspectives provide independent feasibility evaluation.

4. **(z6) digest schema in §4.3 is candidate-only**. Phase-2 MAD deliberates schema as part of (γ) adoption; the §4.3 schema is starting-point for deliberation, not pre-decided spec text.

5. **Cross-product implementation candidates (γ-1) through (γ-5) in §6 are not exhaustive**. P3 frame-completion at S073+ may surface candidate (γ-6)+ not pre-encoded per §10.2 observation 3 examples + §10.1 §10.4-M27 P2 reopen warrant (a) operator-audit-cadence framing alternatives.

6. **Q1-Q10 design questions are framing-ordered, not priority-ordered**. The phase-2 MAD's 4-perspective deliberation may re-order priority per perspective; the orchestrator at phase-1 does not pre-rank.

7. **§3.2 reviewer self-report propagation chain is referenced via S070 design-space §3.2 + EF-067 intake content**. Not freshly verified at S072 design-space production. Forward-direction: phase-2 MAD's P4 cross-family reviewer audits the chain's fidelity as part of laundering-audit stance brief continuation per S071 P4 precedent.

8. **Phase-3 design-space does NOT trigger Layer 2 (γ) reviewer at close** per S057 + S061 + S070 phase-1 close precedent applied to phase-3-arc design-space scope (no Layer 2 trigger fired at phase-1 closes; pattern reified at n=4 with S072). The first reviewer audit on this phase-3-arc fires at S073 phase-2 MAD close per Layer 2 trigger (b) substantive-arc-class.

9. **The phase-2 MAD pre-ratification at §9 is conditional on no operator amendment at S073 open**. Per workspace convention, pre-ratifications by close decision are sufficient warrant for next-session execution unless operator surfaces amendment or exclusion at session-open per §10.4-M10 written-warrant clause (c).

10. **Aggregate impact**: this design-space.md is approximately 5,600 words at production; NOT counted in default-read aggregate per `read-contract.md` v6 §1 (provenance is session-scope read-as-needed, not default-read). The session's net default-read aggregate impact is dominated by close-rotation (S066 4,901 OUT + S072 close ~3,500-4,500 IN) + records/sessions/index.md row +~250-500 + engine-feedback/INDEX.md no extensions. Net forecast: aggregate 90,309 → 89,500-91,000 / 90K soft (range -800 to +700 from soft warning).

## §11 Notes for the S073 phase-2 MAD

- **Perspective P1 (Capture-Mechanism-Maximalist Architect, Claude)**: stance brief should defend (γ-1) maximal-scope direction or (γ-2) (ε)-hybrid-default-scope direction per §10.4-M26 P1 full-(γ)-immediate preservation. Address Q1 (CMD-4 CM1+CM3 hybrid for cross-context primary-authority coverage); Q2 (SCD-3 full extended schema); Q3 (RAD-1 D2.1 always-available-always-read); Q4 (REVD-3 full subsumption + retrospective re-baseline); Q5 (CHKD-1 substrate-aware with required precondition); Q6 (EVD-1 single substantive bump); Q7 (full reviewer-prompt-template extension); Q8 (defer EF-068-read-write-rebalance per S069 D-255 separate-scope to prevent γ scope expansion); Q9 (Path L phase-3 implementation per direction adopted); Q10 (substantive engine-v14 bump). Honest-limit slot: cost of full-shift vs portability friction + records-substrate phase-2/3 pacing constraint per §10.4-M27 reopen warrant (d).

- **Perspective P2 (Minimum-Viable Conservator, Claude)**: stance brief should defend (γ-3) minimum-viable γ scope per §10.4-M27 P2 deferral-criteria position partly absorbed framing. Address Q1 (CMD-3 post-hoc-reconstructed bridge); Q2 (SCD-2 substrate_calls extension only); Q3 (RAD-2 available-at-best-effort); Q4 (REVD-2 partial-deprecation); Q5 (CHKD-3 defer substrate-aware branch); Q6 (EVD-2 two-step bump with smaller substantive scope); Q7 (minimum-viable reviewer-prompt-template extension); Q8 (defer EF-068-read-write-rebalance per S069 D-255 separate-scope); Q9 (Path L phase-3 implementation); Q10 (substantive but smaller engine-v14 bump). Honest-limit slot: minimum-viable's resolution-chain timing + portability friction trade-off.

- **Perspective P3 (Outsider Frame-Completion, codex)**: stance brief should evaluate whether design-space §3-§7 covers choice surface adequately; surface reframes not pre-encoded per §10.2 observation 3 examples; address Q1 (capture-mechanism portability evaluation from outside Claude-family framing — may surface CM2 + CM3 as substantively distinct surfaces from CM1 vs (a) Claude-family-default familiarity bias laundering CM1 as preferred); address Q5 (check 26 substrate-aware branch from outside-Claude-Code-runtime-context); address Q8 (bundle-vs-defer evaluation as scope-question independent of intake-deferral discipline). Honest-limit slot: areas where design-space framing may have laundered choice surface or treated CM1 as preferred without independent justification.

- **Perspective P4 (Cross-Family Reviewer Laundering-Audit, codex)**: stance brief should audit whether (γ-1)/(γ-2)/(γ-3)/(γ-4)/(γ-5) candidate selection at S073 MAD is operationally consistent with §10.4-M29 P4 bundling-by-laundering audit framing (separate dispositions per direction, not bundled inevitability); cross-family reviewer family rule satisfied at S073 MAD execution; counter-frame check on (γ-1) maximal-scope vs (γ-3) minimum-viable-scope bundling pressure; verify producer_kind/authority_level schema field semantics per §10.4-M28 substantive adoption. Honest-limit slot: laundering-audit findings or counter-frame surfaces requiring preservation as first-class minority at phase-2 MAD synthesis (e.g., new §10.4-M30+ candidates).

**MAD output expectations**: per S058 + S062 + S064 + S071 precedent — `01-deliberation.md` (synthesis with cross-family weighted convergence per §9 decision-procedure) + `01a/01b/01c/01d-perspective-*.md` (raw perspectives) + `02-decisions.md` (substantive decisions + minority preservation per first-class-minority discipline) + `03-close.md` + (γ) reviewer audit at close per Layer 2 trigger (b) substantive-arc-class.

**Operator-audit cadence at S073 close** per Layer 6.2 standing operator-audit cadence: triggered (S073 phase-2 MAD substantive-arc-class resolution AND likely engine-version increment per phase-3 implementation forecast at S074+ within close horizon).

**Phase-3 implementation timing forecast post-S073 phase-2 MAD synthesis**: per direction adopted — (γ-1)/(γ-2): S074 phase-3 implementation per S058 D-199 same-session-bounded-after-MAD precedent OR S074+ multi-session per S062 D-220 precedent depending on direction adopted; (γ-3): S074 minimum-viable phase-3 implementation; (γ-4)/(γ-5): S074 phase-3.1 + S075 phase-3.2 + S076 phase-3.3 (full multi-step rollout per staged-rollout discipline).
