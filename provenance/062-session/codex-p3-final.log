---
session: 062
title: P3 Outsider Frame-Completion perspective for EF-058-tier-2-validation MAD
date: 2026-04-25
status: complete
perspective: outsider-frame-completion
committed_at: 2026-04-25T23:15:00+10:00
---

# P3 Outsider Frame-Completion perspective

## Frame critique

The design-space gets the central failure right: `validation-approach.md` v5 §Limitations admits Tier 2 can be self-assessment, and the S051-S058 chain shows that naming the limitation did not prevent laundering. But I think design-space.md §4 over-compresses the analogy between MAD synthesis and session-close Tier 2. The asymmetry is not simply “forbidden self-synthesis vs tolerated self-validation”; it is also “rare canonical synthesis after multiple independent inputs vs frequent close validation of a single session’s work product.” `multi-agent-deliberation.md` v4 §Synthesis has a non-participant synthesizer because synthesis collapses plural perspectives into a canonical artefact, and §Limitations names synthesis as the highest-risk single-agent re-entry point. That does not automatically imply every session close needs a non-doer reviewer.

The missed frame is that EF-058 is less about “another agent should read the close” and more about **liveness of recorded debt**. The failure was not merely that one close was self-approved. It was that a repeated unresolved condition stayed alive as text while losing force as an obligation. That is a state-management failure across sessions. A reviewer helps only if it is given a stateful account of unresolved obligations and a rule that stale obligations require escalation.

I would therefore add two alternatives to design-space.md §5:

- **(z5) Validation-debt lifecycle ledger**: generalise (z2) beyond honest-limit records. Any repeated honest-limit, failed integration workaround, unresolved tool defect, or standing-instruction mismatch becomes a lifecycle item with `introduced_session`, `owner_or_surface`, `next_action`, `review_by_session`, `status`, and `escalation_disposition`. The validator checks stale lifecycle items mechanically. This turns “recording-not-engaging” into an auditable state transition, not a prose judgement.

- **(z6) Harness telemetry digest, not raw transcript first**: before giving reviewers the full tool transcript, produce a structured close-time digest: failed tool calls, retries, repeated reads by path, fallback route-around events, and anomalous command patterns. This is cheaper, less noisy, and more reviewable than asking an LLM to inspect a full transcript. Raw transcript access can remain an escalation path.

These are not replacements for independent review. They are the missing substrate that makes independent review less ceremonial.

## Q1 — Primary direction choice

My primary direction is **(δ) combination, but trigger-scoped and stateful: (α) + (γ for substantive/triggered cases) + (z5) + staged (z6)**.

Mechanical detection alone, design-space.md §5α, is necessary but too narrow. It would have caught near-duplicate honest-limit text, especially given the records-substrate feasibility shown in design-space.md §3.1 and §3.4. But the intake’s adjacent patterns include failed tool calls and repeated Reads, which §5α explicitly cannot see. It also cannot judge Tier 2 Q4’s “meaningful progress” question from `validation-approach.md` v5 §Tier 2.

Universal cross-family review, design-space.md §5γ, is directionally attractive but too expensive and too easy to ritualise. The matrix in §6 correctly scores it high on independence and high on cost. My concern is that a per-session non-Claude reviewer becomes the next ritual: a different model says “looks fine” after reading an under-specified packet.

The best architecture is:

1. Add mechanical detectors for stale/repeated honest-limits and missing lifecycle fields.
2. Create a validation-debt lifecycle ledger, initially light enough to implement without a full records-substrate phase.
3. Trigger cross-family review when a session is engine-definition-touching, substantive-arc-class, closes or defers a lifecycle item, or has mechanical warnings.
4. Use a Claude reviewer only as fallback when cross-family is unavailable, with explicit annotation.
5. Defer full adversarial pre-close review except for high-risk adoption sessions.

This preserves the design-space §6 benefit of (δ), but changes the unit of review from “read the whole close and opine” to “review flagged obligations and their disposition.”

## Q2 — Asymmetry assessment

The asymmetry is **partly principled but currently over-broad**.

It is principled that MAD synthesis has stricter rules than ordinary session-close Tier 2. `multi-agent-deliberation.md` v4 §Synthesis concerns a canonical synthesis after independent perspectives, and §Limitations names synthesis as the highest-risk re-entry point. That role is not identical to a close writer answering `validation-approach.md` v5 Q1-Q9.

But the current Tier 2 rule is under-specified where close validation makes load-bearing claims about progress, unresolved debt, and methodology alignment. `validation-approach.md` v5 §Limitations says self-assessment is mitigated by explicit questions and provenance. The S051-S058 chain, measured in design-space.md §3.1-§3.2 and described in the intake Observation, falsifies that as sufficient mitigation for repeated operational debt.

So I would not say “apply MAD synthesis discipline to all closes.” I would say the asymmetry’s **boundary** is wrong. Routine workspace validation can remain self-assessed. Stale debt, engine-definition changes, substantive arcs, and repeated warnings need distinct review.

## Q3 — Scope-discipline

Reviewer treatment should apply to:

- **All engine-definition-touching sessions**: edits to `specifications/`, methodology prompts, validation tooling, record contracts, or MAD rules.
- **All substantive-arc sessions**: especially adoption/resolution closes.
- **Any session with mechanical validation-debt warnings**: repeated honest-limit, stale lifecycle item, unresolved failed-tool pattern, missing disposition.
- **Operator-discretionary sessions**: explicit operator request should always trigger review.

It should not apply universally at first. Universal review has two problems: cost, and habituation. The design-space §6 matrix recognises the high cost of (γ)/(δ)/(ε). I would rather preserve reviewer attention for cases where the review has teeth.

The mechanical layer should run every session. The distinct reviewer should be triggered.

## Q4 — Reviewer's-own-laundering surface

A mandatory-finding-floor is the wrong fix. It incentivises weak findings. The better controls are:

1. **Structured evidence requirements**: every reviewer pass must cite the close section, decisions section, validator output, and any active lifecycle items reviewed.
2. **Disposition table**: each flagged item must be marked `accepted`, `disputed`, `deferred`, or `resolved`, with rationale.
3. **Stale-item escalation**: if an item persists beyond `review_by_session`, a pass is invalid unless it explains why continued deferral is substantive progress.
4. **Reviewer metrics**: record reviewer identity, family, duration, findings count, and overridden findings. Design-space.md §10 honest-limit 9 gestures toward a three-session observation window; I endorse that.
5. **Operator spot-audit cadence**: not every session, but every engine-v bump and every N substantive arcs.

The reviewer should be allowed to find no issues, but not allowed to provide an evidence-free pass.

## Q5 — Harness-telemetry-feed

Yes, but staged. Full transcript review is probably too large and noisy for S062 adoption. The in-scope S062 decision should specify the requirement; implementation can be deferred.

I recommend (z6): a **harness telemetry digest** first. It should include failed tool calls, repeated reads by file path, retry clusters, fallback route-around events, and unavailable-tool annotations. The intake names failed tool calls and repeated Read calls as transcript-visible but not post-hoc auditable. Design-space.md §3.3 and §6 correctly mark the harness-feed gap as unsolved across all candidates.

S062 should not try to design the whole harness interface. It should record that Tier 2 distinct review is incomplete without telemetry, and create a deferred implementation surface.

## Q6 — Cross-spec interactions

In S062 scope:

- `validation-approach.md` v5 → v6: mandatory. The §Limitations language cannot remain as-is if this MAD decides naming-as-mitigation failed. Add distinct review triggers and validation-debt lifecycle language.
- `tools/validate.sh`: in scope for honest-limit repetition and lifecycle-item checks, consistent with design-space.md §7.5.
- `prompts/development.md`: in scope for close workflow instructions, but only the minimal invocation/disposition pattern.
- `multi-agent-deliberation.md` v4: narrow in scope. Update only if non-Claude participation rules or stance brief requirements are changed.
- `methodology-kernel.md` v6 §7 Validate: defer unless the adopted mechanism changes the conceptual definition of Validate. Kernel edits should be avoided for first adoption if possible.

Deferred:

- `read-contract.md`: defer until telemetry access is designed.
- `records-contract.md`: defer full `records/honest-limits/` or validation-debt record family unless S063 chooses the heavier z5 implementation.
- `tools/build_retrieval_index.py`: defer unless lifecycle records become first-class records immediately.

The cross-spec scope is a deliberation surface because the choice between “prompt + validator check” and “new record family + kernel amendment” changes cost and reversibility.

## Q7 — Multi-session arc shape

Use **three sessions** unless the MAD chooses only (α).

S062 can decide direction. S063 should implement the minimal rule: validation-debt lifecycle fields, mechanical detector, and triggered reviewer protocol. S064 should observe at least one application and adjust. Design-space.md §8.4 suggests phase-3 adoption may take 1-2 sessions; for my recommended shape, collapsing adoption and observation into one session risks reproducing the same self-validation problem.

Arc length and content are partly separable, but heavier directions force longer arcs. (α) can be one adoption session. (δ)+(γ)+(z5) should not be.

## Q8 — Cross-linkage with EF-058-claude-md-drift

Separate the resolutions, but preserve a hard forward recommendation.

Including CLAUDE.md in this MAD’s shared brief is good evidence of the desired discipline, and shared brief §7 does that. But EF-058-claude-md-drift is not the same problem. This MAD concerns Tier 2 validation and session-close review. The CLAUDE.md drift issue concerns what stance briefs must include so independent perspectives do not share a hidden omission.

Jointly resolving both risks a Frankenstein change: one mechanism for close review, another for MAD brief construction, both under-argued because they are bundled. The better result is:

- This MAD recommends that future MAD shared briefs include operator standing instructions when they are load-bearing.
- The claude-md-drift MAD separately decides the exact `multi-agent-deliberation.md` §Stance Briefs amendment.

So: linked evidence, separate adoption.

## Q9 — Bootstrap-paradox handling

Operator audit at resolving close is necessary but not sufficient.

The intake’s Application-Scope Disposition recommends one-time operator audit. That is appropriate for this arc because the engine is changing the mechanism by which it evaluates itself. But the structural bootstrap issue recurs whenever the engine changes validation rules.

I recommend:

1. Operator audit at the S063 or S064 resolving close.
2. A three-session observation window for the new reviewer mechanism, as design-space.md §10 honest-limit 9 suggests.
3. A validator warning if a session resolves a validation-discipline change without either distinct review or operator-audit annotation.
4. Reopen warrant if the new reviewer produces three consecutive evidence-free passes on substantive-arc closes.

This makes bootstrap handling a small standing rule, not an ad hoc exception.

## Q10 — Recursive question

Do not extend the session-close reviewer mechanism to “audit P4’s audit” as a default. That is infinite regress with little payoff.

MAD already has distinct protections: independent perspectives, non-participant synthesis, dissent preservation, and cross-family participation when required by `multi-agent-deliberation.md` v4 §When Non-Claude Participation Is Required. P4 is a perspective, not the final authority. The highest-risk re-entry point remains synthesis, not P4’s perspective.

However, the close reviewer should be allowed to audit the **MAD session close** for whether P4 concerns and preserved dissents were handled. That is different from auditing P4 itself. The reviewer asks: did synthesis and decision records preserve material dissent, cite load-bearing claims, and avoid laundering reviewer objections? This keeps recursion bounded at the session artefact level.

## Honest limits

I reasoned only from the concatenated brief, design-space, and intake text. I did not inspect repository files directly, so my citations depend on the excerpts provided here.

My (z5) lifecycle-ledger proposal may overlap with design-space.md §5z2 more than I claim. The distinction I intend is broader scope: not just honest-limits as records, but all validation debt with liveness fields and stale-item escalation.

I am uncertain about implementation cost. A minimal lifecycle ledger could be a markdown table checked by `validate.sh`; a first-class records family would be substantially larger and would touch `records-contract.md`.

I also cannot evaluate actual Codex/Claude availability constraints beyond the design-space references to WX-44/WX-47 fragility. That matters because my recommended architecture relies on triggered cross-family review.

## Dissent-preservation recommendations

Preserve as dissent if rejected: the asymmetry is partly principled; universal cross-family close review is not justified merely by analogy to MAD §Synthesis.

Preserve as reopen warrant: if the adopted mechanism lacks stateful validation-debt lifecycle tracking, and repeated honest-limit text reappears across three sessions, EF-058 should be considered substantively unresolved.

Preserve as forward arc: harness telemetry should be implemented as a structured digest before raw transcript review becomes a reviewer obligation.