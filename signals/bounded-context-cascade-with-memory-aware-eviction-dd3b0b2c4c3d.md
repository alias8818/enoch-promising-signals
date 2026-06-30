# Bounded Context Cascade with Memory-Aware Eviction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-context-cascade-with-memory-aware-eviction-dd3b0b2c4c3d`
Run ID: `bounded-context-cascade-with-memory-aware-eviction-dd3b0b2c4c3d-20260605T214858458579+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1fd369b1bf6e

## What looked useful

Cascading exact context into compressed summaries/sketches can preserve synthetic long-tail recall under tight budgets, but naive memory-aware scoring over-prioritized long-tail retention and lost enough recent/medium recall to underperform FIFO cascade overall.

## Boundaries and scale limits

Proxy-only CPU simulation; no real language model, KV cache integration, real summarizer quality, production traces, latency, or training/inference cost measurements. The run used 12 seeds and completed in 21.52 seconds with 19 MB max RSS.

## Claim scope

Synthetic delayed-lookup traces with 2000 chunks, fixed token budgets of 2048/4096/8192, and four eviction policies show that compressed cascade tiers improve long-age recall over exact-only LRU, but the tested memory-aware cascade rule does not improve overall weighted recall over a simpler FIFO cascade.

## Why it stopped

The result is useful but no-paper: the tested memory-aware cascade failed to beat FIFO cascade on overall weighted recall at every budget in the synthetic proxy, so it is not a publication-grade positive result.

## Recommended next action

Stop this run as a proxy early falsification of the tested memory-aware eviction rule; a bounded follow-up should test a hybrid policy that reserves a recent exact window and applies memory-aware scoring only to compressed long-tail tiers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid Recent-Window Cascade with Memory-Aware Long-Tail Eviction
- Success threshold: Hybrid policy beats FIFO cascade by >=5% relative overall weighted recall at two budgets while preserving recent weighted recall within 2% relative and improving long-age weighted recall.
- Stop condition: Stop if hybrid policy fails to beat FIFO cascade overall on the synthetic suite or if recent-window protection removes the long-age advantage.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-context-cascade-with-memory-aware-eviction-dd3b0b2c4c3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
