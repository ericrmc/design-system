---
id: EF-075-reviewer-side-substrate-use
source_workspace_id: selvedge-self-development
source_session: 075
target: methodology
severity: observation
status: new
reported_by: operator
filed_at: 2026-04-26
---

# Reviewer-side substrate use is structurally absent

## Summary

Reviewer-prompt-template v3 minimum-viable extension at S075 D-294 instructs reviewers to inspect the harness-telemetry-digest when present, distinguish per-record `producer_kind` / `authority_level`, apply REVD-2 quarantine semantics, and verify capture-adapter metadata coherence. It does NOT instruct reviewers to actively query the retrieval substrate (`mcp__selvedge-retrieval__search` / `forward_references` / `resolve_id`) during their audit.

The result is that Tier 2.5 reviewers operate as artifact-readers rather than substrate-led-evaluators, despite §10.4-M23 P3 substrate-led reviewer-judged frame having been substantively adopted at S064 D-233. The reviewer's audit consumes the artifacts the orchestrator hands them; it does not interrogate the workspace's cross-cutting state with the substrate the workspace exposes.

## Operator note (S075 post-close intake)

> "Surely there's more the orchestrator can do when having a near-instant retrieval mechanism, it should be checking lots of symbols and links to ensure consistency, quality, and integrity."

The same applies to the reviewer at audit time. The operator note framed this as substrate use that the workspace has the capability for but hasn't operationalized.

The operator separately noted that wall-clock + token count for reviewer cost is optional rather than an optimization target. This means reviewer-cost growth from substrate-querying is not a binding constraint — the audit-quality lift is what matters, not the audit-cost minimization.

## Concrete missing instructions in template v3

A v4 template extension could instruct reviewers to:

1. **Before §3a (close correctness)**: run `forward_references('D-<NNN>')` for each load-bearing decision number cited in the close, to confirm each decision is actually present at the cited location.
2. **Before §3b (mechanism adequacy)**: run `search('<mechanism keyword>')` to enumerate every cross-spec mention of the mechanism being audited. Cite the search results when claiming mechanism-text-coherence.
3. **Before §3c (trajectory discipline)**: run `forward_references('VD-<NNN>')` and `forward_references('§10.4-M<NN>')` for each in-flight lifecycle item and preserved minority. Compare ledger state against substrate-surfaced mentions across retention window.
4. **Before §5 (stale-item escalation)**: run a substrate query that enumerates every mention of `review_by_session: S<NNN>` for sessions ≤ current; surface candidates for stale-item escalation that the (z5) ledger hasn't already named.
5. **Before §7 (next-session-shape)**: run `forward_references` for the recommended next-session ID to enumerate forward-commitments that should be honored or explicitly superseded.

These are not optional augmentations; per §10.4-M23 P3 substrate-led reviewer-judged frame, they ARE the discipline the v6 audit-shape was supposed to operationalize. The current template v3 falls short of that.

## Proximate evidence

The S075 codex audit (`provenance/075-session/04-tier-2-audit.md`) found 5 substantive findings (F0-F4). Several of those findings — F1 (authoritative state surfaces lag narrative), F2 (engine-manifest D-NNN placeholders), F3 (active spec text PreToolUse drift) — are exactly the class of cross-cutting consistency that substrate queries would catch immediately. Codex caught them by careful manual reading; substrate-led queries would catch them faster, more reliably, and produce reusable evidence trails.

## Cross-linkage

- **§10.4-M23 P3 substrate-led reviewer-judged frame** (S064; substantively adopted as v7 audit-shape direction) — this record is a direct exercise of M23's reopen warrant (a) reviewer-judges-without-substrate-input.
- **(z7) reviewer-prompt-template versioning + lock-in-after-n=2** — at S075 close template v3 is candidate (n=1 application). v4 extension would require explicit-deliberation-surface per (z7).
- **EF-059 harness-telemetry-feed-for-tier-2-reviewer** — orthogonal: EF-059 is about getting telemetry INTO the reviewer's hands; this record is about the reviewer querying substrate ACTIVELY. Both progress phase-3 (γ) discipline.
- **EF-067 reviewer-wall-clock-self-report-unreliable** — operator's S075 cost-reframe note (cost not optimization-target) means substrate-querying overhead is not a blocker for v4 template extension.

## Candidate dispositions

1. **Path-AS scope at future session** (substantive arc; reviewer-prompt-template v4 substantive extension; new minimum-viable instructions per above).
2. **Path-PD scope** (operator-direct minor extension to template v3 specifically adding 1-2 substrate-call instructions, without full template revision).
3. **Defer past S076** (let v3 lock-in at S076 per (z7) n=2 first; treat v4 extension as the next iteration).

Disposition selection is a future-session decision; not pre-ratifying at intake.

## Triage notes

Operator-surfaced post-session intake at S075 close. Eighth-of-record operator-surfaced intake (after EF-054 + EF-055 + EF-058×3 + EF-067 + EF-068×2 + EF-073). Observation-class, not friction or blocker; the system functions at v3, but the §10.4-M23 substrate-led discipline isn't operationally realized.
