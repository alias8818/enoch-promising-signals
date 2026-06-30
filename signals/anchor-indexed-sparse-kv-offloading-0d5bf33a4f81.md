# Anchor-Indexed Sparse KV Offloading

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-sparse-kv-offloading-0d5bf33a4f81`
Run ID: `anchor-indexed-sparse-kv-offloading-0d5bf33a4f81-20260525T084250943926+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ebb8877a1709

## What looked useful

A 0.78%-of-KV mean-anchor index can route to useful sparse KV pages when attention is page-local or clustered: at 3.125% KV pages touched, clustered traces retained 0.326 mean attention mass with 0.920 output cosine and 0.991 top-1 page recall. Uniform traces retained only 0.041 mass and needle-mismatch traces had only 0.055 top-1 page recall at the same keep ratio, showing simple mean anchors are not robust.

## Boundaries and scale limits

No real transformer decode integration, no CPU-to-GPU paging implementation, no perplexity or text-quality measurement, no production scheduler, no long-context serving benchmark, and no comparison against established KV eviction/offload systems.

## Claim scope

Synthetic exact-attention probe of page-level anchor routing for sparse KV page selection at 16k tokens, d=64, page size 64, 512 queries, 5 seeds. Mean anchors recover useful attention mass on page-local and clustered traces while touching 3.125% to 25% of KV pages, but fail on diffuse and needle-mismatch traces.

## Why it stopped

Closed as no-paper useful signal because the synthetic probe supports the page-routing mechanism in favorable clustered regimes but exposes clear failure modes for diffuse attention and mean-anchor mismatch; this is proxy evidence, not full validation.

## Recommended next action

Run a bounded deepen test with multi-anchor or learned page summaries plus a small real-transformer decode/perplexity harness before considering any larger serving validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust Multi-Anchor KV Page Routing
- Success threshold: At 6.25% KV pages touched, improve needle-mismatch top-1 page recall from under 0.10 to at least 0.60 while keeping clustered output cosine at least 0.93, and show no more than 5% small-transformer perplexity degradation versus dense attention on a bounded corpus.
- Stop condition: Stop if multi-anchor routing cannot exceed 0.30 needle-mismatch top-1 page recall at 6.25% pages touched or if the small-transformer perplexity degradation exceeds 10% at keep ratios that save meaningful KV memory.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-sparse-kv-offloading-0d5bf33a4f81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
