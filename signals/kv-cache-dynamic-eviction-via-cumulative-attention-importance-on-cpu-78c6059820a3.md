# KV-Cache Dynamic Eviction via Cumulative Attention Importance on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `kv-cache-dynamic-eviction-via-cumulative-attention-importance-on-cpu-78c6059820a3`
Run ID: `kv-cache-dynamic-eviction-via-cumulative-attention-importance-on-cpu-78c6059820a3-20260521T193402814407+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b6ddeeefe823

## What looked useful

Raw cumulative attention eviction is brittle because new zero-score KV entries are evicted before becoming useful. Adding a protected recent window and decay fixes that failure mode and can reduce evicted attention mass on delayed-retrieval and shifting-anchor traces, but gains over LRU are pattern-dependent and not paper-ready without real-model validation.

## Boundaries and scale limits

No real transformer model, no perplexity/task metric, no production KV-cache implementation, no latency/memory allocator benchmark, and no large-context serving workload. Evidence is bounded to synthetic future-attention retention under sequence lengths up to 2048 and budgets 128/256/512.

## Claim scope

Dependency-free synthetic attention-trace proxy on CPU: raw cumulative-attention KV eviction, protected-recent cumulative eviction, and decayed protected-recent cumulative eviction compared against FIFO/LRU-like baselines over five deterministic patterns and budget sensitivity checks.

## Why it stopped

Proxy mechanism test completed: raw cumulative eviction is an early synthetic falsification as a standalone rule, while protected variants are only a useful signal requiring direct model evidence before any paper claim.

## Recommended next action

Run a bounded real-model follow-up with a small decoder, actual attention weights, and fixed-window/LRU/cumulative+recent/decay-cumulative+recent comparisons on perplexity or retrieval accuracy plus decode latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV eviction test for protected cumulative attention importance
- Success threshold: Decay-cumulative+recent must reduce loss or improve retrieval accuracy by at least 5% relative to the strongest recency/LRU baseline at the same KV budget while adding less than 10% decode overhead on the measured small-model setup.
- Stop condition: Stop if the protected cumulative variants fail to beat the strongest recency/LRU baseline on both real-model loss and retrieval accuracy at two matched budgets, or if bookkeeping overhead exceeds 10% without accuracy gain.

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-dynamic-eviction-via-cumulative-attention-importance-on-cpu-78c6059820a3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
