---
feedback_id: EF-059-harness-telemetry-feed-for-tier-2-reviewer
source_workspace_id: selvedge-self-development
source_session: 062
created_at: 2026-04-25T22:50:00Z
reported_by: application-agent
target: methodology
target_files:
  - specifications/validation-approach.md
  - specifications/read-contract.md
  - prompts/development.md
  - tools/validate.sh
severity: friction
status: inbox
---

# EF-059 — Harness telemetry feed for Tier-2 reviewer (z6 implementation arc; deferred per S062 D-225)

## Observation

The S062 MAD on EF-058-tier-2-validation adopted a layered structural mechanism (D-221) including a triggered cross-family reviewer (Layer 2) operating against close artefacts. Two of the three intake observable patterns named in EF-058-tier-2-validation §Observation cannot be detected from workspace artefacts alone:

1. **Failed tool calls** — when a tool unexpectedly fails or returns garbage, the agent often retries the same call or routes around the failure via Bash, without escalating "this tool that should work doesn't" as a session-level concern. Observable in agent transcript (visible to harness layer) but not in workspace artefacts.

2. **Repeated Read calls** — reading the same file multiple times in a session because earlier reads weren't preserved or weren't trusted; observable in transcript but not auditable post-hoc.

The third intake pattern (honest-limit text drift) IS coverable by Layer 1 mechanical detection (validate.sh check 26 substrate-aware honest-limit text repetition) + Layer 2 cross-family reviewer reading close artefacts. Patterns 1+2 are not coverable without harness-telemetry-feed.

The S062 MAD per `01-deliberation.md` §1.5 + §2.1 Layer 5 deferred raw-transcript review and adopted P3's reframe (per `01c-perspective-outsider-frame-completion.md` Q5 + frame critique): **harness telemetry should first be implemented as a structured digest before raw-transcript review**. The digest format includes: failed tool calls, retries, repeated reads by path, fallback route-around events, anomalous command patterns, unavailable-tool annotations.

Per S062 D-225 + Layer 5 specification: this intake records the deferred-implementation surface with named activation preconditions for follow-on MAD scheduling.

## Why It Matters

1. **Layer 2 (γ) cross-family reviewer's audit packet is structurally incomplete without harness-telemetry digest.** Per §2.1 Layer 5 specification at S063 phase-3 adoption, the (γ) reviewer's audit packet MUST name the digest section as required input when telemetry is available. Without telemetry availability, the (γ) reviewer audits close artefacts only — covering 3 of 4 intake failure surfaces (honest-limit drift + ceremony-vs-progress + shared-frame-blindness) but leaving 1 of 4 (failed-tool/repeated-Read patterns) structurally undetected.

2. **Engine scope expansion is non-trivial; deferral is principled.** Per P2 [`01b-perspective-incrementalist-conservator.md`, Q5]: "the harness layer is outside the engine's current specification scope — the engine governs workspace artefacts; the harness governs invocation. Bringing harness-telemetry into engine scope is a scope-expansion that the records-substrate adoption at S058 already represents one major scope-expansion in the same arc. The engine should not adopt two scope-expansions in immediate succession."

3. **P4 [`01d-perspective-cross-family-reviewer.md`, counter-frames] preservation requirement**: "The synthesis is likely to fold P3's z5 into z2 and lose the broader category: validation debt includes honest limits, tool defects, route-arounds, and standing-instruction mismatches." Tool defects + route-arounds are the harness-telemetry surface; preserving the broader category requires this implementation arc.

4. **Records-substrate phase-2/3 stabilisation is the natural pacing constraint.** Records-substrate phase-1 is operational at S061 (60+1=61 records at S062 close); phase-2 mirrored-minorities + phase-3 feedback-records-family adoption are pending; phase-2 firing-disposition adjudicated default-(a) at S061. Adding harness-telemetry as a third major scope-expansion before phase-2/3 records-substrate maturity is operationally heavy.

## Suggested Change

**Substantive-arc deliberation; deferred per activation preconditions per S062 D-225 + Layer 5 specification per `provenance/062-session/01-deliberation.md` §2.1 Layer 5.**

Activation preconditions (all three required) for follow-on MAD scheduling:
- (a) **Reviewer mechanism (Layer 2 (γ)) adopted at S063** per S062 D-221 phase-3 adoption.
- (b) **Reviewer operating across ≥3 sessions** per WX-62-1 observation window completion (3 successful triggered applications recorded).
- (c) **≥1 instance documented where harness-telemetry digest (z6) would have caught failed-tool-call or repeated-Read pattern** given digest access.

When activation preconditions fire, recommended arc shape per S057+S058 Path AS-class precedent:
- **Phase 1 — synthesis / design-space session** (Path AS Shape-1). Surveys digest schema design (what fields; what threshold; what scope) + harness-integration mechanism (how the digest is captured + delivered to reviewer) + cost/benefit matrix vs raw-transcript-review. Produces `provenance/<NNN>-session/design-space.md`. Pre-ratifies phase-2 MAD shape.
- **Phase 2 — 4-perspective two-family MAD** on substantive direction. Cross-family essential because the digest schema design is itself a discipline-design surface that benefits from Tier-2-reviewer-mechanism that Layer 2 (γ) embodies (i.e., the question "what should the digest contain" is answered better with cross-family deliberation than single-orchestrator design).
- **Phase 3 — adoption** per direction adopted. Substantive revision to `validation-approach.md` v6 (or v7 depending on intervening sessions); possibly `read-contract.md` v6 → v7 (telemetry source / harness-layer-engine-boundary clarification); possibly new spec section codifying digest schema; possibly new tools/ implementation for digest capture-and-delivery.

Possible candidate digest schema (for the synthesis to deliberate; not pre-committed):

```yaml
# provenance/<NNN>-session/harness-telemetry-digest.yaml
session: <NNN>
captured_at: <ISO-8601>
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
```

The digest is captured during session execution (mechanism: harness-layer integration — possibly Claude Code hook surface; possibly external telemetry capture wrapper; possibly substrate-augmented post-session analysis). The capture mechanism itself is a deliberation surface.

**Possible engine-v impact of phase-3 adoption**: minor if pure validate.sh + reviewer-prompt-template extension; substantive if read-contract.md revision + new spec section + harness-layer-engine-boundary articulation → engine-v12 candidate.

## Evidence

- **EF-058-tier-2-validation §Observation patterns 1+2** (filed S058-post-session; triaged S059 D-209; resolved S062 D-223): explicit naming of failed-tool-calls + repeated-Reads as patterns Tier 2 cannot detect from workspace artefacts.
- **S062 design-space.md §3.3** (`provenance/061-session/design-space.md`): "These patterns are individually small but compound into 'unwillingness to commit to better operational hygiene and performance' (operator framing) over multi-session windows. ... Mechanical detection requires harness-telemetry-feed."
- **S062 design-space.md §6 matrix row "Catches-failed-tool-calls / Catches-repeated-Reads"**: all five (α)-(ε) candidates marked "no" for failed-tool-calls; (α) "no" + (β-ε) "partial (if transcript provided)" for repeated-Reads. Harness-telemetry is dependency for full coverage.
- **`provenance/062-session/01a-perspective-validator-architect.md` Q5 + Honest limits 5**: "(α)+(γ) without harness-telemetry leaves intake patterns 1+2 uncovered."
- **`provenance/062-session/01b-perspective-incrementalist-conservator.md` Q5**: "Defer. Out-of-scope at S062. ... The engine should not adopt two scope-expansions in immediate succession."
- **`provenance/062-session/01c-perspective-outsider-frame-completion.md` Q5 + Frame critique (z6)**: "I recommend (z6): a harness telemetry digest first."
- **`provenance/062-session/01d-perspective-cross-family-reviewer.md` Q5 + counter-frames**: "Coverage: z6 should be preserved because it changes the implementation target."
- **`provenance/062-session/01-deliberation.md` §1.5 + §2.1 Layer 5**: synthesis adoption of (z6) as specified-now-implemented-later per 4-of-4 convergence on raw-transcript-review-not-S062-ready.
- **`provenance/062-session/02-decisions.md` D-221 Layer 5 + D-225 EF-059 filing**: load-bearing decisions for this intake.

## Application-Scope Disposition

Self-dev-originated. Application-agent (Case Steward) filed per S062 D-225 + Layer 5 specification (not operator-surfaced; this is a structural deferral with named activation preconditions, not a post-session operator observation).

`source_workspace_id: selvedge-self-development`. `reported_by: application-agent` (distinct from operator-surfaced records EF-054 / EF-055 / EF-058×3).

Severity `friction` — specified deferral with named preconditions; not pure observation (the problem is structurally named); not blocker (engine continues to function via Layer 1+2 partial coverage); not operator-surfaced-friction (Case-Steward-surfaced per Layer 5 spec).

Triage scheduled: deferred until activation preconditions evaluable (estimated ≥S066 after WX-62-1 observation window completes).

When triage activates, classification likely substantive-arc per S047/S049/S050/S057/S058 substantive-arc precedent chain (digest schema + harness-integration mechanism + cost-benefit deliberation requires multi-perspective MAD).

The recursive concern (a Tier-2-reviewer-mechanism EF triggers another EF for harness-telemetry-feed which is itself addressing a Tier-2-reviewer-mechanism gap) is acknowledged: this is the specified deferral discipline at work, not laundering. The activation preconditions ensure the deferral is structural-and-bounded, not indefinite.

The S062 close §2 recommends operator audit at S062 close per intake §Application-Scope-Disposition closing paragraph; this EF-059 filing is one substantive-arc-relevant data point for the operator audit (was the deferral principled? are the activation preconditions appropriate?).
