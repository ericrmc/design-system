---
session: 190
title: gate-promotion-deliberations — deliberation
generated_by: selvedge export
---

# Deliberation

## D-2 — D-A: OI-S083-1 proactive substrate-canonical reminder pathway

sealed_at: 2026-05-03T22:50:41.739Z

### P-3 (anthropic)

**Position.** Status-quo is sufficient. PreToolUse refuse-substrate-md.py already gates the failure; one slip in 100+ sessions is below DV-S152-1 graduation threshold; close OI-S083-1 by-mechanism with watch-FR.

**schema_sketch.**
- No new files, no new hooks, no new CLAUDE.md sections, no new file-header markers; tools/hooks/refuse-substrate-md.py remains the sole substrate-md gate as shipped at engine-v24.
- New issue row: FR-S190-X watch-trigger naming the substrate-detectable threshold for re-opening this deliberation; folds OI-S083-1's typed-observation bookkeeping into a smaller surface.
- Optionally: a one-line addendum atom on EF-S083-1's parent thread recording the close-by-mechanism disposition, but no spec-version, no prompt edit, no MODE.md edit.
**cli_surface.**
- None. Zero new bin/selvedge subcommands; zero new flags; zero changes to existing CLI surface area.
- Existing SELVEDGE_EXPORT_CONTEXT=1 bypass remains the recovery path; no rename, no scoping change.
**migration_path.**
- Step 1: submit DV closing OI-S083-1 by-mechanism citing DV-S109-1 ceremony-subtraction + DV-S152-1 graduation-precedent + zero recurrence S083 to S189.
- Step 2: submit FR-S190-X naming the watch-trigger (see Q6) so future agents have a substrate-anchored re-open condition without standing mechanism.
- Step 3: nothing. No hook deploy, no CLAUDE.md edit, no spec rewrite, no test additions; the engine surface ends S190 strictly smaller than it began.
**what_not.**
- Excludes pathway (a) PreToolUse hint mode: zero marginal catch over the existing refuse-hook on the only observed slip-shape.
- Excludes pathway (b) file-header markers: spends Read-context budget on every orient/reference read regardless of write intent; pure tax.
- Excludes pathway (c) CLAUDE.md pin: permanent session-open context cost amortised against zero confirmed catches in 7+ post-S083 sessions.
- Excludes any hybrid: each addition is non-free; combining two zero-catch mechanisms compounds cost not capability.
**open_question.**
- Cannot resolve whether unobserved near-misses occurred where the agent self-caught before tool emit; substrate has no negative-evidence row-shape for slips-not-made.
- Cannot resolve whether the post-S083 substrate-aware authoring hygiene reflects the EF itself working (calibration sufficed) vs reflects the underlying tool-shape just not recurring; both fit the data.
- Cannot resolve whether operator-presence on this OI selection signals a §1.5 operator-named-mandate or merely a deliberation-prompt; the role brief is explicit it is the latter.
**risk.**
- Status-quo risk: a future slip lands on a substrate-canonical path where refuse-hook glob does not match (e.g. new specifications/ subdir); recovery is extend TRACKED_PATTERNS, one round-trip, no substrate damage.
- Status-quo risk: the slip recurs at higher cost (e.g. before refuse-hook fires, via Bash echo bypass per the hook's own known-gap clause); recovery is the watch-FR triggering re-open with a now-justified pathway choice.
- Close-by-mechanism risk: future agents read OI-S083-1 disposition as precedent that one-instance OIs are auto-closed; recovery is DV cites recurrence-pressure-not-counts as discriminator, preserving DV-S152-1 discipline.
**what_lost.**
- Lost: any selection-time interception of the channel-disconnection EF-S083-1 named; the kernel accepts this as imperfect-but-recoverable per the T-23/T-29 post-hoc-repair precedent the role brief cites.
- Lost: the rhetorical comfort of having shipped *something* in response to a recorded slip; ceremony-subtraction (DV-S109-1) explicitly names this as the failure mode #6 the engine defends against.
- Lost: the option-value of pathway (c) CLAUDE.md pin as cheap insurance; preserved as a re-open candidate under the watch-FR if recurrence pressure materialises.

### P-4 (anthropic)

**Position.** Status-quo plus one tweak: rewrite refuse-hook stderr imperative-first (CLI on line 1, prose after) so post-selection bounce costs less. No new hook, marker, or CLAUDE.md pin on one observation seven sessions stale.

**schema_sketch.**
- Edit `tools/hooks/refuse-substrate-md.py` print block: lead with the bypass-or-substrate-CLI imperative on line 1, demote provenance prose; keep exit code 2 and tracked patterns unchanged.
- No edit to `~/.claude/settings.json` or `.claude/settings.json` — the PreToolUse matcher (Edit, Write, MultiEdit, NotebookEdit) is already correctly wired and untouched.
- No new file-header markers in `prompts/*.md` or `specifications/*.md`; no new CLAUDE.md section enumerating substrate-canonical paths.
**cli_surface.**
- None. No new `bin/selvedge` subcommand or flag. The recovery path (SELVEDGE_EXPORT_CONTEXT=1 plus spec-version body_md submit) is already documented in development.md §6 and reachable via refuse-hook stderr.
**migration_path.**
- Single PR: edit hook stderr block; add a pytest smoke test under `tools/hooks/tests/` if missing asserting exit-2-on-tracked-path; ship in same session as a coding-kind close.
- No spec-version revision required — the hook is execution-time tooling, not a methodology rule; T-32 substrate-gate logic is unaffected by stderr-prose change.
- No CLAUDE.md edit; no migration NN required since no schema change.
**what_not.**
- Excludes shipping pathway (a) PreToolUse non-blocking hint — adding a second hook on the same matcher doubles per-tool-call cost; the imperative-stderr fix captures most of the recovery-cost reduction.
- Excludes (b) file-header marker — EF-S083-1 slip was Edit-without-prior-Read (active modify-file shape carried from three prior Edits), so a Read-only marker has the structural blind-spot the role brief named.
- Excludes (c) CLAUDE.md pin — current CLAUDE.md is 16 lines tightly scoped; a substrate-canonical-paths enumeration competes with auto-memory-disabled clause for first-turn attention and dilutes existing pins.
- Excludes a fourth pathway (slug-prefix `SUBSTRATE_*.md`) — would require renaming engine-definition files across migrations 001-044 of provenance references, asymmetric cost vs leverage.
**open_question.**
- Whether operator-selecting-OI-S083-1-for-deliberation under presence at S190 is operator-named-mandate per §1.5 DV-S171-1; operator named the OI but not a §1.5 failure mode, so signal is ambiguous.
- Whether one calibration-EF plus operator queueing-for-deliberation crosses the DV-S152-1 typed-observation to gate threshold; my read is no, but synthesis may weight operator-presence higher than I do.
- Whether the imperative-stderr rewrite itself needs a calibration-EF at next observed slip to validate the cost-reduction is real, or whether that follow-up is itself ceremony per Q5#6.
**risk.**
- Imperative-stderr rewrite false-positive: if rewrite drops the `OI-085-002 (engine-v24)` provenance citation, future hook archaeology loses the breadcrumb; recovery is `git blame` on the hook file which is cheap.
- Status-quo risk: the next slip costs one more round-trip; recovery is the same SELVEDGE_EXPORT_CONTEXT=1 bypass that worked at S082, observed-cost one round-trip with no substrate damage.
- Risk that imperative-stderr is itself over-fitting to one observation; mitigated because it edits an existing surface rather than adding new mechanism, so subtraction discipline (Q5#5) is preserved.
**what_lost.**
- Forfeit: chance to ship a selection-time (pre-execution) reminder before next slip lands; existing hook intercepts at execution-time only, channel-connection failure mode remains unaddressed by status-quo.
- Forfeit: any substrate-detectable metric for slip-rate; hook stderr lives in transcript not substrate, so calibration-EF authoring at recurrence remains a manual operator-noticing-and-typing loop.
- Forfeit: option-value of pathway (c) CLAUDE.md pin as session-open always-loaded reminder; if the slip recurs across multiple file-types in one session, status-quo is worse than (c) for that shape.
- Q6 graduation trigger: one more slip-shape calibration-EF within next 10 sessions OR any single session with 2+ refuse-hook fires fires gate-promotion to pathway (a) imperative non-blocking hint with stderr scaffold reused.

### P-1 (anthropic)

**Position.** Ship CLAUDE.md pin enumerating substrate-canonical paths and CLI authoring commands; only harness surface firing before tool-selection, only pathway closing channel-connection gap EF-S083-1 named.

**schema_sketch.**
- Add a `## Substrate-canonical paths` section to `CLAUDE.md` enumerating the four globs from `refuse-substrate-md.py` and the substrate CLI authoring command for each glob category.
- Single-source the glob list: extract `TRACKED_PATTERNS` to `tools/hooks/substrate_paths.py`, import from the hook, and reference it from a close-time export check that asserts CLAUDE.md enumerates live globs.
- No edits to `refuse-substrate-md.py` behaviour; the execution-time refusal remains the adversarial baseline. No file-header markers. No PreToolUse hint mode (rejected — fires after selection).
- Add a new spec-version of `prompts/development.md` §6 cross-referencing the CLAUDE.md pin so the substrate-canonical authoring path is reachable from both surfaces with single-source naming.
**cli_surface.**
- None. No new `bin/selvedge` subcommands or flags. The existing `submit spec-version --payload {body_md: ...}` path is what the pin points at; adding ceremony around it would violate DV-S109-1.
- One new `bin/selvedge export --check-claudemd-sync` validation step, optional flag, that diffs CLAUDE.md enumerated globs against `substrate_paths.TRACKED_PATTERNS` and refuses export on drift.
**migration_path.**
- Step 1 (this session if shipped): extract `TRACKED_PATTERNS` to `tools/hooks/substrate_paths.py`; refactor `refuse-substrate-md.py` to import; add unit test asserting parity.
- Step 2: author `CLAUDE.md ## Substrate-canonical paths` section via direct edit (CLAUDE.md is operator-pinned harness context, not a substrate-canonical export, so direct edit is appropriate).
- Step 3: ship `bin/selvedge export --check-claudemd-sync` and wire it into the close-time export step so glob-list drift between hook and pin is substrate-detectable.
- Step 4: amend `prompts/development.md` §6 via `submit spec-version` to cross-reference the pin; this lands as a normal spec-version row.
**what_not.**
- Excluded: PreToolUse hint mode. Fires after selection, so it cannot close the channel-connection gap; it only echoes `refuse-substrate-md.py` with a token cost on every matched tool call.
- Excluded: file-header markers. They only fire on Read, miss Edit-first failure shapes, and spend per-Read context cost across every legitimate orient-by-reading episode.
- Excluded: hybrid. Pin alone is structurally sufficient; adding the hint mode coexists at per-call token cost without closing a gap the pin leaves open.
- Excluded: any substrate-side enforcement (typed table, kind, etc.). The pin is operator-pinned context, not substrate state; gate-promotion to substrate is reserved for the Q6 recurrence trigger.
**open_question.**
- Whether the S082 slip was Read-then-Edit (file-header would catch) or Edit-first (only pin catches) is recoverable from EF-S083-1 but not load-bearing for the structural argument.
- Whether the `claudeMd` system-reminder persists across long-context compaction is asserted from observed behaviour not documented contract; if it can drop, the pin's guarantee weakens.
- Whether `bin/selvedge orient` should also enumerate the substrate-canonical paths (cheaper if orient runs every session-open anyway) is worth considering as alternative-or-supplement.
**risk.**
- False-positive shape: zero per-tool-call. Pin spends one-time ~200-token session-open budget and never re-fires. Recovery: drift between pin and hook globs is caught by `--check-claudemd-sync` at export.
- Pin staleness risk: globs change in `refuse-substrate-md.py` and pin lags. Recovery: single-source extraction in step 1 makes drift substrate-detectable at export time.
- CLAUDE.md bloat risk: each future operator-pinned addition compounds session-open token cost. Recovery: hold CLAUDE.md to a budget; if it crosses ~2KB, refactor into substrate-driven orient-packet inclusion.
**what_lost.**
- One-time ~200-token session-open budget spent every session forever, regardless of whether the session touches substrate-canonical paths. This is the honest cost.
- The option to argue at the next slip that we tried nothing; shipping closes that fallback. I accept this — DV-S176-1 (prose-and-discipline failed) makes one observation sufficient structural evidence.
- Substrate-detectable withdrawal trigger: if pin is live 20+ sessions and a CLAUDE.md-enumerated-glob slip recurs (queryable as a calibration EF), pin failed and next deliberation escalates to substrate-side enforcement.

### P-2 (openai)

**Position.** Status-quo should hold; one cheap, damage-free refusal does not justify permanent or per-read context spend before recurrence.

**schema_sketch.**
- Add no schema, hook, file-header, or CLAUDE.md surface now; keep `tools/hooks/refuse-substrate-md.py` as the execution-time guard.
- Preserve OI-S083-1 as MEDIUM typed-observation; EF-S083-1 names the slip but not enough recurrence pressure to graduate.
- Graduation trigger is exactly one post-S190 calibration-EF naming a refused Edit/Write/MultiEdit/NotebookEdit on protected markdown with authoring intent.
- If that trigger fires, graduate to one compact CLAUDE.md pin before any PreToolUse hint or file-header marker.
- Future pin language: `Before Edit/Write/MultiEdit, treat prompts/*.md, specifications/*.md, provenance/**/*.md, open-issues/**/*.md as substrate exports; author with bin/selvedge submit.`
- Do not extend the protected path list to MODE.md or CLAUDE.md in this OI; that is a separate authority classification question.
**cli_surface.**
- None; existing `bin/selvedge submit spec-version --payload {body_md: ...}` and `bin/selvedge export --write` remain the recovery path.
- No hook telemetry CLI ships now; the next recurrence should be recorded as a calibration-EF with tool, path, intent, and recovery cost.
- If graduated later, no new CLI is needed because the CLAUDE.md pin points at existing submit kinds.
**migration_path.**
- Ship nothing in S190 for OI-S083-1 beyond this perspective evidence and the later synthesis or decision record.
- Keep the existing refusal hook unchanged and let it continue to catch direct authoring attempts without writing to the primary substrate.
- If the trigger fires, edit CLAUDE.md first, then update prompts/development.md by spec-version only if the synthesis wants the trigger codified.
- Remove the future pin after 20 sessions if zero same-shape slips recur and one calibration-EF names the pin as context noise.
**what_not.**
- Do not ship PreToolUse non-blocking hints; they fire after tool selection and on legitimate orientation reads, so they spend context without fixing the earliest failure point.
- Do not add file-header markers; they tax every read of generated markdown and can make exports look hand-authored.
- Do not add a CLAUDE.md pin on the present evidence; always-loaded context is strongest under pressure but its cost is paid in every session.
- Do not treat operator selection of OI-S083-1 as a DV-S171-1 mandate; it opens deliberation, but it did not name a live section 1.5 failure mode.
- Do not add Bash guards or state/migrations protections under this OI; EF-S083-1 named an Edit tool-shape slip on markdown exports.
**open_question.**
- The substrate currently cannot count hook refusals directly, so recurrence detection still relies on a calibration-EF unless a later gate adds event logging.
- The exact frequency of protected markdown reads per session is unknown, which makes PreToolUse hint and header costs hard to price without adding measurement.
- Status quo weakly discharges failure mode #1 because selection-time context can still drop the substrate rule under pressure.
- Status quo partially fails failure mode #2 because recent Edit momentum can still anchor action selection before the hook refuses.
- Failure mode #4 is neutral here because no substrate value is missing; the decision uses the observed one instance and zero recurrence since S083.
**risk.**
- Existing guard false-positive: an authorised export-like write without SELVEDGE_EXPORT_CONTEXT=1 is refused; recovery is set the bypass only for materialisation and rerun.
- Status-quo false-negative: the agent may select Edit again before remembering section 6; recovery is the existing refusal, then resubmit through `bin/selvedge`.
- PreToolUse hint false-positive would be orientation reads of protected markdown; recovery is ignoring the hint, which is precisely ceremony per legitimate read.
- File-header false-positive would be every Read of generated exports; recovery is deletion at next spec-version, which proves the marker was not free.
- Future CLAUDE.md pin false-positive is permanent context noise; recovery is withdrawal on the 20-session zero-recurrence plus calibration-noise trigger.
- Status quo discharges #5 and #6 by subtracting rather than adding, but it accepts weaker #1 and #2 protection until recurrence appears.
- Status quo discharges #3 through the hook and CLI authority split, while #4 is satisfied by exact recurrence thresholds rather than narrative estimates.
**what_lost.**
- We forfeit selection-time interception for now; the guard remains post-selection and catches only before execution.
- We forfeit the small chance that a CLAUDE.md pin would prevent the next slip without a refusal round-trip.
- We keep recurrence evidence noisier than ideal because `refuse-substrate-md.py` does not write guard-event rows.
- We preserve context budget for every session that only reads substrate exports for orientation.
- We preserve subtraction discipline from DV-S109-1 over the DV-S176-1 intuition that tool-reach failures should become dispatch.
- Evidence that changes this position is one more same-shape refused authoring attempt, or any successful Bash-mediated protected markdown write despite the documented guard gap.

### Synthesis

# D-A synthesis: OI-S083-1 reminder pathway

## Convergence (multi-source)

**C-1 — Status-quo holds under current evidence.** [P-2, position]; [P-3, position]; [P-4, position] — 3-of-4 perspectives converge that the existing PreToolUse refuse-substrate-md.py hook plus cheap one-round-trip recovery is sufficient under zero recurrence S083→S189 plus DV-S109-1 ceremony-subtraction discipline plus failure modes #5 (mechanism-addition default) and #6 (ceremony drift). [synth] The convergence is not over the channel-connection failure mode P-1 surfaced — all three concede the gap exists — but over the discriminator: zero observed recurrence is below DV-S152-1 graduation pressure.

**C-2 — File-header marker (option b) rejected.** [P-1, what_not]; [P-2, what_not]; [P-3, what_not]; [P-4, what_not] — 4-of-4 reject. Convergent reason: the marker only fires on Read, missing the Edit-without-prior-Read shape that EF-S083-1 explicitly named (active modify-file tool-shape carried from prior Edits).

**C-3 — PreToolUse hint mode (option a) rejected as standalone.** [P-1, what_not]; [P-2, what_not]; [P-3, what_not]; [P-4, what_not] — 4-of-4 reject in standalone form. Convergent reason: post-selection (closes no gap refuse-hook leaves open) AND per-tool-call cost on legitimate orient reads. P-4 names imperative-stderr tweak as a smaller intervention capturing the same recovery-cost reduction without the per-call cost.

**C-4 — CLAUDE.md pin (option c) is the right pathway IF graduation triggers.** [P-1, position (ship now)]; [P-2, schema_sketch (graduation target)]; [P-3, what_lost (preserved as re-open candidate)] — 3-of-4 converge on pin-as-graduation-target. P-4 alone names PreToolUse imperative non-blocking hint as their preferred graduation, citing existing stderr scaffold reuse.

**C-5 — Substrate-detectable graduation triggers anchor the watch.** [P-1, what_lost]; [P-2, schema_sketch]; [P-3, Q6/what_lost]; [P-4, Q6/what_lost] — 4-of-4 propose substrate-detectable triggers. Specific triggers vary (count of post-S190 calibration-EFs / refuse-hook fires per session / recurrence within rolling N-session window) but the discipline-shape converges.

## Divergence

**D-1 — Channel-connection-evidence vs zero-recurrence as the discriminator.** [P-1, position] argues the structural argument (selection-precedes-execution; CLAUDE.md is the only pre-selection harness surface; DV-S176-1 lesson applies) is sufficient evidence for ship-now; [P-2, position]; [P-3, position]; [P-4, position] argue zero observed recurrence plus DV-S109-1 ceremony-subtraction is the discriminator and the channel-connection gap is acceptable cost when recovery is one round-trip. The two framings reach opposite ship-decisions on the same evidence base.

## Minority

**M-1 — P-1 ship-now CLAUDE.md pin position.** Preserved as minority. Strongest insight: the channel-connection failure mode is structural (selection precedes execution; PreToolUse cannot intercept selection); the architecture-level argument that the close-path *should* be substrate-canonical regardless of count cuts the same way DV-S176-1 cut for chain-walks. Even ship-nothing perspectives concede the gap exists; they accept it as imperfect-but-recoverable per T-23/T-29 precedent (P-3 explicit on this lineage). Reopen condition: future calibration-EF surfacing a slip with recovery cost > one round-trip OR a slip bypassing the refuse-hook glob would graduate M-1's load-bearing weight to ship-now.

## [synth] — synthesis-original observations

**[synth] Substrate-detectability gap is load-bearing.** P-2 surfaces (open_question + what_lost) that refuse-substrate-md.py writes no substrate row, so all four perspectives' watch-triggers depend on the agent noticing-and-typing a calibration-EF. Without substrate-side instrumentation of refuse-hook fires, the trigger is *aspirational* not *substrate-detectable*. The synthesis adopts P-2's instrumentation observation as a load-bearing follow-up FR — the substrate-canonical answer to recurrence-pressure tracking that 4-of-4 perspectives implicitly require.

**[synth] Operator-presence does not constitute §1.5 mandate.** [P-2, what_not]; [P-3, open_question]; [P-4, open_question] all engage this question. The operator selecting OI-S083-1 for deliberation under presence at S190 opens substantive scope under §1.5 admissibility; absent the operator naming a §1.5 failure mode, the deliberation is not a DV-S171-1 mandate-shaped substantive close. The convergent ship-nothing position is therefore the recurrence-pressure-discipline answer, not the operator-said-ship answer.

**[synth] P-4 stderr-imperative tweak is a separate-and-smaller question.** Independent of the OI-S083-1 graduation question, the existing refuse-hook stderr block could be rewritten imperative-first (CLI command on line 1, prose after) to reduce per-slip recovery cost. This is ergonomic improvement to the existing surface, not new mechanism — it is properly a coding-kind FR for a follow-up session.

## Counterfactual disposition

C-A1 (counterfactual_id=4): ship substrate-detectability instrumentation as primary OI resolution rather than deferred-FR addendum — addressed-in-synthesis per C-5 plus [synth] substrate-detectability-gap; adopted as deferred FR-B not primary because kind=spec_only locks coding work this session and recurrence-pressure discipline favours minimal-close shape.

## Decision feed

The synthesis recommends:
1. Close OI-S083-1 by-mechanism citing convergent 3-of-4 ship-nothing per C-1 plus DV-S152-1 graduation precedent plus DV-S109-1 ceremony-subtraction.
2. Author follow-up FRs anchoring the substrate-detectable graduation work: (FR-A) watch-trigger union per C-5 — re-open OI on any of (a) one post-S190 calibration-EF naming Edit/Write/MultiEdit/NotebookEdit refused on substrate-canonical markdown with authoring intent; (b) one slip bypassing refuse-hook (Bash, glob-miss, symlink); (c) one slip with recovery cost > one round-trip; (FR-B) substrate-detectability instrumentation per [synth] — coding-kind work shipping refuse-hook substrate-side telemetry so the watch becomes queryable; (FR-C) stderr-imperative tweak per P-4 — coding-kind ergonomic improvement.
3. Preserve M-1 minority for D-23-style reopen if the channel-connection argument graduates to load-bearing on future evidence.

### Synthesis points

- **convergence C-1.** Status-quo holds under current evidence; existing PreToolUse refuse-hook plus cheap one-round-trip recovery is sufficient under zero recurrence S083-S189.
- **convergence C-2.** File-header marker (option b) rejected 4-of-4 — only fires on Read, misses Edit-without-prior-Read shape EF-S083-1 named.
- **convergence C-3.** PreToolUse hint mode (option a) rejected as standalone 4-of-4 — post-selection plus per-tool-call cost on legitimate orient reads.
- **convergence C-4.** CLAUDE.md pin (option c) is the right pathway IF graduation triggers; 3-of-4 converge on pin-as-graduation-target.
- **convergence C-5.** Substrate-detectable graduation triggers anchor the watch; 4-of-4 propose substrate-detectable triggers though specific shapes vary.
- **divergence D-1.** Channel-connection-evidence (P-1) vs zero-recurrence (P-2/P-3/P-4) as the discriminator; same evidence base reaches opposite ship-decisions.
- **minority M-1.** P-1 ship-now CLAUDE.md pin position preserved; channel-connection failure mode is structural; reopen on slip with recovery cost > one round-trip OR refuse-hook bypass.

## D-3 — D-B: L5 close-time substrate-filesystem divergence gate (FR-S187-16 + FR-S188-15)

sealed_at: 2026-05-03T22:56:51.480Z

### P-3 (anthropic)

**Position.** Status-quo is sufficient; ship no substrate-side gate; dispose FR-S187-16 + FR-S188-15 by-mechanism citing zero-recurrence and DV-S109-1; if a check is desired, extend tools/validate.sh.

**schema_sketch.**
- No new tables, columns, or triggers; export_manifest (DV-S188-1, migration 044) already provides the recovery index — adding a gate now is mechanism without observed payment.
- Reject any sqlite-trigger formulation outright: triggers cannot read filesystem, so any substrate-side gate is Python-handler code masquerading as substrate enforcement.
- The handler-side filesystem walk + sha256 in _submit_session_close couples a transactional surface (sqlite write_tx) to a non-transactional surface (working tree); that is a category error, not a feature.
**cli_surface.**
- None. No new bin/selvedge subcommands, no new flags on submit session-close, no new flags on export.
- Optional and minimal: tools/validate.sh gains a single block walking provenance/<latest>/ and warning (not failing) when L5 filenames are present on disk that dry-run export would not project.
- Even that block is deferred until one calibration-EF names a divergence-on-commit landing; until then the warning has no recurrence to discipline.
**migration_path.**
- S190 close-record disposes FR-S187-16 + FR-S188-15 with basis=ceremony_subtraction citing DV-S109-1 and zero-recurrence S187 to S189; opens a watch-FR analogous to FR-S082-17 trip-counter shape.
- The watch-FR specifies the substrate-detectable trigger: a calibration-EF with flag=calibration whose body names a stale-L5-on-commit landing observed in git history of provenance/.
- Re-open this deliberation when one such EF lands; no migrations, no handler edits, no spec edits ship in S190 on this question.
**what_not.**
- Excludes any handler-side filesystem walk inside _submit_session_close write_tx; that is the architectural smell, not a placement choice.
- Excludes a precondition-receipt-row pattern (option b in Q2): it inverts the close-path direction (export gates close) without adding capability over §9 prose discipline plus a 1-line validate.sh check.
- Excludes subtraction of §9 export-then-commit prose; the prose is the operator-policed compensator the substrate cannot replicate without coupling transactional + non-transactional surfaces.
**open_question.**
- The exact watch-FR trip-threshold: one EF or two? Default to one given the substrate-loss-defense package low recurrence tolerance, but P-1 + P-2 should debate.
- Whether the validate.sh warning should be silent until tripped or always-on; lean silent until first EF, then promote to always-on.
- Whether harness-file cross-session anchoring (FR-S187-15) materially complicates any future gate; defer answering until evidence forces the question.
**risk.**
- Cross-machine workflow false positive: operator A substrate-edits and exports on laptop, operator B closes on workstation with stale provenance/; gate refuses session-close with no recovery beyond re-running export.
- Cross-machine workflow false positive (cont.): high refusal-debt for legitimate workflow with no in-band recovery for the cross-machine handoff case.
- Concurrent-process race (cf. EF-S185-2): an IDE auto-format or another bin/selvedge process touches a provenance/ file mid-close; gate fires sha256 mismatch with no recovery beyond manual reconciliation.
- Operator deliberately edits an L5 file post-export to fix a typo then closes without re-export; gate refuses, operator either re-runs export (losing the edit since L5 is substrate-projected).
- Operator post-export-edit (cont.): or escapes the gate (proving the gate is theatre); the typo-fix workflow has no in-scope substrate path.
- M-1 framing from D-23 applies directly: a sha256-presence gate proves receipt presence not epistemic adequacy; passing the gate creates false sense the close is correct when only the file matches manifest last write.
**what_lost.**
- Forfeit the symmetry-with-T-39 narrative; argue the partial-symmetry matters — T-39 enforces close_records existence (substrate-internal property substrate fully owns), the proposed gate enforces filesystem state.
- Forfeit T-39 symmetry (cont.): the proposed gate enforces filesystem state which is not substrate-owned and is append-touched by external processes, breaking the symmetry argument.
- Forfeit DV-S176-1 prose-clauses-without-instrumentation framing as automatic: that lesson cuts for substrate-internal consistency (chain-walks), not for substrate enforcing filesystem state.
- Forfeit DV-S176-1 framing (cont.): concede the lesson applied at chain-walks; contest the extrapolation to filesystem-state enforcement.
- Forfeit the close-path should be substrate-canonical aesthetic; gain DV-S109-1 ceremony-subtraction and the failure-mode-#5 default-to-mechanism-addition kernel-defense in exchange.

### P-1 (anthropic)

**Position.** Ship T-NN now via receipt-pattern: export writes a per-session export_receipt row in its own write_tx; session-close handler refuses absent or stale receipt.

**schema_sketch.**
- New table export_receipts(session_no PK, receipt_sha256, manifest_row_count, projected_set_sha256, generated_at, engine_version) populated by export --write inside the same write_tx as record_manifest_entry calls.
- New T-NN dispatched handler-side from _submit_session_close (SQL triggers cannot stat filesystem) refusing E_REFUSAL_TNN when receipt missing or projected_set_sha256 stale vs current substrate dry-run projection.
- projected_set_sha256 = sha256 of sorted (kind,path) tuple list the dry-run export would emit for the session, computed handler-side at close from current substrate state and compared against the receipt.
- Cheap-exit table export_receipt_attestations(session_no PK, reason, attested_at) written by bin/selvedge export --attest-divergence; presence admits close on mismatch (mirrors DV-S180-1 nil_attestation shape).
- No change to export_manifest schema; the gate reads existing manifest rows plus the new receipt and attestation rows.
**cli_surface.**
- bin/selvedge export --session N --write writes export_receipts row in-band; no operator-visible flag change for the happy path.
- bin/selvedge export --attest-divergence --reason TEXT writes attestation row without re-running export; for cross-machine workflows where machine B closes a session whose export ran on machine A.
- bin/selvedge orient surfaces missing or stale export_receipt as a close-path blocker line (same shape as the existing T-39 close_records reminder).
- No --no-divergence-check flag on session-close itself; the cheap-exit lives at export, so the attestation is always a substrate row not a flag-on-handler.
**migration_path.**
- Migration 045 creates export_receipts plus export_receipt_attestations tables with UNIQUE(session_no) on each; engine bumps to v53.
- Migration 045 backfills one receipt per already-closed session in (180..189) by running dry-run projection at migrate-time; backfill makes the gate retroactively satisfied for historical closes.
- Edit selvedge/export/session.py _export_session_provenance to write the receipt after the manifest write loop, computing projected_set_sha256 from the same files dict the function already built.
- Edit selvedge/submit/session.py _submit_session_close to dispatch the receipt check before UPDATE sessions SET status=closed; refusal text names the recovery recipe (run export --write or export --attest-divergence then retry).
- Edit prompts/development.md §9 to delete the prose chain (export --write, validate, git commit) and replace with substrate-enforced ordering language since close now refuses without receipt.
**what_not.**
- Not a filesystem-walk-and-sha256-compare gate at close time; that re-implements export inside the close handler and produces false positives whenever any tool touches a manifest-tracked file post-export.
- Not a cross-session-anchored harness-file gate; FR-S187-15 scope-distinguished those and they need their own opening-session anchor design (deferred).
- Not a SQL trigger; SQLite cannot read filesystem and the receipt-pattern keeps the proof in-substrate where it belongs.
- Not a workspace-wide gate covering open-issues/index.md or specifications/_versions.md; those are workspace-scoped not session-bounded and reconciliation is already idempotent per S187 finding 30 fix.
- Not coexistence with §9 prose; the spec edit to delete the prose chain is part of the ship, not optional.
**open_question.**
- Whether projected_set_sha256 should include only filenames or also content sha256s; content-inclusive is stronger but couples the gate to byte-identical export determinism which any future formatter change would break.
- Whether migration 045 should backfill receipts retroactively or grandfather closed sessions with a sentinel receipt; the choice affects how much history the gate appears to have always covered.
- Whether the attestation row should expire (require re-attestation per close attempt) or persist; persist is simpler but creates a one-time bypass that future tooling could mistake for happy path.
**risk.**
- False positive when operator edits a manifest-tracked file post-export then closes; recovery is one re-run of export --write which regenerates the file from substrate, overwriting the manual edit per DV-S081-1.
- False positive on cross-machine workflow where machine A ran export and machine B closes; recovery is bin/selvedge export --attest-divergence --reason cross-machine on B which writes attestation in one command.
- Race against EF-S185-2-shape concurrent process touching files between export and close; recovery is restore from session-open-snapshot per DV-S081-1 plus re-run export; the gate adds no new race surface.
- Backfill in migration 045 fails if a historical session substrate state can no longer dry-run-project (e.g. rows wiped by S180 collision); recovery is the sentinel-receipt grandfather option.
- Receipt staleness if a substrate write lands between export and close (e.g. close-time engine-feedback row); mitigation is the §9 ordering already requires export immediately before session-close.
**what_lost.**
- One-step close ergonomics: operator must run export --write then session-close in that order with no intervening substrate writes; today the same ordering is prose-recommended but not enforced.
- Migration 045 surface area: two new tables plus engine bump, paying ceremony cost per DV-S109-1; the payment is closing the prose-and-discipline gap DV-S176-1 named as recurring.
- Operator option to skip export when intentionally committing stale markdown for a transitional session; never a sanctioned path but the gate forecloses it without a flag, only via attestation-with-reason.
- Some auditor flexibility: future tooling inspecting closed-session divergence as research artefact must now reckon with the attestation row as part of close evidence, not just manifest plus disk.

### P-4 (anthropic)

**Position.** Status-quo on _submit_session_close; extend tools/validate.sh with a sha256 reconciliation pass against export_manifest; defer substrate-receipt gate until first recurrence-EF lands.

**schema_sketch.**
- No new tables. export_manifest already carries path + sha256 + size_bytes + session_no keyed on UNIQUE(path) from migration 044, sufficient for filesystem-side reconciliation by an external script.
- No new triggers. SQLite cannot read filesystem so a SQL-trigger gate is structurally excluded; T-39 stays the close-path substrate-internal sibling.
- Optional future close_export_receipt table (one row per session capturing last-export sha-roll-up) gated on first recurrence-EF; not shipped now.
**cli_surface.**
- No new bin/selvedge subcommand. The check lives in tools/validate.sh so it runs on the existing operator-policed close path between export --write and git commit already documented in §9.
- Optional bin/selvedge export --verify-only (read-only walk recomputing sha256 against export_manifest rows) as a developer-loop convenience; out of this scope.
**migration_path.**
- Step 1: extend tools/validate.sh with a block that selects path,sha256 from export_manifest, recomputes sha256 of each path on disk, and fails on missing file or mismatch; runs only when substrate is present.
- Step 2: extend the same block to detect on-disk files under provenance/<wno>-<slug>/ matching L5_FILENAMES that are absent from export_manifest for that session_no (the disk-no-manifest shape).
- Step 3: add a pytest case under state/tests/ that seeds a stale on-disk file plus a tampered sha256 and asserts the validator block exits non-zero.
- Step 4: subtract from §9 the prose obligation to remember export --write ahead of validate (the validator now refuses if it was skipped) while keeping the three-step recipe block intact.
**what_not.**
- Not adding a Python filesystem walk inside _submit_session_close; that violates the substrate-only-writes-from-canonical-source principle and exposes the close write_tx to filesystem races (cf. EF-S185-2 concurrent-pytest race).
- Not auto-calling selvedge export --write from _submit_session_close; export is a presentation-layer operation, the handler is a substrate-state transition, mixing them inverts the dependency.
- Not handling cross-session-anchored harness files in this gate; FR-S187-15 punts the cross-session anchoring case and a session-scoped gate would only confuse the divergence signal there.
- Not gating on the projected-not-emitted shape via dry-run-export comparison; once export --write is required pre-validate, the validator already catches the skipped-export case without a separate projection pass.
- Not introducing a --no-divergence-check cheap-exit; cross-machine workflow is handled by the validator running on each machine working tree against its local substrate, not by an opt-out flag.
**open_question.**
- Whether the validator block should fail fast on first mismatch or enumerate all mismatches; enumeration is more diagnostic but doubles the walk cost on large provenance/ trees.
- Whether export_manifest rows for retired filenames (a kind dropped from SESSION_FILE_KINDS in a future engine version) should be tolerated or refused; the manifest kind enum is engine-version-scoped.
- Whether workspace-wide artefacts (open_issues_index, spec_versions_index) belong in the per-session validator block or in a separate workspace-wide reconciliation step; one combined block is cheap.
**risk.**
- False-positive: cross-machine workflow where machine-B pulls machine-A substrate but provenance/ is mid-edit; recovery is bin/selvedge export --session N --write then re-run validate, the existing §9 sequence.
- False-positive: operator hand-edits an exported markdown file post-export; recovery is to revert the hand-edit since substrate is canonical and prose-edits to exports are not authoritative per DV-S081-1.
- False-positive: export_manifest row pre-dates a kind-rename in a later engine version; recovery is the export pipeline rewriting on next --write via INSERT OR REPLACE per migration 044, validator passes after one re-export.
- False-positive: concurrent process touches export_manifest mid-validate; the validator is a read-only sha256 recompute outside any write_tx so it observes a consistent SQLite reader snapshot, no recovery needed.
- M-1 gate-proves-receipt-not-adequacy applies cleanly: a sha256 match proves the exporter wrote what export_manifest recorded, not that substrate state was epistemically adequate; this is a divergence gate, not a quality gate.
**what_lost.**
- The pure substrate-policed close path is forfeit: divergence-detection lives in bash not Python, so an operator who skips tools/validate.sh and goes straight to git commit keeps the existing failure mode.
- The T-32-shaped receipt-pattern symmetry with chain-walk-receipt + counterfactual-presence is forfeit; if recurrence-EF lands later, promoting the validator block to a substrate-receipt gate becomes the second-step path.
- A slice of §9 subtraction is forfeit: §9 still names tools/validate.sh as a step, but the prose obligation to remember the ORDER cannot be subtracted without the receipt-pattern; the validator enforces order by failing.
- DV-S109-1 reading: the validator extension is under twenty bash lines plus one pytest case versus a new table plus handler plus migration; the smaller addition pays for itself by closing the gap without a sixth substrate-gate.
- Constraint-discharge: failure modes #5 (mechanism-addition over subtraction) and #6 (ceremony-drift) cut hardest against a substrate-receipt gate on zero recurrence; the validator extension is the smallest mechanism that closes the gap.
- Failure modes #1-#4 are not engaged by the divergence question: no foundational-instruction-loss, no anchor-on-recent-decision, no authority-confusion, no narrative-numbers; the gate would not discharge them and is not asked to.
- The DV-S152-1 / DV-S159-1 graduation precedent is honoured: typed-observation first, gate second; export_manifest is the typed observation landed at S188, recurrence-EF on stale-file-on-commit is the missing graduation trigger.

### P-2 (openai)

**Position.** Graduate narrowly: export owns projection receipts, close verifies current L5 files against them, and intentional divergence needs a substrate attestation.

**schema_sketch.**
- Add close_export_receipts with session_no, scope, manifest_hash, projection_hash, disk_hash, row_count, generated_at, and engine_version.
- Add close_divergence_attestations with session_no, reason, file_count, created_at, expires_at, and consumed_by_close.
- Leave export_manifest from DV-S188-1 as the per-file recovery index and source for path, sha256, size_bytes, and row_count.
- Add no SQLite trigger; filesystem authority lives in Python because triggers cannot observe disk state.
**cli_surface.**
- Existing bin/selvedge export --session N --write records a close receipt after successful file writes and manifest reconciliation.
- bin/selvedge submit session-close refuses missing, stale, or mismatched L5 receipt state and prints the exact recovery command.
- Add bin/selvedge submit divergence-attestation --session N --reason TEXT as the cheap exit.
- Any --no-divergence-check spelling must create an attestation row, not silently bypass the gate.
**migration_path.**
- Ship a post-044 migration adding receipt and attestation tables without changing export_manifest rows.
- Edit selvedge/export/session.py so receipt emission happens after L5 reconciliation, including the delete-manifest-before-unlink ordering from DV-S187-1.
- Edit _submit_session_close to verify the current L5 session directory against the latest receipt before setting status closed.
- Edit prompts/development.md §9 to delete the session-close then export --write clause and the prose that export-before-commit is operator-policed.
- Keep tools/validate.sh after close as an audit step, not the closing authority.
**what_not.**
- Do not reimplement full projection logic inside _submit_session_close; export remains the single projection author.
- Do not enforce workspace-wide spec_versions in this first gate because it is not session-bounded.
- Do not cover FR-S187-15 cross-session harness files until their opening-session anchoring is modeled explicitly.
- Do not make markdown canonical or recover substrate state from markdown during this gate.
- Do not make a silent bypass flag; every bypass must be substrate-visible.
**open_question.**
- If closing status changes any receipt-covered file, the gate must either scope to status-independent L5 files or emit a post-close receipt.
- Three clean closes since DV-S187-1 narrow the blast radius but do not prove the §9 memory burden is durable.
- The right hash unit is unsettled: per-file sha256 may be enough, but a projected path-set hash would catch omission more cleanly.
- Cross-session anchored files need a separate owner model before a session close can police another session directory.
**risk.**
- Cross-machine pulls may lack generated files; recovery is run export --write on that machine or record an attestation for an intentional handoff.
- Manual post-export edits cause sha mismatch; recovery is rerun export or attest that generated markdown was intentionally diverged.
- Other tooling may touch previous session files; recovery is limited to the current L5 scope and affected sessions can be re-exported.
- EF-S185-2 style concurrent writes can produce transient partial files; recovery is retry after the writer exits and investigate repeat failures.
- The gate proves receipt presence, not epistemic adequacy; M-1 D-23 warning leaves review and tests as separate obligations.
**what_lost.**
- Pure substrate-only session-close is lost because close now depends on a recoverable but non-transactional filesystem projection.
- Some cross-machine flexibility is lost because each machine must materialize current generated files or record a bypass before close.
- Constraints #5 and #6 are stressed; the mechanism pays only if the §9 export-memory clause is actually removed.
- Constraint #1 improves because the close discipline no longer depends on recalling prose under context pressure.
- Constraints #2, #3, and #4 improve because close checks substrate receipts and hashes, not latest habit, speaker confidence, or narrative numbers.

### Synthesis

# D-B synthesis: L5 close-time substrate-filesystem divergence gate

## Convergence (multi-source)

**C-1 — SQL trigger structurally cannot work; placement must be Python.** [P-1, schema_sketch]; [P-2, schema_sketch]; [P-3, what_not]; [P-4, schema_sketch] — 4-of-4 perspectives agree triggers cannot read filesystem; the gate must live in the Python `_submit_session_close` handler, in an export-precondition handler, or in operator-side bash (`tools/validate.sh`).

**C-2 — `export_manifest` plus `L5_FILENAMES` already provide the divergence-detection data.** [P-1, schema_sketch]; [P-2, schema_sketch]; [P-4, schema_sketch] — 3-of-4 explicit (P-3 implicit by treating divergence-data as adequate-but-not-warranting-substrate-gate). The substrate now carries sha256 + path + size_bytes per emitted file (engine-v52, migration 044); the question is which placement queries it, not whether the data exists.

**C-3 — Receipt-pattern (T-32 model) is the architecture IF substrate-side ships.** [P-1, position]; [P-2, position]; [P-4, what_not (acknowledges T-32-shaped receipt is correct architecture but defers ship)] — 3-of-4 endorse the receipt-pattern as the correct architecture-when-shipping. P-1 + P-2 explicit on the receipt-row written by export, queried by close-handler. P-4 acknowledges the architecture but argues recurrence pressure has not justified the mechanism.

**C-4 — Divergence-attestation cheap-exit (mirror DV-S180-1 nil_attestation pattern).** [P-1, schema_sketch]; [P-2, schema_sketch] — 2-of-4 explicit. Coverage not full convergence; no perspective rejects this shape. P-1 proposes `bin/selvedge export --attest-divergence --reason TEXT`; P-2 proposes `divergence-attestation` substrate row submitted as separate kind. Both refuse silent `--no-divergence-check` flags.

**C-5 — §9 prose deletion required if substrate-side gate ships.** [P-1, migration_path]; [P-2, migration_path] — 2-of-4 explicit on no-coexistence per DV-S109-1 ceremony-subtraction reading. The §9 instruction (`run export --write before commit`) becomes redundant when substrate enforces it.

## Divergence

**D-1 — Ship-now (P-1 + P-2) vs defer-until-recurrence (P-3 + P-4).** [P-1, position]; [P-2, position]; [P-3, position]; [P-4, position] — 2-of-4 ship the substrate-receipt gate now citing DV-S176-1 lesson plus cross-family signal plus close-path asymmetry (one refusal cheap, stale-on-commit cross-time-multi-machine). 2-of-4 defer citing zero recurrence S187-S189 plus DV-S109-1 ceremony-subtraction plus transactional-coupling architectural smell. Same evidence base reaches opposite ship-decisions on graduation timing.

**D-2 — Within defer: P-3 ship-nothing vs P-4 validate.sh extension.** [P-3, position]; [P-4, position] — sub-divergence on whether the smaller-mechanism intermediate (validate.sh + pytest) is itself ceremony or is the right next step. P-3 argues the existing validate.sh + zero recurrence is sufficient; P-4 argues a 20-line bash extension validating sha256 reconciliation is the smallest-mechanism payment that closes FR-S187-16 + FR-S188-15.

## Minority

**M-1 — P-3 ship-nothing-anything position.** Preserved as minority. Strongest insights: (a) the substrate (transactional, single-process, ACID) and the filesystem (concurrent, append-only, multi-machine) live on different sides of an authority boundary; the receipt-pattern crosses that boundary in the export-write step which inherits the same coupling; (b) marginal capability gain of substrate-receipt over validate.sh approximately zero on observed evidence; (c) cross-machine workflow + EF-S185-2-style concurrent-process race produces real false positives on a substrate-side gate. Reopen condition: a documented stale-L5-on-commit calibration-EF would invalidate the ship-nothing position.

## [synth] — synthesis-original observations

**[synth] The cross-family signal weights toward ship-eventually, but the smaller-mechanism intermediate honors all four positions.** P-2 codex independently arrived at substrate-receipt gate (narrow scope, L5-only, divergence-attestation cheap-exit, §9 prose delete) — that is a meaningful cross-family signal because the codex prompt biased neither toward nor away from ship. P-1 anthropic architect convergence with P-2 codex on the receipt-pattern shape is therefore stronger than two same-family architect votes would be. However, P-3 + P-4 transactional-coupling concerns are real and the receipt-pattern does not fully resolve them (export still touches filesystem; the receipt is substrate-canonical but the projection is not). The two-step graduation (validate.sh first, substrate-receipt as graduation target) honors P-1 + P-2 architecture-correctness AND P-3 + P-4 incremental-mechanism preference.

**[synth] Receipt-pattern resolves P-3 + P-4 atomicity concerns within the close-handler.** P-3 + P-4 framed atomicity concerns against handler-side filesystem walks; the receipt-pattern decouples this — export touches filesystem and writes a substrate receipt, the close-handler reads only substrate. The handler does not become non-transactional. This is a structural answer to the atomicity critique that P-3 + P-4 did not directly engage because the brief enumerated handler-walk and receipt-pattern as parallel options rather than naming receipt-pattern as the atomicity-fix variant of handler-side placement.

**[synth] kind=spec_only locks all three ship-something paths.** validate.sh extension (bash), substrate-receipt gate (migration + handler dispatch), and any spec-version body edit referencing concrete enforcement all require coding-kind work. The decision-record output of D-B can therefore seal the design and route the implementation to follow-up FRs without compromising the synthesis.

## Counterfactual disposition

C-B1 (counterfactual_id=5): ship substrate-receipt gate directly without validate.sh intermediate per P-1+P-2 cross-family convergence — addressed-in-synthesis. The synthesis preserves the substrate-receipt design as graduation target (honoring DV-S176-1 lesson) but routes through validate.sh-first because P-3+P-4 transactional-coupling and cross-machine concerns warrant a smaller-mechanism intermediate that can measure divergence pressure (validate.sh produces non-zero stale-file warnings → substrate-receipt graduation pressure becomes substrate-detectable). The intermediate is not ceremony; it is the measurement step that converts the 2-2 D-1 split into evidence-anchored graduation timing.

## Decision feed

The synthesis recommends:
1. Defer FR-S187-16 + FR-S188-15 by-mechanism via the sealed two-step design (validate.sh smaller-first, substrate-receipt as graduation target).
2. Author follow-up FRs anchoring the implementation work: (FR-D) coding-kind FR shipping P-4's `tools/validate.sh` extension — sha256 reconciliation block walking `provenance/<wno>-<slug>/0[5-9]-*.md` against `export_manifest` rows + pytest case asserting non-zero exit on injected divergence; (FR-E) coding-kind FR shipping P-1+P-2 substrate-receipt gate per sealed design when graduation triggers — `close_export_receipts` row written by export carrying `projected_set_sha256`, `_submit_session_close` refuses absent-or-stale receipt with `E_REFUSAL_TNN`, divergence-attestation row mirrors DV-S180-1 nil_attestation, §9 prose deleted on ship.
3. Graduation-trigger calibration: re-open the substrate-receipt graduation FR when (a) FR-D ships and `tools/validate.sh` surfaces non-zero stale-L5-on-commit warnings across N closes, OR (b) a calibration-EF names a stale-L5-on-commit landing despite validate.sh, OR (c) cross-machine workflow surfaces a divergence shape validate.sh cannot detect.
4. Preserve M-1 minority for reopen if architectural-coupling concerns prove dominant on implementation evidence (e.g. validate.sh extension itself produces false-positive ceremony in cross-machine workflow without catching real divergence).

### Synthesis points

- **convergence C-1.** SQL trigger structurally cannot read filesystem; gate placement must be Python (handler / export precondition / operator-side bash). 4-of-4 agree.
- **convergence C-2.** export_manifest sha256 + L5_FILENAMES already provide divergence-detection data; question is which placement queries it.
- **convergence C-3.** Receipt-pattern (T-32 model) is the architecture if substrate-side ships; export writes receipt-row, close-handler reads.
- **convergence C-4.** Divergence-attestation cheap-exit (mirror DV-S180-1 nil_attestation) is the right shape; no silent --no-divergence-check flags.
- **convergence C-5.** Section 9 prose deletion required if substrate-side gate ships; no coexistence per DV-S109-1 ceremony-subtraction.
- **divergence D-1.** Ship-now (P-1+P-2) vs defer-until-recurrence (P-3+P-4); same evidence base reaches opposite ship-decisions on graduation timing.
- **divergence D-2.** Within defer cluster: P-3 ship-nothing-anything vs P-4 validate.sh-extension as smallest-mechanism intermediate.
- **minority M-1.** P-3 ship-nothing position; transactional-coupling smell, cross-machine race, marginal-gain-zero over validate.sh; reopen on documented stale-L5-on-commit calibration-EF.
