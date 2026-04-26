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

# Session from which the read-contract is enforced (D-084, Session 022).
# Check 20 applies only to sessions numbered >= this constant.
# Checks 21 and 22 are presence-gated on provenance/*/archive/ subdirectories.
# See specifications/validation-approach.md v5 "Gating Conventions (checks 20, 21, 22)".
# Per-file budget values revised at engine-v4 per D-086 Session 023:
# - Hard ceiling 15000 → 8000 words (calibration-corrective per empirical 3.0× tokens-per-word ratio).
# - Soft warning 10000 → 6000 words (~75% of hard per design principle in read-contract.md §2).
# Aggregate hard budget + close-rotation rule added at engine-v5 per D-096 Session 028:
# - Aggregate hard ceiling 100000 / soft 90000 (§2b; pass/fail/warn, replacing v2 §2a informational-only).
# - Close-rotation window 6 sessions (§2c; default-read includes only most recent 6 session 03-close.md files).
# See specifications/read-contract.md v3 §2 + §2b + §2c + §10 versioning.
readonly READ_CONTRACT_ADOPTION_SESSION=22
readonly AGGREGATE_BUDGET_ADOPTION_SESSION=28
readonly DEFAULT_READ_HARD_WORD_CEILING=8000
readonly DEFAULT_READ_SOFT_WORD_CEILING=6000
readonly DEFAULT_READ_AGGREGATE_ADVISORY=90000
readonly DEFAULT_READ_AGGREGATE_ACTIVATION=100000
readonly DEFAULT_READ_AGGREGATE_HARD=100000
readonly DEFAULT_READ_AGGREGATE_SOFT=90000
readonly DEFAULT_READ_CLOSE_RETENTION_WINDOW=6

# Session from which the records-substrate is enforced (D-200, Session 058).
# Check 25 applies only to sessions numbered >= this constant.
# See specifications/records-contract.md v1 §3 + §6 + specifications/validation-approach.md v5 (check 25 added at engine-v10).
readonly RECORDS_CONTRACT_ADOPTION_SESSION=58
readonly SESSION_RECORD_STATUS_ENUM="closed superseded archived"

# Session from which the layered structural mechanism (Tier 2.5 + (z5) lifecycle) is enforced (D-228, Session 063).
# Checks 26, 27, 28 apply only to sessions numbered >= this constant.
# See specifications/validation-approach.md v6 §Tier 2.5 + §(z5) Validation-Debt Lifecycle + S062 D-221 layer composition.
readonly REVIEWER_AUDIT_ADOPTION_SESSION=63
readonly HONEST_LIMIT_REPETITION_THRESHOLD_WARN=3
readonly HONEST_LIMIT_REPETITION_THRESHOLD_FAIL=6
readonly LIFECYCLE_DEBT_STATUS_ENUM="open in-progress resolved deferred-with-rationale escalated"

# Providers excluded from Tier 2.5 reviewer roles per validation-approach.md v8 §Tier 2.5
# reviewer-family rule clause (d) (added Session 074 per D-288 operator-directive).
# Empirical basis: sustained Gemini findings_count=0 pattern across S063+S067+S071+S073 (n=4)
# + S073 codex cross-check on identical input produced findings_count=2 with substantive findings.
# Existing S063+S067+S071+S073 Gemini audit records remain valid as historical artefacts;
# no future reviewer-role invocation of google is permitted.
# See engine-feedback/inbox/EF-073-gemini-excluded-and-reviewer-family-rule-relaxation.md.
readonly EXCLUDED_REVIEWER_PROVIDERS="google"
readonly EXCLUDED_REVIEWER_ADOPTION_SESSION=74

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
# Post-Session-022 (D-084 R8b): open-issues.md replaced by open-issues/ directory
# with open-issues/index.md as the required default-read entry point.
# Post-Session-058 (D-203): SESSION-LOG.md migrated to records/sessions/ per
# records-contract.md v1; records/sessions/index.md replaces SESSION-LOG.md as
# default-read entry per read-contract.md v6 §1 item 5. Pre-engine-v10 sessions
# may still have SESSION-LOG.md at workspace root; accept either.
echo "[1] Required files"
for f in PROMPT.md; do
  if [[ -f "$WORKSPACE_ROOT/$f" ]]; then
    pass "$f exists"
  else
    fail "$f missing"
  fi
done
# Session log: accept either pre-engine-v10 SESSION-LOG.md OR post-engine-v10 records/sessions/index.md
if [[ -f "$WORKSPACE_ROOT/records/sessions/index.md" ]]; then
  pass "records/sessions/index.md exists (engine-v10 records-substrate)"
elif [[ -f "$WORKSPACE_ROOT/SESSION-LOG.md" ]]; then
  pass "SESSION-LOG.md exists (pre-engine-v10)"
else
  fail "Session log missing (records/sessions/index.md required at engine-v10+; SESSION-LOG.md acceptable pre-engine-v10)"
fi
# open-issues: accept either legacy single-file OR post-R8b directory
if [[ -f "$WORKSPACE_ROOT/open-issues/index.md" ]]; then
  pass "open-issues/index.md exists (post-R8b directory form)"
elif [[ -f "$WORKSPACE_ROOT/open-issues.md" ]]; then
  pass "open-issues.md exists (pre-R8b single-file form)"
else
  fail "open-issues missing (neither open-issues.md nor open-issues/index.md present)"
fi
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
  for dir in ${provdirs[@]+"${provdirs[@]}"}; do
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
# Post-engine-v10 (S058 D-203): SESSION-LOG.md migrated to records/sessions/.
# Verify each provenance dir has a corresponding records/sessions/S<NNN>.md OR
# (pre-engine-v10) is enumerated as a row in SESSION-LOG.md.
echo "[6] Session log completeness"
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
  dirname=$(basename "$dir")
  session_num=$(echo "$dirname" | grep -o '^[0-9]\{3\}')
  session_int=$((10#$session_num))
  rec_path="$WORKSPACE_ROOT/records/sessions/S${session_num}.md"
  if [[ -f "$rec_path" ]]; then
    pass "Session ${session_num} record at records/sessions/S${session_num}.md"
  elif [[ -f "$WORKSPACE_ROOT/SESSION-LOG.md" ]] && grep -qE "\|[[:space:]]*0*${session_int}[[:space:]]*\|" "$WORKSPACE_ROOT/SESSION-LOG.md" 2>/dev/null; then
    pass "Session ${session_num} in SESSION-LOG.md (pre-engine-v10)"
  else
    fail "Session ${session_num} missing from session log (no records/sessions/S${session_num}.md and no SESSION-LOG.md row)"
  fi
done
echo ""

# [7] Provenance directories non-empty
echo "[7] Provenance directory contents"
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
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
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
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
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
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
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
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
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
  dirname=$(basename "$dir")
  manifests_dir="${dir}manifests"
  if [[ ! -d "$manifests_dir" ]]; then
    continue  # no manifests/ directory; out-of-scope (D-030 §1)
  fi
  shopt -s nullglob
  manifest_files=("$manifests_dir"/*.manifest.yaml "$manifests_dir"/*.manifest.yml)
  shopt -u nullglob
  if [[ ${#manifest_files[@]} -eq 0 ]]; then
    fail "$dirname — manifests/ directory present but no *.manifest.yaml files found"
    BLOCK_CHECK_13[$dirname]=1
    continue
  fi
  session_ok=true
  for mf in "${manifest_files[@]}"; do
    mname=$(basename "$mf")
    missing=""
    for field in "${D024_REQUIRED_FIELDS[@]}"; do
      if ! grep -qE "^${field}:" "$mf"; then
        missing="${missing} ${field}"
      fi
    done
    for sub in "${D024_SAMPLING_SUBFIELDS[@]}"; do
      if ! grep -qE "^[[:space:]]+${sub}:" "$mf"; then
        missing="${missing} sampling.${sub}"
      fi
    done
    if [[ -z "$missing" ]]; then
      pass "$dirname/manifests/$mname — all D-024 required fields present"
    else
      fail "$dirname/manifests/$mname — missing D-024 fields:${missing}"
      session_ok=false
    fi
  done
  if ! $session_ok; then
    BLOCKED_SESSIONS="${BLOCKED_SESSIONS} ${dirname}"
  fi
done
echo ""

# [13] Cross-model-claim honesty (D-028, D-029, D-030)
#
# HONEST LIMIT (document read before touching this check):
# This check verifies the session's claim is internally consistent with its
# manifests. It does not and cannot verify that the manifests' lineage claims
# are themselves true. Manifest truth relies on operator integrity and the
# `participant_selected_by` field's accountability. Known gaming modes recorded
# in D-029: value-flipping (editing training_lineage_overlap_with_claude),
# `unknown` laundering, paper-human classification, wrapper impersonation. A
# failure here is a consistency failure; a pass is not a truth certificate.
#
# Gate: session declares cross_model: true in either participants.yaml or any
# file matching *-deliberation*.md (synthesis) frontmatter. Runs after check 12
# per the sequencing rule; sessions where check 12 failed are reported BLOCKED.
echo "[13] Cross-model-claim honesty"
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
  dirname=$(basename "$dir")
  # Discover cross_model declaration
  declared_cross_model=false
  shopt -s nullglob
  candidate_declarations=("${dir}participants.yaml" "${dir}participants.yml" "${dir}"*-deliberation*.md "${dir}"*deliberation.md)
  shopt -u nullglob
  for cf in "${candidate_declarations[@]}"; do
    [[ -f "$cf" ]] || continue
    if grep -qE "^cross_model:[[:space:]]*true" "$cf" 2>/dev/null; then
      declared_cross_model=true
      break
    fi
  done
  if ! $declared_cross_model; then
    continue  # no cross-model claim; out-of-scope
  fi
  # Sequencing: if check 12 failed for this session, block check 13
  if [[ " ${BLOCKED_SESSIONS} " == *" ${dirname} "* ]]; then
    echo "  ⊘ $dirname — BLOCKED: check 12 failed for this session; cannot evaluate check 13"
    continue
  fi
  # Consistency check: at least one manifest must have training_lineage_overlap_with_claude
  # other than known-overlap, or participant_kind: human
  manifests_dir="${dir}manifests"
  honest=false
  if [[ -d "$manifests_dir" ]]; then
    if grep -qE "^training_lineage_overlap_with_claude:[[:space:]]*(independent-claim|unknown)" "$manifests_dir"/*.manifest.yaml 2>/dev/null; then
      honest=true
    fi
    if grep -qE "^participant_kind:[[:space:]]*human" "$manifests_dir"/*.manifest.yaml 2>/dev/null; then
      honest=true
    fi
  fi
  if $honest; then
    pass "$dirname — cross_model: true is consistent with participant manifests"
  else
    fail "$dirname — cross_model: true declared but no participant manifest records training_lineage_overlap_with_claude other than known-overlap, and no participant_kind: human. Fix one of: (a) correct cross_model to false; (b) correct a manifest's training_lineage_overlap_with_claude to unknown or independent-claim (if truthful); (c) add a human participant manifest (if one participated). NOTE: this check verifies consistency of self-report, not truthfulness; see honest-limit comment in validate.sh."
  fi
done
echo ""

# [14] Multi-agent trigger coverage (D-037, D-038, D-039, D-040)
#
# HONEST LIMIT (read before touching this check):
# This check verifies consistency between a decision's self-declared triggers_met
# and the session's multi-agent artefacts. It does not and cannot verify that the
# triggers_met: declaration is itself a truthful classification of the decision
# against D-016. The declaration's truth relies on operator integrity and the
# triggers_rationale: field's adversarial visibility to Tier 2 review.
# Known false-compliance patterns (D-040 rationale): under-declaration, mono-
# perspective launder, strawman positions, fabricated load-bearing claim. A
# failure here is a consistency failure; a pass is not a truthfulness certificate.
#
# Gate: session number >= TRIGGERS_MET_ADOPTION_SESSION (=6). Runs after check 11
# per the sequencing rule (D-040 §Sequencing); sessions where check 11 failed are
# reported BLOCKED. Check 14 does NOT depend on check 12 (it inspects perspective
# files, not manifests — per the Outsider's precision argument in Session 006).
echo "[14] Multi-agent trigger coverage (triggers_met)"
BLOCKED_SESSIONS_14=""
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
  dirname=$(basename "$dir")
  session_num=$(echo "$dirname" | grep -o '^[0-9]\{3\}')
  session_int=$((10#$session_num))
  if [[ $session_int -lt $TRIGGERS_MET_ADOPTION_SESSION ]]; then
    continue  # pre-adoption; out-of-scope
  fi
  decisions_file="${dir}02-decisions.md"
  if [[ ! -f "$decisions_file" ]]; then
    continue  # no decisions file yet (session may be WIP); out-of-scope
  fi
  # Count perspective files (used by the "multi-agent artefacts present" branch)
  shopt -s nullglob
  perspective_files=("$dir"*-perspective-*.md)
  shopt -u nullglob
  perspective_count=${#perspective_files[@]}
  # Check 11 dependency: if perspective files exist but <3, check 11 will fail;
  # we block check 14 for this session.
  check_11_failed=false
  if [[ ${perspective_count} -gt 0 && ${perspective_count} -lt 3 ]]; then
    check_11_failed=true
  fi
  if $check_11_failed; then
    echo "  ⊘ $dirname — BLOCKED: check 11 failed for this session; cannot evaluate check 14"
    BLOCKED_SESSIONS_14="${BLOCKED_SESSIONS_14} ${dirname}"
    continue
  fi
  # Iterate decisions. Each decision block runs from '## D-NNN:' heading to the
  # next '## ' heading. We parse the file once and build an array of blocks.
  session_any_fail=false
  decisions=()
  current=""
  d_id=""
  while IFS= read -r line; do
    if [[ "$line" =~ ^##[[:space:]]+D-[0-9]+: ]]; then
      if [[ -n "$current" ]]; then
        decisions+=("${d_id}||${current}")
      fi
      d_id=$(echo "$line" | sed -E 's/^## (D-[0-9]+):.*/\1/')
      current="$line"
    elif [[ -n "$current" ]]; then
      current="${current}"$'\n'"${line}"
    fi
  done < "$decisions_file"
  if [[ -n "$current" ]]; then
    decisions+=("${d_id}||${current}")
  fi
  for decision_entry in "${decisions[@]}"; do
    did="${decision_entry%%||*}"
    dblock="${decision_entry#*||}"
    # Extract Triggers met: line
    triggers_line=$(echo "$dblock" | grep -E '^\*\*Triggers met:\*\*' | head -1 || true)
    if [[ -z "$triggers_line" ]]; then
      # Post-adoption decision without triggers_met line → fail
      fail "$dirname/$did — post-adoption decision missing **Triggers met:** line. Add **Triggers met:** [d016_X, d023_X] or **Triggers met:** [none] per D-037."
      session_any_fail=true
      continue
    fi
    # Check for d016_* in the list
    if echo "$triggers_line" | grep -qE 'd016_[0-9]+'; then
      # Multi-agent trigger fires. Require perspective count >= 3 OR single-agent-reason annotation.
      has_single_agent_reason=false
      if echo "$dblock" | grep -qE '^\*\*Single-agent reason:\*\*'; then
        has_single_agent_reason=true
      fi
      if [[ ${perspective_count} -ge 3 ]] || $has_single_agent_reason; then
        pass "$dirname/$did — d016_* trigger covered ($([[ ${perspective_count} -ge 3 ]] && echo "${perspective_count} perspective files" || echo "single-agent reason annotated"))"
      else
        fail "$dirname/$did — declares d016_* trigger but session has ${perspective_count} perspective files (expected ≥3) and no **Single-agent reason:** annotation. NOTE: this check verifies consistency of self-report, not truthfulness; see honest-limit comment in validate.sh."
        session_any_fail=true
      fi
    else
      pass "$dirname/$did — no d016_* trigger declared"
    fi
  done
  if $session_any_fail; then
    BLOCKED_SESSIONS_14="${BLOCKED_SESSIONS_14} ${dirname}"
  fi
done
echo ""

# [15] Non-Claude trigger coverage (D-037, D-038, D-039, D-040)
#
# HONEST LIMIT (read before touching this check):
# This check verifies consistency between a decision's self-declared d023_*
# triggers and the session's non-Claude participant manifests. It does not verify
# that a manifest labeled non-Claude in fact represents a non-Claude participant
# (that is check 13's consistency scope) nor that the substantive adequacy of
# any skip reason is genuine (a Tier 2 concern). The declaration's truth relies
# on operator integrity.
# Known false-compliance patterns (D-040 rationale): mislabeled manifest, bogus
# skip annotation, pattern of skips.
#
# Gate: session number >= TRIGGERS_MET_ADOPTION_SESSION (=6) AND check 12 passed.
# Runs after check 12 per the sequencing rule (D-040 §Sequencing).
echo "[15] Non-Claude trigger coverage (triggers_met)"
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
  dirname=$(basename "$dir")
  session_num=$(echo "$dirname" | grep -o '^[0-9]\{3\}')
  session_int=$((10#$session_num))
  if [[ $session_int -lt $TRIGGERS_MET_ADOPTION_SESSION ]]; then
    continue  # pre-adoption; out-of-scope
  fi
  decisions_file="${dir}02-decisions.md"
  if [[ ! -f "$decisions_file" ]]; then
    continue
  fi
  # Sequencing: block if check 12 failed for this session.
  if [[ " ${BLOCKED_SESSIONS} " == *" ${dirname} "* ]]; then
    echo "  ⊘ $dirname — BLOCKED: check 12 failed for this session; cannot evaluate check 15"
    continue
  fi
  manifests_dir="${dir}manifests"
  # Determine if session has a non-Claude manifest (participant_kind outside
  # {claude-subagent, anthropic-other}).
  has_non_claude=false
  if [[ -d "$manifests_dir" ]]; then
    if grep -hE '^participant_kind:[[:space:]]*(non-anthropic-model|human|unknown)' "$manifests_dir"/*.manifest.yaml 2>/dev/null | grep -q .; then
      has_non_claude=true
    fi
  fi
  # Iterate decisions (same parsing approach as check 14)
  decisions=()
  current=""
  d_id=""
  while IFS= read -r line; do
    if [[ "$line" =~ ^##[[:space:]]+D-[0-9]+: ]]; then
      if [[ -n "$current" ]]; then
        decisions+=("${d_id}||${current}")
      fi
      d_id=$(echo "$line" | sed -E 's/^## (D-[0-9]+):.*/\1/')
      current="$line"
    elif [[ -n "$current" ]]; then
      current="${current}"$'\n'"${line}"
    fi
  done < "$decisions_file"
  if [[ -n "$current" ]]; then
    decisions+=("${d_id}||${current}")
  fi
  for decision_entry in "${decisions[@]}"; do
    did="${decision_entry%%||*}"
    dblock="${decision_entry#*||}"
    triggers_line=$(echo "$dblock" | grep -E '^\*\*Triggers met:\*\*' | head -1 || true)
    if [[ -z "$triggers_line" ]]; then
      continue  # check 14 already fails this case; don't double-report
    fi
    if echo "$triggers_line" | grep -qE 'd023_[0-9]+'; then
      # Non-Claude trigger fires. Require non-Claude manifest OR skip annotation.
      has_skip=false
      if echo "$dblock" | grep -qE '^\*\*Non-Claude participation:\*\*' && \
         echo "$dblock" | grep -qE 'reason:' && \
         echo "$dblock" | grep -qE 'retry_in_session:'; then
        has_skip=true
      fi
      if $has_non_claude || $has_skip; then
        pass "$dirname/$did — d023_* trigger covered ($($has_non_claude && echo "non-Claude manifest present" || echo "skip annotation with reason + retry_in_session"))"
      else
        fail "$dirname/$did — declares d023_* trigger but no manifest has participant_kind outside {claude-subagent, anthropic-other} and no **Non-Claude participation:** skip annotation with reason: and retry_in_session: fields. NOTE: this check verifies consistency of self-report, not truthfulness; see honest-limit comment in validate.sh."
      fi
    else
      pass "$dirname/$did — no d023_* trigger declared"
    fi
  done
done
echo ""

# [16] Independent-claim evidence-pointer presence (D-082, Session 021)
#
# HONEST LIMIT (read before touching this check):
# This check verifies the *presence* of the training_lineage_evidence_pointer
# field in manifests claiming training_lineage_overlap_with_claude:
# independent-claim. It does not and cannot verify the *truthfulness* of the
# evidence the pointer points to. A pointer to a fabricated note passes. The
# Tier 2 question paired with this check is the designed counter-pressure.
#
# Gate: session number >= CRITERION4_ARTICULATION_SESSION (=21).
echo "[16] Independent-claim evidence-pointer presence"
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
  dirname=$(basename "$dir")
  session_num=$(echo "$dirname" | grep -o '^[0-9]\{3\}')
  session_int=$((10#$session_num))
  if [[ $session_int -lt $CRITERION4_ARTICULATION_SESSION ]]; then
    continue  # pre-adoption; out-of-scope
  fi
  manifests_dir="${dir}manifests"
  if [[ ! -d "$manifests_dir" ]]; then
    continue
  fi
  for mf in "$manifests_dir"/*.manifest.yaml; do
    [[ -f "$mf" ]] || continue
    mfname=$(basename "$mf")
    if grep -qE '^training_lineage_overlap_with_claude:[[:space:]]*independent-claim' "$mf"; then
      if grep -qE '^training_lineage_evidence_pointer:[[:space:]]*\S+' "$mf"; then
        pass "$dirname/$mfname — independent-claim evidence pointer present"
      else
        fail "$dirname/$mfname — independent-claim without training_lineage_evidence_pointer. NOTE: this check verifies presence of the pointer, not truthfulness of the evidence it points to; see honest-limit comment in validate.sh."
      fi
    fi
  done
done
echo ""

# [17] Claude-output-in-training disclosure presence (D-082, Session 021)
#
# HONEST LIMIT (read before touching this check):
# This check verifies *disclosure of self-report* of whether Claude outputs
# were in the participant's training set. It does not verify the truthfulness
# of the self-report. A known-no claim by a provider that secretly trained on
# Claude outputs passes. The value of the check is that 'unknown' (or absence)
# becomes mechanically visible, raising the cost of silently treating opaque-
# distillation participants as fully independent. Same operator-integrity
# floor as check 13.
#
# Gate: session number >= CRITERION4_ARTICULATION_SESSION (=21).
# Out-of-scope: participant_kind in {claude-subagent, anthropic-other}.
echo "[17] Claude-output-in-training disclosure"
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
  dirname=$(basename "$dir")
  session_num=$(echo "$dirname" | grep -o '^[0-9]\{3\}')
  session_int=$((10#$session_num))
  if [[ $session_int -lt $CRITERION4_ARTICULATION_SESSION ]]; then
    continue  # pre-adoption; out-of-scope
  fi
  manifests_dir="${dir}manifests"
  if [[ ! -d "$manifests_dir" ]]; then
    continue
  fi
  for mf in "$manifests_dir"/*.manifest.yaml; do
    [[ -f "$mf" ]] || continue
    mfname=$(basename "$mf")
    pkind=$(grep -E '^participant_kind:' "$mf" | head -1 | sed -E 's/^participant_kind:[[:space:]]*//' | tr -d '[:space:]')
    case "$pkind" in
      claude-subagent|anthropic-other) continue ;;  # out-of-scope per honest-limit
    esac
    if grep -qE '^claude_output_in_training:[[:space:]]*(known-yes|known-no|unknown|n/a)' "$mf"; then
      pass "$dirname/$mfname — claude_output_in_training disclosed"
    else
      fail "$dirname/$mfname — missing claude_output_in_training field (required for participant_kind=${pkind} per multi-agent-deliberation.md v4 §Heterogeneous-Participant Recording Schema). NOTE: this check verifies disclosure presence, not truthfulness; see honest-limit comment in validate.sh."
    fi
  done
done
echo ""

# [18] OI-004 closure-retrospective well-formedness (D-082, Session 021)
#
# HONEST LIMIT (read before touching this check):
# This check verifies *structural well-formedness* of any oi-004-retrospective.md
# artefact present in the workspace. It does not verify the substantive adequacy
# of the cited evidence. The Tier 2 Q8 question paired with this check is the
# designed counter-pressure: a closure-retrospective that mechanically passes
# this check but cannot survive Q8 substantive review should not justify OI-004
# closure. Same pattern as check 13 + Tier 2 Q6.
#
# Gate: presence of any provenance/*/oi-004-retrospective.md file.
echo "[18] OI-004 closure-retrospective well-formedness"
shopt -s nullglob
retrospectives=("$WORKSPACE_ROOT"/provenance/*/oi-004-retrospective.md)
shopt -u nullglob
if [[ ${#retrospectives[@]} -eq 0 ]]; then
  echo "  (no oi-004-retrospective.md present; out-of-scope)"
else
  for r in "${retrospectives[@]}"; do
    rdir=$(basename "$(dirname "$r")")
    missing=""
    for section in "## Qualifying Deliberations Table" \
                   "## Summary Tally" \
                   "## P4 Assertion"; do
      if ! grep -qF "$section" "$r"; then
        missing="${missing} '${section}'"
      fi
    done
    if [[ -z "$missing" ]]; then
      pass "$rdir/oi-004-retrospective.md — well-formed"
    else
      fail "$rdir/oi-004-retrospective.md — missing required section(s):${missing}. NOTE: this check verifies structural well-formedness only; substantive adequacy is Tier 2 Q8."
    fi
  done
fi
echo ""

# [19] Non-Anthropic participant_organisation closed-set membership (D-082, Session 021)
#
# HONEST LIMIT (read before touching this check):
# This check verifies that participant_organisation is present and falls within
# the spec-enumerated closed set. It does not verify that the declared
# organisation is the actual developer of the model. Same operator-integrity
# floor as checks 13/16/17.
#
# Gate: session number >= CRITERION4_ARTICULATION_SESSION (=21).
# In-scope: participant_kind: non-anthropic-model.
echo "[19] Non-Anthropic participant_organisation closed-set membership"
for dir in ${provdirs[@]+"${provdirs[@]}"}; do
  dirname=$(basename "$dir")
  session_num=$(echo "$dirname" | grep -o '^[0-9]\{3\}')
  session_int=$((10#$session_num))
  if [[ $session_int -lt $CRITERION4_ARTICULATION_SESSION ]]; then
    continue  # pre-adoption; out-of-scope
  fi
  manifests_dir="${dir}manifests"
  if [[ ! -d "$manifests_dir" ]]; then
    continue
  fi
  for mf in "$manifests_dir"/*.manifest.yaml; do
    [[ -f "$mf" ]] || continue
    mfname=$(basename "$mf")
    pkind=$(grep -E '^participant_kind:' "$mf" | head -1 | sed -E 's/^participant_kind:[[:space:]]*//' | tr -d '[:space:]')
    if [[ "$pkind" != "non-anthropic-model" ]]; then
      continue  # out-of-scope
    fi
    porg=$(grep -E '^participant_organisation:' "$mf" | head -1 | sed -E 's/^participant_organisation:[[:space:]]*//' | tr -d '[:space:]')
    if [[ -z "$porg" ]]; then
      fail "$dirname/$mfname — participant_kind=non-anthropic-model but participant_organisation field missing or empty"
      continue
    fi
    in_set=false
    for allowed in $PARTICIPANT_ORGANISATION_CLOSED_SET; do
      if [[ "$porg" == "$allowed" ]]; then
        in_set=true
        break
      fi
    done
    if $in_set; then
      pass "$dirname/$mfname — participant_organisation '$porg' in closed set"
    else
      fail "$dirname/$mfname — participant_organisation '$porg' not in closed set. Allowed: $PARTICIPANT_ORGANISATION_CLOSED_SET. To extend the closed set, name the addition in a decision record and update PARTICIPANT_ORGANISATION_CLOSED_SET in validate.sh in the same session."
    fi
  done
done
echo ""

# [20] Default-read surface per-file budget (D-084, Session 022)
#
# HONEST LIMIT (read before touching this check):
# This check measures word count (wc -w) of body content after the frontmatter
# closing delimiter for files enumerated in read-contract.md §1. It does not
# verify that a file under the budget is well-structured as an orientation-layer
# artefact, nor that its content is actually relevant to the current session.
# A file can pass check 20 while being effectively unreadable (e.g., an opaque
# 14,999-word wall of text); substantive readability is a Tier 2 concern.
#
# Gate: session number >= READ_CONTRACT_ADOPTION_SESSION (=22).
# Pre-adoption sessions' SESSION-LOG.md / open-issues.md states are frozen;
# the migrations in D-084 R8a/R8b bring them under budget as of Session 022.
echo "[20] Default-read surface per-file budget"
# Check if current session (last provenance directory by sort) is >= adoption session
check20_active=false
if [[ ${#provdirs[@]} -gt 0 ]]; then
  last_dir=$(printf '%s\n' "${provdirs[@]}" | sort | tail -1)
  last_dirname=$(basename "$last_dir")
  last_session_num=$(echo "$last_dirname" | grep -o '^[0-9]\{3\}' || echo "000")
  last_session_int=$((10#$last_session_num))
  if [[ $last_session_int -ge $READ_CONTRACT_ADOPTION_SESSION ]]; then
    check20_active=true
  fi
fi
if ! $check20_active; then
  echo "  (pre-adoption; check 20 out-of-scope)"
  echo ""
else
  # Build default-read surface file list per read-contract.md §1
  default_read_files=()

  # (1) Active-status specifications (status: active in frontmatter, not superseded)
  for spec in "$WORKSPACE_ROOT"/specifications/*.md; do
    [[ -f "$spec" ]] || continue
    # Read frontmatter status field (between the first two --- lines)
    status=$(awk 'BEGIN{fm=0} /^---$/{fm++; if(fm==2)exit; next} fm==1 && /^status:/{print $2; exit}' "$spec")
    if [[ "$status" == "active" ]]; then
      default_read_files+=("$spec")
    fi
  done

  # (2) PROMPT.md and prompts/*.md
  [[ -f "$WORKSPACE_ROOT/PROMPT.md" ]] && default_read_files+=("$WORKSPACE_ROOT/PROMPT.md")
  for p in "$WORKSPACE_ROOT"/prompts/*.md; do
    [[ -f "$p" ]] && default_read_files+=("$p")
  done

  # (3) Session log: records/sessions/index.md (engine-v10+) OR SESSION-LOG.md (pre-engine-v10)
  if [[ -f "$WORKSPACE_ROOT/records/sessions/index.md" ]]; then
    default_read_files+=("$WORKSPACE_ROOT/records/sessions/index.md")
  elif [[ -f "$WORKSPACE_ROOT/SESSION-LOG.md" ]]; then
    default_read_files+=("$WORKSPACE_ROOT/SESSION-LOG.md")
  fi

  # (4) open-issues/index.md (post-R8b) or open-issues.md (pre-R8b, during migration)
  if [[ -f "$WORKSPACE_ROOT/open-issues/index.md" ]]; then
    default_read_files+=("$WORKSPACE_ROOT/open-issues/index.md")
  elif [[ -f "$WORKSPACE_ROOT/open-issues.md" ]]; then
    default_read_files+=("$WORKSPACE_ROOT/open-issues.md")
  fi

  # (5) The 03-close.md of the most recent DEFAULT_READ_CLOSE_RETENTION_WINDOW sessions.
  #     (engine-v5 close-rotation rule per read-contract.md v3 §1 item 7 + §2c.
  #      Older closes remain at their paths but are archive-surface by exclusion.)
  #     Pre-engine-v5 behaviour (all closes default-read) applies if the current
  #     session is before AGGREGATE_BUDGET_ADOPTION_SESSION (=28).
  if [[ $last_session_int -ge $AGGREGATE_BUDGET_ADOPTION_SESSION ]]; then
    # Take top N close files by descending session-number (NNN prefix of parent dir).
    retained_closes=$(
      for close in "$WORKSPACE_ROOT"/provenance/*/03-close.md; do
        [[ -f "$close" ]] || continue
        parent=$(basename "$(dirname "$close")")
        nnn=$(echo "$parent" | grep -o '^[0-9]\{3\}')
        [[ -n "$nnn" ]] && printf '%s\t%s\n' "$nnn" "$close"
      done | sort -rn | head -n "$DEFAULT_READ_CLOSE_RETENTION_WINDOW" | cut -f2-
    )
    while IFS= read -r close; do
      [[ -n "$close" && -f "$close" ]] && default_read_files+=("$close")
    done <<< "$retained_closes"
  else
    # Pre-engine-v5: every close file is default-read.
    for close in "$WORKSPACE_ROOT"/provenance/*/03-close.md; do
      [[ -f "$close" ]] && default_read_files+=("$close")
    done
  fi

  # Measure each file
  for file in "${default_read_files[@]}"; do
    # Skip body-word-count computation if file missing
    [[ -f "$file" ]] || continue

    rel=$(realpath --relative-to="$WORKSPACE_ROOT" "$file" 2>/dev/null || echo "${file#$WORKSPACE_ROOT/}")

    # Extract body (content after closing --- of frontmatter, if frontmatter present).
    # If line 1 is '---', treat as frontmatter and body starts after the next '---'.
    # Otherwise, body is the entire file.
    first_line=$(head -1 "$file")
    if [[ "$first_line" == "---" ]]; then
      body=$(awk 'BEGIN{fm=0; body=0} NR==1 && /^---$/{fm=1; next} fm==1 && /^---$/{body=1; next} body==1{print}' "$file")
    else
      body=$(cat "$file")
    fi
    word_count=$(echo "$body" | wc -w | tr -d '[:space:]')

    if [[ $word_count -gt $DEFAULT_READ_HARD_WORD_CEILING ]]; then
      fail "$rel — $word_count words exceeds hard ceiling ($DEFAULT_READ_HARD_WORD_CEILING). Restructure per read-contract.md §8 (split file or relocate detail to archive-pack)."
    elif [[ $word_count -gt $DEFAULT_READ_SOFT_WORD_CEILING ]]; then
      warn "$rel — $word_count words exceeds soft warning threshold ($DEFAULT_READ_SOFT_WORD_CEILING). Approaching hard ceiling ($DEFAULT_READ_HARD_WORD_CEILING)."
    else
      pass "$rel — $word_count words within budget"
    fi
  done

  # Aggregate default-read surface report (added v2 per D-086, Session 023 R3/R5;
  # promoted to pass/fail/warn at engine-v5 per D-096 Session 028).
  #
  # engine-v4 (Sessions 22-27): informational only (advisory/activation notes).
  # engine-v5 (Session 28+): §2b budget enforcement:
  #   - aggregate >= hard (100K): FAIL (session cannot close cleanly; structural remediation required)
  #   - aggregate >= soft (90K): WARN (next substantive session must include aggregate-reducing action)
  # §2a advisory/activation notes are retained for informational continuity.
  aggregate_words=0
  for file in "${default_read_files[@]}"; do
    [[ -f "$file" ]] || continue
    first_line=$(head -1 "$file")
    if [[ "$first_line" == "---" ]]; then
      body=$(awk 'BEGIN{fm=0; body=0} NR==1 && /^---$/{fm=1; next} fm==1 && /^---$/{body=1; next} body==1{print}' "$file")
    else
      body=$(cat "$file")
    fi
    wc_out=$(echo "$body" | wc -w | tr -d '[:space:]')
    aggregate_words=$((aggregate_words + wc_out))
  done
  echo ""
  echo "  Aggregate default-read surface: $aggregate_words words across ${#default_read_files[@]} files."
  if [[ $last_session_int -ge $AGGREGATE_BUDGET_ADOPTION_SESSION ]]; then
    # engine-v5 budget enforcement (§2b)
    if [[ $aggregate_words -gt $DEFAULT_READ_AGGREGATE_HARD ]]; then
      fail "Aggregate default-read surface — $aggregate_words words exceeds hard ceiling ($DEFAULT_READ_AGGREGATE_HARD). Session cannot close cleanly; execute structural remediation per read-contract §2c close-rotation or §8 per-file remediation to return below ${DEFAULT_READ_AGGREGATE_HARD}."
    elif [[ $aggregate_words -gt $DEFAULT_READ_AGGREGATE_SOFT ]]; then
      warn "Aggregate default-read surface — $aggregate_words words exceeds soft warning ($DEFAULT_READ_AGGREGATE_SOFT). Approaching hard ceiling ($DEFAULT_READ_AGGREGATE_HARD); next substantive session must include at least one aggregate-reducing action (close-rotation execution, spec-archive-migration, or enumeration restructure)."
    else
      pass "Aggregate default-read surface — $aggregate_words words within engine-v5 budget (soft $DEFAULT_READ_AGGREGATE_SOFT / hard $DEFAULT_READ_AGGREGATE_HARD)"
    fi
  else
    # Pre-engine-v5 behaviour (informational only per v2 §2a)
    if [[ $aggregate_words -ge $DEFAULT_READ_AGGREGATE_ACTIVATION ]]; then
      echo "  ⚡ Activation threshold reached (≥${DEFAULT_READ_AGGREGATE_ACTIVATION} words). Session N+1 should deliberate aggregate hard budget per read-contract §2a and §5.3 minority."
    elif [[ $aggregate_words -ge $DEFAULT_READ_AGGREGATE_ADVISORY ]]; then
      echo "  ⚠ Advisory threshold reached (≥${DEFAULT_READ_AGGREGATE_ADVISORY} words). Approaching activation (${DEFAULT_READ_AGGREGATE_ACTIVATION}); next session should note aggregate in close."
    fi
  fi
  echo ""
fi

# [21] Archive-pack manifest integrity (D-084, Session 022)
#
# HONEST LIMIT (read before touching this check):
# This check verifies that each manifest.yaml under provenance/*/archive/*/
# has the required keys and that source_hash_sha256 matches the actual hash
# of concatenated chunks in ordinal order. It does not verify that the
# archive's content is what was originally intended, or that the archive
# is the right artefact for the session that created it.
#
# Gate: presence of any provenance/*/archive/ subdirectory.
echo "[21] Archive-pack manifest integrity"
archive_dirs=("$WORKSPACE_ROOT"/provenance/*/archive/*/)
if [[ ! -d "${archive_dirs[0]}" ]]; then
  echo "  (no archive-packs present; check 21 out-of-scope)"
  echo ""
else
  for adir in "${archive_dirs[@]}"; do
    [[ -d "$adir" ]] || continue
    manifest="$adir/manifest.yaml"
    relname="${adir#$WORKSPACE_ROOT/}"
    if [[ ! -f "$manifest" ]]; then
      fail "$relname — manifest.yaml missing"
      continue
    fi

    # Check required keys present
    required_keys=(archive_id originating_session originating_path migrated_in_session kind total_bytes total_words chunk_count chunk_boundary_rule source_hash_sha256)
    missing_keys=""
    for key in "${required_keys[@]}"; do
      if ! grep -qE "^${key}:" "$manifest"; then
        missing_keys="${missing_keys} $key"
      fi
    done
    if [[ -n "$missing_keys" ]]; then
      fail "$relname — manifest.yaml missing required keys:$missing_keys"
      continue
    fi

    # Extract stored hash
    stored_hash=$(grep -E '^source_hash_sha256:' "$manifest" | head -1 | sed -E 's/^source_hash_sha256:[[:space:]]*//' | tr -d '[:space:]"')

    # Find chunks; concatenate in ordinal order; compute hash
    chunks=("$adir"/[0-9][0-9]-*.md)
    if [[ ! -f "${chunks[0]}" ]]; then
      # Try single-source form
      if [[ -f "$adir/00-source.md" ]]; then
        computed_hash=$(shasum -a 256 "$adir/00-source.md" | awk '{print $1}')
      else
        fail "$relname — no chunks or 00-source.md present"
        continue
      fi
    else
      computed_hash=$(cat "${chunks[@]}" | shasum -a 256 | awk '{print $1}')
    fi

    if [[ "$stored_hash" == "$computed_hash" ]]; then
      pass "$relname — manifest well-formed; source_hash_sha256 matches"
    else
      fail "$relname — source_hash_sha256 mismatch. stored=$stored_hash computed=$computed_hash"
    fi
  done
  echo ""
fi

# [22] Archive-pack citation consistency (D-084, Session 022)
#
# HONEST LIMIT (read before touching this check):
# This check verifies that every [archive: <path>] reference in a default-read
# file resolves to an existing archive-pack directory. It does not verify
# that the cited content actually supports the claim at the citation site.
# Tier 2 Q9 is the paired counter-pressure.
#
# Gate: presence of any provenance/*/archive/ subdirectory.
echo "[22] Archive-pack citation consistency"
if [[ ! -d "${archive_dirs[0]}" ]]; then
  echo "  (no archive-packs present; check 22 out-of-scope)"
  echo ""
else
  # Find archive references in all .md files under workspace (excluding .git)
  # Session 033 D-108 Path L: iterate per-match via grep -HoE rather than
  # per-line of grep -rn with inner grep -oE. The per-line approach
  # concatenated multiple [archive:] tokens on a single source line into one
  # invalid path (WX-27-1 greedy-regex sub-pattern observed Sessions 031-032;
  # fired as validator FAIL at Session 033 open on the Session 032 close file's
  # own §4b WX-27-1 meta-commentary line). The per-match loop correctly
  # processes each [archive:] token independently regardless of how many
  # appear on one source line.
  any_refs=false
  broken_refs=0
  while IFS= read -r line; do
    # grep -H output format: <path>:<match>. Split on FIRST colon only.
    file="${line%%:*}"
    ref="${line#*:}"
    path=$(echo "$ref" | sed -E 's/\[archive: ([^#]+)(#[^]]+)?\]/\1/' | tr -d '[:space:]')
    # Skip placeholder references and meta-commentary illustrations.
    # Real archive references resolve to paths starting with `provenance/`
    # per read-contract.md v3 §2c and §6 citation convention. Any other
    # shape (angle-bracket placeholders, literal "path"/"slug", ellipses,
    # regex-character fragments like `[^`, truncated session-illustration
    # paths like `018-/03-close.md`) is spec-text illustration or
    # meta-commentary, not a real reference.
    # Session 033 D-108 Path L: extended placeholder skip beyond the original
    # angle-bracket + literal-"path" cases to cover the new failure modes
    # surfaced when the per-match loop (vs per-line-of-grep-rn loop) began
    # picking up previously-concatenated strings as individual tokens.
    if [[ "$path" == *"<"*">"* ]] || [[ "$path" == "path" ]] || [[ "$path" == "slug" ]]; then
      continue
    fi
    # Skip anything that is not provenance-rooted (real refs start with
    # `provenance/`). Illustrative short forms like `018-/03-close.md` and
    # regex-character fragments like `[^` are filtered out here.
    if [[ "$path" != provenance/* ]]; then
      continue
    fi
    any_refs=true
    rel_file="${file#$WORKSPACE_ROOT/}"
    # Engine-v5 (Session 028+): accept rotated-close citations of the form
    # `[archive: provenance/NNN-title/03-close.md]` (read-contract.md v3 §2c).
    # Engine-v4 (Sessions 022-027): accept only archive-pack directory paths
    # of the form `[archive: provenance/NNN-title/archive/<slug>/]`.
    # Check if path resolves as either a directory (archive-pack) or a regular
    # file (rotated close).
    resolved_dir="$WORKSPACE_ROOT/${path%/}/"
    resolved_file="$WORKSPACE_ROOT/${path%/}"
    if [[ -d "$resolved_dir" ]]; then
      pass "$rel_file — archive reference resolves: $path"
    elif [[ -f "$resolved_file" ]] && [[ "$path" == */03-close.md ]]; then
      pass "$rel_file — archive reference resolves (rotated close): $path"
    else
      fail "$rel_file — archive reference does not resolve: $path (tried $resolved_dir and $resolved_file)"
      broken_refs=$((broken_refs + 1))
    fi
  done < <(grep -rHoE --include="*.md" --exclude-dir=".git" --exclude-dir=".claude" --exclude-dir=".serena" '\[archive: [^]]+\]' "$WORKSPACE_ROOT" 2>/dev/null || true)

  if ! $any_refs; then
    echo "  (no [archive: ...] references found in default-read files; check 22 in-scope but no references to validate)"
  fi
  echo ""
fi

# [23] Workspace-identity marker MODE.md (D-113, Session 036)
#
# Engine-v7 (Session 036 D-113 + D-116) adds `MODE.md` at workspace root as a
# workspace-identity file distinct from engine-definition. `PROMPT.md` §Dispatch
# consults MODE.md as authoritative signal (with structural-signature fallback).
# This check verifies:
#   (a) MODE.md exists at workspace root
#   (b) MODE.md frontmatter carries a recognised `mode:` value
#       (self-development | external-problem)
# For the self-development source workspace (this workspace), the expected value
# is `mode: self-development`. External-workspace validation extensions (e.g.,
# verifying that application_brief path resolves for external-problem mode) are
# deferred to Session 037+ per D-113 scope-bounding.
#
# Gate: engine-v7 adoption session is 036; check 23 applies to session >= 036.
MODE_MD_ADOPTION_SESSION=36
echo "[23] Workspace-identity marker (MODE.md)"
# `|| true` prevents set -e from killing the script when the glob has no matches
# (e.g., a freshly-bootstrapped external workspace with empty provenance/).
current_session_dir=$(ls -d "$WORKSPACE_ROOT"/provenance/[0-9]*/ 2>/dev/null | sort | tail -1 || true)
current_session_num=$(basename "$current_session_dir" 2>/dev/null | sed -E 's/^0*([0-9]+).*/\1/' || true)
# Default to 0 when no session directories exist or the extracted value is
# non-numeric (e.g., bootstrapped-but-pre-Session-001 external workspaces).
# Without this defensive normalisation, the `-lt` comparison below errors under
# set -e when $current_session_num is empty or "." from basename of an empty path.
if [[ -z "$current_session_num" ]] || ! [[ "$current_session_num" =~ ^[0-9]+$ ]]; then
  current_session_num=0
fi
if [[ "$current_session_num" -lt "$MODE_MD_ADOPTION_SESSION" ]]; then
  # Pre-adoption session-number — but for bootstrapped workspaces MODE.md is
  # required at session-0 by engine-manifest §6 bootstrap contract, so still
  # verify when the file is present.
  mode_md="$WORKSPACE_ROOT/MODE.md"
  if [[ -f "$mode_md" ]]; then
    mode_val=$(awk '/^---$/{f=!f; next} f && /^mode:/{print $2; exit}' "$mode_md" | tr -d '[:space:]')
    if [[ "$mode_val" == "self-development" ]] || [[ "$mode_val" == "external-problem" ]]; then
      pass "MODE.md present with recognised mode: $mode_val (pre-Session-$MODE_MD_ADOPTION_SESSION; bootstrap state)"
    elif [[ -z "$mode_val" ]]; then
      fail "MODE.md present but missing \`mode:\` frontmatter value"
    else
      fail "MODE.md present but \`mode:\` value unrecognised: '$mode_val' (expected 'self-development' or 'external-problem')"
    fi
  else
    echo "  (session $current_session_num < $MODE_MD_ADOPTION_SESSION; check 23 out-of-scope pre-adoption)"
  fi
else
  mode_md="$WORKSPACE_ROOT/MODE.md"
  if [[ ! -f "$mode_md" ]]; then
    fail "MODE.md missing at workspace root (required at engine-v7+; see PROMPT.md §Session-001 obligation)"
  else
    # Extract `mode:` frontmatter value. Look within first 20 lines for the
    # frontmatter block and the mode line.
    mode_val=$(awk '/^---$/{f=!f; next} f && /^mode:/{print $2; exit}' "$mode_md" | tr -d '[:space:]')
    if [[ -z "$mode_val" ]]; then
      fail "MODE.md missing \`mode:\` frontmatter value"
    elif [[ "$mode_val" != "self-development" ]] && [[ "$mode_val" != "external-problem" ]]; then
      fail "MODE.md has unrecognised mode value: '$mode_val' (expected 'self-development' or 'external-problem')"
    else
      pass "MODE.md present with recognised mode: $mode_val"
    fi
  fi
fi
echo ""

# --- Check 25: records-substrate integrity (added engine-v10 Session 058 per D-200 + records-contract.md v1) ---
echo "Check 25: records-substrate integrity (records-contract.md v1 §3)"
# Gate: session >= RECORDS_CONTRACT_ADOPTION_SESSION (=58); presence-gate within scope on records/sessions/.
last_session_num=""
last_provdir=$(ls -1d "$WORKSPACE_ROOT"/provenance/*/ 2>/dev/null | sort | tail -1)
if [[ -n "$last_provdir" ]]; then
  last_session_dir="$(basename "$last_provdir")"
  last_session_num="${last_session_dir%%-*}"
fi
if [[ -z "$last_session_num" ]]; then
  echo "  (no provenance directories; check 25 out-of-scope)"
elif ! [[ "$last_session_num" =~ ^[0-9]+$ ]]; then
  echo "  (cannot parse session number from latest provenance dir; check 25 out-of-scope)"
else
  current_session_int=$((10#$last_session_num))
  if [[ $current_session_int -lt $RECORDS_CONTRACT_ADOPTION_SESSION ]]; then
    echo "  (session $current_session_num < $RECORDS_CONTRACT_ADOPTION_SESSION; check 25 out-of-scope pre-adoption)"
  else
    records_dir="$WORKSPACE_ROOT/records/sessions"
    records_index="$records_dir/index.md"
    if [[ ! -d "$records_dir" ]]; then
      fail "records/sessions/ directory missing (required at engine-v10+; see records-contract.md v1 §2.1)"
    elif [[ ! -f "$records_index" ]]; then
      fail "records/sessions/index.md missing (required at engine-v10+; see records-contract.md v1 §2.2)"
    else
      check25_pass=true
      orphan_records=0
      orphan_rows=0
      missing_field=0
      bad_status=0
      drift=0

      # Collect record IDs from filesystem
      declare -a fs_ids=()
      for rfile in "$records_dir"/S*.md; do
        [[ -f "$rfile" ]] || continue
        rid=$(awk '/^---$/{f=!f; next} f && /^id:/{print $2; exit}' "$rfile" | tr -d '[:space:]')
        if [[ -z "$rid" ]]; then
          fail "records/sessions/$(basename "$rfile") missing required \`id\` frontmatter field"
          missing_field=$((missing_field + 1))
          check25_pass=false
          continue
        fi
        # Status enum check
        rstatus=$(awk '/^---$/{f=!f; next} f && /^status:/{print $2; exit}' "$rfile" | tr -d '[:space:]')
        if [[ -z "$rstatus" ]]; then
          fail "records/sessions/$(basename "$rfile") missing required \`status\` frontmatter field"
          missing_field=$((missing_field + 1))
          check25_pass=false
        elif ! echo " $SESSION_RECORD_STATUS_ENUM " | grep -q " $rstatus "; then
          fail "records/sessions/$(basename "$rfile") has invalid status '$rstatus' (expected one of: $SESSION_RECORD_STATUS_ENUM)"
          bad_status=$((bad_status + 1))
          check25_pass=false
        fi
        fs_ids+=("$rid")
      done

      # Collect row IDs from index
      declare -a idx_ids=()
      while IFS= read -r line; do
        # Match table rows like "| [S001](S001.md) | ..."
        if [[ "$line" =~ \[S[0-9]+\]\(S[0-9]+\.md\) ]]; then
          rid=$(echo "$line" | sed -nE 's/.*\[(S[0-9]+)\].*/\1/p')
          [[ -n "$rid" ]] && idx_ids+=("$rid")
        fi
      done < "$records_index"

      # Orphan records: in fs but not in index
      for fid in "${fs_ids[@]:-}"; do
        [[ -z "$fid" ]] && continue
        found=false
        for iid in "${idx_ids[@]:-}"; do
          [[ "$fid" == "$iid" ]] && { found=true; break; }
        done
        if [[ "$found" == "false" ]]; then
          fail "Orphan record: records/sessions/${fid}.md exists but is not enumerated in records/sessions/index.md"
          orphan_records=$((orphan_records + 1))
          check25_pass=false
        fi
      done

      # Orphan index rows: in index but not in fs
      for iid in "${idx_ids[@]:-}"; do
        [[ -z "$iid" ]] && continue
        if [[ ! -f "$records_dir/${iid}.md" ]]; then
          fail "Orphan index row: records/sessions/index.md references ${iid} but records/sessions/${iid}.md does not exist"
          orphan_rows=$((orphan_rows + 1))
          check25_pass=false
        fi
      done

      if [[ "$check25_pass" == "true" ]]; then
        pass "records-substrate integrity OK: ${#fs_ids[@]} session records; index rows match; status enum clean; no orphans"
      fi
    fi
  fi
fi
echo ""

# --- Check 26: Honest-limit text repetition (added engine-v11 Session 063 per D-228; refactored Session 067 per D-244 VD-002 closure to use in-memory bash arrays instead of tempfiles, enabling execution in read-only sandboxes per S064 Tier 2.5 reviewer audit Finding 2 + validation-approach.md v7 §Tier 2.5 + S062 D-221 Layer 1) ---
#
# This check verifies textual repetition of honest-limit content across the §2c
# retention-window's 03-close.md files. It does not and cannot judge whether the
# repetition reflects genuine operational recurrence (legitimate) or ceremonial
# drift (the laundering surface that EF-058-tier-2-validation surfaces). The
# Tier 2.5 cross-family reviewer is the methodology's designed counter-pressure
# for the genuine-vs-ceremonial distinction.
#
# Substrate-aware branch (CHKD-2 evidence-consuming; added engine-v15 Session 075
# per (γ-6) phase-3.1 implementation per S073 D-280 + §10.4-M33 P3 z9 reframe):
# when provenance/<current-session>/harness-telemetry-digest.yaml is present,
# the digest is the orchestrator-produced session-open evidence packet.
# Validator consumes it (does NOT call MCP at runtime per §10.4-M33). When digest
# absent AND 00-assessment.md substrate-evidence absent, the grep-based n-gram
# fallback runs as today. Per multi-agent-deliberation.md v4 §Graceful
# Degradation: when preferred path unavailable, document the degradation, use
# the fallback, do not skip.
#
# Implementation note (S067 D-244 VD-002 closure): the grep-fallback is
# implemented entirely in-memory using bash indexed arrays + here-strings
# (no tempfile creation). This preserves algorithmic equivalence with the
# prior tempfile form while enabling check 26 execution in read-only
# sandboxes (codex CLI sandbox=read-only) where mktemp -d fails. Bash 3.2
# compatible: indexed arrays + linear-scan seen-set + here-string substring
# matching via grep -F.
echo "Check 26: honest-limit text repetition across §2c retention-window (validation-approach.md v9 §Tier 2.5 Layer 1; CHKD-2 evidence-consuming substrate-aware branch added engine-v15 Session 075)"

# Substrate-aware branch evidence probe (engine-v15 Session 075 per (γ-6) phase-3.1).
# Look for digest at provenance/<current-session>/harness-telemetry-digest.yaml.
# Per S073 D-280: validator consumes digest as evidence; does NOT require live MCP.
digest_path=""
digest_substrate_count=0
if [[ -n "${current_session_dir:-}" ]] && [[ -d "$current_session_dir" ]]; then
  digest_candidate="$current_session_dir/harness-telemetry-digest.yaml"
  if [[ -f "$digest_candidate" ]]; then
    digest_path="$digest_candidate"
    # Count harness-measured substrate_calls entries in digest (in-memory grep).
    # No YAML parser dependency: rely on the SCD-3 schema discipline that each
    # substrate_call record begins with `  - tool_name:` indentation under
    # `substrate_calls:`. Reconstructor (CM3) emits records under the same
    # indentation pattern.
    digest_substrate_count=$(awk '
      /^substrate_calls:/ { in_section=1; next }
      /^[a-zA-Z_]/ && in_section { in_section=0 }
      in_section && /^  - tool_name:/ { count++ }
      END { print count+0 }
    ' "$digest_path" 2>/dev/null || echo 0)
    echo "  (substrate-aware: digest consumed at $digest_path; substrate_calls=$digest_substrate_count; validator-as-evidence-consumer per §10.4-M33)"
  fi
fi
if [[ -z "$last_session_num" ]] || ! [[ "$last_session_num" =~ ^[0-9]+$ ]]; then
  echo "  (no provenance directories or unparseable session number; check 26 out-of-scope)"
elif [[ $((10#$last_session_num)) -lt $REVIEWER_AUDIT_ADOPTION_SESSION ]]; then
  echo "  (session $last_session_num < $REVIEWER_AUDIT_ADOPTION_SESSION; check 26 out-of-scope pre-adoption)"
else
  # Collect 03-close.md files within retention window (most recent N sessions)
  declare -a recent_closes=()
  while IFS= read -r close_file; do
    [[ -f "$close_file" ]] || continue
    recent_closes+=("$close_file")
  done < <(ls -1 "$WORKSPACE_ROOT"/provenance/*/03-close.md 2>/dev/null | sort | tail -"$DEFAULT_READ_CLOSE_RETENTION_WINDOW")

  if [[ ${#recent_closes[@]} -lt 2 ]]; then
    pass "check 26 vacuous: <2 closes in retention window; cluster detection requires >=3"
  else
    # In-memory grep-fallback: extract §8 honest-limit numbered items per close as candidate
    # fragments, store in indexed array, then count cross-close occurrences of phrase signatures.
    # No tempfile creation; safe in read-only sandboxes per VD-002 closure.
    declare -a close_content=()
    cluster_count=0
    for cf in "${recent_closes[@]}"; do
      # Extract lines from §8 honest limits section: between '## §8' and next '## §' header.
      # `|| true` suppresses pipefail when grep finds no matches (set -euo pipefail is in
      # effect at script scope); the original tempfile form used `|| true` on the redirect
      # for the same reason.
      content=$(awk '/^## §8/,/^## §[0-9]/' "$cf" 2>/dev/null \
        | grep -E '^[0-9]+\.|^- ' \
        | sed -E 's/^[0-9]+\. \*?\*?//; s/\*\*//g' \
        | head -c 5000 || true)
      close_content+=("$content")
    done

    # Detect honest-limit lines that recur across closes. Phrase signatures are first-50-chars
    # of each line (lowercased + whitespace-collapsed + non-alnum stripped); cross-close
    # presence tested via case-insensitive substring match (grep -F over here-string).
    # Bash 3.2-compatible: indexed array seen-set with linear-scan duplicate detection.
    declare -a seen_sigs=()
    for content in "${close_content[@]}"; do
      [[ -z "$content" ]] && continue
      while IFS= read -r line; do
        [[ -z "$line" ]] && continue
        # Take first 50 chars (lowercased + whitespace-collapsed) as the phrase signature
        sig=$(printf '%s' "$line" | tr '[:upper:]' '[:lower:]' | tr -s '[:space:]' ' ' | cut -c 1-50 | sed 's/[^a-z0-9 ]//g')
        [[ ${#sig} -lt 20 ]] && continue
        # Skip if signature already reported this run (linear scan over indexed array;
        # bash 3.2 lacks associative arrays).
        already_seen=false
        for prior_sig in "${seen_sigs[@]}"; do
          if [[ "$prior_sig" == "$sig" ]]; then
            already_seen=true
            break
          fi
        done
        if $already_seen; then
          continue
        fi
        # Count how many closes contain this signature (case-insensitive substring match
        # against in-memory content via here-string; no tempfile).
        match_count=0
        for other_content in "${close_content[@]}"; do
          if grep -qiF -- "$sig" <<< "$other_content" 2>/dev/null; then
            match_count=$((match_count + 1))
          fi
        done
        if [[ $match_count -ge $HONEST_LIMIT_REPETITION_THRESHOLD_FAIL ]]; then
          fail "Check 26: honest-limit text recurs in $match_count closes (>= FAIL threshold $HONEST_LIMIT_REPETITION_THRESHOLD_FAIL): \"$sig...\""
          seen_sigs+=("$sig")
          cluster_count=$((cluster_count + 1))
        elif [[ $match_count -ge $HONEST_LIMIT_REPETITION_THRESHOLD_WARN ]]; then
          warn "Check 26: honest-limit text recurs in $match_count closes (>= WARN threshold $HONEST_LIMIT_REPETITION_THRESHOLD_WARN): \"$sig...\". NOTE: textual repetition; reviewer judges genuine-vs-ceremonial."
          seen_sigs+=("$sig")
          cluster_count=$((cluster_count + 1))
        fi
      done <<< "$content"
    done

    if [[ $cluster_count -eq 0 ]]; then
      if [[ -n "$digest_path" ]]; then
        pass "check 26: no honest-limit text clusters detected across ${#recent_closes[@]}-close retention window (substrate-aware: digest at $digest_path consumed as evidence per CHKD-2 §10.4-M33; in-memory grep-fallback applied for cluster detection per S067 D-244)"
      else
        pass "check 26: no honest-limit text clusters detected across ${#recent_closes[@]}-close retention window (digest absent at $current_session_dir/harness-telemetry-digest.yaml; in-memory grep-fallback applied per S067 D-244 VD-002 closure + §Graceful Degradation)"
      fi
    fi
  fi
fi
echo ""

# --- Check 27: Cross-family reviewer audit artefact + (α)-flag-coverage (added engine-v11 Session 063 per D-228 + validation-approach.md v6 §Tier 2.5 Layer 3) ---
#
# This check verifies that when the Layer 2 (γ) reviewer mechanism triggers,
# the session committed a provenance/<NNN-session>/04-tier-2-audit.md artefact
# AND its content names every check 26 WARN/FAIL emitted at this session's
# close. It does not and cannot verify that the audit's substantive findings
# are correct, that the disposition table accurately reflects the audit's
# reasoning, or that the reviewer's family is genuinely non-Claude. The
# substrate-aware audit-quality assessment is Tier 2.5's reviewer-prompt +
# operator audit at resolving close (Layer 6).
#
# Layer 2 trigger condition (any of):
#   (a) engine-definition-touching (engine-v bump or specifications/ edit)
#   (b) substantive-arc-class (S048+ precedent; resolves substantive-arc EF or executes Path AS)
#   (c) check 26 emitted WARN/FAIL at this close
#   (d) (z5) lifecycle event (status: resolved or deferred-with-rationale or stale-without-rationale)
#   (e) operator-discretionary annotation
echo "Check 27: cross-family reviewer audit artefact (validation-approach.md v6 §Tier 2.5 Layer 3)"
if [[ -z "$last_session_num" ]] || ! [[ "$last_session_num" =~ ^[0-9]+$ ]]; then
  echo "  (no provenance directories or unparseable session number; check 27 out-of-scope)"
elif [[ $((10#$last_session_num)) -lt $REVIEWER_AUDIT_ADOPTION_SESSION ]]; then
  echo "  (session $last_session_num < $REVIEWER_AUDIT_ADOPTION_SESSION; check 27 out-of-scope pre-adoption)"
else
  # Determine whether Layer 2 trigger fires for the current session.
  # Heuristic (best-effort): trigger fires if (i) any specifications/*.md modified in last commit
  # touching the session's provenance OR (ii) the close cites an engine-v bump OR (iii) check 26
  # emitted any WARN/FAIL above OR (iv) operator-discretionary annotation in close.
  # Implementation: infer from the close-narrative content + git-log if needed; here we adopt a
  # conservative reading: if the close exists, run the artefact-presence check; the trigger
  # condition itself is best assessed by the reviewer/operator. Out-of-scope when no close.
  current_close="$last_provdir/03-close.md"
  audit_artefact="$last_provdir/04-tier-2-audit.md"

  if [[ ! -f "$current_close" ]]; then
    echo "  (current session $last_session_num has no 03-close.md yet; check 27 out-of-scope)"
  else
    # Probe Layer 2 trigger: does close mention engine-v bump, substantive-arc, MAD, or operator-discretionary?
    trigger_hits=0
    if grep -qE 'engine-v[0-9]+ ratif|engine-v[0-9]+ candidate|engine-v[0-9]+ bump|engine-definition-touching|substantive revision|substantive-arc|Path AS|MAD-execution|D-221|D-228' "$current_close" 2>/dev/null; then
      trigger_hits=$((trigger_hits + 1))
    fi
    # Layer 2 trigger (c): check 26 WARN/FAIL was emitted (we approximate by checking for WARN tokens in §8)
    # Skipped here since check 26 result is in the runtime PASS/FAIL/WARN counters.
    if [[ $trigger_hits -gt 0 ]]; then
      if [[ ! -f "$audit_artefact" ]]; then
        fail "Check 27: Layer 2 trigger fired (engine-def or substantive-arc indicator detected) but $audit_artefact missing. NOTE: artefact-presence is mechanical; substantive quality is Layer 6 operator-audit counter-pressure."
      else
        # Verify required sections per validation-approach.md v7 §Tier 2.5 audit shape.
        # v7 sub-clauses (added engine-v12 Session 064 per D-234):
        # - §2 (α)-flag coverage (carried from v6)
        # - §7 Next-session-shape critique (NEW v7 per S064 §10.4-M23 + P3's 5-condition test)
        # - frontmatter scope_coverage_table (NEW v7 per S064 §10.4-M22 P1 audit-shape requirement)
        # - bootstrap-limited-confidence label (NEW v7 per Layer 6.5; required when session adopts Tier 2.5 mechanism revisions)
        check27_pass=true
        # Full required-section enforcement at v9 (added engine-v15 Session 075 per Codex
        # S074 audit Finding F4 disposition: check 27 enforcement extended to match
        # validation-approach.md §Tier 2.5 audit shape per (z7) reviewer-prompt-template
        # v3 minimum-viable extension scope). Pre-v9, check 27 enforced only §2 + §7 +
        # scope-coverage + bootstrap-label + google-provider; per F4 the spec required
        # §1+§3+§4+§5+§6+§8 too. v9 closes that gap.
        for section in "§1" "§2" "§3" "§4" "§5" "§6" "§7" "§8"; do
          if ! grep -qE "^## ${section}" "$audit_artefact" 2>/dev/null; then
            fail "Check 27: $audit_artefact missing required ${section} section per validation-approach.md v9 §Tier 2.5 reviewer audit shape (Codex-S074-F4 close: full §1-§8 enforcement)"
            check27_pass=false
          fi
        done
        # Tripartite §3 sub-section enforcement (added engine-v15 Session 075 per
        # validation-approach.md v7 §10.4-M24 + Codex-S074-F4 close): §3 must
        # decompose into §3a close correctness + §3b mechanism adequacy + §3c
        # trajectory discipline.
        for sub in "§3a" "§3b" "§3c"; do
          if ! grep -qE "^## ${sub}|^### ${sub}" "$audit_artefact" 2>/dev/null; then
            fail "Check 27: $audit_artefact missing tripartite §3 sub-section ${sub} per validation-approach.md v9 §Tier 2.5 §10.4-M24 tripartite distinction"
            check27_pass=false
          fi
        done
        # Scope-coverage table check: scope_coverage_table or session_under_review_subjects with retention-window-closes
        if ! grep -qE '^scope_coverage_table:|retention-window-closes:' "$audit_artefact" 2>/dev/null; then
          fail "Check 27: $audit_artefact missing scope_coverage_table or retention-window-closes in frontmatter per validation-approach.md v9 §Tier 2.5 minimum-evidence-packet"
          check27_pass=false
        fi
        # Bootstrap-limited-confidence label check: required when session adopts Tier 2.5 mechanism revisions.
        # Approximation: if the close mentions a Tier-2.5-revising decision (D-233/D-234/D-288/D-291), an
        # engine-v bump, an explicit Tier 2.5 revision, or an audit-shape revision (added v9 Session 075 per
        # Codex-S074-F4 close), the audit MUST carry bootstrap_status: limited-confidence per Layer 6.5.
        if grep -qE 'D-233|D-234|D-288|D-291|engine-v1[2-9]|engine-v[2-9][0-9]|Tier 2.5 revision|§Tier 2.5.*revis|reviewer-prompt-template v[3-9]|audit-shape extension' "$current_close" 2>/dev/null; then
          if ! grep -qE '^bootstrap_status:[[:space:]]*limited-confidence' "$audit_artefact" 2>/dev/null; then
            warn "Check 27: $audit_artefact appears to audit a session adopting Tier 2.5 mechanism revisions but lacks 'bootstrap_status: limited-confidence' frontmatter declaration per validation-approach.md v9 §Bootstrap-Paradox Layered Handling Layer 6.5"
          fi
        fi
        # Excluded-reviewer-provider check (added v8 Session 074 per D-288 + D-289).
        # Per validation-approach.md v8 §Tier 2.5 reviewer-family rule clause (d):
        # google provider permanently excluded from reviewer roles per operator-directive at S074.
        # Empirical basis: sustained Gemini findings_count=0 across S063+S067+S071+S073 (n=4)
        # + S073 codex cross-check produced findings_count=2 on identical input.
        # Pre-S074 audit records remain valid; this check applies forward from session 74.
        if [[ $((10#$last_session_num)) -ge $EXCLUDED_REVIEWER_ADOPTION_SESSION ]]; then
          if grep -qE '^reviewer_provider:[[:space:]]*google' "$audit_artefact" 2>/dev/null; then
            fail "Check 27: $audit_artefact reviewer_provider: google is excluded per validation-approach.md v8 §Tier 2.5 reviewer-family rule clause (d) per S074 D-288 operator-directive. Acceptable providers: $PARTICIPANT_ORGANISATION_CLOSED_SET excluding $EXCLUDED_REVIEWER_PROVIDERS."
            check27_pass=false
          fi
        fi
        if [[ "$check27_pass" == "true" ]]; then
          pass "Check 27: $audit_artefact present with required sections (§1-§8 + tripartite §3a/§3b/§3c + scope-coverage table per validation-approach.md v9 audit shape; Codex-S074-F4 close at engine-v15)"
        fi
      fi
    else
      echo "  (Layer 2 trigger condition not detected in close narrative; check 27 out-of-scope for this session)"
    fi
  fi
fi
echo ""

# --- Check 28: (z5) Validation-debt lifecycle integrity (added engine-v11 Session 063 per D-228 + validation-approach.md v6 §(z5) Validation-Debt Lifecycle Layer 4) ---
#
# This check verifies that validation-debt/index.md table rows have required
# fields (id, introduced_session, owner_or_surface, next_action,
# review_by_session, status, escalation_disposition), valid status enum
# membership, and well-formed review_by_session values. It does not and cannot
# verify that the items genuinely represent unresolved debt, that next_action
# descriptions are substantive, that owner_or_surface assignments are
# appropriate, or that escalation_disposition rationales are non-formulaic.
# The Tier 2.5 reviewer + operator audit are the counter-pressures for
# substantive adequacy.
echo "Check 28: (z5) validation-debt lifecycle integrity (validation-approach.md v6 §(z5) Layer 4)"
if [[ -z "$last_session_num" ]] || ! [[ "$last_session_num" =~ ^[0-9]+$ ]]; then
  echo "  (no provenance directories; check 28 out-of-scope)"
elif [[ $((10#$last_session_num)) -lt $REVIEWER_AUDIT_ADOPTION_SESSION ]]; then
  echo "  (session $last_session_num < $REVIEWER_AUDIT_ADOPTION_SESSION; check 28 out-of-scope pre-adoption)"
else
  ledger="$WORKSPACE_ROOT/validation-debt/index.md"
  if [[ ! -f "$ledger" ]]; then
    echo "  (validation-debt/index.md absent; check 28 out-of-scope per presence-gating sub-clause)"
  else
    # Parse table rows: lines starting with | VD- and not the header divider row.
    declare -a row_errors=()
    row_count=0
    # Check 28 v7 sub-clause (added engine-v12 Session 064 per D-234): verify frontmatter
    # `authoritative: true` declaration per validation-approach.md v7 §(z5) authoritative-not-witness semantics.
    if ! awk '/^---$/{f=!f; next} f && /^authoritative:[[:space:]]*true[[:space:]]*$/' "$ledger" | grep -q .; then
      row_errors+=("frontmatter missing 'authoritative: true' declaration (required per validation-approach.md v7 §(z5) authoritative-not-witness semantics)")
    fi
    while IFS= read -r line; do
      [[ "$line" =~ ^\|[[:space:]]*VD- ]] || continue
      row_count=$((row_count + 1))
      # Split on | and trim each field
      IFS='|' read -ra fields <<< "$line"
      # Expected layout: empty-leading, id, introduced_session, owner_or_surface, next_action,
      # review_by_session, status, escalation_disposition, [optional empty-trailing dropped by bash read].
      # Minimum 8 tokens = 1 empty leading + 7 data fields.
      if [[ ${#fields[@]} -lt 8 ]]; then
        row_errors+=("row $row_count has fewer than 7 data fields (saw ${#fields[@]} pipe-sep tokens)")
        continue
      fi
      vd_id=$(echo "${fields[1]}" | xargs)
      intro_sess=$(echo "${fields[2]}" | xargs)
      owner=$(echo "${fields[3]}" | xargs)
      next_act=$(echo "${fields[4]}" | xargs)
      review_by=$(echo "${fields[5]}" | xargs)
      status=$(echo "${fields[6]}" | xargs)
      esc_disp=$(echo "${fields[7]}" | xargs)
      # Required field presence
      [[ -z "$vd_id" ]] && row_errors+=("row $row_count missing id")
      [[ -z "$intro_sess" ]] && row_errors+=("row $row_count ($vd_id) missing introduced_session")
      [[ -z "$owner" ]] && row_errors+=("row $row_count ($vd_id) missing owner_or_surface")
      [[ -z "$next_act" ]] && row_errors+=("row $row_count ($vd_id) missing next_action")
      [[ -z "$review_by" ]] && row_errors+=("row $row_count ($vd_id) missing review_by_session")
      [[ -z "$status" ]] && row_errors+=("row $row_count ($vd_id) missing status")
      [[ -z "$esc_disp" ]] && row_errors+=("row $row_count ($vd_id) missing escalation_disposition")
      # Status enum membership
      if [[ -n "$status" ]] && ! echo " $LIFECYCLE_DEBT_STATUS_ENUM " | grep -q " $status "; then
        row_errors+=("row $row_count ($vd_id) invalid status '$status' (expected one of: $LIFECYCLE_DEBT_STATUS_ENUM)")
      fi
      # review_by_session well-formedness (S<NNN> or NNN)
      if [[ -n "$review_by" ]] && ! [[ "$review_by" =~ ^S?[0-9]+$ ]]; then
        row_errors+=("row $row_count ($vd_id) review_by_session '$review_by' not in S<NNN> or numeric form")
      fi
      # Stale-without-rationale: if status is open or in-progress and review_by_session has lapsed, escalation_disposition must not be "n/a"
      if [[ "$status" == "open" ]] || [[ "$status" == "in-progress" ]]; then
        review_by_num=$(echo "$review_by" | sed -E 's/^S?0*//' )
        if [[ "$review_by_num" =~ ^[0-9]+$ ]] && [[ $review_by_num -lt $((10#$last_session_num)) ]]; then
          if [[ "$esc_disp" == "n/a" ]] || [[ -z "$esc_disp" ]]; then
            row_errors+=("row $row_count ($vd_id) past review_by_session $review_by (current $last_session_num) without escalation_disposition rationale")
          fi
        fi
      fi
    done < "$ledger"

    if [[ ${#row_errors[@]} -eq 0 ]]; then
      pass "Check 28: validation-debt/index.md integrity OK: $row_count lifecycle rows; all required fields present; status enum clean; review_by_session well-formed; no stale-without-rationale rows"
    else
      for err in "${row_errors[@]}"; do
        fail "Check 28: $err"
      done
    fi
  fi
fi
echo ""

# --- Check 29: Substrate-use evidence-probe (added engine-v13 Session 071 per D-264 (β)-phase) ---
# Honest limit (mandatory inline per validation-approach.md v7 honest-limits discipline):
#
#   "This check verifies the session declares structured substrate-use evidence in
#    00-assessment.md + 03-close.md per the (ε) hybrid β-phase discipline adopted at
#    S071 D-263. It does not and cannot verify that the declared substrate exercise
#    actually occurred — `producer_kind: agent-declared` per the measurement-authority
#    separation reframe. Until the (γ) phase-3 digest arc lands at S072+ with
#    harness-measured fields per VD-003 gating conditions, structured declaration is
#    self-report and check 29 is WARN-only. The (γ) digest is the methodology's
#    designed counter-pressure for actual substrate-use verification."
#
# Source: validation-approach.md §Tier 2.5 + S071 D-263 + S071 D-264.
# Gate: session number >= CHECK_29_ADOPTION_SESSION (=71); current-session 00-assessment.md AND 03-close.md presence-gated.
# Severity: WARN-only initially per S058 D-204 mechanism-rollout discipline.

readonly CHECK_29_ADOPTION_SESSION=71

echo "[Check 29] Substrate-use evidence-probe (00-assessment.md + 03-close.md structured declaration; WARN-only β-phase per S071 D-264)"
if [[ $((10#$current_session_num)) -lt $CHECK_29_ADOPTION_SESSION ]]; then
  echo "  (session $current_session_num < $CHECK_29_ADOPTION_SESSION; check 29 out-of-scope pre-adoption)"
else
  # Reuse current_session_dir from line 1080 (set to most-recent provenance/NNN-*/ at script open)
  if [[ -z "${current_session_dir:-}" ]]; then
    echo "  (current-session provenance directory absent; check 29 out-of-scope per presence-gating)"
  else
    assessment_file="$current_session_dir/00-assessment.md"
    close_file="$current_session_dir/03-close.md"
    check_29_warnings=()
    # 00-assessment.md probe
    if [[ ! -f "$assessment_file" ]]; then
      check_29_warnings+=("00-assessment.md absent at $assessment_file (substrate_session_open declaration scope unverifiable)")
    else
      if ! grep -qE '(substrate[_-]session[_-]open|substrate use at .* session-open|substrate_calls_at_session_open|forward_references.*S0?[0-9]+)' "$assessment_file"; then
        check_29_warnings+=("00-assessment.md missing substrate-use declaration (expected substrate_session_open + substrate_evidence fields OR explicit prose declaration of substrate exercise/non-availability/skip per S071 D-264 β-phase discipline)")
      fi
    fi
    # 03-close.md probe (only if close exists; close is written at session-end so probe may be absent during mid-session validate runs)
    if [[ -f "$close_file" ]]; then
      if ! grep -qE '(substrate[_-]session[_-]open|substrate use at .* session-open|substrate_calls_at_session_open|forward_references.*S0?[0-9]+|read-discipline coverage|Substrate use)' "$close_file"; then
        check_29_warnings+=("03-close.md missing substrate-use declaration mirror or read-discipline-coverage section per S071 D-264 β-phase discipline)")
      fi
    fi
    if [[ ${#check_29_warnings[@]} -eq 0 ]]; then
      pass "Check 29: substrate-use evidence-probe OK: structured/prose declaration present in 00-assessment.md (and 03-close.md when present)"
    else
      for w in "${check_29_warnings[@]}"; do
        warn "Check 29: $w"
      done
    fi
  fi
fi
echo ""

# --- Summary ---
echo "--- Tier 1 Summary ---"
echo "Passed: $PASS  |  Failed: $FAIL  |  Warnings: $WARN"
if [[ $FAIL -gt 0 ]]; then
  echo "Result: FAIL"
else
  echo "Result: PASS"
fi
echo ""

# --- Tier 2: Guided Assessment ---
echo "--- Tier 2: Guided Assessment ---"
echo ""
echo "The following questions require judgment. Consider each during the session."
echo ""
echo "  Q1. Did this session's Read activity use prior provenance to understand"
echo "      past decisions? Were any past decisions re-proposed without"
echo "      acknowledgment?"
echo ""
echo "  Q2. Are the current specifications semantically consistent with each"
echo "      other? Do any contradict or make assumptions that conflict?"
echo ""
echo "  Q3. In deliberative work, did the adversarial perspective provide genuine"
echo "      challenge, or did it concede too easily?"
echo ""
echo "  Q4. Is the methodology producing meaningful progress, or is it"
echo "      accumulating ceremony without advancing?"
echo ""
echo "  Q5. Are there specifications that describe things that no longer exist,"
echo "      or things that exist without being specified?"
echo ""
echo "  Q6. This session records cross_model: true. Name the concrete evidence —"
echo "      invocation transcript, CLI command, wall-clock gap, human presence —"
echo "      that distinguishes a genuine non-Claude participant from a Claude"
echo "      subagent with an edited manifest. If you cannot, flip cross_model to"
echo "      false. (Skip if this session does not claim cross-model participation.)"
echo ""
echo "  Q7. For each decision in this session declaring **Triggers met:**, read"
echo "      the decision's Decision and Rationale text and state whether the"
echo "      declared trigger list is consistent with the decision's content. For"
echo "      any **Non-Claude participation:** skipped annotation, state whether"
echo "      the reason is substantive (not formulaic) and the retry_in_session:"
echo "      commitment is credible. Flag mismatches and weak reasons; they are"
echo "      the dishonesty surface this session's Tier 1 checks cannot reach."
echo ""
echo "  Q8. OI-004 closure-retrospective substantive adequacy (paired with"
echo "      check 18). If this session contains an oi-004-retrospective.md, read"
echo "      its Qualifying Deliberations Table and P4 Assertion. For each row"
echo "      marked frame-replacement-or-novel-mechanism, verify the cited"
echo "      synthesis section actually contains a non-Claude-originated reframing"
echo "      (not paraphrase or restatement of a Claude perspective's argument)."
echo "      For the P4 assertion, verify the cited divergence shows the synthesis"
echo "      adopted a position that contradicts (or substantively augments) the"
echo "      Claude consensus, not merely supplemented it. Flag rows where the"
echo "      substantive claim is weaker than the structural claim suggests."
echo "      (Skip if no oi-004-retrospective.md present.)"
echo ""
echo "  Q9. Read-contract adherence (paired with check 22). For this session's"
echo "      work, verify: (a) the default-read surface enumeration in"
echo "      read-contract.md §1 was actually followed — every enumerated file"
echo "      was read at session open before any substantive work; (b) any"
echo "      archive-surface records relied on for load-bearing claims are cited"
echo "      via the [archive: path] convention in default-read files; (c) any"
echo "      non-reads of relevant archive records were declared in the session's"
echo "      honest-limits section with the gap they leave. Flag silent skips —"
echo "      these are the harness-layer laundering pattern the read-contract"
echo "      exists to prevent. Flag reliance on archive-surface claims without"
echo "      corresponding reads (the witness-dumping pattern WX-22-1 tracks)."
echo ""
echo "  Q10. Layered-mechanism engagement (added v6; paired with checks 26, 27,"
echo "       28). For this session's close, verify: (a) §8 honest-limits sections"
echo "       were authored deliberately, distinguishing genuine new gaps from"
echo "       recurrences; for recurrences, was the (z5) lifecycle ledger row"
echo "       updated rather than the close re-recording the same text? (b) If"
echo "       Layer 2 (γ) triggered, did the reviewer's audit substantively engage"
echo "       with the session's claims (decisions + close + (α)-flagged items),"
echo "       or was the audit ceremonial? (c) If a (z5) lifecycle item was"
echo "       closed/deferred this session, was disposition substantive (concrete"
echo "       next action or escalation rationale) or formulaic? Flag instances"
echo "       where the structural mechanism passed Tier 1 mechanically but the"
echo "       underlying discipline is not being engaged. The mechanism's value"
echo "       depends on engagement-quality, not artefact-presence; this Q10 is"
echo "       the designed counter-pressure for ceremonialisation."
echo ""

if [[ $FAIL -gt 0 ]]; then
  exit 1
else
  exit 0
fi
