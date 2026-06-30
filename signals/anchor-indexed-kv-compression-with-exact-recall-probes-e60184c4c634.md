# Anchor-Indexed KV Compression with Exact Recall Probes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchor-indexed-kv-compression-with-exact-recall-probes-e60184c4c634`
Run ID: `anchor-indexed-kv-compression-with-exact-recall-probes-e60184c4c634-20260529T174221008055+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ece0442c89b7

## What looked useful

At sequence length 16384, dimension 128, and 64 exposed rows (256x row compression), anchor-indexed retention achieved 1.0 exact recall on anchor probes across 3 seeds, 0.0 on non-anchor targets, and 0.00199 on uniform targets. Sliding-window retention at the same row budget achieved 0.0 on anchor probes, 1.0 on recent-region targets, and 0.00346 on uniform targets. Noise sweep showed anchor-probe recall remained 1.0 through noise 0.10, 0.9885 at noise 0.20, and 0.6753 at noise 0.35.

## Boundaries and scale limits

No transformer model, learned anchor selection, value-vector semantics, generation task, latency benchmark, or real long-context dataset was tested. The result is a retrieval-mechanics proxy over random normalized keys.

## Claim scope

In a synthetic random-key KV cache with exact query keys plus small Gaussian noise, retaining exact anchor/probe rows while compressing non-anchor spans into centroids preserves exact recall for anchored positions at matched row budgets where sliding-window retention only preserves recent positions.

## Why it stopped

No-paper useful signal: the synthetic proxy supports the narrow anchor exact-recall mechanism but does not validate language-model behavior or learned anchor routing.

## Recommended next action

Stop this proxy run; next, implement the same anchor-indexed eviction in a small transformer KV-cache retrieval benchmark and compare exact-match accuracy and latency against sliding-window and full-cache controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchor-indexed KV eviction in a small transformer exact-match retrieval task
- Success threshold: At 8x or greater KV row compression, anchor-indexed cache recovers at least 95% exact match on marked anchor facts, beats sliding-window anchor recall by at least 30 percentage points, and preserves at least 95% of sliding-window recent-target accuracy with no more than 20% throughput loss.
- Stop condition: Stop as negative if anchor-indexed cache fails to exceed sliding-window anchor recall by 10 percentage points at 8x compression or if the indexing overhead removes the memory/latency benefit.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-kv-compression-with-exact-recall-probes-e60184c4c634`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
