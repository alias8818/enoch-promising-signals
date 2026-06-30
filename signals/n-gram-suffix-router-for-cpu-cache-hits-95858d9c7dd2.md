# N-Gram Suffix Router for CPU Cache Hits

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `n-gram-suffix-router-for-cpu-cache-hits-95858d9c7dd2`
Run ID: `n-gram-suffix-router-for-cpu-cache-hits-95858d9c7dd2-20260524T191711521317+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/776b47d08011

## What looked useful

Suffix n-gram routing raised hit rate only when the cached object was legitimately keyed by the suffix itself (+22.06 pp on suffix-template and +15.85 pp on mixed traces), but did not improve valid exact-prompt cache hits and created hot-suffix load imbalance up to 3.62x max/mean shard load.

## Boundaries and scale limits

No real serving traces, no real tokenizer n-grams, no end-to-end latency measurements, and no transformer KV-cache implementation were tested. Suffix-only KV reuse remains unsupported because causal transformer suffix states depend on prefix context.

## Claim scope

Synthetic sharded-LRU CPU cache simulation with exact-prompt keys and suffix-only artifact keys across suffix-template, prefix-template, mixed, and uniform request traces.

## Why it stopped

Moderate synthetic evidence supports only a narrow suffix-artifact mechanism and early-falsifies the broader exact-prompt/KV-cache interpretation; this is a proxy/local result, not full validation.

## Recommended next action

Stop this as no-paper evidence; a bounded follow-up should test load-aware suffix routing only for a real suffix-keyed CPU artifact, not ordinary KV-cache reuse.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Load-Aware Suffix Routing for Real Suffix-Keyed CPU Artifacts
- Success threshold: Suffix-aware routing improves hit rate by at least 10 percentage points over full-prompt hashing on the target artifact while max/mean shard load stays below 1.25 and no correctness violations are found.
- Stop condition: Stop if no valid suffix-keyed artifact is identified, if hit-rate gain is below 5 percentage points on real traces, or if load skew exceeds 1.5 after load-aware balancing.

## Evidence references

- Artifact root: `<local-path>/projects/n-gram-suffix-router-for-cpu-cache-hits-95858d9c7dd2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
