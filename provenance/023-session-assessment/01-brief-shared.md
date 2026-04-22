---
session: 023
title: Shared Brief — Read-contract budget calibration
date: 2026-04-23
status: committed-as-deliberation-anchor
anchor_commit: TBD (committed before perspective launch)
---

# Shared Brief — Session 023

This brief is byte-identical across all four perspectives except for the §7 role-specific stance section. All perspectives receive §1 through §6, their own §7 stance, and §8 through §10. Brief-writing conventions per `specifications/multi-agent-deliberation.md` v4 §Stance Briefs.

## 1. Methodology context

You are participating in a deliberation for the Selvedge methodology's self-development application, Session 023. The methodology has been running for 22 closed sessions; this is the 12th multi-perspective deliberation to convene with non-Claude participation. The engine version loaded is `engine-v3` (adopted Session 022 per D-084).

The Selvedge engine is the current loadable implementation of the Selvedge methodology. Eight active specifications define the engine; the ones directly relevant to this deliberation are:
- `specifications/read-contract.md` v1 — defines the default-read surface and archive surface access discipline (the spec under revision in this session).
- `specifications/engine-manifest.md` — defines engine versioning and enumerates engine-definition files.
- `specifications/validation-approach.md` v5 — defines Tier 1 structural checks including check 20 which enforces the default-read budget.
- `tools/validate.sh` — holds the budget constants as variables.

Your job: reason independently from this brief toward a position on Q1–Q6 below, producing a raw output that the synthesis step will read alongside three other perspectives' outputs. Your output will be committed verbatim to the workspace. Preserve honesty about uncertainty; refuse the premise if you must; distinguish your substantive positions from the brief's framing.

## 2. Problem statement

Session 022 adopted `read-contract.md` v1 per D-084. §2 set a hard ceiling of **15,000 words** for default-read files and a soft warning at **10,000 words**. The §2 Rationale cited: *"The current single-Read-tool ceiling at the time of adoption is approximately 25,000 tokens (≈ 19,250 words at a 1.3× words-to-tokens approximation). A 15,000-word hard ceiling leaves headroom below the single-read ceiling."*

Session 022's own Honest Notes, written at close, flagged that the Rationale's 1.3× ratio was empirically wrong for workspace files:

> My brief §2.2 and operator §3 cite token counts (SESSION-LOG 33,227 tokens; open-issues 27,437 tokens). The new check 20 measures words not tokens. Word counts for the same files: SESSION-LOG 10,405 words; open-issues 9,783 words. Ratio ~3.0× tokens-per-word for these prose-with-markdown files, not the 1.3× my synthesis §2.3 D2 calculation assumed. The 15,000-word hard ceiling therefore translates to ~45,000 tokens in Read-tool terms (far above the 25,000-token single-Read ceiling), not the ~19,500 tokens I stated. This is the Outsider's §5.3 minority concern materialised — the 15K-word budget is more permissive than my synthesis assumed.

The Session 022 Outsider §5.3 minority position (preserved in `read-contract.md` §2 and in the Session 022 synthesis) argued:

> 8,000-word per-file budget is the conservative-preferable value; 15,000 may be permissive. Activation warrant: if any default-read file exceeds 10,000 words (soft warning) within 5 sessions of adoption without subsequent restructure, the 8,000-word ceiling becomes the preferred revision direction.

The Session 022 Outsider also proposed [archive: provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04, Q6]:

> My recommendation is 8,000 words per default-read file. I would also add an aggregate report, and likely a warning threshold, for the total development-provenance default-read surface. Per-file control alone is not sufficient if the default-read set keeps growing by accretion.

The operator ratified Path (C) from Session 022's close at Session 023 open: "Tighten read-contract §2 budget to 8,000 words per Outsider §5.3 minority." This deliberation determines the specific values, engine-version implications, and side-effects of that direction. Operator direction is ratification of path, not binding on values.

## 3. Current state facts

Validator run at Session 023 open: **574 pass, 0 fail, 0 warn**. Default-read surface currently measures 33 files. The five largest default-read files:

| File | Words | Fraction of 8K budget | Fraction of 15K budget |
|------|-------|-----------------------|------------------------|
| `specifications/multi-agent-deliberation.md` | 4,800 (est) | 60% | 32% |
| `specifications/validation-approach.md` | 4,647 | 58% | 31% |
| `provenance/021-oi004-criterion4-articulation/03-close.md` | 4,499 | 56% | 30% |
| `provenance/013-artefact-revision/03-close.md` | 4,454 | 56% | 30% |
| `provenance/022-workspace-scaling-trajectory/03-close.md` | 3,796 | 47% | 25% |

No file exceeds 5,000 words. The Outsider §5.3 activation warrant (any file exceeds 10K soft within 5 sessions) has not fired one session in.

Word-to-token empirical ratio for workspace prose: ~3.0× tokens-per-word (Session 022 Honest Notes).

Single-Read-tool ceiling at Session 023: ~25,000 tokens (unchanged since Session 022).

Derived budgets at 3.0× ratio:
- 8,000 words ≈ 24,000 tokens — within single-Read ceiling.
- 10,000 words ≈ 30,000 tokens — above single-Read ceiling (paginated Read required).
- 15,000 words ≈ 45,000 tokens — ~1.8× single-Read ceiling.

Engine-version history (engine-manifest.md §7):
- `engine-v1` established Session 017 (D-074).
- `engine-v2` established Session 021 (D-082 — OI-004 criterion-4 articulation; multi-agent-deliberation v3→v4; validation-approach v3→v4; validate.sh +checks 16-19).
- `engine-v3` established Session 022 (D-084 — new read-contract.md; methodology-kernel v4→v5; workspace-structure v3→v4; validation-approach v4→v5; validate.sh +checks 20-22).

If Session 023 adopts a substantive revision to `read-contract.md`, this would be `engine-v4` — **three engine-v-bumps in four sessions**.

Session 022 §5.4 Skeptic engine-version-cadence minority (preserved in `provenance/022-workspace-scaling-trajectory/01-deliberation.md` §5 per D-084):

> Activation warrant: three engine-v-bumps in four adjacent sessions OR external-application portability confusion.

## 4. Current spec text (verbatim excerpts)

`specifications/read-contract.md` §2 in full:

> ### 2. Default-read budget
>
> Per-file constraints:
>
> - **Hard ceiling: 15,000 words.** Any file in the §1 enumeration exceeding 15,000 words of body content (frontmatter excluded) is a validation failure at `tools/validate.sh` check 20. The session that produces such a file must either reduce it or restructure it (e.g., split into multiple files each under the ceiling; relocate detail to archive surface with reference from the default-read file).
> - **Soft warning: 10,000 words.** Any file in the §1 enumeration between 10,000 and 15,000 words triggers a validator warning (not a failure). The warning is signal that the file is approaching the ceiling; the next session should consider restructuring.
>
> Measurement: word count via `wc -w` on body content after the closing YAML frontmatter delimiter. The word-count metric is chosen for stability across tokenisers (per Session 022 Outsider [01d-Q6] + Conservator [01b-Q6] convergence).
>
> **Rationale for the chosen values.** The current single-Read-tool ceiling at the time of adoption is approximately 25,000 tokens (≈ 19,250 words at a 1.3× words-to-tokens approximation). A 15,000-word hard ceiling leaves headroom below the single-read ceiling. The 10,000-word soft warning provides early signal before files approach the hard ceiling.
>
> **Outsider minority position** (§5.3 of `provenance/022-workspace-scaling-trajectory/01-deliberation.md`): 8,000-word per-file budget is the conservative-preferable value; 15,000 may be permissive. Activation warrant: if any default-read file exceeds 10,000 words (soft warning) within 5 sessions of adoption without subsequent restructure, the 8,000-word ceiling becomes the preferred revision direction.

`tools/validate.sh` constants:

```
DEFAULT_READ_HARD_WORD_CEILING=15000
DEFAULT_READ_SOFT_WORD_CEILING=10000
READ_CONTRACT_ADOPTION_SESSION=22
```

`specifications/engine-manifest.md` §5 (versioning discipline):

> The engine version (`engine-v1`, `engine-v2`, ...) increments when any file in §3 changes in substance. "In substance" means:
>
> - A new engine-definition file is added to §3.
> - An existing engine-definition file receives a substantive revision (v-bump per the spec-revision discipline in `workspace-structure.md`).
> - An engine-definition file is removed or superseded.
>
> The engine version does not increment on:
> - Typo corrections or formatting adjustments.
> - Minor elaborations within an existing spec's scope (per the OI-002 substantive-vs-minor heuristic).
> - Updates to development-provenance or application-scope files.

`specifications/read-contract.md` §10 Versioning:

> **Substantive:** any change to the §1 enumeration, §2 budget values, §4 archive-pack structure, §5 manifest fields, §6 reference convention, or §7 integrity mechanism. Engine-version bump per `engine-manifest.md` §5.

The §10 text pre-declares that a §2 budget-value change is substantive. This determines v-bump classification mechanically; the deliberation may still challenge whether the classification is correct.

## 5. Survey

Three traditions bear on this problem without importing their conclusions:

1. **Working-set theory (computer architecture, Denning 1968).** A "working set" is the set of pages a process actively uses over a given time window. Working-set theorists distinguish per-page cost (how expensive it is to keep any one page in memory) from aggregate cost (the total cost of the working set). The Outsider §5.3(b) proposal maps to the aggregate side of this distinction.

2. **Document-design constraints in published style guides (e.g., NASA SP-7084, ISO/IEC technical writing standards).** These treat document-length ceilings as a reading-contract between author and reader. Ceilings are not absolute but are calibrated against the reader's expected single-read effort. A ceiling set 1.8× above the single-read effort is, by this discipline, not a ceiling but a soft suggestion.

3. **Budget-as-commitment discipline (procurement / government finance).** Budget values that are set substantially above actual consumption rate become ceremonial rather than binding; when consumption approaches the ceiling, the ceiling is typically revised upward rather than triggering restructure. This is the Outsider §5.3 concern materialised as an analogy: a 15K ceiling when largest file is 4,800 (32%) is well-clear of binding; a 8K ceiling when largest file is 4,800 (60%) binds meaningfully.

Do not import any conclusion from these traditions without flagging it explicitly per the anti-silent-import rule in §10.

## 6. Design questions

You are asked to reason about the following six questions. Your raw output should address each explicitly, in order. Distinguish cases where you take a strong position from cases where you note uncertainty.

### Q1. Hard ceiling value

What should the per-file hard ceiling be? Engage the empirical calibration data in §3 and the single-Read ceiling anchor. Options surveyed (you may propose others):
- 8,000 words (Outsider §5.3 position).
- 10,000 words (compromise; matches current soft warning).
- 12,000 words (modest tightening from 15K).
- 15,000 words (retain current; correct §2 Rationale text only).
- Other.

### Q2. Soft warning value

If the hard ceiling is changed, what should the soft warning be? Options surveyed (you may propose others):
- 6,000 words (75% of 8K hard).
- 5,000 words (63% of 8K hard; more headroom for early signal).
- Remove soft warning entirely (one clean value).
- Tie to a percentage formula rather than a fixed value.
- Other.

### Q3. Aggregate default-read surface budget

The Outsider §5.3(b) proposal at Session 022 was not adopted: "I would also add an aggregate report, and likely a warning threshold, for the total development-provenance default-read surface." Current aggregate is ~81,500 words across 33 default-read files. Session 022 did not adopt; Session 023 may revisit. Options:
- Adopt aggregate budget this session (name value and threshold).
- Do not adopt; add as watchpoint only.
- Reject; argue per-file budget is sufficient.
- Other.

### Q4. Engine-version classification

Read-contract §10 pre-declares §2 budget-value changes as substantive. Per engine-manifest §5, substantive revision to an engine-definition file triggers an engine-version bump. If Q1 adopts a value other than 15K, is this `engine-v4`, or is there a narrow interpretation that avoids the bump (e.g., "constant-tuning within an existing spec's scope" as a minor per OI-002)? Argue on the spec-revision discipline merits; do not argue on cadence-concern grounds (that is Q5's territory).

### Q5. Engine-version cadence (§5.4 minority response)

If Q4 adopts engine-v4, this is three engine-v-bumps in four sessions (engine-v2 Session 021; engine-v3 Session 022; engine-v4 Session 023). The Session 022 §5.4 Skeptic cadence minority activation warrant fires: "three engine-v-bumps in four adjacent sessions OR external-application portability confusion." How should the deliberation respond to the activated warrant?
- Treat as informational signal; proceed with engine-v4 on merits.
- Elevate to substantive concern; re-examine Q1/Q4 under cadence pressure.
- Revise engine-version-bump criteria in engine-manifest §5 to narrow the bump conditions.
- Other.

The §5.4 minority text should be engaged directly per the first-class-minority-preservation discipline.

### Q6. Watchpoints and minorities

What minorities should this deliberation preserve as first-class? What watchpoints should Session 024+ monitor? Name activation triggers concretely.

## 7. Role-specific stance — [YOUR ROLE HERE]

*(This section varies per perspective. Each perspective reads only their own §7 stance.)*

### 7.A — CALIBRATOR (adopts 8K or similar empirical-calibration-grounded value)

You are the Calibrator. Your stance: the read-contract §2 budget values should be revised to align with the empirically-measured tokens-per-word ratio for workspace files. The current 15K hard ceiling was set with an assumed 1.3× tokens-per-word ratio; the measured ratio is ~3.0×, making the current ceiling ~1.8× the single-Read tool limit rather than the under-limit headroom the §2 Rationale claimed. The Outsider §5.3 position (8K hard) produces a ceiling at ~24K tokens — within the single-Read limit, aligned with the original design intent. Your preferred adoption is substantively the 8K direction; within-session refinements (exactly 8K vs 7.5K vs 8.5K) are negotiable.

Engage in Q1: argue for 8K on calibration grounds specifically. Engage in Q2: argue for a soft warning that preserves early-signal function without false-alarming on the current largest files (4,800 words). Engage in Q3: you may support or decline the aggregate budget; argue the merits. Engage in Q4: argue that budget-value changes are substantive per §10's own pre-declaration and that v-bump is the honest classification. Engage in Q5: argue that cadence is a signal worth recording but not a reason to defer a calibration-corrective revision (the mechanism's honesty is served by revising when calibration is wrong, not delaying until the revision is politically convenient). Engage in Q6: name the minorities and watchpoints your direction would preserve.

Do not reach for consensus if consensus weakens calibration-fidelity. If you believe the Pacer or Skeptic positions are defensible, state why rather than dilute your own.

### 7.B — PACER (advocates measured tightening; middle value)

You are the Pacer. Your stance: the calibration concern in §2 is real but the Outsider's 8K proposal overcorrects. The current largest default-read file is 4,800 words (32% of 15K; 60% of 8K). An 8K ceiling binds on the largest files immediately with no headroom for short-term growth. A 10K hard ceiling preserves the spirit of the calibration correction (the §2 Rationale is wrong; the ceiling should reflect reality) while leaving growth headroom consistent with observed Session 001–022 trajectory. A further virtue: 10K-hard is the current soft-warning value, so the transition is psychologically continuous for readers who internalised the current values.

Engage in Q1: argue for 10K on preserve-headroom grounds. Engage in Q2: propose a soft warning matched to your Q1 answer. Engage in Q3: you may support the aggregate budget; argue it is the more impactful lever than per-file budget given actual growth patterns. Engage in Q4: argue that your proposed change is substantive but less so than 8K; still v-bump territory. Engage in Q5: engage the cadence concern seriously; your middle value may reduce the reason to bump frequently in subsequent sessions (a wider ceiling means fewer calibration-corrective revisions). Engage in Q6: preserve both tighter and looser minorities with warrants.

Do not reach for consensus if consensus ignores the observed-growth data. If you believe the Calibrator or Skeptic positions are defensible, state why.

### 7.C — SKEPTIC (adversarial; advocates defer or narrow-correction only)

You are the Skeptic. Your stance: the operator-ratified path ratifies the direction, not the values; the values should reflect the mechanism's own activation discipline. Read-contract §2 declares an explicit Outsider §5.3 activation warrant: "if any default-read file exceeds 10,000 words (soft warning) within 5 sessions of adoption without subsequent restructure, the 8,000-word ceiling becomes the preferred revision direction." The warrant has not fired — no default-read file is above 5K. Revising the budget in Session 023 pre-empts the very mechanism the spec established to govern when revision is warranted.

You have a second critique: three engine-v-bumps in four sessions is cadence-churn. Each bump increases external-application-portability risk (an external application pinned to engine-v2 versus engine-v4 will have materially different read-contract rules). The §5.4 Skeptic minority at Session 022 named this; the warrant activation at Session 023 is precisely the signal worth taking seriously, not dismissing.

Engage in Q1: argue for **no change to budget values** this session; propose only a narrow correction to the §2 Rationale prose paragraph (clarify the actual tokens-per-word ratio; preserve the 15K/10K values). This is a minor correction per OI-002, not substantive, no v-bump, no cadence activation. Engage in Q2: declines to propose a new value; the existing 10K soft stands. Engage in Q3: argue defer until per-file budget actually binds (the aggregate proposal is even more premature). Engage in Q4: argue that clarifying prose is minor per OI-002; no engine-bump. Engage in Q5: argue that the §5.4 warrant activation is itself load-bearing evidence that the bump-trigger criteria are too permissive, and propose revisiting engine-manifest §5's trigger definition in a future session (not this one). Engage in Q6: name the preserve-at-minority and watchpoint structure that would honestly record the Calibrator and Pacer positions while declining their adoption.

Your job is adversarial. Do not concede to majority pressure if your argument stands. Do not advocate the operator's ratified path if your reading is that the path is premature; preserve your dissent with falsifiability conditions.

### 7.D — OUTSIDER (non-Claude; non-Anthropic model family)

You are the Outsider, a non-Anthropic model participating via `codex exec`. Your training lineage is independent of Claude's. Your presence is voluntary for this session per multi-agent-deliberation.md v4 §When Non-Claude Participation Is Required clause 2 (this deliberation substantively revises read-contract.md, which is not in D-023's enumerated list, so non-Claude participation is recommended but not required; your inclusion is voluntary per Sessions 007/008/010/012/013/020/022 precedent).

At Session 022, an Outsider (same model family) produced the §5.3 minority position (8K word per-file budget + aggregate budget proposal) preserved in read-contract.md §2 and in the Session 022 synthesis. Your current stance is not bound to that prior position; reason fresh from this brief's §2 / §3 / §4 / §5 / §6 content.

Engage in Q1: produce your own considered answer. The prior Outsider's 8K position is preserved verbatim in §2 of the brief; you may adopt, refine, or argue against it. Engage in Q2–Q6 per your independent reading. If you find the Pacer 10K or Skeptic defer positions more defensible, adopt them. If you find a position none of the Claude stances anticipates, propose it. Your value to the deliberation is the possibility that your training-distribution-difference produces a contribution Claude perspectives cannot generate (this possibility is open every session; whether it materialises depends on your reading here, not on your prior).

You may consult workspace files if your tooling supports read access; if you do, preserve the Session 021/022 honest-limit pattern of declaring which files you read and what you relied on. You may not import conclusions from outside the workspace without flagging them per §10.

Engage in all six questions. Produce a Meta-note at the end on what you believe your strongest divergence from likely Claude-majority positions is, if any.

## 8. Response format

- Address Q1 through Q6 in order, each with its own `## Q1.` / `## Q2.` etc. heading.
- Target length: 1,500–3,500 words total. Shorter is acceptable if your position is direct; longer is acceptable if you need to preserve reasoning. Do not pad.
- Cite spec text by spec name and section (e.g., `read-contract.md §2`) and session provenance by path + question number where applicable (e.g., `[Session 022 01c-Q9]`). Use the `[archive: path]` convention for archive-surface citations.
- Close with a `## Honest Limits` section naming: what you did not read; what you are uncertain about; where your position rests on assumptions rather than evidence.
- For the Outsider (§7.D only): close with `## Meta-note` in addition to Honest Limits, naming what you expect your strongest cross-model divergence to be.

## 9. Constraint on external imports

Per `PROMPT.md` rule: do not import ideas from outside the process. Reason primarily from this brief's content and the spec text it cites. If a pretrained pattern or analogy arrives (from working-set theory, document-design practice, budget discipline, or anywhere else), flag it as an external input, attribute it, and frame it as hypothesis rather than commit. The §5 survey is the designated on-ramp for pretrained content; use it.

## 10. Closure

Your output will be committed verbatim to `provenance/023-session-assessment/01X-perspective-<role>.md` where `X` is `a/b/c/d` by role order. You will not see the other perspectives' outputs; synthesis operates on all four raw outputs after all are returned. Dissent is preserved; minority positions become first-class record; your honest position is more valuable than consensus.

When ready, produce your raw output.
