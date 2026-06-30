# Semantic Anchor Compression vs Flat Vector Retrieval

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `semantic-anchor-compression-vs-flat-vector-retrieval-a2ee970c7d51`
Run ID: `semantic-anchor-compression-vs-flat-vector-retrieval-a2ee970c7d51-20260620T080812268871+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-plus: enoch://research-facility/provider/qwen/qwen3.7-plus/86bb76839617

## What looked useful

Exact recall@10 versus flat retrieval was very low: best 0.0456 on clustered data and 0.0172 on isotropic data. However, on clustered data the best anchor semantic precision@10 was 0.9562 at 43.07x estimated compression, and the highest-compression tested setting reached 0.7808 semantic precision@10 at 73.44x compression. The isotropic control failed, supporting that the effect depends on semantic cluster structure.

## Boundaries and scale limits

Synthetic embeddings only; 20,000 documents and 500 queries; no real text corpus, no external relevance judgments, no optimized inverted-list implementation, and no ANN baseline. Runtime and storage are proxy estimates for the anchor method, not production serving measurements.

## Claim scope

A sparse semantic-anchor code index was tested as a compressed alternative to exact flat cosine retrieval on synthetic 384-dimensional embeddings with clustered and isotropic controls. It is not a viable drop-in exact-neighbor replacement, but it can preserve semantic topic labels on clustered embeddings at high estimated compression.

## Why it stopped

Proxy evidence falsifies the drop-in exact flat-retrieval replacement claim, while showing a narrower semantic-routing signal that needs real-corpus validation before any paper claim.

## Recommended next action

Stop this run as a no-paper useful signal; run one bounded follow-up on a real embedding benchmark with anchor candidate generation plus exact vector reranking against flat/ANN baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus two-stage semantic-anchor candidate generation with exact reranking
- Success threshold: At least 0.90 recall@10 versus exact flat retrieval after reranking while reducing exact vector comparisons by at least 10x and reducing stored dense-vector memory by at least 4x in the first-stage index.
- Stop condition: Stop if anchor candidate generation cannot reach 0.80 recall@10 at 10x candidate reduction on the first real-corpus benchmark, or if memory/latency is worse than a simple ANN baseline at comparable recall.

## Evidence references

- Artifact root: `<local-path>/projects/semantic-anchor-compression-vs-flat-vector-retrieval-a2ee970c7d51`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
