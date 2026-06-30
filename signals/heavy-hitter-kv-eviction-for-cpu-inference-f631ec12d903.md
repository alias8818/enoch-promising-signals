# Heavy-Hitter KV Eviction for CPU Inference

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `heavy-hitter-kv-eviction-for-cpu-inference-f631ec12d903`
Run ID: `heavy-hitter-kv-eviction-for-cpu-inference-f631ec12d903-20260608T154515934377+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/5bdd7ad33d59

## What looked useful

Practical cached heavy-hitter KV eviction showed essentially no retained-mass gain (+0.0002) or target-retention gain (+0.0038) over a recency window across 15 workload/budget comparisons, while bounded-cache attention latency was 1.43x the window. Oracle heavy-hitter retained synthetic targets better (+0.2802) but did not improve retained mass or output error, exposing a gap between target retention and useful attention-output fidelity.

## Boundaries and scale limits

No real LLM, tokenizer, perplexity/task metric, batching, quantized KV, paged attention kernel, or end-to-end serving measurement. Evidence is a bounded proxy and should not be read as full validation of model-level quality or production throughput.

## Claim scope

Synthetic CPU attention-only benchmark with prompt_len=768, gen_len=192, 8 heads, dim=64, budgets 64-512, comparing full KV, recency window, oracle heavy-hitter, and practical cached-score heavy-hitter on retained mass, output error, target retention, and attention CPU time.

## Why it stopped

Synthetic CPU-attention evidence does not support the practical cached heavy-hitter policy over a simple recency window; this is a proxy early falsification rather than a full model-level validation.

## Recommended next action

Stop this run as an early/proxy negative; if pursuing a bounded follow-up, test recency, cached heavy-hitter, and a sink-pinned or re-entry-capable variant inside a small real decoder-only CPU model on perplexity/task loss and tokens/s.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-model CPU validation of sink-aware KV eviction
- Success threshold: At the same KV budget, sink-aware or re-entry heavy-hitter must improve perplexity/task loss by at least 5% relative to recency-window degradation while preserving at least 1.5x attention-layer speedup versus full KV and not reducing end-to-end tokens/s versus recency.
- Stop condition: Stop if cached or sink-aware heavy-hitter has no statistically meaningful quality advantage over recency or if policy overhead makes end-to-end CPU generation slower than recency at the same budget.

## Evidence references

- Artifact root: `<local-path>/projects/heavy-hitter-kv-eviction-for-cpu-inference-f631ec12d903`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
