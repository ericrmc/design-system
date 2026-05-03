## STANCE — D-B P-1 (anthropic, architect — propose the strongest substrate-side gate)

You are perspective **P-1** of D-B, family **anthropic**, role **architect proposing the strongest available substrate-side divergence gate**.

You carry the load of *arguing that the gate ships now*. The DV-S176-1 lesson — "when discipline depends on the agent reaching for a tool the substrate could dispatch automatically, ship the substrate dispatch" — is your strongest precedent. The §9 prose instruction (`session-close` → `export --write` → `commit`) is the same prose-and-discipline shape that DV-S176-1 named as ceremony without instrumentation. The export_manifest table shipped at S188 is the data structure a gate would query; the materials are in place.

Your strongest argument: the close-path is asymmetric. A substrate that refuses session-close on divergence is a one-time refusal with a cheap recovery (run `bin/selvedge export --session N --write` then re-attempt close). A close-without-export commits stale markdown to git history; that's a multi-machine cross-time artefact that other tools (`bin/selvedge orient`, future re-rebuilds, audit-readers) read as canonical. The cost-asymmetry favours catching divergence at the substrate boundary.

Your second strongest argument: the gate has natural placement. T-39 already refuses session-close on missing close_records (engine-v41). The substrate-side close-path gate is the precedent. A new T-NN refusing on divergence (handler-side; SQL triggers can't read filesystem) extends T-39's discipline.

Specific load you carry:
- Pick **one** primary placement (handler-side filesystem walk vs receipt-pattern via export precondition) and defend concretely. Engage T-32 receipt-pattern (markdown is presentation, row + sha256 is proof) — does it apply here?
- Q3: name *which* divergence shapes the gate refuses on. The four options (manifest-but-no-disk, disk-but-no-manifest, sha mismatch, projected-but-not-emitted) have different cost profiles. Pick deliberately.
- Q3 cheap-exit: propose a substrate-detectable cheap-exit (e.g. an attestation row written by `bin/selvedge export --no-divergence-check` for cross-machine workflows). Mirror DV-S180-1 nil_attestation pattern.
- Q4: name the byte-identical clauses to delete from `prompts/development.md` §9 if the gate ships. Net coherence-gain requires removal, not coexistence.
- Q6: name the *exact* withdrawal-trigger calibration-EF shape (substrate-detectable preferred). Engage P-3's likely "zero recurrence" critique directly.
- Q5: engage cross-machine workflows honestly. The substrate is per-workspace per orient packet, but git history carries provenance markdown across machines; a per-machine gate may produce false positives on machines that did not run the export.

You may NOT yield to "we should wait for recurrence." The architecture-level argument is that the close-path *should* be substrate-canonical regardless of recurrence pressure, by symmetry with T-39 + DV-S176-1. Argue that.

You are perspective P-1. Read `brief-shared-DB.md` first. The `<DB_ID>` for D-B is **3** (verified — D-A is deliberation_id=2). Author `perspective-B-1.json` per the Output target section; then submit via `bin/selvedge submit perspective --payload @deliberations/190-gate-promotion-deliberations/perspective-B-1.json`.
