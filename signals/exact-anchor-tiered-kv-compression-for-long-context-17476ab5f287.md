# Exact-Anchor Tiered KV Compression for Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-tiered-kv-compression-for-long-context-17476ab5f287`
Run ID: `exact-anchor-tiered-kv-compression-for-long-context-17476ab5f287-20260525T040841087783+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/7a13d09d61dc

## What looked useful

Exact-anchor tiering preserved synthetic anchor-recall outputs nearly exactly when true anchors were retained and fit in budget; uniform block compression kept the correct anchor-containing block often but diluted values, producing anchor MSE around 0.124-0.166. Sensitivity testing showed the advantage depends strongly on anchor selector recall and can reverse when true anchors are not retained.

## Boundaries and scale limits

No end-to-end language model, perplexity, downstream long-context task, real decode kernel, learned anchor selector, or production throughput measurement was tested. Synthetic anchors are oracle-labeled except in the selector-recall sensitivity sweep.

## Claim scope

Synthetic NumPy attention probe at sequence length 4096, dimension 96, anchor fractions 1-4%, and KV slot budgets 6.25-25%: exact retention of known true anchors prevents anchor value dilution relative to equal-slot uniform block compression.

## Why it stopped

Closed as no-paper useful signal because the evidence is a bounded synthetic attention mechanism probe, not direct model-level validation.

## Recommended next action

Run one bounded real-model follow-up on a tiny or GPT-2-small-class transformer long-context retrieval/perplexity task comparing exact-anchor tiering, uniform block compression, and recent-window retention at equal KV memory, with anchor selector recall measured explicitly.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model exact-anchor KV compression with measured anchor-selector recall
- Success threshold: At the same KV slot budget, exact-anchor tiering improves task accuracy or perplexity by at least 10% relative over uniform block compression without more than 10% decode latency overhead, and maintains true-anchor recall of at least 75%.
- Stop condition: Stop if oracle anchors fail to beat uniform block compression on the real-model task, or if learned/heuristic anchor recall is below 50% and no cheap selector improvement is available.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-tiered-kv-compression-for-long-context-17476ab5f287`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
