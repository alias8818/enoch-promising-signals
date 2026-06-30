# Anchor-Compressed KV Cache for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-compressed-kv-cache-for-long-context-68529a349102`
Run ID: `anchor-compressed-kv-cache-for-long-context-68529a349102-20260528T172043352928+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5c885858a7e3

## What looked useful

Across 243 GPU trials, iid random caches remained high-error (median relative L2 0.7864). Clustered block-redundant traces compressed well only at matching block size 32 (median relative L2 0.000172 at 24.24x median compression) but failed at block size 128 (median relative L2 0.6874). Anchor retrieval failed without anchors (median relative L2 1.0227) and was rescued by a 1% anchor rate at block size 32 (median relative L2 0.0000286 at 24.24x compression).

## Boundaries and scale limits

No trained-language-model perplexity, generation-quality, long-prompt benchmark, multi-layer cache replay, cache-maintenance overhead, or production serving measurement was run. Sequence lengths were synthetic up to 32768 with 8 heads, 64-dimensional heads, 128 queries, and three seeds.

## Claim scope

Synthetic single-step attention traces only: anchor-compressed KV cache with exact anchors and log-count-corrected block centroids preserves outputs when non-anchor spans are block-redundant or when rare queried tokens are retained as anchors; it fails on iid random caches and oversized mixed-topic blocks.

## Why it stopped

This run produced a synthetic mechanism signal but not direct model-quality evidence; close as no-paper useful signal rather than treating proxy results as validation.

## Recommended next action

Run a bounded deepen test by replaying real KV caches from a small pretrained decoder on long text and comparing logits/perplexity under full cache versus anchor-compressed cache.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV replay for anchor-compressed cache
- Success threshold: At 8x or greater effective KV compression, anchor-compressed replay should reduce median next-token logit KL by at least 50% versus block-centroid-only compression and keep perplexity delta below 5% on the tested text slices.
- Stop condition: Stop if real KV replay shows anchor-compressed cache has similar or worse logit KL than block-centroid-only compression at matched compression, or if perplexity delta exceeds 10% at all tested compression ratios.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-compressed-kv-cache-for-long-context-68529a349102`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
