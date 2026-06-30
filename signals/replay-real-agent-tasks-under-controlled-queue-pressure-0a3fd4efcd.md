# Replay Real Agent Tasks Under Controlled Queue Pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-real-agent-tasks-under-controlled-queue-pressure-0a3fd4efcd`
Run ID: `replay-real-agent-tasks-under-controlled-queue-pressure-0a3fd4efcd-20260531T111743658129+0000`

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

- Parent run decision: Agent Reliability Degradation Under Queue Pressure: enoch://control-plane/projects/agent-reliability-degradation-under-queue-pressure-d18e6c50e6c8/runs/agent-reliability-degradation-under-queue-pressure-d18e6c50e6c8-20260530T063313402874+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d04a9c2427be

## What looked useful

At 0.97 utilization, p95 waits rose above 5,000s and deadline-conditioned success fell from 98.75% to 41.36% even for a loose 4x-median-service deadline, while the no-queue intrinsic success baseline stayed fixed at 100%. All tested deadline multipliers passed the Tier 1 low-to-high utilization threshold in 40/40 paired replicates.

## Boundaries and scale limits

The tasks were not rerun and semantic correctness was not regraded; arrivals were controlled Poisson arrivals, deadlines were median-service multipliers, and the corpus is local Enoch worker sessions rather than production traffic.

## Claim scope

Controlled FIFO replay of 834 real local Enoch/Codex agent-run service durations shows that queue pressure alone can sharply reduce deadline-conditioned completion while intrinsic runner success is held fixed.

## Why it stopped

Tier 1 direct replay threshold was satisfied, but this is no-paper useful signal because it replays service durations rather than live agent behavior or semantic correctness under queueing.

## Recommended next action

Run a bounded live-harness follow-up that reruns a fixed suite of real agent tasks through a controlled queue with task-specific deadlines and independent correctness grading.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Real Agent Task Queue Pressure With Correctness Grading
- Success threshold: At least 80% of paired task-suite replicates show p95 wait growth and at least 2 percentage points deadline-conditioned success loss at high utilization, while no-queue semantic correctness remains within 1 percentage point of baseline.
- Stop condition: Stop if high utilization does not increase p95 wait, if no-queue correctness drifts by more than 1 percentage point, or if deadline-conditioned loss is below 2 percentage points in more than 20% of paired replicates.

## Evidence references

- Artifact root: `<local-path>/projects/replay-real-agent-tasks-under-controlled-queue-pressure-0a3fd4efcd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
