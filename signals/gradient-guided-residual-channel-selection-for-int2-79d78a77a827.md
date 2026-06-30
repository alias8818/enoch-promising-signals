# Gradient-Guided Residual Channel Selection for INT2

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-guided-residual-channel-selection-for-int2-79d78a77a827`
Run ID: `gradient-guided-residual-channel-selection-for-int2-79d78a77a827-20260531T184710893977+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/73c418be7b36

## What looked useful

On 8 GB10 PyTorch CUDA seeds, all-INT2 reduced mean test accuracy from 0.7699 to 0.6723 and raised loss from 1.4665 to 3.7851. Gradient-error residual selection reduced mean INT2 loss by 0.454 to 1.316 across budgets of 1 to 32 channels per layer and usually beat random, weight norm, weight-error norm, and activation norm on loss. Accuracy recovery was smaller and not consistently best versus baselines.

## Boundaries and scale limits

No real pretrained transformer, no natural dataset, no GPT-2-small-class baseline, no real INT2 mixed residual kernel, no throughput/latency measurement, and only 8 random seeds at toy MLP scale.

## Claim scope

Synthetic teacher-generated MLP classification with simulated row-wise weight-only INT2 quantization and per-layer full-precision residual output channels. Gradient-guided residual selection improves cross-entropy recovery versus all-INT2 and most simple heuristics, but accuracy gains are modest and noisy.

## Why it stopped

This run produced a useful synthetic mechanism signal but not direct publication-grade evidence; the result is a proxy/local confirmation, not full validation.

## Recommended next action

Run a bounded direct follow-up on a small real pretrained transformer with real calibration/evaluation data before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gradient-Guided INT2 Residual Channels on a Small Real Transformer
- Success threshold: Gradient-error selection should reduce validation loss or perplexity by at least 5% more than the best non-gradient baseline at two or more practical residual budgets without worse accuracy/task metrics, and overhead must remain plausibly below the quality gain tradeoff.
- Stop condition: Stop if gradient-error is not better than gradient-only or weight-error selection on validation loss at two practical budgets, or if residual-channel overhead eliminates the expected INT2 efficiency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-guided-residual-channel-selection-for-int2-79d78a77a827`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
