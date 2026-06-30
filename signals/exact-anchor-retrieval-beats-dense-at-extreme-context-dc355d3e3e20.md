# Exact-Anchor Retrieval Beats Dense at Extreme Context

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-retrieval-beats-dense-at-extreme-context-dc355d3e3e20`
Run ID: `exact-anchor-retrieval-beats-dense-at-extreme-context-dc355d3e3e20-20260629T183200606789+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d384553fe35e

## What looked useful

Exact-match retrieval should be preserved for opaque identifier queries at extreme context sizes; relying only on dense vectors over long chunks can lose exact anchors even when the query contains the full identifier.

## Boundaries and scale limits

Largest tested setting was 50,000 chunks x 512 tokens/chunk, about 25.6M synthetic tokens, with 500 queries per scenario. The dense baseline was a signed feature-hashing proxy, not a pretrained neural retriever, and no real corpus or downstream RAG answer metric was tested.

## Claim scope

In a deterministic synthetic benchmark with opaque exact anchors embedded in 1k-50k chunks and 32-512 tokens per chunk, exact anchor lookup retained 100% recall@1 while a dense compressed-vector retrieval proxy degraded sharply when anchors were diluted inside long chunks.

## Why it stopped

No-paper closure: this is a useful controlled proxy result, but not direct publication-grade evidence against production dense neural retrieval.

## Recommended next action

Run a bounded deepen follow-up with a modern pretrained dense retriever and BM25 on the same anchor-retrieval task before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Pretrained Dense Retriever Anchor Recall Under Long-Chunk Dilution
- Success threshold: Exact lookup remains 100% recall@1 and the pretrained dense retriever is at least 10 percentage points worse at recall@1 in one or more 10k+ chunk, 128+ token/chunk settings, with BM25/exact controls reported.
- Stop condition: Stop if pretrained dense retrieval matches exact lookup within 1 percentage point recall@1 across all 10k+ chunk and 128+ token/chunk settings, or if model download/execution fails after ordinary dependency installation attempts.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-retrieval-beats-dense-at-extreme-context-dc355d3e3e20`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
