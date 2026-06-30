# GPT-2-small-class real-batch validation of bucketed gradient accumulation

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `83`
Project ID: `gpt-2-small-class-real-batch-validation-of-bucketed-gradie-c2910580ea`
Run ID: `gpt-2-small-class-real-batch-validation-of-bucketed-gradie-c2910580ea-20260612T224832030535+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `83`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Gradient Accumulation Bucket Batching for CPU-Constrained Training: enoch://control-plane/projects/gradient-accumulation-bucket-batching-for-cpu-constrained-training-2639791b6654/runs/gradient-accumulation-bucket-batching-for-cpu-constrained-training-2639791b6654-20260611T153930021055+0000
- Parent run decision: PyTorch Transformer Validation of Bucketed Gradient Accumulation: enoch://control-plane/projects/pytorch-transformer-validation-of-bucketed-gradient-accumu-ddc6f56828/runs/pytorch-transformer-validation-of-bucketed-gradient-accumu-ddc6f56828-20260612T213002948208+0000

## What looked useful

Across seeds 17, 31, and 43, bucketed-vs-real gradient max absolute difference was <=4.17e-7, 20-step loss trace max absolute difference was <=1.53e-5, and bucketed padding ratio was reduced by 32.6% on average. The wrong per-bucket-mean ablation diverged with gradient max absolute differences of 0.0488-0.0651.

## Boundaries and scale limits

Not full GPT-2-small 124M scale; not a real text corpus; CPU-only fp32; no dropout, AMP, fused kernels, distributed training, or long-run perplexity validation.

## Claim scope

For a 1.07M-parameter GPT-2-style causal decoder on deterministic variable-length language-modeling batches, correctly token-normalized bucketed gradient accumulation reproduced the padded real-batch gradient/update trajectory to floating-point tolerance while reducing padded-token work.

## Why it stopped

Bounded Tier-2 mechanism support was achieved, but evidence is not publication-grade because it used a 1.07M-parameter GPT-style model and synthetic deterministic batches rather than full GPT-2-small real-corpus training.

## Recommended next action

Stop this worker run as no-paper useful evidence; the next validation should replicate the same real-batch, bucketed, and wrong-scaling controls on full GPT-2-small with real corpus batches and GPU/mixed-precision settings.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/gpt-2-small-class-real-batch-validation-of-bucketed-gradie-c2910580ea`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
