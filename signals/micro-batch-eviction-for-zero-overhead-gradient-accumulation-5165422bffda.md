# Micro-Batch Eviction for Zero-Overhead Gradient Accumulation

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `micro-batch-eviction-for-zero-overhead-gradient-accumulation-5165422bffda`
Run ID: `micro-batch-eviction-for-zero-overhead-gradient-accumulation-5165422bffda-20260525T012610976500+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/dc70f9f6e915

## What looked useful

Standard immediate-backward gradient accumulation already bounded peak saved activation residency to one micro-batch, while deferred-backward accumulation scaled peak live saved activations linearly with accumulation steps. A saved-tensor eviction/reload proxy preserved gradients but added 11.82% runtime overhead in the calibrated CPU run.

## Boundaries and scale limits

No CUDA/GPU device was available; results do not directly measure accelerator offload, stream overlap, unified-memory behavior, GPT-2-scale training, or multi-node training. The model was a synthetic token MLP, not a full Transformer.

## Claim scope

CPU-worker PyTorch proxy tests of micro-batch saved-activation eviction for gradient accumulation, plus autograd-hook measurement of saved activation residency under immediate-backward and deferred-backward accumulation schedules.

## Why it stopped

Bounded CPU proxy and schedule-residency evidence undermines the zero-overhead claim: the memory issue targeted by eviction is absent in ordinary immediate-backward gradient accumulation, and the eviction proxy has measurable overhead.

## Recommended next action

Stop this run as a no-paper useful negative; only revisit with a direct single-GPU Transformer benchmark that compares against standard immediate-backward gradient accumulation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Single-GPU Transformer Activation Eviction vs Standard Gradient Accumulation
- Success threshold: Eviction must reduce peak GPU memory by at least 25% versus the relevant memory-stressed baseline while keeping throughput within 2% of standard immediate-backward gradient accumulation and preserving gradients within numerical tolerance.
- Stop condition: Stop if standard immediate-backward accumulation already fits the target batch without cross-micro-batch activation residency, or if eviction overhead exceeds 2% throughput loss in two independently repeated GPU runs.

## Evidence references

- Artifact root: `<local-path>/projects/micro-batch-eviction-for-zero-overhead-gradient-accumulation-5165422bffda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
