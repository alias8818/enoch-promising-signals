# Hierarchical Memory Compression with Semantic Chunk Boundaries

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-memory-compression-with-semantic-chunk-boundaries-5dfdb7c786d3`
Run ID: `hierarchical-memory-compression-with-semantic-chunk-boundaries-5dfdb7c786d3-20260611T195554437206+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/15286057a376

## What looked useful

Semantic boundaries can prevent lossy hierarchical memory compression from dropping facts that occur at semantic section starts when fixed windows merge multiple sections. Medium proxy result over 1,440 queries: semantic_shift Recall@1 1.000 vs fixed_words 0.167 with one-sentence summaries, and 1.000 vs 0.320 with two-sentence summaries. Sensitivity showed the effect depends on correctly calibrated boundary detection.

## Boundaries and scale limits

Synthetic corpus only; lexical TF-IDF retrieval only; first-N-sentence compression proxy only; semantic threshold was manually chosen and the benefit disappeared at lower thresholds; no LLM summarizer, embedding retriever, natural corpus, or downstream QA model was tested.

## Claim scope

On a synthetic multi-topic retrieval-after-compression benchmark, a calibrated semantic-shift chunker preserved queryable section-start facts under first-N-sentence lossy compression substantially better than fixed-size chunking.

## Why it stopped

Proxy evidence is useful but not paper-ready because it is synthetic, threshold-dependent, and does not directly test LLM hierarchical memory compression.

## Recommended next action

Run a bounded deepen follow-up on natural long documents using an LLM or embedding-based compressor, with fixed token budgets and downstream answer retrieval metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Natural-document semantic boundary compression benchmark
- Success threshold: Semantic-boundary compression improves Recall@1 or downstream answer accuracy by at least 10 percentage points over fixed-window chunking at matched compression ratio, with a paired 95% confidence interval excluding zero on at least two natural-document domains.
- Stop condition: Stop if semantic boundaries fail to improve retention by at least 5 percentage points in a 200-query pilot, or if gains only appear under manually tuned thresholds that do not transfer across domains.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-memory-compression-with-semantic-chunk-boundaries-5dfdb7c786d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
