---
session: 020
title: Perspective — Splitter
date: 2026-04-22
perspective: splitter
participant_kind: claude-subagent
model_family: claude
model_id: claude-opus-4-7
provider: anthropic
status: verbatim
---

# Splitter Perspective

## Q1 — Is the observed friction load-bearing or cosmetic?

Load-bearing. The brief [§3] records "no information loss detected *for this session's specific audit questions*" — a post-hoc pass on a narrow question-set, not a predictive test.

Three methodology properties are at risk once Read (workspace reading) becomes selectively segmented by default:

1. **Absorb integrity.** The kernel §1 Read activity (D-060) defines workspace reading as Absorb — what the session will reason from. Selective offset-reads make the reasoning base a Grep-shaped subset, not an Absorb-shaped whole. Selection bias is introduced at Read, where the discipline was "absorb-first, choose-later."

2. **Audit-reconstruction fidelity.** Auditors tracking cross-session patterns (OI-004 tally sequences; OI-002 substantive-vs-minor precedents) rely on contiguous reads. When OI-004's body alone is ~14KB inside a 70KB file, "what is OI-004's current state?" requires offset math plus trust that the offset landed right — itself an error surface.

3. **Genesis-provenance legibility.** Per `engine-manifest.md` §4, SESSION-LOG.md and open-issues.md are explicitly NOT inherited by external workspaces. But the self-development workspace is the *one* place these files must remain indefinitely legible — they are the genesis record for what *did* get inherited.

The segment-read workaround serves questions the orchestrator already knows to ask. It fails for questions the orchestrator doesn't know to ask. That is the falsifier pattern: undetectable loss. By the time loss is detected, decisions have been made on incomplete Read.

**Verdict**: load-bearing for properties currently passing precisely because they have not been stressed. Proceed with structural remedy.

## Q2 — Structural fix for `open-issues.md`

I propose **split-by-identity** (one file per OI) with a thin index.

(Pretraining-sourced observation, surfaced per [brief §10]: the ADR pattern `docs/adr/NNN-title.md` is a candidate analogue; not asserted as established fact.)

### Directory shape

```
/open-issues.md                    (index only)
/open-issues/
  OI-002-substantive-vs-minor.md
  OI-004-cross-model-participation.md
  OI-005-sub-activities.md
  OI-006-cross-references.md
  OI-007-scaling-open-issues-format.md
  OI-008-validation-reports-persistence.md
  OI-009-drift-to-ritual-monitor.md
  OI-011-intra-family-mixing.md
  OI-012-validate-sh-hardcoded-path.md
  OI-013-non-file-external-artefacts.md
  OI-014-domain-actor-receipt-variance.md
  OI-015-laundering-enforcement-gap.md
  OI-016-domain-validation-pathway.md
  /resolved/
    OI-001, OI-003, OI-010, OI-017 (one file each)
```

### Why split-by-identity over alternatives

**Vs. split-by-status** (`active/` + `resolved/`): status lives in frontmatter already; filesystem partition duplicates data and forces moves on every status transition. Terminal `resolved/` is tolerable because the move happens once, permanently.

**Vs. split-by-family**: families are later-imposed taxonomy. OIs are born from sessions, not families. Pre-imposing categorisation at OI-creation time is exactly when the family is least clear.

**Vs. hybrid**: invites re-file churn and ongoing disagreement about placement.

Flat-per-OI is invariant: one OI, one file, always. Status changes edit frontmatter, not paths.

### How it serves Read (workspace reading)

- Index is readable in one call (~30 lines at 50-session horizon).
- Any individual OI is readable in one call even if it accretes indefinitely (OI-004 at 14KB is comfortably single-read in its own file; in the current monolith, the surrounding file pushes OI-004 past the ceiling).
- Grep across `open-issues/**` is no more expensive than Grep on one file.

### Preserves provenance continuity and diff review

Each OI's full history lives in one file — complete trajectory, single read. Sessions touching three OIs produce three per-OI diffs rather than one scroll-through-monolith diff. Review granularity strictly improves.

### Draft spec amendment text (replaces current §open-issues.md)

> ### open-issues.md + open-issues/
>
> A registry of known questions, gaps, uncertainties, and unresolved disagreements:
>
> - `open-issues.md` — thin index. One row per issue: identifier, title, surfacing session, current status, filename. Updated on open/status-change/resolution.
> - `open-issues/<OI-id>-<slug>.md` — one file per open issue. Frontmatter: `oi_id`, `title`, `surfaced_session`, `status`, `last_updated_session`. Body: free-form Markdown with session-annotations accreting chronologically.
> - `open-issues/resolved/<OI-id>-<slug>.md` — resolved issues move here on closure. Frontmatter additionally carries `resolved_session`, `resolved_by_decision`.
>
> Opening a new issue creates both the index row and the file. Resolving an issue moves the file to `resolved/` and updates the row. Annotations within a session update only the relevant OI file(s); the index is touched only on status change.

This is substantive (addressed in Q6). Engine-v1 → engine-v2.

## Q3 — Structural fix for `SESSION-LOG.md`

I propose **per-session files + index**, same shape-logic as Q2.

### Directory shape

```
/SESSION-LOG.md           (index: one row per session)
/session-log/
  001-genesis.md
  002-self-validation.md
  ...
  020-workspace-scaling-deliberation.md
```

Each `session-log/NNN-<slug>.md` carries the paragraph-length executive summary currently in a SESSION-LOG row.

### Why this over brief §7 Q3's other options

**Enforce brevity** (rewrite current paragraphs to one-liners): lossy. The brief's claim that "detail already exists in provenance `03-close.md`" is half-true: close docs carry close-specific reasoning (re-opening triggers, next-session menus), not neutral backward-looking summaries. SESSION-LOG's paragraphs *are* the neutral summaries. Stripping them forces re-derivation — this is the "discipline failure retroactively celebrated as discipline win" laundering pattern.

**Re-spec the file (paragraph per entry, single file)**: ratifies drift without solving scale. At ~3KB/session × 50 sessions ≈ 150KB ≈ ~45k tokens — roughly twice the read ceiling. Non-fix.

**Per-session files + index** honours each layer's current intent:
- SESSION-LOG.md as spec'd ("running index for quick orientation") = the index.
- Paragraph-length summaries (current drift) = the per-session files.

Neither layer is lost.

### How it serves Read

- Index is single-read at 50-session horizon (~12KB at ~250 bytes/row).
- Session-specific detail fetched by path (`session-log/011-*.md`) — single-read, full summary, no offset math.
- Cross-session patterns via Grep across `session-log/**` — no retrieval-cost change.

### Respects original spec intent

The spec said "one line per entry." The index is one line per entry. The spec did not anticipate per-session files, but the *principle* it protected (quick-orientation at index level) is protected.

### Draft spec amendment text (replaces current §SESSION-LOG.md)

> ### SESSION-LOG.md + session-log/
>
> The session registry consists of:
>
> - `SESSION-LOG.md` — thin index. One table row per session: number, date, title, status, provenance-directory name, summary-file link. Appended at the close of each session.
> - `session-log/NNN-<slug>.md` — one file per session. Carries the executive summary of what the session accomplished (typically 3–10 short paragraphs). Frontmatter: `session`, `date`, `title`, `status`. Updated only at the close of the session it describes; per the provenance immutability rule, closed-session summary files are not modified in later sessions except by additive annotation with explicit session-and-reason attribution.
>
> The index row is authoritative for `validate.sh` Check 4 ("SESSION-LOG has an entry for every provenance directory"). Per-session files carry quick-orientation content.

Substantive. Engine-v1 → engine-v2.

## Q4 — Tooling fix surface: mempalace adoption

Per [brief §8 Splitter], I treat mempalace as separate from my structural proposals. I address it only to argue that **structural fix and tool adoption address different failure modes** and are not substitutes.

Structural fix makes files single-readable — it protects the Absorb activity. Tool adoption adds semantic search over files of any size. These are orthogonal. `mempalace search "Session 017 decisions"` returns ranked drawers; it does not give the whole-workspace Absorb Read is defined to perform.

Tool-first does not substitute for fixing the two files that currently exceed single-read. The Tooler perspective will make the tool-first case; my position is that structural fix is prior.

## Q5 — Interaction between Q2, Q3, and Q4

Complementary, with asymmetric dependencies:

- Structural fix (Q2+Q3) is **necessary** — addresses the Read-ceiling violation directly. Without it, single-file workspace reading breaks; any tool layered above inherits that break.
- Tool adoption (Q4) is **optional enhancement** — adds retrieval performance and cross-file semantic search. Works whether files are one-or-many (mempalace mines either).

**Minimum-viable change**: Q2 + Q3 together. Both bump engine version regardless of whether one or both are done; no saving from doing only one. Q4 is a separate conversation.

**If mempalace adopted without structural fix**: orchestrator still cannot Read the files in one call. Mempalace helps *find*; Absorb remains broken.

**If structural fix adopted without mempalace**: single-read ceiling respected. Workspace operates as designed. Mempalace remains a future option.

## Q6 — Engine-version impact

Both Q2 and Q3 amendments are **substantive**.

**Q2 could be argued minor** because the current §open-issues.md text explicitly anticipates directory-split ("unless unwieldy") — analogous to Session 002 D-014 adding `tools/` under the "change anticipated by the spec's own language" minor-revision criterion. But my proposal adds beyond what the existing language anticipates: a `resolved/` subdirectory, required frontmatter fields, stated index-vs-per-file update rules. Those cross into substantive territory (new required fields; new rules). I assess Q2 as substantive.

**Q3 is clearly substantive.** The current spec does not anticipate splitting SESSION-LOG at all. Adding a directory with required contents, frontmatter fields, and an immutability rule is new normative content.

**Engine-v1 → engine-v2 is warranted.** Non-trivial but not prohibitive. Per `engine-manifest.md` §5 this is the normal consequence of substantive engine-definition revision. Session 017 already demonstrated willingness to do three simultaneous substantive engine events; this session's proposed revision is smaller and addresses observed friction.

**Minimum-avoid-bump path** (not recommended): split only open-issues.md, reduce the proposal to "split by OI; one file per issue; no subdirectory; no required frontmatter," invoking the "unwieldy" anticipation clause as minor-revision warrant per D-014/D-020 precedent. Weaker resulting structure; less maintainable at 50-session horizon. I flag it exists but argue against it: version-bump aversion is not a methodology value.

## Q7 — Preserve or revisit one-line SESSION-LOG intent

The drift is **(c) genuine informational need** with a contribution from **(b) discipline failure**.

Evidence for (c): current paragraph entries carry content usable for orientation at the session-index layer. A one-line Session 009 summary ("W2/W4 revisions adopted via Outsider copy-plus-reference") is technically true but omits that `applications/` was created, OI-004 tally advanced, Skeptic minority was preserved. Future sessions asking "when was `applications/` created?" need the paragraph. They currently get it from SESSION-LOG.md.

Evidence for (b): the drift happened without deliberation. An unsaid rule ("paragraph per entry") that is operationally load-bearing should be explicit.

Evidence against (a): the spec's intent was tested only in the first few sessions, which were simple enough for one-line. One-line is not inadequate in general; it is inadequate for recent complexity.

My Q3 proposal honours the drift's informational substance while correcting the discipline shape: paragraph content preserved in per-session files; index returned to one-line-per-entry as spec'd originally. Neither intent nor accumulated content is lost.

## Q8 — Anti-laundering check

Session 014 Skeptic Q7 test applied to each proposal.

### Q2 accommodation pressures

Per-OI files could weaken cross-OI interaction tracking. Currently, reading open-issues.md top-to-bottom surfaces adjacencies (OI-014↔OI-016 interdependence is visible because the bodies are near each other). Once split, cross-OI references require explicit citation; missing references are less visible.

**Mitigation**: the index lists all OIs. Cross-file textual references preserve the same content; the same text is read, just across files. Grep remains equally effective.

**Falsifier threshold for Splitter-on-Q2** *(If I argued deferral instead, the threshold would be)*: at 50-session horizon, open-issues.md remains under ~150KB and individual OIs under ~10KB, segment-reading remains reliable for the question-types future sessions actually ask. Unlikely — OI-004 alone is already 14KB open-pending-criterion-4. But that is the falsifier: if OI-004 resolves and OI-016 resolves on first-exercise pass, the single-file may hold longer than I project.

### Q3 accommodation pressures

Moving summaries to per-session files could encourage *longer* summaries — per-file ceilings are looser than the single-file ceiling, and the informal "don't bloat SESSION-LOG" discipline is lifted. Bloat migrates to per-session files, where at ~50KB/session the ceiling would eventually return.

**Mitigation**: amendment includes soft target ("typically 3–10 short paragraphs"). Analogous to kernel's existing terseness norms.

The Skeptic-expected pressure to *shorten* summaries does not materialise under my proposal — the content moves, it is not cut. The "lose historical reasoning" risk is sidestepped by giving paragraphs their own address.

**Falsifier threshold for Splitter-on-Q3**: if a session at 30-session mark can still Read SESSION-LOG.md in one call (total under ~80KB ≈ 25k tokens). Trajectory is ~3KB/session [brief §3]; session 30 projects ~95KB. Unlikely, but that is the falsifier.

### General check: does the change widen what counts as pass?

- Does split make it easier to *omit* an OI annotation? No — work is the same, just localised. Per-file diffs are arguably more visible than monolith-scroll diffs.
- Does split make SESSION-LOG updates stylistically inconsistent across sessions? Slightly — monolith column-shape enforces visual consistency. Mitigation: frontmatter fields (`session`, `date`, `title`, `status`) carry the consistency contract; body style may drift but structured fields don't.

Accommodation pressures exist but are bounded and mitigable. The structural fix is not laundering deferred discipline; it explicitly recognises that single-file scale has hit a specific technical ceiling, and gives the content appropriate filesystem shape.

## Honest-limits

1. **Structural+tool combined case not assessed.** Per [brief §8] I treated tool adoption as separate. A complete deliberation should weigh combined vs structural-alone; I left this unassessed.

2. **External-application asymmetry not developed.** [Brief §8 Outsider] asks whether external workspaces (short-lived, fewer sessions) face this scaling differently. If they don't, engine-v2 cost is paid by all external applications to solve a self-development-only problem. The alternative — splitting only the development-provenance files (which manifest §4 already excludes from engine) *without* a workspace-structure.md spec change — may be more proportionate. I did not develop this branch.

3. **Engine-manifest.md §7 amendment not drafted.** If Q2/Q3 are adopted substantive, the decision record also declares engine-v2 per manifest §5 and §7 needs a new entry. Mechanical once decided; I flag but do not draft.

4. **Migration procedure unspecified.** Splitting is a one-time content-preserving migration. I have not specified whether this is a Produce activity within Session 020, a close-of-session operation, or a separate migration session. I have not checked whether `validate.sh` Checks 4 or others assume single-file shape and need updating.

5. **50-session-horizon assumption.** I designed for 50 sessions per brief framing. If the horizon is much shorter (early stable closure), some argumentation deflates. If much longer, my design itself may need re-revision before then. Not stress-tested for either asymmetry.

6. **Pretraining-sourced analogues surfaced** [per §10]: ADR pattern, monorepo `changelog.d/`, Obsidian-per-entry files. Candidate shapes, not proof at this workspace's exact scale.

7. **Unexplored alternative**: a cleverer in-file shape preserving single-readability (e.g., aggressive summarisation of old annotations collapsed into footnotes). I did not argue this because growth is structural (per-OI, per-session accretion) rather than bloat-cuttable, but I acknowledge the branch exists and I prefer directory-hierarchies — which is itself an accommodation pressure.
