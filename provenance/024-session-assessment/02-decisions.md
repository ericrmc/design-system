---
session: 024
title: Decisions — Session 024
date: 2026-04-23
status: complete
---

# Decisions — Session 024

## D-088: A.4 carry-the-warning + conversion conditions + budget-literal drift cleanup; engine-v4 preserved

**Triggers met:** [d016_3]

**Triggers rationale:** d016_3 (reasonable disagreement) fires — four perspectives produced four distinct positions (A.2 split / A.3 narrow relocate / A.4 / A.4-with-conversion-conditions) with 2-of-4 cross-family convergence (Skeptic + Outsider) for A.4 against 1-of-4 Claude-only for each of A.2 and A.3. d016_1 not fired (methodology-kernel.md unchanged). d016_2 not fired (R6 cleanup is minor per OI-002 stale-witness-correction branch; R1 and R2 do not revise any specification; R3 explicitly preserves engine-v4). d016_4 not fired (operator-directed Path A selection at session open is path-selection per Session 021 precedent, not load-bearing-marking per D-074 precedent). d023_* not fired: no kernel revision (d023_1); no MAD revision (d023_2); R6 validation-approach.md edit is in the §Gating Conventions explanatory block correcting stale constants, not a semantic-Tier-2 revision (d023_3 does not fire per OI-002 minor classification); no OI-004 state change asserted (d023_4 — criterion-3 data-point increment is not a state change per Session 008 D-052 precedent). Non-Claude participation (Outsider) was voluntary under the MAD §Non-Claude Participation Is Recommended clause for d016_3-only decisions; voluntary:required rebalances 8:8 → 9:8.

**Decision:**

Adopt R1–R7 per the Session 024 synthesis:

- **R1**: A.4 carry-the-warning is the Session 024 remediation. No change to `specifications/multi-agent-deliberation.md` text. MAD remains at 6,386 words (live validator-measured); the 6K-soft-warn persists through session close as designed per `read-contract.md` v2 §8.

- **R2**: Pre-committed conversion conditions. If Session 025+ observes either (i) MAD reaches 7,500 words, OR (ii) a substantive MAD revision is warranted on content-merit grounds and cannot coherently integrate into the monolithic file, the carry-the-warning position converts to A.2 split with the OI-004 block (MAD lines 328-429 at engine-v4) as the named seam. Both Splitter [01a Q1, Q5] and Outsider [archive chunk 09, Q1, Q5] endorsed the OI-004 seam; cross-family convergence (4-of-4) on seam-choice carries if conversion fires.

- **R3**: No engine-v bump. Engine-v4 preserved per `engine-manifest.md` §5. §5.4 Session 022 cadence minority remains at activated (not escalated to substantive). OI-018 not activated this session.

- **R4**: §5.1 Pacer counter reads zero through Session 024 (no restructure-for-budget event fired). §5.2 Skeptic vindication runway preserved: MAD at 6,386 is below the 7,500-word trigger; no restructure-for-budget event occurred; runway remains open through Session 027 review.

- **R5**: WX-22-1 laundering-as-codification is not advanced or retired by Session 024. No archive indirection created; no split boundary added. Future A.2 conversion per R2 will engage WX-22-1 via the Splitter [01a Q4] three-piece defence + Session-post-conversion operator-discipline test.

- **R6**: Budget-literal drift cleanup (minor edits per OI-002 heuristic). Three stale literals corrected to align with Session 023 D-086 R5 validate.sh constants (8K hard / 6K soft):

  - `specifications/validation-approach.md` §Gating Conventions code block (lines 108-116): `DEFAULT_READ_HARD_WORD_CEILING=15000` → `8000`; `DEFAULT_READ_SOFT_WORD_CEILING=10000` → `6000`.
  - `specifications/read-contract.md` §4 (line 109): "each chunk ≤ 10,000 words (matching the §2 soft warning)" → "each chunk ≤ 6,000 words (matching the §2 soft warning)".
  - `specifications/read-contract.md` §9 (line 183): "(§2: 15,000 words)" → "(§2: 8,000 words)".

  Classification: minor per OI-002 — stale-literal cross-reference correction; no new normative content; no new rules, required fields, triggers, severity decisions, gating rules, or required artefacts. Frontmatter `last-updated` updated to 2026-04-23, `updated-by-session: 024` on both files. No file-level version bump. No engine-v bump per §5 non-bump list ("minor elaborations within an existing spec's scope").

- **R7**: Watchpoints opened — WX-24-1 (MAD growth monitoring with named thresholds); WX-24-2 (budget-literal drift forward discipline); WX-24-3 (Outsider pre-response workspace exploration pattern at n=4). No new OI opened per OI-007 scaling pressure.

**Rationale:**

A.4 carries the 2-of-4 cross-family convergence (Skeptic + Outsider) per MAD v4 §Synthesis weighting convention. The Outsider's [archive chunk 09 Q1] framing — *"A.4 now, but not as passive drift. Carry the warning this session and record an explicit conversion condition"* — and its [Q3] primary warrant — *"the trigger is the soft-warning threshold, not a discovered semantic incoherence in MAD's current structure"* — are load-bearing for the budget-driven-vs-content-completion classification that the Splitter and Archivist contested. Cross-family composition is the primary adoption signal per Session 021/022/023 precedent for 2-of-4 cross-family splits.

The Outsider's two substantive cross-model findings (§4.1 brief-factual-error catch at 6,403→6,386; §4.2 budget-literal drift in three adjacent spec locations) are OI-004 criterion-3 data points. §4.2 additionally shapes R6: cleaning up Session 023's stale witnesses is necessary before any future restructure deliberation can rest on consistent spec text.

Preserved first-class minorities (§5.1 Splitter; §5.2 Archivist; §5.3 Skeptic four-condition A.1; §5.5 hybrid A.2+A.3) carry operational activation warrants per `01-deliberation.md` §5. §5.4 Outsider conversion-condition adopted as R2 rather than preserved as minority.

**Rejected alternatives:**

- **A.2 split now** (Splitter [01a]) — rejected because 2-of-4 cross-family weighting carries for A.4; Outsider + Skeptic classification of the Session 024 timing as budget-driven cancels the Splitter's content-completion warrant for this session. Splitter's specific seam (OI-004 block at lines 328-429) is preserved as R2 conversion path, not rejected on the merits.
- **A.3 narrow relocate** (Archivist [01b]) — rejected on similar grounds plus Outsider [archive chunk 09 Q2] specific objection that *"archive relocation of the OI-004 or heterogeneous-participant sections would make archive access routine"* (WX-22-1 direct engagement). Archivist's narrow seam (YAML blocks + §Open Extensions) is preserved as §5.2 with operational activation warrant.
- **A.1 compression** — not endorsed by any perspective as primary; Skeptic [01c] four conditional acceptance conditions preserved as §5.3.
- **Engine-v5 bump via same-session OI-018 revision** (Splitter + Archivist preferred pathway) — rejected because A.4 carries and R1 contains no engine-definition-file revision.

**Synthesizer limits:** per `01-deliberation.md` §8 honest-limits section. The 2-of-4 cross-family weighting is load-bearing; the Splitter/Archivist content-completion framing was assessed as weaker than the Outsider/Skeptic budget-driven framing but a Session 025 audit should re-examine D2 specifically.

## D-089: OI state housekeeping; Session 024 watchpoints; OI-004 tally and criterion-3 increments

**Triggers met:** [none]

**Triggers rationale:** Per Session 023 D-087 + Session 022 D-085 + Session 021 D-083 + Session 020 D-081 + Session 019 D-079 + Session 018 D-077 + Session 016 D-073 housekeeping precedent. Records OI consequences of D-088 without adding new normative content. No kernel/spec/MAD/validation-approach revision in D-089 itself (R6's spec edits are under D-088's scope). No OI-004 state change asserted (criterion-3 data point increment per D-088 is not a state change per Session 008 D-052 literal reading of D-023.4). Not operator-marked load-bearing.

**Decision:**

- **OI-002**: 11th data point. R6 minor-edit cleanup is stale-witness correction per OI-002 heuristic; heuristic continues to hold stable. No formal update.
- **OI-004**: tally unchanged at 8-of-3 required (D-088 does not fire d023_4). Voluntary:required rebalances 8:8 → 9:8. Criterion-3 gains 2 data points from Session 024 (§4.1 brief-factual-error catch; §4.2 budget-literal drift catch); cumulative 65 → 67 across Sessions 005-024. Criterion-4 remains articulated (state 3: "Articulated; awaiting closure-retrospective"); no closure-retrospective attempted.
- **OI-007**: active count unchanged at 13.
- **OI-015**: Session 024 is the 6th positive exercise. Operator direction (Path A) treated as path-selection not value-binding; synthesis adopted A.4 position (2-of-4 cross-family for A.4 against the implicit "execute some remediation" framing of Path A).
- **OI-018**: trigger-gated; not activated this session (no engine-v bump per D-088 R3). Remains Open — deferred.
- **Watchpoints opened** (per D-088 R7): WX-24-1 MAD growth monitoring; WX-24-2 budget-literal drift forward discipline; WX-24-3 Outsider pre-response workspace exploration pattern.
- **No new OI opened** per OI-007 scaling pressure precedent (Session 014 Skeptic OI-vs-watchpoint discipline).
- **Five first-class minorities preserved** at `01-deliberation.md` §5.1-§5.5 with operational activation warrants per Session 023 / Session 021 / Session 019 / Session 014 precedent.

**Rationale:** standard OI-state housekeeping following a substantive deliberation. No OI state transitions; three watchpoints opened as lighter-weight alternatives to OI opening per OI-007 scaling pressure.

**Rejected alternatives:**

- **Open OI-019 for budget-literal drift forward discipline** — rejected in favour of WX-24-2 watchpoint per Session 014/020/023 precedent (watchpoints preferred over new OI when operational activation is well-specified and scope is narrow).
- **Open OI-020 for Outsider workspace-read spec asymmetry** — rejected in favour of WX-24-3 watchpoint; asymmetry is now n=4 stable but no material-contribution-disadvantaged-Claude case has arisen.
- **Advance OI-004 criterion-3 threshold** — not proposed by any perspective; tally discipline preserved per Session 021 D-082 four-state lifecycle.
