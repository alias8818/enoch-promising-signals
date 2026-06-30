# Queue Depth Pressure Test for CPU Worker Reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-depth-pressure-test-for-cpu-worker-reliability-51c0e2dfb1d8`
Run ID: `queue-depth-pressure-test-for-cpu-worker-reliability-51c0e2dfb1d8-20260607T045638145522+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d189e1faa4bf

## What looked useful

Bounded outstanding work is a practical local mitigation for queue-depth latency pressure: in the main run, unbounded depth 1024 had 150.6x higher p99 queue wait than bounded submission with zero task errors in both policies. This is useful operational evidence but not paper-grade validation.

## Boundaries and scale limits

Synthetic fixed-duration CPU tasks only; no real Enoch controller queue, no real agent workloads, no long-duration saturation, and no datacenter-scale or multi-worker validation. Peak RSS did not separate meaningfully between policies at tested payload sizes, so memory-pressure claims are not supported.

## Claim scope

On this 8-vCPU CPU worker, a short synthetic ProcessPoolExecutor pressure harness showed that unbounded local submission preserved task completion at depths up to 1024 but caused p99 executor queue wait to grow to 5.2 seconds, while a bounded outstanding-work policy kept p99 wait below 58 ms at the same tested depths.

## Why it stopped

Synthetic local proxy supported the queue-wait backpressure mechanism but did not produce production-queue evidence, task failures, or a memory-pressure boundary; this is not full validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded direct test should replay real Enoch controller-dispatched CPU jobs with admission/start/finish timestamps and retry/failure accounting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end Enoch CPU queue depth replay with admission backpressure
- Success threshold: At the highest tested real queue depth, bounded admission reduces p99 admission-to-start latency by at least 5x versus unbounded admission while maintaining equal or lower failure and retry rates.
- Stop condition: Stop if bounded admission fails to improve p99 admission-to-start latency by at least 2x, increases failures/retries, or if production controller instrumentation is unavailable.

## Evidence references

- Artifact root: `<local-path>/projects/queue-depth-pressure-test-for-cpu-worker-reliability-51c0e2dfb1d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
