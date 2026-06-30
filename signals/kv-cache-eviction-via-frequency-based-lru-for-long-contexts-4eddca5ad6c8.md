# KV Cache Eviction via Frequency-Based LRU for Long Contexts

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `kv-cache-eviction-via-frequency-based-lru-for-long-contexts-4eddca5ad6c8`
Run ID: `kv-cache-eviction-via-frequency-based-lru-for-long-contexts-4eddca5ad6c8-20260609T221119606358+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/fc4580a78627

## What looked useful

Naive frequency-based LRU and simple frequency+recency scoring under-admitted new/recent tokens and lost consistently to access-LRU and sink/recent baselines. In the main sweep, lfu_lru trailed lru_access by 0.33-0.58 retained attention mass across all scenario/capacity cases.

## Boundaries and scale limits

No real model perplexity, task accuracy, serving latency, batching, paged-attention kernel, or real long-context dataset validation was run. This is not publication-grade evidence for deployed inference behavior.

## Claim scope

Synthetic trace-level online KV eviction over four long-context attention regimes, sequence lengths 2048-4096, cache fractions 3-20%, and retained-attention/top-token recall metrics.

## Why it stopped

Bounded proxy experiments falsified the simple mechanism: frequency-based LRU froze around old high-count tokens and retained far less attention mass than simpler recency/access baselines. This is proxy evidence, not full model validation.

## Recommended next action

Stop this idea as a standalone frequency-LRU proposal; any future work should first implement access-LRU/sink-recent/attention-score baselines in a real inference stack before revisiting frequency features.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/kv-cache-eviction-via-frequency-based-lru-for-long-contexts-4eddca5ad6c8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
