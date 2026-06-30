# 4-bit Groupwise KV-Cache for 4K Context Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-groupwise-kv-cache-for-4k-context-inference-453e33742ca3`
Run ID: `4-bit-groupwise-kv-cache-for-4k-context-inference-453e33742ca3-20260528T235220973065+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e74519f2f76a

## What looked useful

The storage format gives the expected KV memory reduction and tolerable synthetic output distortion, but materializing dequantized K/V each decode step dominates runtime and makes the naive implementation latency-negative.

## Boundaries and scale limits

Synthetic tensors only; no full model, perplexity, real generation, serving scheduler, paged KV cache, batching, or fused int4 attention kernel. Results cover batch 1, 16 heads, head_dim 128, sequence lengths up to 4096 on one GB10.

## Claim scope

On GB10 with synthetic decode-step tensors up to 4K context, packed 4-bit groupwise KV-cache storage reduces KV bytes by about 3.6x to 3.9x and preserves attention-output direction, but a simple GPU dequantize-then-attend path is 16x to 17x slower than FP16 attention at 4K.

## Why it stopped

Proxy/local early falsification of the naive dequantize-each-decode path: memory improves, but 4K decode latency regresses by roughly 16x because dequantization alone is far slower than FP16 attention.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should implement a fused packed-int4 KV attention kernel and require it to beat the FP16 decode baseline at 4K without worse output error.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused packed-int4 KV attention for 4K decode
- Success threshold: At 4K context, fused int4 decode attention mean latency is <= 1.1x FP16 baseline with >= 3.5x KV byte reduction and relative L2 output error <= 0.15 on synthetic tensors.
- Stop condition: Stop if the fused kernel cannot avoid materializing dequantized K/V or if its 4K mean latency remains more than 1.5x the FP16 baseline after one focused optimization pass.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-groupwise-kv-cache-for-4k-context-inference-453e33742ca3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
