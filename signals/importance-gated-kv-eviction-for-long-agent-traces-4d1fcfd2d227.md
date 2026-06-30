# Importance-Gated KV Eviction for Long Agent Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `importance-gated-kv-eviction-for-long-agent-traces-4d1fcfd2d227`
Run ID: `importance-gated-kv-eviction-for-long-agent-traces-4d1fcfd2d227-20260524T180235537889+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2d085e78b642

## What looked useful

Across completed 128/256-capacity cells, the best importance policy improved answerable-rate over LRU by 24.4 to 45.5 absolute points and reduced high-importance fact eviction substantially; for example, at capacity 256 and gate noise 0.75, answerable-rate rose from 39.6% to 79.5% while high-importance fact eviction fell from 92.1% to 11.0%.

## Boundaries and scale limits

No real transformer KV cache, real LLM inference, production agent traces, multi-layer/head cache effects, latency overhead, or perplexity/task benchmark was measured. Completed sweep covers 160 generated traces per cell at trace length 4096 for cache capacities 128 and 256 across three gate-noise settings, plus one 512-token sanity cell.

## Claim scope

In a reproducible synthetic long-agent-trace cache-retention model with sparse durable facts, noisy non-fact tokens, delayed fact queries, fixed cache capacity, and noisy online importance estimates, importance-gated KV eviction preserved answerable state substantially better than LRU/FIFO/random baselines.

## Why it stopped

Synthetic/proxy evidence supports the mechanism but is not direct publication-grade validation of transformer KV-cache eviction.

## Recommended next action

Run a bounded direct small-model KV-cache benchmark with real cache eviction hooks and delayed-fact agent traces; this run should stop as no-paper useful signal because the current evidence is synthetic/proxy-only.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct Small-Model KV Eviction Benchmark for Delayed Agent Facts
- Success threshold: At equal cache budget, importance-gated eviction improves delayed-fact answer accuracy by at least 10 absolute percentage points or reduces perplexity/log-loss materially versus the best recency/streaming baseline, while adding less than 10% decode-time overhead in the tested small-model harness.
- Stop condition: Stop as negative if the real-model harness shows less than 5 absolute accuracy points of improvement over LRU/streaming baselines, or if latency overhead exceeds 20% without a compensating accuracy/log-likelihood gain.

## Evidence references

- Artifact root: `<local-path>/projects/importance-gated-kv-eviction-for-long-agent-traces-4d1fcfd2d227`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
