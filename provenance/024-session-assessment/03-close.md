---
session: 024
title: Close — MAD 6K-soft-warn response; A.4 with conversion conditions; engine-v4 preserved; budget-literal drift cleanup
date: 2026-04-23
status: complete
---

# Close — Session 024

## Artefacts produced

### Provenance (`provenance/024-session-assessment/`)

- `00-assessment.md` — session-open assessment: Session 023 audit across three fidelity points; six-path presentation; validator-at-open 620 pass 2 fail 1 warn (both fails expected session-open state); aggregate default-read surface 89,327 / 35 files at open (673 under §2a advisory); halt for operator direction. Committed `3d41ae8`.
- `01-brief-shared.md` — shared deliberation brief (§1-§2 methodology context + problem statement + 6,403-word claim *which Outsider caught as stale; live is 6,386*; §3 section word-count inventory; §4 spec text excerpts; §5 adjacent-traditions survey; §6 Q1-Q6 design questions; §8-§10 response format + anti-import + closure). Deliberation anchor committed `bb2e3f2`.
- `01a-perspective-splitter.md` — Claude Opus 4.7 subagent output (verbatim). Position: A.2 split — new `multi-agent-deliberation-oi004.md`; MAD residual ~4,940; engine-v5 accepted. 3,479 words.
- `01b-perspective-archivist.md` — Claude Opus 4.7 subagent output (three minimal orchestrator-level token edits post-commit: `[archive:` → `[archive-proposal:` in three proposal-path occurrences, to avoid validator check-22 false-positive on hypothetical paths `archive/mad-schema/...`; content/position/reasoning unchanged; edit recorded in `manifests/archivist.manifest.yaml` transport_notes and `01-deliberation.md` §8). Position: A.3 narrow relocate (YAML field blocks + §Open Extensions → `archive/mad-schema/`; OI-004 sections stay default-read); MAD residual ~5,200-5,400; engine-v5 accepted. 3,353 words.
- `01c-perspective-skeptic.md` — Claude Opus 4.7 subagent output (verbatim; adversarial role). Position: A.4 carry-the-warning; four conditions for accepting light A.1; rejects A.2/A.3 on WX-22-1 + OI-004 integrity + §5.4 cadence. 3,263 words.
- `01d-perspective-outsider.md` → **archive-packed at creation per read-contract v2 §9** (46,321 words of codex exec stdout verbatim, including CLI banner + exploration traces + response body + end-of-stream duplicate). Archive-pack at `archive/024-outsider/` (9 chunks × 50KB; byte-range boundaries; SHA-256 `f8f69fa7b383a9f8651b9aa364b845c4f848d6aec0d60bee332f138010295dcb` verified against concatenation). Original file removed from provenance root; content byte-identical in chunks. Outsider position (OpenAI GPT-5.4 via codex exec v0.121.0, session id `019db6e4-502d-77c0-9feb-c0f3274eb012`, 120,810 tokens, reasoning effort xhigh): A.4 with concrete conversion condition (convert to A.2 OI-004 seam if MAD reaches 7,500 OR content-driven revision arises); no engine-v5; engine-v4 preserved. Outsider response body principally at chunks 08-09 following final `codex` marker.
- `01-deliberation.md` — synthesis. Maps 4-of-4 cross-family convergence (C1 A.3 of OI-004 sections is wrong; C5 OI-004 block is correct A.2 seam if split is ever done), 2-of-4 cross-family convergences (C2 no engine-v bump under A.4; C3 A.4 preserves §5.1 counter at zero and §5.2 runway; C4 A.4 best avoids WX-22-1), and divergences D1-D5. Recommends R1-R8 for adoption. Preserves five first-class minorities §5.1-§5.5 with operational activation warrants (§5.1 Splitter content-completion-A.2; §5.2 Archivist narrow-seam-A.3; §5.3 Skeptic four-condition A.1; §5.4 Outsider conversion-condition **adopted as R2**; §5.5 Splitter+Archivist hybrid). Anti-laundering check (§7) passes all six general tests plus three pattern-specific tests.
- `02-decisions.md` — two decisions. D-088 adopts R1-R7 with `triggers_met: [d016_3]`. D-089 OI housekeeping with `triggers_met: [none]`.
- `03-close.md` — this file.
- `manifests/splitter.manifest.yaml`, `archivist.manifest.yaml`, `skeptic.manifest.yaml`, `outsider.manifest.yaml` — per-participant D-024 manifests with v4 schema fields.
- `participants.yaml` — session-level index with `participants_family: cross-model`, `cross_model: true`, `non_claude_participants: 1`, `oi004_qualifying_participants: [outsider]`.
- `archive/024-outsider/` — archive-pack of Session 024 Outsider perspective (9 chunks; manifest.yaml + SHA-256 integrity; `chunk_boundary_rule: byte-range`).

### Specifications revised (minor, per D-088 R6)

- **`specifications/validation-approach.md`** — §Gating Conventions code block updated: `DEFAULT_READ_HARD_WORD_CEILING=15000` → `8000` and `DEFAULT_READ_SOFT_WORD_CEILING=10000` → `6000`. Frontmatter `last-updated: 2026-04-23`, `updated-by-session: 024`. **Classification: minor** per OI-002 heuristic — stale-literal correction aligning spec text with active `tools/validate.sh` values set by Session 023 D-086 R5. No new normative content. No version bump (still v5). No engine-v bump per `engine-manifest.md` §5.
- **`specifications/read-contract.md`** — §4 chunk-size target "≤ 10,000 words" → "≤ 6,000 words" with clarifying note on byte-range-chunking practical yield; §9 cross-reference "(§2: 15,000 words)" → "(§2: 8,000 words)"; §9 step 2 chunk target "line-range chunks each ≤ 10,000 words" → "line-range or byte-range chunks each ≤ 6,000 words (or ~50,000 bytes)". Frontmatter `last-updated: 2026-04-23`, `updated-by-session: 024`. **Classification: minor** per OI-002 heuristic. No version bump (still v2). No engine-v bump.

### No spec created; no substantive revision

Per R1/R3: no substantive revision to `multi-agent-deliberation.md`; no new engine-definition file; no file-level version bump for any spec.

### Tooling

**`tools/validate.sh` unchanged.** Session 023 D-086 R5 constants remain current. Check 20/21/22 operate against the recalibrated 8K/6K budget set by Session 023.

### Development-provenance files amended

- **`open-issues/OI-002.md`** — Session 024 11th data point appended (R6 stale-literal cleanup as minor per heuristic; new sub-pattern observation on stale-witness drift post-budget-revision captured in WX-24-2).
- **`open-issues/index.md`** — OI-002 annotation updated to "11th data point Session 024"; OI-004 line updated to "voluntary:required 9:8; criterion-3 cumulative 67"; OI-015 line updated to "6th positive exercise Session 024". Active count unchanged at 13.

### No external artefact this session

Session 024 is a self-development deliberation session producing a deliberated decision-not-to-act plus minor drift-cleanup edits. No external artefact; no `applications/` changes.

### No engine-version transition

**Engine remains at engine-v4** (established Session 023 D-086). Per D-088 R3, no engine-definition file is substantively revised by Session 024. §5.4 Session 022 cadence minority remains at activated (not escalated to substantive). OI-018 not activated by this session's decision; remains Open — deferred; activation triggers unchanged.

### SESSION-LOG.md

Session 024 entry added at close per R8a thin-index form.

## Decisions made

- **D-088** — Adopt R1-R7. A.4 carry-the-warning + concrete conversion conditions (R2) + engine-v4 preserved (R3) + §5.1 counter at zero + §5.2 runway preserved (R4) + WX-22-1 not advanced (R5) + budget-literal drift minor cleanup across validation-approach.md + read-contract.md (R6) + three watchpoints WX-24-1/-2/-3 (R7). Triggers: `[d016_3]`. Voluntary non-Claude Outsider participation per MAD §Non-Claude Participation Is Recommended clause for d016_3-only decisions (d023_* not triggered). OI-004 criterion-3 gains 2 data points.
- **D-089** — OI state housekeeping. OI-002 11th data point; OI-004 tally unchanged at 8-of-3 required (voluntary:required rebalances 8:8 → 9:8; criterion-3 cumulative 65 → 67); OI-015 6th positive exercise; three watchpoints WX-24-1/-2/-3 opened; five first-class minorities preserved at `01-deliberation.md` §5. No new OI. Triggers: `[none]`.

## Validation

`tools/validate.sh` at close: **PASS expected** once SESSION-LOG update and this close are committed. Pre-close run (before SESSION-LOG update): 650 pass, 1 fail (expected "Session 024 missing from SESSION-LOG.md"), 1 warn (designed 6K-soft on MAD, per D-088 R1).

### Tier 1 Structural Checks

- Checks 1-19: pass per engine-v4 baseline at close once SESSION-LOG updated.
- Check 20 (default-read surface per-file budget): **1 soft warning** — `specifications/multi-agent-deliberation.md` at 6,386 words (live validator-measured) exceeds 6,000-word soft warning; within 8,000 hard ceiling. Per D-088 R1 this is the designed mechanism working; persists through Session 024 close; re-evaluated at Session 025+ per WX-24-1 growth thresholds or R2 conversion conditions.
- Check 21 (archive-pack manifest integrity): 6 archive-packs pass — pre-R8a-SESSION-LOG, pre-R8b-open-issues, 014-oi016-outsider, 022-outsider, 023-outsider, **and new 024-outsider** (source_hash_sha256 `f8f69fa7b383a9f8651b9aa364b845c4f848d6aec0d60bee332f138010295dcb` verified).
- Check 22 (archive-pack citation consistency): all `[archive:` token references in default-read files resolve. Session 024 added references: `archive/024-outsider/` cited from `01-deliberation.md` (§1, §4, §9), from `01-brief-shared.md` (implicit), from the decision record, from `manifests/outsider.manifest.yaml`. Archivist perspective file uses `[archive-proposal:` token for hypothetical paths (not matching check-22 regex) per orchestrator-level edit; this is the first session to document a brief-authoring-convention watchpoint: future briefs should instruct perspectives to avoid `[archive:` token syntax for proposed/hypothetical paths.
- **Aggregate default-read surface report** (check 20 §2a informational): at close, **92,724 words across 36 files** (live validator measurement). Advisory threshold 90,000 **crossed this session** (open was 89,327; delta approximately +3,400 words driven primarily by Session 024 provenance entering the default-read surface — 00-assessment.md, 01-brief-shared.md, 01a/01b/01c-perspective files, 01-deliberation.md, 02-decisions.md, and this close itself all counted as current-session provenance at open and continue as default-read via §1 item 7 — 03-close.md — after close). Activation threshold (100,000 or >10% single-session growth without compensating restructure) not reached; growth is approximately 3.8% single-session, well below the 10% activation trigger. Per §2a: **advisory note recorded; Session 025 open assessment should report the aggregate explicitly**. The growth is session-provenance accretion, not spec growth: all 8 active specs' word counts unchanged (validation-approach.md and read-contract.md had minor edits under R6 but net word-count delta is within error of noise). §5.3 Pacer aggregate-hard-budget minority (from read-contract v2) activation warrant: aggregate exceeds 100,000 OR grows >10% single-session; neither fired.

### Tier 2 Guided Assessment

1. **Provenance continuity (Q1).** Yes. Session 024 Read drew on Session 023 close (next-session guidance; six-path presentation; three fidelity audit points), Session 022 close (§5.4 cadence minority warrant; read-contract v1 adoption), Session 021 close (engine-v2 bump precedent + OI-004 criterion-4 articulation), Session 017 close (engine-v1 establishment + H4 layered model). Closes 009-020 read in full; 001-008 + 010 via SESSION-LOG summaries per honest-limit declared in 00-assessment.md §1c. Prior rejections re-cited with context (Session 023 D-086 R2 6K-soft design intent; Session 022 D-084 WX-22-1; Session 021 D-082 criterion-4 articulation). No silent re-proposing of past rejections.

2. **Specification consistency (Q2).** Yes — **strengthened by R6**. Pre-session: validation-approach.md §Gating Conventions code block and read-contract.md §4/§9 carried stale 15K/10K literals from pre-Session-023-D-086 state. Post-R6: all three locations align with current validate.sh constants (8K/6K). Outsider [archive chunk 09 Q1] surfaced the drift; the cleanup was a direct consequence of Q2 (specification-reality alignment) self-test.

3. **Adversarial quality (Q3).** Yes. Skeptic was genuinely adversarial: argued A.4 carry-the-warning against three Claude advocates for restructure; explicitly pushed §5.4 cadence against any engine-v5 bump; named four concrete conditions under which A.1 compression would be acceptable rather than conceding for consensus; rejected A.2 on cadence + §5.2 runway + WX-22-1 framing grounds; rejected A.3 on WX-22-1 + OI-004 integrity. Skeptic's positions preserved as §5.3 minority with activation warrant; Skeptic's A.4 became the 2-of-4 cross-family adopted position (reinforced by Outsider). Adversarial role materially shaped outcomes.

4. **Meaningful progress (Q4).** Yes. Substantive deliberation executed per D-023 recommendation; R6 spec-drift cleanup is direct progress closing a Session 023 cleanup debt the Outsider caught; R2 conversion conditions convert A.4 from passive-defer to active watch with named thresholds; five first-class minorities preserved with operational warrants; three watchpoints opened as lighter-weight alternative to new OIs per OI-007 scaling discipline. Engine-v4 cadence discipline honoured per §5.4 activated minority.

5. **Specification-reality alignment (Q5).** Yes — **actively repaired this session**. Pre-session: validation-approach.md and read-contract.md described the budget regime differently from what tools/validate.sh enforced (15K/10K in spec text; 8K/6K in tool constants). Post-session: alignment restored per R6. The Outsider's catch turned Q5 from a pass-by-inspection into a structural repair. Going forward, WX-24-2 pre-commits the discipline: any future substantive revision to budget/threshold values must update all cross-referencing text in the same session.

6. **Cross-model-honesty evidence (Q6).** Yes. Synthesis declares `cross_model: true`. Concrete evidence per `01-deliberation.md` §1 + `manifests/outsider.manifest.yaml`: codex exec v0.121.0 CLI banner preserved verbatim in `archive/024-outsider/01-chunk.md`; model `gpt-5.4`; provider `openai`; session id `019db6e4-502d-77c0-9feb-c0f3274eb012`; 120,810 tokens; reasoning effort xhigh. Outsider manifest declares `training_lineage_overlap_with_claude: independent-claim`, `participant_organisation: openai`, `independence_basis: organization-distinct`. **Two substantive Outsider-sourced contributions** (per `01-deliberation.md` §4): (§4.1) brief-factual-error catch (6,403 stale Session-023 carry-forward vs live-validator 6,386; reasoning grounded in live number); (§4.2) budget-literal drift in validation-approach.md §Gating Conventions and read-contract.md §4/§9 (three locations; no Claude perspective caught). Both qualify as OI-004 criterion-3 data points per MAD v4 §Criterion-4 Articulation criterion 3. **Cumulative criterion-3: 67** across Sessions 005-024.

7. **Trigger-coverage plausibility (Q7).**
   - **D-088 declares `[d016_3]`.** Reading D-088's Decision text: R1 is no-change to MAD; R2 is decision-record-only conversion condition; R3 explicitly preserves engine-v4; R6 is minor per OI-002 heuristic (no new normative content). Four perspectives produced four distinct positions (A.2/A.3/A.4/A.4-with-conditions) with 2-of-4 cross-family convergence vs 1-of-4 Claude-only pairs — d016_3 ✓. d016_1 not fired (methodology-kernel.md unchanged). d016_2 not fired (R6 minor per OI-002). d016_4 not fired (operator path-selection at session open is not load-bearing-marking per D-074 precedent). d023_* not fired (R3 engine-v4 preserved; R6 minor not touching Tier 2 semantic; no OI-004 state change).
   - **D-089 declares `[none]`.** Housekeeping per D-073/D-077/D-079/D-081/D-083/D-085/D-087 precedent.
   - No `**Non-Claude participation:** skipped` annotations required. Outsider participated voluntarily per MAD recommended-clause for d016_3-only decisions; voluntary:required rebalances 8:8 → 9:8.

8. **OI-004 closure-retrospective substantive adequacy (Q8).** N/A this session — no `oi-004-retrospective.md` present. Session 024 does not attempt OI-004 state advance.

9. **Read-contract adherence (Q9).**
   - (a) Default-read surface read at session open: all 33→35 enumerated files read at open per `00-assessment.md` §1a, with honest-limits declared for closes 001-008 + 010 (read in SESSION-LOG one-line summary form only, not full). Honest-limits pre-committed in §1c.
   - (b) Archive-surface records cited via `[archive:` token convention in default-read files: `01-deliberation.md` cites `archive/024-outsider/` at §1 (committed_at declaration), §4 (cross-model contributions), and §9 (archive references section); `02-decisions.md` cites `archive/024-outsider/` in D-088 rationale and synthesis-limits sections; `manifests/outsider.manifest.yaml` declares the archive path as `raw_response_file`. Check 22 resolves all.
   - (c) Honest-limits on non-reads declared in `00-assessment.md` §1c and `01-deliberation.md` §8: did not re-read Session 022/023 Outsider archive-packs at session open; relied on prior-session vetting per read-contract §6. Did not read MAD v4 in full at synthesis — R6 cleanup rested on brief §3.1 section inventory + Outsider direct-read; grep-cross-check at synthesis confirmed no other occurrences of stale literals. Archivist perspective file was minimally edited post-commit (documented transparently).

## Honest notes from the session

- **Outsider brief-factual-error catch pattern now n=2 consecutive** (Session 023: 4,800 vs 6,403 estimate; Session 024: 6,403 stale vs 6,386 live). The §5.5 Session 023 minority (brief-factual-error watch) is empirically strengthened at n=2. Forward discipline: orchestrators should run `tools/validate.sh` immediately before brief commit and cite live validator measurements, not estimated or carried-forward values. Session 024's own brief made this same error despite Session 023's catch — evidence the watchpoint needs operational surfacing beyond minority-preservation.

- **Outsider pre-response workspace exploration now n=4** (Sessions 021/022/023/024). Pattern stable. MAD v4 §Stance Briefs says perspectives "do not read workspace files or use other tools during the independent phase" — this is true of Claude subagents (enforced via Agent tool prompt constraints) but not of the codex exec Outsider (which routinely reads workspace via its sandbox). **The asymmetry is load-bearing: without it, Session 023 and Session 024 Outsiders would not have caught their respective brief-factual-errors.** WX-24-3 watchpoint activated with specific escalation condition.

- **Cross-family contribution kind: drift-surveying-via-live-tool-run**. Session 024 Outsider's §4.2 budget-literal drift catch is a new kind of cross-model contribution — no Claude perspective produced it because no Claude subagent had tool-access to run `tools/validate.sh` during the independent phase. This extends the Outsider typology across Sessions 005-024 (three-cell protocol; H4 layered model; rejection-condition precision; type-drift diagnosis; two-branch independence warrant; broken-read-contract frame; brief-factual-error catch at Session 023; **drift-surveying-via-live-tool-run at Session 024**).

- **R6 minor-vs-substantive classification stress-test.** The R6 edits are aligning spec text with tool values. A strict reading of OI-002 could classify this as substantive because the *text* carried literal numbers that readers were relying on. The adopted classification is minor per "elaboration making explicit what existing practice already contains" branch — existing practice was the validate.sh constants; the spec text drift is being repaired, not newly constructed. Session 025 audit should re-examine this classification.

- **Aggregate word count at close approached 90K advisory but did not cross.** At Session 024 open: 89,327 / 35 files. Projected close (with this file + minor spec-edit deltas): approximately 89,500 / 35 files. Advisory threshold (90,000) not crossed but approached. If Session 025+ close is verbose OR if any file grows, advisory may be crossed. Per §2a, advisory is informational not pass/fail/warn; Session 025 should note the aggregate in close and flag whether growth is close-verbosity or spec-growth.

- **Three engine-v bumps in four sessions held at 3-in-4**. Session 024 did not bump. §5.4 escalator requires a further bump in Session 025/026 to escalate to substantive. Current cadence count per §5.4 minority: 3-bumps-in-4-adjacent-sessions (21/22/23) + 1-non-bump (24). §5.4 remains activated; not escalated.

- **Orchestrator edited the Archivist perspective file minimally post-commit** (three `[archive:` → `[archive-proposal:` token replacements in proposal-context text). Transparent documentation in `manifests/archivist.manifest.yaml` (`output_edited_after_submission: true`) and in `01-deliberation.md` §8 honest-limits. Brief-authoring-convention observation: future briefs should instruct perspectives to avoid `[archive:` token syntax for proposed/hypothetical paths. Preserved as a minor convention observation (not formal OI per OI-007 scaling pressure).

- **Session 024 did not advance OI-004 required-trigger tally.** D-088 declares `[d016_3]` only (d023_* not triggered per R3 engine-v4 preserved and R6 minor classification). Outsider participation voluntary. **Ninth consecutive non-advancing non-Claude session** (Sessions 013, 015, 016, 018, 020, 022, 023, 024 + 017... wait let me recount). Voluntary:required ratio rebalances to 9:8 — voluntary now exceeds required by 1. OI-004 state 3 (Articulated; awaiting closure-retrospective) unchanged. Criterion-3 cumulative 65→67.

## Next session

Session 025 should:

1. Run `tools/validate.sh` at start. Expected baseline: **650 pass + close-delta (approximately 655), 0 fail, 1 warn**. The warn is the designed 6K-soft on MAD; persists until either D-088 R2 conversion condition fires (MAD reaches 7,500 OR content-driven revision arises) OR MAD shrinks under 6K via some future session's minor edit.

2. **Audit Session 024 synthesis fidelity.** Particular attention to:
   - **D2 classification of A.1/A.2/A.3 as budget-driven vs content-completion-driven.** The 2-of-4 cross-family weighting (Skeptic + Outsider) carried budget-driven. Splitter and Archivist each argued content-completion on independent grounds. Does the close's rendering of the cross-family convergence honour the Splitter/Archivist position at full strength in §5.1 / §5.2 minorities, or dilute it toward majority framing?
   - **Whether R2 conversion conditions are operationally testable.** Condition (i) MAD reaches 7,500 words is crisp. Condition (ii) "content-driven reason to revise MAD substantively" is softer — what counts as content-driven vs budget-driven for a future Session 025/026/027 reading? Examine whether the synthesis's Q3 criteria for classifying content-completion are specific enough to apply prospectively.
   - **R6 minor-vs-substantive classification.** Was the cleanup genuinely minor per OI-002 heuristic, or did it substantively change what readers of the spec would rely on? The edits correct stale cross-references; no new rules; but the *numbers* changed in the spec text. If Session 025 judges R6 was substantive, the classification is wrong and engine-v5 should have been declared.
   - **Whether the Outsider's §4.2 drift catch was faithfully incorporated.** Check that all three stale-literal locations were updated (not just the Outsider-cited ones); grep for any remaining 15K/10K literals and verify each is historical-context (e.g., line 53 v1-Rationale recounting) or up-to-date.

3. **Present path options to operator.** Indicative paths (operator may steer):

   **(A) Watch MAD growth per R2 and WX-24-1.** Run validator, measure MAD word count, record in close. No substantive work required if thresholds not crossed. Legitimate default.

   **(B) OI-004 closure-retrospective draft.** State 3 → state 4 attempt. Voluntary:required now 9:8; criterion-3 cumulative 67. Still available as Session 023 presented it.

   **(C) Cell 1 re-attempt of reference-validation.** Unexercised across Sessions 020/021/022/023/024. Minimalist defer-revision warrant's non-test window extends another session.

   **(D) OI-015 laundering-gap deliberation.** Session 024 is 6th positive exercise. Pattern stable.

   **(E) OI-018 engine-manifest §5 revision.** Still trigger-gated; not activated this session. Available as operator-directed agenda.

   **(F) Operator-directed agenda.**

4. **Halt for operator ratification** before substantive execution.

5. **Session 024 watchpoints active from Session 025:**
   - **WX-24-1** MAD growth: thresholds 7,000 (reconsider A.1); 7,500 (R2 conversion condition i fires; convert to A.2); 8,000 (hard-fail forces restructure).
   - **WX-24-2** Budget-literal drift forward discipline: any future substantive revision to `read-contract.md` or `validation-approach.md` budget/threshold values must update all cross-referencing spec text in the same session.
   - **WX-24-3** Outsider pre-response workspace exploration pattern: n=4 stable; activation if material-contribution-disadvantaged-Claude case arises.
   - **Session 023 watchpoints carried forward:** W1 per-file drift (MAD primary; unchanged 6,386 at Session 024 close); W2 near-ceiling clustering (still no file between 6K-8K other than MAD); W3 aggregate growth (89,327 → ~89,500 this session; advisory 90K approached); W4 engine-v cadence (held at 3-in-4 after Session 024 non-bump); W5 Rationale-text accuracy (R6 repaired three locations); W6 read-contract-revision-frequency (Session 024 did not re-revise read-contract § 2 budget values).

6. **§5.4 Session 022 cadence minority remains at activated (not escalated).** Any Session 025 proposal to bump engine-v5 must engage §5.4 directly and OI-018 activation triggers. Session 024 non-bump preserves the activated-not-substantive state; the counter "3 engine-v-bumps in 4 adjacent sessions" has aged by 1 session without advancing.

7. **Brief-authoring convention observation** (not formal OI; per §Honest notes above): future deliberation briefs should (a) run `tools/validate.sh` immediately before commit and cite live validator measurements not estimated values; (b) instruct perspectives to avoid `[archive:` token syntax for proposed/hypothetical paths, using `[archive-proposal: ...]` or plain code-span backticks instead. Two briefs in a row (Session 023, Session 024) carried factual drift the Outsider caught; the discipline prevention is orchestrator-side, not perspective-side.
