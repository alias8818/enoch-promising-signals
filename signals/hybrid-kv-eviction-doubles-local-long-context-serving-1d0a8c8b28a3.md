# Hybrid KV eviction doubles local long-context serving

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hybrid-kv-eviction-doubles-local-long-context-serving-1d0a8c8b28a3`
Run ID: `hybrid-kv-eviction-doubles-local-long-context-serving-1d0a8c8b28a3-20260607T141740678420+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/ec992d4816f3

## What looked useful

Hybrid eviction is mechanistically plausible for doubling active local sessions under fixed KV memory when long-range reuse is sparse and identifiable, but the broad serving claim remains unproven without direct LLM serving validation.

## Boundaries and scale limits

No real LLM was served end to end; generated text quality, prompt prefill cost, scheduler overhead, paged-cache allocation, KV quantization, model-specific attention patterns, and real concurrent-user workloads were not tested. Diffuse long-range targets degrade hybrid global recall when the salient set exceeds the heavy-cache budget.

## Claim scope

On seeded synthetic 8192-token retrieval traces, a hybrid recent-plus-heavy KV eviction policy preserved local and sparse long-range target recall at 50% cache, and an isolated GPU decode-attention microbenchmark showed two 4096-token sessions used the same KV bytes as one 8192-token session with lower measured kernel latency.

## Why it stopped

Proxy evidence supports the mechanism but is not full validation of the serving claim; this run closes as no-paper useful signal rather than paper-positive evidence.

## Recommended next action

Run a bounded direct-serving follow-up on a local long-context LLM: implement recent-plus-heavy KV retention, then compare fixed-memory throughput, latency, and task quality against full-cache and recent-window baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct local LLM serving test for hybrid KV eviction
- Success threshold: Hybrid reaches at least 1.8x active sessions or tokens/s under fixed KV memory, preserves at least 95% of full-cache task accuracy, and beats recent-window eviction by at least 10 percentage points on long-range recall.
- Stop condition: Stop if hybrid quality falls more than 5% below full cache at 1.8x concurrency, or if cache-management overhead removes the throughput/concurrency advantage over recent-window eviction.

## Evidence references

- Artifact root: `<local-path>/projects/hybrid-kv-eviction-doubles-local-long-context-serving-1d0a8c8b28a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
