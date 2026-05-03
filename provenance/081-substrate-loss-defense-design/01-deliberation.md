---
session: 081
title: substrate-loss-defense-design — deliberation
generated_by: selvedge export
---

# Deliberation

## D-1 — Substrate-loss defense design — L1 init refusal, L2 subagent isolation, L3 snapshot mechanism, L4 reconstruction scope; ship as one engine-v51 arc.

sealed_at: 2026-05-03T00:23:11.536Z

### P-1 (anthropic)

**Position.** Ship L1a+L1b+L2a+L3(all-triggers)+L4B as engine-v51 single arc; S180 proves single-layer bypassable, defense-in-depth is the only correct response when substrate-loss is terminal.

**schema_sketch.**
- New table snapshots(id INTEGER PK, created_utc TEXT, engine_version INTEGER, trigger TEXT, path TEXT, size_bytes INTEGER, source_session_no INTEGER, sha256 TEXT)
- Trigger enum constrained to {session_open, migrate_apply, init_refused, init_forced, write_tx} with CHECK clause matching engine constants
- New table substrate_guards(id PK, guard_name TEXT UNIQUE, enabled INTEGER, last_tripped_utc TEXT, trip_count INTEGER) seeded with init_force_guard, migrate_apply_guard, readonly_subagent_guard
- Add init_session_offset INTEGER column to workspace_meta (or equivalent) so live-substrate predicate count(sessions WHERE workspace_session_no > init_session_offset) > 0 is durable across re-inits
- Snapshot retention metadata: keep_reason TEXT in snapshots (count_window / time_window / per_version_anchor / trigger_anchor) so prune logic is auditable not heuristic
- Add engine_version_marker row to schema_versions or equivalent capturing v50->v51 bump with migration_id pointer
- decision_effects.target_descriptor extension: substrate_guard:<name> as new typed prefix so guard trips/configures route through standard effects pipeline
- review_findings.finding_kind extension: substrate_guard_bypass as audit category so any --really-force usage is a first-class finding not a log line
**cli_surface.**
- bin/selvedge init --force refuses with exit 2 when live-substrate predicate true; error message names guard, names escape hatch, names snapshot path written before refusal
- bin/selvedge init --really-force required to bypass L1a; additionally requires SELVEDGE_CONFIRM_DESTROY=1 env var present (two-factor); writes snapshot trigger=init_forced before destroy
- bin/selvedge migrate --apply refuses with exit 2 when live-substrate predicate true and any pending migration is non-additive; --really-apply bypass; snapshot trigger=migrate_apply always
- All subagent spawns set SELVEDGE_READONLY=1 in environ; selvedge runtime opens DB with file:state/selvedge.sqlite?mode=ro&immutable=0 URI when env var set; BEGIN raises typed E_SUBSTRATE_READONLY
- bin/selvedge snapshots list/prune/restore subcommands; restore is itself gated by live-substrate predicate plus --really-restore
- bin/selvedge guard list/disable/enable subcommands operating on substrate_guards table; disable requires SELVEDGE_CONFIRM_DESTROY=1
- bin/selvedge legacy-summary emit one-shot extractor writing legacy-substrate-summary.md from a named snapshot path (L4B); pure read, no substrate writes
**migration_path.**
- Migration 033 creates snapshots + substrate_guards tables, seeds three guards enabled=1, adds init_session_offset column with default = current max(workspace_session_no)
- Migration 034 backfills one snapshot at trigger=migrate_apply for the running substrate so retention has an anchor before first prune ever runs
- Engine version bumps v50 -> v51 in code AND doc-marker; not doc-only — the substrate_guards CHECK constraint and SELVEDGE_READONLY enforcement are runtime behavior changes that need version coupling for review-pass replay
- All write_tx call sites wrapped to fire snapshot(trigger=write_tx) under retention policy; existing write_tx surface is small enough that the wrap is mechanical
- selvedge/init_cmd.py + selvedge/migrate_cmd.py + selvedge/runtime/conn.py are the three code surfaces; subagent harness in selvedge/harness.py sets the env var
- L4B legacy-summary tool ships in same arc but is invoked manually post-merge; output committed at provenance/legacy-substrate-summary.md once and never regenerated
- Pytest additions: test_init_force_refuses_with_live_substrate, test_really_force_requires_env, test_subagent_readonly_blocks_begin, test_snapshot_on_each_trigger, test_retention_prune_respects_anchors
**what_not.**
- Do not ship L1c filesystem read-only — too coarse, breaks legitimate session-window writes, OS-dependent, fights the substrate rather than guards it
- Do not ship L2b tempdir clone — admits CLI ops we explicitly want refused (the whole point is subagents cannot mutate); ergonomics win is illusory
- Do not ship L2c operator-managed alternate path — worst ergonomics, requires operator action per spawn, fails closed only when operator remembers
- Do not ship L4C faithful replay — multi-session migration-step-advance is its own substrate-risk surface and S180 framing makes the cost unjustified
- Do not ship L4A skip-entirely — leaves DV-alias-index and open-issue list as tacit knowledge; L4B one-shot is cheap insurance
- Do not gate snapshots behind a config flag — defaults must be conservative-on, opt-out via guard disable not opt-in
- Do not collapse L1a and L1b into one guard — different urgency, different bypass semantics, separate audit trails
**open_question.**
- Snapshot directory state/snapshots/ inside or outside the workspace git boundary — inside means commits balloon, outside means snapshots lost on workspace clone
- Whether write_tx snapshot trigger should be every-tx or every-Nth-tx with N tunable in substrate_guards row (perf vs granularity)
- Whether SELVEDGE_READONLY should also block read paths that rely on temp-table creation (some validators do CREATE TEMP TABLE) and how to whitelist
- Restore semantics — does restore replace state/selvedge.sqlite atomically and snapshot the pre-restore state as trigger=restore_displaced
- Engine-v51 marker placement: schema_versions table vs separate engine_versions table; current substrate has neither named explicitly in recent commits
**risk.**
- SELVEDGE_READONLY env var leaks into non-subagent shells if operator sources a script that set it; mitigation: harness unsets on subagent exit, but parent shell pollution still possible
- Snapshot-on-every-write_tx may 10x state/ disk usage; retention policy critical, prune must run inline not deferred
- substrate_guards table itself becomes a substrate-loss target — guard-disable then init --force is a two-step bypass; partial mitigation via SELVEDGE_CONFIRM_DESTROY two-factor on disable
- Migration 033 adding CHECK constraint on trigger enum will reject any future trigger string not in the enum — forces migration discipline (this is intended but worth naming)
- L4B extractor reads legacy substrate which is a .pre-migrate-backup file — schema version mismatch may break the extractor; ship extractor pinned to engine-v50 read path
- Two-factor (--really-force + env var) increases friction for legitimate test-harness re-init; test fixtures must set env var explicitly which is verbose but auditable
**what_lost.**
- Speed of subagent iteration when subagent legitimately needs a scratch write (e.g. exploratory submit --dry-run that internally BEGINs); workaround is L2b clone but we rejected it
- Operator ergonomics on intentional re-init during early-arc bootstrap; two-factor friction is real and non-trivial
- Disk footprint discipline — snapshot dir grows monotonically until retention prune fires; operators who skip retention config will accumulate
- Single-command init flow — every destructive op now requires a confirmation step, no more one-liner re-init
- The trust-the-subagent stance — explicit shift to subagents-are-read-only-by-default is a cultural change with cost beyond the code diff
- Some legitimate migrate --apply flows on live substrate now require --really-apply; additive migrations will feel over-gated until operators internalize the predicate

### P-2 (openai)

**Position.** Treat this as write-capability containment plus tested recovery, not a subagent etiquette bug; choose L2b, snapshots at boundaries, L4B, and split engine-version from marker.

**schema_sketch.**
- Add snapshot_catalog(id, path, utc_ts, engine_version, trigger, sha256, source_db_sha256, sqlite_page_count).
- Add recovery_test_log(id, snapshot_id, utc_ts, restore_ok, integrity_check_ok, row_counts_json, cli_version).
- Add close_export_manifest(session_no, utc_ts, export_path, required_artifacts_json, artifact_shas_json).
- Add engine_marker(kind, value, utc_ts, reason), where kind separates schema_version, engine_version, and doc_marker.
- Do not encode recovery policy only in filenames; state/snapshots metadata must be queryable after partial filesystem loss.
- L5 mandatory artifacts should have stable names under exports/SNNN/, not prose-only sections hidden in 03-close.md.
**cli_surface.**
- Pick L2b: spawn subagents with a tempdir clone of state/ so all CLI commands run normally without touching primary substrate.
- Keep SELVEDGE_READONLY=1 as advisory defense only; env vars are memory, not an isolation boundary.
- Add bin/selvedge restore --from state/snapshots/X.sqlite --to state/selvedge.sqlite --verify before snapshots become credible.
- Add bin/selvedge snapshot --trigger manual and use sqlite3.Connection.backup(), never cp of a live database.
- Replace dry-run write_tx rollback validation with bin/selvedge submit --validate-only on a forked DB.
- L1a should land in selvedge/init_cmd.py: refuse --force if sessions.workspace_session_no > init_session_offset exists.
- L1b should mirror this for migrate --apply, but require fewer blockers than init because migration is expected maintenance.
- L2c is an operator convenience path, not a security design; humans will point it at primary during pressure.
**migration_path.**
- Ship engine-v51 as a resilience migration only if it creates marker separation, snapshot_catalog, and recovery_test_log.
- If no schema or CLI behavior changes ship, call it doc-marker-2026-05-03, not engine-v51.
- Migration order: add L1a guard first, then L2b spawn cloning, then snapshot_catalog plus restore CLI, then L5 exports.
- Backfill snapshot_catalog only for new snapshots; do not pretend missing S001-S180 history was protected.
- L4 stance is B: produce legacy-substrate-summary.md with high-signal recovered summaries, not faithful replay.
- C needs migration-step-advance and creates false confidence; A discards lessons that can cheaply shape future tests.
- First recovery drill should restore a snapshot to tempdir and run export for the latest session before marking OI-S180-1 closed.
**what_not.**
- Do not rely on SELVEDGE_READONLY=1 as the main control; the failure class is any caller with write capability doing the wrong thing.
- Do not snapshot every write_tx by default; it creates backup spam and hides the need for meaningful recovery points.
- Do not stop at session-open snapshots; mid-session corruption needs a later checkpoint such as deliberation-seal or close.
- Do not make --really-force easy to cargo-cult; require SELVEDGE_REALLY_FORCE=substrate-loss-accepted plus an explicit flag.
- Do not treat markdown export as archival if it excludes open issues, spec_versions, and receipts needed to rebuild decisions.
- Do not call a restore path done until PR or CI exercises restore --from against a real generated snapshot.
- Do not let anthropic-style consensus undervalue operational testability; backups without restore drills are decorative.
**open_question.**
- Should close-time snapshot trigger be deliberation-seal, session-close, or both when those are distinct transaction points?
- What exact table records subagent spawn roots, so L2b can prove a destructive command ran only against a clone?
- Should init --force refusal count any sessions row, or only sessions.workspace_session_no > init_session_offset?
- Where should restored DBs land by default: state/selvedge.sqlite or state/restored/<snapshot-id>/selvedge.sqlite?
- What is the canonical close export root: state/exports/SNNN/ or docs/sessions/SNNN/?
- Should restore --to primary require the same two-key ceremony as init --really-force?
- Does reference_harness state have enough stable schema to export as markdown, or should it be JSON plus a markdown index?
**risk.**
- L2b can diverge from primary substrate if clone creation misses WAL or sidecar files; implement via SQLite backup API, not file copy.
- L1 app-side checks do not protect direct sqlite writes; acceptable only if CLI is the supported mutation surface.
- Snapshot retention can delete the only good pre-corruption copy if it is pure count-based.
- Use count plus age: keep last 20, all pre-migrate/init snapshots, and one close snapshot per engine_version for 90 days.
- Restore tooling can become destructive; default restore target should be a tempdir unless --to-primary is explicit.
- Mandatory exports increase close latency, so export_manifest must record partial failures and block close only for required artifacts.
- Anthropic perspectives may overfocus on reconstructing S179 and underweight preventing the next live-writer mistake.
**what_lost.**
- Make open-issues snapshot mandatory at close: issue id, severity, status, owner/session, blocking refs, and latest disposition.
- Make spec_versions index mandatory: version, title, body_sha256, created_session, supersedes, and current/retired status.
- Make engine_feedback ledger mandatory because it captures operator intent that decision rows often compress away.
- Make deliberation_counterfactuals mandatory; v50 made them decision-relevant, so loss weakens replay reasoning.
- Make forward_reference_dispositions mandatory because they explain why unresolved references were accepted or closed.
- Make decision_prechecks receipts mandatory; they are compact proof that gates ran before decisions were sealed.
- Make decision_chain_walks receipts mandatory when present, but allow an empty artifact with manifest status.
- Keep reference_harness state mandatory as machine-readable JSON plus markdown summary; harness state is too structured for prose only.

### P-3 (anthropic)

**Position.** Ship L1a plus a subagent prompt clause; refuse L2 code, L3, L4, and version bumps; S180 is one bug with a one-line fix and operator-stated non-critical loss.

**schema_sketch.**
- No new tables, no snapshots manifest, no retention metadata; the substrate stays exactly the shape it is post-S180 genesis.
- init_session_offset already exists on workspace; reuse it as the live-data sentinel rather than inventing a new column.
- If a guard counter is needed, derive it at query time from sessions table; do not denormalize into a guard_state row.
- Reject any schema_migration that exists solely to mark defense shipped; markers without code are decoration.
- Snapshots, if ever added, belong on the filesystem with no DB-side index; the OS already lists files.
- L4 reconstruction needs zero schema because L4 is not happening.
**cli_surface.**
- bin/selvedge init --force refuses when count(sessions WHERE workspace_session_no > init_session_offset) > 0; exit non-zero with message naming the count.
- Escape hatch is --really-force flag only; no env var, because env vars get exported in shell rc files and become routine.
- migrate --apply gets no new guard; migration is additive and the threat model does not include it (L1b rejected).
- No SELVEDGE_READONLY env var; subagent isolation is a PROMPT.md clause subagents must not invoke init/migrate/destructive bin commands; cheaper, auditable, sufficient.
- No snapshot subcommand, no restore subcommand, no list-snapshots; zero new CLI surface beyond the one --really-force flag.
- L2c alternate-workspace-path is rejected as worst-ergonomics-for-zero-marginal-safety over the prompt clause.
**migration_path.**
- No migration. Engine version stays v50. A doc-only v51 bump to mark the defense is exactly the ceremony to refuse.
- The L1a guard is a 5-10 line app-side check in selvedge/init_cmd.py with a unit test asserting refusal-with-live-sessions and pass-with-empty.
- The PROMPT.md amendment is one bullet under existing subagent-discipline section; no new doc file.
- No snapshot directory created at install time; nothing to migrate, nothing to clean up later when this defense is revisited.
- Operator-deferred call 5 (engine-v51 marker): reject both variants; the code change is small enough to live in commit message provenance.
**what_not.**
- Do NOT ship L3 snapshots in any trigger combination; non-critical data times near-zero realized recovery value equals manufactured complexity.
- Do NOT ship L4 reconstruction in any of A/B/C shapes; A is correct framing, B is a one-shot script not engine code, C is multi-session waste.
- Do NOT ship L2a readonly-DB code path; subagents that need writes will work around it via --really-force-equivalent escape and the guard rots.
- Do NOT ship L2b tempdir clone; per-spawn copy of state/ is disk churn and a coherence bug surface for zero incident-aligned benefit.
- Do NOT ship L1b migrate guard or L1c filesystem-readonly; both expand surface beyond the actual S180 failure mode.
- Do NOT bump engine version for a guard; version bumps are for substrate-shape changes that consumers must adapt to.
- Do NOT add retention policy machinery for snapshots that do not exist.
**open_question.**
- What is the actual subagent threat surface beyond init --force, are there other bin commands warranting the same one-line guard pattern preemptively?
- Does the --really-force flag need a confirmation prompt, or is the explicit flag itself sufficient friction given operator-only audience?
- Should the PROMPT.md clause enumerate forbidden commands by name, or state a principle and trust subagent comprehension?
- If a future incident reveals that prompt-clause isolation is insufficient, what is the trip-wire that promotes L2a from rejected to shipped?
**risk.**
- Guard fires on legitimate re-init scenarios (corrupted substrate, intentional reset) and operator learns to type --really-force reflexively, defeating the guard.
- PROMPT.md clause is ignored by future subagent prompts that do not inherit it; mitigation is the L1a guard catching it anyway, which is why L1a is the load-bearing piece.
- Minimalist package leaves zero recovery option if a different destructive op (not init) wipes substrate later; accepted because operator framed data as non-critical.
- Refusing snapshots now means a future we should have had snapshots incident has no fallback; accepted as the cost of refusing speculative defense.
**what_lost.**
- No point-in-time recovery for any future incident; rebuilding from git history of state/ is the only fallback.
- No defense-in-depth: a single bug in the L1a check (off-by-one on init_session_offset, missing flag plumbing) is total defense failure.
- No protection against destructive ops that are not init --force; the next novel destructive path is undefended until it fires.
- No reconstruction artefact summarising pre-S180 substrate; the S001-S179 deliberation history exists only in git log and SESSION-LOG.md narrative.
- No snapshot to diff against when investigating future did the substrate change unexpectedly questions.
- L5 close-time export expansion deferred indefinitely; if substrate is wiped again, recoverable surface is exactly what was exported pre-S181.

### P-4 (anthropic)

**Position.** Defenses must ship with named documented ergonomic escape hatches; default permissive with opt-in strict mode; L2a breaks reviewer dry-run and must not be the only isolation primitive.

**schema_sketch.**
- Snapshot table state/snapshots/<utc-ts>-<engine-version>-<trigger>.sqlite with sidecar JSON naming trigger + session_no + caller_kind for forensic replay.
- Add init_session_offset column already implied; expose via SELECT for app-side L1a guard so refusal predicate is one query not a join.
- Caller-kind enum (operator/subagent/hook/cron) propagated via SELVEDGE_CALLER env so defenses can branch on caller without sniffing tty.
- Snapshot retention metadata (count, age, engine_version) stored alongside files so prune logic is declarative not stat-based.
- Strict-mode flag SELVEDGE_STRICT=1 is the single switch that escalates default-warn defenses to default-refuse across L1+L2.
**cli_surface.**
- L1a: init --force refuses on non-empty live substrate; escape hatch --really-force AND SELVEDGE_INIT_REALLY_FORCE=1 (belt+suspenders, both must be present in subagent contexts).
- L1a refusal message must name the snapshot path written immediately before refusal so operator can recover without reading docs.
- L1b: migrate --apply warns but does not refuse; --apply --on-live acknowledges; subagents inherit refuse-by-default via SELVEDGE_CALLER=subagent.
- L2 choice: ship L2b (tempdir clone) as default subagent isolation; L2a available as SELVEDGE_READONLY=1 opt-in for read-only review tasks that do not need dry-run.
- L2c rejected: operator-managed alternate workspace path is the status quo that failed at S180; do not re-ship as primary.
- Snapshot CLI: bin/selvedge snapshot create/list/restore/prune as first-class verbs, not buried under admin/.
- Restore is interactive by default and requires --confirm <snapshot-id> matching listed id to prevent fat-finger.
- All refusal paths exit 2 (distinct from generic error 1) so wrappers can branch on defense-triggered-refusal vs real failure.
**migration_path.**
- engine-v51 marker bump IS warranted: schema-adjacent (init_session_offset semantics + snapshot trigger surface) plus operator-visible CLI changes meet the bar; doc-only would understate the contract shift.
- Migration 033 adds snapshot table + init_session_offset read path; ships behind feature flag SELVEDGE_DEFENSES=1 for one session before becoming default.
- L1a guard ships first and alone in S181; L2b + L3 + L4 follow in S182+ to bound blast radius of the defense rollout itself.
- L4 scope: ship B (one-shot extractor to legacy-substrate-summary.md); A loses provenance, C is multi-session work that delays L1a indefinitely.
- L4-B extractor runs once against pre-S180 backup files in state/, produces markdown, commits to provenance/, then is deleted from codebase to prevent reuse drift.
**what_not.**
- Do NOT make L2a the only isolation: it silently breaks reviewer subagents that legitimately validate migrations via dry-run BEGIN/ROLLBACK.
- Do NOT snapshot on every write_tx: dominates latency, fills disk, trains operator to disable defenses wholesale.
- Do NOT ship L1c (filesystem read-only): too heavy, breaks legitimate operator ad-hoc queries, requires sudo on macOS, escape hatch is ugly.
- Do NOT couple snapshot retention to engine-version alone: a chatty session can produce 50 snapshots at one version and starve older versions.
- Do NOT ship defenses without a single-command recovery path tested in CI; undocumented recovery is no recovery.
- Do NOT use --force as the override for --force; --really-force is the convention but document the asymmetry explicitly in --help.
**open_question.**
- Does L2b tempdir clone need to copy WAL+SHM atomically or can it use SQLite backup API? Latter is correct but adds dependency on conn lifecycle in subagent spawn path.
- For L3 triggers: is session-open (i) sufficient given session-close already commits, or do we need session-open AND migrate-apply (i+ii) as the minimum viable set?
- Should --really-force require typing the workspace name as confirmation token (rm -rf style) or is env-var-plus-flag friction enough?
- How does L1a behave during legitimate fresh-clone bootstrap where init IS the right call? Predicate count(sessions)>0 handles it but verify edge case of partial-init crash recovery.
- Does SELVEDGE_CALLER=subagent get spoofed trivially, and does that matter given the threat model is accident not adversary?
**risk.**
- L1a + L2b + L3-on-session-open is the minimum that defends without operator burden; anything more risks override-by-default culture where defenses become noise.
- Snapshot disk growth: cap at last-20-count + last-7-days union, prune on session-close, surface size in selvedge status to keep operator aware.
- L2b tempdir clone may mask race conditions present in shared-substrate access; document that subagents see point-in-time view not live.
- Recovery ergonomics gap: if restore requires manual file copy, operators will skip snapshots entirely; restore must be one command with confirmation.
- Defense-rollout itself is risky: ship L1a alone in S181, observe one session of friction, then layer L2+L3 in S182 to avoid compound regression.
- --really-force normalization: if reviewer subagents routinely pass it, the defense degrades to ceremony; gate subagent escape via separate SELVEDGE_SUBAGENT_DESTRUCTIVE=1 distinct from operator --really-force.
**what_lost.**
- L2a-only isolation loses reviewer dry-run validation capability, which is exactly the audit pattern S177-S180 relied on for substrate-correctness.
- L4-A (skip reconstruction) loses the DV alias index and open-issue continuity that downstream sessions cite by ID; B preserves the citations cheaply.
- Snapshot-on-every-write-tx loses session-latency budget and trains operators to disable defenses; the marginal recovery point is not worth the steady cost.
- Doc-only engine marker loses the operator signal that CLI surface changed; bumping to v51 is the cheap honest move.
- Strict-mode-as-default loses the testing workflow where operators legitimately destroy state to provoke errors, which is the explicit operator framing at S180.

### Synthesis points

- **convergence C-1.** All four perspectives converge on L1a (init --force refusal when live substrate exists) as the load-bearing minimum defense.
- **convergence C-2.** P-1, P-2, P-4 converge on shipping L4B one-shot extractor to legacy-substrate-summary.md preserving DV alias index and open-issue continuity.
- **convergence C-3.** P-1, P-2, P-4 converge on shipping snapshot machinery via SQLite Connection.backup() API rather than file-copy of WAL-journaled DB.
- **convergence C-4.** P-2 + P-4 converge: restore CLI is mandatory alongside snapshots; backups without single-command tested restore are decorative.
- **convergence C-5.** All four perspectives reject L1c (filesystem read-only on state/selvedge.sqlite) as too coarse and OS-dependent.
- **convergence C-6.** All four perspectives reject L2c (operator-managed alternate workspace path) as primary defense; status-quo that already failed at S180.
- **convergence C-7.** P-2 + P-4 converge against snapshot-on-every-write_tx; latency dominator and operator-fatigue trainer; bounded triggers required.
- **convergence C-8.** P-2 explicit + P-4 implicit + operator mid-deliberation: L5 close-time export expansion is mandatory (open-issues, spec_versions index, EF ledger, counterfactuals, FR dispositions, prechecks, chain-walks, harness state).
- **convergence C-9.** P-1 + P-2 + P-4 converge: threat model is write-capability-containment broadly, not specifically subagent-runs-init; env-var defenses alone are insufficient.
- **divergence D-1.** L2 subagent-isolation shape: P-1 says L2a (RO env var) only; P-2 says L2b (tempdir clone) only; P-4 says L2b default + L2a opt-in; P-3 says no L2 code.
- **divergence D-2.** L3 trigger set: P-1 every-trigger including write_tx; P-2 boundaries (deliberation-seal/session-close/migrate/init); P-4 session-open+migrate minimum; P-3 none.
- **divergence D-3.** Migration marker: P-1 + P-4 say engine-v51 warranted (real CLI/schema changes); P-2 conditional (only if real schema ships); P-3 rejects any version bump.
- **minority M-1.** P-3 minimalist position: defenses-in-depth themselves rot via override-routinization; ship only L1a + PROMPT.md clause; preserved as carried-forward warning.
- **minority M-2.** P-1 every-write_tx snapshot extreme: preserved as the if-disk-is-cheap-and-operator-never-disables maximalist endpoint of the L3 trigger spectrum.
- **minority M-3.** P-4 phased-rollout-across-S181-S182: ship L1a alone in S181, observe friction, layer L2+L3 in S182; rejected in favor of single-arc but preserved as risk-management option.
