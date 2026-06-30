# Evicted grouped-query KV cache for 32k context on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evicted-grouped-query-kv-cache-for-32k-context-on-gb10-2921841075cc`
Run ID: `evicted-grouped-query-kv-cache-for-32k-context-on-gb10-2921841075cc-20260611T082451825973+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d5a821022275

## What looked useful

At 32k context, full-cache GQA decode measured 5.469 ms/token and 128 MiB KV; retaining 1024 KV entries measured 0.124 ms/token and 4 MiB KV, a 44.2x latency speedup and 32x KV reduction. Pure eviction of an old forced target gave relative L2 1.001 and cosine 0.0028 versus full-cache output; retaining 256 sink tokens made the same target visible and matched full-cache output in the synthetic case.

## Boundaries and scale limits

No real model quality, perplexity, long-context benchmark, fused serving kernel, multi-layer stack, quantized KV format, batching, or production scheduler was tested. Random tensors and synthetic retrieval are proxy evidence only.

## Claim scope

On GB10 with a BF16 PyTorch single-token GQA decode microbenchmark using B=1, 32 query heads, 8 KV heads, head_dim=128, evicting a 32k KV cache down to fixed retained windows makes decode latency and KV memory scale with retained length; pure eviction fails a constructed old-token retrieval case, while a sink+window variant preserves a known sink target in that synthetic diagnostic.

## Why it stopped

Bounded microbenchmark supports the systems mechanism but synthetic retrieval exposes the quality hazard; this is proxy evidence, not full validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should test full-cache versus sliding-window versus sink+window KV policies on a real small/pretrained GQA model with 32k retrieval and perplexity tasks plus end-to-end decode throughput.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model 32k quality and throughput test for sink+window GQA KV eviction
- Success threshold: Sink+window retains at least 90% of full-cache retrieval accuracy on bounded 32k tasks, keeps perplexity degradation within 5% on the tested corpus, and delivers at least 4x KV memory reduction plus at least 2x decode speedup versus full-cache on GB10.
- Stop condition: Stop if pure and sink+window eviction both lose more than 10% absolute retrieval accuracy or exceed 5% perplexity degradation at retained windows up to 8192, or if end-to-end decode speedup falls below 2x after implementing the real cache path.

## Evidence references

- Artifact root: `<local-path>/projects/evicted-grouped-query-kv-cache-for-32k-context-on-gb10-2921841075cc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
