# Bounded queue depth KV compression for CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-queue-depth-kv-compression-for-cpu-inference-eac100394137`
Run ID: `bounded-queue-depth-kv-compression-for-cpu-inference-eac100394137-20260611T180158310256+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/c3a6d8866078

## What looked useful

8-bit KV compression used 0.266x to 0.388x of fp32 KV memory with mean relative L2 error 0.00852 to 0.00564 as queue depth increased from 0 to 128, but latency was 10.25x to 12.28x slower than fp32. 4-bit KV used 0.141x to 0.284x memory with error improving from 0.156 to 0.103 as queue depth increased, but latency was 9.74x to 11.95x slower.

## Boundaries and scale limits

No real LLM weights, tokenizer, perplexity, generation-quality, RSS, or optimized CPU inference kernel was tested. Results isolate attention/KV behavior and should not be claimed as end-to-end LLM serving performance.

## Claim scope

In a deterministic NumPy incremental-attention proxy at seq_len 768, heads 8, dim 64, bounded recent fp32 KV entries reduce quantized-attention output error at predictable KV memory cost, but a naive CPU path that repeatedly dequantizes compressed KV before fp32 attention is much slower than an fp32 KV baseline.

## Why it stopped

Proxy/early falsification of the naive CPU latency benefit: bounded queue depth helps quality versus memory, but the measured compressed path is 9.7x to 12.3x slower than fp32 in the medium proxy and is not paper-ready.

## Recommended next action

Stop this run as a no-paper useful signal; if continuing, test an optimized blockwise or fused-dequant CPU attention path on a small real model rather than repeating the naive dequantize-then-attend proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused compressed-KV CPU attention on a small real model
- Success threshold: At least 2x KV memory reduction with mean next-token distribution divergence under 1% and compressed-KV latency no worse than 1.25x fp32, or a clear throughput win under a memory-pressure setting.
- Stop condition: Stop if the optimized/fused path remains more than 2x slower than fp32 at 8-bit KV or if quality degradation exceeds the threshold at all queue depths that save at least 2x KV memory.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-queue-depth-kv-compression-for-cpu-inference-eac100394137`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
