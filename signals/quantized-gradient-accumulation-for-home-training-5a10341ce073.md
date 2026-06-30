# Quantized gradient accumulation for home training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantized-gradient-accumulation-for-home-training-5a10341ce073`
Run ID: `quantized-gradient-accumulation-for-home-training-5a10341ce073-20260611T024142834994+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/79b0409ff79c

## What looked useful

Across four linear-task seeds, int8 accumulation had mean gradient cosine 0.99893 versus FP32, mean relative gradient error 0.0458, mean validation-loss delta 0.000161, mean accuracy delta -0.000122, and 0.25024x FP32 persistent accumulator memory. A larger MLP diagnostic showed 0.0318 relative gradient error and 0.999694 cosine with negligible validation deltas, but little learning in the short run.

## Boundaries and scale limits

Synthetic data only; no real language-model trainer, no AdamW or mixed-precision optimizer stack, no packed quantized kernels, no activation-checkpointing interaction, no out-of-memory boundary demonstration, and no long-run stability test.

## Claim scope

In a bounded CUDA PyTorch prototype on synthetic MLP and linear classification tasks, per-tensor int8 gradient accumulation approximated FP32 accumulation closely and preserved short-run learning while reducing persistent accumulator storage to about 25% of FP32.

## Why it stopped

Closed as no-paper useful signal: the evidence is direct for synthetic accumulation and short learning, but proxy-only for home LLM training and not a production trainer validation.

## Recommended next action

Run a bounded follow-up integrating int8 accumulation into a small transformer or GPT-2-small-class trainer with AdamW, mixed precision, activation checkpointing, and measured peak memory at the largest fitting batch sizes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Quantized accumulation in a small transformer trainer
- Success threshold: Validation loss within 1% of FP32 accumulation and either at least 20% measured peak-memory reduction or a larger fitting batch/effective batch under the same memory limit.
- Stop condition: Stop if the transformer run shows more than 3% validation-loss degradation at matched steps, no measured peak-memory improvement, or quantization overhead makes throughput less than 70% of FP32 without enabling a larger batch.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-gradient-accumulation-for-home-training-5a10341ce073`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
