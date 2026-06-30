# Bounded Queue Depth Controller for CPU Worker

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-queue-depth-controller-for-cpu-worker-db71c5f4de42`
Run ID: `bounded-queue-depth-controller-for-cpu-worker-db71c5f4de42-20260609T212221059442+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/11df40c64e18

## What looked useful

AIMD queue-depth bounding reduced p95 latency by 32x-116x versus unbounded queueing across smoke, confirmation, and sensitivity runs, with throughput ratios near 0.99 in the main and heavy-overload runs. Static bounding helped but missed the 250 ms p95 target at the tested cap.

## Boundaries and scale limits

Evidence is limited to synthetic arrivals and local ProcessPoolExecutor CPU tasks on cpu-worker. It does not include real Enoch queue traces, production Proxmox scheduling effects, upstream retry behavior, multi-tenant interference, or live controller integration.

## Claim scope

On a local 4-process CPU-worker benchmark with stochastic overload and real CPU-bound subprocess tasks, an AIMD bounded in-flight admission controller kept p95 completion latency below a 250 ms target while preserving roughly unbounded-executor completed throughput by applying explicit backpressure.

## Why it stopped

No-paper closure: local harness evidence supports the mechanism, but production trace replay or canary evidence is required before claiming deployment-grade or paper-ready results.

## Recommended next action

Run a bounded deepen experiment that replays real Enoch cpu-worker arrival/service traces through the same controller and measures p95 latency, throughput, backpressure rate, host load, and retry effects.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace Replay Validation for AIMD CPU Worker Queue Depth Control
- Success threshold: AIMD p95 latency stays at or below the chosen target in overload windows, completed throughput is at least 95% of unbounded, and retry/backpressure amplification remains operationally acceptable.
- Stop condition: Stop if trace replay shows AIMD misses the p95 target in two representative overload windows, loses more than 5% completed throughput without a latency win, or creates retry amplification that exceeds the measured queueing benefit.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-queue-depth-controller-for-cpu-worker-db71c5f4de42`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
