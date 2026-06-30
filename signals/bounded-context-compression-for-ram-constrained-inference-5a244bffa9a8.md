# Bounded Context Compression for RAM-Constrained Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-context-compression-for-ram-constrained-inference-5a244bffa9a8`
Run ID: `bounded-context-compression-for-ram-constrained-inference-5a244bffa9a8-20260607T044608696842+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d189e1faa4bf

## What looked useful

Frequency-aware bounded compression produced +0.142 to +0.151 absolute overall accuracy gains over recent-window at alpha 0.8 and +0.185 to +0.253 long-lag gains; at alpha 1.1 long-lag gains were about +0.249 to +0.270. Uniform access showed near-zero overall gain. A naive fixed-slot fingerprint hash compressor underperformed recency overall on skewed workloads.

## Boundaries and scale limits

Synthetic trace only; no transformer inference, learned compressor, real token/KV-cache state, serving latency, or real task quality was measured. Sweep used up to 80,000 updates, 4,096 keys, budgets of 32-256 retained cells, and 5 seeds per condition.

## Claim scope

In a synthetic streaming key/value recall task with Zipf-skewed access, LFU-style bounded context summaries improve long-lag recall over a same-entry recent-window baseline; under uniform access they do not materially improve overall accuracy.

## Why it stopped

Proxy-only synthetic validation supports a mechanism but is not direct/full validation for RAM-constrained LLM inference.

## Recommended next action

Stop this run as no-paper useful signal; next direct evidence should test a small transformer or retrieval-augmented LM with the same-memory sliding-window control and real memory/latency/task-quality metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-transformer bounded context compression under equal KV-memory budgets
- Success threshold: At equal peak memory, the compressor improves long-range task accuracy by at least 5 absolute points over sliding window on a structured workload, loses no more than 2 points on low-skew control workload, and adds less than 15% latency.
- Stop condition: Stop if same-memory compressor gain is below 2 absolute points on structured workload or if latency/memory overhead exceeds the budget before quality improves.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-context-compression-for-ram-constrained-inference-5a244bffa9a8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
