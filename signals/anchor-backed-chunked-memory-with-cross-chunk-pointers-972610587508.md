# Anchor-Backed Chunked Memory with Cross-Chunk Pointers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-backed-chunked-memory-with-cross-chunk-pointers-972610587508`
Run ID: `anchor-backed-chunked-memory-with-cross-chunk-pointers-972610587508-20260525T215511598189+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b6629cf0c69c

## What looked useful

Complete anchor-backed cross-chunk pointers matched repeated global rescoring at 100% answer accuracy and support recall while scoring on average 1.086% as many chunks; anchor dropout showed strong brittleness, with 4-hop accuracy falling to 0.834 at 95% pointer retention and 0.668 at 90%.

## Boundaries and scale limits

CPU-only proxy benchmark; no learned anchor extraction, natural-language corpus, LLM generation, embedding retrieval, update/delete workload, or production serving validation.

## Claim scope

Synthetic symbolic multi-hop retrieval with complete entity anchors across 27 local configurations up to 2500 chunks, 10000 entities, 800 queries per configuration, and 6 hops.

## Why it stopped

No-paper closure: local evidence supports the indexing mechanism only under perfect synthetic anchors, and the dropout probe shows anchor completeness is a major unresolved risk.

## Recommended next action

Run a bounded direct-evidence follow-up with noisy learned entity/phrase anchors on a small natural-language multi-hop QA corpus, comparing pointer expansion against dense retrieval and global reranking.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noisy Learned Anchors for Cross-Chunk Pointer Retrieval
- Success threshold: Pointer expansion scores at most 10% as many chunks as global reranking while retaining at least 90% answer accuracy and support recall on the bounded corpus.
- Stop condition: Stop if measured anchor recall below 95% drives answer accuracy under 85% or if pointer expansion offers less than 5x chunk-scoring reduction versus global reranking.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-backed-chunked-memory-with-cross-chunk-pointers-972610587508`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
