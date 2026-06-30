# Adaptive Per-Head Four-Bit KV Quantization for Local Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-per-head-four-bit-kv-quantization-for-local-inference-3d675cacc4da`
Run ID: `adaptive-per-head-four-bit-kv-quantization-for-local-inference-3d675cacc4da-20260607T162558679870+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/94ace52d2eee

## What looked useful

Adaptive per-head percentile selection reduced relative RMSE versus per-head max-abs by 11.3% to 35.2% across four synthetic cases, including head-variance and rare-outlier distributions, at about 0.25x fp16 KV storage. Unoptimized quantize/dequantize plus attention was 25.7x to 33.9x slower than fp16, so the mechanism is accuracy/storage-promising but not an inference-speed result.

## Boundaries and scale limits

No real model KV traces, no perplexity/logit quality evaluation, no 7B+ model, and no fused int4 KV attention kernel. Runtime measurements are for an unoptimized PyTorch path that materializes dequantized fp16 K/V.

## Claim scope

Synthetic decode-attention tensors on NVIDIA GB10 show calibrated adaptive per-head 4-bit KV quantization can reduce fp16 attention-output error versus per-head max-abs 4-bit while preserving an approximately 25% KV-cache storage footprint.

## Why it stopped

No-paper useful signal: the current evidence is synthetic and the tested implementation is an unoptimized proxy, not a production local-inference validation.

## Recommended next action

Run a bounded real-KV follow-up on a GPT-2-small-class decoder and require both logit/perplexity tolerance and a packed-cache or fused-kernel timing path before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-KV Adaptive Per-Head 4-bit Quantization on GPT-2-small-class Decode
- Success threshold: Adaptive per-head 4-bit must reduce held-out logit MSE by at least 15% versus per-head max-abs 4-bit while keeping perplexity increase under 3% versus fp16 and maintaining approximately 0.25x fp16 KV storage.
- Stop condition: Stop if adaptive per-head 4-bit fails to improve held-out logit MSE by 10% versus per-head max-abs or if perplexity increases by more than 5% versus fp16.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-per-head-four-bit-kv-quantization-for-local-inference-3d675cacc4da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
