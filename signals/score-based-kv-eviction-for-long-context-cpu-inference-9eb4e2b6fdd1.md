# Score-based KV eviction for long-context CPU inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `score-based-kv-eviction-for-long-context-cpu-inference-9eb4e2b6fdd1`
Run ID: `score-based-kv-eviction-for-long-context-cpu-inference-9eb4e2b6fdd1-20260526T023921141374+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/77620b22bbc3

## What looked useful

Score-based eviction reduced mean attention-output MSE versus recent eviction by about 29% at a 128-slot budget and about 54% at a 256-slot budget on anchor-reuse traces, while a local-only control showed only tiny absolute differences. The mechanism appears useful specifically when old KV entries are repeatedly reused.

## Boundaries and scale limits

Proxy-only single-layer attention; no pretrained language model, no tokenizer/document distribution, no real CPU inference kernel, no task quality or perplexity, no comparison to established heavy-hitter KV eviction baselines, and no validation beyond 2048-token context.

## Claim scope

In a deterministic synthetic CPU decode-attention proxy with 2048-token contexts, 64-dimensional keys/values, 5 seeds, and fixed KV budgets of 128 or 256 slots, pure score-based eviction preserves long-range reused anchor tokens better than recent or random eviction, lowering attention-output MSE versus a full-KV reference.

## Why it stopped

Closed as no-paper useful signal because the current evidence is synthetic/proxy-only, despite supporting the long-range reuse mechanism.

## Recommended next action

Run a bounded real-model CPU follow-up: implement score-based KV eviction in a small transformer decode loop and compare perplexity/task quality, tokens/sec, and memory against recency and a heavy-hitter baseline at 4k-8k context.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU validation of score-based KV eviction at 4k-8k context
- Success threshold: At the same KV budget, score-based eviction must improve quality over recency by at least 10% relative error or recover a clear long-range retrieval target, while keeping decode throughput within 20% of recency and matching or improving peak memory.
- Stop condition: Stop if score-based eviction fails to beat recency on quality at 4k context, or if score maintenance overhead reduces CPU decode throughput by more than 20% without a compensating quality gain.

## Evidence references

- Artifact root: `<local-path>/projects/score-based-kv-eviction-for-long-context-cpu-inference-9eb4e2b6fdd1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
