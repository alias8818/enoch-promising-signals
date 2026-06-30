# Batched Speculative Decoding with Shared KV-Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `batched-speculative-decoding-with-shared-kv-cache-243151aebc53`
Run ID: `batched-speculative-decoding-with-shared-kv-cache-243151aebc53-20260608T115453072973+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/f44864991620

## What looked useful

Parallel shared-prefix KV verification crossed from slower than duplicate full recomputation at batch 4-8/prefix 64 to 1.82x at batch 16/prefix 128 and 3.02-4.79x at prefix 256; modeled KV bytes fell by 70.6-95.4%. Sequential token-by-token shared verification was mostly slower, showing that block parallelism is required for latency benefit.

## Boundaries and scale limits

Test used a small random decoder, synthetic token IDs, draft length 4, one shared prefix group, generic PyTorch attention, and no trained target/draft models, acceptance traces, paged KV cache, production scheduler, or 7B+ scale.

## Claim scope

In a local fp16 GB10 PyTorch mechanism test with a 6-layer random decoder, batched speculative verification with a shared prefix KV cache is numerically equivalent to duplicate full recomputation within fp16 tolerance and becomes faster only when suffix verification is block-parallel and the shared prefix/batch amortization is large enough.

## Why it stopped

Proxy/mechanism evidence supports a scoped implementation signal but is not full validation of production speculative decoding or large-model serving.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should use a small trained target model plus realistic speculative traces and a paged-attention baseline to validate the crossover under end-to-end accepted-token latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Shared KV speculative verification on a trained small target with realistic traces
- Success threshold: At least 1.3x accepted-token throughput or p50 verification latency improvement over the strongest duplicate-prefix/cached baseline in two or more realistic trace buckets, with identical accepted-token decisions and at least 25% measured KV memory reduction.
- Stop condition: Stop if shared-KV remains below 1.0x latency speedup after block-parallel/paged-cache implementation in realistic trace buckets, or if correctness diverges beyond fp16/bfloat16 tolerance.

## Evidence references

- Artifact root: `<local-path>/projects/batched-speculative-decoding-with-shared-kv-cache-243151aebc53`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
