# QuantMem: 4-bit memory embeddings with exact-anchor preservation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `quantmem-4-bit-memory-embeddings-with-exact-anchor-preservation-ea024ca97a85`
Run ID: `quantmem-4-bit-memory-embeddings-with-exact-anchor-preservation-ea024ca97a85-20260620T042442122382+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cc79cf7494ed

## What looked useful

q4_exact_anchor achieved anchor recall@1 1.0000 and semantic recall@1 0.9316 on 8,192 synthetic memories and 2,048 queries, using an estimated 16.21% of fp32 embedding-only storage. q4_embedding_only had anchor recall@1 0.0000.

## Boundaries and scale limits

Synthetic embeddings and records only; no real embedding model, no real repeated-agent memory corpus, no packed int4 vector index, and no production latency or memory-bandwidth measurement.

## Claim scope

In a deterministic synthetic retrieval benchmark where identifier-like anchors are collapsed by the embedding function, a 4-bit embedding store with a lossless exact-anchor sidecar restored exact-anchor recall to 100% while retaining 93.16% semantic recall.

## Why it stopped

No-paper closure because this run produced synthetic/proxy-only mechanism evidence, not direct real-corpus or production-system validation.

## Recommended next action

Run the same strategy matrix with a real embedding model on a realistic repeated-agent memory corpus, including fp32, q8, q4, and q4-plus-anchor sidecar.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-embedding QuantMem anchor preservation benchmark
- Success threshold: q4+sidecar anchor recall@1 at least 0.99, semantic recall@1 no more than 5 percentage points below fp32 embedding-only, and measured or estimated storage at least 4x smaller than fp32 embedding-only.
- Stop condition: Stop if q4+sidecar anchor recall@1 falls below 0.95 on normalized real anchors or semantic recall drops more than 10 percentage points versus fp32 embedding-only.

## Evidence references

- Artifact root: `<local-path>/projects/quantmem-4-bit-memory-embeddings-with-exact-anchor-preservation-ea024ca97a85`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
