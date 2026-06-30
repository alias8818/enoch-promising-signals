# Memory-Constrained KV Compression for Agent Reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `memory-constrained-kv-compression-for-agent-reliability-6f01c36070bd`
Run ID: `memory-constrained-kv-compression-for-agent-reliability-6f01c36070bd-20260607T132638580516+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/143d4d45374d

## What looked useful

Across 24,000 synthetic trials, the best compressed retention method beat fp16 recency eviction by a mean absolute accuracy delta of 0.594 across 16 cells. At context length 4096 with a 256-fp16-token byte budget, fp16 recency reached 0.053 uniform accuracy and 0.007 old-quartile accuracy, while the best compressed stratified policy reached 0.397 and 0.253 respectively. Full-cache controls reached 1.0 accuracy for fp16/int8/int4, confirming the task is solvable when K/V is retained.

## Boundaries and scale limits

No real LLM, no multi-layer KV cache, no agent tool-use benchmark, no latency/kernel measurement, and only synthetic random-vector facts on a CPU-only short run.

## Claim scope

In a synthetic associative-recall proxy, low-bit KV retention under equal estimated byte budgets improves recall over fp16 recency eviction mainly by retaining more target facts; old-fact reliability additionally requires a temporal coverage policy such as stratified retention.

## Why it stopped

Proxy evidence supports the retention mechanism but is not direct/full validation of agent reliability or production KV compression.

## Recommended next action

Run a bounded direct small-LLM KV-cache follow-up on needle-in-haystack or agent-memory tasks with matched byte budgets and latency accounting; stop this run as no-paper proxy evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LLM KV Compression on Needle-in-Haystack Memory Reliability
- Success threshold: At least +10 percentage-point absolute task accuracy over fp16 recency eviction at one constrained budget and context length, with less than 25% decode-latency overhead and full-cache control above 90% accuracy.
- Stop condition: Stop if compressed policies fail to beat fp16 recency by 5 percentage points on direct LLM task accuracy after matched-budget implementation and verified full-cache control.

## Evidence references

- Artifact root: `<local-path>/projects/memory-constrained-kv-compression-for-agent-reliability-6f01c36070bd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
