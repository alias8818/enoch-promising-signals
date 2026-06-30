# 1-bit weights plus residual channels for GPT-2-small inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `1-bit-weights-plus-residual-channels-for-gpt-2-small-inference-72fd1b7bcbf3`
Run ID: `1-bit-weights-plus-residual-channels-for-gpt-2-small-inference-72fd1b7bcbf3-20260522T184046496262+0000`

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

Pure 1-bit raised perplexity from 162.0 to 63296.5; the best residual-channel setting was 2% residual channels at about 1.61 approximate bits per quantized weight, but still had perplexity 31994.0, or 197.5x dense. Larger residual fractions did not recover monotonically.

## Boundaries and scale limits

Evaluated 3072 tokens from embedded technical prose on pretrained GPT-2-small using CUDA on GB10. This did not use a standard benchmark corpus, quantization-aware training, learned residual selection, activation calibration, bit-packed kernels, or production serving measurements.

## Claim scope

A simple post-training GPT-2-small scheme that replaces quantizable Conv1D/Linear weights with per-output-channel 1-bit sign-scale weights plus fixed residual output channels selected by quantization error does not preserve inference quality on a deterministic local next-token perplexity probe.

## Why it stopped

Early falsification on direct GPT-2-small inference quality, with proxy limitations around corpus size and kernel/storage realism rather than a full benchmark validation.

## Recommended next action

Stop this mechanism as a paper path; only revisit with a bounded calibrated-residual follow-up that tests a standard validation set and requires a clear perplexity recovery threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Calibrated residual-channel selection for post-training GPT-2-small 1-bit quantization
- Success threshold: At 10% or fewer residual channels, calibrated selection achieves no more than 2x dense perplexity on the chosen standard validation subset and improves NLL by at least 50% relative to pure 1-bit.
- Stop condition: Stop if the best calibrated 10% residual variant remains above 2x dense perplexity or if recovery is not better than the global quantization-error residual baseline.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-weights-plus-residual-channels-for-gpt-2-small-inference-72fd1b7bcbf3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
