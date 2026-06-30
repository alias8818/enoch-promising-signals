# Exact-Anchor Compressed KV Retrieval

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `exact-anchor-compressed-kv-retrieval-aaed92f4abda`
Run ID: `exact-anchor-compressed-kv-retrieval-aaed92f4abda-20260607T183046355412+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/e787b6d18d00

## What looked useful

Exact anchors restored anchor-target top1 retrieval to 1.000 in all main and validation conditions; all-compressed KV dropped as low as 0.019 at 16k tokens/rank 8. Non-anchor controls showed no rescue effect, with exact-anchor average top1 slightly below all-compressed by about 0.008-0.011.

## Boundaries and scale limits

Tested only synthetic key retrieval geometry at 1k-16k sequence lengths, 128-dimensional keys, rank 8-64 orthogonal low-rank compression, and periodic anchor strides of 64 or 128. Not tested on trained transformers, learned KV compression, real corpora, value semantics, or end-to-end language-model quality/latency.

## Claim scope

In a synthetic low-rank compressed KV retrieval model with random unit keys and noisy target-key queries, keeping periodic anchor keys exact restores top-1 retrieval for anchor-position targets while leaving non-anchor target retrieval at the all-compressed baseline.

## Why it stopped

Closed as no-paper useful signal because the local evidence supports the retrieval mechanism only in a synthetic low-rank key-compression probe, not in an end-to-end model or real-cache setting.

## Recommended next action

Run a bounded small-transformer or real inference-cache benchmark that inserts explicit anchor tokens and compares dense KV, all-compressed KV, and exact-anchor compressed KV on task-level retrieval plus memory/latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer exact-anchor compressed KV benchmark
- Success threshold: Exact-anchor compressed KV improves anchor-target task accuracy by at least 20 percentage points over all-compressed KV at matched memory, remains within 10 percentage points of dense KV on anchor targets, and does not claim benefit for non-anchor targets unless directly observed.
- Stop condition: Stop if exact-anchor KV fails to improve anchor-target task accuracy by 10 percentage points over all-compressed KV in the small-transformer benchmark, or if memory/latency overhead eliminates the intended compression advantage.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-compressed-kv-retrieval-aaed92f4abda`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
