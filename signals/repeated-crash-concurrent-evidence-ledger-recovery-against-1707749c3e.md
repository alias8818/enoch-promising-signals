# Repeated-crash concurrent evidence-ledger recovery against a real idempotent external store

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `repeated-crash-concurrent-evidence-ledger-recovery-against-1707749c3e`
Run ID: `repeated-crash-concurrent-evidence-ledger-recovery-against-1707749c3e-20260523T085312778876+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Crash-restart evidence ledger integration for a real local agent loop: enoch://control-plane/projects/crash-restart-evidence-ledger-integration-for-a-real-local-d601706dfa/runs/crash-restart-evidence-ledger-integration-for-a-real-local-d601706dfa-20260523T075504346532+0000
- Parent run decision: Crash-window evidence ledger test inside a real LangGraph local loop: enoch://control-plane/projects/crash-window-evidence-ledger-test-inside-a-real-langgraph-00d775d839/runs/crash-window-evidence-ledger-test-inside-a-real-langgraph-00d775d839-20260523T084304546423+0000

## What looked useful

The mechanism recovered 7,500/7,500 operations with zero duplicates in the clean comparison and 30,000/30,000 with zero duplicates in a larger stress run. Controls showed the boundary: removing external idempotency caused 3,256 duplicate effects, and removing the durable ledger lost 7,192 of 7,500 operation keys.

## Boundaries and scale limits

Tested on one host with localhost HTTP, SQLite WAL, process-level SIGKILL crashes, up to 30,000 proposed-mechanism operations and 20,129 forced crashes. Not tested on multi-host networks, production external APIs, long-running service outages, real cloud stores, disk corruption, or day-scale traffic.

## Claim scope

Within a single-host local harness, a durable SQLite evidence ledger plus a separate SQLite-backed HTTP store with a database idempotency constraint recovered all tested operations after repeated concurrent worker crashes in the ambiguous external-commit-before-ledger-finalization window.

## Why it stopped

Bounded local evidence supports the mechanism but does not establish novelty or publication-grade generality beyond a known ledger/idempotency pattern.

## Recommended next action

Stop as no-paper useful signal; a future depth-4 follow-up should test the same harness pattern against a production-grade external system with multi-host clients and real timeout/restart fault injection before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-host evidence-ledger recovery against a production-grade idempotent store
- Success threshold: At least 100,000 operations across multiple clients with >=10,000 ambiguous-window crashes/timeouts, zero lost operation keys, zero duplicate committed effects, and controls reproducing loss or duplication.
- Stop condition: Stop if any proposed-mechanism trial loses a key, creates a duplicate external effect, or requires non-recoverable manual repair; otherwise stop after the bounded multi-host matrix completes.

## Evidence references

- Artifact root: `<local-path>/projects/repeated-crash-concurrent-evidence-ledger-recovery-against-1707749c3e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
