# Ring Buffer KV Eviction for Long Context on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ring-buffer-kv-eviction-for-long-context-on-cpu-2f7a12118b56`
Run ID: `ring-buffer-kv-eviction-for-long-context-on-cpu-2f7a12118b56-20260607T073305357686+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c5f32c29a0f0

## What looked useful

Ring-buffer eviction gave 39.34x faster KV updates and 1.78x faster steady step time than naive shift eviction at window 512, and 81.71x faster updates and 2.89x faster steady step time at window 1024. At window 128, ring lost on total step time due to wrapped-attention overhead. A synthetic evicted-needle diagnostic showed full cache retained a needed first-token value while fixed-window ring eviction returned zero after eviction.

## Boundaries and scale limits

Synthetic Q/K/V tensors only; no trained language model quality, no production inference kernel, no multi-layer transformer stack, and maximum tested window was 1024 with 8 heads and head dimension 64.

## Claim scope

On a CPU NumPy synthetic decode benchmark, a ring-buffer KV cache preserves sliding-window attention semantics while avoiding per-token whole-window shifts; it improves steady step time for medium windows tested here, but does not preserve information outside the retained window.

## Why it stopped

Proxy benchmark supports the CPU cache-update mechanism but also early-falsifies any broad claim that plain ring-buffer eviction preserves arbitrary long-range dependencies; this is not a full validation or paper-ready result.

## Recommended next action

Stop this worker run as no-paper useful signal; the concrete next bounded test is a small real-model CPU perplexity/retrieval comparison of full cache, plain ring sliding window, and ring plus attention-sink tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU quality test for ring-buffer KV eviction with attention sinks
- Success threshold: Ring plus sinks should retain at least 80% of full-cache retrieval accuracy on the bounded synthetic task while keeping peak KV cache memory within 25% of the plain ring window and improving CPU decode throughput versus full cache at long contexts.
- Stop condition: Stop if plain ring and ring plus sinks both lose more than 50% retrieval accuracy for out-of-window dependencies or if the production-style CPU implementation shows no throughput or memory advantage over full cache at the tested context lengths.

## Evidence references

- Artifact root: `<local-path>/projects/ring-buffer-kv-eviction-for-long-context-on-cpu-2f7a12118b56`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
