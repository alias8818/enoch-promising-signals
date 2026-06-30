# Exact Anchor KV Compression for Long Context Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-kv-compression-for-long-context-retrieval-92a55031635e`
Run ID: `exact-anchor-kv-compression-for-long-context-retrieval-92a55031635e-20260603T185346307825+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/810c7576d010

## What looked useful

Exact anchor retention matched full attention for anchor-target queries with cosine 0.9547-0.9966 across 1k-16k contexts, while recent/uniform/pooled controls were much lower. For arbitrary mixed targets, exact anchors failed similarly to other sparse policies because the target was usually not retained.

## Boundaries and scale limits

Proxy-only synthetic attention test; no pretrained LLM, no learned semantic anchor selector, no multi-layer KV cache, no tokenizer/RoPE effects, no real QA dataset, and no serving latency benchmark.

## Claim scope

In a synthetic single-query attention retrieval probe with random KV caches up to 16384 tokens, retaining 128 semantically marked anchor KVs exactly preserved near-full-attention outputs when the target was anchor-marked.

## Why it stopped

No-paper closure: the current evidence is a useful synthetic mechanism signal, not direct publication-grade validation in an LLM.

## Recommended next action

Run a bounded small-transformer inference follow-up that implements exact-anchor KV retention on real text needle/key-value retrieval and compares accuracy, memory, and latency against full KV and sliding-window baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-Transformer Exact Anchor KV Retrieval
- Success threshold: At 8k or longer context and equal retained-KV budget, exact anchors recover at least 90% of full-KV retrieval accuracy and outperform the best non-semantic retention baseline by at least 15 percentage points.
- Stop condition: Stop if exact anchors fail to beat sliding-window or uniform retention by at least 5 percentage points on two consecutive context lengths, or if implementation cannot preserve valid generation with compressed caches.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-long-context-retrieval-92a55031635e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
