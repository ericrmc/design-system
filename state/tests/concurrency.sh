#!/usr/bin/env bash
# Concurrency falsification trial (079 D-11 step 6 / D-9).
#
#   16 parallel `selvedge submit decision` against one open session.
#   Inject sleep on each worker (200ms) before commit to broaden the contention window.
#   Kill one worker mid-transaction (SIGKILL) to force a non-graceful abort.
#
# D-9 expected outcomes:
#   - Contiguous local ordinals (decisions.decision_no = 1..N where N = surviving submits).
#   - All references resolve.
#   - Killed process leaves no partial rows.
#   - Queued work items recoverable (none queued in this trial; OK).
#   - PRAGMA integrity_check + foreign_key_check clean.
#   - No raw "database is locked" reaches the agent layer (errors only as E_WRITE_BUSY).
#
# Trial is **falsifying** (not just informational): exit non-zero on any expected-condition
# breach. Calibration parameters (busy_timeout, retry budget) are at CLI defaults.

set -u

cd "$(dirname "$0")/../.."

PRIMARY="state/selvedge.sqlite"
PRIMARY_BACKUP="state/selvedge.sqlite.concurrency-backup"

cleanup() {
  if [ -f "$PRIMARY_BACKUP" ]; then
    mv "$PRIMARY_BACKUP" "$PRIMARY"
    rm -f "$PRIMARY"-wal "$PRIMARY"-shm
  fi
  rm -f /tmp/selvedge-concurrency-*.log
}
trap cleanup EXIT

if [ -f "$PRIMARY" ]; then
  cp "$PRIMARY" "$PRIMARY_BACKUP"
fi
rm -f "$PRIMARY" "$PRIMARY"-wal "$PRIMARY"-shm

echo "== concurrency trial =="
echo

bin/selvedge init --force >/dev/null

# Single session — all submits target it.
bin/selvedge submit session-open --payload '{
  "session_no": 1,
  "slug": "concurrency-trial",
  "mode": "self-development",
  "workspace_id": "selvedge-self-development",
  "engine_version_at_open": "engine-v17"
}' >/dev/null

N_PARALLEL=16
KILL_WORKER=8
INJECT_SLEEP_PY=0.2

# Slow submit: a Python wrapper that opens the workspace, parses argv, and inserts a
# decision with the standard CLI but with a sleep injected just before commit. We don't
# add a sleep flag to the CLI for this; instead, the wrapper holds open a temp marker so
# we can SIGKILL one worker mid-transaction.
WORKER_PY="$(mktemp -t selvedge-conc-worker.XXXX.py)"
cat > "$WORKER_PY" <<'PYEOF'
import json, os, sys, sqlite3, time, hashlib, signal
sys.path.insert(0, os.environ["WS"])
from selvedge import cli

worker_id = int(sys.argv[1])
inject_sleep = float(sys.argv[2])
mark_kill = (len(sys.argv) > 3 and sys.argv[3] == "kill")

# Hand-roll the equivalent of `selvedge submit decision` but with a sleep before COMMIT,
# so that several writers genuinely contend for the BEGIN IMMEDIATE lock.
db = cli.db_path()
conn = sqlite3.connect(str(db), isolation_level=None, timeout=cli.DEFAULT_BUSY_TIMEOUT_MS / 1000)
conn.row_factory = sqlite3.Row
conn.execute(f"PRAGMA busy_timeout = {cli.DEFAULT_BUSY_TIMEOUT_MS}")
conn.execute("PRAGMA foreign_keys = ON")

attempt = 0
RETRY_BUDGET = cli.DEFAULT_RETRY_BUDGET
RETRY_BASE = cli.DEFAULT_RETRY_BASE_MS

while True:
    try:
        conn.execute("BEGIN IMMEDIATE")
        sess = conn.execute("SELECT session_id, session_no FROM sessions WHERE session_no=1").fetchone()
        if sess is None:
            raise RuntimeError("missing session")
        next_no = conn.execute(
            "SELECT COALESCE(MAX(decision_no),0)+1 AS n FROM decisions WHERE session_id=?",
            (sess["session_id"],),
        ).fetchone()["n"]
        title = f"concurrency worker {worker_id}"
        body = f"worker {worker_id} body"
        cur = conn.execute(
            "INSERT INTO decisions (session_id, decision_no, kind, title, body_md) VALUES (?,?,?,?,?)",
            (sess["session_id"], next_no, "calibration", title, body),
        )
        did = cur.lastrowid
        alias = f"D-S{sess['session_no']:03d}-{next_no}"
        conn.execute(
            "INSERT INTO objects (object_kind, typed_row_id, citable_alias) VALUES ('decision', ?, ?)",
            (did, alias),
        )
        oid = conn.execute("SELECT last_insert_rowid() AS r").fetchone()["r"]
        conn.execute("UPDATE decisions SET object_id=? WHERE decision_id=?", (oid, did))
        # Insert the rejected alternative (T-02 happiness on later close).
        conn.execute(
            "INSERT INTO decision_alternatives (decision_id, label, summary, rejection_reason_md) VALUES (?,?,?,?)",
            (did, "R-1.1", "alt", "alternative rejected for concurrency-trial purposes only"),
        )

        # Inject sleep INSIDE the transaction to broaden the contention window.
        if inject_sleep > 0:
            time.sleep(inject_sleep)

        if mark_kill:
            # Mark "I am about to commit" to a tempfile so the killer knows we're inside the tx,
            # then sleep an extra second to give the killer time to fire SIGKILL.
            Path = __import__("pathlib").Path
            Path(f"/tmp/selvedge-concurrency-killmark-{worker_id}.flag").write_text("ready")
            time.sleep(2)

        conn.execute("COMMIT")
        print(json.dumps({"ok": True, "worker": worker_id, "decision_no": next_no, "alias": alias}))
        sys.exit(0)
    except sqlite3.OperationalError as e:
        msg = str(e)
        try: conn.execute("ROLLBACK")
        except Exception: pass
        if ("database is locked" in msg or "database is busy" in msg) and attempt < RETRY_BUDGET:
            time.sleep((RETRY_BASE * (2 ** attempt)) / 1000)
            attempt += 1
            continue
        # CRITICAL: never let raw lock error escape — convert to E_WRITE_BUSY.
        if "database is locked" in msg or "database is busy" in msg:
            print(json.dumps({"ok": False, "worker": worker_id, "code": "E_WRITE_BUSY", "detail": msg}), file=sys.stderr)
            sys.exit(2)
        print(json.dumps({"ok": False, "worker": worker_id, "code": "E_DB", "detail": msg}), file=sys.stderr)
        sys.exit(3)
    except sqlite3.IntegrityError as e:
        try: conn.execute("ROLLBACK")
        except Exception: pass
        print(json.dumps({"ok": False, "worker": worker_id, "code": "E_REFUSAL", "detail": str(e)}), file=sys.stderr)
        sys.exit(3)
PYEOF

export WS="$PWD"

# Launch workers in parallel.
PIDS=()
for i in $(seq 1 $N_PARALLEL); do
  if [ "$i" = "$KILL_WORKER" ]; then
    python3 "$WORKER_PY" "$i" "$INJECT_SLEEP_PY" "kill" > "/tmp/selvedge-concurrency-${i}.log" 2>&1 &
  else
    python3 "$WORKER_PY" "$i" "$INJECT_SLEEP_PY" > "/tmp/selvedge-concurrency-${i}.log" 2>&1 &
  fi
  PIDS+=($!)
done

# Wait briefly for the kill-marked worker to enter its tx, then SIGKILL it.
KILL_PID=${PIDS[$((KILL_WORKER-1))]}
for _ in $(seq 1 50); do
  if [ -f "/tmp/selvedge-concurrency-killmark-${KILL_WORKER}.flag" ]; then
    break
  fi
  sleep 0.1
done
if kill -0 "$KILL_PID" 2>/dev/null; then
  kill -9 "$KILL_PID" 2>/dev/null || true
  echo "killed worker $KILL_WORKER (pid $KILL_PID)"
fi
rm -f "/tmp/selvedge-concurrency-killmark-${KILL_WORKER}.flag"

# Wait for rest.
for pid in "${PIDS[@]}"; do
  wait "$pid" 2>/dev/null || true
done

echo
echo "== results =="

# Parse logs.
SUCCEEDED=0
WRITE_BUSY=0
KILLED_OK=0
OTHER=0
for i in $(seq 1 $N_PARALLEL); do
  out=$(cat "/tmp/selvedge-concurrency-${i}.log" 2>/dev/null || echo "")
  if echo "$out" | grep -q '"ok": true'; then
    SUCCEEDED=$((SUCCEEDED+1))
  elif echo "$out" | grep -q "E_WRITE_BUSY"; then
    WRITE_BUSY=$((WRITE_BUSY+1))
  elif [ "$i" = "$KILL_WORKER" ] && [ -z "$out" ]; then
    KILLED_OK=$((KILLED_OK+1))
  elif [ "$i" = "$KILL_WORKER" ]; then
    KILLED_OK=$((KILLED_OK+1))   # killed; output state irrelevant
  else
    OTHER=$((OTHER+1))
    echo "  worker $i unexpected: $out"
  fi
done
echo "succeeded=$SUCCEEDED  E_WRITE_BUSY=$WRITE_BUSY  killed=$KILLED_OK  other_failures=$OTHER"

# Substrate sanity.
N_DECISIONS=$(sqlite3 "$PRIMARY" "SELECT COUNT(*) FROM decisions WHERE kind='calibration';")
MIN_NO=$(sqlite3 "$PRIMARY" "SELECT MIN(decision_no) FROM decisions WHERE kind='calibration';")
MAX_NO=$(sqlite3 "$PRIMARY" "SELECT MAX(decision_no) FROM decisions WHERE kind='calibration';")
DUP_NO=$(sqlite3 "$PRIMARY" "SELECT COUNT(*) FROM (SELECT decision_no FROM decisions WHERE kind='calibration' GROUP BY session_id, decision_no HAVING COUNT(*) > 1);")
INTEGRITY=$(sqlite3 "$PRIMARY" "PRAGMA integrity_check;")
FK=$(sqlite3 "$PRIMARY" "PRAGMA foreign_key_check;")
ORPHAN_OBJECTS=$(sqlite3 "$PRIMARY" "SELECT COUNT(*) FROM objects o WHERE o.object_kind='decision' AND NOT EXISTS (SELECT 1 FROM decisions d WHERE d.decision_id = o.typed_row_id);")
ORPHAN_ALTS=$(sqlite3 "$PRIMARY" "SELECT COUNT(*) FROM decision_alternatives da WHERE NOT EXISTS (SELECT 1 FROM decisions d WHERE d.decision_id = da.decision_id);")

echo "  decisions(calibration) = $N_DECISIONS  min=$MIN_NO  max=$MAX_NO  dup=$DUP_NO"
echo "  integrity_check = $INTEGRITY"
echo "  foreign_key_check (rows) = $(echo "$FK" | grep -c .)"
echo "  orphan decision objects = $ORPHAN_OBJECTS"
echo "  orphan alternatives = $ORPHAN_ALTS"

# Falsification gates.
FAIL=0
[ "$INTEGRITY" = "ok" ] || { echo "FAIL  integrity_check"; FAIL=1; }
[ -z "$FK" ] || { echo "FAIL  foreign_key_check returned violations"; FAIL=1; }
[ "$DUP_NO" = "0" ] || { echo "FAIL  duplicate decision_no observed"; FAIL=1; }
[ "$ORPHAN_OBJECTS" = "0" ] || { echo "FAIL  orphaned decision-objects (killed worker left partial rows)"; FAIL=1; }
[ "$ORPHAN_ALTS" = "0" ] || { echo "FAIL  orphan decision_alternatives"; FAIL=1; }
# Surviving submits should match contiguous 1..N_DECISIONS.
EXPECTED_MAX="$N_DECISIONS"
[ "$MAX_NO" = "$EXPECTED_MAX" ] || { echo "FAIL  decision_no max=$MAX_NO != count=$N_DECISIONS"; FAIL=1; }
[ "$MIN_NO" = "1" ] || { echo "FAIL  decision_no min=$MIN_NO != 1"; FAIL=1; }
[ "$OTHER" = "0" ] || { echo "FAIL  $OTHER worker(s) failed in unexpected ways"; FAIL=1; }

# Killed worker should not have left a row.
KILLED_DECISIONS=$(sqlite3 "$PRIMARY" "SELECT COUNT(*) FROM decisions WHERE title='concurrency worker $KILL_WORKER';")
[ "$KILLED_DECISIONS" = "0" ] || { echo "FAIL  killed worker left $KILLED_DECISIONS decision row(s) — atomicity breach"; FAIL=1; }

# Surviving = N_PARALLEL - 1 expected (the killed one).
EXPECTED_SURVIVING=$((N_PARALLEL - 1))
[ "$SUCCEEDED" = "$EXPECTED_SURVIVING" ] \
  && echo "ok  surviving submits = $EXPECTED_SURVIVING (killed=1)" \
  || { echo "FAIL  surviving=$SUCCEEDED expected=$EXPECTED_SURVIVING"; FAIL=1; }

echo
[ "$FAIL" = "0" ] && { echo "concurrency: PASS"; exit 0; } || { echo "concurrency: FAIL"; exit 1; }
