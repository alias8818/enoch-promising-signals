# Anchor-Compress KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-compress-kv-cache-711561977a74`
Run ID: `anchor-compress-kv-cache-711561977a74-20260608T165625259840+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e6366c2e2979

## What looked useful

Anchor targets remained exactly retrievable with near-identical attention outputs at 0.99%-7.04% cache ratios, but non-anchor targets had 0.0 compressed exact-hit rate at every tested block size despite 1.0 full-cache hit rate.

## Boundaries and scale limits

No pretrained LLM, real prompt, multi-layer decode, latency kernel, or quality benchmark was run; evidence is limited to controlled CUDA tensor attention over synthetic KV caches up to sequence length 8192.

## Claim scope

Synthetic attention-level probe of anchor-preserving KV-cache compression with exact anchor KV entries retained and non-anchor history replaced by mean block representatives.

## Why it stopped

Proxy attention-level evidence is a useful early falsification of generic anchor-compress KV caching, not a full validation or full rejection of adaptive anchor policies in real LLMs.

## Recommended next action

Run one bounded pretrained-decoder long-context retrieval benchmark with adaptive anchor selection, full-KV and sliding/eviction controls, and cache-size plus decode-latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive anchors on pretrained long-context retrieval
- Success threshold: At <=10% KV cache ratio, adaptive anchor-compress is within 5 percentage points exact-match or task quality of full KV and beats the matched-budget eviction baseline by at least 10 percentage points on retrieval prompts.
- Stop condition: Stop if adaptive anchor selection fails to anchor relevant evidence often enough to keep exact-match loss within 5 percentage points, or if decode latency overhead erases the memory benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-compress-kv-cache-711561977a74`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
