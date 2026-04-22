---
session: 022
title: Shared Brief — Workspace Scaling Trajectory and Canonical-vs-Witness Frame
date: 2026-04-22
status: frozen
---

# Shared Brief — Session 022 Deliberation

This is the shared brief. All four perspectives receive it byte-identical. Each perspective's role-specific stance is in a separate file (`01a-perspective-*.md` etc.); only the stance differs between perspectives' briefs.

## 1. Methodology context

The Selvedge methodology (see `specifications/identity.md` v2; `specifications/engine-manifest.md`) is a self-hosting design methodology executing via a nine-activity kernel (`specifications/methodology-kernel.md` v4). This workspace has been the self-development application across Sessions 001–022. Current engine version: `engine-v2`, established Session 021 per D-082 (OI-004 criterion-4 articulation bump).

Each session reads the workspace, assesses, convenes perspectives, deliberates, decides, produces, validates, records, closes. Multi-agent deliberation rules per `specifications/multi-agent-deliberation.md` v4: non-Claude participation required for decisions modifying kernel / revising multi-agent-deliberation.md / revising validation-approach.md semantic validation / asserting OI-004 state change.

Prior full-session deliberations on related topics: Session 020 (`provenance/020-workspace-scaling-deliberation/`) adopted R1–R3 preserving `engine-v1` and adding `CLAUDE.md` orchestrator-convenience mempalace paragraph with four hands-on caveats; Session 021 (`provenance/021-oi004-criterion4-articulation/`) bumped engine-v1 → engine-v2 with criterion-4 articulation and four-state OI-004 lifecycle.

## 2. Problem statement

### 2.1 Session 022 session-open state

Session 022 opened under no default pre-commitment. `tools/validate.sh`: 498 pass, 0 fail, 0 warn. Session-open audit of Session 021 synthesis fidelity clean across five close-directed dimensions.

### 2.2 Scale facts observed at session open

- Total markdown files (excluding `.git/`, `.serena/`, `.claude/`): **212**.
- Total markdown word count: **676,879 words**.
- `SESSION-LOG.md`: **33,227 tokens** at session open (up from 25,713 at Session 020 open; up from the ~single-read ceiling at Session 020 close).
- `open-issues.md`: **27,437 tokens** at session open.
- Single largest provenance file: `provenance/014-oi016-resolution/01d-perspective-outsider.md` at **96,651 words** (next-largest is 7,877 words — a 12× jump).
- Session 021 SESSION-LOG summary entry: **11,340 characters** (94% of Skeptic's Session 020 F3 falsifier upper bound of 12,000 chars).

### 2.3 §5.4 Skeptic mempalace-non-use trigger 1 — materialised

Per Session 020 `01-deliberation.md` §5.4 operational warrant (a): "within 3 sessions of R3 adoption, mempalace is not used substantively (indicating the tool was not actually needed)." Sessions 020, 021, and 022 (opener) have not used mempalace substantively. Trigger 1 **has activated.** This ratifies the §5.4 rollback direction: defer-entirely on mempalace becomes preferred direction for R3.

### 2.4 Operator session-open ratification (direct text; surfaced per §10 anti-import)

Operator ratified path (E.1) with expanded framing. The direct text is committed at `provenance/022-session-open-audit/operator-direction.md` (appended below verbatim at §3). Perspectives MUST treat this text as **input to be surveyed / hypothesised against / partially accepted / rejected**, not as a decided direction. Per kernel §1 Read domain-reading reconciliation clause (OI-015 laundering-gap): domain input is surfaced; at Deliberate/Decide each perspective must re-examine whether the operator's frame should be adopted and, if so, in what shape.

Specifically the perspectives are asked in §8 Design Questions to:
- evaluate the operator's diagnosis of Session 022's own §1 Tooling note (paginated `Read --offset` resolution) as OI-015-at-the-harness-layer;
- evaluate the two-artefact-kind frame (canonical surfaces vs witnesses);
- evaluate the nine candidate surfaces for adoption / reject each independently;
- evaluate the falsifier burden operator names for defer-positions.

The operator expressed that rejection of the frame or of specific candidate surfaces is permitted if the perspective can meet the stated falsifier burden.

## 3. Operator direction verbatim (OI-015 anti-import disclosure)

The following is the operator's Session 022 direction in full, committed verbatim and surfaced as domain input:

> **Ratify E.1: remove R3 `CLAUDE.md` mempalace paragraph this session.** §5.4 Skeptic mempalace-non-use trigger 1 has materialised (three consecutive non-use sessions: 020, 021, 022); R3's contested adoption has its operational rollback warrant satisfied. Not D-023-triggering (CLAUDE.md is not engine-definition). Voluntary multi-perspective convening recommended per R3's original contested adoption.
>
> **E.1 alone does not address the trajectory.** Since Session 020's null adoption, the workspace has grown to ~647K words across 206 markdown files; SESSION-LOG.md is now ~33,227 tokens (up from ~25,713 at Session 020 open); open-issues.md is ~27,437 tokens; a single Session 014 Outsider perspective file is 96,651 words. Session 022 faced two ceiling-violating canonical files and declined mempalace — instead resolving them via "paginated `Read --offset` on 25-line table structure" and "`### OI-NNN:` section grepping followed by paginated `Read --offset`." That is the OI-015 laundering pattern materialised at the harness layer: the methodology's Read instruction satisfied by surgical-read routing-around rather than by direct reading. Engine-v2 did not address this; engine-v3 bump is acceptable if warranted.
>
> **Session adoption set must produce net-negative workspace word delta** and reduce the canonical-surface files-exceeding-Read-ceiling count to zero. Anticipate d016_1, d016_2, d023_1/2/3 firing alongside E.1; plan mandatory non-Claude convening.
>
> **Core frame: two artefact kinds, not one.** `prompts/development.md` line 19 ("read every file") and line 43 ("preserve everything") are not productive tension at 647K words; they are operational contradiction, satisfied in practice by harness-layer summarisation and surgical-read routing — silent-import of derived state into positions where kernel §1 Read requires direct reading. Session 022's own resolution ("paginated Read --offset... yields cleanly") is the exemplar. Distinguish:
>
> - **Canonical surfaces** — bounded orientation layer (specs, SESSION-LOG index, open-issues index, per-session `03-close.md`). Readable in full at session open. Size-gated.
> - **Witnesses** — immutable exact-text records (raw perspective outputs, superseded spec versions, historical annotations). Accessed by explicit reference, not default read. Over-budget witnesses stored as *manifest + numbered chunks* — raw text preserved verbatim; summarisation or silent compression forbidden.
>
> **Required `prompts/development.md` revisions:**
>
> - **Line 19:** *"Begin by reading the workspace's canonical orientation layer completely; then read any preserved witnesses needed to ground the claims you will rely on."*
> - **Line 25:** revise in the same direction or the contradiction moves down the page.
> - **Line 43:** *"Preserve all provenance. Do not delete or silently compress historical records. When a record exceeds routine-read bounds, preserve it as an immutable witness with stable references and a bounded manifest."*
>
> **Session 020 minority activation under current state.** §5.1 Splitter per-OI (warrant: 50K-token file ceiling — satisfied). §5.2 Splitter per-session SESSION-LOG (warrant: Skeptic F3 >12K chars without corresponding complexity — inspect 020–022 entries). §5.3 Outsider restore-to-index (warrant: R1 variance-clause insufficient — inspect 020–022 entries against complexity). §5.4 already activated per E.1 ratification. Assess §5.1–§5.3 against their own warrants.
>
> **Candidate surfaces (non-exhaustive):**
>
> 1. Remove R3 paragraph from `CLAUDE.md` (E.1 ratified).
> 2. Manifested witness-pack specification (format, location, inclusion rules, reference conventions).
> 3. Retroactive migration of over-budget raw perspectives (incl. `provenance/014-oi016-resolution/01d-perspective-outsider.md`) to witness-pack form.
> 4. Per-epoch consolidation: sessions 001–010 synthesised to canonical epoch-index; raws witness-packed.
> 5. `open-issues.md` split per its own spec anticipation clause — 20+ sessions of deferral is the falsifier.
> 6. `SESSION-LOG.md` restoration to true one-line index (§5.3 activation).
> 7. Superseded spec copies (`*-v1.md`, `*-v2.md`, ...) moved from canonical to witness surface.
> 8. `tools/validate.sh` Tier 1 hard-gate: no canonical-surface file exceeds the configured single-read budget; over-budget raw records must be witness-packed, not summarised. Hard-fail at session close.
> 9. `prompts/development.md` lines 19, 25, 43 revisions as above.
>
> **Falsifier burden on defer-positions.** "Paginated Read yields cleanly" / "surgical-read works on this session's specific questions" is not adequate; it is the laundering pattern named above. Adequate defer-falsifier must address (a) the 96,651-word single-perspective file, (b) kernel §1 Read's current unexecutability as written, and (c) external-application inheritance of the scaling trajectory.
>
> **Close shape.** Session close artefacts conform to the adoption set. If witness-packs are adopted, this session's own raw perspectives are witness-packed at close. No grandfather clause.

(End of verbatim operator direction.)

**Note on operator text accuracy vs current measurements**: the operator cites ~647K words / 206 markdown files. Current session-open measurements (at the time of this brief): **676,879 words / 212 markdown files**. The operator's numbers are slightly lower, probably reflecting an earlier measurement or different exclusions. The delta is small; the operator's qualitative claim (scale is substantial and trending up) is robust. Operator's claim of §5.1 warrant "50K-token file ceiling — satisfied" does not match literal spec text (`open-issues.md` at 27K tokens vs 50K warrant text); this is a point perspectives should flag if they read the warrant text directly.

## 4. Current spec text — relevant excerpts

Perspectives should not re-read full specs; the relevant excerpts are below. Full specs are in `specifications/` if perspectives need more.

### 4.1 `methodology-kernel.md` v4 §1 Read (lines 31–37)

> Absorb what the session will reason from before changing anything. In every session this includes **workspace reading**: the full current state of the workspace — every file, every specification, every provenance record, and, where relevant, recent version-control history. Build a complete picture of the workspace's own state.
>
> When the session produces or revises an artefact intended for use outside the workspace, it also includes **domain reading**: the domain constraints the session operates under (stated by the user or operator in-session), cited external materials introduced into the session, and domain knowledge that the orchestrating agent surfaces explicitly as input to the work. Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step (per PROMPT.md). Perspective pretraining enters the session via stance briefs and perspective responses, not via §1 Read.
>
> This is a receptive activity. Its output is understanding, not artifacts.

### 4.2 `prompts/development.md` lines 17–45 (executable prompt under self-development)

Current text (lines 17–33):

> ## How to operate
>
> Begin by reading the workspace completely. Every file, every document, every historical record, every commit message if the workspace is under version control. Build a full picture of what exists before changing anything.
>
> From that reading, determine what state the methodology is in and what should happen next. [...]
>
> State your determination explicitly at the start of each session [...]
>
> Before doing any substantive work, read everything the workspace has preserved about prior decisions. If an idea was considered and rejected earlier, do not silently re-propose it. If you believe a rejected idea deserves reconsideration, cite the prior rejection and explain what has changed. Continuity of reasoning is the whole point of preserving provenance.
>
> Substantive work in this methodology should not be done by a single perspective. [...]

Current text (lines 33–45):

> ## Rules that hold across applications
>
> These rules apply to both the self-development application and to external-problem applications of the engine.
>
> Do not import ideas from outside the process. [...]
>
> Do not skip steps. [...]
>
> Do not overwrite prior specifications silently. [...]
>
> Preserve all provenance. Do not delete historical records, even when they feel embarrassing or outdated. A rejected idea from long ago may be the key to understanding a decision made today.
>
> Leave the workspace in a coherent state at the end of every application. [...]

### 4.3 `workspace-structure.md` v3 §SESSION-LOG.md (lines 61–63)

> A running index of sessions for quick orientation. Each entry is one line (one Markdown table row) containing the session number, date, title, and a summary of what was accomplished. The summary length scales to session complexity: planning-only, single-perspective, or assessment-only sessions produce shorter summaries; deliberation sessions producing substantive spec revisions, cross-model influences, or external artefacts produce longer summaries calibrated to record the decision surface and load-bearing influences. The canonical detail for each session lives in its provenance `03-close.md` file; the SESSION-LOG entry is an index over that detail, not a replacement. This file is updated at the close of each session.

### 4.4 `workspace-structure.md` v3 §open-issues.md (lines 65–67)

> A list of known questions, gaps, uncertainties, and unresolved disagreements. Each entry has a brief description, the session that identified it, and its current status. Issues are removed when resolved (with a reference to the session that resolved them). **This is a single file, not a directory, unless the number of issues makes a single file unwieldy.**

The "unless" clause is a pre-existing split-authorisation that has not yet been exercised.

### 4.5 `workspace-structure.md` v3 §provenance/ (lines 98–123)

Current convention: each session's provenance is a numbered directory. Files within are numbered for reading order. All provenance files use Markdown with YAML frontmatter. Provenance records are **immutable** once the session closes.

**Relevant tension:** the immutability rule (per D-017, reaffirmed in v3) prevents editing existing raw perspective files. Any retroactive migration must honor immutability — either by preserving originals in place + adding a witness-pack structure alongside, or by a copy-plus-reference pattern (see Session 009 D-054 precedent for `applications/` regularization).

### 4.6 `multi-agent-deliberation.md` v4 §Provenance Layout (lines 257–305)

Flat-layout is the current default; raw perspective files live at `provenance/<NNN-title>/01a-perspective-<role>.md` etc. The v4 spec does not currently prescribe a bound on raw-file size.

### 4.7 `engine-manifest.md` §3 at engine-v2 (file enumeration)

| File | Role |
|------|------|
| `PROMPT.md` | Dispatcher |
| `prompts/development.md` | Self-development executable prompt |
| `prompts/application.md` | External-application template |
| `specifications/methodology-kernel.md` | Kernel |
| `specifications/multi-agent-deliberation.md` | Multi-agent rules |
| `specifications/validation-approach.md` | Two-tier validation |
| `specifications/workspace-structure.md` | Structure rules |
| `specifications/identity.md` | Denotation |
| `specifications/reference-validation.md` | Reference-validation |
| `specifications/engine-manifest.md` | This file |
| `tools/validate.sh` | Structural validator |

Any substantive revision to these files triggers an engine-version bump per `engine-manifest.md` §5.

## 5. Session 020 minorities assessment against warrants

Per operator direction, each §5.x minority's warrants are re-examined against current session-open state.

### 5.1 (Splitter per-OI directory for open-issues.md)

Warrant text: "(a) future session's OI-housekeeping task completes incorrectly because a segment-read missed a relevant cross-reference in a not-loaded segment of `open-issues.md`; (b) two consecutive sessions' OI count tallies disagree with git history because of segment-read undercount; (c) `open-issues.md` exceeds 50,000 tokens (requires >2 segment-reads for full traversal)."

**Current state:** open-issues.md at 27,437 tokens. Requires 2 segment-reads (first ~25K, second ~2K). Strict warrant (c) says >2 segment-reads = >50K tokens. Not met. Warrants (a) and (b) not observed.

**Operator claim** that this warrant is satisfied does not match literal spec text. Perspectives should evaluate whether to (i) adhere to literal warrant, (ii) revise the warrant downward (e.g., to "exceeds single-read ceiling" which IS satisfied), (iii) reject the minority adoption path altogether and treat open-issues separately.

### 5.2 (Splitter per-session files for SESSION-LOG.md)

Warrant text: "(a) after R1 adoption, a session's SESSION-LOG entry exceeds 12,000 characters without corresponding session complexity (Skeptic's F3 falsifier); (b) SESSION-LOG.md exceeds single-read ceiling within 5 sessions of R1 adoption (i.e., by Session 025); (c) a session records a specific reasoning error traceable to segmented SESSION-LOG read (Skeptic's F1 falsifier)."

**Current state:** SESSION-LOG.md at 33,227 tokens (exceeds 25K single-read ceiling). R1 adopted Session 020; Session 022 is 2 sessions later (well within 5-session window). **Warrant (b) IS SATISFIED.** Warrant (a) not satisfied (Session 021 entry at 11,340 chars with high complexity — below F3 bound; variance-clause invoked appropriately). Warrant (c) not observed.

### 5.3 (Outsider restore-to-brief-index)

Warrant text: "(a) after R1 adoption, a session cites SESSION-LOG as primary source while 03-close.md exists and carries the same content (i.e., citation laundering detected); (b) the R1 variance-clause ('summary length scales to session complexity') is invoked as permission for an unwarrantedly long entry that does not correspond to complexity by decision count or artefact count; (c) within 5 sessions of R1, SESSION-LOG.md exceeds single-read ceiling despite the variance-clause."

**Current state:** Warrant (c) IS SATISFIED on the same ceiling-breach basis as §5.2(b). Warrants (a) and (b) not observed.

### 5.4 (Skeptic defer-entirely on tools)

Warrant text: "(a) within 3 sessions of R3 adoption, mempalace is not used substantively; (b) any 'search laundering' incident occurs; (c) mempalace version drift causes silent index staleness resulting in a missed session finding; (d) external-application workspaces report confusion from the 'CLAUDE.md tool reference but no engine requirement' pattern."

**Current state:** Warrant (a) SATISFIED (Sessions 020, 021, 022 non-use). Warrants (b)-(d) not observed. Operator ratifies E.1 adoption.

### Summary

§5.2, §5.3, and §5.4 warrants are **vindicated**. §5.1 strict warrant is **not vindicated**, but related warrants (single-read ceiling breach) are satisfied, raising a question of whether §5.1 should be triggered by the softer ceiling-breach condition too.

## 6. Survey — related framings from adjacent traditions

Per kernel §1 Read and PROMPT.md anti-silent-import, domain knowledge surfaced explicitly as input. Perspectives may reason against these; they are not authoritative.

**Computing / data systems:**
- **Memory hierarchies** (registers → L1/L2/L3 cache → RAM → disk → tape). Canonical-orientation-layer ≈ "hot" tier (read at session open); witness layer ≈ "cold" tier (accessed by explicit reference). Analogous to the operator-proposed frame.
- **Literate programming / weave-and-tangle** (Knuth). The same source decomposes into a "woven" human-readable document and a "tangled" machine-compilable output. Analogous: maybe canonical-vs-witness is "woven" summary vs "tangled" raw.
- **Git LFS and large-file handling.** Git stores pointers to large objects outside the repo proper. Analogous: the over-budget Outsider file could be LFS-shaped.
- **Database indexing vs storage.** An index is a bounded-size structure that points into unbounded storage. Analogous to SESSION-LOG as index, 03-close.md as storage.
- **Content-addressable storage** (IPFS, Git object store). Objects addressed by hash; references are pointers. Analogous for witness integrity.

**Information / library sciences:**
- **Cataloguing vs archive.** The card catalog is indexed at constant cost; the stacks are unbounded but accessed by reference. Analogous.
- **Scholia vs text.** Medieval manuscripts had a bounded canonical text surrounded by scholia (marginal annotations). Annotations grew over time but the canonical text did not.

**Document / software engineering:**
- **API docs vs source code.** The canonical API doc is read first; the source is read for details. Revision discipline keeps the API doc current; implementation can be arbitrarily complex below.
- **Executive summary + appendices.** Classic corporate-document pattern. Summary is bounded; appendices are unbounded.

**Constraints-vs-mechanism in this workspace specifically:**
- Kernel §1 Read says "every file, every specification, every provenance record." This is the *constraint* the methodology imposes on itself.
- `prompts/development.md` line 19 says "read the workspace completely." This is the executable *restatement*.
- Current *mechanism* (observed at Session 022 open): paginated `Read --offset` + `Grep` on section anchors. This is "harness-layer routing."

The tension between constraint and mechanism is the object of this deliberation. **Options:**
- (I) Revise the constraint to match the mechanism: "read canonical layer completely; read witnesses by reference." Operator-proposed.
- (II) Revise the mechanism to match the constraint: require that every file be readable in a single call; force workspace to shrink until constraint is executable. Extreme but coherent.
- (III) Keep both; explicitly tolerate the gap as a hedge: current state. Laundering concern.
- (IV) Reframe entirely (no layer distinction; different diagnosis of the scaling tension).

## 7. Role-specific stances — placement

Each perspective has its role stated in a separate `01X-perspective-<role>.md` file written before this brief is committed. See §8 below for the design questions each perspective must answer.

Perspectives in this deliberation:
- **01a — Architect.** Constructive design of the adoption set. Canonical/witness distinction advocate.
- **01b — Conservator.** Preservation-first. Tests fidelity costs of restructuring; immutability concerns.
- **01c — Skeptic.** Adversarial. Tests whether the canonical/witness frame introduces new failure modes; holds defer-positions to operator's stated falsifier burden.
- **01d — Outsider.** Non-Claude (OpenAI GPT-5.4 via `codex exec`). Bring training-distribution-independent reasoning to the table.

## 8. Design questions

Each perspective answers all eight questions below. Responses are independent — each perspective forms its position before seeing the others.

**Q1. Frame acceptance.** Do you accept the operator's two-artefact-kind frame (canonical surfaces vs witnesses) as the right diagnosis? If yes, what is your load-bearing reason. If no, what is your alternative frame or rejection argument. If partially, which parts and which not.

**Q2. `prompts/development.md` revisions.** Evaluate the operator's proposed text for lines 19, 25, 43. Propose your own text if different. Must address:
- Whether line 19 should be revised (and how);
- Whether line 25 (the "read everything the workspace has preserved about prior decisions") needs corresponding revision;
- Whether line 43 (the preservation rule) should be revised to name witness-packing explicitly;
- Whether kernel `methodology-kernel.md` §1 Read should be revised (d023_1 trigger) or whether prompts-layer revision alone is sufficient.

**Q3. Witness-pack specification.** If witness-packs are adopted, what is the specification? Required fields:
- Format: directory with manifest + numbered chunks? Single file with chunks? Zip-like archive?
- Location: alongside the original in provenance? Separate top-level directory?
- Inclusion rules: what classifies a record as "over-budget" (token count? word count? single-read-failure?)
- Reference conventions: how does a canonical file point at a witness? How does a reader resolve the pointer?
- Integrity: how is verbatim preservation guaranteed? Hash? Append-only?
- Does witness-packing require an engine-v3 bump?

**Q4. Retroactive migration scope.** Given immutability (D-017; workspace-structure.md §provenance), which of the following should be retroactively migrated this session? (Each yes/no with reason.)
- (a) `provenance/014-oi016-resolution/01d-perspective-outsider.md` (96,651 words; the extreme outlier)
- (b) All over-threshold raw perspective files (if threshold T defined)
- (c) Superseded spec copies (`specifications/*-v1.md`, `*-v2.md`, `*-v3.md`)
- (d) Long OI annotations in `open-issues.md`
- (e) Long SESSION-LOG entries (Sessions 011+)
- (f) Sessions 001–010 "epoch-index" consolidation (operator candidate #4)

**Q5. Canonical-surface restoration this session.** Should this session:
- (a) restore `SESSION-LOG.md` to a thin one-liner index (§5.3 activation)?
- (b) restructure `open-issues.md` (§5.1 variant; maybe not strict per-OI directory if warrant not fully met)?
- (c) both, one, or neither?
- What is the risk of losing information in this restoration?

**Q6. `tools/validate.sh` hard-gate check.** Evaluate operator candidate #8 (no canonical-surface file exceeds configured single-read budget; hard-fail at close). What single-read budget? How is "canonical-surface" vs "witness" detected by the validator? Where does the list live?

**Q7. Session 020 minority activations.** Each of §5.1, §5.2, §5.3 has warrants assessed in §5 above. For each:
- (a) adopt the rollback direction?
- (b) re-revise the warrant text if strict reading not met?
- (c) subsume into the canonical/witness frame adoption (i.e., the frame's adoption supersedes the minority's separate activation)?

**Q8. Close shape — this session's own raws.** Operator stipulates: no grandfather clause; this session's own raws are witness-packed at close if witness-packs are adopted. Do you accept? What is the practical consequence for this session's provenance directory and SESSION-LOG entry?

**Q9 (meta).** What is the engine-version implication of the adopted set? Is engine-v3 warranted? Which D-023 triggers fire? The operator anticipates `d016_1, d016_2, d023_1/2/3`. Do you agree with that trigger declaration?

## 9. Response format

Per `multi-agent-deliberation.md` v4 §Stance Briefs:

- Length target per perspective: 1,500–3,500 words.
- Structure: opening position (2-3 sentences), then Q1–Q9 in order. Each question answered with explicit position + reasoning + cites to this brief or to current spec text where relevant. Honest-limits section at the end naming what the perspective could not verify independently.
- Citation style: `[§N]` for sections of this brief; `[spec-name §N]` for specifications; `[01X-Q#]` when referring to another perspective's response (not applicable during the independent phase — only relevant in synthesis).
- Perspectives must NOT read other perspectives' responses during the independent phase. Perspectives MAY read this brief and current specifications in `specifications/`. Perspectives MUST NOT read raw files in `provenance/NNN/` unless explicitly needed and the read is declared in the honest-limits section.
- Refusal or substantive rejection is permitted and is signal, not error.

## 10. Anti-import constraint (OI-015 laundering-gap reconciliation)

Per PROMPT.md, kernel §1 Read, and OI-015: reason primarily from this brief. Do not import ideas from pretraining, unrelated sources, or conversations outside this deliberation without naming the import and routing it through explicit surveying (§6 above is the surveying step for this deliberation).

**Specific risk at Session 022**: the operator's text in §3 includes vocabulary ("canonical surfaces", "witnesses", "manifest + numbered chunks", "laundering at the harness layer") that is NOT yet in any specification and may be partially novel. Perspectives should evaluate:
- Whether to adopt this vocabulary directly or coin their own;
- Whether operator-vocabulary shapes the available solution space unduly;
- Whether the frame the vocabulary encodes is the right frame.

**Brief-priming observation from Session 008, 014, 016** etc.: briefs that quote operator text tend to propagate that text into perspective responses even when the perspective's own reasoning would have used different words. Be aware of this effect; prefer your own vocabulary where your reasoning does not specifically adopt the operator's frame.

## 11. Closure

The deliberation ends when all four perspectives have committed their responses verbatim. Synthesis proceeds per `multi-agent-deliberation.md` v4 §Synthesis. Session decisions at `02-decisions.md`. Close at `03-close.md`.

Deliberation anchor commit: this brief is committed at the next commit; the commit hash is the anchor.

---

(End of shared brief.)
