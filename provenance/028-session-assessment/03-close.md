---
session: 028
title: Close — §5.3 Pacer aggregate-hard-budget minority converted; read-contract.md v3; close-rotation rule adopted; engine-v4 → engine-v5; six new first-class minorities preserved
date: 2026-04-23
status: complete
---

# Close — Session 028

## §1 Artefacts produced

### §1a Provenance (`provenance/028-session-assessment/`)

- `00-assessment.md` — session-open assessment; default-read surface read; Path G selected per operator default-path directive; trigger analysis; determination of 4-perspective cross-family deliberation (3 Claude + 1 Outsider voluntary).
- `01-brief-shared.md` — shared deliberation brief; byte-identical §§1–3, §5–§6 across all four perspectives per MAD v4 §Brief immutability. Committed at commit `d0d81e4` before any perspective launched.
- `01a-perspective-pacer-advocate.md` — Pacer-advocate raw response (~3,900 words). Position: adopt §5.3 at revised values 95K hard / 85K soft; close-rotation + prompt-guidance + migration; engine-v5 minimal cadence engagement.
- `01b-perspective-skeptic-preserver.md` — Skeptic-preserver raw response (~3,800 words, adversarial role). Position: continue preservation; softer-intervention first; defer conversion to Session 029+ pending evidence.
- `01c-perspective-synthesiser-integrator.md` — Synthesiser-integrator raw response (~4,400 words). Position: partial adoption with revision at 110K soft / 120K hard; pair aggregate budget with close-rotation at 10-session window; engine-v5 clean bump.
- `01d-perspective-outsider.md` — Outsider raw response (OpenAI GPT-5 via codex exec; ~2,100 words). Position: adopt at 100K hard / 90K soft (§2a thresholds as budget values); close-rotation first at 6-session window; "laundering the activation" critique against above-current values; engine-v5 separate from OI-018 cadence.
- `01-deliberation.md` — synthesis (~5,000 words). Cross-family convergences identified (4-of-4 on orthogonal per-file interaction; 3-of-4 on adoption-with-revision; 4-of-4 on close-rotation as primary remediation; 3-of-4 on keep §5.4 separate). Values divergence acknowledged (85K/95K Pacer; 100K/90K Outsider; 110K/120K Synthesiser). Outsider's "laundering" critique adopted as disambiguating signal. Six first-class minorities preserved with activation warrants.
- `02-decisions.md` — D-096 (substantive revision adopting §5.3 at 100K/90K; close-rotation at 6-session window; read-contract.md v2 → v3; engine-v4 → engine-v5; six new first-class minorities preserved); D-097 (OI housekeeping; OI-004 tally update; watchpoint WX-28-1 opened).
- `participants.yaml` — session-level index. Four perspectives; `participants_family: cross-model`; `cross_model: true`; `non_claude_participants: 1`; `oi004_qualifying_participants: [Outsider]`.
- `manifests/pacer-advocate.manifest.yaml`, `skeptic-preserver.manifest.yaml`, `synthesiser-integrator.manifest.yaml`, `outsider.manifest.yaml` — Layer 2 per-participant manifests per MAD v4 §Heterogeneous-Participant Recording Schema. Outsider manifest carries all v4 criterion-4 fields (`participant_organisation: openai`; `claude_output_in_training: known-no`; `training_lineage_evidence_pointer`; `independence_basis: organization-distinct`).
- `03-close.md` — this file.

No `STATUS.md` (no awaited non-Claude response; Outsider responded synchronously). No `human-review.md` (no reviewer-shape participant). No `archive/` subdirectory (no current-session raw exceeds 8,000-word hard ceiling; largest is Synthesiser-integrator at ~4,400 body words; Outsider at ~2,100 body words well under threshold).

### §1b Specification change — `read-contract.md` v2 → v3 (substantive)

Per D-096. Changes:

- **Frontmatter**: `version: 2 → 3`; `last-updated: 2026-04-23`; `updated-by-session: 028`; `supersedes: read-contract-v2.md`.
- **§1 item 7 revised**: from "Every `provenance/NNN-title/03-close.md` across all closed sessions" to "The `03-close.md` file of each of the **most recent 6 session closes**"; older closes become archive-surface by exclusion per §3.
- **§1 item 8 minor clarification**: current-session provenance default-read scope during session; at close, becomes archive-surface unless it is a `03-close.md` within the §7 retention window.
- **§1 retention-exception (new)**: a session may record a retention-exception decision to keep a specific older close in default-read for load-bearing governance purposes.
- **§2a role clarified**: sensor layer providing informational advisory/activation notes; at engine-v5 supplemented by §2b budget enforcement layer.
- **§2b (new)**: Aggregate hard budget. Hard ceiling 100,000 words; soft warning 90,000 words. Pass/fail/warn enforcement via validator check 20. Rationale documents matching-§2a-thresholds design decision (avoids "moving the trigger after it fired" per Outsider cross-family critique). Six new first-class minorities §5.6–§5.11 preserved with activation warrants. §5.3 original-minority text preserved verbatim in §2b archive block.
- **§2c (new)**: Close-rotation rule. Most recent 6 sessions' closes in default-read; older closes archive-surface by exclusion. Rotation mechanics; no physical file movement (files remain at `provenance/NNN-title/03-close.md`); citation convention for rotated closes; retention-exception mechanism.
- **§10 versioning**: v3 entry added. WX-28-1 watchpoint (close-rotation-exception-frequency) recorded.

v2 preserved as `specifications/read-contract-v2.md` with `status: superseded`, `superseded-by: read-contract.md (v3)`, `superseded-at-session: 028`.

Body word count after revision: ~4,050 words. Well within per-file budget (under 6K soft; under 8K hard).

### §1c Specification change — `engine-manifest.md` documentary update

Per D-096 engine-v bump. Changes:

- **§2**: `engine-v4` → `engine-v5`.
- **§3 heading**: "Engine-definition files at `engine-v4`" → "Engine-definition files at `engine-v5`" (file set unchanged; no files added or removed).
- **§7**: engine-v4 history entry extended with Sessions 024–027 preservation note and §5.3 activation at Session 027; engine-v5 history entry added documenting Session 028 D-096 substantive content.
- **Frontmatter**: `last-updated: 2026-04-23`; `updated-by-session: 028`. engine-manifest.md's own version remains at v1 per Session 021/023 sub-pattern (documentary updates to the tracking spec do not bump the tracking spec's own version).

### §1d Tooling update — `tools/validate.sh` substantive

Per D-096. Changes:

- **New constants**: `AGGREGATE_BUDGET_ADOPTION_SESSION=28`; `DEFAULT_READ_AGGREGATE_HARD=100000`; `DEFAULT_READ_AGGREGATE_SOFT=90000`; `DEFAULT_READ_CLOSE_RETENTION_WINDOW=6`.
- **Existing constants retained**: `DEFAULT_READ_HARD_WORD_CEILING=8000`; `DEFAULT_READ_SOFT_WORD_CEILING=6000` (per-file, unchanged); `DEFAULT_READ_AGGREGATE_ADVISORY=90000`; `DEFAULT_READ_AGGREGATE_ACTIVATION=100000` (§2a sensor-layer, retained for informational continuity at engine-v4 and as pre-engine-v5 behaviour).
- **Check 20 default-read detection revised**: apply close-rotation (most recent 6 sessions only) when current session ≥ `AGGREGATE_BUDGET_ADOPTION_SESSION=28`; pre-adoption behaviour (every close) retained for sessions < 28 so historical validator runs remain reproducible.
- **Check 20 aggregate-report revised**: at engine-v5 (session ≥ 28), promote from informational-only (advisory/activation notes) to pass/fail/warn enforcement against §2b budget. Hard-ceiling exceed → fail; soft-warning exceed → warn; within-budget → pass. Pre-engine-v5 behaviour (v2 §2a informational notes) retained via session-number gate.
- **Check 22 extended**: accept rotated-close citation form `[archive: provenance/<NNN-title>/03-close.md]` (regular file path) in addition to archive-pack directory path `[archive: provenance/<NNN-title>/archive/<slug>/]`.
- **Honest-limit comments added** above new engine-v5 code paths.

### §1e Development-provenance files amended

- **`open-issues/OI-018.md`** — Session 028 update appended: engine-v5 bump rationale; §5.4 status unchanged at activated-not-escalated; OI-018 carries forward; re-examination triggers and operator-direction remain.
- **`open-issues/OI-002.md`** — 13th data point appended (Session 028 D-096 substantive revision of read-contract.md v2 → v3). Also filled in missing data points for Sessions 020, 021, 022, 023, 027 in the Status line that had not been maintained across sessions 024-027.
- **`open-issues/index.md`** — OI-002 status updated; OI-004 tally updated (voluntary:required 9:8 → 10:8; criterion-3 67 → 68); OI-018 status note updated.
- **`SESSION-LOG.md`** — Session 028 entry added at close per R8a thin-index form.

### §1f Close-rotation first exercise (primary aggregate-reduction action)

Per D-096 §9 and §5: initial exercise of the §2c close-rotation rule. No physical file movement. The 20 close files for Sessions 002–022 (~56,180 body words total) become archive-surface by exclusion per the revised §1 item 7 enumeration. They remain at their original paths under `provenance/NNN-title/03-close.md`, preserved verbatim per §3, but are no longer counted in default-read by validator check 20.

Retained in default-read per 6-session window (at Session 028 close): Sessions 023, 024, 025, 026, 027, 028 `03-close.md` files (6 files).

**Pre-session aggregate**: 105,399 words / 39 files (per Session 028 open validator run).  
**Post-close aggregate (projected)**: ~55,000 words / 19 files (per pre-close validator run at Session 028: 54,905 words / 19 files measured during revision drafting; will increase slightly with this close file entering the count, landing around 55,000–56,000 words).

Post-rotation aggregate is well below both §2b soft (90K) and hard (100K) thresholds, leaving substantial headroom for forward growth. Close-rotation remains active standing rule; at Session 029 close, Session 023's close will rotate out of default-read (replaced by Session 029's own close entering the window). Steady-state expected: one close rotates out, one new close enters, net close-file count stays at 6.

### §1g No external artefact

Session 028 is a self-development deliberation session on read-contract.md revision. No `applications/` directory changes.

### §1h Engine-version transition — engine-v4 → engine-v5

This is the methodology's **fourth engine-version increment**. Notable: first engine-v-bump triggered by a preserved minority's activation warrant firing (§5.3 Pacer aggregate-hard-budget, preserved Session 023, activated Session 027, converted Session 028). Also: first bump after a five-session preservation window (engine-v4 preserved across Sessions 024–027). Recorded in `engine-manifest.md` §2 and §7.

The bump does not re-engage the §5.4 Session 022 engine-version-cadence minority: §5.4's R9 automatic-escalation window aged out at Session 026 close per D-092; the Session 028 bump is content-driven (preserved-minority activation response) not cadence-driven; per 3-of-4 cross-family convergence (Pacer, Skeptic, Outsider) engine-manifest §5 revision remains deferred per OI-018.

Fourth bump in eight sessions (engine-v2 Session 021; engine-v3 Session 022; engine-v4 Session 023; engine-v5 Session 028) — outside the original "3-bumps-in-4-sessions" R9 window but contributing to long-run cadence tracked by §5.4.

## §2 Decisions made

- **D-096** — Adopt §5.3 aggregate-hard-budget with revised values 100K/90K and paired close-rotation rule (6-session window); `read-contract.md` v2 → v3 substantive revision; engine-v4 → engine-v5. `triggers_met: [d016_2, d016_3]`. `triggers_rationale:` d016_2 fires because decision substantively revises `read-contract.md` (adds §2b and §2c; revises §1 item 7; adjusts §2a role); d016_3 fires because deliberation produced genuine 4-way disagreement on values (85K/95K vs 100K/90K vs 110K/120K vs no-conversion) and 3-way disagreement on retention window (3/6/10 sessions) with at least two plausible positions namable before deliberation. Non-Claude participation: voluntary (Outsider contributed load-bearing "laundering the activation" critique on Q2 values; `participant_organisation: openai`; d023_* not triggered — read-contract.md is not in D-023's enumerated list covering methodology-kernel, multi-agent-deliberation, validation-approach Tier 2, and OI-004 state changes).

- **D-097** — OI state housekeeping. OI-002 13th data point (Session 028 substantive revision of read-contract.md v2 → v3). OI-004 voluntary:required 9:8 → 10:8; criterion-3 cumulative 67 → 68 (Outsider's laundering critique materially shaped values decision; cross-lineage contradiction-prevailing over Claude Synthesiser's 110K/120K recommendation). OI-018 continues carry-forward; §5.4 minority unchanged. OI-007 active count: 13 (unchanged; no new OI opened per 3-of-4 convergence). New watchpoint WX-28-1 (close-rotation-exception-frequency) opened. Pre-existing watchpoints WX-22-1, WX-24-1, WX-24-2, WX-24-3, WX-27-1 all carry forward (WX-24-3 Outsider pre-response workspace exploration pattern now at n=5). `triggers_met: [none]`.

## §3 Validation

### §3a Tier 1 Structural Checks

Pre-close validator run (before SESSION-LOG update): **710 pass / 1 fail / 1 warn**. Post-SESSION-LOG-and-close commit projected: approximately 713–715 pass / 0 fail / 1 warn (close adds pass counts; the "Session 028 missing from SESSION-LOG" fail clears on SESSION-LOG update; the designed MAD 6K-soft warning persists).

- **Checks 1–19**: pass per engine-v5 baseline (engine-definition file set unchanged from engine-v4; schema expectations unchanged).
- **Check 20 (default-read surface per-file budget + §2b aggregate budget enforcement)**:
  - Per-file: 1 soft warning — `specifications/multi-agent-deliberation.md` at 6,386 words exceeds 6,000-word soft warning (within 8,000 hard ceiling). Designed persistence; unchanged across Sessions 023–028 closes (six consecutive). **§5.2 Skeptic no-change + warrant-literalism minority retroactively vindicated at Session 027** remains the load-bearing recognition here.
  - Aggregate (new at engine-v5 pass/fail/warn semantics): **pass** — 54,905 words (pre-close; projected ~56K post-close) within engine-v5 budget (soft 90,000 / hard 100,000). Initial close-rotation first exercise delivered the reduction from 105,399 pre-session to 54,905 mid-session. 
- **Check 21 (archive-pack manifest integrity)**: 6 archive-packs pass unchanged (`pre-R8a-SESSION-LOG`, `pre-R8b-open-issues`, `014-oi016-outsider`, `022-outsider`, `023-outsider`, `024-outsider`). No new archive-packs created this session (raw perspectives all well under 6K soft; Outsider at ~2.1K body words).
- **Check 22 (archive-pack citation consistency + rotated-close citation)**: all `[archive:` token references in default-read files resolve. Check 22 extension for rotated-close references (`[archive: provenance/<NNN-title>/03-close.md]`) implemented and tested. No new rotated-close citations in Session 028 default-read content (rotated closes are archive-surface-by-exclusion; references to them from default-read files would use the new convention; no such reference is load-bearing for this session).

### §3b Tier 2 Guided Assessment

1. **Provenance continuity (Q1).** Yes. Session 028 Read drew on: Session 027 close (Path G recommendation as default; §5.3 activation warrant firing; aggregate 105,399 measurement); Session 023 close (origin of §5.3 minority text; engine-v4 adoption precedent; D-086 R9 cadence trigger text); Session 026 close (§5.4 R9 age-out at Session 026); Session 022 close (§2a aggregate report adoption; thin-index precedent for rotation analogy); Session 024 close (A.4 carry-the-warning precedent; Outsider precedent). Closes for Sessions 025, 026, 027 read in full; Sessions 001–014 read in honest-limit-declared SESSION-LOG one-line index form per `00-assessment.md` §7; Session 022 close consulted via Session 023 close citation. No silent re-proposing of past rejections. The §5.3 activation-warrant-firing response draws on the §5.2 vindication precedent (Skeptic-preserver) and on the preservation-with-warrant discipline established across engine-v2/v3/v4 bumps.

2. **Specification consistency (Q2).** Yes. One specification revised (`read-contract.md` v2 → v3 — substantive per OI-002; v-bumped; v2 preserved as superseded). `engine-manifest.md` documentary update (§2, §3 heading, §7 history; no v-bump per Session 021/023 sub-pattern). `tools/validate.sh` substantively updated to match new §2b/§2c. `validation-approach.md` v5 section-references (§1 enumeration, §2 per-file budget, §2a aggregate report) all remain consistent with v3 (§1 item 7 revised; §2 per-file budget unchanged; §2a role clarified with §2b addition; check 20 gating conventions still apply at `READ_CONTRACT_ADOPTION_SESSION=22` for general check 20 activation, with `AGGREGATE_BUDGET_ADOPTION_SESSION=28` as separate gate for the engine-v5 budget-enforcement promotion). No cross-spec contradiction introduced. The new §2b cross-references to §2a, §2c, §8, §5.x minorities; the new §2c cross-references to §1, §2b, §3, §6; all cross-references resolve. `workspace-structure.md` v4 is unchanged this session (its §SESSION-LOG.md parenthetical "currently 15,000 words hard ceiling, 10,000 words soft warning" remains pre-Session-023 outdated text; this is a pre-existing WX-24-2 drift item not in Session 028's scope per scope discipline).

3. **Adversarial quality (Q3).** Genuine cross-family adversarial coverage at the deliberation level. Skeptic-preserver occupied the designated adversarial role and produced substantive dissent against conversion (Q1 no; Q2 no values; Q6 mechanism-gap; Q7 new-information insufficient). Adversarial arguments that shaped the synthesis included: (i) activation-threshold-set-without-empirical-grounding (Skeptic Q6); (ii) §5.2-vindication precedent applies structurally (Skeptic Q1); (iii) 2023 values obsolete against 2026 state (Skeptic Q2 — this argument was accepted into the synthesis); (iv) anti-laundering discipline requires new-information beyond activation-firing (Skeptic Q7). The Outsider additionally provided cross-family adversarial content: the "laundering the activation" critique against the Synthesiser's 110K/120K headroom position materially disambiguated the Q2 values decision. Skeptic's core "defer conversion" position was preserved as first-class minority §5.6 with activation warrant; Skeptic's methodology-level "pressure-signal audit" observation preserved as §5.11. Substantive dissent on Q2 values (Synthesiser 110K/120K vs Outsider 100K/90K) preserved as §5.8.

4. **Meaningful progress (Q4).** Yes, substantive. Five increments:
   - **§5.3 Pacer aggregate-hard-budget minority converted** from preservation-with-warrant to active specification at revised values (100K hard / 90K soft). First conversion of a Session 023-era minority in response to its own activation warrant firing.
   - **Close-rotation rule specified** in `read-contract.md` v3 §2c — structural mechanism paired with §2b budget; addresses close-file accretion as dominant growth driver per 4-of-4 deliberation convergence on the diagnostic.
   - **Aggregate reduced 49% in one session** via first close-rotation exercise (105,399 → ~55,000). Reversible (rotated closes remain at their paths; retention-exception available).
   - **Six first-class minorities preserved** with activation warrants (§5.6 defer-to-softer-intervention; §5.7 tighter values 85K/95K; §5.8 headroom values 110K/120K; §5.9 10-session retention window; §5.10 3-session retention window; §5.11 pressure-signal-audit methodology-level). The engine's minority-preservation mechanism now carries 18 first-class minorities across Sessions 021/023/024/027/028.
   - **Cross-family Outsider contribution: "laundering the activation" critique** — new methodology-level framing (moving a fired threshold is self-protective drift) that now informs future threshold-revision discipline. Contributes one criterion-3 data point (67 → 68) and preserves voluntary:required ratio progression (9:8 → 10:8).

5. **Specification-reality alignment (Q5).** Yes, strengthened. Pre-session: `read-contract.md` v2 §2a described aggregate as informational-only; operational reality was aggregate crossing 100K without any remediation mechanism beyond "next session deliberates." Post-session: v3 §2b adds enforcement; §2c names the primary remediation mechanism; §1 item 7 bounds the close-file accretion class. The spec's response to the observed pattern (close-file accretion over six sessions from 81K to 105K without compensating restructure) is the close-rotation rule, directly matching the diagnosis. No drift introduced; existing drift (workspace-structure.md §SESSION-LOG.md parenthetical 15K/10K) is pre-existing and flagged but not addressed in scope.

6. **Cross-model-honesty evidence (Q6).** Yes. Session 028 declares `cross_model: true`. Concrete evidence per Outsider manifest: codex exec CLI wrapper invocation (`codex exec --config model_reasoning_effort=high --color=never --skip-git-repo-check <brief>`); codex-cli version 0.121.0; model `gpt-5` provider `openai`; tokens used (reported by codex) 56,140; session duration approximately 5 minutes; output 66.2 KB including intermediate workspace-read traces and final response; committed raw at `01d-perspective-outsider.md` (2,071 body words). Outsider manifest declares `training_lineage_overlap_with_claude: independent-claim`, `participant_organisation: openai`, `claude_output_in_training: known-no`, `independence_basis: organization-distinct`. Per MAD v4 §Criterion-4 Articulation, all required v4 fields present and closed-set membership verified by check 19. Material contribution: the Outsider's "laundering the activation" critique `[01d, Q2]` prevailed over the Synthesiser Claude-subagent's 110K/120K recommendation in the values decision — documented cross-lineage contradiction-prevailing case per Session 021 D-082 P4 Assertion requirement. OI-004 criterion-3 cumulative 67 → 68; voluntary:required 9:8 → 10:8.

7. **Trigger-coverage plausibility (Q7).**
   - **D-096 declares `[d016_2, d016_3]`.** Reading D-096's Decision and Rationale text: d016_2 fires because R1–R9 substantively revises `read-contract.md` (new §2b enforcement layer; new §2c rule; revised §1 item 7; §2a role adjustment) and substantively updates `tools/validate.sh` (new constants; check 20 enforcement promotion; check 22 extension). Session 021 D-082 precedent: documentary updates to `engine-manifest.md` don't bump its own version but the underlying `read-contract.md` revision does bump the engine. d016_3 fires because deliberation produced genuine multi-way disagreement: Q1 3-of-4 adopt vs 1-of-4 preserve; Q2 four distinct value recommendations (85K/95K Pacer; no-conversion Skeptic; 100K/90K Outsider; 110K/120K Synthesiser); Q3 three distinct retention windows (3/6/10). At least two plausible positions namable before deliberation — confirmed by §5a of the brief's shared §5 design questions. d016_1 not asserted: methodology-kernel.md unchanged. d016_4 not asserted: operator directed default-path execution but did not mark the decision load-bearing beyond that; the load-bearingness flows from §5.3 minority activation rather than operator marking.
   - **D-096 declares non-Claude participation voluntary** (not via skip annotation — Outsider actually participated). d023_* does not fire: `read-contract.md` is not in D-023's enumerated list (methodology-kernel.md; multi-agent-deliberation.md; validation-approach.md Tier 2 semantic changes; OI-004 state changes). Non-Claude participation is "recommended" per MAD v4 §When Non-Claude Participation Is Required; Outsider participated voluntarily; no skip annotation required; voluntary:required 9:8 → 10:8.
   - **D-097 declares `[none]`.** Housekeeping; no new normative content. OI-004 state unchanged (tally and criterion-3 updated per Outsider contribution but state itself remains "articulated; awaiting closure-retrospective" at 3-of-4); no spec revision; watchpoint WX-28-1 opened (observational). `[none]` consistent with content per the long precedent chain (D-073/D-077/D-079/D-081/D-083/D-085/D-087/D-089/D-090/D-091/D-093/D-095).

8. **OI-004 closure-retrospective substantive adequacy (Q8).** N/A this session — no `oi-004-retrospective.md` present. Session 028 does not attempt OI-004 state advance. Voluntary:required 9:8 → 10:8; criterion-3 cumulative 67 → 68 (+1 for Outsider laundering-critique load-bearing contribution).

9. **Read-contract adherence (Q9).**
   - (a) Default-read surface read at session open: all 39 enumerated files at session-open time read per `00-assessment.md` §1a, with honest limits declared for Sessions 001–014 (consulted via SESSION-LOG one-line index) and Sessions 015–022, 024–026 (consulted via Session 027 close synthesis rather than full re-read). Load-bearing file reads: read-contract.md v2 (subject specification); engine-manifest.md (engine-v4 declaration + cadence history); OI-018 (full read for engine-manifest §5 cadence interaction check); Session 027 close (full; Path G identification + §5.3 activation record); Session 023 close (full; §5.3 origin + engine-v4 precedent); multi-agent-deliberation.md v4 (trigger analysis + Outsider criterion-4 articulation); validation-approach.md v5 (check 20 detection scope); methodology-kernel.md v5 (nine-activity structure); workspace-structure.md v4 (§provenance folder-name + default-read implications).
   - (b) Archive-surface records cited via `[archive:` token convention: one citation in `read-contract.md` v3 at line 78, citing `provenance/022-workspace-scaling-trajectory/archive/022-outsider/#chunk-04` for the Session 022 Outsider prophylactic-against-accretion argument. This is a historical citation preserved from v2 unchanged; the reference resolves per check 22. No new archive citations for Session 028 load-bearing claims (the load-bearing Session 022 / Session 023 content is present in default-read via their `03-close.md` files or via the §5.3 preserved minority text itself).
   - (c) Honest-limits declared in `00-assessment.md` §7 and recorded here. Archive-surface reads not performed this session: Session 024 Outsider archive-pack not re-read (non-load-bearing for Path G; the Session 024 A.4 carry-the-warning deliberation is adjacent but not directly subject of Session 028); Session 022 Outsider archive-pack consulted only via Session 023/027 close citations (chunk-level reading not re-performed at this session open). No silent skips. The Outsider's own Honest Limits declare the workspace reads it performed: read-contract.md, engine-manifest.md, OI-018.md, validate.sh aggregate-report section, Session 027 close, Session 028 00-assessment.md; this is a known cross-family read pattern (WX-24-3 at n=5 stable).

## §4 First-class minorities and watchpoints at Session 028 close

### §4a Minorities preserved this session (six new)

All documented with full text and activation warrants in `read-contract.md` v3 §2b minority block and in `provenance/028-session-assessment/01-deliberation.md` §6. Summary:

- **§5.6 Skeptic-preserver defer-to-softer-intervention** (adversarial role). Activation warrant: if within 3 sessions new budget fires through accretion-growth only, without observable friction, and softer-intervention alone would have achieved equivalent reduction — Skeptic-preserver position retroactively vindicated.
- **§5.7 Pacer-advocate 85K/95K tighter-values**. Activation warrant: if within 5 sessions new 100K/90K budget fires twice+ without compensating restructure forcing actual remediation — Pacer-advocate tighter values become preferred direction.
- **§5.8 Synthesiser-integrator 110K/120K headroom-values**. Activation warrant: if within 3 sessions remediation-chaos materialises (forced restructure mid-deliberation; deliberation distortion from emergency compliance) — Synthesiser-integrator headroom values become preferred direction.
- **§5.9 Synthesiser-integrator 10-session retention-window**. Activation warrant: if within 6 sessions the 6-session window + citation-exception produces a pattern where 7–10-session-back closes are consulted via retention-exception more than twice per session on average.
- **§5.10 Pacer-advocate 3-session retention-window**. Activation warrant: if within 6 sessions 6-session window proves insufficient for aggregate control (sessions consistently approach new 90K soft).
- **§5.11 Skeptic-preserver pressure-signal-audit (methodology-level)**. Activation warrant: if any Session 029+ budget-firing surfaces a case where firing triggers remediation that later proves operationally unnecessary.

### §4b Pre-existing minorities state at Session 028 close

- **§5.1 Pacer 10K/7.5K per-file** (Session 023): unactivated; preserved unchanged.
- **§5.2 Skeptic no-change + warrant-literalism** (Session 023): **retroactively vindicated Session 027**; ongoing tracking complete.
- **§5.3 Pacer aggregate-hard-budget** (Session 023): **converted to active spec at revised values Session 028 D-096**. Original minority text preserved verbatim in `read-contract.md` v3 §2b archive block for provenance.
- **§5.4 Session 022 engine-v-cadence** (Session 023): activated-not-escalated; R9 aged out Session 026; **unchanged by Session 028 engine-v5 bump per 3-of-4 convergence** (bump is content-driven not cadence-driven; engine-manifest §5 revision remains deferred per OI-018).
- **§5.5 tokeniser-drift watch** (Session 023): unactivated; preserved unchanged.
- **Session 024 A.4 minorities** (Splitter A.2; Archivist A.3; Skeptic A.1; Outsider carry-the-warning): all preserved unchanged; no activation-trigger event this session.
- **Session 027 minorities §A Discoverer / §B Minimalist / §C Archivist**: all preserved unchanged; no activation.

### §4c Minority count tracking summary at Session 028 close

**Total first-class minorities preserved across the engine: 18.**

- Session 023: 4 (§5.1, §5.2 [now vindicated-complete], §5.3 [now converted], §5.5) — effective active count 2 after Session 027 vindication of §5.2 and Session 028 conversion of §5.3.
- Session 023 engine-cadence: 1 (§5.4 activated-not-escalated).
- Session 024: 4 (A.4 deliberation; A.2, A.3, A.1, Outsider carry-the-warning).
- Session 027: 3 (§A Discoverer, §B Minimalist, §C Archivist).
- Session 028 (new): 6 (§5.6, §5.7, §5.8, §5.9, §5.10, §5.11).

Two additional precedent-tracking notes: **first preserved-minority conversion event** (§5.3 Session 028) follows **first preserved-minority vindication event** (§5.2 Session 027). The engine's minority-preservation mechanism has now demonstrated three resolution modes: (i) vindication-through-preservation (§5.2); (ii) activation-then-conversion (§5.3); (iii) continued-preservation (§5.1, §5.5, Session 024 A.4 group, Session 027 §A/§B/§C, etc.). This distribution is healthy; the mechanism is doing discriminating work.

### §4d Watchpoints active at Session 028 close

- **WX-22-1** witness-dumping pattern (Session 022): no new data.
- **WX-24-1** MAD growth: current 6,386 unchanged across six consecutive session closes 023/024/025/026/027/028. §5.2 vindicated; carry-the-warning per D-088 R1 / D-090 / D-092 / D-094 / D-096 implicitly continues.
- **WX-24-2** Budget-literal drift forward discipline: **exercised this session**. D-096's substantive revision names new literals (100K hard, 90K soft, 6-session retention) across three files (read-contract.md, validate.sh, engine-manifest.md) with matching values; no drift introduced. Pre-existing drift in `workspace-structure.md` v4 §SESSION-LOG.md parenthetical (still says 15K/10K from pre-Session-023) flagged but not addressed in scope — this is a candidate for a future minor-cleanup amendment.
- **WX-24-3** Outsider pre-response workspace exploration pattern: **n=5** (Session 028 Outsider read workspace files per Honest Limits: read-contract.md, engine-manifest.md, OI-018.md, validate.sh, Session 027 close, Session 028 00-assessment.md). Pattern stable at n=5.
- **WX-27-1** archive-token citation fragility: **exercised this session**. One illustrative archive-token reference in read-contract.md v3 initial draft triggered check 22 as a false-positive citation; repaired to use `<NNN-title>` placeholder form before final commit (per placeholder-filter in check 22 implementation). Pattern n=2 now observed; if n=3 recurs, minor-amendment to `read-contract.md` v3 §6 guidance may be warranted.
- **WX-28-1** (new) close-rotation-exception-frequency: observational. Activation threshold: if within 10 sessions (Sessions 029–038) retention-exception decisions are recorded in 3 or more sessions, the 6-session window may be too narrow; Synthesiser-integrator §5.9 10-session window minority may become preferred direction.

## §5 Honest notes from the session

- **First preserved-minority conversion event.** §5.3 (Session 023 Pacer aggregate-hard-budget) converts from preservation-with-activation-warrant to active specification at revised values. This is paired with Session 027's first preserved-minority vindication event (§5.2). The engine's minority-preservation mechanism can now resolve minorities in multiple directions per their own warrant language. The mechanism is doing discriminating work, not ratcheting one way.

- **Revised values, not preserved values.** §5.3's original proposal was 80K soft / 90K hard against an 81K aggregate; this session adopted 90K soft / 100K hard against a 105K aggregate. The revision is substantively justified by: (i) aggregate has grown 29% since the original values were set; (ii) the Outsider's "laundering the activation" cross-family critique against alternative above-current values; (iii) the semantic-layering argument for matching §2a advisory/activation thresholds. The adopt-with-revision pattern is the engine's first demonstration of preservation-with-warrant resolving as a principled update rather than either verbatim adoption or continued preservation.

- **Outsider's "laundering" critique as load-bearing cross-family contribution.** The Outsider's key argument in Q2 — that moving the hard ceiling above 100K after crossing it is "self-protective drift" — was not produced by any Claude perspective. Three Claude perspectives proposed three distinct values (85K/95K Pacer; 110K/120K Synthesiser; no-conversion Skeptic). The Outsider's 100K/90K at the fired threshold, paired with same-session remediation, emerged as the synthesis resolution because it honours the fired activation without moving the trigger. This is documented cross-lineage contradiction-prevailing — criterion-3 data point for OI-004 and a direct P4 Assertion-shape case.

- **Close-rotation as reversible mechanism.** The first exercise of §2c rotates 20 close files out of default-read *by exclusion*, not by physical movement. Files remain at `provenance/NNN-title/03-close.md` paths; only the default-read enumeration changes. This is reversible via (i) the retention-exception decision mechanism in §2c itself, (ii) future revision of the retention window, or (iii) temporary override for session-specific work. The reversibility property was noted in Synthesiser [01c, Q3] and adopted into the specification text.

- **Aggregate reduction 49% in one session.** Pre-session 105,399 → post-rotation ~55,000 words, achieved by the §2c rule's initial automatic application. This is the largest single-session aggregate change in the engine's history. It returns the default-read surface to a pre-Session-024 size while preserving all content; the reduction is structural (enumeration change) not content-destructive. Future sessions should find the workspace faster to Read (smaller default-read) and more navigable (SESSION-LOG.md thin-index remains the historical index).

- **§5.4 cadence minority status unchanged despite v5 bump.** The engine-v4 → engine-v5 bump is the fourth bump in eight sessions (Sessions 021/022/023/028). It follows a five-session preservation window (Sessions 024–027) and is content-driven (preserved minority activation response). Per 3-of-4 cross-family convergence (Pacer, Skeptic, Outsider; with Synthesiser dissenting only on "engage vs keep separate"), the §5.4 cadence minority is not re-escalated; OI-018 remains deferred. This is the engine's demonstration that bump-cadence and bump-substance are distinct axes: substantive revision is not cadence-violation when preceded by substantial restraint.

- **Close-verbosity pattern n=3.** Session 026 flagged close-verbosity pattern n=2 (Sessions 025 and 026 Path-A closes at ~2,700 and ~3,200 words with no substantive decisions). Session 027 was substantive (5,253 words — largest to date, driven by substantive deliberation content). This Session 028 close is also substantive (projected ~5,000–6,000 words for this file) and appropriately sized for its content. Close-verbosity framing is scoped to Path-A-shape sessions per Session 027 close §5 observation; substantive-deliberation closes retain their full Tier 2 structure. Session 028's close size is appropriate.

- **No Outsider brief-factual-error this session.** Session 023 Outsider caught a brief-factual-error (MAD word count). Session 028 Outsider's Honest Limits do not flag any brief-factual-errors; the brief's §3 aggregate-trajectory table matches validator-measured values (Outsider's Q7 cites 105,399 matching the brief's table). This is either (i) the brief was factually accurate, or (ii) the Outsider's own Honest Limits did not exhaustively verify the brief's numbers. The §3a table's prior-session aggregates (~81,500, ~83,000, ~92,500, 95,675, 99,532, 105,399) derive from Session 022 close, Session 023 close, Session 024 close, Session 025 close, Session 026 close, and Session 028 pre-session validator run. No inconsistency observed between these values and validator-measured state.

- **Outsider read the Session 028 00-assessment.md.** Per the Outsider's Honest Limits, the Outsider read `provenance/028-session-assessment/00-assessment.md` during its independent-phase reasoning. This is consistent with the n=5 WX-24-3 Outsider workspace-read pattern. The Outsider's reading of the in-session assessment means it had access to the orchestrator's trigger analysis and path selection reasoning before forming its response. Per MAD v4 §Workspace context per perspective, Claude perspectives do not read workspace files during the independent phase (this is the designed asymmetry per the Session 022 Outsider observation). The asymmetry is preserved via the brief's §7 anti-import constraint and the Outsider's own transparent declaration in Honest Limits; future sessions may consider whether the asymmetry should be documented as engine behavior.

- **Eleven first-class minorities preserved from Sessions 023/024/027 + six new from Session 028 = eighteen total.** The engine's minority-preservation mechanism now carries eighteen active first-class minorities. This is healthy accumulation: preserved positions represent disagreement that the engine honours rather than suppressing. At some future point the engine may need to deliberate minority-count management (e.g., a deliberation on when minorities graduate to "historical provenance" after sustained non-activation); no such mechanism exists now and none is warranted by Session 028's scope.

- **The 29% aggregate growth over 6 sessions was the evidence needed.** One of the Skeptic-preserver's concerns was that the activation threshold was set without empirical grounding. That critique has force for the *original* 100K number (it was a round-number choice in Session 023). But the *trajectory* from 81K to 105K over six sessions, with growth accelerating in substantive sessions, is empirical evidence that advisory-only reporting does not produce remediation. The §2a advisory was emitted at Session 024; the engine proceeded with growth; activation crossed at Session 027. This trajectory is the Skeptic-preserver's own activation warrant backwards: the evidence of advisory-insufficiency is what justifies the §5.3 conversion, not the arbitrary threshold-crossing.

## §6 Next session

Session 029 should:

1. **Run `tools/validate.sh` at start.** Expected baseline: approximately 710–715 pass, 0 fail, 1 warn (the designed MAD 6K-soft on `multi-agent-deliberation.md` persists until MAD changes; aggregate budget pass at ~55K–60K range depending on Session 028 post-close growth and any Session 029 pre-session additions). The validator now runs the engine-v5 §2b enforcement and the §2c close-rotation via `AGGREGATE_BUDGET_ADOPTION_SESSION=28` session-number gate.

2. **Audit Session 028 synthesis fidelity.** Particular attention to:
   - **Whether the Outsider's "laundering the activation" critique was faithfully load-bearing** or post-hoc-rationalised. Examine `01-deliberation.md` §3 and §8 against the Outsider's actual Q2 text `[01d, Q2]`. The synthesizer-original resolution (`[synth]` marking at §3) should align with the Outsider's framing without over-reading.
   - **Whether D-096's classification of the `read-contract.md` revision as substantive is consistent with OI-002 heuristic.** D-096 argues substantive on "severity decisions" (new pass/fail/warn enforcement at numeric thresholds) + "new normative content" (new rule types). Audit should examine whether this aligns with prior substantive-classification decisions (Session 023 D-086 budget-recalibration; Session 021 D-082 schema additions; Session 022 D-084 new-spec-creation).
   - **Whether the 6-session retention window's initial exercise (rotating 20 files, 56,180 words) caused any information-access regressions.** Session 029 open should test: can the opening assessment draw on Session 022-or-earlier content without friction when needed? If friction is observed, the retention-exception mechanism should be considered.

3. **Operator path options available at Session 029 open.** With §5.3 now converted and engine-v5 adopted:
   - **(A) Watch aggregate trajectory under new budget.** §2b budget is passive in the sense that it doesn't trigger action until crossed. Session 029+ should observe whether aggregate stabilises or continues climbing under the rotation rule.
   - **(B) OI-004 closure-retrospective draft.** Voluntary:required 10:8; criterion-3 cumulative 68; one more closure-retrospective-drafted-by-session would push toward closure discussion.
   - **(C) Cell 1 re-attempt of reference-validation.** Unexercised across 020–028 (9 consecutive non-test sessions).
   - **(D) OI-015 laundering-gap deliberation.** Six-exercise positive pattern through Session 024; stable.
   - **(E) OI-018 engine-manifest §5 revision.** Substantive engagement possible given Session 028's v5 bump interaction with §5.4; no re-escalation at Session 028 but operator may elect to take this up.
   - **(F) Operator-directed agenda.**
   - **(G)** [Path G from Session 027 close] was consumed this session.
   - **(H) Index-audit altitude deliberation.** From Session 027 Q6 finding; low-urgency.
   - **(I) NEW: §5.6 Skeptic-preserver defer-to-softer-intervention minority activation check.** At Session 031 close (3 sessions after Session 028 adoption), the Skeptic-preserver minority's activation warrant will be evaluable: did the new budget fire only through accretion with no observable friction, and would softer-intervention alone have sufficed? This is an activation-check rather than a substantive deliberation but is calendar-triggered.

4. **§5.3 conversion is complete; further §5.3-related deliberation is activated only if a minority warrant fires** (§5.6, §5.7, §5.8, §5.9, §5.10, §5.11). Until then, the aggregate-budget + close-rotation regime operates as the engine's standing mechanism.

5. **Session 028 watchpoints active from Session 029 start**:
   - WX-22-1 witness-dumping pattern: no new data.
   - WX-24-1 MAD growth: current 6,386 stable.
   - WX-24-2 budget-literal drift forward discipline: Session 028 exercised cleanly; workspace-structure.md pre-existing drift (§SESSION-LOG.md 15K/10K parenthetical) flagged for future minor-cleanup.
   - WX-24-3 Outsider workspace-read pattern: n=5 stable.
   - WX-27-1 archive-token citation fragility: n=2 observed (one Session 028 instance repaired pre-commit).
   - WX-28-1 (new) close-rotation-exception-frequency: observational; zero exceptions recorded.

6. **Forward observations carried**:
   - Close-verbosity framing continues scoped to Path-A-shape sessions per Session 027 observation.
   - Pressure-signal-audit methodology-level observation preserved as §5.11 minority; may become preferred-direction if any future budget-firing produces operationally-unnecessary remediation.
   - Outsider-asymmetric workspace-read pattern (n=5) remains outside the MAD v4 §Workspace context per perspective rule; future MAD revision may document the asymmetry.

7. **Minority count tracking summary for Session 029 open**: 18 first-class minorities preserved across Sessions 023/024/027/028. §5.2 vindication-complete; §5.3 converted-to-active-spec; §5.4 activated-not-escalated (unchanged); other 15 preserved-with-activation-warrants.

8. **Engine-v5 is the current loadable implementation.** External-application workspaces initialising from engine-v5 inherit: aggregate hard budget + close-rotation at 6-session window + all engine-v4 content. External-application behavior at engine-v5 is a forward concern; no external-application launch this session.

9. **Operator directive compliance note**: Session 028 was opened with the operator directive "Pick default agent-recommended path and do not wait for operator ratification." Path G (§5.3 conversion deliberation) was identified as the default-agent-recommended path per Session 027 close §6 item 3. The directive was honoured: no ratification halt; multi-agent deliberation convened; substantive decision produced; artefacts committed. Session 029 onwards: operator may resume standard ratification-halt framing or continue default-path execution as preferred.
