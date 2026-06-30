# Exact-Anchor Memory Beats Flat RAG on Verbatim Long-Context Recall

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-memory-beats-flat-rag-on-verbatim-long-context-recall-c3d4d7bc7dbd`
Run ID: `exact-anchor-memory-beats-flat-rag-on-verbatim-long-context-recall-c3d4d7bc7dbd-20260619T080152130096+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/7e33b636a484

## What looked useful

Exact anchors remove a chunk-boundary and distance failure mode that persists for flat retrieval even when top-k and neighbor expansion are increased under a fixed context budget.

## Boundaries and scale limits

Synthetic records only; lexical BM25 flat retrieval only; no embedding retriever, reranker, parent-document expansion, natural corpus, or end-to-end LLM generation was tested. This is a mechanism probe, not publication-grade validation.

## Claim scope

In a synthetic anchored-record benchmark where queries contain exact anchor ids, exact-anchor memory achieved 1.000 oracle verbatim recall while flat BM25 chunk retrieval under a 1024-token context budget dropped as anchor-payload distance increased, reaching 0.000 recall at a 1024-token gap.

## Why it stopped

No-paper useful signal: corrected synthetic retrieval evidence supports the mechanism, but it proxies LLM recall and does not cover natural corpora or strong modern RAG baselines.

## Recommended next action

Run a bounded end-to-end LLM exact-match recall follow-up using the same harness with stronger RAG controls, including embedding retrieval, reranking, and parent-document expansion.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Exact-Anchor Memory vs Strong RAG Controls for Verbatim Recall
- Success threshold: Exact-anchor memory improves exact-match recall by at least 20 percentage points over the strongest RAG control at 256-token and 1024-token anchor-payload gaps, with no loss on easy 16-token and 64-token gaps.
- Stop condition: Stop if the strongest RAG control matches exact-anchor recall within 5 percentage points across all gap settings, or if generation errors dominate despite gold payload being present in retrieved context.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-memory-beats-flat-rag-on-verbatim-long-context-recall-c3d4d7bc7dbd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
