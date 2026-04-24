---
session: 045
title: Decisions — D-138 Scope A §B activation (NNN-session-assessment → NNN-session) minor amendment to workspace-structure.md v5 §provenance; D-139 Scope B OI-019 cross-linkage (§2c preserved; new long-horizon visibility signal feeds OI-019 sub-question f); D-140 §5.14 Folder-Name Reviewer preserve-D-094 first-class minority preservation (#31 engine-wide); D-141 housekeeping (D-129 second-of-3 + D-133 M2 first-of-3 verification exercises; WX-43-1 6-of-8 cumulative OI-promotion threshold met; WX-44-1 second occurrence; §5.6 GPT-concentration worst-case-side data point; engine-v7 preservation window count 9 new longest extended; fifteenth close-rotation)
date: 2026-04-24
status: decisions-complete
---

# Session 045 Decisions

Four decisions ratifying the §3 synthesis of `01-deliberation.md`. Numbering continues the engine-wide decision register (D-137 was at S044 close; D-138 opens this session).

## D-138: Scope A §B activation — `NNN-session-assessment` → `NNN-session` (minor amendment to workspace-structure.md v5 §provenance)

**Triggers met:** [d016_2]

**Triggers rationale:** D-138 produces a revision (minor per OI-002) to the engine-definition specification file `workspace-structure.md` §provenance folder-name discipline paragraph. The MAD v4 §Triggers d016_2 text covers revisions-triggering-deliberation without distinguishing substantive-vs-minor classification at trigger time. 3-of-4 cross-family including both non-Claude per `01-deliberation.md` §2 Q1 convergence; brief §8 threshold met (exceeds 3-of-4 threshold for substantive; comfortable at threshold for minor classification). `d016_3` does NOT fire at this specific decision: by synthesis time, 3-of-4 converged on one specific replacement (`NNN-session`), reducing plausible positions at decision time to two (adopt `NNN-session` / preserve per §5.14) not four. `d016_4` does NOT fire: no methodology-level engine-self-observability-failure pattern at this decision (pattern was detected at S027 Q6; S045 is a continued exercise of already-detected pattern, not a new detection event). `d023_*` structurally fires at session level (cross-family participation executed: 2 Claude + 2 Codex); scope A's minor classification means strict "substantive required" trigger is not the canonical fire, but voluntary-substantive-deliberation-rigor-for-minor-decision pattern is recorded as precedent for operator-surfaced-agenda treatment.

### Decision text

Activate S027 D-094 §B Minimalist minority. Amend `specifications/workspace-structure.md` v5 §provenance folder-name discipline paragraph to change the opening default from `NNN-session-assessment` to `NNN-session`. Forward-only from S046+; S001-S045 folder names preserved as historical witnesses per D-017 immutability. Spec frontmatter updated: `last-updated: 2026-04-24`; `updated-by-session: 045`. No v-bump on the spec (minor amendment per OI-002 heuristic); no supersession file created; no engine-v bump. 15th OI-002 data point (minor classification).

### OI-002 minor classification rationale

Per P1 (hypothetical), P2, P3, P4 all converge on minor: the amendment changes one string literal within an existing normative clause; does not introduce new file classes, top-level directories, close-step obligations, validator checks, or `read-contract.md` §1 enumeration changes. Precedent: S027 D-094 itself was classified minor as an amendment to the same paragraph (the Rationale "changing a string inside an existing normative clause, not adding a new clause" applies symmetrically to a subsequent string change). Subtle counter-argument acknowledged in P1 raw output: "directional reversal of a minor's normative content" could argue substantive; judgement is that minor is the better fit because the clause's SHAPE remains unchanged (one paragraph with default + permanence + historical-artefact-preservation clauses; only the default-title literal changes within that paragraph).

### Why `NNN-session` and not bare `NNN`

3-of-4 explicitly reject bare numeric on tooling-risk grounds: `tools/validate.sh` check 5 enforces `^[0-9]{3}-.+` pattern; bare `NNN` would require regex loosening and cross-spec edits to examples across `workspace-structure.md`, `read-contract.md`, `tools/validate.sh`, and `prompts/*.md`, escalating to substantive. `NNN-session` retains the `NNN-title/` shape (session is a valid title) and preserves one bit of type-information ("this is a session folder, not an issue folder or artefact folder"). P3 Outsider's tooling-check finding: bare `NNN` "would convert a small address-cleanup into a structure change." P4 Cross-Family Reviewer's retrofit-risk audit concurs.

### Why forward-only (no retroactive rename)

Operator R3 dropped Q2 (retroactive treatment) at session open per `00-assessment.md` §8 R3 ratification; D-017 immutability protects S001-S045 historical folder names; 4-of-4 convergence on forward-only adoption. S027 D-094 precedent rejected retroactive rename 2-of-3 (Archivist + Minimalist vs Discoverer dispensation-scoped retroactive).

### Rejected alternatives

1. **Preserve D-094 (P1 Claude-only 1-of-4 dissent position)**: preserved as §5.14 first-class minority per D-140 with three operational reopen warrants rather than prevailing. P1's argument: operator's language ("adds no value", "legacy") does not literally meet §B's "misleading a future reader" wording; change-in-circumstance (4 instances at S027 → 21 at S045) is weak for spec-revision against OI-007 scaling-restraint. 3-of-4 majority disagreed: P3 reframe (accumulation has produced interpretive pressure §B anticipated); P4 (operator's provenance-imprecision is itself evidence of misleading semantic work); P2 (threshold appears met on warrant-adjacent grounds).

2. **Bare `NNN` (choice ii in brief Q1)**: tooling-risk + substantive-escalation (P3, P4 flagged); 3-of-4 rejected (P2, P3, P4 all prefer `NNN-session` over bare `NNN`).

3. **§A Discoverer close-step rename forward (not candidate this session)**: S027 2-of-3 against stands; not re-proposed per §5a role-scoping.

4. **Retroactive rename**: dropped per operator R3; D-017 immutability; 4-of-4 convergence on forward-only.

5. **Add numeric sub-warrant to §B** (P1 Q7 forward observation): OI-007 scaling-restraint; not proposed at this session. Recorded as forward observation in `01-deliberation.md` §6 item 2.

## D-139: Scope B disposition — §2c preserved; OI-019 cross-linkage to sub-question (f)

**Triggers met:** [d009_1]

**Triggers rationale:** D-139 performs OI state management: `open-issues/OI-019.md` gains cross-linkage from this session's scope B deliberation (§Cross-linkage entry appended; §Session 043+ activation triggers entry appended for S045 scope B load-bearing new-class signal). Substantive augmentation of OI-019 content (not merely reference). `d009_1` is the canonical OI-management trigger (matches OI-019's own opening-decision trigger code at S043 D-130). No `d016_*` fires at this decision (no specification file is amended by D-139 per se — the spec edit is D-138 scope A). No `d023_*` fires at this decision level (no substantive engine-definition spec edit by D-139; scope B disposition is preserve-with-cross-link). `d004_3_minority_preservation` handled separately at D-140.

### Decision text

Preserve `specifications/read-contract.md` v4 §2c close-rotation at 6-session retention window unchanged. Record operator observation (deliberation-horizon-compression from 6-session retention) as load-bearing new-class signal in `open-issues/OI-019.md` §Session 043+ activation triggers + §Cross-linkage. OI-019 sub-question (f) "extended-baseline visibility mechanism periodic-vs-triggered-vs-narrow" is the forward design-space hook for future OI-019-led deliberation on tiered/diagnostic long-horizon mechanism. No specification file amendment this session. No engine-v bump.

### Why not §2c value revision (rejected alternatives 1-3)

4-of-4 cross-family convergence Q3(c) partially warranted: operator observation is load-bearing for a NEW mechanism (long-horizon visibility, cross-sectional read) distinct from §2c access-budget-control mechanism. §5.9 literal warrant (retention-exception frequency ≥2 per session for 7-10-session-back closes) has NOT fired — WX-28-1 16-of-16 zero-retention-exceptions is actively vindicated through S044. §5.10 opposite-direction 3-session minority also vindicated S034. Proposing window-value revision on non-literal grounds against actively-vindicated mechanism without resolving attribution ambiguity (P2 four competing attributions per `01-deliberation.md` §2 Q3: retention-length / engine-maturation / Path-A-default convention / watchpoint-only-by-design — none dominant) would launder the watchpoint discipline.

### Why cross-link to OI-019 rather than open new OI

OI-019 already carries sub-question (f) "extended-baseline visibility mechanism periodic-vs-triggered-vs-narrow" opened S043 per D-130. Opening a new OI for the same design space would duplicate. Cross-linkage preserves session-level provenance continuity — OI-019 accumulates cross-sectional / long-baseline / path-selection concerns as a unified design space per S043 Outsider reframe. S044 D-136 precedent: cross-linkage without bundling (not opening new OI for the same space).

### Why not tiered-mechanism invention this session

3-of-4 explicit warning against stealth-mechanism-design within a synthesis scoped as question-answering not design-space-exploration. P3 Outsider: "That should be synthesised with OI-019 rather than invented fully here." P4 Cross-Family Reviewer: "tiered mechanism must be tightly specified or it becomes stealth all-closes"; flagged specific laundering surfaces (retention-exception inflation; post-hoc exception for specific sessions; aggregate gaming via thin summaries). P2 Retention-Window Reviewer: "scope-B-proper deliberation would need to examine whether tiered mechanism adds value over SESSION-LOG.md's already-thin-index function." OI-019-led deliberation with appropriate design-space expansion + multi-perspective dedicated to the mechanism question is the better venue.

### Rejected alternatives

1. **Q3(a) + Q4(i) §5.9 literal 10-session activation**: 4-of-4 against literal non-activation (non-literal activation against vindicated watchpoint; P2 direct measurement +18K aggregate fits under 90K soft, but not the load-bearing remedy given attribution ambiguity).
2. **Q3(a) + Q4(ii-12) 12-session**: P2 direct measurement crosses 90K soft at 92K; laundering-risk per P4.
3. **Q3(a) + Q4(ii-15 or higher or all-closes)**: crosses §2b 100K hard (107K measured at 15; 128K at 20; 195K at all-closes); incompatible with §2b without paired revision; 4-of-4 rejection.
4. **Q3(a) + Q4(iv) tiered-mechanism invented this session**: 3-of-4 explicit against stealth-design; OI-019 is correct venue.
5. **Q3(b) preserve with forward observation only (no OI-019 cross-link)**: under-weights operator's epistemic access per P2 §3.4 argument; 4-of-4 implicit rejection in favor of cross-linkage.
6. **Open new OI for scope B**: duplicates OI-019 sub-question (f); S044 D-136 cross-linkage-not-bundling precedent.

## D-140: §5.14 Folder-Name Reviewer preserve-D-094 first-class minority preservation (#31 engine-wide)

**Triggers met:** [d004_3_minority_preservation]

**Triggers rationale:** D-140 preserves a substantive 1-of-4 cross-family dissent position as a first-class minority per MAD v4 §Minority Preservation discipline. The dissent is cited verbatim to P1 raw output; three operational reopen warrants are articulated below per minority-preservation schema. `d004_3_minority_preservation` is the canonical minority-preservation trigger. Dissent position is classified substantial enough to warrant first-class preservation (not orchestrator-absorbed): P1's rigorous S027-precedent-aware test of the §B activation warrant's literal wording against operator's observation's literal wording is a distinct contribution not reducible to the prevailing 3-of-4 synthesis.

### Decision text

Preserve P1 Folder-Name Reviewer's Q1 preserve-D-094 position as **§5.14 first-class minority** (#31 engine-wide) with three operational reopen warrants enumerated below.

Position (verbatim anchor from P1 raw output `01a-perspective-folder-name-reviewer.md` §Q1): "§B requires 'confusion caused' and 'misleading' — operator has reported mild redundancy and historical-origin awareness, not confusion or being misled." The §B activation warrant is worded in forward-looking misleadingness terms; operator's observation uses value-language not misleadingness-language; literal warrant-fire test is not met; change-in-circumstance from S027 close (4 instances → 21 instances; operator observation newly present) is weak for spec-revision against OI-007 scaling-restraint.

### Operational reopen warrants

**(a) Future operator re-surface with misleading-framing language within 6 sessions (S046-S051)**: if operator re-surfaces the scope-A observation using "misleading" / "confusing" / "misled-a-future-reader" wording (not "adds no value" / "legacy"), §B literal warrant fires retroactively at S045 and P1's preserve disposition is shown to have been correct in the literal-fire test. S052 close audit evaluates. If warrant (a) fires, the spec-edit at D-138 was premature per P1's literal-fire test — but the spec edit is not retroactively withdrawn; the §5.14 preservation is upgraded to retroactively-vindicated status.

**(b) Deliberation-reclassification pattern S046-S051**: if S046+ adoption of D-138 produces effects that reclassify scope A from minor to substantive at any subsequent session close audit (e.g., spec edits cascade beyond the one-paragraph default-change to `read-contract.md` examples, `tools/validate.sh` regex, `prompts/*.md` references, or similar), P1's preserve-under-OI-007-scaling-restraint concern is vindicated; adoption was premature per the OI-002 minor-classification argument. Evaluation: if any post-S045 session records OI-002 reclassification of D-138 from minor to substantive, §5.14 warrant (b) is vindicated.

**(c) Tooling-pressure indicating bare-NNN (or deeper) argument re-emerging**: if S046+ adoption produces pressure to loosen `NNN-title/` validator pattern (check 5 regex expansion beyond current `^[0-9]{3}-.+`) or to modify cross-spec literal references to `NNN-session-assessment` (examples in specs referring to the default-name literal), the `NNN-session` adoption is not the stable endpoint and bare-NNN (or deeper revision) is re-emerging. In that case §5.14's preserve-either-D-094-or-bare-NNN stability-case becomes re-examinable. Evaluation: any session that proposes regex-loosening or cross-spec literal-reference changes beyond the D-138 one-paragraph edit fires warrant (c).

### Status at S045 close

Preserved-not-activated (P1 dissent-position; D-138 prevailed 3-of-4). Observational data points begin S046; S052 close evaluates 6-session window (a); post-S045 sessions evaluate (b) and (c) on per-session basis.

### Rejected alternatives

1. **Not preserve (absorb into synthesis)**: MAD v4 §Minority Preservation mandates preservation of substantial dissent; 1-of-4 with rigorous cited reasoning qualifies.
2. **Preserve without reopen warrants**: weakens future-evaluability; all prior first-class minorities carry operational warrants per MAD v4 §Minority Preservation schema.
3. **Preserve under different warrants** (e.g., only warrant (a)): warrants (b) and (c) extracted from P1's own OI-002 classification subtlety + P1 Honest-limit 5 aggregate-budget quantification caveat (warrant (c) connects to tooling-pressure class that P3+P4 synthesis raised, echoing P1's own Honest-limit concerns about unverified tooling-pressure assumptions).
4. **Upgrade to 2-of-4 minority coalition (try to recruit P2 tentative-activation to reconsider)**: P2's position was clearly-tentative activate §B; coalescing P2 and P1 as joint dissent would misrepresent P2's actual position (P2 defers-to-P1-depth AND agrees with activation; only P1 clearly dissents).

## D-141: Housekeeping — verification windows, watchpoint advancements, forward observations, engine-v disposition, close-rotation, minority-count

**Triggers met:** [none]

**Triggers rationale:** Housekeeping record; no new normative content; no OI opened/resolved beyond D-139 cross-linkage; no specification edit beyond D-138. `[none]` classification per D-077/D-079/D-081/D-083/D-085/D-087/D-089/D-090/D-091/D-093/D-095/D-097/D-099/D-101/D-103/D-105/D-110/D-112/D-118/D-120/D-122/D-124/D-128/D-132/D-137 precedent chain (twenty-five `[none]` housekeeping records prior to S045; D-141 continues the pattern for housekeeping-only decisions).

### §D-141a D-129 convention verification (second-of-3)

**D-129 3-session verification window S044/S045/S046**: S045 **second-of-3 verification exercise**. `00-assessment.md` §5d surfaced three considered-and-rejected non-Path-A alternatives (Path L+A bundle-both-as-minor; Split-into-two-sessions; Path A defer) with non-vacuous rationales (not vacuous template). **Vindication-side data point this session.** S046 close evaluates the full 3-session window; S044 was first-of-3 vindication-side per S044 close §6; if S046 is vindication-side the convention graduates to standing discipline per D-129 text.

### §D-141b D-133 M2 Convene-time role/lineage matrix verification (first-of-3)

**D-133 M2 3-session verification window S045/S046/S047**: S045 **first-of-3 verification exercise**. Full 7-column matrix populated at `00-assessment.md` §5a (role / function / participant-kind / provider-model-family / MAD-v4-trigger / lineage-constraint / function-audit). Lineage-constraint compliance verified: Outsider seat filled by non-Claude per 21-for-21 convention (22 exercises post-operator-correction at S044; S045 is 23rd Outsider exercise with non-Claude in the seat). Synonym-drift guard: Cross-Family Reviewer function (laundering-audit + retrofit-risk-rating + evidence-stress-test) distinct from Outsider (frame-completion + reframe-seeking); no function drift observed (P3 did frame-completion "access-budget vs epistemic-horizon distinction" reframe; P4 did laundering-audit + evidence-stress-test + measurable-conditions; functions distinct). Departure discipline not triggered (no convene-time lineage-constraint violation). **Vindication-side data point this session.** S047 close evaluates full window.

### §D-141c WX-43-1 subagent-self-commit cumulative pattern — OI-promotion threshold met at S045 close

- S045 P1 (a043540) + P2 (86dfe06) both self-committed raw-output files during Claude-subagent Agent-tool runs.
- Cumulative across S043+S044+S045: **6 self-commits of 8 Claude-subagent opportunities = 75% self-commit rate** (S043: 2 of 4; S044: 2 of 2; S045: 2 of 2).
- Per S044 Observation 8: "OI-promotion candidate at S046 if cumulative n ≥ 6." **Threshold met at S045 close (n=6).**
- **S046 evaluation triggered**: is subagent-self-commit-inconsistency worth an OI? Observational pattern question: what varies across subagents (task framing? agent tool configuration? subagent model disposition?); is it load-bearing for provenance integrity? S046 Path decision should assess. No OI opened at S045 (Case Steward respects S044 D-136 precedent of not reflexively bundling-or-OI-ing cross-link-class observations without deliberation).

### §D-141d WX-44-1 second occurrence — P4 inadvertent cross-reads

P4 Cross-Family Reviewer disclosed in `01d-perspective-cross-family-reviewer.md` §Confidence-and-limits:
(i) initial brief extraction included §§5a-5c (other perspectives' stances);
(ii) broad `rg "retention-exception"` search exposed snippets of P3 `codex-outsider-raw-output.log` (command/output context around retention-exception searches).
P4 honest-limits statement: snippets were not relied on for positions.

Pattern: P4 role + codex-cli transport + broad filesystem-search convergence. **n=2 cumulative across S044 + S045** (S044: P4 120-line P3 log read; S045: P4 §5a-c + broad-rg P3 snippets).

Forward observation for S046+: Codex prompt files may benefit from explicit instruction to NOT use broad `rg` or broad file-tree searches during independent phase; use narrow per-file reads only. Not formalized as convention at S045; observational pattern. **S047 close OI-promotion candidate if n=3** (observational pattern recurs in any S046 deliberation).

### §D-141e §5.6 GPT-family-concentration data point

S045 is **worst-case-side** data point for §5.6 reopen-warrant (i): two Codex/GPT-5.5 perspectives + zero non-GPT non-Claude. Disclosed transparently at brief §0b; P4 self-scrutinized at §5d raw output.

Cumulative since S043 vindication-side event: S043 vindication-side (first-ever Gemini); S044 worst-case-side (per operator R2); S045 worst-case-side (per S044 standing preference). Mixed record.

Reopen-warrant (ii) literally discharged S043; spirit-level sustained-exercise question open for S046 re-examination. S046 Path decision should consider whether to re-engage Gemini (for minor scope) or wait for improved non-GPT non-Claude capability.

### §D-141f Engine-v disposition and preservation window

**Engine preserved at engine-v7**. Ninth non-bump session at engine-v7 — **engine-v7 preservation window count at S045 close: 9** (Sessions 037/038/039/040/041/042/043/044/045). **This extends the new-longest engine-v preservation window established at S042 (6), S043 (7), S044 (8), and now S045 (9).** First engine-v to reach preservation depth 9 for any substantive-content session class. Fourth substantive-content session at engine-v7 (S041 + S043 + S044 + S045).

§5.4 Session 022 engine-v-cadence minority (activated-not-escalated) does NOT re-escalate per content-driven-bump precedent chain (S028 D-096 / S033 D-107 / S036 D-114): S045 produces substantive content (scope A minor amendment + scope B preservation) but no engine-v bump; the cadence minority concerns bump frequency, not substantive-content frequency.

Engine-v7 operational friction at ninth post-adoption session: **zero at structural level**. Spec-edit discipline (D-138 minor amendment with frontmatter update), deliberation shape (MAD v4 four-perspective cross-family), OI cross-linkage (D-139 to OI-019), minority preservation (D-140 §5.14) all executed within engine-v7 discipline without friction. D-094 paragraph directly amended per D-138 ends its 18-session stability run (S028-S045 unrevised; longest minor-amendment stability run in engine history; recorded as OI-007 scaling-restraint data point).

### §D-141g Close-rotation mechanics

**Fifteenth close-rotation** steady-state at S045 close. S039 `03-close.md` rotates OUT of default-read surface (replaced by S045 `03-close.md`). S039-S044 retention window becomes S040-S045. Zero retention-exceptions recorded (WX-28-1 **17-of-17** cumulative; continuing vindicated pattern despite scope B operator observation on deliberation-horizon-compression — per D-139 rationale, operator observation is a distinct signal class from retention-exception frequency).

### §D-141h Active OI count and minority count at S045 close

- **Active OI count**: 13 (unchanged). OI-019 cross-linkage amendment (§Session 043+ activation triggers + §Cross-linkage) does not open new OI; does not resolve existing. Per D-139.
- **First-class minority count**: **30→31** (§5.14 NEW per D-140). All 30 prior minorities unchanged.
- **OI-002 data point count**: **14→15** (D-138 scope A 15th minor classification). Per D-138.

### §D-141i Forward observations

1. **Attribution-test experiment deferred** (P2 forward observation): one session with manually-expanded retention window to observe causality on deliberation-horizon-compression. Not proposed at S045; OI-019 (f) deliberation may find it useful.
2. **Scope A 21-instance point-of-departure**: 21 `NNN-session-assessment` folders at S045; S046+ use `NNN-session`; mixed-vintage condition continues under D-017 immutability.
3. **D-094 paragraph stability run**: 18 sessions (S028-S045 unrevised before D-138). Recorded as OI-007 scaling-restraint tracking data.
4. **Scope B attribution-unresolved**: OI-019 (f) deliberation venue; preserved as design uncertainty.
5. **§5.9 + §5.10 double-vindication tension**: if future scope B deliberation proposes window-expansion, §5.10 3-session vindication creates reconciliation burden. Forward observation.

## Summary

| # | Triggers met | Subject | Engine-v | Minority |
|---|---|---|---|---|
| D-138 | [d016_2] | Scope A §B activation NNN-session (minor) | v7 preserved | 1-of-4 P1 → §5.14 at D-140 |
| D-139 | [d009_1] | Scope B OI-019 cross-linkage (§2c preserved) | v7 preserved | none new |
| D-140 | [d004_3_minority_preservation] | §5.14 preserve-D-094 first-class minority (#31) | v7 preserved | 30→31 |
| D-141 | [none] | Housekeeping | v7 preserved; window 9 | no impact |

`[none]` housekeeping streak extended: D-141 continues the pattern (26th cumulative `[none]` housekeeping record post-adoption).
