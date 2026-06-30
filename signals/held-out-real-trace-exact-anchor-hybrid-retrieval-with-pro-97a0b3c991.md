# Held-out real-trace exact-anchor hybrid retrieval with production dense embeddings

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `held-out-real-trace-exact-anchor-hybrid-retrieval-with-pro-97a0b3c991`
Run ID: `held-out-real-trace-exact-anchor-hybrid-retrieval-with-pro-97a0b3c991-20260620T185142818198+0000`

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

- Parent run decision: Real-trace exact-anchor hybrid retrieval vs flat embedding retrieval: enoch://control-plane/projects/real-trace-exact-anchor-hybrid-retrieval-vs-flat-embedding-33844ad70f/runs/real-trace-exact-anchor-hybrid-retrieval-vs-flat-embedding-33844ad70f-20260620T180102224878+0000
- Parent run decision: Exact-anchor suffix memory vs flat-vector retrieval: enoch://control-plane/projects/exact-anchor-suffix-memory-vs-flat-vector-retrieval-3bfa05a03872/runs/exact-anchor-suffix-memory-vs-flat-vector-retrieval-3bfa05a03872-20260620T170002623589+0000

## What looked useful

Exact-anchor hybrid improved overall hit@1 over dense-only by 0.1917, lexical BM25 by 0.0542, and no-anchor hybrid by 0.0167, but exact-anchor hit@1 remained weak at 0.1833 and below anchor-only at 0.2583.

## Boundaries and scale limits

Not a publication-scale corpus; uses project-local trace/context chunks, generated held-out queries, single-gold ranking, no private production labels, no serving latency test, and no learned reranker.

## Claim scope

Bounded project-local real trace/context retrieval with sentence-transformers/all-MiniLM-L6-v2 over 132 redacted chunks and fixed seeds 17, 29, and 43.

## Why it stopped

Medium bounded validation produced mixed evidence: useful overall retrieval gain, but the exact-anchor mechanism did not beat the anchor-only control on the exact-anchor slice.

## Recommended next action

Stop this follow-up as no-paper evidence; if pursued, test a predeclared exact-match gated hybrid on a labeled real-trace corpus with group relevance for repeated anchors.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Labeled group-relevance exact-anchor gated hybrid retrieval
- Success threshold: Gated exact-anchor hybrid improves exact-anchor hit@1 by at least 0.10 over the best of lexical BM25, anchor-only, and no-anchor hybrid, while preserving semantic hit@1 within 0.02 of the best non-anchor method.
- Stop condition: Stop if the gated method fails to beat the best control by 0.05 exact-anchor hit@1 on two fixed seeds or if labeled group relevance cannot be constructed without private/manual evidence.

## Evidence references

- Artifact root: `<local-path>/projects/held-out-real-trace-exact-anchor-hybrid-retrieval-with-pro-97a0b3c991`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
