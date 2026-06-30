# Multi-host evidence-ledger recovery against a production-grade idempotent store

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `58`
Project ID: `multi-host-evidence-ledger-recovery-against-a-production-g-e46786bae9`
Run ID: `multi-host-evidence-ledger-recovery-against-a-production-g-e46786bae9-20260523T100804551763+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `58`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Repeated-crash concurrent evidence-ledger recovery against a real idempotent external store: enoch://control-plane/projects/repeated-crash-concurrent-evidence-ledger-recovery-against-1707749c3e/runs/repeated-crash-concurrent-evidence-ledger-recovery-against-1707749c3e-20260523T085312778876+0000
- Parent run decision: Crash-window evidence ledger test inside a real LangGraph local loop: enoch://control-plane/projects/crash-window-evidence-ledger-test-inside-a-real-langgraph-00d775d839/runs/crash-window-evidence-ledger-test-inside-a-real-langgraph-00d775d839-20260523T084304546423+0000

## What looked useful

Evidence ledgers are useful when source progress can advance separately from a remote idempotent write: the ledger recovered crash-after-intent/before-remote and crash-after-remote/before-ack windows with zero missing operations, whereas no-ledger early checkpointing lost exactly the crash-after-checkpoint/before-remote operations. The mechanism is supported locally but not paper-ready.

## Boundaries and scale limits

Not a physical multi-machine production deployment. Did not test network partitions, disk loss, Postgres failover, queue integrations, cross-region stores, high-concurrency saturation, tail latency, or mature transactional-outbox deployments. The store-only checkpoint-after-success control also achieved zero loss in this simple ordered source model.

## Claim scope

In a local deterministic crash-injection harness with PostgreSQL 16.13 as an idempotent store, eight process-isolated hosts, per-host SQLite WAL evidence ledgers, and five fixed seeds, durable intent-before-checkpoint recovery preserved all 200,000 ledger-strategy operations despite 624 process restarts, while a no-ledger early-checkpoint baseline lost 271 of 200,000 operations.

## Why it stopped

Tier 4 paper-readiness was not met: evidence is local harness replication against PostgreSQL rather than production multi-host deployment robustness, and a checkpoint-after-success control matched zero-loss correctness for the simple source model.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful signal; do not chain another follow-up from this run, and only revisit in a separate campaign with real multi-machine queue/store/failover infrastructure.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/multi-host-evidence-ledger-recovery-against-a-production-g-e46786bae9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
