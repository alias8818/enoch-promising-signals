# Anchor-Indexed Memory vs Semantic Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-indexed-memory-vs-semantic-retrieval-bbb9de080089`
Run ID: `anchor-indexed-memory-vs-semantic-retrieval-bbb9de080089-20260619T160322204749+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/6e23f283e0f4

## What looked useful

Stable anchors are useful as exact retrieval keys when arbitrary IDs are not preserved by the semantic retriever, but they should complement rather than replace semantic retrieval.

## Boundaries and scale limits

Synthetic corpus only: 96 memory documents, 96 queries, 48 anchored decisions, 48 decoys, one seed, Python stdlib TF-IDF proxy rather than real embedding/vector retrieval, no naturalistic operator traces, no malformed/duplicate anchor stress test.

## Claim scope

On a seeded synthetic repeated-agent memory replay with stable anchor IDs, near-duplicate semantic decoys, and ID-blind TF-IDF as a semantic proxy, explicit anchor lookup recovers anchored decisions perfectly while the semantic proxy often retrieves decoys. Anchor-only memory fails unanchored queries, so the supported design is hybrid anchor lookup plus semantic fallback.

## Why it stopped

Closed as a useful-signal proxy result: the bounded synthetic test supports the mechanism but does not provide direct/full validation or publication-grade evidence.

## Recommended next action

Run a bounded deepen study on naturalistic replay traces with real embedding retrieval plus BM25/lexical and hybrid controls; stop treating this synthetic proxy as sufficient for paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Naturalistic Anchor-Indexed Memory Retrieval With Embedding and Lexical Controls
- Success threshold: Hybrid retrieval improves anchored-query top-1 accuracy by at least 20 percentage points over embedding-only retrieval, matches or exceeds BM25/lexical control on anchored queries, and does not reduce no-anchor top-1 accuracy by more than 2 percentage points versus semantic fallback.
- Stop condition: Stop if hybrid retrieval does not outperform embedding-only retrieval by at least 10 percentage points on anchored queries, or if anchor noise causes more than 5 percent wrong exact-anchor matches after deduplication checks.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-memory-vs-semantic-retrieval-bbb9de080089`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
