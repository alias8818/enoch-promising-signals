# Bounded GB10 worker stability probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `bounded-gb10-worker-stability-probe-8d101af373`
Run ID: `bounded-gb10-worker-stability-probe-8d101af373-20260613T173517533727+0000`

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

- Parent run decision: Tier-0 volunteer worker liveness and capability probe: enoch://control-plane/projects/tier-0-volunteer-worker-liveness-and-capability-probe-3231811523a1/runs/tier-0-volunteer-worker-liveness-and-capability-probe-3231811523a1-20260613T171451904256+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10a2893af618

## What looked useful

Smoke and controlled runs both succeeded. The 600-second run completed 18,513 synchronized iterations at 30.855 iterations/s; median latency was 32.201 ms and p95 was 32.935 ms. Median sampled GPU utilization was 96%, max temperature was 86 C, earlyoom remained active, and MemAvailable declined by only 984,496 kB from a 120,934,040 kB start.

## Boundaries and scale limits

One host, one GPU, one PyTorch version, one dtype, one tensor shape, one process, and a 10-minute run. Does not validate mixed model training, multi-process contention, repeated worker lifecycle churn, long thermal soak, or day-scale reliability.

## Claim scope

Single GB10 worker completed a bounded 600-second single-process PyTorch/CUDA bfloat16 matmul stability probe with swap disabled and earlyoom active, without CUDA/Python errors, OOM/earlyoom intervention, or runaway MemAvailable decline.

## Why it stopped

Tier 1 controlled direct test met its operational stability threshold, but the evidence is intentionally narrow and not sufficient for paper-positive closure.

## Recommended next action

Run a bounded mixed-workload deepen test that combines sustained CUDA kernels, checkpoint-like disk I/O, moderate UMA allocation pressure, and repeated process startup/teardown for 30 minutes on the same GB10 host.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GB10 mixed workload stability probe with UMA and lifecycle pressure
- Success threshold: Complete 30 minutes and at least 20 lifecycle cycles with success true, no errors, earlyoom active, final MemAvailable above 90 GiB, MemAvailable decline under 10 GiB, and no sustained latency degradation above 2x the corresponding matmul-only baseline phase median.
- Stop condition: Stop early on any CUDA error, OOM/earlyoom intervention, final/projected MemAvailable below 90 GiB, MemAvailable decline over 10 GiB, or repeated lifecycle failure; otherwise stop at 30 minutes and report useful-signal/no-paper evidence.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-gb10-worker-stability-probe-8d101af373`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
