# Micro-batch VRAM-Adaptive Gradient Accumulation for Home Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `micro-batch-vram-adaptive-gradient-accumulation-for-home-training-0ea10ae9d6c9`
Run ID: `micro-batch-vram-adaptive-gradient-accumulation-for-home-training-0ea10ae9d6c9-20260524T005309940394+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d71a8a620cd6

## What looked useful

Adaptive micro-batch sizing is a plausible home-training throughput mechanism when sequence lengths create variable activation memory pressure. Sparse calibration was unsafe, but exact sequence-length calibration avoided violations and preserved update coverage while fixed aggressive skipped 40% of updates.

## Boundaries and scale limits

Synthetic data, toy model, 30 optimizer-update stress run, artificial memory cap rather than physical OOM, no convergence claim, no GPT-2-small-class or larger workload, and no comparison against production trainer memory techniques beyond fixed micro-batch controls.

## Claim scope

On a toy CUDA Transformer workload on NVIDIA GB10 with synthetic variable-length token batches and an artificial 900 MB PyTorch allocator cap, exact-bucket calibrated adaptive micro-batching with gradient accumulation completed all planned updates, avoided cap violations, and improved tokens/sec by 30.6% versus a conservative fixed micro-batch baseline.

## Why it stopped

Bounded toy CUDA evidence supports the mechanism but is not a full validation or paper-ready result.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should repeat the controller on a real small LM fine-tuning workload with real dataset batches and physical high-water memory pressure.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Micro-batch Gradient Accumulation on Real Small-LM Fine-tuning
- Success threshold: Adaptive achieves at least 15% higher tokens/sec than the safe fixed baseline, completes at least 95% of planned updates, and has no unrecovered OOMs while preserving comparable loss trajectory over the measured window.
- Stop condition: Stop if adaptive cannot beat the safe fixed baseline by 10%, causes unrecovered OOMs, or requires calibration overhead that erases throughput gains.

## Evidence references

- Artifact root: `<local-path>/projects/micro-batch-vram-adaptive-gradient-accumulation-for-home-training-0ea10ae9d6c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
