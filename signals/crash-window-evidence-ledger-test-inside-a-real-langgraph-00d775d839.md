# Crash-window evidence ledger test inside a real LangGraph local loop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `crash-window-evidence-ledger-test-inside-a-real-langgraph-00d775d839`
Run ID: `crash-window-evidence-ledger-test-inside-a-real-langgraph-00d775d839-20260523T084304546423+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Crash-restart evidence ledger integration for a real local agent loop: enoch://control-plane/projects/crash-restart-evidence-ledger-integration-for-a-real-local-d601706dfa/runs/crash-restart-evidence-ledger-integration-for-a-real-local-d601706dfa-20260523T075504346532+0000
- Parent run decision: Evidence ledger for small local agents with hash rollback: enoch://control-plane/projects/evidence-ledger-for-small-local-agents-with-hash-rollback-285fb95e160d/runs/evidence-ledger-for-small-local-agents-with-hash-rollback-285fb95e160d-20260523T060034565690+0000

## What looked useful

Across 60 after-effect-before-return crash trials, checkpoint_only achieved 0/60 exactly-once outcomes with 60 duplicate ops, ledger_commit_only achieved 0/60 with 60 duplicate ops, and ledger_reconcile achieved 60/60 exactly-once with 0 duplicate or missing ops. All before-effect and no-crash controls completed exactly once.

## Boundaries and scale limits

Tested on one local machine with JSONL files and SQLite checkpoints, 360 crash-injection trials, 60 seeds per condition, 12 loop steps, one crash per trial, one thread at a time. Not tested on remote APIs, non-idempotent sinks without operation ids, concurrent threads, repeated crashes, power-loss storage reordering, or production LangGraph deployment.

## Claim scope

In a local real LangGraph StateGraph loop with SQLite checkpointing, fixed injected process exits, and a durable JSONL external-effect sink with operation ids, evidence-ledger recovery that reconciles sink evidence prevents duplicate effects in the after-effect-before-checkpoint crash window where checkpoint-only and commit-only ledger baselines duplicate one operation per trial.

## Why it stopped

Medium local evidence supports the mechanism but remains no-paper because the external sink is a local JSONL model and the test does not cover production stores, concurrency, repeated crashes, or storage failure modes.

## Recommended next action

Run a bounded deepen test with repeated crashes and concurrent LangGraph thread ids against a real idempotent external store, then stop unless reconciliation remains exactly-once and materially better than checkpoint-only and commit-only baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Repeated-crash concurrent evidence-ledger recovery against a real idempotent external store
- Success threshold: ledger_reconcile reaches at least 99% exactly-once outcomes with zero missing ops and at least a 50 percentage-point exactly-once-rate improvement over both checkpoint_only and ledger_commit_only in after-effect crash windows.
- Stop condition: Stop if ledger_reconcile has any unrecoverable missing operation, falls below 99% exactly-once, or fails to beat both baselines by at least 50 percentage points in the direct crash-window metric.

## Evidence references

- Artifact root: `<local-path>/projects/crash-window-evidence-ledger-test-inside-a-real-langgraph-00d775d839`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
