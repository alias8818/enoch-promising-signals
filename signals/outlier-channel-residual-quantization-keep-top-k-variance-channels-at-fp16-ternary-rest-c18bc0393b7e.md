# Outlier-Channel Residual Quantization: Keep Top-k Variance Channels at FP16, Ternary Rest

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `outlier-channel-residual-quantization-keep-top-k-variance-channels-at-fp16-ternary-rest-c18bc0393b7e`
Run ID: `outlier-channel-residual-quantization-keep-top-k-variance-channels-at-fp16-ternary-rest-c18bc0393b7e-20260529T094251181024+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ccfb7d53fa1b

## What looked useful

Variance/L2 channel retention captures planted outliers and reduces reconstruction error, but the simple post-training method still raises distilgpt2 perplexity from 74.72 to at best 6616.96, so it is not paper-ready or practically viable in this form.

## Boundaries and scale limits

Tested synthetic 512x512 matrices and distilgpt2 WikiText-2 perplexity probes up to 25% FP16 internal output-channel retention; did not test quantization-aware training, activation/Hessian selectors, production kernels, larger LMs, or long calibration corpora.

## Claim scope

Early local evidence for post-training GPT-2-family internal-layer quantization: keeping top weight-variance output channels in FP16 while ternary-quantizing the rest improves over all-ternary on synthetic outliers and small LM probes, but remains far from usable perplexity on distilgpt2.

## Why it stopped

Proxy plus bounded real-LM evidence falsified the simple post-training form: synthetic reconstruction improves, but corrected distilgpt2 perplexity remains orders of magnitude above baseline, so this is not a full validation and not paper-positive.

## Recommended next action

Stop this project as an early negative for the simple weight-variance selector; if continuing, run a bounded activation-variance or sensitivity-aware selector with per-layer scale calibration and require perplexity below 2x baseline at no more than 25% FP16 internal channels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-Sensitivity Channel Selection for FP16-plus-Ternary Residual Quantization
- Success threshold: Perplexity below 2x the unquantized baseline with no more than 25% FP16 internal output channels, and statistically consistent improvement over random same-budget retention.
- Stop condition: Stop if activation/sensitivity selection still exceeds 2x baseline perplexity at 25% FP16 channels or fails to beat random same-budget retention.

## Evidence references

- Artifact root: `<local-path>/projects/outlier-channel-residual-quantization-keep-top-k-variance-channels-at-fp16-ternary-rest-c18bc039`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
