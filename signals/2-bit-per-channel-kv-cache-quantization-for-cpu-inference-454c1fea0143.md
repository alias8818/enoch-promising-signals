# 2-bit per-channel KV cache quantization for CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-per-channel-kv-cache-quantization-for-cpu-inference-454c1fea0143`
Run ID: `2-bit-per-channel-kv-cache-quantization-for-cpu-inference-454c1fea0143-20260528T135213252148+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c8ad9af5b056

## What looked useful

Packed 2-bit per-channel KV reduced cache storage by about 15-16x including scales and improved median long-context decode latency in the prototype at seq 2048 and 8192, but naive 2-bit quantization badly distorted attention outputs with median relative L2 above 1.0 and cosine near 0.51 at seq 8192.

## Boundaries and scale limits

No real transformer model, tokenizer, perplexity, generation-quality, or production optimized AVX512 kernel was tested; results are not a full validation for deployed LLM inference.

## Claim scope

Synthetic CPU decode-attention microbenchmark with Gaussian Q/K/V, heads=8, head_dim=128, sequence lengths 512-8192, comparing fp32 KV cache against naive packed 2-bit per-channel min/max quantized K and V.

## Why it stopped

This is a proxy synthetic early falsification of naive full-cache 2-bit per-channel min/max K/V quantization, not a full model validation; the observed fidelity loss is too high for a paper-ready or deployable result as tested.

## Recommended next action

Run a bounded real-model follow-up testing hybrid 2-bit KV with an unquantized recent-token residual window and calibrated clipping, measuring both decode latency and perplexity before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model hybrid 2-bit KV cache with residual recent window
- Success threshold: At context length at least 2048, achieve at least 1.5x decode latency improvement or at least 4x KV memory reduction while keeping perplexity degradation within 5% of the fp32/fp16 KV baseline.
- Stop condition: Stop if all tested residual-window and calibration settings either degrade perplexity by more than 15% or fail to beat the fp32/fp16 baseline latency at context length 2048.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-per-channel-kv-cache-quantization-for-cpu-inference-454c1fea0143`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
