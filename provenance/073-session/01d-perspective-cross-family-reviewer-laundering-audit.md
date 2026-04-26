---
session: 073
title: P4 Cross-Family Reviewer Laundering-Audit — Session 073 phase-2 MAD response
date: 2026-04-26
status: complete
perspective: cross-family-reviewer-laundering-audit
committed_at: 2026-04-26T00:00:00+10:00
---

# P4 Cross-Family Reviewer Laundering-Audit

## Frame critique
The brief correctly names the main laundering risks, but the cross-product table in §3c still exerts bundling pressure. A candidate can look coherent because its parts all point toward "harness measurement," while the real decision is several separable authority decisions: who emits the digest, which fields become authoritative, whether reviewers must read it, whether self-report remains admissible, and when validation starts enforcing substrate behavior. I would name the reframe as **z-laundering-1: measurement authority is not inherited from the YAML container**. Authority attaches to the capture path and field semantics, not to the existence of a digest-shaped file.

A second reframe is **z-laundering-2: staging must be per-direction, not a softened bundle label**. "Staged rollout" is only anti-laundering if the staging preserves separate disposition for CM, SCD, RAD, REVD, CHKD, and EVD. Otherwise it can launder delay into prudence or launder maximal scope into inevitability.

Reviewer overlap disclosure: this P4 role is downstream of S071 P4's §10.4-M29 bundling-by-laundering position and endorses the S071 §10.4-M28 measurement-authority separation. That is not independent validation of those prior claims. It is an audit continuation from the same family surface, and synthesis should counterweight it with P3 or subsequent Tier 2.5 review where those claims are load-bearing.

## Q1 — capture mechanism preferred end-state
Preferred end-state: **CM1 primary plus CM3 secondary reconstruction**, with CM2 reserved as a portability path. I do not support CM3-only as the end-state, because §3b classifies it as secondary post-hoc reconstruction and because it cannot carry the same authority as harness-emitted telemetry. I also do not support CM1-only as sufficient for the full arc, because a hook-only implementation can hide deployment gaps behind "not available here" conditions.

CM1 should be the primary authority path because §3b identifies it as low-cost and harness-emitted. CM3 should be implemented or specified as a secondary comparator or bridge, not because it is equal authority, but because it prevents hook availability from becoming a single point of truth. CM4 remains excluded; in-session agent emission must not become "harness-measured" by writing the same schema.

## Q2 — schema scope
I support **SCD-3 as the target schema**, with an initial implementation tranche no smaller than SCD-2 if staging requires it. SCD-1 is too narrow for the adopted §10.4-M28 authority separation and EF-068 D2 read-discipline telemetry. SCD-4 should remain deferred because records-substrate promotion is a different maturity step, and folding it into γ would be classic bundling-by-laundering.

The §3d schema has the right mandatory fields: `producer_kind` and `authority_level`. However, a top-level pair is insufficient if one digest can contain mixed-origin fields. Either the digest must be single-producer by construction, or individual sections/records need their own authority metadata. For example, a harness-emitted file can contain an agent-declared workaround description, and that text must not inherit primary status from the file-level header. The schema also needs an explicit rule that `agent-declared` can never be promoted to `harness-measured` solely through digest shape.

## Q3 — reviewer availability discipline
I support **RAD-3**: D2.1 as the named end-state with a D2.2 transition window. RAD-1 is too brittle during rollout because unavailable or malformed digest capture would block reviewer audit before the system has proven its capture path. RAD-2 alone is too weak because "available when available" can become permanent non-adoption.

The transition should be named against the VD-003 window. Until S076 review, reviewers should always receive the digest when present and must record absent-digest limits. At or after S076, if capture has produced stable primary or secondary digests, the engine should decide whether to activate the D2.1 hard precondition.

## Q4 — reviewer self-report disposition
I support **REVD-2 with quarantine semantics, transitioning to REVD-3 after stable harness measurement**. Immediate REVD-1 risks pretending the harness baseline already exists. But REVD-2 is acceptable only if self-report fields are explicitly marked `producer_kind: agent-declared`, `authority_level: tertiary`, and excluded from threshold arithmetic where harness data is required.

This is the highest laundering-risk area. If `duration_minutes` and `reviewer_cost` remain visible beside measured fields without strict admissibility rules, reviewers and syntheses may keep treating them as comparable evidence. That would preserve the EF-067 surface under a new label. The correct stance is: preserve self-report during transition for continuity and anomaly comparison, but do not let it settle decisions that require measurement authority.

## Q5 — check 26 substrate-aware branch
I support **CHKD-2 substrate-preferred-with-fallback**. §3a shows n=2 observation points after codification, explicitly insufficient for adjudicating durable behavior change versus design-space-salience compliance. CHKD-1 would turn an immature observation window into a hard gate too early. CHKD-3 would defer enforcement past the point where γ is supposed to make substrate use load-bearing.

The fallback must be narrow. If substrate tooling is available, zero session-open use should be exceptional and recorded. If tooling is unavailable, the validation result should preserve an honest-limit path rather than pretending the requirement was satisfied.

## Q6 — engine-v cadence
I support **EVD-3 multi-step bump** for the direction I recommend. A single substantive bump would launder several distinct changes into one ratification event: capture mechanism, schema authority semantics, reviewer input discipline, self-report disposition, and validation behavior. EVD-2 is acceptable for a smaller γ-2 implementation, but it under-specifies the transition to a D2.1 end-state.

The cadence should separate at least: capture/digest scaffolding, reviewer prompt/read discipline transition, and final substantive validation-approach revision. The substantive bump should occur when authority semantics and reviewer obligations are settled, not merely when a file can be emitted.

## Q7 — reviewer-prompt-template extension scope
I support **minimum-viable extension immediately, full extension after n=2 digest-producing sessions**. The immediate prompt template must force reviewers to inspect `producer_kind`, `authority_level`, absent-digest handling, and self-report quarantine. That is the minimum needed to prevent measurement-authority laundering.

The full extension should wait until two sessions have exercised the digest path. Otherwise the template may encode speculative fields and create compliance theater around an untested schema. This matches the brief's lock-in-after-n=2 framing for Q7.

## Q8 — bundle-vs-defer EF-068-read-write-rebalance
Defer the EF-068-read-write-rebalance four-record bundle. The aggregate-budget obligation in §2 is real, but close-rotation S067 OUT mechanically discharges the S073 must-include aggregate-reducing action. Using that pressure to open a broader read-write rebalance bundle would launder budget maintenance into γ implementation scope.

The reopen warrant should remain live for S074+, especially if aggregate pressure persists after close rotation. But S073's phase-2 MAD is already deciding a dense authority and capture surface. Expanding it now would reduce rather than increase decision clarity.

## Q9 — implementation-locus session-shape
I support **Path-AS at S074+**. The implementation touches capture, schema, validation behavior, reviewer prompts, and possibly read-contract semantics. A single-orchestrator path would concentrate too many authority decisions in one implementation locus.

Path-AS should still be bounded. Separate work should be assigned by surface: capture mechanism, schema/spec semantics, validation check behavior, and reviewer prompt changes. That preserves reviewability and prevents one successful slice from laundering the rest as already settled.

## Q10 — cross-spec interaction depth
The target should be **substantive `validation-approach.md` revision plus targeted minor read-contract/retrieval-contract amendments as needed**, not a new spec class. The digest is a validation and reviewer-input artifact before it is a records substrate. Creating a new spec class now would invite SCD-4 by implication.

If D2.1 becomes a hard reviewer precondition, read-contract implications may become substantive later. For S073 selection, the clean line is: validation-approach owns authority semantics and reviewer use; read-contract records the session-open substrate expectation and fallback discipline; retrieval-contract changes only if digest generation or indexing actually depends on it.

## Cross-product candidate position
I advocate **(γ-6) de-laundered staged hybrid**, closest to γ-5 but with explicit per-direction disposition:

CM: CM1 primary plus CM3 secondary bridge/comparator; CM2 deferred portability option; CM4 excluded.
SCD: SCD-3 target, with SCD-2 permitted as first implementation tranche only if field-level authority rules are already specified.
RAD: RAD-3, with S076 review as the natural decision point for D2.1 activation.
REVD: REVD-2 now with quarantine semantics, transition to REVD-3 after stable harness measurements.
CHKD: CHKD-2.
EVD: EVD-3.
Q8: defer EF-068-read-write-rebalance bundle.

If synthesis requires one of the named candidates, select **γ-5 over γ-2**. γ-2 is not wrong, but it leaves too much hidden in "default per ε hybrid": CM1-only can obscure capture unavailability, RAD-2 can become indefinite best-effort, and REVD-2 can preserve self-report authority unless quarantined. γ-5 better names the staged movement toward measurement authority while retaining post-hoc reconstruction as secondary evidence.

I reject γ-1 as bundled-inevitability framing. It treats the shared direction of travel toward harness measurement as a reason to adopt maximal schema, hard substrate requirement, retrospective re-baseline, and single substantive bump together. Those components do not have equal maturity. I also reject γ-3 as bundled-deferral framing. CM3 plus SCD-2 plus CHKD-3 is too likely to produce a digest-looking artifact while deferring the very authority separation γ is meant to implement.

## Honest limits
I have not read the full S072 design-space file; this response relies only on the embedded condensed brief.

I cannot verify the actual Claude Code hook behavior, transcript format, or implementation effort. No external hook details are imported here.

The proposed S076 activation point is an inference from VD-003 review timing, not a quoted requirement.

I cannot inspect whether current validation tooling can express CHKD-2 cleanly without creating brittle false positives.

My overlap with the S071 P4 laundering position means this is continuity of audit reasoning, not independent corroboration of §10.4-M29.

The field-level authority concern depends on whether the final digest allows mixed-origin content in one file; the brief's §3d example does not settle that.

## Dissent-preservation
If synthesis adopts γ-1, preserve a minority warrant: **M30 candidate — maximal-scope measurement-authority laundering risk**. Activation trigger: any implementation step treats YAML presence, hook emission, or a single substantive bump as sufficient to retire agent-declared self-report or activate hard reviewer preconditions without field-level authority rules.

If synthesis adopts γ-2 without RAD-3 and self-report quarantine, preserve: **M31 candidate — ε-default laundering by indefinite best-effort**. Activation trigger: two digest-capable sessions pass with reviewers treating absent digest as ordinary rather than as an honest-limit condition, or self-report fields remain used in threshold arithmetic.

If synthesis adopts γ-3, preserve: **M32 candidate — minimum-viable deferral laundering**. Activation trigger: CM3/SCD-2 artifacts are cited as satisfying EF-059 z6 or EF-068 D2 without a named transition to primary capture and SCD-3 authority semantics.

If synthesis adopts γ-5 or γ-6, preserve a narrower implementation warrant: **M33 candidate — staged-hybrid per-direction disposition requirement**. Activation trigger: any stage collapses CM, SCD, RAD, REVD, CHKD, and EVD decisions into one ratification claim rather than recording separate disposition and evidence for each.
