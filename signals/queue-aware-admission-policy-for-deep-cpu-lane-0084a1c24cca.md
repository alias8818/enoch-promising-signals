# Queue-aware admission policy for deep CPU lane

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `queue-aware-admission-policy-for-deep-cpu-lane-0084a1c24cca`
Run ID: `queue-aware-admission-policy-for-deep-cpu-lane-0084a1c24cca-20260611T085519869272+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7c9d6f5d0952

## What looked useful

Queue-aware admission improved bursty-overload deadline goodput from 8.886/s under FIFO and 31.445/s under the best fixed backlog cap to 36.790/s, a 314.0% gain over FIFO and 17.0% gain over the best fixed cap. It was neutral under underload. A conservative p90 estimator avoided admitted misses but over-rejected and reduced goodput, showing estimator sensitivity.

## Boundaries and scale limits

Synthetic only: no production traces, no measured CPU kernels, no caller retry/rejection cost, no multi-lane fallback, and no OS/cache/NUMA scheduling overhead. The strongest overload result is from 40 seeds of a 300 s simulated bursty workload.

## Claim scope

In a reproducible discrete-event simulation of an 8-worker CPU lane with bursty mixed light/deep request service times, queue-aware deadline admission using mean class service estimates improves deadline goodput over FIFO and tuned non-class-aware fixed backlog caps, while remaining neutral in the underloaded control.

## Why it stopped

Simulation produced a useful scoped mechanism signal but not publication-grade direct evidence from real CPU lane workloads.

## Recommended next action

Run a bounded trace-driven or real CPU microbenchmark replay with measured light/deep service classes and compare FIFO, tuned fixed backlog caps, and queue-aware admission on deadline goodput and rejection cost.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-driven validation of queue-aware CPU-lane admission
- Success threshold: Queue-aware admission achieves at least 10% higher deadline goodput than the best tuned fixed backlog cap under bursty mixed-cost load and no more than 2% goodput loss in underloaded control periods.
- Stop condition: Stop if measured service classes do not provide stable admission signal, or if queue-aware admission fails to beat the best fixed backlog cap by 10% deadline goodput under bursty load.

## Evidence references

- Artifact root: `<local-path>/projects/queue-aware-admission-policy-for-deep-cpu-lane-0084a1c24cca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
