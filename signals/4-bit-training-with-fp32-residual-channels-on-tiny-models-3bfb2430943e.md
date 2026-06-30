# 4-bit Training with FP32 Residual Channels on Tiny Models

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-training-with-fp32-residual-channels-on-tiny-models-3bfb2430943e`
Run ID: `4-bit-training-with-fp32-residual-channels-on-tiny-models-3bfb2430943e-20260608T064706951164+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e2b1eb0a4bf6

## What looked useful

Full q4 fake quantization was only +0.00149 validation loss worse than FP32, while q4 with 12.5% FP32 residual channels was only 0.00033 better than all-q4, far below the roughly 0.003 cross-seed standard deviation. The mechanism did not show a measurable benefit in this bounded tiny setting.

## Boundaries and scale limits

This run used synthetic data, tiny models, FP32 master weights, straight-through fake quantization, and no real int4 kernels, activation quantization, optimizer-state quantization, natural-language corpus, GPT-2-small-class baseline, or long training horizon.

## Claim scope

On a 2-layer width-128 tiny autoregressive transformer trained for 400 steps on deterministic synthetic Markov-token data, symmetric per-row signed-int4 fake-quantized linear weights trained nearly identically to FP32, and keeping 12.5% output channels in FP32 did not produce a meaningful validation-loss gain over all-q4 fake quantization.

## Why it stopped

Bounded tiny synthetic fake-quant evidence found no meaningful residual-channel benefit; this is a scoped early negative/useful signal rather than full validation.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should add a harder quantization bottleneck, such as activation or optimizer-state quantization on a real text corpus, before spending larger-scale compute.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Residual FP32 Channels Under Activation Quantization on Real Tiny Text
- Success threshold: q4_residual must reduce the all-q4 validation-loss degradation versus FP32 by at least 25% across 3 seeds without worse instability and with documented memory/throughput tradeoffs.
- Stop condition: Stop if all-q4 again remains within 0.5% validation loss of FP32 or q4_residual improves all-q4 by less than one cross-seed standard deviation.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-training-with-fp32-residual-channels-on-tiny-models-3bfb2430943e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
