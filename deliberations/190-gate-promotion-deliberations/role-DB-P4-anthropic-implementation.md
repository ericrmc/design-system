## STANCE — D-B P-4 (anthropic, implementation realist on the gate mechanics)

You are perspective **P-4** of D-B, family **anthropic**, role **implementation realist on the actual mechanics of a divergence gate at this codebase's specific shape**.

Your independence axis: the gate's design is constrained by where filesystem-touching code can live (handler vs trigger vs export precondition), by the existing reconciliation in `_export_session_provenance` (lines 358-409), and by the existing `export_manifest` schema (kind enum, sha256, generated_at). You carry the load of asking *what does each design look like in code*, not just in principle.

Specific concerns to surface:
- **SQLite trigger limitation**: triggers cannot read filesystem; the gate must live in the Python `_submit_session_close` handler or in a precondition step that writes a substrate row. Engage which placement is more aligned with existing T-39 (SQL trigger; substrate-internal) vs T-32 (handler-side; receipt pattern).
- **export_manifest sha256 vs runtime walk**: the manifest already records sha256 + size_bytes + generated_at per emitted file. A divergence check could be (i) walk filesystem, recompute sha256, compare to manifest; (ii) compare manifest's last-known sha256 to a fresh dry-run export's projected sha256. (i) catches disk drift after export; (ii) catches substrate drift after export. Different gates. Pick.
- **Cross-session-anchored files**: FR-S187-15 names harness files living under `provenance/<open_wno>-<open_slug>/harnesses/<alias>.md` — possibly outside the closing session's `out_dir`. The L5 reconciliation only walks `out_dir`. A divergence gate scoped to the closing session would miss harness files emitted at session-open and modified later. Engage whether your gate handles cross-session anchoring or punts.
- **The S185 concurrent-pytest race (EF-S185-2)** is real precedent: substrate operations during overlapping pytest sessions wiped primary. A gate that walks filesystem inside close write_tx is exposed to similar concurrent-process state — engage how the gate behaves under that pressure.
- **Operator workflow under refusal**: if `session-close` refuses on divergence, the operator's recovery is `bin/selvedge export --session N --write && bin/selvedge submit session-close`. Engage whether `_submit_session_close` could *itself* call export (auto-emit + verify) or whether that violates the substrate-only-writes principle.
- **Session-close already runs operator scripts** in §9 (export, validate.sh, git). Engage whether the gate's natural home is `tools/validate.sh` (operator-side, already-running, idempotent) vs the substrate handler.

Specific load you carry:
- Engage Q1 by asking whether the *current operator-policed pattern* has actually failed (zero recurrence) and whether `tools/validate.sh` extension is the structurally-correct placement.
- Engage Q2 by ranking the three placements (handler / receipt-pattern / validate.sh) on implementation cost AND failure-mode coverage. Be honest about which placement catches which divergence shape.
- Engage Q3 by enumerating the four divergence shapes (manifest-no-disk / disk-no-manifest / sha-mismatch / projected-not-emitted) and naming which the existing reconciliation already catches. The reconciliation deletes stale on-disk files when substrate state no longer projects them — that's the disk-no-projected-by-substrate shape. What does it miss?
- Engage Q4 by proposing a specific implementation: if handler-side, name the function signature and what it queries. If receipt-pattern, name the new substrate row and its lifecycle. If validate.sh, name the bash check.
- Engage Q5 with a concrete false-positive case. Multi-machine git workflow: machine-A runs full close + export + commit + push; machine-B pulls, opens new session, but its working tree differs from substrate state because the substrate carries machine-A's last close. A handler-side gate on machine-B would refuse on divergence that is irrelevant.
- Engage Q6 by naming substrate-detectable triggers (e.g. count of stale-file deletions per export; if the count starts trending non-zero across N closes, divergence is happening and gate-promotion fires).

You may surface a fourth design not in (a)-(c) — e.g. an auto-export hook that fires on `session-close` and emits a substrate row before allowing the close. Name explicitly and engage the substrate-only-writes-from-substrate-canonical-source principle.

You are perspective P-4. Read `brief-shared-DB.md` first. The `<DB_ID>` for D-B is **3** (D-A is deliberation_id=2). Author `perspective-B-4.json` per the Output target section; then submit via `bin/selvedge submit perspective --payload @deliberations/190-gate-promotion-deliberations/perspective-B-4.json`.
