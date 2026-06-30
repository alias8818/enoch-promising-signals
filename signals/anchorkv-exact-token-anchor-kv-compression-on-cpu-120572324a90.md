# AnchorKV: exact-token-anchor KV compression on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `anchorkv-exact-token-anchor-kv-compression-on-cpu-120572324a90`
Run ID: `anchorkv-exact-token-anchor-kv-compression-on-cpu-120572324a90-20260620T040030573221+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/cc79cf7494ed

## What looked useful

Exact-token-anchor retention reached mean RMSE 0.3329 and top-1 attention match 90.23% versus recent-only RMSE 0.7903 and top-1 match 46.61%, while retaining the same mean 7.03% of KV rows and preserving 100% of anchor rows.

## Boundaries and scale limits

Synthetic K/V and query distributions only; no real transformer, tokenizer, multi-layer/multi-head cache, generation-quality metric, paged-attention allocator, or end-to-end CPU serving benchmark was tested.

## Claim scope

In a deterministic single-head CPU attention simulation with exact known anchor token ids and 3.125%-12.5% retained KV-row budgets, preserving exact anchor-token KV rows materially improves attention-output fidelity versus recent-only or stride-plus-recent retention at the same budget.

## Why it stopped

Closed as no-paper useful signal because the evidence supports the local exact-anchor mechanism only in a synthetic attention proxy, not a full KV-cache compression claim.

## Recommended next action

Run a bounded real-model follow-up on a small CPU-compatible transformer with tokenizer-defined anchors, fixed KV budget, generation quality or perplexity metrics, and end-to-end decode latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU validation of exact-token-anchor KV retention
- Success threshold: At the same retained-row budget, exact-token-anchor retention improves the selected quality metric by at least 20% relative to recent-only retention while keeping at least 1.5x CPU decode speedup versus full-cache attention.
- Stop condition: Stop if exact-token-anchor retention fails to improve quality by at least 10% over recent-only retention or if cache-management overhead removes the CPU speedup versus full-cache attention.

## Evidence references

- Artifact root: `<local-path>/projects/anchorkv-exact-token-anchor-kv-compression-on-cpu-120572324a90`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
