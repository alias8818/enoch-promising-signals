# Saliency-guided residual channels for 2-bit activations

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `saliency-guided-residual-channels-for-2-bit-activations-3fa21a0fc966`
Run ID: `saliency-guided-residual-channels-for-2-bit-activations-3fa21a0fc966-20260522T185047444365+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c268c71efb9e

## What looked useful

2-bit activation quantization reduced mean accuracy from 0.9820 to 0.8411. Residual-aware saliency recovered only 0.0343 accuracy at a 20% residual budget, below variance at 0.0674, mean_abs at 0.0789, and random_mean at 0.0522; the single-channel diagnostic had mean Spearman correlation -0.1033.

## Boundaries and scale limits

Small synthetic classification task, 128-channel MLP, post-training inference quantization only; no transformer, language-model, vision-benchmark, training-time quantization, or hardware-kernel validation.

## Claim scope

In a 5-seed synthetic teacher/student MLP proxy with post-training 2-bit ReLU activation quantization, saliency-guided residual channel selection did not outperform simple activation-statistic controls, though residual channels themselves recovered some accuracy.

## Why it stopped

Proxy/local evidence did not support the saliency selector mechanism and is insufficient for a paper-positive claim.

## Recommended next action

Stop this run as a proxy early falsification of saliency-guided channel choice; only revisit if a direct GPT-2-small-class or real benchmark test beats variance, mean-activation, and random controls at matched residual budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small-class residual channel selector comparison for 2-bit activations
- Success threshold: Residual-aware saliency must beat the best simple statistic control by at least 10% relative recovery of quantization-induced NLL/perplexity loss at two or more budgets, without losing accuracy.
- Stop condition: Stop as negative if residual-aware saliency fails to beat variance or mean-activation controls on the primary metric at matched budgets.

## Evidence references

- Artifact root: `<local-path>/projects/saliency-guided-residual-channels-for-2-bit-activations-3fa21a0fc966`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
