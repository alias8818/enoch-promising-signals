# Quantized LoRA with Activation-Aware Scaling

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `quantized-lora-with-activation-aware-scaling-c79b3fc238f5`
Run ID: `quantized-lora-with-activation-aware-scaling-c79b3fc238f5-20260522T182128468090+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2912fd585656

## What looked useful

Row/column factor quantization showed only 0.028% mean reduction in added error despite 9/10 wins, while per-tensor factor quantization showed 4.46% mean reduction with 7/10 wins and high variance. The mechanism may matter only when quantization granularity exposes rank-channel scale imbalance.

## Boundaries and scale limits

No transformer, tokenizer, real dataset, language modeling objective, production groupwise quantizer, or 7B-class/full QLoRA training was tested; all evidence is from 10-trial synthetic CUDA runs at 512x512 scale plus one smoke run.

## Claim scope

Synthetic frozen-linear LoRA adaptation with anisotropic activations: activation-aware rank rescaling before 4-bit factor quantization is nearly inert with row/column factor scales but can reduce quantization-induced MSE under harsher per-tensor factor quantization.

## Why it stopped

Current evidence is a synthetic/proxy useful signal with mixed effect size, not direct publication-grade validation of quantized LoRA for real models.

## Recommended next action

Run a bounded real-transformer follow-up on GPT-2-small-class LoRA modules using real calibration hidden states and realistic groupwise quantizers before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-transformer activation-aware scaling for quantized LoRA modules
- Success threshold: At least 2% relative reduction in quantization-induced validation loss or adapter-output MSE versus the strongest realistic quantization baseline, with wins in at least 4/5 seeds or module/task settings.
- Stop condition: Stop if the best calibrated scaling improves the strongest realistic quantization baseline by less than 1% on average or loses in more than half of tested module/task settings.

## Evidence references

- Artifact root: `<local-path>/projects/quantized-lora-with-activation-aware-scaling-c79b3fc238f5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
