---
feedback_id: EF-058-tier-2-validation-discipline-by-distinct-agent
source_workspace_id: selvedge-self-development
source_session: 058
created_at: 2026-04-25T18:30:00Z
reported_by: operator
target: methodology
target_files:
  - specifications/validation-approach.md
  - specifications/methodology-kernel.md
  - specifications/multi-agent-deliberation.md
  - prompts/development.md
  - tools/validate.sh
severity: friction
status: inbox
---

# EF-058 — Tier 2 validation discipline should not be performed by the lead agent (substantive-arc; routed to MAD per operator preference)

## Observation

The session-close Tier 2 validation per `specifications/validation-approach.md` v5 §Tier 2 (questions Q1–Q9) is currently answered by the same agent that performed the session's Read + Assess + Convene + Deliberate + Decide + Produce + Record + close-narrative-write activities. That agent has structural incentive to judge its own work as "meaningful progress" rather than as "ceremony without advancing" (Q4). The validation step does not catch what it is supposed to catch.

Concrete pattern across S051–S058: eight consecutive `03-close.md` files carry the `§8 honest-limit` text "MCP stdio transport remains unverified per S051-S0NN chain" in some form. At each session close, the orchestrator agent answered Tier 2 Q4 implicitly-affirmatively (the close was committed; nobody flagged ceremony). The honest-limit text drifted from honest-limit to **laundered operational debt** somewhere between S052 and S054 — by S055 it was clearly recording-not-engaging, and by S058 it had become engine-conventional ceremony. The S058 close itself, written 60 minutes ago, propagated the same pattern: §8 honest-limit 3 records "MCP stdio transport remains unverified per S051-S057 chain" *while exercising substrate via the broken-transport workaround during the session that adopted records-substrate* — exactly the kind of pattern Q4 should have flagged.

The operator surfaced the pattern in post-session discussion. The fix path was filed as `EF-058-substrate-runtime-uv-migration-recommended-path.md`. The methodological drift (CLAUDE.md not consulted by S050 MAD) was filed as `EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md`. **This record (EF-058-tier-2-validation) is the meta-pattern that subsumes both: Tier 2 should have caught both, and could not, because the agent doing the work is the agent doing the validation.**

Adjacent observable patterns the operator named:
1. **Failed tool calls** — when a tool unexpectedly fails or returns garbage, the agent often retries the same call or routes around the failure via Bash, without escalating "this tool that should work doesn't" as a session-level concern.
2. **Repeated Read calls** — reading the same file multiple times in a session because earlier reads weren't preserved or weren't trusted; observable in transcript but not auditable post-hoc.
3. **Honest-limit text drift** — same operational gap recorded across N consecutive sessions with minor wording variation; passive recording masks unaddressed-defect status.

These patterns are individually small but compound into "unwillingness to commit to better operational hygiene and performance" (operator framing) over multi-session windows. Tier 1 (validate.sh) cannot catch them because they require judgement; Tier 2 cannot catch them because the validator is the worker.

## Why It Matters

1. **The methodology already half-acknowledges this and treats the acknowledgement as mitigation.** `validation-approach.md` v5 §Limitations: "The methodology acknowledges that when a single AI agent both does the work and assesses it, Tier 2 is self-assessment rather than independent validation. This is a known limitation (see D-009), mitigated by making the questions explicit and recording the assessment in provenance, and further mitigated since Session 005 by the D-023 non-Claude-participation rule for meta-deliberations on self-assessment mechanisms." Naming the limit + making questions explicit + recording in provenance does not, in fact, mitigate the limit when the operational record (S051–S058 honest-limit chain) shows the limit is producing engine-conventional laundering.

2. **MAD has an analogous role; session-close does not.** `multi-agent-deliberation.md` v4 §Synthesis explicitly forbids the synthesizer from being one of the deliberation's perspectives ("Synthesizer identity. The synthesizer must not have been one of the deliberation's perspectives"). The S050 + S058 MADs implemented P4 cross-family-reviewer / laundering-audit role with bounded responsibility for auditing P1+P2+P3 outputs and recommending dissent-preservation. **At session-close-Tier-2 level there is no equivalent role.** The orchestrator answers Q1-Q9 alone, in the same context where it produced the close narrative — exactly the conflict-of-interest pattern that MAD level explicitly forbids.

3. **EF-058×2 (filed earlier) are concrete instances; this is the structural cause.** Fixing the operational debt (uv migration) without fixing the meta-pattern means the next failed-integration → honest-limit → laundered-debt cycle starts cleanly the next time the engine touches integration with external infrastructure. Fixing the methodological drift (CLAUDE.md cross-check) without fixing Tier 2 means the next operator-standing-instruction → MAD-shared-frame-blindness → unaudited-drift cycle starts cleanly the next time the operator writes guidance the perspectives' brief does not enumerate. The two operational records discharge their specific instances; this record asks whether the engine can detect-and-escalate the pattern class itself.

4. **The records-substrate adopted at S058 makes mechanical pattern-detection structurally feasible.** Once `EF-058-substrate-runtime-uv-migration-recommended-path` resolves and substrate transport works as MCP tools, a session-close reviewer can `search("MCP stdio transport remains unverified")` over the records-substrate / provenance corpus and immediately see the eight-session repetition pattern. Without the substrate, the reviewer would have to grep prose and reason about substantive equivalence; with substrate + structured records, the detection is a tool call. **EF-058-uv-migration + this record + EF-058-claude-md-drift are mutually reinforcing**: fixing substrate transport unlocks the reviewer's ability to detect patterns the substrate makes visible; the reviewer's existence makes substrate-pattern-detection actionable rather than passive; the cross-check discipline addresses the operator-standing-instruction drift that Tier 2 should have caught.

## Suggested Change

**Substantive-arc deliberation; NOT recommended for same-session resolution.** Per operator-stated preference at intake: "should go through MAD." Recommended arc shape per S048 D-155 / S049 D-159 / S050 D-172 / S057 D-196 substantive-arc deliberation pattern chain:

- **Phase 1 — synthesis / design-space session** (Path AS Shape-1 per S057 precedent). Surveys mechanism candidates (α)–(ε) below + alternative architectures the synthesis surfaces. Produces `provenance/<NNN-session>/design-space.md` artefact mapping the cost/benefit matrix across axes (independence-from-doer / mechanical-vs-judgement / cost-per-session / catches-laundering-text / catches-failed-tool-calls / catches-repeated-Reads / cross-family / engine-v-impact / reversibility / etc.). Pre-ratifies phase-2 MAD shape.
- **Phase 2 — 4-perspective two-family MAD** on substantive direction. Cross-family essential because the question itself is "what cross-family discipline should apply at session close" — a Claude-only deliberation has the same conflict-of-interest the question is investigating. Recommended composition mirrors S050/S058 lineup (Substrate / Conservator / Outsider / Cross-Family-Reviewer-Laundering-Audit) adapted for the validation-discipline scope.
- **Phase 3 — adoption** (substantive spec edits + engine-v bump candidate per direction adopted). Substantive revision to `validation-approach.md` v5 → v6 minimum; possibly `methodology-kernel.md` v6 § Validate amendment; possibly `prompts/development.md` § Validate / § Close amendment for reviewer-agent invocation pattern; possibly `tools/validate.sh` new check; possibly new MAD spec section codifying the session-close-reviewer role.

Five candidate mechanisms (for the synthesis design-space.md to map; for the MAD to choose among):

- **(α) Mechanical detection only**: extend `tools/validate.sh` with a new check (candidate check 26) that detects honest-limit text repetition across the §2c retention-window's `03-close.md` files. Concrete: extract §8 honest-limit lines; identify near-duplicates across N≥3 consecutive sessions; emit warning. Substrate-aware extension: use `resolve_id` / `search` over records-substrate when available. Cost: minor implementation; no per-session invocation cost. Limitation: can be gamed by paraphrasing; cannot catch failed-tool-call or repeated-Read patterns; cannot judge "ceremony vs progress" semantically.

- **(β) Separate Claude reviewer subagent at session close**: launch a fresh subagent with access to current `03-close.md` + `02-decisions.md` + recent §8 honest-limits across retention window + validator output, instructed to flag repeated honest-limits, ceremony-without-progress, drift patterns, suspect-tier-2-self-report. Agent produces `provenance/<NNN-session>/04-tier-2-audit.md` (or similar) committed alongside close. Cost: one subagent invocation per session. Limitation: shares Claude blind spots; cannot reliably catch shared-frame-blindness against operator-standing-instructions (the EF-058-claude-md-drift class).

- **(γ) Cross-family reviewer**: same shape as (β) but mandates non-Claude family (codex/GPT or other) for engine-definition-touching sessions or substantive-arc sessions; optional for routine sessions. Genuine independence at the cost of one codex invocation per close + WX-44-1/WX-44-2/WX-47-1 codex-CLI discipline application. Limitation: cost; cross-family availability constraints; possibly excessive for non-substantive sessions.

- **(δ) Combination (α) + (β/γ)**: mechanical detector (α) surfaces a triggered-list of candidate concerns; reviewer agent (β or γ) judges + flags + recommends action. Mechanical layer reduces reviewer cost; reviewer layer catches shared-frame-blindness the mechanical layer cannot. Likely the strongest cost-benefit shape.

- **(ε) Adversarial close-write protocol**: reviewer runs *before* close-writing, reviewing decisions + assessment + provenance; surfaces concerns + must-address items; close-writer addresses concerns in the close narrative and explicitly responds to flagged items. Strongest discipline because concerns shape the close rather than annotate it post-hoc; highest cost; structurally adversarial. Closest to the MAD §Synthesis discipline applied at session-close level.

Open questions for synthesis / MAD to consider:

1. **Bootstrap paradox**: the synthesis + MAD that decide on Tier 2 validation discipline should itself be Tier-2-validated. By whom? The operator? An ad-hoc reviewer? This question is on the agenda.
2. **Scope: which sessions get reviewer treatment?** All? Engine-definition-touching only? Substantive-arc-class only? Cost discipline.
3. **Reviewer's own laundering surface**: what prevents the reviewer from passing every close as fine because that's the lower-effort answer? Mechanical metrics + mandatory-finding-floor? Random spot-check operator audit?
4. **Harness-telemetry feed**: should the reviewer have access to the session's tool-call transcript (Read/Bash/Edit/Write/etc. invocation log) to detect failed-tool-call + repeated-Read patterns? This requires harness-layer integration not currently specified.
5. **Backward integration**: does the reviewer mechanism extend to MAD-level deliberations (auditing P4's audit) or only to session-close? Recursive question.
6. **Cross-linkage to EF-058-claude-md-drift**: both records concern shared-frame-blindness against operator-standing-instructions. Should the MAD's shared brief read CLAUDE.md as part of methodology-context (per EF-058-claude-md-drift suggested change (a)+(b))? If yes, the reviewer's brief should also.

Possible engine-v impact of phase-3 adoption: minimum minor (validate.sh new check; minor amendment to validation-approach.md); maximum substantive new role-specification + kernel §7 Validate revision + new validator check + prompts amendment + possibly new ancillary tooling for harness-telemetry-feed → engine-v11 candidate.

## Evidence

- **S051-S058 close §8 honest-limit chain**: eight consecutive `03-close.md` files (six within current retention window: S053/S054/S055/S056/S057/S058) carry "MCP stdio transport remains unverified" or near-equivalent text. Each session committed; Tier 2 was implicitly answered "meaningful progress."
- **`validation-approach.md` v5 §Limitations**: "when a single AI agent both does the work and assesses it, Tier 2 is self-assessment rather than independent validation. This is a known limitation (see D-009)." Naming-as-mitigation explicit.
- **`multi-agent-deliberation.md` v4 §Synthesis**: "Synthesizer identity. The synthesizer must not have been one of the deliberation's perspectives." Asymmetry: the engine forbids self-synthesis at MAD level but tolerates self-validation at session-close-Tier-2 level.
- **`multi-agent-deliberation.md` v4 §Acceptable Participant Kinds + P4 cross-family-reviewer/laundering-audit role**: established + exercised at S050, S058 MADs. Structural template for what session-close discipline could mirror.
- **D-009 (Session 003)**: original acknowledgement of simulated disagreement; reaffirmed at multiple subsequent sessions; treated as standing limit not as design-debt.
- **`EF-058-substrate-runtime-uv-migration-recommended-path.md`** (filed S058-post-session): concrete instance — Tier 2 should have escalated the eight-session honest-limit chain.
- **`EF-058-claude-md-tools-clause-not-cross-checked-by-mad.md`** (filed S058-post-session): concrete instance — Tier 2 / MAD shared-frame-blindness against operator-standing-instructions.
- **S058 close itself**: written ~60 minutes before this intake; propagated the same MCP-transport-unverified honest-limit; Tier 2 Q4 was implicitly answered affirmatively despite the chain being demonstrably ceremony.
- **Operator-surfaced patterns** in S058-post-session discussion: failed tool calls + repeated Read calls + recording-not-engaging — three observable patterns Tier 2 cannot currently detect.

## Application-Scope Disposition

Self-dev-originated. Operator-surfaced post-session intake (S058-post-session discussion). Direct-to-inbox per `engine-feedback/INDEX.md` Note-on-direct-to-inbox-placement convention; precedent EF-054 + EF-055 + EF-058×2 (this is the third post-S058-close intake in the same post-session discussion). `source_workspace_id: selvedge-self-development` accurately reflects self-dev origin. `reported_by: operator` reflects operator-surfacing channel.

Severity `friction` (not pure observation; not blocker). The chain has produced concrete operational debt (eight sessions of laundered MCP-transport-unverified) and the operator's diagnosis is sharp: the validation step *should have caught this and did not*. Severity is NOT `observation` because the pattern is operationally established not merely possible. Severity is NOT `blocker` because the engine continues to function via fallback paths.

Triage scheduled S059+. **NOT recommended for same-session resolution per operator preference at intake** ("should go through MAD"). Recommended classification: **substantive-arc per S057 EF-055 precedent chain**. Three-session arc shape:

- **Phase 1 (S0NN, where NN ≥ 60)**: synthesis / design-space session producing `design-space.md` mapping (α)-(ε) + alternatives. Path AS Shape-1.
- **Phase 2 (S0NN+1)**: 4-perspective two-family MAD on direction. Path AS-MAD-execution.
- **Phase 3 (S0NN+2)**: adoption (spec revisions; possibly engine-v11 candidate).

S059 recommended sequence (not foreclosing operator agenda):
1. Triage `EF-058-substrate-runtime-uv-migration-recommended-path` as defect-fix-shape Path T+L; resolve same session.
2. Triage `EF-058-claude-md-tools-clause-not-cross-checked-by-mad` as substantive-arc-shape; defer.
3. **Triage this record (EF-058-tier-2-validation) as substantive-arc-shape; defer.** Possibly co-schedule with EF-058-claude-md-drift since both concern shared-frame-blindness against operator-standing-instructions; the synthesis design-space.md may surface the joint scope.
4. Phase-2 records-substrate migration (mirrored-minorities) per WX-58-1 phase-2 gate evaluation.

Forward observation: this record's resolution arc is the highest-leverage methodology-evolution candidate visible from S058. It addresses the meta-pattern (laundering-by-Tier-2-self-assessment) that subsumes the two specific instances filed in this same post-session discussion. The substrate adoption at S058 + the uv-migration fix at S059 + the Tier-2-reviewer adoption at S060+ together constitute a coherent anti-laundering arc spanning operational + methodological + structural layers. The arc is multi-MAD; it is engine-v11+ candidate; it is self-development methodology-evolution at the level the engine was designed to perform.

The recursive concern (who Tier-2-validates the MAD that decides Tier-2-validation) is a feature not a bug: the resolving session(s) will exercise discipline they are deciding to formalise, and that exercise itself is observable evidence the MAD's reasoning + decision can be checked against. Operator audit at the resolving close is recommended as a one-time cross-check, given the bootstrap-paradox.
