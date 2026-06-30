# Real-transformer activation-aware scaling for quantized LoRA modules

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-transformer-activation-aware-scaling-for-quantized-lo-f136647a5b`
Run ID: `real-transformer-activation-aware-scaling-for-quantized-lo-f136647a5b-20260522T213802385703+0000`

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

- Parent run decision: Quantized LoRA with Activation-Aware Scaling: enoch://control-plane/projects/quantized-lora-with-activation-aware-scaling-c79b3fc238f5/runs/quantized-lora-with-activation-aware-scaling-c79b3fc238f5-20260522T182128468090+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2912fd585656

## What looked useful

The 220-step controlled run won 3/3 seeds but improved mean final validation loss by only 0.00215 nats, below the predeclared >=0.02 threshold. A bounded 50-step diagnostic won 5/5 seeds with mean validation loss improvement 0.0757 nats, suggesting activation-aware scaling mainly helps early sample efficiency rather than converged quality on this task.

## Boundaries and scale limits

Tested only a 4-layer width-96 synthetic-language Transformer with PyTorch simulated 4-bit per-row quantized weights, 3 seeds for the 220-step controlled run, and 5 seeds for the 50-step early-adaptation diagnostic. Not validated on natural-language corpora, GPT-2-small-class models, production int4 kernels, 7B+ models, or long finetuning.

## Claim scope

In a tiny causal Transformer with frozen simulated 4-bit quantized linear modules and LoRA adapters on a deterministic shifted language task, activation-aware per-module LoRA scaling improved early adaptation versus fixed alpha/r scaling, but only produced a very small converged final validation loss improvement.

## Why it stopped

No-paper closure: the controlled small direct test produced a useful early-adaptation signal, but missed the predeclared converged final-loss threshold and remains too small/synthetic for publication-grade evidence.

## Recommended next action

Run a preregistered medium direct test on a harder GPT-2-small-class or real text finetuning task with production-relevant quantization and explicit thresholds for early sample efficiency and final perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium GPT-2-small-class activation-aware LoRA scaling test
- Success threshold: Activation-aware scaling improves early validation perplexity or loss by at least 5% or >=0.05 nats at a fixed small update budget in >=4/5 seeds, and final validation perplexity is not worse than fixed scaling by more than 1%.
- Stop condition: Stop if activation-aware scaling fails to improve early validation loss in at least 3/5 seeds, causes instability/NaNs, or final validation perplexity is worse than fixed scaling by more than 1%.

## Evidence references

- Artifact root: `<local-path>/projects/real-transformer-activation-aware-scaling-for-quantized-lo-f136647a5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
