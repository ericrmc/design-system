---
session: 045
title: Perspective 3 — Outsider (Codex/GPT-5.5; frame-completion; access-budget-vs-epistemic-horizon reframe at Q3; §B activation narrow reader-confusion ground)
perspective: Outsider
perspective_index: 3
lineage: gpt
date: 2026-04-24
status: raw-output-committed
---

# Perspective 3: Outsider

**Identity line:** Outsider; non-Claude participant via Codex/GPT; model `gpt-5.5`; token count not available during response generation.

**Independence attestation:** I did not read other perspectives' raw outputs. I did not read `01a-*`, `01b-*`, or `01d-*` files. I listed filenames in `provenance/045-session-assessment/` and saw `codex-reviewer-raw-output.log`, but did not open or search its contents. I read only my own `codex-outsider-raw-output.log` for the `model:` line.

## Reading performed

- `provenance/045-session-assessment/01-brief-shared.md`: §0, §0b, §1–§4, §5c, §6–§9. I avoided §5a, §5b, §5d.
- `provenance/045-session-assessment/00-assessment.md`: §1–§5.
- `specifications/read-contract.md`: §1, §2, §2a, §2b, §2c, §3, §5–§6 excerpts.
- `specifications/workspace-structure.md`: top-level structure, §provenance, validation.
- `specifications/engine-manifest.md`: §1–§3, §7.
- `provenance/027-session-assessment/03-close.md`: §1b, §2, §4c.
- `SESSION-LOG.md`: S021–S044 rows, with emphasis S023 onward.
- Current default-read close files S039–S044: targeted retention/aggregate/path excerpts and word counts, not full rereads.
- `tools/validate.sh`: constants, provenance naming check, close-retention default-read selection, current-session detection.
- `open-issues/OI-019.md`: full file, because scope B points directly at its long-baseline visibility problem.
- `git log --all --grep='retention-exception' --oneline` and `rg "Retention-exception:" provenance/*/02-decisions.md`; the latter found no retention-exception decisions.

## Q1 (scope A: folder-name §B activation)

Yes: activate S027 D-094 §B, but on the narrow ground of reader-confusion, not on "legacy" alone.

My reframe is that scope A is not really "remove a legacy phrase"; it is an address-semantics problem. The folder name is doing two possible jobs: a stable machine/human address, and a semantic title. D-094 deliberately moved semantic title work to `SESSION-LOG.md` and made the folder name a permanent container address. That choice remains sound. The problem is that `session-assessment` still looks semantic while being semantically stale. It mislabels sessions that are not merely assessments: S041 OI-004 closure, S043 Path PSD, S044 Path OC, and S045 Path OS are all broader than "assessment".

The tooling supports the narrow change. `tools/validate.sh` check 5 only requires `^[0-9]{3}-.+`; check 20 extracts the numeric prefix for close rotation; nothing I saw depends on the literal string `session-assessment`. Bare `NNN` would fail the current `NNN-title` pattern and would require broader validation/spec changes. That would convert a small address-cleanup into a structure change.

Recommendation: change the S046+ opening default to `NNN-session`, preserve all historical folders unchanged under D-017, and do not revive close-step renaming. Classify as minor per OI-002, matching D-094's own classification: same directory class, same `NNN-title/` pattern, no new top-level structure, no new validator check, no new close obligation.

## Q3 (scope B: revision load-bearing?)

Partially warranted. Operator's observation is load-bearing, but I would not treat it as direct evidence that `6` is the wrong full-close count.

The reframe is: §2c controls the access budget; it does not by itself guarantee a long deliberation horizon. WX-28-1 and the zero retention-exception record show that the citation-driven exception mechanism has not been needed. They do not show that the engine is preserving long-baseline awareness. Those are different measurements.

The strongest evidence is that S043's Long-Baseline Auditor had to quantify a distributional pattern: post-engine-v4 Path-A concentration at 47% versus 0% pre-S024. That is not the kind of pattern a six-close recent-memory window is designed to surface. OI-019 already names the adjacent missing mechanism: extended-baseline visibility and warrant-surface diversity.

So my answer is Q3(c): operator's observation warrants change, but the likely target is a new cross-sectional read/diagnostic mechanism, not simply changing §2c from 6 to another number.

## Q4 (scope B: window value — conditional on Q3)

Ranked preference:

1. **(iv) Tiered mechanism.** Keep the last 6 full closes as working memory, and add a thin long-baseline layer or triggered diagnostic. The layer should read across `SESSION-LOG.md` and, when needed, selected older close headings/decision summaries by explicit citation. It should be diagnostic, not automatically work-generating, to avoid laundering OI-019 into a permanent work factory.
2. **(i) 10-session full window** as fallback only. It is budget-comfortable and tracks the preserved §5.9 direction, but §5.9's literal activation warrant did not fire. Adopting 10 because of horizon-compression should be described as a new rationale, not as literal §5.9 activation.
3. **15 sessions** only with a paired aggregate-monitoring rationale; it crosses the soft budget in the brief's estimate.
4. **20 sessions or all closes:** reject under current §2b. These exceed or overwhelm the hard budget and undo D-096's core aggregate-control function.

If codified in `read-contract.md`, the tiered mechanism is substantive and should be treated as an engine-v8 candidate. If adopted first as an OI-019-linked convention pending verification, it can be minor-convention-first, but then it should not be represented as a completed §2c fix.

## Q5 (scope B: aggregate-budget interaction)

At S045 open, aggregate is 64,615 words / 19 files. The current six close files total about 22.8K words by `wc -w`, roughly consistent with the brief's 2.5K–4K per-close estimate.

My preferred tiered option has low aggregate impact if it uses existing `SESSION-LOG.md` plus explicit older-close citation. If it creates a thin long-baseline index, that index should be capped tightly, probably under 1–2K words, and remain diagnostic.

The full-window alternatives behave as the brief models them: 10 sessions lands around 79K, safely below the 90K soft warning; 15 lands around 92K, crossing soft warning; 20 lands around 107K, crossing hard failure; all closes is incompatible without rewriting the aggregate budget regime. This is why I would not solve a horizon problem by restoring large full-close retention.

## Q6 (cross-scope: bundle or separate)

Separate decisions, same session.

Scope A is a minor `workspace-structure.md` address-default amendment. Scope B is either a substantive `read-contract.md`/engine-v8 change or a convention/diagnostic deferred into OI-019. Bundling them into one decision would blur classification. If scope B becomes engine-v8, the manifest can record both session changes in the version history, but the decision records should keep the minor folder-default change distinct from the substantive read-surface mechanism.

## Q7 (forward observations + honest limits)

Forward observations:

- Scope A should be recorded as "address semantics clarified", not "legacy cleanup". The engine should keep resisting close-step rename pressure unless S027 §A separately fires.
- Scope B should be cross-linked to OI-019. This session is fresh evidence that long-baseline visibility is a live problem, but it is not evidence that all older closes need to be default-read.
- WX-28-1 should not be over-read. Zero retention exceptions can coexist with horizon compression.
- If a tiered long-baseline diagnostic is adopted, it needs an anti-laundering guard: diagnostic visibility alone does not authorize substantive work without a separate warrant.
- §5.6 GPT-family concentration remains a real limitation this session: both non-Claude seats are Codex/GPT-5.5, so the record is cross-family but not non-GPT-non-Claude.

Honest limits:

- I did not read S028 raw deliberation or archive chunks; I relied on `read-contract.md`, `engine-manifest.md`, and `SESSION-LOG.md` for D-096 and §5.9/§5.10 history.
- I did not full-read every S039–S044 close; I read targeted excerpts and word counts relevant to retention, aggregate, and path history.
- I did not inspect other current perspectives' outputs. I did see current-session raw-output filenames from `rg --files`; no contents were read.

## Independent claim

This perspective separates two things the current framing risks merging: access-budget control and epistemic-horizon control. Scope A should reduce false semantic load in the address; scope B should add long-baseline visibility without undoing the aggregate discipline that close-rotation was built to protect.

## Confidence and limits

I am confident in the narrow §B activation for `NNN-session`, the minor classification for scope A, and the rejection of bare `NNN` under current `NNN-title` validation. I am also confident that scope B is not answered cleanly by retention-exception frequency: the observed problem is cross-sectional and long-baseline.

I am less confident in the exact tiered mechanism shape. That should be synthesised with OI-019 rather than invented fully here. No inadvertent content cross-read occurred; only filenames of current-session raw logs were seen.

MODEL_VERSION: gpt-5.5
