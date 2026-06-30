# Queue Depth Pressure Testing for Evidence Artifact Generation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-depth-pressure-testing-for-evidence-artifact-generation-d8c6b9d5f56d`
Run ID: `queue-depth-pressure-testing-for-evidence-artifact-generation-d8c6b9d5f56d-20260610T212954960106+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eb27cdc59ebe

## What looked useful

Queue depth 2 improved throughput from 722.14 to 879.73 artifacts/s versus depth 1 and was the best observed throughput point. Depth 64 increased p95 resident queue wait 33.90x and p95 end-to-end latency 5.84x versus depth 1. Independent verification re-read 14,336 artifacts and 3,762,037,566 bytes with zero failures.

## Boundaries and scale limits

Synthetic local JSON-plus-payload artifacts only; no live Enoch controller queue, no multi-worker contention, no remote object storage, no database writes, no model/GPU artifact producers, and no long-running concurrent research-job load.

## Claim scope

On this single GB10 worker, a bounded local artifact-generation benchmark with 8 writer threads, atomic fsync writes, and independent hash verification showed that shallow queues recovered most throughput while deep queues mainly increased artifact availability latency.

## Why it stopped

Local synthetic evidence supports shallow bounded queues plus backpressure for artifact generation, but the result is not direct production-controller evidence and is not publication-grade.

## Recommended next action

Stop this run as no-paper useful signal; if operationally relevant, run a bounded deepen follow-up against the actual Enoch evidence artifact pipeline with real controller queue depths and persistence backends.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Enoch Evidence Pipeline Queue-Depth Sweep
- Success threshold: Zero integrity failures and evidence that a shallow queue, preferably depth 2 to 8, achieves at least 95% of best observed throughput while keeping p95 artifact availability latency less than half of depth 64.
- Stop condition: Stop if any queue depth produces artifact loss/corruption, if throughput varies too much to distinguish a latency frontier after repeated bounded runs, or if the live pipeline differs so much that this local benchmark is not comparable.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-pressure-testing-for-evidence-artifact-generation-d8c6b9d5f56d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
