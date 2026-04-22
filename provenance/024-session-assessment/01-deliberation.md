---
session: 024
title: Deliberation synthesis — MAD 6K-soft-warn response
date: 2026-04-23
status: complete
synthesizer: claude-opus-4-7-orchestrator
participants_family: cross-model
cross_model: true
non_claude_participants: 1
oi004_qualifying_participants: [outsider]
brief_anchor_commit: bb2e3f2
---

# Synthesis — Session 024 deliberation

Four perspectives reasoned independently from the §1-§6 + §8-§10 shared brief at commit `bb2e3f2`. Splitter [01a] advocated A.2 split; Archivist [01b] advocated A.3 narrow relocate (YAML blocks + §Open Extensions, explicitly not OI-004 sections); Skeptic [01c] advocated A.4 carry-the-warning; Outsider [01d / archive chunk 09] advocated A.4 with a concrete conversion condition.

Throughout this synthesis: claims attributable to a perspective cite `[01X, QN]`; synthesiser-original claims are marked `[synth]`; Outsider attributions cite `[archive: provenance/024-session-assessment/archive/024-outsider/]` with the understanding that the response body lives principally at chunks 08-09 following the final `codex` marker.

## §1 Cross-model composition

`cross_model: true` with one non-Claude participant (Outsider: OpenAI GPT-5.4 via `codex exec`, session id `019db6e4-502d-77c0-9feb-c0f3274eb012`, 120,810 tokens, reasoning effort xhigh). Three Claude Opus 4.7 subagents: Splitter, Archivist, Skeptic. Outsider manifest declares `training_lineage_overlap_with_claude: independent-claim`; `participant_organisation: openai`; `independence_basis: organization-distinct`. Qualifies for OI-004 criterion-4 narrowing under MAD v4 §Criterion-4 Articulation [model-branch prongs 1-3 met].

## §2 Convergences

### C1 (4-of-4 cross-family): A.3 relocation of the OI-004 sections is wrong

Splitter [01a Q5]: *"Moving them to archive (A.3 applied to these sections) is wrong for exactly that reason — archive-access is by exception, validator-check-predicates are every-session, the disciplines collide."* Archivist [01b Q5] explicitly excludes the four OI-004 sections from its A.3 seam: *"A.3 as I have specified it does not touch the four OI-004-scoped sections... Those four sections are load-bearing normative text."* Skeptic [01c Q5]: *"A.3 relocate-to-archive is prima facie wrong: it converts validator-consulted predicates into archive-accessed ones."* Outsider [archive chunk 09, Q5]: *"archive relocation of the OI-004 apparatus would demote active validation law into exception-read material. I would reject that outright."* Four-of-four cross-family convergence.

### C2 (2-of-4 cross-family, Claude-only Archivist adjacent): Under A.4, no engine-v bump; §5.4 does not escalate this session

Skeptic [01c Q2]: *"A.4 is a deliberated decision-not-to-act. Per brief §2, A.4 involves no spec change, no tool change, no engine-v bump."* Outsider [archive chunk 09, Q2]: *"On my chosen shape, no engine-v bump. The honest classification is 'no engine-v5 because no engine-definition file changed.'"* Both explicitly derive non-escalation of §5.4: the activation escalator is a further engine-v-bump, not mere discussion of one. The Claude-only Splitter and Archivist do not disagree with this conditional; they disagree with A.4 as the shape.

### C3 (2-of-4 cross-family): A.4 preserves §5.1 Pacer counter at zero and §5.2 Skeptic runway through Session 025 review

Skeptic [01c Q3]: *"A.4 is a content-completion-lack-of-event, not a budget-driven restructure; it preserves §5.2 runway. A.1/A.2/A.3 begin consuming §5.1's 3-event counter on the first data point in the 5-session window."* Outsider [archive chunk 09, Q3]: *"The evidence is in the framing of the work itself. Session 023 explicitly set up Session 024 as 'respond to the immediate 6K-soft-fire on multi-agent-deliberation.md'. The trigger is the soft-warning threshold, not a discovered semantic incoherence in MAD's current structure... adopting A.1/A.2/A.3 now would count, in substance, as the first budget-driven restructure event in the Session 024-028 window."* The Claude-only Splitter [01a Q3] and Archivist [01b Q3] each argue their restructure is content-completion-driven; Outsider and Skeptic treat the session's *framing* as determinative and find the content-completion argument inverted by the timing.

### C4 (2-of-4 cross-family): A.4 best avoids WX-22-1 laundering-as-codification

Skeptic [01c Q4]: *"A.4 engages WX-22-1 trivially: no content moves, no archive reference created, no split boundary added."* Outsider [archive chunk 09, Q4]: *"Carrying the warning keeps default-read meaning simple: there is still one governing MAD file read in full at session open. No archive indirection is introduced, and no 'secondary' spec is created that may be treated socially as optional even if formally default-read."* Splitter [01a Q4] and Archivist [01b Q4] argue their shapes *survive* WX-22-1 with discipline; they do not claim to avoid it as cleanly as A.4.

### C5 (4-of-4 cross-family): A.2 is the right seam *if* restructure is taken

Not Q1 convergence but Q5 convergence: Splitter [01a Q1] endorses the four-OI-004-sections seam; Archivist [01b Q5] agrees the OI-004 seam is content-coherent but does not relocate it; Skeptic [01c Q5] concedes A.2's seam preserves default-read status *nominally* (the objection is cadence and OI-004 integrity, not seam-choice); Outsider [archive chunk 09, Q1, Q5] names the OI-004 block at lines 328-429 explicitly as the A.2 seam for future conversion. **Cross-family agreement: if a split is ever done, the OI-004 block is the correct seam.**

## §3 Divergences

### D1 Q1 remediation shape

- **A.2 split (Splitter, 01a Claude):** new `multi-agent-deliberation-oi004.md`; MAD residual ~4,940 words.
- **A.3 narrow relocate (Archivist, 01b Claude):** YAML field-blocks + §Open Extensions → `archive/mad-schema/`; MAD residual ~5,200-5,400 words; OI-004 sections stay default-read.
- **A.4 carry-the-warning (Skeptic, 01c Claude; Outsider, 01d non-Claude):** no spec change this session.

Cross-family composition: A.4 carries **2-of-4 cross-family** (Skeptic + Outsider). A.2 and A.3 each carry **1-of-4 Claude-only**. Per MAD v4 §Synthesis "convergence across lineage is stronger than convergence within lineage" and the Session 021/023 2-of-4 cross-family precedents, A.4 is the load-bearing adoption signal.

### D2 Classification of restructure as budget-driven vs content-completion-driven

- **Content-completion-driven** (Splitter + Archivist, 2-of-4 Claude-only): Splitter [01a Q3]: *"I would recommend this split even if the soft-warn had not fired."* Archivist [01b Q3]: *"If the soft-warn had fired at 7,000 instead of 6,403, my proposal would be identical."*
- **Budget-driven** (Skeptic + Outsider, 2-of-4 cross-family): the Session 024 framing (responding to the soft-fire) and the absence of a reader-reported coherence signal are both evidence that any A.1/A.2/A.3 now would be budget-driven in substance, regardless of post-hoc rationalisation.

Adopted reading: synthesis follows cross-family convergence. **Any A.1/A.2/A.3 adopted at Session 024 would increment §5.1 Pacer's counter as a budget-driven event.** This does not settle whether such a restructure is ever right; it says the classification of Session 024's action as budget-driven is correct if the action is taken.

### D3 §5.4 cadence minority engagement

- **Activated-to-substantive escalation acceptable** (Splitter + Archivist, 2-of-4 Claude-only): both propose accepting engine-v5 and running same-session OI-018 §5 revision deliberation.
- **Preserve activated-not-substantive** (Skeptic + Outsider, 2-of-4 cross-family): avoid the bump; §5.4 stays at activated; counter reads 3-bumps-in-4-sessions without advancing.

Adopted reading: A.4 carries, so §5.4 remains at activated-not-substantive through Session 024.

### D4 Outsider's concrete conversion condition (A.4 is not passive drift)

Outsider [archive chunk 09, Q1]: *"A.4 now, but not as passive drift. Carry the warning this session and record an explicit conversion condition: if MAD grows again, or if a future substantive MAD revision is already warranted on content grounds, convert then to A.2 with the OI-004 block as the named split seam."* Skeptic [01c Q6] opens WX-24-1 in a similar but less committal form (reach 7,500 → reconsider A.1; reach 8,000 → hard-fail forces restructure). The Outsider's formulation is sharper and cross-family-anchored; synthesis adopts the Outsider's conversion-condition wording, cross-referenced with Skeptic's thresholds.

### D5 Light A.1 compression

Skeptic [01c, "Evidence that would change position"] names four conditions under which light A.1 compression becomes acceptable (literal duplication; semantic preservation demonstrable; residual >5,500 words; minor-classification defensible). Neither Splitter nor Archivist endorses A.1; Outsider [archive chunk 09, Q1] judges compression-in-place worse than A.4 under present conditions. Adopted: A.1 is **not** taken at Session 024; Skeptic's four conditions preserved as §5.2 minority-scope activation material for future sessions.

## §4 Cross-model contributions (Outsider-originated, shape outcomes)

Two substantive Outsider contributions no Claude perspective produced. Both are OI-004 criterion-3 data points.

### §4.1 Brief-factual-error catch (recurring pattern from Session 023)

Outsider [archive chunk 09, preamble]: *"I do not accept the brief's implicit claim that the current validator-measured MAD size is 6,403 words. The live workspace now reports specifications/multi-agent-deliberation.md at 6,386 words, with aggregate default-read surface at 89,327 words across 35 files; 6,403 is a stale carry-forward witness from Session 023 prose, not the current live measurement. I am reasoning from the live number."*

Brief §2 cites 6,403 words from Session 023 close; live validator at Session 024 open measured 6,386. Splitter, Archivist, and Skeptic all reasoned from 6,403. Outsider ran `tools/validate.sh` directly and used the live number. This is the *second consecutive session* with an Outsider brief-factual-error catch (Session 023 Outsider caught the 4,800 vs 6,403 word-count estimate). The §5.5 Session 023 minority (brief-factual-error watch) is thereby empirically strengthened: future briefs citing file-size claims MUST use validator-measured data, not estimated; orchestrators should include a live validator run in brief preparation.

### §4.2 Budget-literal drift in adjacent specs

Outsider [archive chunk 09, Q1]: *"I also note the budget recalibration wave is not textually fully settled: read-contract.md still contains inherited 10K/15K witnesses in §4/§9, and validation-approach.md still prints the old 15K/10K constants in its explanatory block."*

Verified at synthesis (orchestrator read directly):
- `specifications/validation-approach.md` lines 108-116 (§Gating Conventions checks 20/21/22): `DEFAULT_READ_HARD_WORD_CEILING=15000` and `DEFAULT_READ_SOFT_WORD_CEILING=10000`. The actual `tools/validate.sh` constants are now `8000` and `6000` (updated Session 023 D-086 R5). Spec text drifts from tool.
- `specifications/read-contract.md` line 109 (§4 Archive-pack structure): *"Chunk size target: each chunk ≤ 10,000 words (matching the §2 soft warning)"*. §2 soft warning is now 6,000; cross-reference broken.
- `specifications/read-contract.md` lines 183-189 (§9 Close-time obligation): *"Any file exceeding the default-read per-file hard ceiling (§2: 15,000 words)"*. §2 now says 8,000; stale literal.

This finding is independent of the MAD 6K-soft-warn question. It is evidence that Session 023's v2 revision introduced drift that Session 024 has caught. Remediation is minor per OI-002 heuristic (stale-witness correction, not new normative content). Synthesis recommends R6 minor-edit cleanup.

The second finding strengthens the Outsider + Skeptic A.4 position: the budget-recalibration cycle is not textually settled; doing another engine-level restructure *on top of* this unsettled text would compound drift. Clean the drift first, then (if the soft-warn is still firing) reconsider restructure.

## §5 Preserved first-class minorities

Per MAD v4 §Synthesis and Session 023 [01-deliberation.md §5] precedent, adopted decisions preserve minority positions with operational activation warrants.

### §5.1 Splitter content-completion-A.2 minority (Claude-only, 1-of-4)

**Position** [01a, Q1, Q2, Q5]: the OI-004 four-section block has accumulated a content seam that warrants A.2 split on its own merits, independent of budget signal. Engine-v5 acceptable at same-session OI-018 §5 revision.

**Activation warrant**: if MAD grows to 7,500 words by Session 027, OR a future content-driven substantive MAD revision arises that cannot coherently integrate into the monolithic file, the Splitter's A.2 proposal with the OI-004 seam (lines 328-429) becomes the preferred revision direction. Both the Session 024 Splitter [01a Q1-Q5] three-piece WX-22-1 defence (validator enforcement, cross-reference density, closure-retrospective cite-surface) and the five-item execution checklist [01a Q5] are pre-committed design for that future session.

### §5.2 Archivist narrow-seam-A.3 minority (Claude-only, 1-of-4)

**Position** [01b, Q1, Q4]: MAD's bulk problem is detail-layers not OI-004 content — specifically §Heterogeneous-Participant Recording Schema's YAML field-blocks (~400 words) and §Open Extensions (671 words of non-normative futures register). Relocating these to `archive/mad-schema/` (default-read prose retained + archive-referenced detail) is repair-of-intent not codification-of-laundering.

**Activation warrant**: if a Session 025+ pre-commit check confirms that (a) validation-approach checks 16-19 reference Heterogeneous-Participant Recording Schema fields by name not by literal YAML parse, AND (b) §Open Extensions is demonstrably not consulted during routine deliberation work over 3+ sessions, the Archivist's A.3 narrow-seam proposal becomes available as alternative remediation if a future soft-warn fires. Archivist's six-section Session 025 audit criteria [01b Q6] pre-commit the evaluation surface.

### §5.3 Skeptic A.1 light-compression conditional minority (Claude, 1-of-4)

**Position** [01c, "Evidence that would change position"]: light A.1 compression is acceptable if and only if four conditions hold simultaneously — named literal-duplication cuts; semantic-preservation demonstrable; residual ≥5,500 words; minor-classification defensible under §5.

**Activation warrant**: any Session 025+ proposal of A.1 compression must satisfy all four conditions in its decision record. Short of all four, A.1 collapses to forbidden silent-compression per `read-contract.md` v2 §8 second paragraph. This minority operationally defines when A.1 is and is not available.

### §5.4 Outsider conversion-condition enrichment of A.4 (non-Claude, 1-of-4 but adopted as R2)

**Position** [archive chunk 09, Q1]: A.4 is not passive drift; it must carry a concrete conversion condition. *"If MAD reaches 7,500 words, or if a future session already has a content-driven reason to revise MAD substantively, then prefer A.2 over A.1/A.3. The seam should be the contiguous OI-004 block at lines 328-429 into a new active default-read file such as multi-agent-deliberation-oi004.md."*

This position is adopted as R2 rather than preserved as minority — the Outsider's sharpening of Skeptic's A.4 creates the cross-family 2-of-4 bound form. Preserved here for provenance completeness: the bare-A.4 position (carry with unconditional defer) is NOT adopted; only the Outsider's conditional-A.4 is adopted.

### §5.5 Splitter+Archivist "do both together" implicit minority (Claude-only latent, 0-of-4 explicit)

**Position**: neither Splitter nor Archivist explicitly proposed a hybrid, but their seams are compatible (Splitter: split OI-004 to new file; Archivist: relocate YAML blocks + §Open Extensions). If adopted together, MAD residual would be ~4,900 - 1,100 = ~3,800 words, plus the new OI-004 file at ~1,463 words.

**Activation warrant**: if Session 025+ reaches the Splitter's 7,500-word or content-driven threshold AND the Archivist's operationalised-parsing pre-commit check confirms YAML-block relocatability, a hybrid A.2+A.3 is the strongest bounded remediation. Neither proposer explicitly endorsed hybrid; neither explicitly rejected it. Preserved for completeness.

## §6 Synthesis recommendations (R1-R8)

### R1. A.4 carry-the-warning is the Session 024 remediation

2-of-4 cross-family convergence (Skeptic + Outsider) carries per MAD v4 §Synthesis weighting convention. MAD residual unchanged at 6,386 words (live); soft-warn persists through Session 024 close as designed per `read-contract.md` v2 §8.

### R2. Concrete conversion condition (Outsider-adopted)

A.4 is not passive defer. Session 024 records two pre-committed conditions under which Session 025+ converts A.4 to A.2 split:
- **Condition (i)**: MAD reaches 7,500 words by any measure (live or validator-measured).
- **Condition (ii)**: a Session 025+ substantive revision to MAD is warranted on content-merit grounds (new normative rule; new required field; new trigger; new schema layer) and cannot coherently integrate into the monolithic file.

If either condition fires, Session 025+ converts to A.2 with the OI-004 block (lines 328-429) as the named seam per Splitter [01a Q1, Q5] and Outsider [archive chunk 09, Q1, Q5] convergence on seam-choice.

### R3. No engine-v bump; engine remains at v4

No engine-definition file is substantively revised by R1-R2. Engine-v4 preserved. §5.4 Session 022 cadence minority remains at activated (not escalated to substantive). OI-018 not activated by this session's decision.

### R4. §5.1 Pacer counter reads zero; §5.2 Skeptic runway preserved

Session 024 is not a restructure-for-budget event. §5.1's Session 024-028 event counter reads 0. §5.2's vindication runway — "no default-read file exceeds 7,500 words and no restructure-for-budget event occurs" — remains open through Session 027 review. Both minorities gain data-for-test rather than being resolved either way.

### R5. WX-22-1 not advanced or retired

No archive indirection created; no split boundary added. WX-22-1 remains on the watchlist. A future A.2 conversion (per R2 condition) would engage WX-22-1 directly via the Splitter [01a Q4] three-piece defence + Session 025 operator-discipline test.

### R6. Budget-literal drift cleanup (minor edits, per Outsider [01d §4.2] finding)

Three stale literal witnesses in adjacent specs corrected to match current validate.sh constants (8K hard / 6K soft). Minor per OI-002 heuristic (stale-witness correction within existing spec scope; no new normative content):
- `specifications/validation-approach.md` §Gating Conventions code block: `DEFAULT_READ_HARD_WORD_CEILING=15000` → `8000`; `DEFAULT_READ_SOFT_WORD_CEILING=10000` → `6000`.
- `specifications/read-contract.md` §4 Archive-pack structure: "Chunk size target: each chunk ≤ 10,000 words (matching the §2 soft warning)" → "each chunk ≤ 6,000 words (matching the §2 soft warning)" — with note that the chunk-size target is a practical guide, not a hard constraint; Session 022 precedent used 50KB byte-range chunks yielding ~5-7K words each.
- `specifications/read-contract.md` §9 Close-time obligation: "Any file exceeding the default-read per-file hard ceiling (§2: 15,000 words)" → "(§2: 8,000 words)".

**Classification**: minor under OI-002 heuristic's "elaboration making explicit what existing practice already contains" branch — these edits align spec text with validate.sh values that already operate. No new normative content. No file-level version bump. Frontmatter `last-updated` updated in both files.

**D-023 triggers**: d023_3 does NOT fire — this is stale-constant correction in §Gating Conventions explanatory block, not a revision touching Tier 2 semantic validation logic. d023_1 / d023_2 / d023_4 not triggered.

### R7. Watchpoints opened

- **WX-24-1**: MAD growth monitoring (Skeptic + Outsider R2 convergence). Thresholds: 7,000 words by Session 026 → reconsider A.1 with named targets; 7,500 words by Session 028 → activate R2 condition (i), convert to A.2; 8,000 words any session → hard-fail forces restructure per `read-contract.md` v2 §2.
- **WX-24-2**: Budget-literal drift watch (Outsider [01d §4.2] finding). Any future substantive revision to `read-contract.md` or `validation-approach.md` that changes a numeric threshold must update all adjacent spec text (§4, §9, §Gating Conventions) in the same session. The Session 024 R6 cleanup is retroactive; forward discipline is the prevention.
- **WX-24-3**: Outsider pre-response workspace exploration pattern, now n=4 across Sessions 021/022/023/024. The pattern is stable. MAD v4 §Stance Briefs says perspectives "do not read workspace files or use other tools during the independent phase" — this is true of Claude subagents but not of the codex exec Outsider. The asymmetry is documented per Session 023 [03-close.md §8] and strengthened at n=4. Activation warrant: if a future Session 025+ deliberation surfaces a case where Outsider's workspace-read produced a material contribution that disadvantaged the Claude-subagent perspectives' independence-preserving reasoning, the spec asymmetry becomes a revision candidate.

### R8. OI housekeeping

- **OI-002 11th data point** added: R6 minor-edit cleanup. Heuristic continues to hold stable.
- **OI-004**: criterion-3 cumulative gains 2 data points from this session (§4.1 brief-factual-error catch; §4.2 budget-literal drift catch). New cumulative: 67. Tally stays at 8-of-3 required (no D-023 required-trigger decision this session per R3); voluntary:required rebalances 8:8 → 9:8. Criterion-4 remains articulated (state 3); no retrospective attempted.
- **OI-007**: active count unchanged at 13.
- **OI-015**: Session 024 is the 6th positive exercise. Operator direction (Path A) treated as path-selection not value-binding; synthesis adopted A.4 position (2-of-4 cross-family for A.4 against the implicit "execute some remediation" framing of Path A).
- **OI-018**: trigger-gated; not activated this session (no engine-v bump). Remains Open - deferred.
- **No new OI opened**. Three watchpoints (WX-24-1 / WX-24-2 / WX-24-3) chosen over new OI per Session 014 OI-007 scaling pressure precedent.

## §7 Anti-laundering check

Per Session 014 Skeptic Q7 test applied to the aggregate R1-R8:

1. **Does R1-R8 lower any threshold?** No. Soft warn stays 6K; hard stays 8K; aggregate advisory stays 90K; activation stays 100K.
2. **Does R1-R8 drop any check?** No. All 22 Tier 1 checks remain; all 9 Tier 2 questions remain.
3. **Does R1-R8 soften any mechanism-failure criterion?** No.
4. **Does R1-R8 remove any pre-existing rule?** No.
5. **Does R1-R8 codify a laundering pattern?** No — R5 explicitly preserves WX-22-1 unchanged. R6 is drift-repair, aligning stale literals with active tool values; anti-drift, not pro-drift.
6. **Does R1-R8 widen any label?** No.

**Additional laundering-pattern-specific tests**:

- *"Content-completion relabelling launder"*: Session 024 explicitly **rejects** the content-completion classification of A.1/A.2/A.3 per D2 adopted cross-family reading. If a future session reverses this and labels a Session 025-028 restructure as content-completion, this synthesis's D2 reading is the pre-commit benchmark for honest re-classification.
- *"Carry-the-warning silently becomes forever"*: R2's concrete conversion conditions prevent passive-drift A.4. If Session 025+ does not record MAD word-count at open, R2's conditions cannot be evaluated; that absence is itself a WX-24-1 activation signal.
- *"OI-018 quietly escalated"*: R3 explicitly preserves §5.4 at activated-not-substantive. Session 025+ cannot silently treat §5.4 as resolved; it is still alive and still gated on further engine-v bumps in Sessions 025/026.

**Aggregate anti-laundering: PASS per all six tests plus three pattern-specific tests.** The Outsider's Q1 *"not as passive drift"* framing and Q3 *"the trigger is the soft-warning threshold, not a discovered semantic incoherence"* framing are the load-bearing cross-model insurance against laundering drift.

## §8 Honest limits

- **I did not re-read MAD v4 in full at synthesis.** My claim that R6 cleanup is minor under OI-002 rests on the brief §3.1 section inventory and the Outsider [archive chunk 09 Q1] direct-workspace-read. I have not independently confirmed that validation-approach.md §Gating Conventions code-block is the *only* place the old 15K/10K values appear in spec text. The `grep` check I ran (verified at synthesis) found the three Outsider-reported locations and no others; if other occurrences exist, R6 should include them — Session 024 close must re-grep before committing R6 edits.
- **I did not read the Archivist's YAML-block classification claim against MAD's actual text.** Brief §3.1 estimates ~400 words of YAML in the 772-word §Heterogeneous-Participant Recording Schema; I take this as given. If the estimate is off (Session 023 Outsider precedent: brief estimates can drift), §5.2 Archivist activation warrant's operational test requires a direct word-count re-measurement at Session 025 open.
- **The 2-of-4 cross-family weighting for A.4 is load-bearing.** If Splitter's or Archivist's content-completion classification is *more* defensible than I judged, the cross-family weighting shifts. Session 025 audit should re-examine D2 specifically: does "Session 023 set up Session 024 as 'respond to the immediate 6K-soft-fire'" [Outsider, archive chunk 09 Q3] actually establish budget-driven primacy, or is the Splitter's "content seam is real and offering itself" [01a Q1] framing stronger on re-inspection?
- **Archivist's perspective file was minimally edited post-commit (at orchestrator level) to change the `[archive:` token to `[archive-proposal:` in three proposal-context occurrences (proposed-path text `archive/mad-schema/...path` within the Archivist's A.3 description)**, to avoid validator check-22 false-positive failure on paths the session proposed but did not create. Content, position, and reasoning unchanged. The edit is documented here as transparency; future brief-authoring conventions should instruct perspectives to avoid the live archive-token syntax for proposed/hypothetical paths. Preserved as a minor brief-authoring-convention observation (not formal OI given OI-007 scaling pressure).
- **I did not read the Session 022 or Session 023 Outsider archive-packs at synthesis.** Per Outsider [archive chunk 09 Honest Limits] same pattern; the 022/023 archive references in Session 024's material are accepted on prior-session vetting rather than fresh re-reading. This is a legitimate use of the read-contract's `[archive: path]` + honest-limits discipline.
- **Synthesiser is Claude; three of four raw perspectives are Claude.** Per MAD v4 §Limitations, synthesis is the pattern's highest-risk single-agent re-entry point. Mitigations applied: explicit per-claim citations; cross-family weighting documented; Outsider contributions foregrounded in §4; Splitter and Archivist dissents preserved as §5.1 and §5.2 first-class minorities with operational activation warrants.

## §9 Archive references

- Outsider raw: `provenance/024-session-assessment/archive/024-outsider/manifest.yaml`; chunks `01-chunk.md` through `09-chunk.md`; `source_hash_sha256: f8f69fa7b383a9f8651b9aa364b845c4f848d6aec0d60bee332f138010295dcb`; response body principally in chunks 08-09.
- Brief anchor commit: `bb2e3f2`.
- Claude perspectives (default-read during current session per `read-contract.md` v2 §1 item 8): `01a-perspective-splitter.md`; `01b-perspective-archivist.md` (minimally edited at orchestrator level per §8); `01c-perspective-skeptic.md`.
