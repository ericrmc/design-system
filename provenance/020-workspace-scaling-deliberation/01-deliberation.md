---
session: 020
title: Synthesis — Workspace Scaling Deliberation
date: 2026-04-22
status: complete
synthesizer: Claude Opus 4.7 (orchestrating agent)
participants_family: cross-model
cross_model: true
non_claude_participants: 1
deliberation_anchor_commit: c4025d5
---

# Synthesis — Session 020 Deliberation

## 1. Participants

Four perspectives, four raw outputs committed verbatim:

| Perspective | File | Participant kind | Model | Stance |
|---|---|---|---|---|
| Splitter | `01a-perspective-splitter.md` | claude-subagent | claude-opus-4-7 | Split both files; engine-v2; structural fix is prior |
| Tooler | `01b-perspective-tooler.md` | claude-subagent | claude-opus-4-7 | mempalace orchestrator-convenience-only via CLAUDE.md; no engine change; hands-on testing recorded |
| Skeptic | `01c-perspective-skeptic.md` | claude-subagent | claude-opus-4-7 | Defer structural change; minor SESSION-LOG spec clarification; OI-007 monitoring annotation; engine-v1 preserved |
| Outsider | `01d-perspective-outsider.md` | non-anthropic-model | gpt-5.4 | Frame-challenge: indexes drifted to dossiers; restore to true-index shape first; split only if still unwieldy after restoration; mempalace optional-only |

Full manifests at `manifests/*.manifest.yaml`.

## 2. Position map across Q1–Q8

### Q1 — Friction load-bearing or cosmetic?

- **Splitter** [01a Q1]: Load-bearing. "No information loss on this audit" is a post-hoc pass on narrow question-set, not a predictive test. Names three at-risk methodology properties (Absorb integrity; audit-reconstruction fidelity; genesis-provenance legibility).
- **Tooler** [01b Q1]: Real but narrow. "Adequacy-today, not safety-forward." Names three risks (cross-session provenance traversal; audit fidelity; OI continuity).
- **Skeptic** [01c Q1]: Currently cosmetic. Future-load-bearing risk speculative. "The timing correlates suspiciously with orchestrator friction, not with demonstrated methodology degradation."
- **Outsider** [01d Q1]: **Frame-challenge.** The primary problem is not "file size exceeded ceiling" — it is that two artifacts specified as *indexes* have drifted toward *dossiers*. The load-bearing property is type-integrity, not retrievability.

**Convergences:** 3-of-4 (Splitter + Tooler + Outsider) agree friction is at least somewhat real; Skeptic alone says cosmetic-now.

**Cross-family composition of the 3-of-4:** 2 Claude + 1 non-Claude (cross-family affirmative). Skeptic's minority is single-family (Claude).

**Outsider's frame-challenge is the Session 017 precedent pattern** — a non-Claude perspective reframing the question rather than picking a Claude-originated option. Session 017's Outsider originated H4 (layered model) rejecting H1/H2/H3. Session 020's Outsider originates "type drift" diagnosis rejecting "scaling" framing.

### Q2 — open-issues.md structure

- **Splitter** [01a Q2]: **Split-by-identity** (per-OI files + thin index + `resolved/` subdir). Substantive revision; engine-v1 → engine-v2. Draft spec text provided.
- **Tooler** [01b Q2]: **Not my proposal.** Separation: specs describe content, tools retrieve it. File-split orthogonal to tool adoption; either can exist without the other.
- **Skeptic** [01c Q2]: **Reject split.** Single-file Read shows all 12 OIs at once; per-OI files increase risk of forgotten OIs. Propose annotation to OI-007 adding per-OI-annotation-size as second monitoring dimension. No spec change.
- **Outsider** [01d Q2]: **Not yet.** First restore `open-issues.md` to brief-index form per current spec. If still unwieldy after restoration, split-by-identity with thin index is the right shape. Draft text provided for future engine-v2 if warranted.

**Convergences:**
- **3-of-4 against split-NOW** (Tooler orthogonal; Skeptic defer; Outsider defer-after-restore). 1-of-4 for split-now (Splitter).
- **Outsider + Splitter agree on the shape if split happens** (per-OI + thin index), disagreeing only on timing.

**Cross-family composition of the 3-of-4:** 2 Claude (Tooler + Skeptic) + 1 non-Claude (Outsider). Cross-family affirmative against split-now.

### Q3 — SESSION-LOG.md structure

- **Splitter** [01a Q3]: **Per-session files + index** (`session-log/NNN-<slug>.md`). Each session file carries current paragraph content; SESSION-LOG.md becomes one-row-per-session index. Substantive; engine-v2. Draft spec text provided.
- **Tooler** [01b Q3]: **Keep as-is.** Content drift is a separate question from retrievability. Paragraph entries "earn their keep" per Q7. One-word edit to "summary" acceptable.
- **Skeptic** [01c Q3]: **Minor amendment only.** Change "brief note" to "summary" + add one sentence about variance scaling to session complexity. Minor per OI-002 ("makes explicit what existing practice already contains"). No v-bump. Draft text provided.
- **Outsider** [01d Q3]: **Restore to one-line genuine brief.** SESSION-LOG is specified as *index*; provenance `03-close.md` is canonical detail. Rewrite entries back to short index lines. Do not create per-session files. Paragraph drift is discipline failure, not genuine need.

**Divergences:** 4-way divergence on shape.

**Convergences:**
- Splitter + Tooler + Skeptic agree paragraph content is load-bearing (Q7 (c)). Outsider alone argues Q7 (b) discipline-failure + (c)-is-false.
- Tooler + Skeptic + Outsider all agree no structural split (keep SESSION-LOG.md as single file) — though with different rationales.
- Skeptic + Outsider both propose minor amendments; the amendments differ in *direction* (Skeptic ratifies "summary" drift; Outsider restores to "brief" intent).

**Cross-family analysis:** The single-file preservation is 3-of-4 cross-family (Tooler + Skeptic + Outsider vs Splitter). But the content direction splits: Splitter + Tooler + Skeptic agree content-preservation (3-of-3 Claude) vs Outsider alone for content-restoration (1-of-1 non-Claude). This Q3 is the **one question where cross-family and same-family compositions point in opposite directions**.

### Q4 — mempalace adoption

- **Splitter** [01a Q4]: Orthogonal to structural fix; tool and structure address different failure modes.
- **Tooler** [01b Q4]: **Orchestrator-convenience-only adoption.** CLAUDE.md entry (not engine-manifest.md §3). Classified analogous to `gemini`/`codex`. Draft text provided. Hands-on findings surface three critical caveats:
  - Search is semantic/vector, not "exact words" as help text claims (`D-074` query returned zero D-074 results).
  - Wake-up is drawer-count-dominated, not recency-weighted.
  - Mine does not dedupe versioned specs (`-v2.md` surfaces above `.md`).
- **Skeptic** [01c Q4]: **Defer entirely.** Engine is Markdown + one shell script; that minimal surface is load-bearing for external-application portability. Even orchestrator-convenience adoption introduces cognitive load (two retrieval mechanisms).
- **Outsider** [01d Q4]: **Optional retrieval helper; not substitute; not engine-definition dependency.** "If unavailable in CI, a fresh clone, or an external application workspace, the engine should still function. That strongly argues against making it part of engine load."

**Convergences:**
- **4-of-4 against mempalace as engine-definition.** No perspective supports adding mempalace to `engine-manifest.md` §3.
- **2-of-4 cross-family for some form of orchestrator-convenience use** (Tooler Claude + Outsider non-Claude). Tooler proposes concrete CLAUDE.md paragraph; Outsider permits optional use without formal recording.
- **1-of-4 against any use** (Skeptic Claude defer-entirely).
- **Hands-on empirical evidence from Tooler is decisive:** mempalace's self-description as "exact words" search is misleading; the tool is candidate-discovery only, not authoritative lookup. This changes the calculus from "the operator named a turnkey fix" to "the operator named a tool that requires understood limits."

**Cross-family composition of the 2-of-4 for orchestrator-convenience use:** 1 Claude (Tooler) + 1 non-Claude (Outsider). Affirmative cross-family for permissive-use; single-family Claude minority (Skeptic) for defer-entirely.

### Q5 — Interaction between Q2, Q3, Q4

- **Splitter** [01a Q5]: Structural fix (Q2+Q3) necessary; tool (Q4) optional enhancement. Minimum-viable = Q2+Q3.
- **Tooler** [01b Q5]: Orthogonal surfaces. Minimum-viable with smallest surface = Q4 alone. Structural fix is irreversible; tool adoption is reversible.
- **Skeptic** [01c Q5]: "Each adopted surface weakens the defer-case for the others." Minimum-change set = Q3 minor amendment + Q2 OI-007 annotation; no Q4.
- **Outsider** [01d Q5]: **Strict sequential order.** First restore true-index shape (content normalisation). If still unwieldy, then split. Tool remains optional on top. Minimum-viable = content normalisation, not tool and not spec rewrite.

**Divergence on minimum-viable-change is 4-way.**

**Convergence on "structural and tool surfaces are not substitutes"** — even the disagreeing parties acknowledge that fixing one does not remove the question of the other.

### Q6 — Engine-version impact

- **Splitter** [01a Q6]: engine-v2 warranted. Q2 and Q3 are substantive. Version-bump-aversion is not a methodology value.
- **Tooler** [01b Q6]: **No v-bump.** CLAUDE.md is not engine-definition. Optional one-sentence spec elaboration pointing to CLAUDE.md would be minor (not required).
- **Skeptic** [01c Q6]: **No v-bump.** The minor amendment (Q3) is elaboration within existing scope per OI-002. Strongest defer-leverage: any splitter/tooler proposal that adds normative content triggers engine-v2 prematurely. engine-v1 has not yet been exercised by external application.
- **Outsider** [01d Q6]: **No v-bump yet.** Content normalisation is corrective maintenance, not substantive definition change. Directory creation would be substantive but only justified after restoration fails.

**Convergences:** **3-of-4 cross-family against engine-v2 bump now** (Tooler Claude + Skeptic Claude + Outsider non-Claude vs Splitter Claude). This is the strongest cross-family signal of the session on a direct decision question.

**Cross-family composition:** 2 Claude + 1 non-Claude affirmative against; 1 Claude for. Cross-family majority against.

### Q7 — SESSION-LOG drift interpretation

Three options: (a) original intent inadequate; (b) discipline failure; (c) genuine informational need.

- **Splitter** [01a Q7]: **(c) + some (b).** Paragraphs carry load-bearing content; drift happened without deliberation.
- **Tooler** [01b Q7]: **(a) + (c) dominate.** Paragraphs earn their keep; "brief note" was authored before complexity grew.
- **Skeptic** [01c Q7]: **(c) with bounded drift.** Paragraph length correlates with session complexity; evidence favours ratification not correction.
- **Outsider** [01d Q7]: **(b) discipline-failure.** Paragraph content does not belong in scan surface by default; provenance carries detail.

**Convergence:** 3-of-4 for reading (c) as at least part of the interpretation (Splitter + Tooler + Skeptic, all Claude). **1-of-4 for reading (b) as primary** (Outsider non-Claude).

This is the **second question where same-family and cross-family compositions point in opposite directions** (Q3 is the first). The Claude perspectives read the drift as evidentially earned (paragraph content serves Read); the non-Claude perspective reads the same evidence as type drift (paragraphs in wrong location; 03-close.md should carry detail).

### Q8 — Anti-laundering

All four perspectives applied the Session 014 Skeptic Q7 test; all four passed their own self-test. Falsifier thresholds stated per Session 015/019 Minimalist precedent:

- **Splitter** [01a Q8]: Falsifiers on Q2 (at 50-session horizon, files remain single-readable), on Q3 (session 30 SESSION-LOG single-read). Both unlikely per trajectory.
- **Tooler** [01b Q8]: Withdraws proposal if any two of: laundered citation; index drift with missed finding; external-application friction absent tool; mempalace deprecation.
- **Skeptic** [01c Q8]: Four falsifiers (F1 reasoning error from segment-read; F2 OI housekeeping failure; F3 SESSION-LOG entry >12K chars without complexity; F4 decision error from absence of semantic search).
- **Outsider** [01d Q8]: Falsifier: if after restoring to brief-index form, either file still exceeds ceiling, OR two consecutive sessions require multi-segment reads for orientation, OR provenance 03-close.md proves insufficient as detail-carrier.

**Accommodation pressures named by perspectives:**

- Splitter: cross-OI visibility loss; per-file bloat migration
- Tooler: orchestrator-discipline-dependent mitigation (strongest pressure); hidden indexing-as-Read-substitute drift (unfalsifiable without metric)
- Skeptic: n=1 → systemic revision without intervening demonstrated failure
- Outsider: "brief" becoming euphemism for unrecoverable deletion; compression-as-deletion

**Aggregate anti-laundering check:** Every perspective identified a specific pressure in its own proposal and articulated a mitigation. The patterns diverge, but the discipline is applied consistently across perspectives. This is the fourth consecutive session with strong anti-laundering reflexes across all perspectives (Sessions 014/017/019 precedent).

## 3. Divergences

Three divergences are not resolved by convergence; they are presented to the adoption decision as explicit forks.

### 3.1 — Content direction on SESSION-LOG.md

- **Splitter** + **Tooler** + **Skeptic**: paragraph content earns keep, varying on whether to preserve (Tooler), ratify (Skeptic), or relocate (Splitter).
- **Outsider**: paragraph content does not belong in index file at all; restore to brief.

**Synthesis resolution:** Adopt Skeptic's minor amendment to `workspace-structure.md` ("brief note" → "summary" + variance clause). This is the **smallest-viable change** that addresses operator's named blocker (both files exceed read ceiling) without (a) engine-v2 bump, (b) re-writing 19 historical entries, (c) creating a new directory. The Outsider's type-drift diagnosis is **preserved as first-class minority** with operational warrant: if future sessions' SESSION-LOG entries grow further or the "detail already in provenance" principle is found to be false (i.e., provenance 03-close.md does not in practice preserve what entries claim), the restoration direction is vindicated. The Splitter per-session-directory proposal is **preserved as first-class minority** with operational warrant: if after Session 020's amendment SESSION-LOG.md still exceeds single-read ceiling within 5 sessions or Skeptic's F3 (entry >12K chars without complexity) fires.

### 3.2 — mempalace orchestrator-convenience adoption

- **Tooler** + **Outsider**: permissive orchestrator-convenience use (Tooler: concrete CLAUDE.md paragraph; Outsider: optional).
- **Skeptic**: defer entirely.
- **Splitter**: orthogonal (no position for or against).

**Synthesis resolution:** Adopt Tooler's CLAUDE.md paragraph **with the hands-on caveats baked in explicitly**. mempalace is orchestrator-convenience-only, not engine-definition. The CLAUDE.md paragraph records:
- Candidate-discovery role (not authoritative lookup).
- Search is semantic not exact-words despite help text (per hands-on Tooler finding).
- Re-confirm via Read before citing.
- `mempalace.yaml` and `entities.json` are gitignored if created.
- Fresh-clone and external-application workspaces operate without mempalace.

Skeptic's **defer-entirely minority** is preserved with operational warrant: if within 3 sessions mempalace is not used substantively, or if any "search laundering" incident occurs (orchestrator cites mempalace output not verifiable in source), the CLAUDE.md paragraph is candidate for removal.

### 3.3 — Engine-v2 bump vs preservation

- **Splitter**: engine-v2 warranted.
- **Tooler** + **Skeptic** + **Outsider**: engine-v1 preserved.

**Synthesis resolution:** 3-of-4 cross-family convergence against bump. Engine-v1 preserved. The Splitter's engine-v2 **minority is preserved** with operational warrant: if Skeptic's F1, F2, or Splitter's own Q8 falsifiers (file ceiling persistently exceeded within 5-session horizon) fire, the engine-v2 revision direction is vindicated.

## 4. Specific adopted revisions (R1–R3)

### R1 — Minor amendment to `workspace-structure.md` §SESSION-LOG.md (Skeptic Q3)

Current text:
> A running index of sessions for quick orientation. Each entry is one line containing the session number, date, title, and a brief note on what was accomplished. This file is updated at the close of each session.

Replacement text:
> A running index of sessions for quick orientation. Each entry is one line (one Markdown table row) containing the session number, date, title, and a summary of what was accomplished. The summary length scales to session complexity: planning-only, single-perspective, or assessment-only sessions produce shorter summaries; deliberation sessions producing substantive spec revisions, cross-model influences, or external artefacts produce longer summaries calibrated to record the decision surface and load-bearing influences. The canonical detail for each session lives in its provenance `03-close.md` file; the SESSION-LOG entry is an index over that detail, not a replacement. This file is updated at the close of each session.

**Classification per OI-002 heuristic:** **Minor.** The change (a) makes explicit what existing practice already contains (drift from "brief" to "summary" was already happening under current spec without violation of "one line per entry"), (b) names the variance pattern already observable, (c) points to existing canonical-detail location (03-close.md) without requiring relocation of any content, (d) adds no new rules, required fields, severity decisions, gating rules, triggers, or required artefacts. Analogous to Session 002 D-014 precedent and Session 017 minor scope-clarification sentences.

**Engine-version impact:** **No v-bump.** Minor elaboration within existing spec scope per engine-manifest.md §5. engine-v1 preserved.

### R2 — OI-007 monitoring-dimension annotation in `open-issues.md` (Skeptic Q2)

Add Session 020 annotation to existing OI-007 entry:

> **Session 020 annotation (monitor, no format change).** Session 020 open observed that `open-issues.md` now exceeds the 25,000-token single-read ceiling, driven by per-OI annotation accretion (OI-004 ~8 KB; OI-016 ~5 KB) rather than by issue count (still 12). The count-based argument ("count oscillates between 12–13; format scales adequately") continues to hold on the count axis. A second monitoring dimension (per-OI annotation size vs single-read ceiling) is added. Session 020 deliberation adopted no format change from this observation alone per Session 019 Minimalist defer-precedent applied to structural (not content) friction. A directory split per the workspace-structure.md "unless unwieldy" clause is preserved as first-class Splitter minority (see §5 below) with operational warrant: activated if (a) OI-housekeeping incorrect because segment-read missed a cross-reference in not-loaded segment, (b) two consecutive sessions' OI count tallies disagree with git history, or (c) `open-issues.md` exceeds 50,000 tokens (i.e., requires more than two segment-reads for full traversal). Monitoring continues.

**Classification:** This is an open-issues.md annotation, not a workspace-structure.md revision. No spec change. Pure development-provenance update.

**Engine-version impact:** None. engine-v1 preserved.

### R3 — CLAUDE.md orchestrator-convenience mempalace paragraph (Tooler Q4, hands-on-grounded)

Add to existing CLAUDE.md §Tools section:

> #### mempalace (orchestrator-convenience, non-engine)
>
> `mempalace` v3.1.0 is installed via `uv tool`. It is classified as orchestrator-convenience tooling, analogous to the `gemini`/`codex` CLIs. **It is NOT part of `engine-manifest.md` §3 and is NOT required by any specification.** External-application workspaces loading the engine do not inherit the dependency; fresh clones of this workspace can operate without it.
>
> Suggested use: when a single Read would exceed the 25,000-token ceiling (SESSION-LOG.md, open-issues.md, aggregated provenance search), orchestrators may run `mempalace search "<query>" --wing complex-systems-engine` or `mempalace wake-up --wing complex-systems-engine` to retrieve candidate matches.
>
> **Critical caveats (per Session 020 hands-on finding):**
> - Despite the `mempalace --help` description ("Find anything, exact words"), `search` is semantic/vector-ranked, not exact-string match. Exact-string queries like `D-074` may return zero results containing that string even when the string exists in indexed files. Use explicit Grep for exact-string verification.
> - `wake-up` output is drawer-count-dominated rather than recency-weighted; it is useful for fresh-session priming but does not substitute for reading SESSION-LOG.md.
> - `mine` does not deduplicate versioned specs — superseded `-v2.md` / `-v3.md` files are indexed alongside current canonical files and may rank above them.
> - mempalace output is **candidate-discovery only.** Every cited claim must be reconfirmed against the source file via Read before inclusion in session artefacts. Treating mempalace output as authoritative is the laundering risk (OI-015-adjacent).
>
> Initialisation (one-time): `mempalace init . && mempalace mine .` in workspace root. The init creates `mempalace.yaml` + `entities.json` in the workspace root — add both to `.gitignore`. The palace state itself lives at `~/.mempalace/palace/`, outside the workspace.
>
> Re-mine cadence: manual, typically at session close after substantive file changes. Not a spec requirement; orchestrators not using mempalace need not re-mine.

**Classification:** CLAUDE.md amendment. CLAUDE.md is project-instructions (checked into the codebase per opening tag) but **is not in engine-manifest.md §3** — it is a workspace-level operator-and-orchestrator convention file, not engine-definition. CLAUDE.md has been revised before without spec-level consequence (Session 016 recorded `uv tool` authorisation; this extends that pattern).

**Engine-version impact:** None. engine-v1 preserved.

## 5. Preserved first-class minorities

Four minorities preserved with operational warrants. Each minority has specific text or shape; each has a concrete activation trigger.

### 5.1 — Splitter per-OI directory for `open-issues.md` (Session 020, 01a Q2)

**Position.** When `open-issues.md` exceeds single-read ceiling or exhibits OI-housekeeping discipline failure, split into `open-issues/OI-<id>-<slug>.md` per-issue files + thin index + `resolved/` subdir. Substantive engine-v1 → engine-v2 revision.

**Operational warrant.** Minority is vindicated and becomes preferred revision direction if any of: (a) future session's OI-housekeeping task completes incorrectly because a segment-read missed a relevant cross-reference in a not-loaded segment of `open-issues.md`; (b) two consecutive sessions' OI count tallies disagree with git history because of segment-read undercount; (c) `open-issues.md` exceeds 50,000 tokens (requires >2 segment-reads for full traversal).

### 5.2 — Splitter per-session files for SESSION-LOG.md (Session 020, 01a Q3)

**Position.** When SESSION-LOG.md cannot be single-read and the R1 amendment's variance-clause proves insufficient bounding, split into `session-log/NNN-<slug>.md` per-session files + thin index. Substantive engine-v1 → engine-v2 revision.

**Operational warrant.** Minority is vindicated and becomes preferred revision direction if any of: (a) after R1 adoption, a session's SESSION-LOG entry exceeds 12,000 characters without corresponding session complexity (Skeptic's F3 falsifier); (b) SESSION-LOG.md exceeds single-read ceiling within 5 sessions of R1 adoption (i.e., by Session 025); (c) a session records a specific reasoning error traceable to segmented SESSION-LOG read (Skeptic's F1 falsifier).

### 5.3 — Outsider type-drift diagnosis / restore-to-true-index (Session 020, 01d Q1–Q3)

**Position.** Both SESSION-LOG.md and open-issues.md are specified as *indexes* and have drifted toward *dossiers*. The correct remedy is to restore both files to brief-index form (not ratify drift, not split), with provenance `03-close.md` and per-OI sessions carrying canonical detail. R1 is a ratification-direction minor amendment; the restoration-direction would have been an in-place rewrite of existing entries back to index brevity.

**Operational warrant.** Minority is vindicated and becomes preferred revision direction if any of: (a) after R1 adoption, a session cites SESSION-LOG as primary source while 03-close.md exists and carries the same content (i.e., citation laundering detected); (b) the R1 variance-clause ("summary length scales to session complexity") is invoked as permission for an unwarrantedly long entry that does not correspond to complexity by decision count or artefact count; (c) within 5 sessions of R1, SESSION-LOG.md exceeds single-read ceiling despite the variance-clause (i.e., ratification proves unbounded).

### 5.4 — Skeptic defer-entirely on tools (Session 020, 01c Q4)

**Position.** No mempalace adoption in any form, including CLAUDE.md. The engine is Markdown + one shell script; even orchestrator-convenience adoption introduces cognitive load (two retrieval mechanisms) and version drift surface. The minimal-surface principle dominates.

**Operational warrant.** Minority is vindicated and becomes preferred direction if any of: (a) within 3 sessions of R3 adoption, mempalace is not used substantively (indicating the tool was not actually needed); (b) any "search laundering" incident occurs — orchestrator cites mempalace output not verifiable against source file via Read; (c) mempalace version drift causes silent index staleness resulting in a missed session finding; (d) external-application workspaces report confusion from the "CLAUDE.md tool reference but no engine requirement" pattern.

## 6. Adoption summary

### 6.1 — Adopted (3-of-4 cross-family majority)

- R1: Minor amendment to `workspace-structure.md` §SESSION-LOG.md. Ratifies "summary" variance. No v-bump. Classified minor per OI-002 heuristic.
- R2: OI-007 monitoring-dimension annotation in `open-issues.md`. No spec change.
- R3: CLAUDE.md orchestrator-convenience mempalace paragraph with hands-on caveats. No engine-definition change.
- Engine-v1 preserved (3-of-4 cross-family for no bump).
- mempalace NOT in engine-manifest.md §3 (4-of-4 convergence).
- open-issues.md structure unchanged (3-of-4 against split-now).
- SESSION-LOG.md structure unchanged (3-of-4 against split; 4th way of restore preserved as minority).

### 6.2 — Not adopted (preserved as minorities)

- Splitter per-OI directory for open-issues.md (§5.1)
- Splitter per-session directory for SESSION-LOG.md (§5.2)
- Outsider restore-to-brief-index direction (§5.3)
- Skeptic defer-entirely on mempalace (§5.4)

### 6.3 — Cross-family weighting check

**Macro-question "no engine-v2 bump":** 3-of-4 cross-family (Tooler Claude + Skeptic Claude + Outsider non-Claude vs Splitter Claude). Both families affirmative on preservation side. Non-Claude presence is substantive, not coincidental — Outsider's position rests on the type-drift frame-challenge which no Claude perspective produced.

**Macro-question "no structural split now":** 3-of-4 cross-family (Tooler + Skeptic + Outsider vs Splitter). Both families on preservation side.

**Macro-question "mempalace not engine-definition":** 4-of-4 all families. Unambiguous.

**Session 019 close's caveat on cross-family macro-vs-specific distinction applies here too:** the 3-of-4 on macro engine-v1 preservation does not transfer automatically to specific content choices (R1's amendment text is Skeptic-authored, not cross-family derived; R3's paragraph is Tooler-authored with hands-on findings baked in). The adoption decision is defensible at the macro level; specific text credits are attributed to authoring perspective.

## 7. Cross-model contributions (per v3 §Closure Criteria criterion 3)

**Five concrete Outsider-sourced contributions materially shaped adopted content:**

1. **Frame-challenge "indexes drifted to dossiers" diagnosis** [01d Q1]. Reframes the problem from file-size-scaling to role-confusion. Shapes R3's "canonical detail in 03-close.md" pointer added to R1 amendment text. No Claude perspective produced this diagnosis. **First frame-replacement contribution since Session 017.**

2. **"Scan surface vs detail surface" separation principle** [01d Q1]. Shapes R1 amendment's closing sentence pointing at 03-close.md as canonical-detail location. Claude perspectives treated SESSION-LOG as single-purpose; Outsider named the dual-role and made the location explicit.

3. **Strict-sequential minimum-viable-change ordering** [01d Q5]. "First, restore both root files to true index shape. Then split if still unwieldy. Then tool optional." This ordering shapes the §5 minorities' activation triggers (restoration is preferred direction before split-direction under certain empirical conditions).

4. **Portability-loss argument against engine-definition tool adoption** [01d Q4]. "If the tool is unavailable in CI, a fresh clone, or an external application workspace, the engine should still function." This argument (cross-family independent from Skeptic's Markdown-+-shell-script argument) shapes R3's explicit non-engine-definition classification and the "external-application workspaces do not inherit the dependency" text.

5. **Semantic-retrieval staleness general concern** [01d Q4]. "Semantic retrieval tools often improve speed while weakening guaranteed recall, especially for negative evidence and edge cases." This pretraining-sourced observation (surfaced per brief §10 as input, not fact) is corroborated by Tooler's hands-on finding that `D-074` query returned zero D-074 results — independent cross-family arrival at the same concern from different reasoning paths.

**Criterion-3 cumulative:** 50 (through Session 019) + 5 (Session 020) = **55** across Sessions 005–020.

**Notable Outsider contribution genre (new data point for OI-004 closure deliberation):** Session 020 Outsider produced **frame-replacement** (type drift) similar to Session 017 (H4 layered model). This is the **second frame-replacement contribution** after Session 017 and extends WX-11-3 pattern — prior contributions resolved within-frame disagreements via third-ways; Sessions 017 and 020 reject the frame itself. Two instances across sessions establish frame-replacement as a distinct Outsider contribution kind worth naming.

## 8. Brief-priming check

**Inspection of all four raw outputs for vocabulary echo from brief.**

- Splitter: used "split-by-identity", "Absorb integrity", "audit-reconstruction fidelity", "genesis-provenance legibility" — all Splitter-originated; brief's vocabulary ("per-OI files", "split by status", "split by family") cited not echoed.
- Tooler: used "orchestrator-convenience-only", "candidate-discovery", "pointer-generator" — Tooler-originated; brief's vocabulary ("mempalace adoption", "orchestrator convenience") extended with specific caveats from hands-on testing.
- Skeptic: used "monitoring-dimension", "bounded drift", "accommodation pressure", "category confusion" — Skeptic-originated; brief's vocabulary cited not echoed; inheritance from Session 019 Minimalist explicit per instruction in brief §8.
- Outsider: used "type drift", "index vs dossier", "scan surface vs detail surface", "discipline failure plus type confusion" — Outsider-originated; brief's vocabulary ("file-scaling", "directory-split") cited not echoed.

**Verdict:** No brief-priming detected. Perspectives produced independent framings of the same empirical substrate. **Brief-priming-absent for tenth consecutive session.**

## 9. Adoption recommendation

The synthesizer recommends adopting R1, R2, R3 together per §6. The recommendation rests on:

- 3-of-4 cross-family convergence on engine-v1 preservation.
- 3-of-4 against structural split of either file at Session 020.
- 4-of-4 convergence against mempalace engine-definition.
- Four preserved first-class minorities with concrete operational warrants that can activate in future sessions.
- Minimum-viable-change shape: two spec-adjacent changes (one minor amendment to engine-definition; one CLAUDE.md paragraph) + one open-issues annotation. No new directories. No engine-version bump. No tool dependency added to engine.

The Outsider's frame-challenge is the session's strongest single cross-family contribution; it is **preserved as a first-class minority rather than converted to main adopted text** because (a) retrospective re-writing of 19 session entries and 12 OI bodies is not minimum-viable-change, (b) the existing provenance 03-close.md files already carry canonical detail per Outsider's own diagnosis, so R1's pointer to them operationalises the Outsider position without the aggressive rewrite. If the Outsider's diagnosis proves further vindicated by Session 021+ observations, the §5.3 operational warrant activates and restoration-direction becomes the preferred Session 022+ revision path.

The Splitter minorities (§5.1, §5.2) are the fallback revision directions if Session 021–025 observations demonstrate R1/R2/R3 insufficient. The activation thresholds are specific and observable.

The Skeptic defer-entirely minority (§5.4) is the rollback direction for R3 if mempalace proves unused or laundering-prone.

## 10. Expected decision triggers

**D-080** (adopts R1-R3): `[d016_2]` fires for the R1 minor amendment to workspace-structure.md (spec revision, albeit minor). Note: d016_2's triggering is for *substantive* revisions per Check 14 validation rubric — minor revisions do not fire d016_2 per OI-002 precedent. **Re-check this at decision authoring.**

Actually per validate.sh Check 14 schema, `d016_2` fires on "substantive spec creation/revision." R1 is minor per OI-002 heuristic (elaboration within existing scope). d016_2 does NOT fire for minor amendments per Sessions 005/006/017 precedent. R1 classification is minor → d016_2 does not fire.

R2 is an open-issues.md annotation (development-provenance), not a spec revision. No d016_* fires.

R3 is a CLAUDE.md amendment. CLAUDE.md is not in engine-manifest.md §3. **Not a spec revision. No d016_* fires.**

However, R1 is a reasonable-disagreement deliberation that synthesises multi-perspective positions into spec amendment text, which is the classic d016_3 trigger. **d016_3 likely fires.**

No d023_* fires: no kernel revision, no multi-agent-deliberation.md revision, no validation-approach.md Tier 2 revision, no OI-004 state change asserted.

**D-080 expected triggers: `[d016_3]`.**

**D-081** (OI state housekeeping): records OI-002 9th data point (R1 minor amendment classification), OI-004 tally (unchanged at 6-of-3; voluntary:required 7:6), OI-007 R2 annotation formalisation.

**D-081 expected triggers: `[none]`** per D-073/D-077/D-079 housekeeping precedent.

## 11. Synthesizer's anti-laundering check on own synthesis

**Session 014 Skeptic Q7 test applied to the §6 adoption.**

Does the adoption widen what counts as pass?

- R1 widens "brief note" → "summary" with a variance clause. Widening acknowledged in §3.1. Bounding is the variance-clause's mention of legitimate sources (session complexity). Falsifier: F3 (entry >12K chars without complexity). **Widening bounded; falsifier observable.**
- R2 is pure monitoring addition. No widening.
- R3 creates a new orchestrator-convenience path. Does it widen what counts as Read? The CLAUDE.md paragraph explicitly states mempalace is candidate-discovery only and Read remains authoritative. **Widening risk exists (orchestrator may drift toward search-as-Read); mitigation is explicit in paragraph text; §5.4 Skeptic minority activates on laundering incident.**

Does the adoption drop any check? No.

Does the adoption soften any mechanism-failure criterion? No. `validate.sh` checks unchanged. Engine-version rule unchanged. OI-016 triggers unchanged. kernel §7 three-senses unchanged.

Does the adoption narrow any scope without concurrent strengthening? No — all changes are additive (clarification; new annotation; new optional tool reference).

**Aggregate assessment:** adoption passes anti-laundering check. The one widening (R1 "brief note" → "summary") is bounded by specific variance clause + §5.3 Outsider minority with activation warrant for restoration if bounding fails.

**One honest concern:** R3's CLAUDE.md paragraph relies on orchestrator discipline to treat mempalace output as candidate-discovery not authoritative. This is the "orchestrator-discipline-dependent mitigation" pressure Tooler honestly named in 01b Q8. It is the session's weakest-bonded mitigation. The §5.4 Skeptic minority's operational warrant (activate on any search-laundering incident) is the backstop. If that incident is observed, the CLAUDE.md paragraph is candidate for removal and the Skeptic's defer-entirely direction is vindicated.
