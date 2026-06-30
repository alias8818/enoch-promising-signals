# Layered Agent Memory with Trace-Derived Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `layered-agent-memory-with-trace-derived-compression-8ef61a155ad5`
Run ID: `layered-agent-memory-with-trace-derived-compression-8ef61a155ad5-20260614T120000005215+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9d7f0382a986

## What looked useful

Trace-derived compression improved layered memory over flat recency by +0.104, +0.219, and +0.404 exact-match accuracy at 512, 1,024, and 2,048 tokens in the skewed regime, and beat non-trace recent-summary selection by +0.077, +0.164, and +0.294. However, trace-derived summary-only beat layered trace memory by +0.060 to +0.105 because recent events consumed budget without being needed by the recall-only task. Under uniform queries, trace weighting gave little advantage.

## Boundaries and scale limits

Proxy-only synthetic evidence. No natural-language summaries, no LLM agent loop, no learned embeddings, no noisy compression, no real task traces, and no long-horizon deployment. The benchmark favors final-state fact summaries and does not require exact recent verbatim trace recall.

## Claim scope

Synthetic mutable-fact trace benchmark with 2,400 keys, 6,000 updates, 1,200 trace-derived weighting queries, 1,000 held-out recall queries, 8 seeds, and 512-2,048 token budgets. Trace-derived compressed summaries improve compact recall under skewed future query demand, but the tested recent-plus-compressed layered policy is not best for recall-only final-state queries.

## Why it stopped

No-paper useful signal from a synthetic proxy: trace-derived compression is supported under skew, but the stronger layered-memory claim is mixed because summary-only wins on the recall-only benchmark.

## Recommended next action

Run a bounded deepen follow-up with mixed query types where some held-out questions require recent exact trace events and others require older compressed facts; stop if layering still fails to beat summary-only at matched token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mixed Recent-Verbatim and Old-Fact Trace Memory Benchmark
- Success threshold: Layered trace memory improves overall exact-match accuracy by at least 0.05 over trace-summary-only and recency-only at two token budgets, while improving recent-verbatim accuracy by at least 0.15 over summary-only.
- Stop condition: Stop if layered trace memory fails to beat trace-summary-only by at least 0.02 overall at all tested budgets or if its old-fact recall loss outweighs recent-verbatim gains.

## Evidence references

- Artifact root: `<local-path>/projects/layered-agent-memory-with-trace-derived-compression-8ef61a155ad5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
