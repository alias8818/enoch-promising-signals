# Low-Rank KV-Cache Compression for CPU LLM Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `low-rank-kv-cache-compression-for-cpu-llm-inference-dc9e3c1632da`
Run ID: `low-rank-kv-cache-compression-for-cpu-llm-inference-dc9e3c1632da-20260611T004741733119+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/3cf9fae43f79

## What looked useful

At 128-query batched proxy, structured low-rank K/V reached <=2% output error in 9/12 cases and best 1.31x speedup at T=2048 rank=32 with 0.266 memory ratio. Random K/V never reached <=2% error and had 0.69-0.99 output relative error. In single-query decode, all structured cases were accurate but only T=4096 rank=16 was slightly faster at 1.13x; T=8192 rank=16 was 0.41x and higher ranks were slower. The mechanism is memory-promising under strong low-rank structure but not a general CPU latency win without real KV traces and optimized kernels.

## Boundaries and scale limits

No real LLM weights, tokenizer, perplexity, human quality, multi-layer/multi-head cache, prefill/decode integration, quantized kernels, or production attention implementation were tested. Synthetic structured and Gaussian controls bound only the core attention mechanism.

## Claim scope

Single-head CPU NumPy proxy for decode attention with synthetic K/V shows that truncated-SVD KV compression can preserve attention outputs only when the cache has strong low-rank structure; it does not show a robust CPU inference speed win for realistic single-query decode.

## Why it stopped

Proxy evidence is mixed: favorable synthetic caches compress accurately, but random controls fail and realistic single-query CPU latency is usually slower, so this is not paper-ready or a broad validation.

## Recommended next action

Stop this run as a proxy useful signal; a bounded follow-up should test real small-transformer KV traces with an optimized single-token CPU kernel before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real KV Trace Low-Rank Compression for Single-Token CPU Decode
- Success threshold: At context length >=4096, rank <=32 achieves <=2% perplexity increase or <=0.02 mean relative attention-output error on real traces and >=1.2x median single-token CPU decode speedup with <=0.30 KV memory ratio after amortized compression cost is reported.
- Stop condition: Stop if real KV spectra require rank >64 for <=2% quality/error preservation, or if an optimized rank <=32 path fails to beat exact attention latency by at least 1.1x at 4096-token context.

## Evidence references

- Artifact root: `<local-path>/projects/low-rank-kv-cache-compression-for-cpu-llm-inference-dc9e3c1632da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
