# Direct vLLM replay of wait-aware KV eviction under GPU cache pressure

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `direct-vllm-replay-of-wait-aware-kv-eviction-under-gpu-cac-982eceef76`
Run ID: `direct-vllm-replay-of-wait-aware-kv-eviction-under-gpu-cac-982eceef76-20260531T114853734843+0000`

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

- Parent run decision: KV-Cache Eviction Prioritized by Queue Wait Time: enoch://control-plane/projects/kv-cache-eviction-prioritized-by-queue-wait-time-c9f07a135d2a/runs/kv-cache-eviction-prioritized-by-queue-wait-time-c9f07a135d2a-20260530T065423904410+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/d04a9c2427be

## What looked useful

Wait-aware eviction priority is mechanically compatible with vLLM's KV block eviction path: reordering eviction candidates by request wait age changed actual vLLM block victims and preserved high-wait prefix-cache state under constrained cache capacity.

## Boundaries and scale limits

No GPU, no CUDA memory pressure, no full vLLM engine serving, no model kernels, no production vLLM wait-metadata patch, and only a tiny 6-usable-block cache with synthetic token prefixes.

## Claim scope

In a controlled CPU direct replay using vLLM 0.22.0 v1 KVCacheManager and BlockPool, wait-aware free-queue ordering preserved high-wait cached KV blocks under small cache pressure and retained vLLM-observable prefix-cache hits that default LRU lost at pressure 2 and 3.

## Why it stopped

Tier 1 controlled direct vLLM KV replay completed and produced useful mechanism support, but the evidence is not a full GPU serving validation or paper-ready result.

## Recommended next action

Implement a minimal vLLM patch that records request wait age on cached KV blocks and rerun the same repeated-prefix pressure workload on a GPU-capable vLLM worker with TTFT, prefix-hit, eviction-victim, and throughput metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPU vLLM serving test of wait-aware KV eviction under constrained cache
- Success threshold: Compared with default vLLM LRU/free-queue order, wait-aware eviction preserves at least 25% more high-wait prefix blocks or improves high-wait p95 TTFT by at least 10% while keeping aggregate throughput within 5%.
- Stop condition: Stop if the patch cannot alter actual vLLM eviction victims, if constrained GPU serving shows no high-wait prefix-hit or TTFT improvement at observed eviction pressure, or if throughput regresses by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/direct-vllm-replay-of-wait-aware-kv-eviction-under-gpu-cac-982eceef76`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
