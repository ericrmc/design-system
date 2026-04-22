---
session: 022
title: Perspective — Outsider
date: 2026-04-22
perspective: outsider
participant_kind: non-anthropic-model
model_family: gpt
model_id: gpt-5.4
provider: openai
endpoint: cli-wrapper
invocation_method: codex-exec
reasoning_effort: xhigh
tokens_used: unknown-not-echoed-at-close
session_id: 019db521-775f-7872-9b38-f0c4b0094c28
status: verbatim
anchor_commit_cited: 46f0baf
transport_note: |
  Committed verbatim from `codex exec` stdout including CLI banner
  (OpenAI Codex v0.121.0 research preview, model gpt-5.4, provider
  openai, approval never, sandbox read-only, reasoning effort xhigh,
  session id 019db521-775f-7872-9b38-f0c4b0094c28), user prompt echo
  (full shared brief + Outsider stance + response-now instruction),
  four codex markers delimiting pre-response workspace-exploration
  tool calls (reading CLAUDE.md, prompts/development.md,
  prompts/application.md, specifications/methodology-kernel.md,
  specifications/workspace-structure.md, specifications/engine-manifest.md,
  specifications/validation-approach.md, specifications/multi-agent-deliberation.md,
  tools/validate.sh, provenance/014-oi016-resolution/01d-perspective-outsider.md
  outlier structure), reasoning summary entries, and the final response
  body (opening position statement + Q1-Q9 + Honest Limits section).
  Invocation used stdin-pipe form per Session 021 lesson:
  `codex exec -c model_reasoning_effort=xhigh < /tmp/022-outsider-prompt.txt
  > /tmp/022-outsider-response.txt 2>&1`. No stdin-wait hang this session.
  Exit code 0; background task id bfutmoq27. Full verbatim preservation
  (including CLI noise and workspace-exploration traces) per Session 014
  precedent and operator's §3 "witnesses preserve verbatim; summarisation
  or silent compression forbidden" constraint. At session close, if
  witness-packs are adopted, this file is migrated per the adoption
  decision.
---

Reading prompt from stdin...
OpenAI Codex v0.121.0 (research preview)
--------
workdir: /Users/ericmccowan/Development/complex-systems-engine
model: gpt-5.4
provider: openai
approval: never
sandbox: read-only
reasoning effort: xhigh
reasoning summaries: none
session id: 019db521-775f-7872-9b38-f0c4b0094c28
--------
user
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
---
session: 022
title: Role-Specific Stance — Outsider
date: 2026-04-22
status: stance-brief
perspective: outsider
---

# Role-Specific Stance — Outsider

You are the Outsider. You are not from the Claude model family.

You were invited to this deliberation because the methodology's Open Issue OI-004 requires non-Claude perspectives to be genuinely independent in training lineage and to shape outcomes through contributions Claude-only deliberation could not produce. Prior Outsider contributions (Sessions 005, 006, 009, 011, 012, 013, 014, 017, 019, 020, 021) have included frame-replacement (Session 017 H4 layered model; Session 020 "indexes drifted to dossiers" type-drift), split-resolving third-ways (Sessions 009/010/011 voice-and-structure patterns), and structural bifurcation (Session 021 criterion-4 two-branch model-vs-human articulation). The typology of non-Claude contribution is open; your contribution may be of any kind.

Your specific assignment:

- Evaluate the operator's canonical-vs-witness frame **independently** of what the Claude perspectives in this deliberation would produce. If you see a different diagnosis of the scaling tension, name it.
- Respond to Q1–Q9 in §8 of the shared brief. Your honest assessment of each is more valuable than consensus with Claude perspectives.
- If you see a gap in the frame (e.g., a participant kind the frame does not accommodate; an operational contradiction the adoption creates; a cheaper alternative the Claude-perspective space is not likely to produce), name it explicitly.

You may perform workspace exploration via `codex exec` tool calls before producing your response body (Session 021 precedent). If you do, cite specific files and sections. You may NOT read other perspectives' responses — this deliberation is independent-phase.

You may refuse a stance, propose a fourth or fifth hypothesis, or argue for a frame-replacement rather than within-frame answers. Refusal and reframing are signal, not error.

Target length: 1,500–3,500 words. Answer all Q1–Q9.

---

Respond now. Write directly as your response body. Do not summarise the brief back to me; cite §N references as needed. Answer Q1 through Q9 in the order presented. Open with a short (2-3 sentence) position statement. Close with an honest-limits section. Length target: 1500-3500 words.

codex
Writing the Outsider stance body. I’m checking the current executable prompt, kernel, structure, manifest, validator, and `CLAUDE.md` so the response is anchored to the live workspace rather than only the brief excerpts.
exec
/bin/zsh -lc "sed -n '1,220p' CLAUDE.md" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "sed -n '1,220p' prompts/development.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
# CLAUDE.md

## Commit workflow

Before finishing your response, stage all changed/new files, commit with a concise message, and push using git directly.

## Tools
This contains usage instructions for tools you have requested. If you decide more are needed, you can install them using `uv tool` or ask the user to ratify your tool decision and install something on your behalf. Add additional instructions here as you see fit.

### Multi-agent work

When work would benefit from multiple independent perspectives or parallel efforts, consider using agent teams via the `TeamCreate` tool (`CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS`). You also have access to the Google `gemini` and OpenAI `codex` CLI tools for non-Anthropic LLM access. Codex is preferred for any thinking or reasoning tasks.

### mempalace (orchestrator-convenience, non-engine)

`mempalace` v3.1.0 is installed via `uv tool`. It is classified as orchestrator-convenience tooling, analogous to the `gemini`/`codex` CLIs above. **It is NOT part of `engine-manifest.md` §3 and is NOT required by any specification.** External-application workspaces loading the engine do not inherit the dependency; fresh clones of this workspace can operate without it. This classification is load-bearing for the engine's text-only portability claim; do not promote mempalace into any engine-definition file without a dedicated deliberation.

Suggested use: when a single Read would exceed the 25,000-token ceiling (SESSION-LOG.md, open-issues.md, aggregated provenance search), orchestrators may run `mempalace search "<query>" --wing complex-systems-engine` or `mempalace wake-up --wing complex-systems-engine` to retrieve candidate matches.

**Critical caveats (per Session 020 hands-on finding; see `provenance/020-workspace-scaling-deliberation/01b-perspective-tooler.md`):**

- Despite the `mempalace --help` description ("Find anything, exact words"), `search` is semantic/vector-ranked, not exact-string match. Exact-string queries like `D-074` may return zero results containing that string even when the string exists in indexed files. Use `Grep` for exact-string verification.
- `wake-up` output is drawer-count-dominated rather than recency-weighted; it is useful for fresh-session priming but does not substitute for reading SESSION-LOG.md.
- `mine` does not deduplicate versioned specs — superseded `-v2.md` / `-v3.md` files are indexed alongside current canonical files and may rank above them.
- mempalace output is **candidate-discovery only.** Every cited claim must be reconfirmed against the source file via Read before inclusion in session artefacts. Treating mempalace output as authoritative is the laundering risk (OI-015-adjacent, WX-20-1 watchpoint).

Initialisation (one-time, if adopted): `mempalace init . && mempalace mine .` in workspace root. The init creates `mempalace.yaml` + `entities.json` in the workspace root — both are gitignored. The palace state itself lives at `~/.mempalace/palace/`, outside the workspace.

Re-mine cadence: manual, typically at session close after substantive file changes. Not a spec requirement; orchestrators not using mempalace need not re-mine.

 succeeded in 0ms:
You are operating on the **self-development application** of the **Selvedge engine**. This is the foundational application in which the engine evolves its own specifications by running its own process on itself. Every session so far (001 through the most recent) has been an instance of this application. This prompt is applied repeatedly. Each application advances the work by one increment. The workspace may be empty, partial, or mature. Determine the state and take the next right step.

Selvedge is the methodology (abstract approach). The **Selvedge engine** is its current loadable implementation, enumerated in `specifications/engine-manifest.md`. An **application** of the engine is any specific run — this one is the self-development application. See `specifications/identity.md` for the three-layer denotation; see `PROMPT.md` (the dispatcher) for the top-level framing.

## What this application is

This application is the engine's own development: a self-hosting design activity in which specifications evolve themselves by running the engine on its own outputs. What emerges from this workspace is intended to be used by others, on their own projects, in their own domains, as a separately-initialised application of the engine (per `prompts/application.md` and `engine-manifest.md` §6). The methodology is self-hosting — the engine evolves itself by running its own process on itself. Specifications are the durable artefacts that persist between its stages, and provenance — the reasoning trail, the rejected alternatives, the dissenting views — is preserved alongside decisions so that future readers, human or agent, can reconstruct not just what was decided but what was considered and why.

The engine exists because traditional ways of managing requirements and design intent were optimized for a world where humans were the expensive part of producing and maintaining specifications. In a world where language models can read, generate, challenge, and evolve specifications at the moment they are needed, the old ceremonies collapse into something lighter and more continuous. This self-development application discovers what that lighter approach looks like by being built through the approach it proposes.

The methodology is not specific to any domain. An external-problem application of the engine may design software, research programmes, physical systems, policy interventions, curricula, organisations, or anything else. The methodology itself — the mechanic of diverse perspectives reasoning together, producing durable artefacts, preserving their reasoning, and evolving the system by running the same mechanic on its own outputs — is domain-general.

A preference, not a rule: text-based artefacts in a format that is both human-readable and machine-readable tend to serve this kind of methodology well, because they can be read by people, parsed by agents, diffed between versions, and preserved indefinitely with minimal tooling. Markdown is the obvious candidate for most work. For domains where text alone cannot carry the specification — a spatial layout, a circuit diagram, a molecular structure, a musical score — use whatever representation the domain demands, but keep a text-based record of the intent and reasoning alongside it so the provenance remains legible.

Another preference, not a rule: every application of the engine should include some mechanism by which its specifications can be shown to still describe reality. In a software context this is automated tests. In a research context it may be reproducibility of results. In a policy context it may be a pilot study or an evaluation against stated outcomes. In a physical system it may be a qualification campaign. The word "test" is used in this prompt as a shorthand for whatever form of validation is appropriate; `specifications/methodology-kernel.md` §7 names three senses (Workspace, Domain, Reference).

## How to operate

Begin by reading the workspace completely. Every file, every document, every historical record, every commit message if the workspace is under version control. Build a full picture of what exists before changing anything.

From that reading, determine what state the methodology is in and what should happen next. If the workspace has not yet defined its own structure, the first work is to do so — by surveying prior approaches, reasoning about what this methodology needs, and committing a proposed shape along with the reasoning that led to it. If the workspace has defined a structure but not yet applied it, the next work is to begin applying it. If the structure has been applied but produces artefacts that have not been validated, the next work is validation. If everything has been exercised at least once, the methodology is in evolution mode — identify the weakest aspect of the current system and do whatever work addresses it.

State your determination explicitly at the start of each session, so the next application of this prompt has a clear record of what you inferred and why.

Before doing any substantive work, read everything the workspace has preserved about prior decisions. If an idea was considered and rejected earlier, do not silently re-propose it. If you believe a rejected idea deserves reconsideration, cite the prior rejection and explain what has changed. Continuity of reasoning is the whole point of preserving provenance.

Substantive work in this methodology should not be done by a single perspective. Convene a group of AI agents with genuinely different viewpoints suited to the work at hand. Some perspectives generate options, some challenge them, some attend to what is unknown, some attend to what has been ignored, some reason about how the work will be received by those who must live with it. The specific perspectives, their number, and how they collaborate are for you to develop. Over repeated applications, patterns will emerge — document them when they do, so future applications can build on what worked.

The work should produce a concrete output: a structured record of what was proposed, what was decided, what was rejected with reasoning, and what remains uncertain. This record is the provenance. Commit it to the workspace in a way that preserves it permanently and makes it findable by future applications. Alongside the provenance, update or create whichever artefacts the work warrants. If the work produced a new specification, write the specification. If it produced an implementation, build it. If it surfaced problems, record them where subsequent work will find them. The structure of the workspace should evolve to serve the methodology, not the other way around.

Before ending the session, verify the workspace is in a coherent state. Specifications describe the engine as it currently is. Validations pass against those specifications, or their failures are documented as open issues for subsequent work to address. Any human-facing summary of the workspace accurately reflects its current state. Every piece of work done in this session has committed its provenance.

## Rules that hold across applications

These rules apply to both the self-development application and to external-problem applications of the engine.

Do not import ideas from outside the process. If an insight arrived through reading something unrelated, a conversation with a human, or your own pretraining, introduce it as an input to an explicit surveying or hypothesising step rather than committing it directly. The value of this methodology is that its artefacts are traceable to the reasoning that produced them.

Do not skip steps. Each piece of work's output is the next piece's input, and skipping breaks the chain of reasoning that makes the methodology evolveable.

Do not overwrite prior specifications silently. When a specification is revised, preserve the prior version and make the succession traceable. The form of that preservation — filenames, directory structure, supersession markers, or something else — is for you to develop. Whatever you choose, be consistent so future readers can follow the thread.

Preserve all provenance. Do not delete historical records, even when they feel embarrassing or outdated. A rejected idea from long ago may be the key to understanding a decision made today.

Leave the workspace in a coherent state at the end of every application. If a piece of work cannot complete, commit what was produced, document the blocker, and end cleanly rather than leaving work in an indeterminate state.

## Now begin

Read the workspace. Determine what state it is in. Read prior provenance. Convene the perspectives suited to the work at hand. Do the work. Commit its outputs and its record. Report what was done, what state the workspace is now in, and what the next application should address.

exec
/bin/zsh -lc "sed -n '1,220p' specifications/engine-manifest.md" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "sed -n '1,260p' tools/validate.sh" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
---
title: Engine Manifest
version: 1
status: active
created: 2026-04-22
last-updated: 2026-04-22
updated-by-session: 021
supersedes: none
---

# Engine Manifest

## Purpose

This specification names what constitutes the **Selvedge engine** at any given engine version. The engine is the current loadable implementation of the Selvedge methodology (per `identity.md` v2 layered denotation): a file set that, when loaded together, executes the methodology's nine-activity process against an application's context. The manifest makes the engine pointable-at, versionable, and cleanly separable from the workspace's own development-provenance.

Created Session 017 per D-074 as the resolution of OI-017 (engine-vs-methodology reframing). Its minimal scope is deliberate: the manifest enumerates and declares invariants, but does not restate the content of the specifications it enumerates.

## Specification

### 1. Engine definition

The **Selvedge engine** is the current loadable implementation of the Selvedge methodology, consisting of the file set enumerated in §3 at the engine version named in §2. Loading the engine means having these files available and treating them as a closed unit for the purposes of executing a session.

The engine is distinct from:
- The **methodology** — the abstract-approach, domain-general mechanic that the engine realises (named "Selvedge" per `identity.md` v2).
- The **development-provenance** — the self-development application's own accumulated reasoning trail (`SESSION-LOG.md`, `open-issues.md`, `provenance/`).
- Any **specific application** — a particular run of the engine against a problem (self-development or external-problem).

### 2. Current engine version

**`engine-v2`** (established Session 021 per D-082).

Subsequent engine versions (`engine-v3`, `engine-v4`, ...) increment per the versioning discipline in §5. The current engine version is always named by this §2.

### 3. Engine-definition files at `engine-v2`

The following files constitute the engine at the current version:

| File | Role |
|------|------|
| `PROMPT.md` | Thin dispatcher: names the three layers and two operating modes; points to `prompts/development.md` and `prompts/application.md`. |
| `prompts/development.md` | Executable prompt for the self-development application (this workspace's entry point). |
| `prompts/application.md` | Template prompt for external-problem applications (loads the engine by reference to this manifest; specifies application-context slots). |
| `specifications/methodology-kernel.md` | Kernel: defines the nine-activity execution semantics. |
| `specifications/multi-agent-deliberation.md` | Defines multi-perspective deliberation triggers, non-Claude participation, recording schema. |
| `specifications/validation-approach.md` | Two-tier validation: structural checks and guided-assessment questions. |
| `specifications/workspace-structure.md` | Defines file classes, top-level structure, provenance conventions. |
| `specifications/identity.md` | Records the name Selvedge and the three-layer denotation. |
| `specifications/reference-validation.md` | Defines reference-validation as the third sense of validation. |
| `specifications/engine-manifest.md` | **This file.** |
| `tools/validate.sh` | Executable: runs the Tier 1 structural checks from `validation-approach.md`. |

An external-application workspace that clones the engine should copy (or reference) these files and nothing else from the source workspace.

### 4. What is explicitly NOT part of the engine

The following are development-provenance or application-scope; they are **not** loaded when an external application initialises:

- `SESSION-LOG.md` (development-provenance)
- `open-issues.md` (development-provenance)
- `provenance/` (development-provenance: all session records)
- `applications/NNN-*/` (application-scope: prior application outputs, not reusable as engine load)
- `specifications/*-v1.md`, `*-v2.md`, `*-v3.md` (superseded spec versions: preserved in the workspace but not active engine definition)

This manifest's own version history is also not part of the engine load; the current `engine-manifest.md` is what counts.

### 5. Versioning discipline

The engine version (`engine-v1`, `engine-v2`, ...) increments when any file in §3 changes in substance. "In substance" means:

- A new engine-definition file is added to §3.
- An existing engine-definition file receives a substantive revision (v-bump per the spec-revision discipline in `workspace-structure.md`).
- An engine-definition file is removed or superseded.

The engine version does **not** increment on:
- Typo corrections or formatting adjustments.
- Minor elaborations within an existing spec's scope (per the OI-002 substantive-vs-minor heuristic).
- Updates to development-provenance or application-scope files.
- Changes to `SESSION-LOG.md`, `open-issues.md`, or `provenance/`.

Engine-version increments are declared by a decision record in the session that executes the increment. The decision names the file(s) changed and the new engine version.

### 6. Loading the engine / minimal external-application initialisation contract

An external application workspace is initialised by:

1. **Copy the engine-definition file set** (§3) into a fresh directory (or reference them from a canonical engine repository). The copy is flat: maintain the same paths (`PROMPT.md`, `prompts/`, `specifications/`, `tools/`).
2. **Create fresh development-provenance files** in the new workspace:
   - Empty `SESSION-LOG.md` (header only).
   - Empty `open-issues.md` (header only).
   - Empty `provenance/` directory.
3. **Create the first application directory** `applications/001-<slug>/` containing at minimum a `brief.md` carrying:
   - The problem statement.
   - Constraints (domain constraints; time constraints; stakeholder constraints).
   - Stakeholders (who holds the problem; who will receive the artefact; who validates).
   - Success condition (what the artefact must do for the application to be considered successful).
4. **Select the execution prompt.** For an external-problem application, copy `prompts/application.md` to the workspace's `PROMPT.md` (or reference it), then fill in the template slots with the application-specific content from `brief.md`. For a self-development application (like this workspace), use `prompts/development.md`.
5. **Record the engine version loaded.** The first session's provenance (e.g., `provenance/001-*/00-assessment.md`) should name the engine version (`engine-v1` or later) the workspace was initialised from.
6. **Run Session 001** per the loaded execution prompt. The session Reads the application's initial state (the `brief.md` + the engine specifications), Assesses what the application's first increment should be, Convenes perspectives, Deliberates, Decides, Produces the first artefact or design fragment, Validates, Records, and Closes.

The critical rule per Outsider [Session 017 01d Q6]: **external application workspaces inherit the engine, not the engine's autobiography.** The development-provenance of the Selvedge engine's own development is preserved in this source workspace; it does not travel with the engine to an external application.

### 7. Engine version history

- **`engine-v1`** — established Session 017 via D-074. First versioned engine definition. File set per §3. Corresponds to the post-Session-017 state of the workspace: `methodology-kernel.md` v4 + scope-clarification sentence; `multi-agent-deliberation.md` v3 + minor scope-applicability sentence; `validation-approach.md` v3 + minor scope-applicability sentence; `workspace-structure.md` v3; `identity.md` v2; `reference-validation.md` v1; `tools/validate.sh` as of Session 005/006 last substantive change; `PROMPT.md` as thin dispatcher; `prompts/development.md` and `prompts/application.md` as created by D-074. Subsequent intra-engine-v1 changes (Session 019: `reference-validation.md` v1 → v2; Session 020: `workspace-structure.md` v3 minor amendment) did not bump the engine version because v3 minor amendments do not trigger §5 bump per OI-002 heuristic.

- **`engine-v2`** — established Session 021 via D-082. Substantive revisions to three engine-definition files: `multi-agent-deliberation.md` v3 → v4 (added §Criterion-4 Articulation for OI-004; §Acceptable Participant Kinds for OI-004; six new Layer 2 manifest fields; one new synthesis frontmatter field; one new session-level participants.yaml block; four-state OI-004 lifecycle with §Closure Procedure for OI-004); `validation-approach.md` v3 → v4 (added §Tier 2 Q8; documented gating conventions for new checks 16-19); `tools/validate.sh` substantive update (added checks 16, 17, 18, 19; added CRITERION4_ARTICULATION_SESSION constant; added PARTICIPANT_ORGANISATION_CLOSED_SET constant; added Tier 2 Q8 print-out). v3 of the two specs preserved as `multi-agent-deliberation-v3.md` and `validation-approach-v3.md` (both `status: superseded`). All other engine-definition files unchanged at engine-v2 boundary: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `methodology-kernel.md` v4, `workspace-structure.md` v3, `identity.md` v2, `reference-validation.md` v2, `engine-manifest.md` (this file, frontmatter `last-updated: 2026-04-22` + `updated-by-session: 021`).

Future engine-version increments will extend this history in this section.

## Validation

To validate this specification:

1. Confirm the files enumerated in §3 all exist at the declared paths.
2. Confirm that any file NOT enumerated in §3 but present in the workspace is either (a) in §4's explicit exclusion list, or (b) a superseded spec version, or (c) clearly out-of-scope (e.g., `.git`, `.gitignore`, `.claude`, `.serena`).
3. Confirm that `identity.md` v2 references this manifest as the definition of the engine at the current version.
4. Confirm that `workspace-structure.md` v3 references the same three file-class distinction this manifest implies (engine-definition / development-provenance / application-scope).
5. When a session executes a substantive revision to an engine-definition file, confirm the session's decision record declares a new engine version in this manifest's §2 and §7.
6. When an external application workspace is first initialised, confirm its Session 001 provenance records the engine version loaded per §6.5.
7. Confirm that no engine-version increment has occurred without a decision record authorising it (guard against silent engine-version drift).

 succeeded in 0ms:
#!/usr/bin/env bash
# Methodology workspace validation tool
# Two-tier validation: automated structural checks + guided semantic questions
# Read-only: this script never modifies any files

set -euo pipefail

# Session from which the triggers_met schema is enforced (D-039, Session 006).
# Checks 14 and 15 apply only to sessions numbered >= this constant.
# See specifications/validation-approach.md v3 "Gating Conventions (checks 14, 15)".
readonly TRIGGERS_MET_ADOPTION_SESSION=6

# Session from which OI-004 criterion-4 schema is enforced (D-082, Session 021).
# Checks 16, 17, 19 apply only to sessions numbered >= this constant.
# Check 18 is presence-gated (fires only when oi-004-retrospective.md exists).
# See specifications/validation-approach.md v4 "Gating Conventions (checks 16-19)".
readonly CRITERION4_ARTICULATION_SESSION=21

# Closed set of acceptable participant_organisation values (D-082 R3, Session 021).
# Extensible by named decision per multi-agent-deliberation.md v4 §Acceptable
# Participant Kinds. Membership check used by check 19.
readonly PARTICIPANT_ORGANISATION_CLOSED_SET="anthropic openai google meta xai mistral deepseek cohere local human-individual other-named"

WORKSPACE_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PASS=0
FAIL=0
WARN=0

pass() { PASS=$((PASS + 1)); echo "  ✓ $1"; }
fail() { FAIL=$((FAIL + 1)); echo "  ✗ $1"; }
warn() { WARN=$((WARN + 1)); echo "  ⚠ $1"; }

echo "=== Methodology Validation Report ==="
echo "Workspace: $WORKSPACE_ROOT"
echo "Date: $(date +%Y-%m-%d)"
echo ""
echo "--- Tier 1: Structural Checks ---"
echo ""

# [1] Required top-level files
echo "[1] Required files"
for f in PROMPT.md SESSION-LOG.md open-issues.md; do
  if [[ -f "$WORKSPACE_ROOT/$f" ]]; then
    pass "$f exists"
  else
    fail "$f missing"
  fi
done
echo ""

# [2] Required directories
echo "[2] Required directories"
for d in specifications provenance; do
  if [[ -d "$WORKSPACE_ROOT/$d" ]]; then
    pass "$d/ exists"
  else
    fail "$d/ missing"
  fi
done
echo ""

# [3] Specification frontmatter
echo "[3] Specification frontmatter"
shopt -s nullglob
specs=("$WORKSPACE_ROOT"/specifications/*.md)
shopt -u nullglob
if [[ ${#specs[@]} -eq 0 ]]; then
  warn "No specifications found"
else
  for spec in "${specs[@]}"; do
    name=$(basename "$spec")
    if ! head -1 "$spec" | grep -q '^---$'; then
      fail "$name — no YAML frontmatter"
      continue
    fi
    frontmatter=$(awk 'BEGIN{n=0} /^---$/{n++; next} n==1{print}' "$spec")
    missing=""
    for field in title version status created last-updated supersedes; do
      if ! echo "$frontmatter" | grep -q "^${field}:"; then
        missing="${missing} ${field}"
      fi
    done
    if [[ -z "$missing" ]]; then
      pass "$name — all required fields present"
    else
      fail "$name — missing:${missing}"
    fi
  done
fi
echo ""

# [4] Specification sections
echo "[4] Specification sections"
for spec in "${specs[@]}"; do
  name=$(basename "$spec")
  missing=""
  for section in Purpose Specification Validation; do
    if ! grep -q "^## ${section}" "$spec"; then
      missing="${missing} ${section}"
    fi
  done
  if [[ -z "$missing" ]]; then
    pass "$name — all required sections present"
  else
    fail "$name — missing sections:${missing}"
  fi
done
echo ""

# [5] Provenance directory naming
echo "[5] Provenance directory naming"
shopt -s nullglob
provdirs=("$WORKSPACE_ROOT"/provenance/*/)
shopt -u nullglob
if [[ ${#provdirs[@]} -eq 0 ]]; then
  warn "No provenance directories found"
else
  for dir in "${provdirs[@]}"; do
    dirname=$(basename "$dir")
    if [[ "$dirname" =~ ^[0-9]{3}-.+ ]]; then
      pass "$dirname"
    else
      fail "$dirname — does not match NNN-title pattern"
    fi
  done
fi
echo ""

# [6] Session log completeness
echo "[6] Session log completeness"
for dir in "${provdirs[@]}"; do
  dirname=$(basename "$dir")
  session_num=$(echo "$dirname" | grep -o '^[0-9]\{3\}')
  session_int=$((10#$session_num))
  if grep -qE "\|[[:space:]]*0*${session_int}[[:space:]]*\|" "$WORKSPACE_ROOT/SESSION-LOG.md" 2>/dev/null; then
    pass "Session ${session_num} in SESSION-LOG.md"
  else
    fail "Session ${session_num} missing from SESSION-LOG.md"
  fi
done
echo ""

# [7] Provenance directories non-empty
echo "[7] Provenance directory contents"
for dir in "${provdirs[@]}"; do
  dirname=$(basename "$dir")
  shopt -s nullglob
  files=("$dir"*.md)
  shopt -u nullglob
  if [[ ${#files[@]} -gt 0 ]]; then
    pass "$dirname — ${#files[@]} file(s)"
  else
    fail "$dirname — empty (no .md files)"
  fi
done
echo ""

# [8] Provenance frontmatter
echo "[8] Provenance frontmatter"
for dir in "${provdirs[@]}"; do
  for prov in "$dir"*.md; do
    [[ -f "$prov" ]] || continue
    relpath="$(basename "$(dirname "$prov")")/$(basename "$prov")"
    if ! head -1 "$prov" | grep -q '^---$'; then
      fail "$relpath — no YAML frontmatter"
      continue
    fi
    frontmatter=$(awk 'BEGIN{n=0} /^---$/{n++; next} n==1{print}' "$prov")
    missing=""
    for field in session title date status; do
      if ! echo "$frontmatter" | grep -q "^${field}:"; then
        missing="${missing} ${field}"
      fi
    done
    if [[ -z "$missing" ]]; then
      pass "$relpath"
    else
      fail "$relpath — missing:${missing}"
    fi
  done
done
echo ""

# [9] Decision record quality
echo "[9] Decision record quality"
found_decisions=false
for dir in "${provdirs[@]}"; do
  for f in "$dir"*decision*.md "$dir"*decisions*.md; do
    [[ -f "$f" ]] || continue
    found_decisions=true
    relpath="$(basename "$(dirname "$f")")/$(basename "$f")"
    if grep -qi "rejected alternative" "$f"; then
      pass "$relpath — includes rejected alternatives"
    else
      warn "$relpath — no rejected alternatives found"
    fi
  done
done
if ! $found_decisions; then
  warn "No decision records found"
fi
echo ""

# [10] Provenance immutability (basic heuristic)
echo "[10] Provenance immutability"
if command -v git &>/dev/null && git -C "$WORKSPACE_ROOT" rev-parse --git-dir &>/dev/null 2>&1; then
  uncommitted=$(git -C "$WORKSPACE_ROOT" diff --name-only -- provenance/ 2>/dev/null || true)
  staged=$(git -C "$WORKSPACE_ROOT" diff --cached --name-only -- provenance/ 2>/dev/null || true)
  if [[ -z "$uncommitted" && -z "$staged" ]]; then
    pass "No uncommitted changes to provenance/"
  else
    warn "Uncommitted changes in provenance/ (may be current session's work-in-progress)"
  fi
else
  warn "Git not available — skipping immutability check"
fi
echo ""

# [11] Multi-agent three-raw-output floor (D-028, D-030)
# Gate: a session directory containing at least one file matching *-perspective-*.md
# is multi-agent; verify ≥3 such files exist.
echo "[11] Multi-agent three-raw-output floor"
for dir in "${provdirs[@]}"; do
  dirname=$(basename "$dir")
  shopt -s nullglob
  perspective_files=("$dir"*-perspective-*.md)
  shopt -u nullglob
  if [[ ${#perspective_files[@]} -eq 0 ]]; then
    continue  # not a multi-agent session; out-of-scope
  fi
  if [[ ${#perspective_files[@]} -ge 3 ]]; then
    pass "$dirname — ${#perspective_files[@]} raw perspective files"
  else
    fail "$dirname — only ${#perspective_files[@]} raw perspective file(s); multi-agent requires ≥3"
  fi
done
echo ""

# [12] Heterogeneous-participant schema well-formedness (D-028, D-030)
# Gate: a session directory containing a manifests/ subdirectory.
# For each *.manifest.yaml in manifests/, verify D-024 required fields are present as literal keys.
# Stores per-session fail state in BLOCKED_SESSIONS (space-separated) for the sequencing
# rule (D-030 §3). Uses a flat string rather than associative array for bash 3.2 compatibility.
BLOCKED_SESSIONS=""
echo "[12] Heterogeneous-participant schema well-formedness"
D024_REQUIRED_FIELDS=(
  perspective participant_kind participant_identity
  model_family model_id model_version provider endpoint invocation_method
  sampling training_lineage_overlap_with_claude
  participant_selected_by participant_selection_method
  identity_known context_source delivered_at received_at
  raw_response_file transport_notes output_edited_after_submission
  participation_shape
)
D024_SAMPLING_SUBFIELDS=(temperature top_p max_tokens)
for dir in "${provdirs[@]}"; do
  dirname=$(basename "$dir")
  manifests_dir="${dir}manifests"
  if [[ ! -d "$manifests_dir" ]]; then
    continue  # no manifests/ directory; out-of-scope (D-030 §1)

exec
/bin/zsh -lc "sed -n '1,220p' specifications/workspace-structure.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
---
title: Workspace Structure
version: 3
status: active
created: 2026-04-17
last-updated: 2026-04-22
updated-by-session: 020
supersedes: workspace-structure-v2.md
---

# Workspace Structure

## Purpose

This specification defines how the workspace is organized: what directories and files exist, what each contains, and how they relate. It ensures that any agent or person reading the workspace can orient themselves quickly and knows where to find — and where to put — each kind of content.

Version 3 (Session 017, D-074) adds the three file-class distinction (engine-definition / development-provenance / application-scope) and documents `prompts/` as a new directory created by the PROMPT.md split. v2 preserved as `workspace-structure-v2.md`.

## Specification

### File classes (added v3)

Under the three-layer denotation established in `identity.md` v2 (Selvedge methodology / Selvedge engine / application), workspace files fall into one of three classes:

- **Engine-definition files** — the loadable Selvedge engine. An external application workspace may (and should) clone this set without inheriting development-provenance. Enumerated canonically by `specifications/engine-manifest.md`. At `engine-v1`: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `specifications/*.md` (all active files in the `specifications/` directory), `tools/validate.sh`.
- **Development-provenance files** — the self-development application's own accumulated history. Not part of the engine load; not inherited by external-application workspaces by default. Includes `SESSION-LOG.md`, `open-issues.md`, and `provenance/`.
- **Application-scope files** — per-application content (inputs, outputs, application-specific briefs and notes). Mutable per the `applications/` directory rules below. Organised as `applications/NNN-<slug>/`.

The normative rule: an external application workspace may load the engine-definition set as a read-only unit (or a cloned starting point) without inheriting development-provenance. The self-development application (this workspace) carries all three classes by construction (the engine is being developed here; the provenance is the development record; the applications are the by-products).

### Top-level structure

The workspace has the following top-level structure:

```
/PROMPT.md
/prompts/
  development.md
  application.md
/SESSION-LOG.md
/open-issues.md
/specifications/
/provenance/
/tools/
/applications/
```

### PROMPT.md

The bootstrap prompt. Under v3 (D-074, Session 017) `PROMPT.md` is a thin **dispatcher**: it names the three layers (methodology / engine / application), names the two operating modes (self-development and external-problem), and points to the two mode-specific executable prompts in `prompts/`. It is part of the engine-definition file class. It may be revised, but any revision is a significant event and recorded in provenance (as it was when the v3 split occurred in Session 017). The self-development application's executable content was moved to `prompts/development.md`; the template for external-problem applications lives at `prompts/application.md`.

### prompts/

Contains the two mode-specific executable prompts created by the D-074 split. Part of the engine-definition file class.

- `prompts/development.md` — the self-development application's executable prompt. Carries the content that was in the pre-split `PROMPT.md` (minus the high-level framing moved up into the dispatcher), reframed as the engine's own self-development. This workspace's current application loads this file.
- `prompts/application.md` — the template for external-problem applications. Loads the engine by reference (engine-manifest), names the slots an external application fills (problem statement, constraints, stakeholders, success condition, initial state), and declares that development-provenance is NOT part of the application's context unless explicitly imported. An external application workspace copies this file (typically renamed to `PROMPT.md` in the new workspace, or loaded from its canonical location here) and fills in the slots.

Both files are revisable under the methodology's spec-revision discipline (significant revisions recorded in provenance; v-suffix preservation if substantive changes accumulate).

### SESSION-LOG.md

A running index of sessions for quick orientation. Each entry is one line (one Markdown table row) containing the session number, date, title, and a summary of what was accomplished. The summary length scales to session complexity: planning-only, single-perspective, or assessment-only sessions produce shorter summaries; deliberation sessions producing substantive spec revisions, cross-model influences, or external artefacts produce longer summaries calibrated to record the decision surface and load-bearing influences. The canonical detail for each session lives in its provenance `03-close.md` file; the SESSION-LOG entry is an index over that detail, not a replacement. This file is updated at the close of each session.

### open-issues.md

A list of known questions, gaps, uncertainties, and unresolved disagreements. Each entry has a brief description, the session that identified it, and its current status. Issues are removed when resolved (with a reference to the session that resolved them). This is a single file, not a directory, unless the number of issues makes a single file unwieldy.

### specifications/

Contains the living specifications that describe the methodology's current state. Each specification is a Markdown file with YAML frontmatter:

```yaml
---
title: [what this specifies]
version: [integer, starting at 1]
status: draft | active | superseded | deprecated
created: [date]
last-updated: [date]
supersedes: [path to prior version, or "none"]
---
```

The body of each specification has three sections:

1. **Purpose** — What this specification governs and why it exists
2. **Specification** — The normative content
3. **Validation** — How to verify this specification still describes reality

When a specification undergoes substantive revision, the prior version is preserved with a version suffix (e.g., `workspace-structure-v1.md`) and the new version takes the canonical filename. Minor corrections are committed through git without file-level versioning.

Status lifecycle:
- **draft** — Proposed but not yet deliberated and accepted
- **active** — Deliberated, accepted, and governing
- **superseded** — Replaced by a newer version (the `supersedes` chain connects them)
- **deprecated** — No longer relevant because the thing it governed no longer exists

### provenance/

Contains the historical reasoning records. Organized by session:

```
/provenance/
  /001-genesis/
    00-survey.md
    01-deliberation.md
    02-decisions.md
  /002-[title]/
    ...
```

Each session's provenance is a numbered directory. Files within are numbered for reading order. All provenance files use Markdown with YAML frontmatter:

```yaml
---
session: [number]
title: [title]
date: [date]
status: complete | in-progress
---
```

Provenance records are **immutable** once the session closes. Errors or retractions are recorded in subsequent sessions, not by editing past records.

### tools/

Contains tooling that supports the methodology's operations. Tools are executable scripts or programs that automate aspects of the methodology (e.g., validation, reporting). Each tool should have a corresponding specification in `specifications/`.

Current contents:
- `validate.sh` — Two-tier validation tool (see `specifications/validation-approach.md`)

### applications/

Contains **external artefacts** — work-products the methodology has produced for use outside the workspace (specifications, sequences, templates, design fragments, and the like). Organized by the session that originally produced the artefact:

```
/applications/
  /NNN-[slug]/
    [artefact-files]
```

`NNN` is the producing session's number; `[slug]` is a short descriptive name. Filenames within the directory are descriptive (not numbered for reading order) — the numbered-reading-order convention applies to provenance records only.

External artefacts are **mutable**: they may be revised by later sessions in response to domain validation (see `methodology-kernel.md` §7 Domain validation) or other feedback. Revisions update the artefact in place; the revising session's provenance records what changed and why. When an artefact is revised, any corresponding copies in the originating session's provenance directory and in prior revising sessions' provenance remain untouched (per the provenance immutability rule) and serve as historical witnesses to earlier versions.

Each external artefact file includes in its frontmatter the fields `originating_session` (the session that first produced the artefact) and, when applicable, `regularized_in_session` (the session that moved the artefact into `applications/` after the fact) and `provenance_witness_path` (the path to the frozen provenance copy, if one exists). Subsequent revisions update `last-revised-session` in the frontmatter.

**Regularization of pre-existing external artefacts.** When an external artefact was placed in a producing session's provenance directory before `applications/` existed as a defined top-level directory, the artefact is regularized into `applications/` by **copy-plus-reference**: a copy is made to `applications/NNN-[slug]/[filename]` with the frontmatter fields above; the provenance copy is not moved, modified, or deleted. The regularizing session's decision record is the authoritative cross-reference.

### Additional directories

New top-level directories may be created by future sessions when the work demands them (e.g., `implementations/`, `examples/`). Any new directory should be documented by updating this specification. `applications/` was defined by Session 009 (D-054) for external artefacts and is no longer a hypothetical example.

## Validation

To validate this specification:

1. Check that all top-level elements listed above exist in the workspace
2. Check that each specification in `specifications/` has the required frontmatter fields and three body sections
3. Check that each provenance directory follows the naming convention `NNN-title/`
4. Check that `SESSION-LOG.md` has an entry for every provenance directory
5. Check that no provenance record dated before the current session has been modified since its session closed (immutability check via git)
6. Check that each directory in `applications/` corresponds to an external artefact produced or regularized in a session whose decision record in provenance authorises its presence
7. Check that every external artefact file in `applications/` carries the `originating_session` frontmatter field; for regularized artefacts, also `regularized_in_session` and `provenance_witness_path`

exec
/bin/zsh -lc "sed -n '1,220p' specifications/methodology-kernel.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
---
title: Methodology Kernel
version: 4
status: active
created: 2026-04-17
last-updated: 2026-04-22
updated-by-session: 014
supersedes: methodology-kernel-v3.md
---

# Methodology Kernel

## Purpose

This specification defines the core process of the methodology: what happens during each application of the prompt, in what order, and to what standard. It is the minimum viable process — the kernel that every session follows. As the methodology matures, additional specifications may elaborate on individual activities, but this kernel defines the overall shape.

This specification defines the Selvedge methodology kernel: the abstract execution semantics that a conforming engine must realise. `specifications/engine-manifest.md` enumerates the files that constitute the current engine; `specifications/identity.md` establishes the denotation layering (Selvedge names the methodology; "Selvedge engine" denotes the current executable implementation; each session is an application of that engine). The kernel applies equally to the self-development application and to external-problem applications.

## Specification

### Application Model

The methodology advances by **sessions**. Each session is one application of PROMPT.md to the workspace. A session reads the full workspace state, determines what work is needed, does that work through multi-perspective deliberation, produces artifacts, and closes cleanly.

Each session advances the workspace by **one increment** — a coherent unit of progress that leaves the workspace in a better state than it found it. The size of an increment is a judgment call informed by the work at hand; it is not time-boxed.

### The Nine Activities

Each session performs nine activities. These are a **vocabulary, not a strict sequence**. They have a general flow (you cannot decide before you deliberate) but permit recursion (deliberation may reveal the need for more reading).

#### 1. Read

Absorb what the session will reason from before changing anything. In every session this includes **workspace reading**: the full current state of the workspace — every file, every specification, every provenance record, and, where relevant, recent version-control history. Build a complete picture of the workspace's own state.

When the session produces or revises an artefact intended for use outside the workspace, it also includes **domain reading**: the domain constraints the session operates under (stated by the user or operator in-session), cited external materials introduced into the session, and domain knowledge that the orchestrating agent surfaces explicitly as input to the work. Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step (per PROMPT.md). Perspective pretraining enters the session via stance briefs and perspective responses, not via §1 Read.

This is a receptive activity. Its output is understanding, not artifacts.

#### 2. Assess

Determine what state the methodology is in and what this session should address. State the determination explicitly so future sessions have a record of what was inferred.

Assessment questions:
- What is the most important work the workspace needs right now?
- Are existing specifications consistent with each other and with reality?
- Are there open issues that should be addressed?
- Is there work from a prior session that needs continuation?
- Is the methodology itself showing signs of strain (stale specifications, unaddressed issues, loss of coherence)?

This activity produces the session's **agenda**: a statement of what will be worked on and why.

#### 3. Convene

Assemble perspectives suited to the work at hand. Name each perspective, describe its stance, and record why it was chosen.

For deliberative work (where decisions will be made), at least one perspective must be **adversarial** — its role is to challenge the emerging consensus, identify unstated assumptions, and argue for alternatives.

The choice of perspectives shapes outcomes and should be treated as a design decision, not an afterthought.

When a decision meets the triggers defined in `specifications/multi-agent-deliberation.md`, perspectives must be instantiated as independent agents whose outputs are synthesised rather than as multiple voices produced within a single context. Decisions that meet those triggers but are made single-perspective anyway must record the reason.

#### 4. Deliberate

Reason together from multiple perspectives. Each perspective contributes its genuine position on the questions at hand.

Requirements:
- Perspectives state positions before hearing others (to prevent anchoring)
- Disagreements are preserved in the record, even when resolved
- Alternatives are articulated, not just dismissed
- Uncertainty is flagged explicitly

This activity produces the richest provenance. The record should capture not just conclusions but the reasoning that led to them.

#### 5. Decide

Make concrete decisions with rationale. Each decision records:
- What was decided
- Why (the key arguments that carried it)
- What was rejected and why
- What remains open

Decisions are distinct from deliberations. A deliberation explores options; a decision commits to one.

#### 6. Produce

Create or update the artifacts that the decisions warrant. This may include:
- New specifications
- Revisions to existing specifications
- Updates to open issues
- New workspace structure

Artifacts should be produced to the standard defined in their respective specifications (e.g., specifications have the required frontmatter and three sections).

#### 7. Validate

Validate the session's output at each level on which it makes claims. Three senses apply.

**Workspace validation** applies to every session. Check that:
- New specifications don't contradict existing ones
- Specifications describe the workspace as it actually is
- Provenance records are complete and well-formed
- Open issues reflect the actual state of uncertainty

**Domain validation** applies when a session produces or revises an artefact intended for use outside the workspace and a domain-actor is available. Obtain evidence from the domain-actor who holds the problem the artefact addresses — the user of a sequence, the reader of a specification, the participant in a process, or an equivalent — that the artefact functioned for its intended use. Record who performed the validation, what was tried, what happened, and whether modifications were requested. Domain validation may complete out-of-session; when it does, the receiving session records the report and decides whether it triggers revision.

**Reference validation** applies when a session produces an external-intent artefact and no domain-actor is available. A reference-validation exercise pairs the methodology's Produce step (run blind against a staged constraint tranche set whose emergent constraints surface during the run) with comparison against a pre-selected documented proven solution the Produce agents do not see. The exercise runs across a small number of sessions in a sealed three-cell protocol (Curation, Produce, Validation) specified in `specifications/reference-validation.md`. The exercise records constraint-satisfaction, structural correspondence, cross-model divergence, and a contamination audit.

**Reference validation supplies evidence about the methodology's capacity to derive artefacts under stated constraints. It does not establish that the artefact functioned in its intended use. It does not substitute for Domain validation when a domain-actor is available.** Artefacts passing reference-validation carry the label `validation: reference-validated` in frontmatter and retain that scoping in any later citation.

If any validation reveals problems, they are either fixed in this session (return to Produce) or recorded as open issues for subsequent sessions.

#### 8. Record

Commit provenance to the workspace. Ensure all deliberations, decisions, and the reasoning behind them are captured in the session's provenance directory.

This activity is about completeness and permanence. Nothing decided or considered in this session should be lost.

#### 9. Close

Verify the workspace is in a coherent state:
- All new and modified files are committed to version control
- SESSION-LOG.md is updated with this session's entry
- open-issues.md reflects any new issues or resolved issues
- A statement of what the next session should address is included in the session log or provenance

### Continuity Rules

- **Read prior provenance before proposing.** If an idea was considered and rejected in a prior session, do not silently re-propose it. Cite the prior rejection and explain what has changed.
- **Do not overwrite silently.** When a specification is revised, preserve the prior version and make the succession traceable.
- **Preserve all provenance.** Do not delete historical records, even when they feel outdated.
- **Leave coherent state.** If work cannot complete, commit what was produced, document the blocker, and close cleanly.

### Self-Hosting

The methodology is self-hosting: it evolves by applying its own process to itself. This means:
- The methodology's specifications are subject to the same deliberation, decision, and versioning processes as any other artifact
- The methodology can revise its own kernel (this specification) through a regular session
- Changes to the kernel are recorded in provenance like any other decision
- The kernel should be revised when the process it describes no longer matches the process actually followed, or when a better process is discovered

## Validation

To validate this specification:

1. Review the most recent session's provenance and check that all nine activities were performed (or that their omission was explained — e.g., Convene is not needed for pure validation work)
2. Check that deliberative sessions included at least one adversarial perspective
3. Check that decisions record rejected alternatives, not just the chosen option
4. Check that SESSION-LOG.md is up to date
5. Check that no provenance from closed sessions has been modified
6. Ask: did the session's Read activity successfully use prior provenance to understand past decisions? If not, the provenance format or depth may need revision

codex
The live files match the brief’s core tension: `prompts/development.md` still says “read the workspace completely,” the kernel still says “every file,” `CLAUDE.md` still carries the mempalace paragraph, and the validator has no size-budget notion yet. I’m checking the deliberation/validation specs and a few concrete workspace facts next so the stance can make specific operational claims.
exec
/bin/zsh -lc "nl -ba prompts/development.md | sed -n '17,45p'" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "nl -ba specifications/methodology-kernel.md | sed -n '28,42p'" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
    28	
    29	Each session performs nine activities. These are a **vocabulary, not a strict sequence**. They have a general flow (you cannot decide before you deliberate) but permit recursion (deliberation may reveal the need for more reading).
    30	
    31	#### 1. Read
    32	
    33	Absorb what the session will reason from before changing anything. In every session this includes **workspace reading**: the full current state of the workspace — every file, every specification, every provenance record, and, where relevant, recent version-control history. Build a complete picture of the workspace's own state.
    34	
    35	When the session produces or revises an artefact intended for use outside the workspace, it also includes **domain reading**: the domain constraints the session operates under (stated by the user or operator in-session), cited external materials introduced into the session, and domain knowledge that the orchestrating agent surfaces explicitly as input to the work. Domain reading enlarges what must be understood; it does not permit silent import of outside ideas. Knowledge not already present in the workspace or in the session's explicit domain inputs must still be introduced through an explicit surveying or hypothesising step (per PROMPT.md). Perspective pretraining enters the session via stance briefs and perspective responses, not via §1 Read.
    36	
    37	This is a receptive activity. Its output is understanding, not artifacts.
    38	
    39	#### 2. Assess
    40	
    41	Determine what state the methodology is in and what this session should address. State the determination explicitly so future sessions have a record of what was inferred.
    42	

 succeeded in 0ms:
    17	## How to operate
    18	
    19	Begin by reading the workspace completely. Every file, every document, every historical record, every commit message if the workspace is under version control. Build a full picture of what exists before changing anything.
    20	
    21	From that reading, determine what state the methodology is in and what should happen next. If the workspace has not yet defined its own structure, the first work is to do so — by surveying prior approaches, reasoning about what this methodology needs, and committing a proposed shape along with the reasoning that led to it. If the workspace has defined a structure but not yet applied it, the next work is to begin applying it. If the structure has been applied but produces artefacts that have not been validated, the next work is validation. If everything has been exercised at least once, the methodology is in evolution mode — identify the weakest aspect of the current system and do whatever work addresses it.
    22	
    23	State your determination explicitly at the start of each session, so the next application of this prompt has a clear record of what you inferred and why.
    24	
    25	Before doing any substantive work, read everything the workspace has preserved about prior decisions. If an idea was considered and rejected earlier, do not silently re-propose it. If you believe a rejected idea deserves reconsideration, cite the prior rejection and explain what has changed. Continuity of reasoning is the whole point of preserving provenance.
    26	
    27	Substantive work in this methodology should not be done by a single perspective. Convene a group of AI agents with genuinely different viewpoints suited to the work at hand. Some perspectives generate options, some challenge them, some attend to what is unknown, some attend to what has been ignored, some reason about how the work will be received by those who must live with it. The specific perspectives, their number, and how they collaborate are for you to develop. Over repeated applications, patterns will emerge — document them when they do, so future applications can build on what worked.
    28	
    29	The work should produce a concrete output: a structured record of what was proposed, what was decided, what was rejected with reasoning, and what remains uncertain. This record is the provenance. Commit it to the workspace in a way that preserves it permanently and makes it findable by future applications. Alongside the provenance, update or create whichever artefacts the work warrants. If the work produced a new specification, write the specification. If it produced an implementation, build it. If it surfaced problems, record them where subsequent work will find them. The structure of the workspace should evolve to serve the methodology, not the other way around.
    30	
    31	Before ending the session, verify the workspace is in a coherent state. Specifications describe the engine as it currently is. Validations pass against those specifications, or their failures are documented as open issues for subsequent work to address. Any human-facing summary of the workspace accurately reflects its current state. Every piece of work done in this session has committed its provenance.
    32	
    33	## Rules that hold across applications
    34	
    35	These rules apply to both the self-development application and to external-problem applications of the engine.
    36	
    37	Do not import ideas from outside the process. If an insight arrived through reading something unrelated, a conversation with a human, or your own pretraining, introduce it as an input to an explicit surveying or hypothesising step rather than committing it directly. The value of this methodology is that its artefacts are traceable to the reasoning that produced them.
    38	
    39	Do not skip steps. Each piece of work's output is the next piece's input, and skipping breaks the chain of reasoning that makes the methodology evolveable.
    40	
    41	Do not overwrite prior specifications silently. When a specification is revised, preserve the prior version and make the succession traceable. The form of that preservation — filenames, directory structure, supersession markers, or something else — is for you to develop. Whatever you choose, be consistent so future readers can follow the thread.
    42	
    43	Preserve all provenance. Do not delete historical records, even when they feel embarrassing or outdated. A rejected idea from long ago may be the key to understanding a decision made today.
    44	
    45	Leave the workspace in a coherent state at the end of every application. If a piece of work cannot complete, commit what was produced, document the blocker, and end cleanly rather than leaving work in an indeterminate state.

exec
/bin/zsh -lc "sed -n '1,260p' specifications/validation-approach.md" in /Users/ericmccowan/Development/complex-systems-engine
exec
/bin/zsh -lc "sed -n '1,220p' prompts/application.md" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
You are operating on an **external-problem application** of the **Selvedge engine**. This application runs the engine against a specific problem that is not the engine's own development. You have loaded the engine definition (the files enumerated in `specifications/engine-manifest.md` §3) and are now executing the engine against this application's context.

Selvedge is the methodology (abstract approach). The Selvedge engine is its current loadable implementation. This application is one specific run of that engine; it has its own inputs, its own artefacts, its own validation pathway, and its own provenance. The engine's development-provenance (the `SESSION-LOG.md`, `open-issues.md`, and `provenance/` of the source workspace where the engine was developed) is NOT part of this application's context unless explicitly imported by a decision in this workspace.

## This application's context

The orchestrator filling this template should replace each `<<slot>>` with the application's concrete content before the first session runs. The slots are named; their content is the application's scope.

### Problem statement

<<Problem statement. What is being designed, for whom, under what constraints. One to three paragraphs. This is the primary input to every session's Read activity for this application.>>

### Constraints

<<Constraints on the design: domain constraints (what the physical, social, or procedural domain permits or forbids), time constraints (when the artefact must exist and in what progression), stakeholder constraints (who must find it usable, who must approve it, who must live with its consequences). Enumerate concretely.>>

### Stakeholders

<<Who holds the problem. Who will receive the artefact. Who will validate that the artefact worked (the domain-actor for Domain validation per `methodology-kernel.md` §7). If no domain-actor is available, Reference validation (per `specifications/reference-validation.md`) may substitute — the initialising session should determine.>>

### Success condition

<<What the artefact must do for this application to be considered successful. State as observable evidence, not as internal properties. Example: "a practitioner reads the artefact once and produces a usable attempt within five minutes" vs. "the artefact is clear" — the former is observable, the latter is not. Concrete success conditions make Validate possible.>>

### Initial state

<<Any materials, references, partial work, or prior context the application starts with. If starting from scratch, state "no prior materials; starting from the problem statement." If building on prior work, identify it explicitly and include references or copies in `applications/001-<slug>/` (or whichever numbered directory is first in this workspace).>>

### Engine version loaded

<<The engine version under which this application is running (e.g., `engine-v1`). Record this in every session's provenance so future readers know which engine behaviour applies. See `specifications/engine-manifest.md` §2 and §7.>>

---

## How to operate

All rules and activities from `prompts/development.md` §How to operate and §Rules that hold across applications apply to this application with the following application-specific adjustments.

### Read

The session's Read activity covers:

- **Workspace reading** — the full current state of this application's workspace (this workspace, not the engine's source workspace). Every file, every prior session's provenance, every prior artefact in `applications/`.
- **Domain reading** — this application's problem statement, constraints, stakeholders, success condition, initial state (the slots above), plus any domain materials introduced into the session.
- **Engine reading** — the loaded engine-definition files (`specifications/` + `tools/validate.sh` + `PROMPT.md` + this file). These are the normative rules the session executes under. They are not up for revision within this application's sessions unless a kernel-revision is explicitly authorised by the engine's source workspace.

### Convene and Deliberate

Per `specifications/methodology-kernel.md` §3 and `specifications/multi-agent-deliberation.md` v3, substantive work requires multi-perspective deliberation with adversarial coverage. For this application, perspectives are selected to surface the problem's specific contested dimensions. Domain perspectives (a perspective whose stance is grounded in domain knowledge — a practitioner, a stakeholder, a target audience) are expected to appear in most external-problem applications.

### Validate

Per `specifications/methodology-kernel.md` §7, three senses of validation apply. For this application:

- **Workspace validation** always applies (per session). `tools/validate.sh` runs in every session.
- **Domain validation** applies when a domain-actor (per §Stakeholders) is available. Obtain evidence from the domain-actor that the artefact functioned for its intended use.
- **Reference validation** applies when no domain-actor is available and a documented proven solution exists against which the artefact can be compared. See `specifications/reference-validation.md` for the sealed three-cell protocol.

The choice of validation sense is an application decision made at Session 001's Decide activity (or revisable at subsequent decisions).

### Produce

External artefacts live in `applications/NNN-<slug>/` per `specifications/workspace-structure.md` v3 §applications. Frontmatter includes `originating_session`, `artefact_kind`, `domain`, `engine_version`, and validation-label fields per the workspace-structure conventions.

### Record and Close

Provenance accumulates in `provenance/NNN-<slug>/` as in the self-development application. `SESSION-LOG.md` accumulates one-line session entries. `open-issues.md` accumulates application-scoped open issues (distinct from engine-scoped open issues, which live in the source workspace).

## Anti-silent-import and anti-laundering

The PROMPT.md anti-silent-import rule (no ideas from outside the process without an explicit surveying/hypothesising step) applies in full. Per OI-015's laundering-enforcement concern, domain inputs must not be absorbed as given context and re-examined as choices — they must be surveyed as options competing with alternatives at Deliberate or Decide.

## Now begin

Read the workspace (including this application's scope slots above). Determine what state the application is in and what Session 001 (or the current session) should address. Convene perspectives. Deliberate. Decide. Produce. Validate. Record. Close. Report what was done, what state the workspace is now in, and what the next application of this prompt should address.

 succeeded in 0ms:
---
title: Validation Approach
version: 4
status: active
created: 2026-04-17
last-updated: 2026-04-22
updated-by-session: 021
supersedes: validation-approach-v3.md
---

# Validation Approach

## Purpose

This specification defines how the methodology validates itself: what is checked, how checks are organized, and what the checks can and cannot assure. It serves the methodology's self-hosting principle — a methodology that cannot verify its own specifications cannot evolve reliably.

**Scope note (added as a minor correction in Session 009 per D-056).** This specification covers **Workspace validation** as defined in `methodology-kernel.md` v2 §7. **Domain validation** (the second sense of §7, concerning whether an external artefact functions in its target domain) is performed by domain-actors outside this specification's Tier 1 / Tier 2 scope and is not automated by `tools/validate.sh`. Its governance lives in the kernel §7 text itself.

**Scope note (added as a minor correction in Session 017 per D-074).** The Tier 1 structural checks and Tier 2 guided-assessment questions defined in this specification apply equally to the self-development application and to external-problem applications of the Selvedge engine. Validation is engine-level; the specific artefacts checked (and the appropriate domain-validation pathway) vary by application kind, but the two-tier discipline is invariant.

Version 4 adds four new Tier 1 checks (16, 17, 18, 19) operationalising the OI-004 criterion-4 articulation in `multi-agent-deliberation.md` v4 (D-082, Session 021), and one new Tier 2 question (Q8) paired with check 18's honest limit. It specifies gating, severity, and sequencing rules for the new checks. It supersedes v3 (`validation-approach-v3.md`).

Version 3 added two new Tier 1 checks (14, 15) that operationalised v2 `multi-agent-deliberation.md` Validation items 1 and 2 (now v3+ Validation items), and one new Tier 2 question (Q7) paired with checks 14/15's honest limits. It specified gating, severity, and sequencing rules for those checks. It superseded v2 (`validation-approach-v2.md`).

Version 2 added three new Tier 1 checks (11, 12, 13) that enforce the D-024 heterogeneous-participant schema introduced by `multi-agent-deliberation.md` v2, and one new Tier 2 question paired with check 13's honest limit. It superseded v1 (`validation-approach-v1.md`).

## Specification

### Two-Tier Model

Validation has two tiers, reflecting the distinction between properties that can be checked mechanically and those that require judgment.

**Tier 1: Structural Checks** are automated checks run by `tools/validate.sh`. They verify that the workspace's files conform to the formats and conventions defined in other specifications. Structural checks are necessary but not sufficient for methodology health — a workspace can pass all structural checks while its specifications are semantically wrong or its provenance is misleading.

**Tier 2: Guided Assessment** is a set of questions printed by the validation tool for the agent or human conducting the session to consider. These questions address properties that cannot be checked mechanically: semantic consistency, provenance usefulness, and whether the methodology is making genuine progress.

### Tier 1: Structural Checks

The following checks are automated:

| # | Check | Source Spec | Severity | Gate |
|---|-------|-------------|----------|------|
| 1 | Required top-level files exist (PROMPT.md, SESSION-LOG.md, open-issues.md) | workspace-structure | Fail | unconditional |
| 2 | Required directories exist (specifications/, provenance/) | workspace-structure | Fail | unconditional |
| 3 | Each specification has YAML frontmatter with required fields (title, version, status, created, last-updated, supersedes) | workspace-structure | Fail | unconditional |
| 4 | Each specification has three required section headings (Purpose, Specification, Validation) | workspace-structure | Fail | unconditional |
| 5 | Provenance directories follow NNN-title naming convention | workspace-structure | Fail | unconditional |
| 6 | Session log has an entry for each provenance directory | workspace-structure | Fail | unconditional |
| 7 | Each provenance directory contains at least one .md file | methodology-kernel | Fail | unconditional |
| 8 | Provenance files have YAML frontmatter with required fields (session, title, date, status) | workspace-structure | Fail | unconditional |
| 9 | Decision records include rejected alternatives sections | methodology-kernel | Warning | unconditional |
| 10 | No uncommitted changes to provenance files (basic immutability heuristic) | workspace-structure | Warning | unconditional |
| 11 | Multi-agent three-raw-output floor: ≥3 files matching `*-perspective-*.md` | multi-agent-deliberation (v2 Validation #3) | Fail | session has ≥1 `*-perspective-*.md` file |
| 12 | Heterogeneous-participant schema well-formedness: each `manifests/*.manifest.yaml` has all D-024 required fields as literal keys | multi-agent-deliberation (v2 Validation #8) | Fail | session has `manifests/` subdirectory |
| 13 | Cross-model-claim honesty: `cross_model: true` implies ≥1 manifest with `training_lineage_overlap_with_claude` other than `known-overlap` OR `participant_kind: human` | multi-agent-deliberation (v2 Validation #9) | Fail | session declares `cross_model: true` AND check 12 passed for that session |
| 14 | Multi-agent trigger coverage: decision declares any `d016_*` trigger implies ≥3 raw perspective files plus synthesis OR `**Single-agent reason:**` annotation on the decision | multi-agent-deliberation (v3 Validation #1 operationalised) | Fail | session ≥ 006 AND session has ≥1 decision record with `**Triggers met:**` line |
| 15 | Non-Claude trigger coverage: decision declares any `d023_*` trigger implies ≥1 manifest with `participant_kind` outside `{claude-subagent, anthropic-other}` OR `**Non-Claude participation:**` skip annotation with `reason:` and `retry_in_session:` sub-fields | multi-agent-deliberation (v3 Validation #2 operationalised) | Fail | session ≥ 006 AND check 12 passed for that session |
| 16 | Independent-claim evidence-pointer presence: each manifest with `training_lineage_overlap_with_claude: independent-claim` has non-empty `training_lineage_evidence_pointer:` field | multi-agent-deliberation v4 §Heterogeneous-Participant Recording Schema | Fail | session ≥ 021 |
| 17 | Claude-output-in-training disclosure: each manifest with `participant_kind` in `{non-anthropic-model, human}` has a `claude_output_in_training:` field whose value is in `{known-yes, known-no, unknown, n/a}` | multi-agent-deliberation v4 §Heterogeneous-Participant Recording Schema | Fail | session ≥ 021 |
| 18 | OI-004 closure-retrospective well-formedness: any `provenance/*/oi-004-retrospective.md` artefact contains the three required sections `## Qualifying Deliberations Table`, `## Summary Tally`, `## P4 Assertion` | multi-agent-deliberation v4 §Closure Procedure for OI-004 | Fail | presence of `oi-004-retrospective.md` artefact |
| 19 | Non-Anthropic participant_organisation closed-set membership: each manifest with `participant_kind: non-anthropic-model` has non-empty `participant_organisation:` field whose value is in the spec-enumerated closed set | multi-agent-deliberation v4 §Acceptable Participant Kinds for OI-004 | Fail | session ≥ 021 |

Checks marked **Fail** cause the tool to exit with a non-zero code. Checks marked **Warning** are reported but do not cause failure.

### Gating Conventions (checks 11, 12, 13)

**Presence-gating.** Checks 11, 12, and 13 apply only to sessions whose provenance exhibits the relevant artefact. A session without any `*-perspective-*.md` files is not a multi-agent session and is out-of-scope for check 11. A session without a `manifests/` subdirectory has not adopted the D-024 schema and is out-of-scope for check 12 (and by extension, check 13). Out-of-scope sessions produce no output from the gated check — no warning, no failure.

**Consequence for prior sessions.** Sessions 001 (Genesis) and 002 (Self-Validation) are not multi-agent; they are out-of-scope for all three new checks. Session 003 and Session 004 are multi-agent (have perspective files) but did not produce a `manifests/` subdirectory; they are in-scope for check 11 and out-of-scope for checks 12 and 13. Session 005 and later sessions that adopt the full schema are in-scope for all three.

**Rationale for the gate granularity.** Gating at `manifests/` subdirectory presence — rather than at `participants.yaml` presence or at session-number — was chosen to (a) keep Session 004's bootstrap-exempt minimal `participants.yaml` naturally out-of-scope without requiring an inline exemption list, (b) avoid encoding a numeric session cutoff that must be maintained in the tool, and (c) produce the same outcome in practice as session-number gating (Session 005 is the first session to have a `manifests/` subdirectory). This decision is recorded in D-030 (Session 005) along with the genuine cross-model disagreement that preceded it.

### Gating Conventions (checks 14, 15) — Session-number gating

**Session-number-gating.** Checks 14 and 15 apply only to sessions numbered ≥ 006. The gate is encoded as an explicit constant `TRIGGERS_MET_ADOPTION_SESSION=6` near the top of `validate.sh` so a future reader can see the history in one line. Out-of-scope sessions (001 through 005) produce no output from these checks — no warning, no failure.

**Rationale for session-number gating here (distinct from check 12's artefact-presence gating).** Session 006 deliberated (D-039) on whether to use presence-gating (as with checks 11–13) or session-number gating for checks 14 and 15. The cross-perspective result: three of four perspectives (Archivist, Skeptic, Outsider — cross-model) converged on session-number gating; one (Implementer) preferred presence-gating. The decisive arguments were (a) ambiguity of absence under presence-gating (a missing `**Triggers met:**` line cannot be distinguished from "pre-adoption" vs "author forgot"), and (b) bypass-by-omission: presence-gating invites operators who want to avoid a check to simply omit the triggering field. Session-number gating makes absence in a post-adoption session unambiguously a failure. This is the same cross-perspective divergence pattern that Session 005 faced (D-030); the resolution here is the opposite because the failure-mode calculus differs — check 12's artefact-presence gating could not be gamed-by-omission (the `manifests/` directory is a substantive artefact, not a trivially-omittable field), whereas `**Triggers met:**` can be trivially omitted.

**Consequence for prior sessions.** Sessions 001 through 005 are out-of-scope for checks 14 and 15. Session 006 and later sessions must include `**Triggers met:**` on every decision record (with `[none]` if no triggers fired).

### Gating Conventions (checks 16, 17, 19) — Session-number gating; Check 18 — presence-gating

**Session-number-gating (checks 16, 17, 19).** Apply only to sessions numbered ≥ 021. The gate is encoded as an explicit constant `CRITERION4_ARTICULATION_SESSION=21` near the top of `validate.sh` so a future reader can see the history in one line. Out-of-scope sessions (001 through 020) produce no output from these checks — no warning, no failure.

**Rationale for session-number gating.** Checks 16, 17, 19 enforce schema fields introduced by `multi-agent-deliberation.md` v4 §Heterogeneous-Participant Recording Schema (D-082, Session 021). Pre-adoption manifests do not have these fields and cannot have them retroactively per the immutability rule (D-017). Per the Session 006 D-039 precedent for checks 14/15, session-number gating is the correct mechanism for prospective-only schema adoption. Presence-gating would create the ambiguity-of-absence problem (a missing `claude_output_in_training:` field cannot be distinguished from "pre-adoption" vs "author forgot").

**Presence-gating (check 18).** Check 18 fires only when an `oi-004-retrospective.md` file is present anywhere under `provenance/*/`. The artefact does not exist until a future session writes it; pre-existence sessions are out-of-scope. Once written, check 18 verifies structural well-formedness; substantive adequacy is Tier 2 Q8 (paired).

**Out-of-scope behaviour for participant_kind values.** Check 17 is out-of-scope for `participant_kind` in `{claude-subagent, anthropic-other}` (no Claude-output disclosure required for Claude-family participants). Check 19 is out-of-scope for `participant_kind` other than `non-anthropic-model` (organisational origin closed-set membership is required only for non-Anthropic LLM participants). These are recorded inline in the validate.sh check implementation and in the honest-limit comments.

**Closed-set extension discipline.** The PARTICIPANT_ORGANISATION_CLOSED_SET in `validate.sh` is initialised at engine-v2 with values `{anthropic, openai, google, meta, xai, mistral, deepseek, cohere, local, human-individual, other-named}`. Extending this set requires a named decision in a session's `02-decisions.md` and a same-session update to the constant. Adding a new provider is **not** a substantive revision to `multi-agent-deliberation.md` per OI-002 heuristic (the spec already permits the closed set to extend); it is a substantive update to `tools/validate.sh` per `engine-manifest.md` §5 only when the addition substantively changes what counts as criterion-4-eligible. Routine provider additions (e.g., adding `cohere` after first operational use) are treated as minor validator-data updates not triggering an engine-version bump. This convention is established Session 021 and may be revisited if it produces silent failures.

**Consequence for prior sessions.** Sessions 001 through 020 are out-of-scope for checks 16, 17, 19. Session 021 and later sessions whose manifests claim OI-004 narrowing must include the new fields per the schema in `multi-agent-deliberation.md` v4. Pre-adoption sessions retain their original manifests unchanged.

### Sequencing (check 13 after check 12; check 14 after check 11; check 15 after check 12)

Check 13 depends on well-formed manifests. If check 12 fails for a given session, check 13 reports `BLOCKED: check 12 failed for this session; cannot evaluate check 13` for that session and does not itself fail or warn. This prevents double-reporting of a single underlying problem and keeps the tool honest about what it actually evaluated.

Check 14 depends on the three-raw-output floor established by check 11. If check 11 fails for a given session (fewer than three perspective files when multi-agent artefacts are asserted), check 14 reports `BLOCKED: check 11 failed for this session; cannot evaluate check 14`. Check 14 does **not** depend on check 12: it inspects perspective-file presence, not manifest content (per D-040, the Outsider's precision argument).

Check 15 depends on well-formed manifests. If check 12 fails for a given session, check 15 reports `BLOCKED: check 12 failed for this session; cannot evaluate check 15`. Check 15 is independent of check 14 (a decision can fail 15 while passing 14 or vice versa).

### Check 13's Honest Limit (mandatory inline documentation)

Check 13 enforces **consistency of self-report**, not **truthfulness of self-report**. This limit is mandatory content in three locations:

1. A comment block in `tools/validate.sh` directly above check 13's implementation.
2. Check 13's failure message (as an inline NOTE).
3. This specification (above).

The language to preserve verbatim:

> This check verifies the session's claim is internally consistent with its manifests. It does not and cannot verify that the manifests' lineage claims are themselves true. Manifest truth relies on operator integrity and the `participant_selected_by` field's accountability.

**Known gaming modes** (recorded in D-029 and preserved for future maintainers):

- **Value-flipping.** An operator edits `training_lineage_overlap_with_claude` in the manifest of a Claude subagent from `known-overlap` to `independent-claim`; the check passes.
- **`unknown` laundering.** An operator sets one participant's lineage field to `unknown` (a valid value) when the true value is `known-overlap`; the check passes.
- **Paper-human classification.** An operator records a nominal human participant who did not substantively participate; the check passes because `participant_kind: human` bypasses the lineage-value check.
- **Wrapper impersonation.** An operator routes a Claude call through a wrapper that looks like a non-Claude CLI and lies in the `provider` field; the check cannot distinguish this from a genuine non-Claude invocation.

These gaming modes are not fixed by check 13 alone. The Tier 2 question paired with check 13 (see below) is the methodology's designed counter-pressure to laundering by self-report.

### Check 14's Honest Limit (mandatory inline documentation)

Check 14 enforces **consistency between a decision's self-declared triggers and the session's multi-agent artefacts**, not **truthfulness of the declaration itself**. This limit is mandatory content in three locations:

1. A comment block in `tools/validate.sh` directly above check 14's implementation.
2. Check 14's failure message (as an inline NOTE).
3. This specification (above).

The language to preserve verbatim:

> This check verifies consistency between a decision's self-declared `triggers_met:` and the session's multi-agent artefacts. It does not and cannot verify that the `triggers_met:` declaration is itself a truthful classification of the decision against D-016. The declaration's truth relies on operator integrity and the `triggers_rationale:` field's adversarial visibility to Tier 2 review.

**Known false-compliance patterns** (recorded in D-040 rationale and preserved for future maintainers):

- **Under-declaration.** Writing `triggers_met: [none]` on a decision that in fact modifies the kernel. Check 14 passes silently.
- **Mono-perspective launder.** Three raw perspective files generated by re-prompting the same model with minor wording changes. Check 11 passes (three files present); check 14 passes (artefacts present for declared trigger); the substantive mono-perspective nature is undetected.
- **Strawman positions.** A `triggers_met: [d016_3]` claim (reasonable-disagreement trigger) justified by "two plausible positions" that are in fact strawmen. Deliberation-quality is out of scope for Tier 1.
- **Fabricated load-bearing claim.** A `triggers_met: [d016_4]` (operator-marked load-bearing) with a plausible-sounding Rationale that reclassifies a trivial decision as deliberation-worthy, or the inverse.

These patterns are not fixed by check 14 alone. The Tier 2 Q7 question (see below) is the designed counter-pressure.

### Check 15's Honest Limit (mandatory inline documentation)

Check 15 enforces **consistency between a decision's self-declared `d023_*` triggers and the session's non-Claude participant manifests**, not **truthfulness of manifest labels or skip reasons**. This limit is mandatory content in three locations:

1. A comment block in `tools/validate.sh` directly above check 15's implementation.
2. Check 15's failure message (as an inline NOTE).
3. This specification (above).

The language to preserve verbatim:

> This check verifies consistency between a decision's self-declared `d023_*` triggers and the session's non-Claude participant manifests. It does not verify that a manifest labeled non-Claude in fact represents a non-Claude participant (that is check 13's consistency scope) nor that the substantive adequacy of any skip reason is genuine (a Tier 2 concern). The declaration's truth relies on operator integrity.

**Known false-compliance patterns** (recorded in D-040 rationale):

- **Mislabeled manifest.** Relabeling a Claude-subagent manifest entry as `participant_kind: non-anthropic-model`. Check 15 passes; check 13's consistency scope catches this only if `cross_model: true` is also claimed.
- **Bogus skip annotation.** `**Non-Claude participation:** skipped — reason: "time constraints"; retry_in_session: S999` with no intention of retry. Check 15 passes on field presence; the reason's quality and retry commitment are Tier 2 concerns.
- **Pattern of skips.** Over-using the skip annotation across many sessions. No single check catches this; Tier 2 pattern-review is the counter-pressure.

### Tier 2: Guided Assessment

The following questions are printed for the assessor to consider:

1. **Provenance continuity:** Did this session's Read activity use prior provenance to understand past decisions? Were any past decisions re-proposed without acknowledgment?
2. **Specification consistency:** Are the current specifications semantically consistent with each other? Do any contradict or make assumptions that conflict?
3. **Adversarial quality:** In deliberative work, did the adversarial perspective provide genuine challenge, or did it concede too easily?
4. **Meaningful progress:** Is the methodology producing meaningful progress, or is it accumulating ceremony without advancing?
5. **Specification-reality alignment:** Are there specifications that describe things that no longer exist, or things that exist without being specified?
6. **Cross-model-honesty evidence (paired with check 13):** This session records `cross_model: true`. Name the concrete evidence — invocation transcript, CLI command, wall-clock gap, human presence — that distinguishes a genuine non-Claude participant from a Claude subagent with an edited manifest. If you cannot, flip `cross_model` to false. (Skip if this session does not claim cross-model participation.)

7. **Trigger-coverage plausibility (new in v3; paired with checks 14 and 15):** For each decision in this session declaring `**Triggers met:**`, read the decision's `**Decision:**` and `**Rationale:**` text and state whether the declared trigger list is consistent with the decision's content. For any `**Non-Claude participation:** skipped` annotation, state whether the reason is substantive (not formulaic) and the `retry_in_session:` commitment is credible. Flag mismatches and weak reasons; they are the dishonesty surface this session's Tier 1 checks cannot reach.

8. **OI-004 closure-retrospective substantive adequacy (new in v4; paired with check 18):** If this session contains an `oi-004-retrospective.md`, read its Qualifying Deliberations Table and P4 Assertion. For each row marked frame-replacement-or-novel-mechanism, verify the cited synthesis section actually contains a non-Claude-originated reframing (not paraphrase or restatement of a Claude perspective's argument). For the P4 assertion, verify the cited divergence shows the synthesis adopted a position that contradicts (or substantively augments) the Claude consensus, not merely supplemented it. Flag rows where the substantive claim is weaker than the structural claim suggests. (Skip if no `oi-004-retrospective.md` present.)

### Tool Location and Behavior

The validation tool is located at `tools/validate.sh`. It:
- Is **read-only**: it never modifies any workspace file.
- Produces a **structured report** with pass/fail/warning counts for Tier 1.
- Prints the **Tier 2 questions** after the Tier 1 report.
- Exits with **code 0** if no Tier 1 failures, **code 1** otherwise.
- Has **no dependencies** beyond standard Unix tools (bash 3.2+, grep, sed, awk) and git.

### When to Run

Validation should be run:

- At the **start** of each session, during or immediately after the Read activity.
- After the **Produce** activity, to check that new artifacts meet structural requirements.
- Before the **Close** activity, as a final coherence check.

### Limitations

Automated structural checks verify form, not meaning. Passing all structural checks does not mean:

- Specifications are correct about what they describe.
- Provenance captures the actual reasoning (it may be post-hoc rationalization).
- Decisions were well-considered.
- The methodology is serving its purpose.
- Cross-model participation is genuine rather than theatrical (see check 13's honest limit).
- Declared `triggers_met:` lists match the decisions they classify (see check 14 and 15 honest limits).
- Independent-claim evidence pointers (check 16) point to truthful evidence (the check verifies presence only, not truthfulness — see check 16's honest limit in `validate.sh`).
- Claude-output-in-training disclosures (check 17) are truthful (the check verifies disclosure presence, not truthfulness — same operator-integrity floor as check 13).
- Closure-retrospective substantive content (check 18) is well-grounded (the check verifies structural well-formedness only; substantive adequacy is Tier 2 Q8).
- Participant_organisation values (check 19) reflect actual model developers (the check verifies closed-set membership, not factual provenance).

These deeper questions are the purpose of Tier 2, which depends on honest assessment by the agent or human conducting the session. The methodology acknowledges that when a single AI agent both does the work and assesses it, Tier 2 is self-assessment rather than independent validation. This is a known limitation (see D-009), mitigated by making the questions explicit and recording the assessment in provenance, and further mitigated since Session 005 by the D-023 non-Claude-participation rule for meta-deliberations on self-assessment mechanisms.

The immutability check (Check 10) is a basic heuristic — it detects uncommitted changes to provenance files but does not verify full immutability across git history. Comprehensive immutability verification is a potential future improvement.

Check 12 verifies the presence of D-024 required keys but does not verify that the values are correct. A manifest may have all required keys while containing nonsense values; check 12 passes. The boundary between key-presence and value-correctness is a deliberate archival choice (the Archivist's Q3 position in Session 005: "the check succeeds if a field literally contains the string `unknown`, because D-024 explicitly admits `unknown` as a truthful value").

Check 13 is **consistency-of-self-report**, not **truthfulness-of-self-report**, as documented above. The Tier 2 Q6 is the methodology's designed complement. Passing check 13 *and* the operator answering Q6 with concrete evidence is stronger than either alone; neither is a truth certificate.

Checks 14 and 15 are **consistency between self-declared triggers and session artefacts**, not **truthfulness of the trigger declaration itself**, as documented above. The Tier 2 Q7 is the methodology's designed complement. Passing checks 14 and 15 *and* the operator answering Q7 with a substantive per-decision plausibility check is stronger than either alone. Check 14's gating rule (session ≥ 006) means the check does not apply to pre-adoption sessions; the immutability-preserving alternative for retrospective trigger classification is a separate artefact (D-039's retrospective-artefact pattern), not a retroactive rewrite.

## Validation

To validate this specification:

1. Run `tools/validate.sh` and verify it performs the nineteen structural checks listed in the table above.
2. Verify the tool prints the eight guided questions listed above.
3. Compare the tool's actual checks against the table in this specification — they should match.
4. Verify the tool is read-only (it makes no changes to any file).
5. Verify the tool exits with code 0 when all fail-severity checks pass, and code 1 otherwise.
6. Verify that check 13's honest-limit language appears in `tools/validate.sh` (comment block above check 13), in check 13's failure message, and in this specification's "Check 13's Honest Limit" subsection. Any divergence is a specification violation.
7. Verify that check 13 reports `BLOCKED` (not `FAIL` and not `PASS`) for sessions where check 12 failed.
8. Verify that check 14's honest-limit language appears in `tools/validate.sh` (comment block above check 14), in check 14's failure message, and in this specification's "Check 14's Honest Limit" subsection. Any divergence is a specification violation.
9. Verify that check 15's honest-limit language appears in `tools/validate.sh` (comment block above check 15), in check 15's failure message, and in this specification's "Check 15's Honest Limit" subsection. Any divergence is a specification violation.
10. Verify that check 14 reports `BLOCKED` for sessions where check 11 failed and check 15 reports `BLOCKED` for sessions where check 12 failed.
11. Verify that checks 14 and 15 apply only to sessions numbered ≥ 006 (the `TRIGGERS_MET_ADOPTION_SESSION` constant in `validate.sh`).
8. Verify that check 11 applies only to sessions with at least one `*-perspective-*.md` file, check 12 applies only to sessions with a `manifests/` subdirectory, and check 13 applies only to sessions that declare `cross_model: true`.

exec
/bin/zsh -lc 'wc -w provenance/014-oi016-resolution/01d-perspective-outsider.md SESSION-LOG.md open-issues.md' in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
   96651 provenance/014-oi016-resolution/01d-perspective-outsider.md
   10405 SESSION-LOG.md
    9783 open-issues.md
  116839 total

exec
/bin/zsh -lc 'rg -n "Provenance Layout|Acceptable Participant Kinds|Criterion-4|participants.yaml|raw perspective" specifications/multi-agent-deliberation.md' in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
21:Version 4 adds the OI-004 criterion-4 articulation (`### Criterion-4 Articulation for OI-004`), the acceptable-participant-kinds enumeration (`### Acceptable Participant Kinds for OI-004`), six new Layer 2 manifest fields (`participant_organisation`, `claude_output_in_training`, `training_lineage_evidence_pointer`, `aggregator_intermediary`, `selection_relationship_to_operator`, `independence_basis`), one new synthesis frontmatter field (`oi004_qualifying_participants`), one new session-level participants.yaml block (`mechanical_cross_family_invocation:`), the four-state OI-004 lifecycle, and the closure procedure (operationalised by `validate.sh` checks 16-19 and `validation-approach.md` v4 Tier 2 Q8). It supersedes v3 (`multi-agent-deliberation-v3.md`). Adopted Session 021 per D-082; engine-v1 → engine-v2 bump declared in `engine-manifest.md` §2 + §7.
148:3. The synthesizer reads `human-review.md` as an input alongside the raw perspective outputs.
190:**Layer 2 fields added in v4 (D-082, Session 021)** — for OI-004 criterion-4 enforcement; see §Criterion-4 Articulation for OI-004 below for normative use:
203:**Layer 3 — Session-level index.** `provenance/NNN/participants.yaml` (preferred) or `provenance/NNN/participants.md` listing each participant and their manifest path.
214:**Session-level participants index extension (added v4, D-082, Session 021).** When mechanical cross-family invocation occurs outside the perspective-deliberation frame (e.g., the Session 018 contamination-canary pattern), it is recorded as a separate top-level block in `provenance/NNN/participants.yaml`:
226:This block records mechanical cross-family invocation as corroborating evidence for criterion 3 of OI-004 (recorded impact on outcomes); it is **not** a participant kind for criterion 4 (per §Acceptable Participant Kinds for OI-004 below). The block is optional; absence is permitted (most sessions will not record mechanical invocation).
247:- **Reviewer input.** If the deliberation includes a reviewer-shape non-Claude participant, the synthesizer reads `human-review.md` alongside the raw perspective outputs.
249:- **Synthesizer-original claims.** Claims not directly sourced from any raw perspective are marked `[synth]`. This lets future readers compute the ratio of sourced to synthesised content and judge faithfulness.
257:### Provenance Layout
273:  participants.yaml             # session-level index
297:      participants.yaml
335:4. **Articulation.** A successor decision defines what "substantively different training provenance" means and enumerates acceptable participant kinds. Articulated Session 021 per D-082; see §Criterion-4 Articulation for OI-004 below.
339:### Criterion-4 Articulation for OI-004
356:2. Selection method MUST be one of `solicited-externally`, `pre-registered`, or `solicited-from-graph` (the last conditionally; see §Acceptable Participant Kinds for OI-004 below).
359:**Operational corroboration** (criterion 3, the existing acceptance test) is required to convert eligibility-under-this-articulation into actual narrowing. Criterion-4 articulation defines *who can count*; criterion 3 verifies *whether they did*. This bifurcation follows the 2-of-4 cross-family Session 021 split with cross-family weighting (Skeptic + Outsider) on placing operational corroboration in criterion 3 rather than in criterion-4 definition. The Articulator's [01a, Q1] D-Min ∩ O-Corr position and the Operationaliser's [01c, Q1] P4 position (operational corroboration as definitional prong) are preserved as joint first-class minority §5.5 in `provenance/021-oi004-criterion4-articulation/01-deliberation.md` with operational activation triggers.
367:### Acceptable Participant Kinds for OI-004
409:3. **Articulated; awaiting closure-retrospective.** All four criteria articulated as auditable predicates per §Criterion-4 Articulation above. Closure requires a one-time `oi-004-retrospective.md` artefact applying the criteria to the cumulative record. (Sessions 021+ hold this state.)
437:- **D-022** (Claude-only is not cross-model) — integrated as the Claude-Only-Is-Not-Cross-Model rule above; v4 extends this to anthropic-other per §Acceptable Participant Kinds for OI-004.
460:1. For every session with provenance, identify each Decision the session recorded. Each Decision that meets any trigger in "When Multi-Agent Deliberation Is Required" must be backed by either (a) multi-agent deliberation artifacts (raw perspective files plus a synthesis) or (b) an explicit single-agent annotation naming the reason.
462:3. For each multi-agent deliberation, verify that at least three raw perspective files exist in the session's provenance.

exec
/bin/zsh -lc "printf 'superseded specs:\\n'; rg --files specifications | rg -- '-v[0-9]+\\.md"'$'"'; printf '\\nmarkdown count:\\n'; rg --files -g '*.md' -g '"'!.git/**'"' -g '"'!.serena/**'"' -g '"'!.claude/**'"' | wc -l" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
superseded specs:
specifications/methodology-kernel-v2.md
specifications/multi-agent-deliberation-v2.md
specifications/identity-v1.md
specifications/workspace-structure-v2.md
specifications/methodology-kernel-v3.md
specifications/multi-agent-deliberation-v3.md
specifications/validation-approach-v1.md
specifications/validation-approach-v2.md
specifications/validation-approach-v3.md
specifications/workspace-structure-v1.md
specifications/methodology-kernel-v1.md
specifications/multi-agent-deliberation-v1.md
specifications/reference-validation-v1.md

markdown count:
     217

codex
I have enough to ground the diagnosis. One more pass on the deliberation spec’s provenance layout will let me answer the witness-pack and close-shape questions without hand-waving.
exec
/bin/zsh -lc "nl -ba specifications/multi-agent-deliberation.md | sed -n '257,320p'" in /Users/ericmccowan/Development/complex-systems-engine
 succeeded in 0ms:
   257	### Provenance Layout
   258	
   259	Tiered by the number of deliberations in a session.
   260	
   261	**Single-deliberation sessions** use flat numbered files at the session's provenance root, consistent with Sessions 001, 002, 003, and 004:
   262	
   263	```
   264	provenance/<NNN-title>/
   265	  00-assessment.md
   266	  01-brief-shared.md            # optional: shared brief preserved for auditability
   267	  01a-perspective-<role>.md
   268	  01b-perspective-<role>.md
   269	  ...
   270	  01-deliberation.md            # synthesis
   271	  manifests/
   272	    <role>.manifest.yaml        # one per participant
   273	  participants.yaml             # session-level index
   274	  human-review.md               # if a reviewer-shape participant was included
   275	  STATUS.md                     # if the session halted awaiting a non-Claude response
   276	  02-decisions.md
   277	  03-close.md
   278	```
   279	
   280	When all briefs in the deliberation share byte-identical non-role sections (the default), briefs need not be preserved as separate files — each raw-output file already contains the role-specific stance, and the shared sections are derivable from any brief. If briefs in a deliberation depart from this shape (e.g., differentiated context), the briefs must be preserved as separate files named `01*-brief-<role>.md`.
   281	
   282	**Multi-deliberation sessions** use a subdirectory layout:
   283	
   284	```
   285	provenance/<NNN-title>/
   286	  00-assessment.md
   287	  deliberations/
   288	    <decision-id>/
   289	      briefs/
   290	        00-shared-context.md
   291	        01-<role>.md
   292	      responses/
   293	        01-<role>.md
   294	        ...
   295	      manifests/
   296	        <role>.manifest.yaml
   297	      participants.yaml
   298	      human-review.md             # if a reviewer-shape participant was included
   299	      synthesis.md
   300	      manifest.json               # session-level metadata (model IDs, timestamps, commit)
   301	  02-decisions.md
   302	  03-close.md
   303	```
   304	
   305	`manifest.json` records deliberation-level metadata (commit hash at convening time, deliberation decision-id, start/end timestamps). Per-participant detail lives in the `manifests/` directory.
   306	
   307	### Graceful Degradation
   308	
   309	- **Minimum viable quorum.** If a perspective fails to return an output (error, refusal, malformed response), the deliberation may proceed with the remaining perspectives provided at least three returned valid outputs. The failure is recorded in the synthesis file's frontmatter or in `manifest.json`.
   310	- **Stance refusal.** A perspective that refuses the assigned stance, or that substantively disagrees with the brief itself, has its refusal preserved as provenance. Refusal is signal, not an error to coerce around.
   311	- **Fewer than three valid outputs.** The deliberation must be re-run or the question reformulated. A synthesis over one or two perspectives is not a multi-agent deliberation.
   312	- **Non-Claude participant non-response.** Per the halt-before-synthesis rule, synthesis does not proceed when a Shape-A non-Claude participant has not responded. Timeout policy (whether a session may eventually proceed after N days with a recorded opt-out) is not mandated by v2; the halt is in place until the awaited response is committed or the session formally records opt-out.
   313	
   314	### Limitations
   315	
   316	These statements are required content for every multi-agent deliberation's synthesis or decision record that relies on a Claude-only mechanism:
   317	
   318	- **All Claude-subagent perspectives share a model family.** The parallel-subagent implementation uses instances of the same Claude model family. Shared training produces shared blind spots: the same cultural priors, argumentative reflexes, refusal patterns, and aesthetic preferences.
   319	- **Intra-Claude-family size-mixing is not cross-model participation.** Mixing Opus, Sonnet, and Haiku does not narrow OI-004; it may surface capability-band differences but does not introduce independent training lineages. See OI-011 for separate tracking of intra-family mixing.
   320	- **Parallel isolation prevents conversational anchoring, not training-distribution anchoring.** Four instances of the same model, given briefs written in a shared vocabulary, will correlate in ways that look like agreement but are actually shared priors. Consensus across subagents is weak evidence, not strong.

codex
I accept the direction of the operator’s concern, but not the operator’s ontology as stated. The failure here is a broken read contract: the engine still normatively requires exhaustive reading while actual sessions already rely on paging, grepping, and routing around oversized surfaces [§2.2, §3, §6; methodology-kernel §1 Read; §4.2]. A canonical-vs-witness distinction is the right repair only if it is treated as a bounded access rule layered on top of the existing file classes, not as a claim that every historically important file remains default-read forever [workspace-structure §File classes].

## Q1. Frame acceptance

Partially yes. I accept the need for a bounded default-read surface and a preserved reference/archive surface. I do not accept “two artefact kinds” as the deepest diagnosis. The deeper diagnosis is that the workspace’s normative read obligation and its operational reading mechanism have diverged [§3, §6]. “Canonical surfaces” and “witnesses” are a repair for that divergence, not the root conceptual model.

That distinction matters because the workspace already has a load-bearing ontology: engine-definition, development-provenance, and application-scope [workspace-structure §File classes; engine-manifest §1, §4]. The new distinction should cut across those classes as an access discipline:

- `default-read surface`: what every session must read in full before acting.
- `reference/archive surface`: what must be preserved exactly and read when relied on, cited, or challenged.

My main disagreement with the operator’s examples is that putting all per-session `03-close.md` files on the canonical/default-read surface would recreate the same growth problem in a slower form. That controls per-file size but not aggregate session-open burden. A bounded surface must be bounded in total, not only in its largest member. So I accept the direction, but I would define the repair as a “bounded working-set contract,” not simply “two artefact kinds.”

## Q2. `prompts/development.md` revisions

Yes, line 19 must change. Yes, line 25 must change with it. Yes, line 43 should explicitly authorize archive/witness packing. And no, prompt-only revision is not sufficient; the kernel must change too, because the kernel currently makes the prompt-level relaxation semantically illegal [methodology-kernel §1 Read; §4.1, §4.2].

My proposed text is:

- Line 19: “Begin by reading the workspace’s default-read surface completely: the active engine-definition files, the workspace’s bounded orientation records, and the current session’s explicit inputs. Then read any archived records you will rely on, cite, challenge, or revise.”
- Line 25: “Before substantive work, read the bounded decision-orientation records the workspace designates for continuity, then read any archived prior records needed to understand relevant rejections, unresolved disputes, or dependency chains.”
- Line 43: “Preserve all provenance. Do not delete or silently compress historical records. When a preserved record exceeds default-read bounds, retain it as an immutable archived witness with a stable manifest, chunk references, and integrity metadata.”

I would also revise `methodology-kernel.md` §1 Read in the same direction. The current text says “every file, every specification, every provenance record” [methodology-kernel §1 Read]. That is the contradiction. If the session changes only `prompts/development.md`, the kernel and executable prompt diverge.

I would further align `prompts/application.md`, because its current Read section still says the full current state of the application workspace. If that text is left untouched, the engine exports the same contradiction to external applications.

## Q3. Witness-pack specification

I will use “witness-pack” because the brief uses it, but the load-bearing idea is archived exact-text packaging.

- Format: directory, not zip, and not a single monolith. Use `manifest.md` plus numbered raw chunks such as `0001.raw.md`, `0002.raw.md`, etc. Zip-like archives are wrong here because they break grep/diff/referenceability.
- Location: a top-level `witnesses/` or `archives/` directory, not retroactively inserted into closed provenance directories. That respects provenance immutability better than adding new files inside old session folders [workspace-structure §provenance/].
- Inclusion rule: any archived record that exceeds the default-read per-file budget must have a pack. Small archived records can remain single-file archived records without chunking. Superseded specs should become archive-surface by rule even if they do not need chunking [engine-manifest §4].
- Reference convention: canonical/default-read files cite a stable witness id and, when needed, a chunk id. Example: `witness:W-014-01d#0003` or equivalent path-plus-chunk reference.
- Resolution rule: the manifest states `source_path`, `reason_for_archiving`, `source_hash`, ordered chunk list, and reconstruction rule.
- Integrity: hash the source file and each chunk. The pack is append-only. If the source was copied from an existing immutable record, the manifest says so explicitly.
- Engine impact: yes, this is engine-v3 work. It changes read semantics, provenance handling, and validation.

I would put the normative classification rules in a new engine-definition spec, something like `specifications/read-contract.md`. This is cross-cutting enough that burying it in `workspace-structure.md` would make the rule hard to follow and easy to drift.

## Q4. Retroactive migration scope

- (a) Yes. `provenance/014-oi016-resolution/01d-perspective-outsider.md` is the clearest falsifier to the old read contract [§2.2]. If nothing else is migrated, this one should be.
- (b) Yes, in principle. If the methodology adopts a threshold, all over-threshold raw perspective files should eventually receive archive packs. Otherwise the rule is selective and arbitrary. If the set is too large to finish now, do not pretend the migration is complete.
- (c) Yes, but as reclassification first, chunking second. Superseded spec copies are already explicitly not part of engine load [engine-manifest §4]. They should move off the default-read surface immediately; only oversize ones need packing.
- (d) Yes. Long annotations in `open-issues.md` should move into issue-specific detail records or witness packs, with the index left thin [workspace-structure §open-issues.md].
- (e) Yes, but not via witness-packing by default. `SESSION-LOG.md` is mutable and already defined as an index over `03-close.md`, not a replacement for it [workspace-structure §SESSION-LOG.md]. Long entries should simply be shortened in place.
- (f) No, not this session. Epoch consolidation for Sessions 001–010 is plausible later, but it is not necessary to repair the broken read contract immediately. It adds synthesis risk and a lot of migration surface.

## Q5. Canonical-surface restoration this session

Yes on both.

`SESSION-LOG.md` should be restored to a true thin index this session. The specification already says it is “a running index” and that canonical detail lives in `03-close.md` [workspace-structure §SESSION-LOG.md]. The current state is type-drift, not just growth [§2.2, §5.3].

`open-issues.md` should also be restructured this session. I do not think §5.1’s original strict 50,000-token warrant has literally fired [§5.1]. I do think the file is already “unwieldy” under the structure spec’s own authorization clause [workspace-structure §open-issues.md], and the current session-open read workaround proves that operationally [§3, §6].

The risk of information loss is low for `SESSION-LOG.md` and moderate for `open-issues.md`.

- `SESSION-LOG.md`: low risk, because the detailed content already has a canonical home in `03-close.md`.
- `open-issues.md`: moderate risk, because annotations often carry live reasoning, cross-links, and conditional states. The mitigation is mechanical relocation with stable OI ids and exact-text preservation, not summary-only rewriting.

## Q6. `tools/validate.sh` hard-gate check

I support candidate #8, but not exactly as written.

It should hard-fail when any default-read file exceeds the configured per-file budget. I would set that budget in words, not tokens, because the current validator is bash-only and already uses standard Unix tooling [validation-approach §Tool Location and Behavior]. My recommendation is `8,000` words per default-read file.

I would also add an aggregate report, and likely a warning threshold, for the total development-provenance default-read surface. Per-file control alone is not sufficient if the default-read set keeps growing by accretion.

Canonical/default-read versus archive/witness must be detected by explicit classification, not filename heuristics. The normative list should live in a dedicated read-contract spec. The validator can mirror that list as constants or globs, as it already mirrors other spec rules [validation-approach §Tier 1: Structural Checks]. Without explicit classification, the validator will become a maze of accidental path rules.

## Q7. Session 020 minority activations

- §5.1: do not declare the old warrant vindicated as written. The literal 50,000-token condition is not met [§5.1]. Revise the warrant downward to the actual failure mode, or better, subsume the whole question into the new read-contract adoption. I prefer subsumption.
- §5.2: yes, adopt the rollback/restoration direction. Its warrant is satisfied [§5.2], and the fix belongs inside the new bounded default-read model.
- §5.3: yes, adopt. Its warrant is also satisfied [§5.3], and again the right framing is that `SESSION-LOG.md` returns to being an index, not a dossier.

So my pattern is: literal no on §5.1’s old trigger, yes on revising the underlying rule, yes on subsuming all three into the broader read-contract repair.

## Q8. Close shape for this session’s own raws

I accept “no grandfather clause” only in the thresholded sense. If this session adopts witness-packs, then any raw output from this session that exceeds the archive-pack threshold should be packed before close. Small raw outputs should remain ordinary provenance files; packing everything by default would add ceremony without solving a real problem.

Practically, that means this session’s provenance may close with ordinary raw perspective files plus zero or more witness-pack references if any response runs over budget. The `SESSION-LOG` entry should stay thin and simply record that the session adopted the bounded-read/archive model and, if applicable, created witness packs for over-threshold raws.

## Q9. Engine-version implication and triggers

Engine-v3 is warranted if the session adopts the substantive repair rather than E.1 alone.

E.1 by itself is only a `CLAUDE.md` cleanup. I verified the current mempalace paragraph is still there, and removing it does not touch engine-definition files. No engine bump is warranted for that alone.

The full repair, by contrast, changes engine behavior in substance. At minimum it touches:

- `specifications/methodology-kernel.md`
- `prompts/development.md`
- `prompts/application.md`
- `specifications/workspace-structure.md`
- `specifications/multi-agent-deliberation.md`
- `specifications/validation-approach.md`
- `tools/validate.sh`
- `specifications/engine-manifest.md`

If a dedicated read-contract spec is added, that is another engine-definition change. On that package, `engine-v3` is plainly correct [engine-manifest §5].

On triggers: I agree with the operator’s anticipated trigger declaration if the session takes the full adoption set. My confidence is highest on the non-Claude/engine-governance side because the proposed set revises the kernel, revises `multi-agent-deliberation.md`, and revises validation semantics. I am less certain on the exact D-016 numbering because I did not independently re-open the originating trigger-definition record, so that portion of my agreement is inferential rather than text-verified.

## Honest Limits

I verified the live current text of `prompts/development.md`, `prompts/application.md`, `specifications/methodology-kernel.md`, `specifications/workspace-structure.md`, `specifications/engine-manifest.md`, `specifications/validation-approach.md`, `specifications/multi-agent-deliberation.md` §Provenance Layout, `tools/validate.sh`, and `CLAUDE.md`.

I did not read other perspectives’ responses. I did not inspect raw provenance records beyond the one named extreme outlier path and did not inventory all over-threshold raw files across the workspace. I also did not reproduce the brief’s token counts with the same tokenizer, so where I discuss thresholds I am reasoning from the brief’s stated ceilings plus live file inspection, not from an independently matched token audit.
tokens used
46,382
I accept the direction of the operator’s concern, but not the operator’s ontology as stated. The failure here is a broken read contract: the engine still normatively requires exhaustive reading while actual sessions already rely on paging, grepping, and routing around oversized surfaces [§2.2, §3, §6; methodology-kernel §1 Read; §4.2]. A canonical-vs-witness distinction is the right repair only if it is treated as a bounded access rule layered on top of the existing file classes, not as a claim that every historically important file remains default-read forever [workspace-structure §File classes].

## Q1. Frame acceptance

Partially yes. I accept the need for a bounded default-read surface and a preserved reference/archive surface. I do not accept “two artefact kinds” as the deepest diagnosis. The deeper diagnosis is that the workspace’s normative read obligation and its operational reading mechanism have diverged [§3, §6]. “Canonical surfaces” and “witnesses” are a repair for that divergence, not the root conceptual model.

That distinction matters because the workspace already has a load-bearing ontology: engine-definition, development-provenance, and application-scope [workspace-structure §File classes; engine-manifest §1, §4]. The new distinction should cut across those classes as an access discipline:

- `default-read surface`: what every session must read in full before acting.
- `reference/archive surface`: what must be preserved exactly and read when relied on, cited, or challenged.

My main disagreement with the operator’s examples is that putting all per-session `03-close.md` files on the canonical/default-read surface would recreate the same growth problem in a slower form. That controls per-file size but not aggregate session-open burden. A bounded surface must be bounded in total, not only in its largest member. So I accept the direction, but I would define the repair as a “bounded working-set contract,” not simply “two artefact kinds.”

## Q2. `prompts/development.md` revisions

Yes, line 19 must change. Yes, line 25 must change with it. Yes, line 43 should explicitly authorize archive/witness packing. And no, prompt-only revision is not sufficient; the kernel must change too, because the kernel currently makes the prompt-level relaxation semantically illegal [methodology-kernel §1 Read; §4.1, §4.2].

My proposed text is:

- Line 19: “Begin by reading the workspace’s default-read surface completely: the active engine-definition files, the workspace’s bounded orientation records, and the current session’s explicit inputs. Then read any archived records you will rely on, cite, challenge, or revise.”
- Line 25: “Before substantive work, read the bounded decision-orientation records the workspace designates for continuity, then read any archived prior records needed to understand relevant rejections, unresolved disputes, or dependency chains.”
- Line 43: “Preserve all provenance. Do not delete or silently compress historical records. When a preserved record exceeds default-read bounds, retain it as an immutable archived witness with a stable manifest, chunk references, and integrity metadata.”

I would also revise `methodology-kernel.md` §1 Read in the same direction. The current text says “every file, every specification, every provenance record” [methodology-kernel §1 Read]. That is the contradiction. If the session changes only `prompts/development.md`, the kernel and executable prompt diverge.

I would further align `prompts/application.md`, because its current Read section still says the full current state of the application workspace. If that text is left untouched, the engine exports the same contradiction to external applications.

## Q3. Witness-pack specification

I will use “witness-pack” because the brief uses it, but the load-bearing idea is archived exact-text packaging.

- Format: directory, not zip, and not a single monolith. Use `manifest.md` plus numbered raw chunks such as `0001.raw.md`, `0002.raw.md`, etc. Zip-like archives are wrong here because they break grep/diff/referenceability.
- Location: a top-level `witnesses/` or `archives/` directory, not retroactively inserted into closed provenance directories. That respects provenance immutability better than adding new files inside old session folders [workspace-structure §provenance/].
- Inclusion rule: any archived record that exceeds the default-read per-file budget must have a pack. Small archived records can remain single-file archived records without chunking. Superseded specs should become archive-surface by rule even if they do not need chunking [engine-manifest §4].
- Reference convention: canonical/default-read files cite a stable witness id and, when needed, a chunk id. Example: `witness:W-014-01d#0003` or equivalent path-plus-chunk reference.
- Resolution rule: the manifest states `source_path`, `reason_for_archiving`, `source_hash`, ordered chunk list, and reconstruction rule.
- Integrity: hash the source file and each chunk. The pack is append-only. If the source was copied from an existing immutable record, the manifest says so explicitly.
- Engine impact: yes, this is engine-v3 work. It changes read semantics, provenance handling, and validation.

I would put the normative classification rules in a new engine-definition spec, something like `specifications/read-contract.md`. This is cross-cutting enough that burying it in `workspace-structure.md` would make the rule hard to follow and easy to drift.

## Q4. Retroactive migration scope

- (a) Yes. `provenance/014-oi016-resolution/01d-perspective-outsider.md` is the clearest falsifier to the old read contract [§2.2]. If nothing else is migrated, this one should be.
- (b) Yes, in principle. If the methodology adopts a threshold, all over-threshold raw perspective files should eventually receive archive packs. Otherwise the rule is selective and arbitrary. If the set is too large to finish now, do not pretend the migration is complete.
- (c) Yes, but as reclassification first, chunking second. Superseded spec copies are already explicitly not part of engine load [engine-manifest §4]. They should move off the default-read surface immediately; only oversize ones need packing.
- (d) Yes. Long annotations in `open-issues.md` should move into issue-specific detail records or witness packs, with the index left thin [workspace-structure §open-issues.md].
- (e) Yes, but not via witness-packing by default. `SESSION-LOG.md` is mutable and already defined as an index over `03-close.md`, not a replacement for it [workspace-structure §SESSION-LOG.md]. Long entries should simply be shortened in place.
- (f) No, not this session. Epoch consolidation for Sessions 001–010 is plausible later, but it is not necessary to repair the broken read contract immediately. It adds synthesis risk and a lot of migration surface.

## Q5. Canonical-surface restoration this session

Yes on both.

`SESSION-LOG.md` should be restored to a true thin index this session. The specification already says it is “a running index” and that canonical detail lives in `03-close.md` [workspace-structure §SESSION-LOG.md]. The current state is type-drift, not just growth [§2.2, §5.3].

`open-issues.md` should also be restructured this session. I do not think §5.1’s original strict 50,000-token warrant has literally fired [§5.1]. I do think the file is already “unwieldy” under the structure spec’s own authorization clause [workspace-structure §open-issues.md], and the current session-open read workaround proves that operationally [§3, §6].

The risk of information loss is low for `SESSION-LOG.md` and moderate for `open-issues.md`.

- `SESSION-LOG.md`: low risk, because the detailed content already has a canonical home in `03-close.md`.
- `open-issues.md`: moderate risk, because annotations often carry live reasoning, cross-links, and conditional states. The mitigation is mechanical relocation with stable OI ids and exact-text preservation, not summary-only rewriting.

## Q6. `tools/validate.sh` hard-gate check

I support candidate #8, but not exactly as written.

It should hard-fail when any default-read file exceeds the configured per-file budget. I would set that budget in words, not tokens, because the current validator is bash-only and already uses standard Unix tooling [validation-approach §Tool Location and Behavior]. My recommendation is `8,000` words per default-read file.

I would also add an aggregate report, and likely a warning threshold, for the total development-provenance default-read surface. Per-file control alone is not sufficient if the default-read set keeps growing by accretion.

Canonical/default-read versus archive/witness must be detected by explicit classification, not filename heuristics. The normative list should live in a dedicated read-contract spec. The validator can mirror that list as constants or globs, as it already mirrors other spec rules [validation-approach §Tier 1: Structural Checks]. Without explicit classification, the validator will become a maze of accidental path rules.

## Q7. Session 020 minority activations

- §5.1: do not declare the old warrant vindicated as written. The literal 50,000-token condition is not met [§5.1]. Revise the warrant downward to the actual failure mode, or better, subsume the whole question into the new read-contract adoption. I prefer subsumption.
- §5.2: yes, adopt the rollback/restoration direction. Its warrant is satisfied [§5.2], and the fix belongs inside the new bounded default-read model.
- §5.3: yes, adopt. Its warrant is also satisfied [§5.3], and again the right framing is that `SESSION-LOG.md` returns to being an index, not a dossier.

So my pattern is: literal no on §5.1’s old trigger, yes on revising the underlying rule, yes on subsuming all three into the broader read-contract repair.

## Q8. Close shape for this session’s own raws

I accept “no grandfather clause” only in the thresholded sense. If this session adopts witness-packs, then any raw output from this session that exceeds the archive-pack threshold should be packed before close. Small raw outputs should remain ordinary provenance files; packing everything by default would add ceremony without solving a real problem.

Practically, that means this session’s provenance may close with ordinary raw perspective files plus zero or more witness-pack references if any response runs over budget. The `SESSION-LOG` entry should stay thin and simply record that the session adopted the bounded-read/archive model and, if applicable, created witness packs for over-threshold raws.

## Q9. Engine-version implication and triggers

Engine-v3 is warranted if the session adopts the substantive repair rather than E.1 alone.

E.1 by itself is only a `CLAUDE.md` cleanup. I verified the current mempalace paragraph is still there, and removing it does not touch engine-definition files. No engine bump is warranted for that alone.

The full repair, by contrast, changes engine behavior in substance. At minimum it touches:

- `specifications/methodology-kernel.md`
- `prompts/development.md`
- `prompts/application.md`
- `specifications/workspace-structure.md`
- `specifications/multi-agent-deliberation.md`
- `specifications/validation-approach.md`
- `tools/validate.sh`
- `specifications/engine-manifest.md`

If a dedicated read-contract spec is added, that is another engine-definition change. On that package, `engine-v3` is plainly correct [engine-manifest §5].

On triggers: I agree with the operator’s anticipated trigger declaration if the session takes the full adoption set. My confidence is highest on the non-Claude/engine-governance side because the proposed set revises the kernel, revises `multi-agent-deliberation.md`, and revises validation semantics. I am less certain on the exact D-016 numbering because I did not independently re-open the originating trigger-definition record, so that portion of my agreement is inferential rather than text-verified.

## Honest Limits

I verified the live current text of `prompts/development.md`, `prompts/application.md`, `specifications/methodology-kernel.md`, `specifications/workspace-structure.md`, `specifications/engine-manifest.md`, `specifications/validation-approach.md`, `specifications/multi-agent-deliberation.md` §Provenance Layout, `tools/validate.sh`, and `CLAUDE.md`.

I did not read other perspectives’ responses. I did not inspect raw provenance records beyond the one named extreme outlier path and did not inventory all over-threshold raw files across the workspace. I also did not reproduce the brief’s token counts with the same tokenizer, so where I discuss thresholds I am reasoning from the brief’s stated ceilings plus live file inspection, not from an independently matched token audit.
