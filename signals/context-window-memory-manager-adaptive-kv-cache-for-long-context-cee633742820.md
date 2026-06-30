# Context Window Memory Manager: Adaptive KV Cache for Long Context

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `context-window-memory-manager-adaptive-kv-cache-for-long-context-cee633742820`
Run ID: `context-window-memory-manager-adaptive-kv-cache-for-long-context-cee633742820-20260613T185531001842+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/5d0558a2f703

## What looked useful

The tested adaptive split did not consistently outperform simple fixed controls. Across 72 condition/seed pairs, adaptive minus fixed 50/50 mean hit-rate delta was +0.00067 and median was -0.00083; adaptive minus best non-full baseline mean delta was -0.01119 and was positive in only 14/72 pairs.

## Boundaries and scale limits

Proxy-only CPU simulation; no transformer model, no per-layer/head KV tensors, no LongBench or Needle-in-a-Haystack task accuracy, no latency or GPU-memory measurement. Does not evaluate stronger published adaptive methods directly.

## Claim scope

Synthetic long-context target-retention traces at sequence length 4096, 1200 events, 8 seeds, 2-8% KV budgets, comparing a naive adaptive recency/importance split against recency, heavy-hitter, and fixed 50/50 baselines.

## Why it stopped

Proxy early falsification: the naive adaptive recency-versus-importance manager failed to beat simple fixed baselines on the direct synthetic retention objective, so scaling this exact mechanism is not justified.

## Recommended next action

Stop this specific approach unless a future implementation uses a stronger task/head/layer signal and compares directly against H2O/FastGen/SnapKV/DynamicKV-style baselines.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/context-window-memory-manager-adaptive-kv-cache-for-long-context-cee633742820`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
