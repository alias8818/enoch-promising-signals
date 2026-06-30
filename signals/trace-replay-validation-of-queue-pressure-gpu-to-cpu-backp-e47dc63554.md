# Trace-Replay Validation of Queue-Pressure GPU-to-CPU Backpressure Routing

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `trace-replay-validation-of-queue-pressure-gpu-to-cpu-backp-e47dc63554`
Run ID: `trace-replay-validation-of-queue-pressure-gpu-to-cpu-backp-e47dc63554-20260610T142231184283+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Queue-Pressure Backpressure Routing Between GPU and CPU Tiers: enoch://control-plane/projects/queue-pressure-backpressure-routing-between-gpu-and-cpu-tiers-5f22367dd87f/runs/queue-pressure-backpressure-routing-between-gpu-and-cpu-tiers-5f22367dd87f-20260610T070257296262+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/01fe695f76d4

## What looked useful

Queue pressure alone was not a viable routing signal for this workload/host mix. CPU service was 63x-111x slower than GPU service at calibrated sizes; whenever CPU routing occurred, burst p95 latency worsened by 3.29x-18.00x and throughput fell by 68.0%-88.6%. A threshold that routed zero CPU jobs showed small noise-level improvement but did not support the mechanism.

## Boundaries and scale limits

Synthetic controlled traces, homogeneous GPU-favored kernel, one GB10 host, simple backlog-threshold scheduler, short local replay; not a production trace, heterogeneous serving workload, datacenter-scale system, or publication-grade validation.

## Claim scope

Tier 1 controlled local trace replay on NVIDIA GB10 using real CPU and GPU execution of homogeneous matrix-multiply jobs; queue-pressure-only GPU-to-CPU routing was compared with GPU-only on control and burst traces across multiple thresholds.

## Why it stopped

Tier 1 direct controlled replay failed the success threshold: no CPU-routing threshold achieved 20% burst p95 latency reduction with no more than 5% throughput loss, and routed runs materially worsened latency and throughput.

## Recommended next action

Stop this queue-pressure-only route as no-paper evidence; the only concrete next bounded test is a cost-aware heterogeneous trace replay that routes jobs only when measured CPU service can beat estimated GPU drain time.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cost-Aware Heterogeneous Trace Replay for GPU-to-CPU Backpressure Routing
- Success threshold: Cost-aware routing reduces burst p95 latency by at least 20% versus GPU-only, loses no more than 5% throughput, beats queue-pressure-only routing, and regresses control-trace p95 by no more than 10%.
- Stop condition: Stop if calibration finds no job class with CPU completion time below estimated GPU drain time under burst backlog, or if cost-aware routing fails the latency/throughput threshold on the controlled replay.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-validation-of-queue-pressure-gpu-to-cpu-backp-e47dc63554`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
