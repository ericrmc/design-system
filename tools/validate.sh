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
# Budget values revised at engine-v4 per D-086 Session 023:
# - Hard ceiling 15000 → 8000 words (calibration-corrective per empirical 3.0× tokens-per-word ratio).
# - Soft warning 10000 → 6000 words (~75% of hard per design principle in read-contract.md §2).
# See specifications/read-contract.md v2 §2 + §10 versioning.
readonly READ_CONTRACT_ADOPTION_SESSION=22
readonly DEFAULT_READ_HARD_WORD_CEILING=8000
readonly DEFAULT_READ_SOFT_WORD_CEILING=6000
readonly DEFAULT_READ_AGGREGATE_ADVISORY=90000
readonly DEFAULT_READ_AGGREGATE_ACTIVATION=100000

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
echo "[1] Required files"
for f in PROMPT.md SESSION-LOG.md; do
  if [[ -f "$WORKSPACE_ROOT/$f" ]]; then
    pass "$f exists"
  else
    fail "$f missing"
  fi
done
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
for dir in "${provdirs[@]}"; do
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
for dir in "${provdirs[@]}"; do
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
for dir in "${provdirs[@]}"; do
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
for dir in "${provdirs[@]}"; do
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
for dir in "${provdirs[@]}"; do
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
for dir in "${provdirs[@]}"; do
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

  # (3) SESSION-LOG.md
  [[ -f "$WORKSPACE_ROOT/SESSION-LOG.md" ]] && default_read_files+=("$WORKSPACE_ROOT/SESSION-LOG.md")

  # (4) open-issues/index.md (post-R8b) or open-issues.md (pre-R8b, during migration)
  if [[ -f "$WORKSPACE_ROOT/open-issues/index.md" ]]; then
    default_read_files+=("$WORKSPACE_ROOT/open-issues/index.md")
  elif [[ -f "$WORKSPACE_ROOT/open-issues.md" ]]; then
    default_read_files+=("$WORKSPACE_ROOT/open-issues.md")
  fi

  # (5) Every provenance/*/03-close.md
  for close in "$WORKSPACE_ROOT"/provenance/*/03-close.md; do
    [[ -f "$close" ]] && default_read_files+=("$close")
  done

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

  # Aggregate default-read surface report (added v2 per D-086, Session 023 R3/R5).
  # Informational; not pass/fail/warn at engine-v4. Thresholds inform Session N+1
  # deliberation if fired. See read-contract.md v2 §2a.
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
  if [[ $aggregate_words -ge $DEFAULT_READ_AGGREGATE_ACTIVATION ]]; then
    echo "  ⚡ Activation threshold reached (≥${DEFAULT_READ_AGGREGATE_ACTIVATION} words). Session N+1 should deliberate aggregate hard budget per read-contract §2a and §5.3 minority."
  elif [[ $aggregate_words -ge $DEFAULT_READ_AGGREGATE_ADVISORY ]]; then
    echo "  ⚠ Advisory threshold reached (≥${DEFAULT_READ_AGGREGATE_ADVISORY} words). Approaching activation (${DEFAULT_READ_AGGREGATE_ACTIVATION}); next session should note aggregate in close."
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
  any_refs=false
  broken_refs=0
  while IFS= read -r line; do
    file=$(echo "$line" | cut -d: -f1)
    ref=$(echo "$line" | grep -oE '\[archive: [^]]+\]')
    path=$(echo "$ref" | sed -E 's/\[archive: ([^#]+)(#[^]]+)?\]/\1/' | tr -d '[:space:]')
    # Skip placeholder references (documentation examples with angle brackets or
    # the literal tokens "path" and "slug" used as generic placeholder text).
    # These are spec-text illustrations, not real references.
    if [[ "$path" == *"<"*">"* ]] || [[ "$path" == "path" ]]; then
      continue
    fi
    any_refs=true
    # Check if path exists (accept trailing slash)
    resolved="$WORKSPACE_ROOT/${path%/}/"
    rel_file="${file#$WORKSPACE_ROOT/}"
    if [[ -d "$resolved" ]]; then
      pass "$rel_file — archive reference resolves: $path"
    else
      fail "$rel_file — archive reference does not resolve: $path (tried $resolved)"
      broken_refs=$((broken_refs + 1))
    fi
  done < <(grep -rn --include="*.md" --exclude-dir=".git" --exclude-dir=".claude" --exclude-dir=".serena" -E '\[archive: [^]]+\]' "$WORKSPACE_ROOT" 2>/dev/null || true)

  if ! $any_refs; then
    echo "  (no [archive: ...] references found in default-read files; check 22 in-scope but no references to validate)"
  fi
  echo ""
fi

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

if [[ $FAIL -gt 0 ]]; then
  exit 1
else
  exit 0
fi
