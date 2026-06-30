# 8-bit AdamW CPU Pretraining for GPT-2-small

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-adamw-cpu-pretraining-for-gpt-2-small-349689f6e362`
Run ID: `8-bit-adamw-cpu-pretraining-for-gpt-2-small-349689f6e362-20260525T131701068390+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ee1b9b06ebf8

## What looked useful

8-bit CPU AdamW has a real optimizer-state memory benefit at GPT-2-small scale, but naive PyTorch quantize/dequantize overhead and second-moment quantization sensitivity make it insufficient as a practical CPU pretraining result without kernel and stability work.

## Boundaries and scale limits

No full GPT-2-small forward/backward, real-token pretraining, validation perplexity, long-horizon stability, or optimized CPU kernel was tested. The GPT-2-small result is optimizer-state/step-only with random gradients.

## Claim scope

On a CPU-only worker, a transparent blockwise uint8 AdamW implementation reduced GPT-2-small-shaped optimizer state from 949.40 MiB to 252.18 MiB and preserved tiny repeated-batch loss movement at lr=1e-5, but the target-scale optimizer step was 6.11x slower than PyTorch fp32 AdamW.

## Why it stopped

Useful no-paper signal: bounded local evidence supports memory reduction but not a full CPU-pretraining viability claim.

## Recommended next action

Do not write a paper from this run; next run should test a kernelized or fused CPU 8-bit AdamW on a short real-token GPT-2-small training slice and require near-fp32 optimizer-step time before scaling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Kernelized CPU 8-bit AdamW on a Real GPT-2-small Training Slice
- Success threshold: At least 3x optimizer-state memory reduction, optimizer-step time no worse than 1.5x fp32 AdamW, and validation loss within 2% of fp32 AdamW over the bounded slice.
- Stop condition: Stop if a fused/kernelized implementation remains slower than 2x fp32 AdamW or shows repeated loss instability under reasonable learning-rate/block-size settings.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-adamw-cpu-pretraining-for-gpt-2-small-349689f6e362`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
