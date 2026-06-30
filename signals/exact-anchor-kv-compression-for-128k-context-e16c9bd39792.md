# Exact Anchor KV Compression for 128k Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-128k-context-e16c9bd39792`
Run ID: `exact-anchor-kv-compression-for-128k-context-e16c9bd39792-20260608T140023485131+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/715307f7e303

## What looked useful

Exact anchors are a plausible retrieval-protection component: oracle exact-anchor schemes reached 100% synthetic needle retrieval through 128k at median item ratios near 0.59% with block summaries and 0.20% anchor-only. Periodic and recent-window controls had 0% retrieval for unselected long-range needles. Diffuse-attention cases exposed output magnitude distortion despite high cosine similarity.

## Boundaries and scale limits

No real transformer layers, no trained language model, no multi-head/layer decode path, no production KV cache implementation, and no task-level long-context QA benchmark were run. Positive retrieval results rely on an oracle anchor tag for the needle.

## Claim scope

Synthetic single-query attention probes up to 128k context length show that oracle-selected exact KV anchors preserve top-1 needle retrieval at very low KV item ratios, but do not by themselves solve anchor selection or softmax mass calibration.

## Why it stopped

Closed as no-paper useful signal: the local synthetic evidence supports the exact-anchor retrieval mechanism under oracle selection but is insufficient for publication-grade claims about 128k KV compression in real models.

## Recommended next action

Run a bounded direct transformer decoding test with a small long-context model or toy transformer, comparing oracle/tagged anchors, learned or heuristic anchor selection, and calibrated block summaries on a needle-retrieval task.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Tiny-Transformer Test of Exact Anchor KV Compression
- Success threshold: Oracle/tagged exact-anchor compression preserves at least 95% of full-KV retrieval accuracy with sub-1% KV item ratio and materially lower logit/output divergence than periodic or recent-window controls.
- Stop condition: Stop if exact-anchor variants fail to beat recent-window or periodic controls on retrieval, or if output/logit divergence remains high even when anchors are selected correctly.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-128k-context-e16c9bd39792`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
