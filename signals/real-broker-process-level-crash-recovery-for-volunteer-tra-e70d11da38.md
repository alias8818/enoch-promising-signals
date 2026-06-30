# Real broker process-level crash recovery for volunteer training coordination

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `real-broker-process-level-crash-recovery-for-volunteer-tra-e70d11da38`
Run ID: `real-broker-process-level-crash-recovery-for-volunteer-tra-e70d11da38-20260610T214000782987+0000`

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

- Parent run decision: Broker-backed volunteer training coordinator crash-recovery test: enoch://control-plane/projects/broker-backed-volunteer-training-coordinator-crash-recover-0a26c7cce0/runs/broker-backed-volunteer-training-coordinator-crash-recover-0a26c7cce0-20260610T211920739836+0000
- Parent run decision: Queue-backed volunteer training coordinator fault-injection prototype: enoch://control-plane/projects/queue-backed-volunteer-training-coordinator-fault-injectio-c2ed9e7633/runs/queue-backed-volunteer-training-coordinator-fault-injectio-c2ed9e7633-20260610T202149092806+0000

## What looked useful

Durable recovery achieved 5/5 exact-once successful crash trials with zero duplicate canonical completions, zero missing tasks, and max first-completion-after-restart latency of 0.2348 s. The in-memory baseline passed no-crash control but failed 5/5 crash trials with median 1,689 duplicate completion events per 1,000-task trial.

## Boundaries and scale limits

Synthetic deterministic shard updates, custom local broker, one host, 12 workers, 1,000 tasks per trial, 40 total full-validation broker kills; no real model training, no production broker, no worker process kill matrix, no network partitions, and no multi-hour heterogeneous volunteer deployment.

## Claim scope

In a local multi-process TCP broker harness for volunteer-style shard coordination, a durable broker with SQLite WAL task, lease, and idempotent completion state preserved exact-once completion through 5 matched 1,000-task trials with 8 broker SIGKILL restarts per trial, while an in-memory broker baseline failed exact-once correctness under the same crash schedule.

## Why it stopped

Bounded local validation produced useful mechanism support but remains synthetic/custom-broker evidence, not publication-grade evidence for real volunteer training coordination.

## Recommended next action

Deepen with the same SIGKILL/restart protocol against the intended production broker technology and real checkpoint application before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Production broker hard-kill recovery for volunteer training coordination
- Success threshold: Production broker variant reaches 5/5 exact-once successful crash trials with zero duplicate checkpoint updates, zero missing shards, and p95 first-completion-after-restart latency below 1 second, while the non-durable baseline fails under crash conditions but passes no-crash control.
- Stop condition: Stop if the production broker cannot preserve exact-once checkpoint/update semantics in 2 or more of 5 matched crash trials, or if required production broker semantics cannot be exercised locally without private infrastructure.

## Evidence references

- Artifact root: `<local-path>/projects/real-broker-process-level-crash-recovery-for-volunteer-tra-e70d11da38`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
