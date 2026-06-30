# Ternary weight residual channel for GPT-2-small

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `ternary-weight-residual-channel-for-gpt-2-small-5642ee9d27df`
Run ID: `ternary-weight-residual-channel-for-gpt-2-small-5642ee9d27df-20260522T115509501324+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4286aa1c5b71

## What looked useful

Dense GPT-2-small reached perplexity 33.972 on the 8,176-token confirmation. Optimized per-row ternary rank-0 reached 12,808.209 perplexity, rank-1 reached 7,728.205, and rank-4 reached 5,326.791, still 156.8x worse than dense. Rank-16 sensitivity on 4,088 tokens remained 203.8x worse than dense while reducing estimated compression to 6.504x fp16.

## Boundaries and scale limits

Evaluated pretrained Hugging Face gpt2 on 1,020-token smoke, 8,176-token bounded confirmation, and 4,088-token rank-16 sensitivity windows from WikiText-2 test text. This did not train or fine-tune the ternary/residual representation, did not quantize embeddings, did not evaluate full-corpus perplexity, and did not implement compressed inference kernels.

## Claim scope

Post-training replacement of GPT-2-small projection matrices with per-output ternary weights plus small low-rank residual channels is not viable for preserving language-model perplexity on bounded WikiText-2 evaluation.

## Why it stopped

Bounded direct GPT-2-small post-training evaluation was strongly negative; this is not a full validation of training-time variants, but it falsifies the cheap ternary-plus-small-residual-channel route as paper-worthy.

## Recommended next action

Stop this post-training formulation; only revisit as a separate quantization-aware training experiment with a direct perplexity threshold and storage/runtime accounting.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weight-residual-channel-for-gpt-2-small-5642ee9d27df`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
