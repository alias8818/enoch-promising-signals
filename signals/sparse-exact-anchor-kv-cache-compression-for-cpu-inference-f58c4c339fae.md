# Sparse Exact-Anchor KV Cache Compression for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-exact-anchor-kv-cache-compression-for-cpu-inference-f58c4c339fae`
Run ID: `sparse-exact-anchor-kv-cache-compression-for-cpu-inference-f58c4c339fae-20260613T202211900109+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/ffda7f9aacb9

## What looked useful

Exact-anchor-window compression selected 3.9% of tokens at 4096 context and 1.9% at 16384 context, with about 10.5x-127.4x synthetic CPU attention latency speedups and perfect anchor top-1 recall in anchor-heavy and mixed traces. It had poor dense-output fidelity and 0.0 top-1 match on long-range non-anchor adversarial traces.

## Boundaries and scale limits

No real language model, no tokenizer-driven anchor selection, no multi-layer cache, no perplexity/logit evaluation, no production decode server, and no broad workload validation. Longest context tested was a synthetic 16384-token proxy.

## Claim scope

Synthetic single-query CPU attention traces show that exact retained anchor KV entries plus a recency window can preserve dense top-1 anchor recall while reducing candidate count, estimated KV bytes, and CPU attention latency.

## Why it stopped

No-paper useful signal: bounded synthetic evidence supports anchor recall but early-falsifies the broader dense-attention preservation claim for exact anchors plus recency alone.

## Recommended next action

Run a bounded small-transformer decode follow-up that measures logits/perplexity under exact-anchor-window compression plus a retained-mass or fallback gate; stop if it cannot meet a predeclared drift tolerance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer exact-anchor KV compression with retained-mass fallback
- Success threshold: At least 2x CPU attention/decode speedup or 50% KV-byte reduction on the tested small model while keeping perplexity delta within 5% or mean top-token agreement above 95% versus dense KV.
- Stop condition: Stop if ungated and gated variants both exceed the quality tolerance or if fallback usage eliminates the claimed CPU/KV savings.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-exact-anchor-kv-cache-compression-for-cpu-inference-f58c4c339fae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
