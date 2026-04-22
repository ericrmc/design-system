---
session: 020
title: Shared Brief — Workspace Scaling Deliberation (SESSION-LOG.md + open-issues.md; Tool Adoption)
date: 2026-04-22
status: anchor-committed
---

# Shared Brief — Session 020 Workspace Scaling Deliberation

**This brief is committed as the deliberation anchor before any perspective-launch per multi-agent-deliberation.md v3 D-017.** The same brief is given to all four perspectives (3 Claude subagents + 1 non-Claude Outsider).

## §1 — Methodology context

You are participating in the self-development application of the Selvedge engine (per `PROMPT.md` dispatcher + `prompts/development.md` + `specifications/engine-manifest.md` v1). Session 020 has opened under Path (E) of Session 019's close menu: **operator-directed agenda**. The operator ratified a session topic they themselves named (the ratification message is quoted verbatim in §2 below). Your work is one of four independent perspectives on the chosen topic.

The engine-definition spec set (per engine-manifest.md §3) is: `PROMPT.md`, `prompts/development.md`, `prompts/application.md`, `specifications/methodology-kernel.md`, `specifications/multi-agent-deliberation.md`, `specifications/validation-approach.md`, `specifications/workspace-structure.md`, `specifications/identity.md`, `specifications/reference-validation.md`, `specifications/engine-manifest.md`, `tools/validate.sh`. **A substantive revision to any engine-definition file bumps the engine version per engine-manifest.md §5.** `engine-v1` is current.

## §2 — Operator input (verbatim domain reading)

On Session 020 engagement, the operator wrote:

> E.
> At the start of this session, referring to the SESSION-LOG.md and open-issues.md, you commented "Both large files. Let me read them in segments, starting with most recent content."
>
> `specifications/workspace-structure.md` states for `open-issues.md` that "This is a single file, not a directory, unless the number of issues makes a single file unwieldy."
> You should consider if the system would benefit from a discussion on this. As the number of words increases, you may also find benefit from the installed "mempalace" tool. This offers high-performance indexing and semantic search once text files are mined, so that not all files need to be read into context. If you deliberate and find this optimisation useful, run the `mempalace` CLI command with the help flag to learn how to set up a wing and mine text files. You may find similar or better tools are available to install via `uv tool`.

**Recording per OI-015 laundering-gap discipline (kernel §1 Read reconciliation clause):** the operator input is surfaced as domain reading, not absorbed as decision. The operator names (a) a candidate problem (file-scaling friction), (b) a candidate partial-solution (split per the spec's own anticipation clause), and (c) a candidate tool (mempalace). Each is **input** — not given context. The deliberation must re-examine each as a choice on its merits; agreement with operator input is not presumed.

The orchestrating agent's session-open comment the operator references is real: both files exceed the 25,000-token single-read ceiling and required segment-reading at `00-assessment.md` authoring time.

## §3 — Problem quantification

Current state of the two files at Session 020 open:

| File | Lines | Words | Bytes | Est. tokens | Single-read status |
|---|---|---|---|---|---|
| `SESSION-LOG.md` | 23 | 8,155 | 67,600 | ~25,713 | **Exceeds Read ceiling** (cannot read in one call) |
| `open-issues.md` | 203 | 8,986 | 69,954 | ~25,007 | **Exceeds Read ceiling** (cannot read in one call) |

Growth trajectory:
- SESSION-LOG.md: one logical entry per session. 19 sessions have produced 23 lines (some early sessions had short entries; recent sessions have prose paragraphs per entry). Per-session bytes have drifted upward over time. At current per-entry size, each future session adds ~3,000 bytes.
- open-issues.md: 12 active OIs + 5 resolved. Active OIs accrete annotations per session (e.g., OI-004 has ~8 KB of session-specific tally annotations; OI-016 has ~5 KB).

Operational impact observed in Session 020 open:
- Orchestrating agent could not read either file in one call.
- Had to use targeted `offset`/`limit` reads, `Grep` for specific sections, and `head`-style line counts.
- Session 020 audit work was accomplished under segment-reading; no information loss detected *for this session's specific audit questions*.
- Risk for future sessions: Read (workspace reading) becomes increasingly selective; context retention may degrade if important prior reasoning is in segments the orchestrator does not load.

## §4 — Current spec text (workspace-structure.md v3)

### §4.1 — `SESSION-LOG.md` spec text

> A running index of sessions for quick orientation. Each entry is one line containing the session number, date, title, and a brief note on what was accomplished. This file is updated at the close of each session.

Observations:
- Spec says "one line" per entry. Current file honours this syntactically (23 lines for 19 sessions + header = 4 unused lines). The "one line" prose blocks have grown to paragraph length.
- Spec says "brief note on what was accomplished." Current entries are closer to executive summaries than brief notes.
- Spec does not anticipate directory-split (unlike open-issues.md).

### §4.2 — `open-issues.md` spec text

> A list of known questions, gaps, uncertainties, and unresolved disagreements. Each entry has a brief description, the session that identified it, and its current status. Issues are removed when resolved (with a reference to the session that resolved them). **This is a single file, not a directory, unless the number of issues makes a single file unwieldy.**

Observations:
- Spec explicitly anticipates directory-split at unwieldy scale.
- "Issues are removed when resolved" — but current file preserves resolved issues in a ## Resolved Issues table rather than removing them. This is a pragma-vs-spec drift recorded for possible surfacing.
- The "brief description" intent has drifted to multi-paragraph annotations per OI (OI-004 is most extreme).

### §4.3 — Engine-version-bump rule (engine-manifest.md §5)

> The engine version (`engine-v1`, `engine-v2`, ...) increments when any file in §3 changes in substance. "In substance" means:
> - A new engine-definition file is added to §3.
> - An existing engine-definition file receives a substantive revision (v-bump per the spec-revision discipline in `workspace-structure.md`).
> - An engine-definition file is removed or superseded.

**workspace-structure.md is in §3.** A substantive revision is engine-v1 → engine-v2. This is a non-trivial decision surface — engine version is what external applications pin to.

## §5 — Tool landscape

### §5.1 — `mempalace` v3.1.0 (already installed via `uv tool`)

Subcommands (from `mempalace --help`):

- `init <dir>` — Detect rooms (logical groupings) from folder structure. Sets up a palace wing.
- `split <dir>` — Split concatenated transcript mega-files into per-session files (pre-mine step).
- `mine <dir>` — Mine project files. Modes: `projects` (default; code, docs, notes), `convos` (chat exports). Respects `.gitignore` by default.
- `search "query" [--wing WING] [--room ROOM]` — Exact-word search across mined content.
- `wake-up [--wing WING]` — Show L0 + L1 wake-up context (~600-900 tokens).
- `compress [--wing WING]` — Compress drawers using AAAK Dialect (~30x reduction claimed).
- `hook` — Reads JSON from stdin, outputs JSON to stdout (integration hook).
- `instructions` — Output skill instructions.
- `repair` — Rebuild palace vector index.
- `status` — Show palace state.

Current palace state: one existing wing `assistant-vault` with 12 rooms and 1,405 drawers. No wing for this workspace (`complex-systems-engine`) exists.

Migration shape if adopted: `mempalace init .` in workspace root (detects rooms from folder structure — would likely produce rooms for `specifications`, `provenance`, `applications`, `prompts`, `tools`, plus root-level `SESSION-LOG.md` and `open-issues.md`). Then `mempalace mine .` to index contents.

Operational retrieval pattern: instead of `Read SESSION-LOG.md`, orchestrator runs `mempalace search "Session 017 decisions" --wing complex-systems-engine` and gets only relevant drawers. Wake-up provides a compressed high-level view in ~600–900 tokens.

### §5.2 — Other installed tools (via `uv tool list`)

- `markitdown` v0.1.5 — document-to-markdown converter (Word/PDF/HTML → Markdown). Useful for external-source ingestion; not directly relevant to internal-file-scaling.
- `pytest` v9.0.3 — Python testing. Not relevant here.
- `serena-agent` v1.1.2 — MCP server already active in the current Claude Code session; provides semantic coding tools (symbol-level reads, memory system). Serena's memory system is project-scoped (`.serena/memories/`) but is code-oriented rather than prose-indexing-oriented. Possible-but-marginal fit for this problem.

### §5.3 — Tool alternatives (not yet installed)

The operator's message authorizes investigation of `uv tool`-installable alternatives. Candidates in the general space:

- **`ripgrep` / `rg`** (Grep backend) — already available via Claude Code's Grep tool; fast exact-text + regex search; does not do semantic search.
- **`fzf`** (via shell) — fuzzy interactive search; not autonomous-agent-friendly.
- **Vector-search libs** (e.g., `chromadb`, `sentence-transformers` + `faiss`) — require setup + embedding models; overkill for this workspace's current size.
- **`git grep`** — for searching historical versions; already usable without install.
- **File-format converters**: beyond markitdown, specialised extractors may exist but the files at stake are already Markdown.

**Default assessment:** `mempalace` is already installed, has non-trivial feature-overlap with the problem, and is maintained. If a tool is adopted, it is the leading candidate. A "no tool" outcome is also on the table.

## §6 — Surveying (prior patterns inside and outside the workspace)

### §6.1 — Internal precedent: how the workspace has scaled so far

- **Specifications**: preserved via file-suffix versioning (`*-v1.md`, `*-v2.md`, etc.). Each spec is one file; no spec has been split into a directory. `methodology-kernel.md` v4 is still one file; its v1/v2/v3 predecessors are separate files at `methodology-kernel-v1.md` etc.
- **Provenance**: one directory per session (`provenance/NNN-<slug>/`). Each directory has numbered reading-order files (00-assessment.md, 01-deliberation.md, etc.). This pattern scales linearly with sessions; no in-directory split yet needed.
- **Applications**: one directory per application (`applications/NNN-<slug>/`). Similar scaling discipline.
- **SESSION-LOG.md + open-issues.md**: single-file at workspace root; not yet split; the structural layer the operator is asking about.

### §6.2 — External patterns (agent surveys own pretraining; record explicitly)

This survey is the orchestrating agent's domain reading and is being surfaced explicitly per OI-015 discipline. Perspectives should treat these as candidate inputs to evaluate, not as established facts.

- **Monorepo `CHANGELOG.md` convention**: often split at scale into `changelog.d/` (e.g., via `towncrier`), with per-change-entry files that concatenate at release.
- **ADR (Architecture Decision Record) pattern**: each decision in its own file (`docs/adr/NNN-title.md`), not a single file. Analogous to per-OI files.
- **Issue trackers (GitHub, Linear)**: one issue per record; full-text search is central. Analogous to what mempalace provides for open-issues.md.
- **Journalling/knowledge systems** (Obsidian, Logseq): per-entry files with tag-based aggregation; cross-linking via backlinks.
- **Session-log patterns in agentic workflows**: often one file per session (`sessions/NNN.md`) concatenated on demand rather than a single running log. Per-session files enable targeted reads.

### §6.3 — Prior internal deliberations directly relevant

- **Session 001 D-001 (workspace structure v1)**: `SESSION-LOG.md` and `open-issues.md` created as single files. Rationale: minimal structure at genesis; directory splits deferred to "when unwieldy."
- **Session 009 D-054**: created `applications/` as new top-level directory after Session 008's external artefact forced the question. Precedent for "create directory when a single-file answer stops working."
- **Session 017 D-074**: engine-manifest.md split PROMPT.md into dispatcher + two mode-specific prompts. Precedent for "split a file when a single-file answer conflates roles."
- **OI-007 (scaling the open issues format)**: surfaced Session 001; currently open; the count-based argument has been consistently "count oscillates between 12–13, format scales adequately." But the count-based argument does not speak to per-OI annotation-size growth. OI-007 may be load-bearing for this deliberation.
- **OI-002 (substantive vs minor revision heuristic)**: workspace-structure.md revision substantive would be OI-002's 9th data point.

## §7 — Design questions

Each perspective should address all eight questions.

**Q1 — Is the observed friction load-bearing or cosmetic?**
The orchestrator completed Session 020's audit under segment-reading without detectable information loss on the audit-specific questions. Is that sufficient evidence that segment-reading is an acceptable workaround? Or is "no detectable loss on this audit" an under-powered test — i.e., does the risk live in *future* sessions whose Read activity may miss context the current-session approach happens not to need? Quantify the risk: what specific methodology properties are at stake if Read (workspace reading) becomes selectively segmented by default?

**Q2 — Structural fix surface: file-split for `open-issues.md`.**
The spec explicitly anticipates "directory, if unwieldy." What specifically does the directory shape look like? Options include:
- One file per OI (`open-issues/OI-002.md`, `open-issues/OI-004.md`, ...) with an index file.
- Split by status (`open-issues/active/`, `open-issues/resolved/`).
- Split by family (e.g., `open-issues/cross-model/`, `open-issues/spec-heuristics/`).
- Hybrid.

Evaluate: which shape best serves Read (workspace reading)? Which best preserves provenance continuity (per kernel §1 domain-reading discipline)? Which is most amenable to git-diff review across sessions?

**Q3 — Structural fix surface: SESSION-LOG.md.**
Spec says "one line per entry, brief note." Current entries are paragraph-length prose. Two shape-options:
- **Enforce brevity**: rewrite current entries to conform to spec intent; make provenance `03-close.md` the canonical detail. SESSION-LOG becomes a true index. Cost: rewriting history-prose feels lossy; but the detail *already exists* in provenance close docs.
- **Re-spec the file**: document the current paragraph-per-entry reality; possibly split to `session-log/NNN.md` per-session files with a top-level index.
- **Hybrid**: keep one-line entries in SESSION-LOG.md; move current-paragraph content into provenance close docs (which already have it) or new `session-log/NNN-summary.md` files.

Which shape best serves Read (workspace reading)? Which respects the spec's original intent vs ratifying current drift?

**Q4 — Tooling fix surface: `mempalace` adoption.**
Does indexing + semantic search solve (or materially reduce) the friction without structural change? Concrete evaluation:
- Would `mempalace search "Session 017 D-074"` be a satisfactory substitute for `Read SESSION-LOG.md offset/limit`?
- Does `mempalace wake-up` provide enough high-level context to substitute for reading SESSION-LOG.md entirely?
- What fails if tool is unavailable (e.g., CI environment, fresh clone, external application using the engine)?
- What's the cost of tool-dependency for an engine that aspires to be domain-general and text-only?

Concrete proposal shape: "mempalace is orchestrator-convenience-only; not an engine-definition dependency; orchestrator may choose to use it; specs unchanged" vs "mempalace is part of the engine load, specs reference it."

**Q5 — Interaction between Q2, Q3, and Q4.**
Are these three surfaces mutually exclusive, complementary, or redundant?
- If mempalace is adopted (Q4), is the structural fix (Q2, Q3) unnecessary?
- If structural fix is adopted (Q2, Q3), is mempalace still worth adopting?
- Is there a minimum-viable-change that addresses the friction with the smallest engine-definition surface touched?

**Q6 — Engine-version impact.**
Substantive revision to `workspace-structure.md` bumps engine-v1 → engine-v2 (per engine-manifest.md §5). What is the minimum-change that (a) addresses the observed friction *and* (b) avoids the version bump (i.e., minor revision: elaboration within existing scope)? The spec's own anticipation clause — "unless unwieldy" — may admit directory-split as a "change anticipated by the spec's existing language" — which is the OI-002 minor-revision criterion. Is directory-creation for open-issues.md substantive or minor?

Does SESSION-LOG.md restructure necessarily bump version, given the spec does not anticipate a split there?

**Q7 — Preserve or revisit one-line-per-session SESSION-LOG intent.**
The current drift from "brief note" to "executive-summary paragraph" happened organically. Does the drift represent (a) the spec's original intent being inadequate (entries *need* to be longer to serve "quick orientation"), (b) discipline failure (entries got bloated over time without anyone resisting), or (c) genuine informational need (future sessions rely on these paragraphs for Read)? Which interpretation is right? What's the evidence?

**Q8 — Anti-laundering check.**
Session 014 Skeptic's Q7 test: does this change widen what counts as pass? Apply to each proposal:
- Does file-split for open-issues *weaken* any methodology discipline (e.g., make it easier to lose track of OIs across files)?
- Does tool adoption *weaken* any discipline (e.g., orchestrator relies on tool's semantic search and misses issues the tool's index does not surface)?
- Does shortening SESSION-LOG entries *lose* historical reasoning that future sessions need?

Where is the accommodation pressure? Name it specifically.

Per Session 015/019 Minimalist precedent: *"If I argued deferral instead, the threshold would be..."* — state the falsifier threshold for your position as part of Q8.

## §8 — Role-specific stances

**Splitter.** You advocate for structural change: split one or both files per their scaling pressure. Your task is to propose concrete directory shapes (Q2, Q3) that address the friction through workspace-structure.md revision. Treat mempalace as *separate* from your proposals; structural fix should stand alone. You should design for the 50-session horizon (i.e., workspace-structure.md revised now should not require re-revision at session 50). You carry Session 014 Architect pure-within-session-shape minority forward *in spirit* (prefer in-file mechanisms over hand-offs when possible; but this specific case may warrant a hand-off-shaped solution — argue your choice).

**Tooler.** You advocate for tool-first solution: keep the spec files as-is (or with minimal change) and solve the friction through retrieval tooling. Your task is to propose a concrete mempalace-adoption shape (Q4) that reduces the friction without workspace-structure.md substantive revision. Address the tool-dependency concern: what does the engine lose if it depends on mempalace? Your strongest argument is probably the "specs describe content; tools retrieve it — don't conflate them" separation principle. Your weakest argument is probably the "orchestrator convenience doesn't count as engine requirement" edge case.

**Skeptic.** You are adversarial. Your first question is whether this session's work is warranted at all. The orchestrator completed Session 020 audit under segment-reading without reported information loss. Argue the strong-defer case: current workaround is adequate; any structural change bumps engine-v1 → engine-v2 (a significant change-event); any tool adoption introduces dependency surface that external-application workspaces may not have. You inherit Session 019 Minimalist defer-revision posture forward to this session. Your second question, if the deliberation proceeds, is to find the accommodation pressure in any proposed change — what thresholds would be lowered, what discipline weakened? You are not bound to "no change" — you are bound to maximally adversarial scrutiny of any proposed change.

**Outsider.** You are a non-Claude participant (GPT-5.4 via `codex exec`). Cross-family view is valuable here because file-scaling patterns and tool ecosystems are domains where different training-distribution perspectives may surface different norms. You are authorized to challenge the *frame* of the deliberation (per Session 017 precedent): if the Q1-Q8 questions are the wrong questions, name better questions. You are *not* bound to endorse the Splitter, Tooler, or Skeptic positions; a fourth-way is on the table if you propose one with operational warrant. Particular contribution-surface: you may be better positioned than Claude perspectives to assess (a) whether the operator-named mempalace tool has general-purpose merit vs ecosystem-specific fit, (b) whether external-application workspaces (the engine's asserted external claim) would face the same scaling problem differently.

## §9 — Response format

Produce a Markdown response with sections Q1 through Q8. Use explicit citation format `[01x, Qn]` when referencing your own content and `[brief §X]` when referencing this brief. Include any draft spec text *inline* (not pasted from files) so synthesis can assess text coherence. If your position adopts a proposal, *draft the exact text* for any spec amendment you propose. If your position preserves status-quo, argue *specific falsifiers* that would move you off that position.

At the end of your response, add a single section **"Honest-limits"** listing anything you know but did not address, or any reasoning you would need additional evidence to complete. Include the Session 014 Skeptic Q7 anti-laundering check applied to your own proposals (see §7 Q8).

## §10 — Constraint on external imports

Per PROMPT.md anti-silent-import rule: if you use an idea from your pretraining (e.g., a file-scaling pattern from a specific codebase tradition, a tool-ecosystem observation), surface it explicitly as survey-input — *"From my pretraining, I recall that ..."* — rather than stating it as established fact. The orchestrator will treat surfaced-pretraining claims as candidate evidence to evaluate, not as given facts. Unsourced assertions that could be pretraining-derived weaken your argument.

## §11 — Closure

This brief is committed as the deliberation anchor. Perspective files (`01a-perspective-splitter.md`, `01b-perspective-tooler.md`, `01c-perspective-skeptic.md`, `01d-perspective-outsider.md`) will be produced in isolation from each other and committed verbatim. Synthesis (`01-deliberation.md`) will follow. Decisions (`02-decisions.md`) and close (`03-close.md`) will complete Session 020.

No other substantive activity has occurred in Session 020 between the committed assessment (`00-assessment.md`) and this brief.
