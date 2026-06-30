# Residual-Channel-Aware QLoRA Finetune for Home Quantization Recovery

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `residual-channel-aware-qlora-finetune-for-home-quantization-recovery-32d49fe1c3b7`
Run ID: `residual-channel-aware-qlora-finetune-for-home-quantization-recovery-32d49fe1c3b7-20260630T010343348242+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cf6e5946a388

## What looked useful

Standard uniform LoRA matched or beat the tested residual-channel-aware variants on total held-out recovery MSE. Residual-weighted loss slightly redirected error toward high-residual channels in one setting but did not improve overall recovery. A rank-matched SVD residual oracle shows low-rank recoverable error remains, motivating only a bounded residual-initialization follow-up.

## Boundaries and scale limits

Not a full QLoRA finetune; no tokenizer, transformer hidden-state distribution, language-model perplexity, downstream task accuracy, or home-serving validation. The result covers simple residual-energy gates and residual-weighted loss, not all residual-aware initialization methods.

## Claim scope

Layer-scale synthetic 4-bit quantization recovery with frozen 512x512 linear weights, Gaussian activations, rank-matched LoRA adapters, five seeds per setting, and held-out output-MSE evaluation.

## Why it stopped

Proxy evidence early-falsifies the tested simple residual-channel-aware gate/loss mechanisms rather than providing full QLoRA validation.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, run a bounded tiny-transformer follow-up comparing uniform LoRA with residual-SVD/LoftQ-style initialization on validation perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual-SVD Initialized LoRA for Tiny Transformer Quantization Recovery
- Success threshold: Residual-initialized LoRA improves validation loss or recovery MSE by at least 2% relative to uniform LoRA at matched trainable parameter count in at least two of three seeds without worse final perplexity.
- Stop condition: Stop if residual initialization fails to beat uniform LoRA by 2% relative on validation loss/recovery MSE, is unstable in more than one seed, or requires longer than the bounded local budget without checkpointed signal.

## Evidence references

- Artifact root: `<local-path>/projects/residual-channel-aware-qlora-finetune-for-home-quantization-recovery-32d49fe1c3b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
