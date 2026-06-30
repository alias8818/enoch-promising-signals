# KV-Cache Eviction Policy for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-eviction-policy-for-cpu-inference-85d505e89e0a`
Run ID: `kv-cache-eviction-policy-for-cpu-inference-85d505e89e0a-20260613T075101975255+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e553faf733bb

## What looked useful

Streaming sinks+recent was best by retained attention mass in 12/15 regime-budget buckets and was cheaper than attention-guided policies. Lazy CPU-aware hybrid recovered near-heavy-hitter anchor recall in retrieval-like regimes at much lower overhead than exact heavy-hitter, and won the topic-shift budget-256 bucket, but it did not dominate overall retained mass.

## Boundaries and scale limits

No real model weights, no perplexity/task-quality measurement, no production serving stack, no real attention traces, no batch/concurrency study, and no 7B+/datacenter-scale validation.

## Claim scope

Local CPU-only synthetic sparse-attention proxy for KV-cache eviction over 2048-token traces, 4 traces per regime, budgets 64/128/256, comparing recent window, streaming sinks+recent, exact heavy-hitter, lazy CPU-aware hybrid, and random policies.

## Why it stopped

Proxy evidence is mixed and insufficient for paper writing; it early-falsifies the broad general-improvement claim under retained-attention mass while preserving a retrieval-heavy direct-test follow-up.

## Recommended next action

Run a direct CPU inference follow-up on a small decoder model with fixed KV budgets, measuring perplexity/task quality, decode throughput, memory, and policy overhead for streaming, exact heavy-hitter, and lazy hybrid controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct CPU decode validation of lazy hybrid KV eviction on retrieval-heavy prompts
- Success threshold: Lazy hybrid must beat streaming sinks+recent by at least 3% relative on retrieval-heavy quality/perplexity while staying within 2x streaming policy overhead and preserving local-context quality within 1%.
- Stop condition: Stop if lazy hybrid fails to improve retrieval-heavy quality/perplexity versus streaming or exceeds 2x streaming policy overhead on the direct CPU model run.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-eviction-policy-for-cpu-inference-85d505e89e0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
