# Outlier-Channel Residual: FP16 for High-Variance Activation Channels at 2-bit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `outlier-channel-residual-fp16-for-high-variance-activation-channels-at-2-bit-023d78bcac1a`
Run ID: `outlier-channel-residual-fp16-for-high-variance-activation-channels-at-2-bit-023d78bcac1a-20260528T102153376612+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b81ac000324e

## What looked useful

High-variance FP16 residual channels sharply reduced 2-bit error when outliers were persistent by channel: synthetic persistent-channel output rel MSE ratio was 0.0124 versus all-2-bit and 0.0130 versus same-fraction random. On distilgpt2 final hidden states, 5% high-variance FP16 residual channels reduced LM-head logit rel MSE from 0.6199 to 0.000371, while 5% random residual remained 0.5573. Gaussian, Student-t, and token-sparse controls showed little advantage over random residuals.

## Boundaries and scale limits

Synthetic tensor regimes plus one pretrained distilgpt2 final-hidden-state probe with 1088 calibration tokens and 1088 held-out tokens. No intermediate-layer injection, no perplexity evaluation, no multi-model robustness, no packed 2-bit kernel throughput, and no storage/index overhead beyond simple effective bits per activation.

## Claim scope

Bounded evidence supports FP16 residuals for calibrated high-variance activation channels as a way to reduce 2-bit activation reconstruction and downstream linear/logit error when outliers are persistent by channel. Evidence includes synthetic controls and a distilgpt2 final-hidden LM-head probe, not end-to-end perplexity or deployment kernels.

## Why it stopped

No-paper closure: the local evidence supports the mechanism as a useful signal, but it is not full validation because end-to-end model quality, layerwise robustness, and deployment overhead were not measured.

## Recommended next action

Run a bounded layerwise transformer follow-up that injects quantized/residual activations during forward passes and measures perplexity/logit KL against same-budget random, 3-bit/4-bit, and activation-smoothing baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Layerwise perplexity validation for high-variance FP16 residual activation channels
- Success threshold: At <=2.7 effective bits per activation excluding index overhead, high-variance residuals reduce logit KL or perplexity degradation by at least 2x versus all-2-bit and same-budget random residuals on held-out data for most tested layers/models, without worse memory-bandwidth cost than a plausible 3-bit or 4-bit alternative.
- Stop condition: Stop if high-variance residuals fail to beat same-budget random residuals on held-out perplexity/logit KL in the first two real-model layerwise tests, or if index/residual overhead makes the method dominated by a simpler 3-bit or 4-bit baseline.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-channel-residual-fp16-for-high-variance-activation-channels-at-2-bit-023d78bcac1a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
