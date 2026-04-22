---
session: 024
title: Shared deliberation brief — MAD 6K-soft-warn response
date: 2026-04-23
status: anchor
---

# Session 024 shared brief (byte-identical non-role sections across all four perspectives)

## §1 Methodology context

Selvedge is the methodology; the Selvedge engine at engine-v4 is its current loadable implementation; this workspace is the self-development application. The nine-activity kernel (`methodology-kernel.md` v5), multi-perspective deliberation (`multi-agent-deliberation.md` v4), two-tier validation (`validation-approach.md` v5), and the read-contract (`read-contract.md` v2) are all operative.

This session is operator-directed Path A per Session 023 close: respond to the designed 6K-soft-warn firing on `specifications/multi-agent-deliberation.md` (hereafter "MAD") under `read-contract.md` v2 §8. The soft-warn is the mechanism working — Session 023 D-086 R2 adopted 6K/8K values precisely to fire at files approaching the hard ceiling. Session 024's job is to deliberate which §8 remediation shape fits.

## §2 Problem statement

**MAD is 6,403 words of body content** (validator-measured via `wc -w`, frontmatter excluded). The `read-contract.md` v2 §2 soft-warning threshold is 6,000 words; the hard ceiling is 8,000 words. MAD is at 80% of the hard ceiling and 107% of the soft warning. No other default-read file is above either threshold.

`read-contract.md` v2 §8 names four remediation shapes:

- **A.1 Restructure in place.** Reduce MAD to under 6K (soft clears) or under ~5.2K (well-clear) by compression, redundancy removal, consolidation of YAML examples, prose tightening.
- **A.2 Split.** Partition MAD into two or more default-read files each under the soft warning. Candidate seam: the four v4-added OI-004 sections (Closure Criteria + Criterion-4 Articulation + Acceptable Participant Kinds + Closure Procedure ≈ 1,463 words) move to a new `multi-agent-deliberation-oi004.md`. MAD residual: ~4,940 words.
- **A.3 Relocate to archive.** Move detail-heavy content (e.g., the full YAML schema blocks in §Heterogeneous-Participant Recording Schema; the non-normative §Open Extensions list) to an archive-pack; retain governance text at default-read with `[archive: path]` references. MAD residual depends on what moves.
- **A.4 Carry the warning.** Legitimate per §8 ("the next session should consider restructuring"; *consider* ≠ *execute*). No spec change; no tool change; no engine-v bump. §5.2 Skeptic vindication strengthens if content does not grow.

A.1 / A.2 / A.3 substantively revise MAD and hence fire d016_2 + d023_2 → D-023 required non-Claude participation (satisfied by the Outsider included in this deliberation). If the revision is classified as an engine-v-bump per `engine-manifest.md` §5, engine-v4 → engine-v5 — **and §5.4 Session 022 cadence minority escalates from activated to substantive, forcing a same-session §5 revision deliberation per OI-018** (engine-v5 before Session 026 is the escalation trigger).

A.4 is a deliberated decision-not-to-act. No engine-v bump. Still d016_3 if the deliberation is substantive.

## §3 Current-state facts (validator-measured at session open)

### §3.1 MAD section structure and word counts

| Section | Lines | Words | Classification |
|---|---|---|---|
| Purpose | 13 | 324 | header/scope |
| §Specification (container) | — | — | — |
| When Multi-Agent Deliberation Is Required | 13 | 152 | normative core (D-016 triggers) |
| When Non-Claude Participation Is Required | 25 | 215 | normative core (D-023 triggers) |
| Trigger-Coverage Annotation Schema | 42 (incl. code example) | 474 | normative-plus-schema |
| Perspectives | 7 | 94 | normative core |
| Stance Briefs | 17 | 259 | normative core |
| Non-Claude Participation Mechanism | 22 | 317 | normative core |
| Heterogeneous-Participant Recording Schema | 79 | 772 | **normative + large YAML blocks** |
| Mechanism | 8 | 113 | normative core |
| Synthesis | 15 | 244 | normative core |
| Provenance Layout | 50 | 196 | normative + layout example |
| Graceful Degradation | 7 | 160 | normative core |
| Limitations | 14 | 301 | normative + important caveats |
| Closure Criteria for OI-004 | 11 | 149 | OI-004-scoped |
| **Criterion-4 Articulation for OI-004** (v4) | 28 | 497 | OI-004-scoped |
| **Acceptable Participant Kinds for OI-004** (v4) | 34 | 397 | OI-004-scoped |
| **Closure Procedure for OI-004** (v4) | 29 | 420 | OI-004-scoped |
| Interaction with Existing Decisions | 11 | 160 | history/cross-reference |
| Open Extensions | 15 | 671 | **non-normative futures register** |
| Validation | 20 | 389 | normative (checklist) |

**Total body: 6,403 words.** The four OI-004-scoped sections (Closure Criteria + Criterion-4 Articulation + Acceptable Participant Kinds + Closure Procedure) = **1,463 words**. §Heterogeneous-Participant Recording Schema = **772 words** (of which an estimated ~400 words are YAML field blocks and code examples). §Open Extensions = **671 words** (candidate-register; `[activation precondition: ...]` items).

### §3.2 Aggregate default-read surface at session open

Check 20 informational aggregate report: **89,327 words across 35 files** (validator output at Session 024 open, after Session 023 close). §2a advisory threshold is 90,000 words; activation is 100,000 OR >10% single-session growth. **Current aggregate is 673 words below advisory.**

Post-session aggregate depends on which §8 shape is chosen:

- A.1 compression: aggregate decreases by whatever MAD shrinks; default-read surface count unchanged (35 files).
- A.2 split: aggregate unchanged at default-read layer (both halves counted); file count 35 → 36.
- A.3 relocate-to-archive: aggregate decreases by whatever moves to archive; default-read file count unchanged or minor change; archive layer grows.
- A.4 carry-warning: aggregate unchanged (no content moved or deleted). Session 024's own 03-close.md adds a few thousand words at close; may cross advisory on its own if close is verbose.

### §3.3 Engine-version cadence context

Three engine-v bumps in three adjacent sessions:
- engine-v1 → engine-v2 (Session 021, D-082): OI-004 criterion-4 articulation (MAD v3→v4; validation-approach v3→v4).
- engine-v2 → engine-v3 (Session 022, D-084): read-contract.md v1 created; kernel v4→v5; workspace-structure v3→v4; validation-approach v4→v5.
- engine-v3 → engine-v4 (Session 023, D-086): read-contract.md v1→v2 (budget recalibration).

**Session 022 §5.4 Skeptic cadence minority activation warrant:** "three engine-v-bumps in four adjacent sessions OR external-application portability confusion." Satisfied at Session 023 engine-v4 adoption. §5.4 is now ACTIVATED. Per D-086 R9 escalation clause: any further engine-v-bump in Sessions 024/025/026 elevates §5.4 to substantive and forces a dedicated engine-manifest §5 revision deliberation in that session.

**OI-018 (Open, deferred, trigger-gated).** Activation if engine-v5 proposed before Session 026, OR external-application portability confusion, OR operator-directed. Scope per OI-018: revisit §5 bump-trigger criteria (bundle-trigger; threshold-trigger; major-vs-minor-substantive differentiation; cadence-aware bumping); possible §7-history-entry discipline strengthening; possible engine-v-compatibility metadata.

## §4 Current spec text excerpts (load-bearing for this deliberation)

### §4.1 `read-contract.md` v2 §8 remediation options (verbatim)

> Remediation when a default-read file exceeds the budget: reduce the file in place; or split the file into multiple default-read files (each under budget) with the original split-file designated archive-surface (its content preserved as an archive-pack); or relocate detail to archive-pack form with references from a thinner default-read replacement.
>
> Remediation must not summarise or silently compress; the archive-pack discipline preserves content verbatim.

### §4.2 `read-contract.md` v2 §5.1 Pacer 10K/7.5K minority (verbatim)

> Position: 10,000-word hard ceiling with 7.5K soft warning preserves calibration-corrective discipline while leaving growth headroom. Activation warrant: if the adopted 8K/6K budget produces three or more restructure-for-budget events in the next 5 sessions (restructures prompted by budget rather than by content completion), revisit upward toward 10K/7.5K. Alternatively, if 8K binds on `multi-agent-deliberation.md` or `reference-validation.md` in a way that forces content-coherence-damaging split, this position becomes preferred revision direction.

### §4.3 `read-contract.md` v2 §5.2 Skeptic no-change + warrant-literalism minority (verbatim)

> Position: the v1 Outsider-§5.3 activation warrant had not literally fired; revising values one session into a five-session grace window subverts the spec's own governance mechanism for self-revision. Vindication warrant: if within 5 sessions of Session 022 adoption (i.e., by Session 027) no default-read file exceeds 7,500 words and no restructure-for-budget event occurs, the Skeptic no-change position is vindicated retroactively — Session 023's revision was premature.

Note on §5.2 applicability here: MAD is 6,403 words — below the 7,500 trigger Skeptic's warrant names. A.4 (carry-the-warning) *preserves* §5.2's vindication runway. A.1/A.2/A.3 is a "restructure-for-budget event" that begins to consume §5.1's 3-event counter (5-session window Sessions 024-028).

### §4.4 `engine-manifest.md` §5 versioning discipline (verbatim excerpt)

> The engine version (engine-v1, engine-v2, ...) increments when any file in §3 changes in substance. "In substance" means:
> - A new engine-definition file is added to §3.
> - An existing engine-definition file receives a substantive revision (v-bump per the spec-revision discipline in workspace-structure.md).
> - An engine-definition file is removed or superseded.
>
> The engine version does **not** increment on:
> - Typo corrections or formatting adjustments.
> - Minor elaborations within an existing spec's scope (per the OI-002 substantive-vs-minor heuristic).
> - Updates to development-provenance or application-scope files.

### §4.5 OI-018 activation scope (relevant subset)

> **Whether engine-manifest §5 bump-trigger criteria are too permissive.** Current criteria: any substantive revision to any engine-definition file triggers a bump. Alternative criteria to consider:
> - Bundle-trigger: multiple substantive revisions within a session counted as one bump.
> - Threshold-trigger: bump required only when cumulative substantive changes pass a named threshold.
> - Differentiation: distinguish "major" (new spec files, kernel revisions, new required-fields) from "minor" substantive (budget-value tuning, constant updates, prose corrections with behavioral change).
> - Cadence-aware bumping: raise the bar for adjacent-session bumps; require exceptional justification.

### §4.6 WX-22-1 laundering-as-codification (Session 022 watchpoint, still active)

The concern: the read-contract mechanism could inadvertently codify the harness-layer routing-around-oversized-files pattern that OI-015 identified, by making archive-pack reference a normative mechanism rather than a repair. Any A.3 relocate-to-archive proposal must engage this: does moving detail to archive-pack *repair* the read-contract's intent (default-read means read-in-full) or *codify* the pattern of treating detail as routinely-not-read?

## §5 Survey of adjacent remediation traditions

Four approaches from practice worth naming as surveying input (per PROMPT.md anti-silent-import; introduced as surveying, not committed to any shape):

1. **Unix `man`-page layering.** Governance content at short top-level; detailed examples and edge cases in separate sections accessed by cross-reference. Analog: A.3 relocate detail to archive while keeping governance text default-read.
2. **Software spec families: RFC splitting by topic.** When an RFC grows too large, it is commonly split into multiple RFCs each addressing one coherent topic, with the original RFC either obsoleted or kept as meta-index. Analog: A.2 split by OI-004 scope.
3. **Legal code versioning.** Statutes are not edited for length; accumulation of amendments is normal; cross-referencing external regulatory detail is how length is managed. Analog: A.4 accept-as-routine if load-bearing content has accumulated legitimately.
4. **Kernel vs sysctl separation.** Core semantics in short kernel document; tunable parameters and edge-case handling in separate parameter-tuning documents. Analog: A.2 with the governance/parameter cut rather than OI-004/non-OI-004 cut.

None of these traditions is authoritative; each names a pattern this methodology could adopt, adapt, or reject.

## §6 Design questions (Q1–Q6)

### Q1. Which §8 remediation shape is right for MAD at 6,403 words?

Argue for one shape primarily (A.1 / A.2 / A.3 / A.4) or a hybrid with named components. State why the *content* warrants this shape (not just the budget). If A.2 or A.3, name the specific seam — which sections move where. If A.1, name the specific compression strategy and estimate the residual word count. If A.4, name the content-stability evidence and the conditions under which A.4 would convert to A.1/A.2/A.3 in a later session.

### Q2. Does the chosen shape constitute an engine-v-bump?

Apply the `engine-manifest.md` §5 criteria explicitly. If A.2 (new spec file) or A.3 (substantive revision to MAD), engine-v5 is the default reading. Argue for or against engine-v5 classification with reasoning that engages both §5 as currently written *and* OI-018's alternative criteria (bundle-trigger, threshold-trigger, major-vs-minor differentiation, cadence-aware bumping). If engine-v5 is proposed, §5.4 Session 022 cadence minority escalates — address this directly.

### Q3. How does the chosen shape interact with §5.1 Pacer and §5.2 Skeptic minorities in `read-contract.md` v2?

- §5.1 Pacer activation counts "restructure-for-budget events"; Session 024's action is the first data point in the 5-session window (Sessions 024–028). Is your chosen shape a *budget-driven* restructure or a *content-completion*-driven restructure? Name the evidence.
- §5.2 Skeptic vindication needs "no default-read file exceeds 7,500 words and no restructure-for-budget event occurs" by Session 027. MAD at 6,403 is below 7,500; A.4 preserves the §5.2 runway; A.1/A.2/A.3 ends it. Is ending §5.2's runway the right call *on the merits* rather than on budget pressure?

### Q4. If the chosen shape splits or relocates, how does it engage WX-22-1 laundering-as-codification?

If A.2 (split): are both files genuinely default-read (both read in full at every session open), or is the split an on-ramp to treating the secondary file as de facto archive? Concrete operator-discipline test: would Session 025 actually read both files at open, or only the "core" one?

If A.3 (relocate): is the archived material genuinely reference-accessed (the work of the deliberation is served by the default-read text; the archive is consulted only when the specific detail is needed), or is the archive the load-bearing content that readers will have to consult routinely? The read-contract's purpose is that default-read means *read-in-full*; archive access is by exception.

### Q5. What is the OI-004 criterion-3 and criterion-4 integrity impact?

The four OI-004-scoped sections in MAD (1,463 words, 23% of total) are the load-bearing surface for Criterion-4 Articulation, Acceptable Participant Kinds enumeration, and Closure Procedure. Any A.2 split placing these sections in a new file must preserve their cross-reference integrity with the rest of MAD (§Limitations + §Closure Criteria + §Heterogeneous-Participant Recording Schema fields) and with `validation-approach.md` v5 checks 16-19 + Q8. Any A.3 relocate-to-archive of these sections would make them archive-accessed rather than default-read — but these are the load-bearing predicates for validator checks that run in every session. Moving them to archive is likely wrong; the question is whether A.2 split preserves their default-read status correctly.

### Q6. What does the Session 024 close declare, and what watchpoints open?

Name the close's essential recorded surface: decision trigger declarations (d016_* / d023_*); engine-v classification; §5.4 engagement; §5.1 / §5.2 / WX-22-1 engagement; any new OI or watchpoint opened; synthesis-fidelity self-check; aggregate word count delta. Also name what a Session 025 audit would look for to judge whether Session 024 correctly honoured the §8 remediation discipline without drifting into budget-driven restructuring.

## §7 Role-specific stances (differ per perspective; rest of brief is byte-identical)

[Role-specific stance appears in each perspective's own file. Each perspective receives: §1–§6 (byte-identical), one §7.x stance (their own), and §8–§10 (byte-identical).]

## §8 Response format

For each Q1–Q6, one to three paragraphs with a clear **Position:** line and **Reasoning:** prose. Cite spec text and session history by file/line where applicable. Flag disagreement with the brief's framing explicitly rather than absorbing it. Preserve dissent from the other perspectives once you have seen none of them — reason from the brief and your own stance only. Target total length 1,500–3,500 words per perspective. Do not read other perspective files; do not look at synthesis drafts; do not commit or push. End with a **Honest Limits:** section naming what you didn't do, what you're uncertain about, and where your stance could be wrong.

## §9 Anti-import constraint

Per PROMPT.md and `multi-agent-deliberation.md` v4 §Stance Briefs item 6: reason primarily from the brief and your own stance. If you bring in concepts or examples from outside (pretraining, prior conversations, other projects), flag them as surveying-input with explicit attribution rather than committing them as within-process reasoning. The register-drift watchlist (per Session 013 WX-13-2) remains informal guidance.

## §10 Closure

Commit your perspective file verbatim when complete. No further action — the orchestrator handles synthesis, decision records, and spec revision. Honest limits preserved verbatim.

---

## Anchor commit

This brief is the deliberation anchor. After this commit, four perspective files will be launched in parallel (three Claude Opus 4.7 subagents + one OpenAI GPT-5.4 via `codex exec`), each receiving §1–§6 + their own §7 stance + §8–§10. No perspective sees another's output before committing its own.
