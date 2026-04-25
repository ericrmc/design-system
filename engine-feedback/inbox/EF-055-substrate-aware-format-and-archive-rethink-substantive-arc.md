---
feedback_id: EF-055-substrate-aware-format-and-archive-rethink-substantive-arc
source_workspace_id: selvedge-self-development
source_session: 055
created_at: 2026-04-25T14:30:00Z
reported_by: operator
target: engine
target_files:
  - SESSION-LOG.md
  - specifications/read-contract.md
  - specifications/workspace-structure.md
  - specifications/engine-manifest.md
  - specifications/reference-validation.md
  - specifications/retrieval-contract.md
  - engine-feedback/INDEX.md
  - specifications/aliases.yaml
severity: friction
status: inbox
---

# EF-055 — Substrate-aware format and archive rethink (substantive-arc scope)

## Observation

Files in the workspace's default-read surface that grow accretively impose a structural read-to-edit cost paid every session (or every substantive event). The cost compounds with workspace age and is not addressed by the existing periodic-restructure precedent chain (S022 R8a / S040 D-123 / S051 D-178), which defers ceiling pressure but does not change the linear-growth shape.

**Strictly linear-per-session** in the default-read surface:

- `SESSION-LOG.md` — one row per session. Currently **6,598 words** at S055 close; soft warning fires; forecast hard-ceiling pressure window S058–S063 at current row-density cadence.

**Linear-per-event accretive without explicit bound**:

- `specifications/engine-manifest.md` §7 — one entry per engine-v bump (9 entries v1–v9; entries 500–1,500 words each).
- `specifications/workspace-structure.md` v6 §10.4 — one minority block per MAD that preserves a minority (M1–M11 currently).
- `specifications/reference-validation.md` v3 §10 — minority block per substantive RV revision (§10.1/§10.2/§10.3 with three minorities each).
- `specifications/retrieval-contract.md` v1 §7 — mirrored minorities (§7.1–§7.5).
- `engine-feedback/INDEX.md` — one row per feedback record (currently 7 lifecycle records).
- `specifications/aliases.yaml` — one entry per alias (currently 8 canonicals; alias fan-out 20).

**Effectively bounded** by existing rotation/count discipline:

- The 6 most recent `03-close.md` files (close-rotation §2c handles).
- `open-issues/index.md` — thin index with one-line status summaries and pointers; bounded by OI count not session count. **This is the model exemplar already in the workspace.**

The engine-v9 substrate (`search` + `resolve_id` + `forward_references`) provides cross-reference navigation that previously required prose-scan reading. Detail can live in per-record files; indices can be truly thin (open-issues-style: header + thin status phrase + path pointer). Adding a row to a thin index does not require reading the whole index first; the substrate handles "what was decided in S055?" via `resolve_id('S055')` or `forward_references('S055')` rather than requiring a prose summary in the index.

The S055 close §2 observation 1 demonstrated this empirically: `forward_references('S055')` at session-open surfaced 4+ S055-landing forward-commitments from S050 raw perspective files + 01-deliberation §6.1 that close-narrative-only relay across five consecutive close §7 lists did NOT enumerate. The substrate already does work that prose-scan reading was carrying.

## Why It Matters

1. **Read-to-edit cost** is paid every session for `SESSION-LOG.md` and on substantive sessions for the other accretive files. Reading a 6.5K-word file before appending a 30-word row is structurally wasteful when the substrate can index the content directly. The cost compounds with workspace age and applies to every future operator/agent interaction.

2. **Periodic restructure is reactive**. The S022/S040/S051 precedent chain treats accretion as a periodic crisis to be deferred. It works but the "thin-index-spirit-but-verbose-rows-in-practice" drift recurs because the per-row format itself isn't aligned with the substrate's affordances.

3. **The substrate enables the open-issues pattern at scale.** The §10.4-M10 Substrate-N2 minority preserved at S050 D-172 + mirrored at `retrieval-contract.md` v1 §7.4 is exactly the reframe direction this question lives in. Its activation warrants are framed in cost-or-dominance terms (phase-2 maintenance ≥2× across 3 sessions, or multi-hop ≥5× dominance over 5 sessions). This intake adds **operator-surfacing** as the activation channel — precedent: Path PD/PSD/OC/OS at S036/S043/S044/S045/S047 and Path AS at S049/S050.

4. **Continuing without reframe entrenches a discipline calibrated for prose-scan reading.** The S050 P3 outsider's framing — "Selvedge may not need a search product as much as it needs a fact discipline" + "The corpus is already heavily ID-structured. If each session writes durable thin rows for decisions, open issues, minorities, edges, and archive references, then a database can be rebuilt from those rows without re-interpreting prose" — describes the reframe target. The substrate makes it adoption-feasible at engine-v9; the question is whether to commit to the multi-session arc.

5. **Operator-surfaced scaling concern.** The accretive-file pattern is recognised as structurally unscalable; the substrate availability changes the urgency calculus. Specifically the SESSION-LOG read-to-edit cost is paid every session and the substrate availability for cross-reference navigation has matured through five organic-use-or-smoke-test sessions (S051 EF-051; S052 resolve; S053 EF-053; S054 resolve EF-053+EF-054; S055 forward_references first-organic-use).

## Suggested Change

Three directions for future-session deliberation. Operator's stated preference at intake: **Direction A**.

### Direction A — Substantive Substrate-N2 reframe arc (operator-recommended)

Multi-session MAD-based arc activating §10.4-M10. Re-design `read-contract.md` + `workspace-structure.md` + accretive-spec-blocks under the principle: **substrate is source-of-truth for cross-reference navigation; prose specs hold normative content only; accretive blocks become thin indices pointing to per-record files.**

Concrete shape candidates (for the arc to deliberate):

- **`SESSION-LOG.md`** → thin pointer-only index (`| NNN | YYYY-MM-DD | <one-sentence-title> | →path |`); detail in `03-close.md` (already there); cross-reference via `forward_references` + `resolve_id`. Pre-restructure preserved as archive-pack.
- **`specifications/engine-manifest.md` §7** → thin index `| Engine version | Session | Bump-provenance class | →path |`; detail moves to `specifications/engine-versions/v{N}.md` per-version files; substrate handles `resolve_id('engine-v9')`.
- **`specifications/workspace-structure.md` §10.4** → thin index pointing to `specifications/minorities/M-NNN.md` per-minority files; same for `reference-validation.md` §10 and `retrieval-contract.md` §7.
- **`engine-feedback/INDEX.md`** → already close to the right shape; tighten if needed.
- **`specifications/aliases.yaml`** → already structured/bounded; no change.

Engine-v10 candidate. Multi-session arc structure: synthesis session (design-space style per S049 D-157 precedent) → MAD session (4-perspective two-family per S050 lineup) → adoption session. Likely 2–4 sessions total.

Forward dependencies:
- The arc would necessarily revisit `read-contract.md` v5 §1 enumeration, §2 per-file budget calibration, §2c retention-window value (now that substrate makes "older closes" still queryable), §4 archive-pack structure (may simplify if structured-records replace prose blocks).
- Phase-2 substrate WX-50-1 gate is currently paused (`retrieval-contract.md` v1 §6); this arc may interact with the gate's status by surfacing query-class data (multi-hop, structured-filter) that activates §10.4-M10's empirical warrants from a different angle.
- The S050 P3 + P4 cross-family contributions on Substrate-N1 / Substrate-N2 / Substrate-N3 frames need to feed back into the deliberation; raw perspective files are preserved as archive surface but the arc should re-read them.

### Direction B — Tactical thin-index-plus-pointer extension (intermediate scope)

Apply the `open-issues/index.md` pattern to `SESSION-LOG.md` alone via Path L+A in the next routine-restructure session (S057-ish per S055 close §D-190g forecast). Each row reduces to `| NNN | YYYY-MM-DD | <one-sentence-title> | →path |` (~25–40 words/row asymptotic). Pre-restructure preserved as archive-pack. Defer the broader question. Minor per OI-002 per S022/S040/S051 precedent chain.

Buys ≥30 sessions of SESSION-LOG headroom under the new asymptote. Does not address `engine-manifest.md` §7 / `workspace-structure.md` §10.4 / `reference-validation.md` §10 / `retrieval-contract.md` §7 accretive blocks.

Compatible with Direction A: a Direction A arc subsumes Direction B's SESSION-LOG-only restructure as a subset of the broader reframe. Direction B as standalone preserves Direction A optionality for a later session.

### Direction C — Defer until §10.4-M10 activation warrants empirically fire (conservative)

Preserve the existing structure. Allow §10.4-M10 to activate per its written warrants:
- (a) cumulative phase-2+ maintenance time exceeds projection 2× across 3 consecutive sessions; or
- (b) multi-hop cross-reference query class dominates ≥5× prose-search over a 5-session window.

Restrict near-term action to periodic SESSION-LOG restructure per existing precedent chain (S057–S060 candidate window per S055 close §D-190g).

Conservative position; honours the §10.4-M10 minority's preservation rationale that adoption should earn expansion through measured use rather than anticipated architecture.

## Evidence

**Empirical signal that substrate provides genuine new affordance**:
- S055 close §2 observation 1 — `forward_references('S055')` first organic-use surfaced 4+ S055-landing forward-commitments from S050 raw perspective files + 01-deliberation §6.1 that close-narrative-only relay across five consecutive close §7 lists did NOT enumerate.
- S055 close §D-190f finding meta-observation — substrate-cross-reference-navigation does work that prose-scan reading was carrying; the value is empirically demonstrated not just argued.

**Existing accretive-file growth rates**:
- `SESSION-LOG.md`: 4,621 words post-S051-restructure → 6,598 at S055 close (4 sessions, +1,977 words avg ~494 words/session content-adaptive density).
- `multi-agent-deliberation.md` v4: 6,637 words stable 28 sessions (last edited S021).
- `reference-validation.md` v3: 7,160 words stable since S033 v3 adoption.
- `engine-manifest.md` §7: 9 versioned-entries; each substantive (500–1,500 words).
- `workspace-structure.md` v6 §10.4: 11 minority blocks (M1–M11); each ~200–400 words.

**Substrate-N2 framing source documents** (archive-surface; should be re-read at arc time):
- `provenance/050-session/01a-perspective-substrate-architect.md` §1.2 + §3.5 — substrate as read-model over canonical markdown.
- `provenance/050-session/01b-perspective-incrementalist-skeptic.md` §1 — what is wrong with continuing ripgrep + grep + git-log + validate.sh.
- `provenance/050-session/01c-perspective-outsider-frame-completion.md` §1 + §2 — "fact discipline" reframe + Substrate-N1/N2/N3 candidates.
- `provenance/050-session/01d-perspective-cross-family-reviewer.md` §1 + §2 — laundering audit of P1/P2; preserved-minority recommendations.
- `provenance/050-session/01-deliberation.md` §6 — synthesis with five preserved minorities.

**Standing minority preservation**:
- `specifications/workspace-structure.md` v6 §10.4-M10 — Substrate-N2 structured-artefacts-as-source-of-truth reframe minority.
- `specifications/retrieval-contract.md` v1 §7.4 — same mirrored.

**Pattern exemplar**:
- `open-issues/index.md` — thin index + per-OI files; bounded by OI count not session count; the model the linear-growth files should look like.

**Precedent chain for routine SESSION-LOG restructure** (Direction B baseline; subsumed by Direction A):
- S022 R8a (D-084) — pre-Session-022 SESSION-LOG restored to thin-index form.
- S040 D-123 — pre-Session-040 verbose multi-cell rows compressed back to thin-index.
- S051 D-177/D-178 — forced restructure on hard-ceiling breach; S041–S048 verbose rows compressed; archive-pack preserved.
- S055 close §D-190g — preemptive-restructure candidate window forecast S057–S060 if cadence holds.

## Application-Scope Disposition

Self-dev-originated; placed direct-to-inbox per `engine-feedback/INDEX.md` "Note on direct-to-inbox placement" convention. Precedent chain for direct-to-inbox: EF-051 self-dev-originated S051 → inbox; EF-053 self-dev-originated S053 → inbox; EF-054 operator-surfaced S053-post-session → inbox; **EF-055 operator-surfaced S055-post-session → inbox** (this record).

`source_workspace_id: selvedge-self-development` accurately reflects self-dev origin. `reported_by: operator` reflects operator-surfacing channel (precedent: EF-054 same field).

**Triage scheduled S056+**. Scope hint: this is **not** a defect-fix-shaped record (unlike EF-051 / EF-053 / EF-054 which were resolved as minor implementation fixes within one or two sessions). It is closer in shape to **EF-047-retrieval-discipline-and-text-system-scaling-ceiling**, which produced the S050 4-perspective two-family MAD via S049 design-space synthesis + S050 adoption. This intake is in the same arc-scope class.

If S056 default-agent state finds this the primary agenda, **Path T (Triage-classify)** is appropriate but with the understanding that triage will likely defer the substantive deliberation to a dedicated MAD session. Triage decision: classify substantive, schedule MAD, identify perspective composition (likely Substrate Architect / Incrementalist / Outsider non-Claude / Cross-Family Reviewer non-Claude per S050 lineup precedent + D-133 M2 lineage-constraint matrix).

If operator prefers earlier substantive scope, **Path PD/OS surfacing** at any subsequent session is also legitimate per S036/S043/S045/S047 precedent (operator-surfaced agenda activates §10.4-M10 deliberation directly without intake-triage delay).

If the arc proceeds to engine-v10 candidate, a synthesis session (Path SYN per S049 design-space precedent) would precede the MAD session (Path AS per S050 precedent) which would precede adoption. Two-to-four-session arc estimated.

**Operator's intake-time preference**: Direction A. Directions B and C preserved for completeness per S051/S053/S054 inbox-record convention.
