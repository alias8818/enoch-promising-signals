# Hierarchical memory compressor for CPU long-context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-memory-compressor-for-cpu-long-context-7e4ae0506bc0`
Run ID: `hierarchical-memory-compressor-for-cpu-long-context-7e4ae0506bc0-20260527T213140983290+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/72faf9de0682

## What looked useful

Default compressor achieved 14.22x memory reduction and 2.38x speedup at 131072 tokens on topic-coherent traces with 1.000 segment recall and 0.971 top-1 segment match. On sparse exact needles at the same size it achieved 2.16x speedup but only 0.020 routed segment recall and 0.018 top-1 segment match. A wider 32768-token ablation improved needle recall to 0.350 but was slower than full scan and reduced memory savings to 3.88x.

## Boundaries and scale limits

Tested only synthetic normalized key/query traces up to 131072 tokens, 64 dimensions, 512 queries, one CPU process with NumPy. No transformer KV cache, no perplexity/task metric, no trained model, no production serving trace.

## Claim scope

Bounded synthetic CPU proxy: centroid-plus-landmark hierarchical compression can reduce memory and become faster than full key scan on topic-coherent segment retrieval, but does not preserve sparse exact-token retrieval.

## Why it stopped

Early proxy falsification rather than full validation: centroid/landmark hierarchy is conditionally useful for topic-coherent retrieval but structurally weak for exact sparse long-context retrieval.

## Recommended next action

Stop this broad compressor claim as no-paper; the next bounded test should add a content-addressed fallback to the hierarchy and require high needle recall without giving up the CPU/memory benefit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hierarchical centroid memory with content-addressed sparse fallback
- Success threshold: At 32768 tokens and 64 dimensions, needle_exact top-1 segment match >= 0.90, topic_coherent segment recall >= 0.98, memory reduction >= 4x, and hmc_total_ms_per_query <= full_scan_ms_per_query.
- Stop condition: Stop if needle_exact top-1 segment match remains below 0.75 at 32768 tokens under any configuration with memory reduction >= 4x and latency parity.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-memory-compressor-for-cpu-long-context-7e4ae0506bc0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
