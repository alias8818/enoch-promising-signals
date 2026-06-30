# Stochastic 4-bit Gradient Quantization for VRAM Reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `stochastic-4-bit-gradient-quantization-for-vram-reduction-39d2bfc0b308`
Run ID: `stochastic-4-bit-gradient-quantization-for-vram-reduction-39d2bfc0b308-20260522T131544400055+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/afd07c8c9072

## What looked useful

The storage mechanism is promising for persistent gradient accumulation memory, but the practical peak-VRAM claim is not supported by this naive implementation. Future work should target a fused accumulator before scaling model training.

## Boundaries and scale limits

The run did not test GPT-2-small, real language data, long convergence, mixed-precision transformer training, distributed training, or a fused CUDA/Triton accumulator. The unfused PyTorch prototype increased measured peak allocation by 132.4712 MB because it materialized full-size transient tensors during dequantization/requantization.

## Claim scope

On a GB10 GPU using a parameter-heavy synthetic MLP with 8-step microbatch accumulation, GPU-resident stochastic blockwise int4 gradient storage reduced persistent stored-gradient memory from 258.2579 MB to 33.2912 MB and reduced post-backward allocated memory by 224.9575 MB, while an 80-step synthetic AdamW probe over three seeds showed near-zero final-loss delta.

## Why it stopped

Mixed bounded result: persistent gradient storage improved substantially, but peak VRAM did not improve in the unfused prototype and quality evidence was synthetic/short-horizon only.

## Recommended next action

Stop this run as no-paper useful signal; implement a fused CUDA/Triton int4 gradient accumulator and rerun the same memory test before attempting GPT-2-small-class convergence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused stochastic int4 gradient accumulator for peak VRAM reduction
- Success threshold: At least 30% lower measured CUDA peak allocation than fp32 accumulation on the parameter-heavy workload, no more than 1% validation-loss regression in the bounded transformer probe, and no more than 10% throughput penalty.
- Stop condition: Stop if the fused implementation cannot reduce measured CUDA peak allocation versus fp32 accumulation or if bounded transformer validation loss regresses by more than 1%.

## Evidence references

- Artifact root: `<local-path>/projects/stochastic-4-bit-gradient-quantization-for-vram-reduction-39d2bfc0b308`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
