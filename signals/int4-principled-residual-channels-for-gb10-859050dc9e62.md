# INT4 + Principled Residual Channels for GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-principled-residual-channels-for-gb10-859050dc9e62`
Run ID: `int4-principled-residual-channels-for-gb10-859050dc9e62-20260608T171403658822+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a7a5ca60e240

## What looked useful

At batch=1024, in=4096, out=4096, group size=64, 2% residual channels selected by activation RMS times quantization-error RMS reduced INT4 relative MSE by 48.9% on outlier_channels and 50.3% on mixed_tail, versus 1.17% and 1.26% for random residual channels at the same effective 4.49 bits/weight. On gaussian data the selector reduced error by only 2.22%, similar to random at 2.03%.

## Boundaries and scale limits

No production packed-INT4 kernel, no real transformer calibration activations, no perplexity/task metric, no training or fine-tuning run, and no large-model validation. Matmul throughput is fp16/dequantized proxy throughput only.

## Claim scope

Synthetic GB10 CUDA tensor probe of groupwise INT4 linear weight quantization with small fp16 residual input-channel sets. The activation_weight_error selector strongly reduces output relative MSE on heavy-tailed channel distributions and is near-random on iid gaussian controls.

## Why it stopped

Synthetic proxy evidence supports a mechanism under heavy-tailed channel structure but does not provide direct real-model or production-kernel validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same selector on GPT-2-small-class real transformer layers with calibration activations and perplexity/error metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Transformer Calibration Test for INT4 Residual Channels
- Success threshold: At 2% residual channels, activation_weight_error improves perplexity degradation by at least 25% relative to vanilla INT4 and beats random residual channels by at least 15 percentage points at equal effective bits/weight on at least two representative layer groups.
- Stop condition: Stop if activation_weight_error is within 5 percentage points of random residual channels at 1%, 2%, and 4% budgets, or if real-layer calibration shows no concentrated channel error structure.

## Evidence references

- Artifact root: `<local-path>/projects/int4-principled-residual-channels-for-gb10-859050dc9e62`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
