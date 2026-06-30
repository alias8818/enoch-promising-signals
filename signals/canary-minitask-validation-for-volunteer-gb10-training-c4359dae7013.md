# Canary-MiniTask Validation for Volunteer GB10 Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `canary-minitask-validation-for-volunteer-gb10-training-c4359dae7013`
Run ID: `canary-minitask-validation-for-volunteer-gb10-training-c4359dae7013-20260612T232441057400+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3474a9ab489f

## What looked useful

PyTorch 2.12.0+cu130 selected CUDA on NVIDIA GB10, trained a 3.26M-parameter bf16 causal Transformer, reduced eval loss from 5.0234 to 0.0416, sustained about 687,793 tokens/s after warmup, showed 92-93% SM utilization in nvidia-smi dmon during calibration, and kept MemAvailable stable around 114.9 GiB with swap disabled.

## Boundaries and scale limits

Tested only a 3.26M-parameter synthetic next-token Transformer for 1000 optimizer steps over about 12 seconds; not evidence for large-model, real-dataset, multi-hour, checkpoint/restart, distributed, or datacenter-scale training.

## Claim scope

Bounded canary validation that this volunteer GB10 worker can run and measure a short PyTorch CUDA mini-training workload with loss reduction, sustained GPU activity, and stable MemAvailable telemetry.

## Why it stopped

The canary directly validated the local mini-training path, but the evidence is synthetic and short-duration, so it is insufficient for paper-positive or full volunteer-training validation claims.

## Recommended next action

Stop this canary as no-paper useful signal; the next validation should run a bounded real-dataset training job with checkpoint/resume and at least 30 minutes of telemetry on the same GB10 class.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bounded Real-Workload GB10 Training Stability Check
- Success threshold: Complete at least 30 minutes of real workload training with checkpoint/resume, no process/runtime failure, MemAvailable remaining above 20 GiB, sustained GPU utilization above 50% outside data-loading gaps, and post-resume loss within 10% of pre-resume trend.
- Stop condition: Stop early if CUDA/PyTorch errors occur, MemAvailable falls below 20 GiB, utilization remains below 30% for 10 consecutive minutes due to host bottlenecks, checkpoint/resume fails, or loss diverges after resume.

## Evidence references

- Artifact root: `<local-path>/projects/canary-minitask-validation-for-volunteer-gb10-training-c4359dae7013`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
