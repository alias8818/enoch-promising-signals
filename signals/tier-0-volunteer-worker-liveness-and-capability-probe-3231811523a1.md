# Tier-0 volunteer worker liveness and capability probe

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `tier-0-volunteer-worker-liveness-and-capability-probe-3231811523a1`
Run ID: `tier-0-volunteer-worker-liveness-and-capability-probe-3231811523a1-20260613T171451904256+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/10a2893af618

## What looked useful

The worker passed a bounded liveness/capability probe: 64 MiB filesystem integrity check succeeded, CPU checksum loop completed, memory telemetry showed about 121 GiB total with swap disabled, nvidia-smi and nvcc were visible, and PyTorch 2.12.0+cu130 completed an 8-repeat 2048x2048 CUDA matmul on NVIDIA GB10.

## Boundaries and scale limits

Single short local probe only; no long-duration stability, sustained throughput, multi-process scheduling, network, container isolation, or model-training validation was performed.

## Claim scope

At probe time on host gx10-efe8, the assigned Enoch worker was live, could write/read project-local artifacts, exposed Python 3.12, had no swap, exposed NVIDIA GB10 and CUDA 13.0 tooling, and completed a small PyTorch CUDA matmul smoke workload.

## Why it stopped

The worker liveness/capability question was answered by direct local evidence, but the result is operational no-paper evidence rather than a scientific publication claim.

## Recommended next action

Stop for this tier-0 liveness run; optional next action is a bounded 30-minute stability probe with repeated CUDA work and periodic memory/GPU telemetry.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded GB10 worker stability probe
- Success threshold: At least 30 minutes of repeated CUDA smoke workloads with zero device-loss errors, zero failed iterations, no monotonic unbounded memory growth, and all artifacts written successfully.
- Stop condition: Stop immediately on CUDA device loss, repeated workload failure, earlyoom pressure, or projected runtime exceeding the bounded 30-minute stability window.

## Evidence references

- Artifact root: `<local-path>/projects/tier-0-volunteer-worker-liveness-and-capability-probe-3231811523a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
