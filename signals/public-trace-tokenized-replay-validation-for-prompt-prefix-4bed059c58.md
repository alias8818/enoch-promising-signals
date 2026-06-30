# Public-trace tokenized replay validation for prompt-prefix lookup latency

Status: `useful_signal`
Curation bucket: `weak_local_only_preserved`
Curation score: `73`
Project ID: `public-trace-tokenized-replay-validation-for-prompt-prefix-4bed059c58`
Run ID: `public-trace-tokenized-replay-validation-for-prompt-prefix-4bed059c58-20260523T095734510289+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Weak/local-only preserved signals
- Score: `73`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": -10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Model-tokenized serving replay for prompt-prefix lookup latency: enoch://control-plane/projects/model-tokenized-serving-replay-for-prompt-prefix-lookup-la-0c3c1292ce/runs/model-tokenized-serving-replay-for-prompt-prefix-lookup-la-0c3c1292ce-20260523T093842821145+0000
- Parent run decision: Serving endpoint prompt-lookup latency distribution on natural repeated-context workloads: enoch://control-plane/projects/serving-endpoint-prompt-lookup-latency-distribution-on-nat-057e7fad9b/runs/serving-endpoint-prompt-lookup-latency-distribution-on-nat-057e7fad9b-20260523T092544597224+0000

## What looked useful

Tokenized public-trace replay is viable and reproducible. Across three WildChat shards, token trie p95 lookup latency averaged 7.57 us on natural replay and 8.58 us on shared-prefix replay, versus 829.13 us and 808.03 us for an exact token-prefix hash baseline and 405.16 us and 1989.69 us for naive text scan. The mechanism is supported locally but not paper-ready.

## Boundaries and scale limits

CPU-only lookup microbenchmark; no model-serving integration, GPU KV-cache reuse, concurrent request load, eviction policy, memory-pressure test, production cache baseline, full WildChat replay, or cross-dataset replication. The text-scan baseline is intentionally simple and not a production optimized text index.

## Claim scope

On three public WildChat-1M parquet shards totaling 55,654 replayed unique user prompts per workload, a token-prefix trie provides matched prefix-hit semantics against an exact token-prefix hash baseline and substantially lower prompt-prefix lookup latency for natural replay, shared-prefix replay, and randomized-control workloads.

## Why it stopped

The replicated local benchmark supports the scoped lookup-latency mechanism but falls short of the requested Tier 4 paper-readiness standard, which would require end-to-end serving/KV-cache integration, production baselines, concurrency/eviction robustness, and broader trace replication.

## Recommended next action

Stop this depth-4 follow-up as no-paper useful evidence; do not recommend another follow-up from this branch because the controller depth cap is reached.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/public-trace-tokenized-replay-validation-for-prompt-prefix-4bed059c58`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
