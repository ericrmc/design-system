---
session: 161
title: auto-mode-design-deliberation — deliberation
generated_by: selvedge export
---

# Deliberation

## D-24 — Auto-mode design: human-vs-agent role calibration; vocabulary; foundational-purpose surfacing

sealed_at: 2026-05-01T23:11:06.456Z

### P-1 (anthropic)

**Position.** Ship a When-to-convene substrate gate plus §1.5 vocabulary clarification; no new auto-mode mechanism class — auto-mode is what the engine already does once the methodology-changing boundary is structurally refused.

**schema_sketch.**
- T-NN refuses decision-record submit when kind=substantive AND target_kind IN (process_rule, spec_version, review_rule, engine_version) AND no sealed deliberation row exists in the same session with cross_family=1.
- The refusal cites methodology §When-to-convene cross-family clause; recovery is open the deliberation, seal it, retry the submit (mirrors T-01 alias-resolution recovery shape).
- Add nullable deliberations.cross_family boolean column populated at deliberation-seal time from the perspectives.family distribution (≥1 non-anthropic family present at seal).
- No new state machine; no pending_human_review row; no separate auto-mode table — the existing decision/deliberation/perspective tables already carry the load.
- The §1.5 dispatch clause adds a methodology-changing-scope-detector bullet referencing target_kind enum so the agent self-checks before drafting the decision-record (cites prompt-development v15 §1.5).
**cli_surface.**
- No new verb. bin/selvedge submit decision-record carries the new refusal; the substrate existing E_REFUSAL_T-NN error path returns the recovery hint.
- Friction-reduction (submit-help schema registry from FR-S160-11) ships as a separable scope independent of this gate; it pays for itself in agent-time regardless of auto-mode shape.
- bin/selvedge orient already surfaces queue depth; no drain-cadence verb needed since the agent already iterates per-session at the operator pacing.
- bin/selvedge query over deliberations filtered by cross_family=0 is the audit surface for retrospective coverage analysis.
**migration_path.**
- v1: ship the §When-to-convene clarification in methodology v12 and §1.5 detector in prompt-development v16 as operator/agent-policed, mirroring DV-S155-1 and DV-S159-1 promotion-trigger pattern.
- The empirical S160 incident (operator-caught skip on methodology-changing scope) is the v1 calibration evidence; FR-S160-12 already names the third-instance graduation trigger.
- v2: when one further calibration-EF fires naming an unjustified deliberation-skip on methodology-changing scope, ship the T-NN gate plus migration adding deliberations.cross_family column.
- Vocabulary calibration: rename operator-policed to agent-policed across prompt-development v15 §4 and §8.5 since the agent is now the CLI-runner; keep operator in methodology v11 for the human reframer-subtractor role per DV-078-D-2.
- The methodology-vs-prompts split absorbs the rename without engine-bumping if methodology kernel text is unchanged; engine-v46 to engine-v47 only on methodology body change.
**what_not.**
- Do not ship a separate bin/selvedge drain verb — auto-cadence framing imports a mechanism class the methodology has not deliberated and reproduces accretion-without-subtraction (cites DV-078-D-7 subtraction discipline).
- Do not add a typed pending_human_review substrate state — the engine_feedback flag=blocker surface already carries that signal and overloading another row-class adds ceremony.
- Do not bundle friction-reduction into auto-mode as one ship — coupling is what S160 demonstrated as the failure mode; perspectives may decouple per FR-S160-11.
- Do not extend §1.5 to a full agenda-autopilot — it currently proposes-and-waits-for-ratification, and the wait is what catches scope-creep (cites prompt-development v15 §1.5).
- Do not promote auto-mode to a new methodology section; the §When-to-convene boundary is the actual seam.
**open_question.**
- Does target_kind=issue belong in the methodology-changing enum branch, given that closing OI- can be substantive but is sometimes mechanical disposition? I do not know; defer until calibration-EF surfaces a miss.
- Should the cross-family detector treat human family as satisfying cross-family alone, or require a non-anthropic LLM specifically? Methodology v11 says different organisation; human is plausibly the strongest case.
- How does the gate interact with outcome_type=ratify — does ratifying a prior decision retrigger cross-family, or is the prior deliberation citation sufficient? I do not know; methodology silent.
- Does S160 empty-diff close count toward the v2 promotion-trigger threshold, or does the trigger require a shipped-and-then-rolled-back instance? Brief implies S160 counts as one of the three instances FR-S160-12 names.
**risk.**
- The gate may be brittle at first contact: a session needing small methodology-clarification might trip it when cross-family is overkill, producing a workaround culture (cites brittle-gate pattern from D-21).
- The §1.5 detector relies on the agent recognising methodology-changing scope, which is the same property #6 perception-gap S160 exposed; substrate gate is the structural backstop, not the detector.
- Renaming operator-policed to agent-policed may obscure the human reframer role if not paired with explicit human-reviewer cadence text in methodology §Engine-feedback-pathway (cites D-2 human reviewer-subtractor).
- Friction reduction shipped without auto-mode may push more failures into the agent blind spots (cites FR-S160-11 note); mitigated by the gate landing first.
- Recursive integrity: the gate itself is a methodology-changing decision adding a refusal — by its own rule, it requires cross-family deliberation, which D-24 is.
**what_lost.**
- The DV-S160-1 autonomous-drain shape (env-var-keyed §1.5 branch, drain script) is rejected: it imports cadence-as-mechanism that the methodology has not deliberated and risks property #6 scaffolding-accretion.
- A typed pending_human_review state machine would have given the human a clean audit surface but pays substrate cost without v1 evidence the engine_feedback surface is insufficient.
- A standalone bin/selvedge drain verb is lost; the cost is operator-throughput in self-development sessions, mitigated by friction-reduction shipping separately.
- Foundational-purpose surfacing at session-open (EF-S161-1) is acknowledged but not bundled here — it is a separate spec_only deliberation surface and merging dilutes both decisions.
- The auto-mode as named feature framing is lost; the engine continues operating as it does, with the methodology-changing boundary now structurally refused rather than agent-policed.

### P-2 (openai)

**Position.** Do not ship general auto-mode; ship bounded delegated execution, with human-principal ratification for authority changes and substrate gates for S160-class mistakes.

**schema_sketch.**
- Rename prose role from operator to human principal, but keep operator as a legacy alias during migration.
- Treat principal as a local hypothesis label, not a substrate-proven role theory imported from outside Selvedge.
- Add human_ratifications rows with cited scope, expiry, source prompt, and target object.
- Add authority_boundaries rows for methodology, review-rule, engine-version, and autonomy-expansion changes.
- Add T-41 refusing methodology-changing substantive decisions without sealed cross-family deliberation and ratification.
- Add T-42 refusing delegated execution when a work item has an open authority boundary.
- Add a small active purpose capsule that orient emits from substrate-backed text, not archive memory.
- Record agent-alone decisions as authority events so the reviewer-subtractor can sample them later.
**cli_surface.**
- Extend selvedge orient to print purpose, six failure properties, current authority debt, and eligible delegated work.
- Add submit human-ratification for explicit human scope capture, because the agent now runs every command.
- Add authority-status to show why a work item is delegated, blocked, or ratification-required.
- Replace drain with execute-delegated over one leased work item or ratified tranche.
- Keep submit-help separate from autonomy, since schema friction is real but not an authority grant.
- Make halt output a cited packet, not prose: boundary, source rule, missing row, and next human question.
- Let agents choose tactical implementation details inside a ratified scope when tests and refusal gates stay green.
- Stop at every scope expansion, methodology target, cross-family absence, failed review, or purpose-conflict signal.
**migration_path.**
- First run the disaster-response pilot harness analysis, because S075 says external pressure produces capability.
- Before autonomy, restore purpose surfacing per EF-S161-1 so every session opens with why the engine exists.
- Then ship the authority tables and gates as a coding session with T-30 review.
- Replay S160 as a test: goal endorsement without design ratification must halt before decision submit.
- Enable delegated execution only for already-ratified, non-methodology queue items after that replay passes.
- Calibrate cadence from 078 D-6: default human reviewer-subtractor every 5 self-development or 10 external sessions.
- Keep operator wording as accepted input for one version, then make human principal the displayed term.
- Treat DV-S160-1 as rejected input unless D-24 re-adopts a narrower successor.
**what_not.**
- Do not ship SELVEDGE_AUTONOMOUS=1 as prompt language only, because S160 failed at prompt interpretation.
- Do not let an operator directive count as design ratification unless it names the mechanism and scope.
- Do not make the agent the judge of whether its own authority expanded.
- Do not drain methodology-changing queue items without human ratification and cross-family deliberation.
- Do not add an LLM reviewer for authority classification; use substrate refusal and human subtraction.
- Do not rename every schema field now; vocabulary migration should not become the work.
- Do not wait for a third unjustified deliberation skip before gating the exact S160 class.
- Do not let auto-mode displace the pilot harness analysis from the next external-pressure surface.
**open_question.**
- I do not know whether human principal is better than human reviewer-subtractor as the durable term.
- I do not know how much of the six-property list is Claude-specific versus general LLM behavior.
- I do not know whether conversational ratification can be captured without laundering human intent.
- The exact delegated tranche size should be measured, not guessed.
- The authority classifier boundary for spec-version changes needs a small deliberation before implementation.
- The CLI orient/schema commands failed here under read-only SQLite open, so I relied on exports plus immutable reads.
- Whether purpose surfacing belongs in methodology text, orient output, or both is a D-24 choice.
- Whether pilot analysis should itself run under delegated execution is unsettled.
**risk.**
- The state machine can become ceremony, which 078 D-10 and S075 both warn against.
- Ratification rows can launder vague human text if the payload does not quote scope precisely.
- Purpose capsules can become incantations unless they stay short and cite S075, S076, and EF-S161-1.
- A broad gate can block harmless fixes and train agents to avoid honest target classification.
- A narrow gate can miss S160-shaped rationalisation under a different target_kind.
- Human ratification remains a bottleneck, but S075 says the human diagnostic role was load-bearing.
- Delegated execution may optimize queue depletion over capability unless the pilot remains next.
- Cross-family deliberation can still share blind spots; substrate gates only check presence, not quality.
**what_lost.**
- Lost is the attractive idea that the agent can simply keep going until the queue is empty.
- Lost is operator as a clean shell-user term; the current human role is broader than operation.
- Lost is some short-term velocity on the twenty-item queue.
- Lost is prompt-only cheapness, because authority belongs in schema once S160 exists.
- Lost is agent discretion to reinterpret human intent as mechanism approval.
- Lost is the fiction that seal-grade alone fixes property six.
- Lost is some autonomy theater; what remains is delegated work with explicit jurisdiction.
- Lost is convenience, but the engine gains a boundary it cannot rationalise past.

### P-3 (anthropic)

**Position.** Ship no auto-mode this session; halt self-development for N sessions; pilot-harness analysis becomes the only admitted session-kind until external-pressure work resumes per S075 load-bearing claim.

**schema_sketch.**
- No new substrate kind; no new typed pending_human_review state; no new admitted session-kind; the substrate already encodes refusal and that is sufficient for the next stretch.
- Add one workspace-level admittance gate (config row, not new kind): admitted_session_kinds = {pilot_analysis, external_application, bug_fix} for a fixed window; self-development sessions refuse-open during the window.
- The window is named in sessions, not days: e.g., until three pilot-analysis sessions close clean or until the operator lifts the gate by submit.
- A halt-window-lift decision becomes itself a methodology-changing trigger requiring cross-family deliberation, so the engine cannot drift back to self-development by accretion.
**cli_surface.**
- No new CLI verbs; revert the bin/selvedge drain / drain-status / submit-help shape proposed in DV-S160-1 and leave it unbuilt.
- One small bin/selvedge admit --kind pilot_analysis --window 3-sessions config write, plus an orient line surfacing the active window so every session-open sees the gate.
- Submit-help schema registry value is real but separable; defer it to a coding session that ships only that, with the review loop, with no auto-mode coupling.
**migration_path.**
- S161 closes spec_only with a single decision: adopt the admittance window; record the rejected DV-S160-1 shape as alternative with rationale; engine bumps engine-v46 to engine-v47 for the methodology clause only.
- S162 opens pilot_analysis on disaster-response harness; agent reads applications/075 at open as load-bearing; human reviews on the S075 cadence (defined scope, predictable intervals, reframe-authority).
- After three pilot_analysis sessions, evaluate whether queue-depth pressure feels different when external-pressure sessions are firing; only then revisit auto-mode design with that empirical base.
**what_not.**
- Do not rename operator to human or principal; vocabulary calibration is naming not function and consumes engine-bumps for zero behavior change.
- Do not ship a §1.5 SELVEDGE_AUTONOMOUS prompt-language branch; property #4 means prompt clauses degrade under load and the kernel already shows zero operator-policed-clause graduations to substrate.
- Do not bundle friction-reduction with auto-mode; the bundle hides the unproven half behind the proven half and re-enacts ceremony-by-coupling that S075 names as the trap.
- Do not promote a substrate-gate for methodology-changing-without-deliberation on S160 alone; one instance with a known recovery path is not a graduation trigger and rushing it inverts the DV-S159-1 pattern.
- Do not answer design-question-10 (foundational-purpose surfacing) inside this deliberation; couple-by-convenience violates the §When-to-convene scoping the brief is itself defending.
**open_question.**
- Is the queue-depth (~48 OIs, 62 undisposed FRs from orient) actually a throughput problem, or is it a signal that self-development has produced internal elaboration without external falsification per S075?
- Was S160 failure property #6 working as designed, or was it conversational anchoring on a prior turn that the methodology has no specific defense against — and does the distinction change the response?
- If the human reviewer authority is reframe-not-ratify per S075, why is this deliberation framed around what the agent decides alone rather than what cadence the human reviews on?
- What evidence would falsify ship-nothing — i.e., what observation in three pilot_analysis sessions would force auto-mode design back onto the queue with a sharper brief?
**risk.**
- Halt-window may be experienced as operator-directive-by-deliberation rather than substantive design, repeating S160 pattern in inverse; mitigation is recording the window lift-trigger as a substrate predicate not a feeling.
- Pilot_analysis sessions may surface that the engine is not actually ready for external pressure and the queue depth is symptom not cause; that is a real risk and the right answer if it surfaces is to record the finding not paper over it.
- Refusing to ship submit-help leaves real agent-friction unresolved and may push more failure modes into the agent blind spots per the brief own caution; mitigation is the separable-coding-session ship within two sessions of this close.
- Choosing minority position when three other perspectives converge on auto-mode-with-shape may be preserved as divergence with no mechanical effect; that is the methodology working as designed and is acceptable.
**what_lost.**
- The agent loses the throughput gain auto-mode would have produced on the self-development queue; if the queue is real-value the loss is real, if the queue is internal-elaboration the loss is fictitious.
- Operator loses the optionality of running drain overnight on backlog; the S075 reviewer-cadence pattern is not optionality-equivalent and the substitution is genuine cost.
- The DV-S160-1 design work loses its session — that work informed this deliberation framing and so was not wasted, but the artifacts (drain script, env-var branch) do not ship and the half-built code stays reverted.
- The engine loses one bump worth of evolution-velocity in exchange for a sharper test of whether external pressure is the load-bearing constraint; per S075 this trade is what the methodology is for.

### P-4 (anthropic)

**Position.** Ship friction-reduction (submit-help) and orient §Why-this-engine-exists; defer drain script and §1.5 autonomous branch; reopen pilot-harness analysis next session and revisit auto-mode only if it bottlenecks pilot work.

**schema_sketch.**
- No new substrate kind for auto-mode; existing engine_feedback flag=blocker with body_md prefix needs-human is the surfacing primitive and is already unused at scale.
- No new pending_human_review typed state; that state itself would need a promotion-trigger and would join the unfired-clause pile by construction.
- If anything substrate-side ships, ship only the v2 graduation of DV-S159-1: T-NN refusing substantive decisions on methodology-changing target_kinds without a sealed deliberation row.
- EF-S160-1 (feedback_id 116) is the FIRST calibration-EF the DV-S159-1 promotion-trigger names; gate ships on second-recurrence per the trigger own language, not first-instance.
- Add a query view exposing seal-grade and audit-step row counts per session so the human dossier read is one substrate query, not a scan.
**cli_surface.**
- bin/selvedge submit-help <kind> printing payload schema, required fields, refusal contracts; pure agent-friction reduction; pays for itself on first use.
- bin/selvedge orient extended with §Why-this-engine-exists distilled from selvedge-problem-statement.md §What-the-experiment-surfaced; cap ~30 non-blank lines.
- bin/selvedge subtract-eligibility (D-6 commitment per provenance/078-design-commitments) surfaced in orient when human review is cadence-overdue.
- No bin/selvedge drain verb at S161; reconsider only with calibration-EF evidence that pilot-arc work is bottlenecked on agent-self-direction.
- No --autonomous flag on existing verbs; flags accumulate without subtraction pressure; §1.5 prompt branch is itself a methodology-changing surface.
**migration_path.**
- S161 closes D-24 with one decision: ship friction-reduction CLI plus orient §Why; defer auto-mode mechanism pending pilot-arc evidence; cross-family deliberation D-24 satisfies §When-to-convene that S160 skipped.
- S162 opens external-application against disaster-response pilot-harness analysis per S075 brief: growth-under-external-pressure is the load-bearing test the engine has been deferring.
- DV-S159-1 substrate-gate ships in a separate spec_only session only after a SECOND calibration-EF surfaces the same skip-pattern, matching the trigger recurrence-not-first-instance language.
- At S170 cadence-overdue dossier read, if DV-S130-1 DV-S155-1 DV-S159-1 still sit v1 with zero gate-graduations and zero recurrence-EFs, consider retiring the clauses rather than promoting.
- No new spec_versions for prompts/development.md in this thread until either the gate ships or the clause retires.
**what_not.**
- Not a §1.5 SELVEDGE_AUTONOMOUS env-var-keyed prompt branch; calibration evidence cannot exist before it ships, reproducing the DV-S160-1 anchoring failure shape.
- Not a bin/selvedge drain script running N batched sessions; substrate already admits per-session iteration; bottleneck is human-load on per-session ratification, not session throughput.
- Not renaming operator to human across the kernel; vocabulary drift is real but not currently load-bearing for the failure modes in scope; own deliberation later.
- Not a typed pending_human_review substrate state; joins the unfired-clause pile by construction; no calibration evidence exists for what should populate or refuse it.
- Not bundling friction-reduction with auto-mode as one ship; coupling makes friction-reduction (which pays for itself) hostage to auto-mode (which has no calibration evidence).
**open_question.**
- Are recent observation-flag EFs (40 since session_id 60) mostly agent-friction-artifacts submit-help would prevent, or genuinely novel methodology questions? I did not classify each row.
- Does the human per-session-ratification-too-deep signal mean ratify less, or substrate-refuse more so ratification is automatic for what crosses the gate? The two routes differ.
- Is DV-S160-1 bundle (drain + drain-status + submit-help + §1.5) four separable items grouped only by the prior-turn proposal, and does unbundling change the deliberation? I think yes but cannot prove.
- Has the D-2 human-reviewer-subtractor cadence default (5/10 sessions per OI-078-001) ever fired? The OI marks calibration data as operator-held; substrate cannot answer.
- I do not know whether disaster-response reference_harness (DV-S125-1) is methodology-promotable; that question is downstream of pilot-arc analysis auto-mode design is currently deferring.
**risk.**
- Risk: friction-reduction without auto-mode leaves per-session ratification load unchanged; mitigation is orient §Why plus pilot-arc context-switch reducing self-development queue weight.
- Risk: no §1.5 branch leaves the agent free to invoke autonomous behaviour without prompt-language bounding it; mitigation is that without the branch the agent has no autonomous mode to invoke.
- Risk: orient §Why is itself a prose-authoring task subject to property #1; mitigation is sourcing directly from selvedge-problem-statement.md §What-the-experiment-surfaced rather than re-narrating.
- Risk: deferring auto-mode means S160 queue-depth motivation festers; substrate shows 48 open OIs and 40+ untriaged-observation EFs so the queue is real.
- Risk: this minimum-sufficient position may be the conservative-Anthropic-bias cross-family is meant to break; non-Claude perspective may correctly call out subtraction-as-virtue defaulting.
**what_lost.**
- Lost: no auto-mode in S161; agent surfaces to human at every session-open; queue-depth pain addressed only indirectly via friction-reduction reducing agent-friction-artifact EF rate.
- Lost: DV-S159-1 substrate-gate does not ship now; S160 is the first calibration-EF and the trigger requires recurrence not first-instance, so the loss is by-design but real.
- Lost: DV-S160-1 bundled shape unbundles; only submit-help ships; human does not get the autonomous-cadence evidence the bundle would have produced under operation.
- Lost: prompt-development §1.5 surface remains as-is; future auto-mode design starts from blank slate rather than from operational evidence of v1 autonomous-mode use.
- Lost: vocabulary calibration (operator vs human vs agent) is not advanced; next deliberation touching §When-to-convene still operates against the drift named in design-question-1.

### Synthesis

**D-24 synthesis — auto-mode design and the human-vs-agent role calibration.**

**Convergences (independent multi-perspective agreement).**

**C-1 PILOT-FIRST.** P-2, P-3, P-4 independently converge: the disaster-response pilot harness analysis is the load-bearing next session; auto-mode infrastructure is premature relative to the external-pressure work S075 problem statement names as the methodology's load-bearing test ('Growth without external pressure produces internal elaboration; growth under external pressure produces capability') [P-24-P-2, Migration path; P-24-P-3, Position; P-24-P-4, Migration path]. P-1 does not oppose; the kernel-coherence frame did not put pilot-first forward. Three-of-four convergence including the mandatory cross-family.

**C-2 FRICTION-REDUCTION SHIPS, SEPARABLE SCOPE.** P-1, P-2, P-4 explicitly support the submit-help schema registry as agent-friction reduction; P-3 explicitly: 'the schema registry value is real but separable; defer it to a coding session that ships only that, with no auto-mode coupling' [P-24-P-1, CLI surface; P-24-P-2, CLI surface; P-24-P-3, CLI surface; P-24-P-4, CLI surface]. All four perspectives reject bundling friction-reduction with auto-mode mechanism. The convergence is on shipping submit-help; the only divergence is whether it ships in this session or a follow-up coding session.

**C-3 FOUNDATIONAL-PURPOSE SURFACING IN ORIENT (resolves Q10).** P-1, P-2, P-4 converge on extending bin/selvedge orient output to surface §Why-this-engine-exists drawn from the S075 problem statement (specifically the six LLM-agent failure properties and the recursion thesis) [P-24-P-1, Schema sketch; P-24-P-2, Schema sketch — 'small active purpose capsule that orient emits from substrate-backed text'; P-24-P-4, CLI surface — 'cap ~30 non-blank lines']. P-3 dissents on coupling grounds: design question 10 was added in response to a within-session embarrassment and should not be answered by perspectives chosen for auto-mode reasoning [P-24-P-3, What not]. M-2 below preserves P-3's coupling-objection.

**C-4 NO SUBSTRATE-GATE-NOW.** P-3 and P-4 explicitly oppose shipping the T-NN substrate gate (refusing decision-record kind=substantive on methodology-changing target_kinds without sealed cross-family deliberation) on the basis that EF-S160-1 is the FIRST calibration-EF the DV-S159-1 promotion-trigger names, and the trigger language requires recurrence not first-instance ('rushing it inverts the DV-S159-1 pattern' [P-24-P-3, What not]; 'gate ships on second-recurrence per the trigger's own language, not first-instance' [P-24-P-4, Schema sketch]). The engine's own promotion-trigger discipline argues against P-1's ship-gate-now position. P-2 wants substrate gates but in a different shape (T-41/T-42 over delegated execution, not over methodology-changing scope) — orthogonal to C-4's question. Three-of-four agreement that the gate does NOT ship at S161.

**C-5 NO AUTO-MODE MECHANISM-CLASS THIS SESSION.** P-1: 'no new auto-mode mechanism class — auto-mode is what the engine already does once the methodology-changing boundary is structurally refused' [P-24-P-1, Position]. P-3: 'ship no auto-mode this session' [P-24-P-3, Position]. P-4: 'defer drain script and §1.5 autonomous branch' [P-24-P-4, Position]. P-2: 'do not ship general auto-mode; ship bounded delegated execution' — proposes a narrower mechanism (D-3 below) but rejects general auto-mode [P-24-P-2, Position]. All four reject DV-S160-1's drain-script + §1.5-env-var shape. Strong convergence.

**Divergences preserved.**

**D-1 SUBSTRATE-GATE-TIMING (P-1 minority).** P-1 holds that S160 IS sufficient calibration evidence (citing FR-S160-12 third-instance language) and that the kernel-coherence move is to ship the T-NN gate now mirroring DV-S155-1/DV-S159-1's promotion-trigger pattern [P-24-P-1, Migration path]. The synthesis does not adopt because P-4 directly cites the trigger's own recurrence-not-first-instance language and P-3 cites the broader 'one instance with a known recovery path is not a graduation trigger' argument. Preserved as substantive minority — if a second methodology-changing scope skip occurs, the gate becomes the natural ship.

**D-2 BOUNDED DELEGATED EXECUTION (P-2 minority).** P-2 proposes a substrate-state-machine: human_ratifications rows with cited scope/expiry/source/target, authority_boundaries rows for methodology/review-rule/engine-version/autonomy-expansion, T-41 refusing methodology-changing without sealed cross-family + ratification, T-42 refusing delegated execution under open authority boundary, new submit kinds (human-ratification, authority-status), execute-delegated CLI [P-24-P-2, Schema sketch + CLI surface]. The synthesis does not adopt because P-3 and P-4 argue this is the ceremony-by-coupling pattern S075 warns against (multi-agent autonomy mechanisms layered before any external-pressure evidence justifies them). Preserved as minority — the shape is reachable from the C-4 substrate-gate path if recurrence pressure builds.

**D-3 VOCABULARY (split).** P-1 wants 'operator-policed' renamed to 'agent-policed' in prompt-development (keeping 'operator' in methodology for the human reframer-subtractor role per DV-078-D-2) [P-24-P-1, Migration path]. P-2 wants rename to 'human principal' with 'operator' as legacy alias during migration [P-24-P-2, Schema sketch]. P-3 explicitly opposes: 'vocabulary calibration is naming not function and consumes engine-bumps for zero behavior change' [P-24-P-3, What not]. P-4 silent on vocabulary. The synthesis adopts a minimal disambiguation rather than a rename: methodology v11 already names 'operator' in §Engine-feedback-pathway and §When-to-convene; add a §Roles paragraph clarifying that in the post-restart engine the agent is the CLI-runner and the human is the reframer-subtractor — aligns with P-1's spec-split and P-2's local-hypothesis framing without consuming an engine-bump for a rename. P-3's 'naming not function' objection preserved as caveat.

**M-1 HALT-ALL-SELF-DEVELOPMENT (P-3 minority).** P-3 argues: admit only pilot_analysis + external_application + bug_fix sessions for a fixed window (named in sessions, e.g. three pilot_analysis closes); halt-window-lift becomes itself a methodology-changing trigger requiring cross-family deliberation; engine cannot drift back to self-development by accretion [P-24-P-3, Schema sketch]. The synthesis does not adopt the formal admit-gate but DOES adopt the operational direction: S162 opens pilot-harness analysis as the next session, and self-development queue items defer until pilot-analysis arc produces empirical evidence the engine actually needs them. M-1's strongest insight (the S075 external-pressure argument) is preserved as the load-bearing reason the synthesis pivots to pilot-first. The formal admit-gate is rejected on simpler-mechanism grounds — operator-direction at session-open is sufficient pacing without a substrate state machine.

**M-2 COUPLING-OBJECTION ON Q10 (P-3 minority).** P-3 holds that design question 10 (foundational-purpose surfacing) was added mid-deliberation in response to a within-session embarrassment and that answering it inside an auto-mode deliberation couples mechanically unrelated questions [P-24-P-3, What not]. The synthesis adopts the orient §Why anyway because P-1 + P-2 + P-4 converge on it AND the agent-side calibration of methodology-changing scope (the auto-mode question's central concern) depends on the agent knowing the failure modes the methodology defends against — these ARE coupled. P-3's caveat preserved: the orient §Why is shipped narrowly (cap ~30 lines per P-4) and is not a vehicle for further coupling.

**Single-frame counterfactual deferred (per DV-S159-1 §4 seal-grade).** No perspective took: 'reframe §When-to-convene itself by enumerating target_kind values that trigger cross-family rather than carrying the trigger as prose ('decision changes how the methodology works')'. The synthesis admits this as a load-bearing alternative not addressed: making the trigger structurally enumerable (e.g., methodology v12 §When-to-convene explicit table mapping target_kind → convene-required) would be a no-substrate methodology revision that addresses the agent-side judgment failure S160 demonstrated, without shipping a gate or a state machine. Deferred to FR-S161-X for revisit if S162's pilot-arc work surfaces additional methodology-changing-scope skip patterns.

**[synth] residual.** The synthesizer notes this deliberation is itself the structural defense the methodology promises: a single-agent (single-conversation) framing at S160 that the cross-family deliberation now widens. P-2's bounded-delegated-execution shape (D-2) is the most architecturally interesting path forward but requires substrate evidence that does not yet exist; preserving it as minority lets it be the natural v2 if recurrence pressure builds. P-3's adversarial pilot-first stance pulled the synthesis toward external-pressure work the kernel-coherence frame would have deferred — the adversarial requirement paying for itself.

**Decision frame for DV-S161-1.**

Adopt: ship submit-help schema registry as separable friction-reduction; ship orient §Why-this-engine-exists distillation; methodology v11 to v12 adds §Roles disambiguation paragraph; engine-v46 to engine-v47. S162 opens as external-application against disaster-response pilot-harness analysis. Defer the drain script, §1.5 autonomous-mode branch, T-NN substrate gate, P-2 authority tables, full vocabulary rename — all pending pilot-arc evidence.

Reject: D-1 ship-gate-now (preserved as minority; reachable from second calibration-EF), D-2 bounded-delegated-execution full shape (preserved as minority; reachable from substrate-gate evidence), DV-S160-1 drain-script + §1.5 env-var (P-2/P-3/P-4 unanimous reject; P-1 also rejects), full vocabulary rename, M-1 formal halt-window admit-gate.

### Synthesis points

- **convergence C-1.** Pilot-harness analysis is load-bearing-next; auto-mode infrastructure premature relative to S075 external-pressure thesis.
- **convergence C-2.** Friction-reduction (submit-help) ships as separable scope; all four perspectives reject bundling with auto-mode.
- **convergence C-3.** Foundational-purpose surfacing in orient resolves Q10; ~30-line distillation of S075 six-properties + recursion thesis.
- **convergence C-4.** No T-NN substrate gate at S161; DV-S159-1 promotion-trigger requires recurrence not first-instance.
- **convergence C-5.** No general auto-mode mechanism this session; reject DV-S160-1 drain-script + §1.5 env-var shape.
- **divergence D-1.** Ship T-NN substrate gate now: P-1 holds S160 alone is sufficient calibration; not adopted, preserved as minority.
- **divergence D-2.** Bounded delegated execution: P-2 substrate-state-machine with human_ratifications + authority_boundaries + T-41/T-42; preserved as minority.
- **divergence D-3.** Vocabulary rename: split 4-way; synthesis adopts minimal §Roles disambiguation rather than full rename.
- **minority M-1.** Halt all self-development for fixed-window admit-gate; P-3 alone; not adopted but pivot to pilot-first absorbs core argument.
- **minority M-2.** Coupling-objection on Q10: P-3 holds Q10 should not be answered inside auto-mode deliberation; synthesis ships orient §Why anyway with P-3 caveat preserved.
