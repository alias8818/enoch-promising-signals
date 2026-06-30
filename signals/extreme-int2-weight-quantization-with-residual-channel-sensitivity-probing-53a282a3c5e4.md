# Extreme INT2 Weight Quantization with Residual Channel Sensitivity Probing

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `extreme-int2-weight-quantization-with-residual-channel-sensitivity-probing-53a282a3c5e4`
Run ID: `extreme-int2-weight-quantization-with-residual-channel-sensitivity-probing-53a282a3c5e4-20260607T093038571795+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/be9b9f64c67c

## What looked useful

Sensitivity-selected residual channels reduced relative output MSE by 22.8% versus INT2-only and 19.5% versus random on average, but only by 0.23% versus weight-error ranking overall. The advantage over weight-error was concentrated in the activation_anisotropic profile: 0.92% mean and up to 2.50% relative MSE reduction.

## Boundaries and scale limits

No pretrained transformer, real text calibration set, perplexity, packed INT2 kernel, or multi-layer propagation test was run. Evidence is bounded to synthetic layer-output reconstruction on shapes up to 2048x1024.

## Claim scope

In synthetic linear-layer proxies with 1-10% full-precision residual output channels, residual channels reduce INT2 output error substantially versus INT2-only and random selection. Calibration residual sensitivity closely tracks oracle channels, but it only materially improves over per-channel weight-error selection when activation covariance is strongly anisotropic.

## Why it stopped

Proxy evidence is mixed: the mechanism works for residual INT2 channel repair, but the proposed activation-sensitive novelty does not beat the cheap weight-error control except under deliberately anisotropic activations.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded pretrained GPT-2-small-class layer/perplexity follow-up only if direct model evidence is desired.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained GPT-2 INT2 Residual Channel Sensitivity Check
- Success threshold: Sensitivity must improve held-out perplexity or next-token loss and layer-output relative MSE by at least 2% versus weight-error ranking at one or more residual budgets, without losing at other budgets.
- Stop condition: Stop if sensitivity is within +/-1% of weight-error on held-out layer-output MSE and perplexity across tested budgets, because the simpler heuristic is then preferred.

## Evidence references

- Artifact root: `<local-path>/projects/extreme-int2-weight-quantization-with-residual-channel-sensitivity-probing-53a282a3c5e4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
