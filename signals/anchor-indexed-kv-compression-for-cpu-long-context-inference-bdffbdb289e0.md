# Anchor-Indexed KV Compression for CPU Long-Context Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-kv-compression-for-cpu-long-context-inference-bdffbdb289e0`
Run ID: `anchor-indexed-kv-compression-for-cpu-long-context-inference-bdffbdb289e0-20260523T103904437065+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/8e30b7823e28

## What looked useful

Anchor-only KV compression gives large CPU speedups and memory reduction when targets are anchor-aligned but fails on off-anchor retrieval. Oracle-hot non-anchor retention restores synthetic output accuracy while preserving large compression, suggesting the next useful question is causal hot-entry discovery rather than anchor-only retention.

## Boundaries and scale limits

No real LLM layers, no perplexity or task accuracy, no production inference engine, no causal online hot-entry policy, and no validation beyond 16k-token synthetic KV traces.

## Claim scope

Synthetic CPU one-step attention traces with sequence lengths 4096-16384, dimension 64, 48 decode queries, and periodic anchor compression plus optional oracle-hot non-anchor retention.

## Why it stopped

No-paper useful signal: bounded synthetic evidence rejects anchor-only compression as a general method and the positive oracle-hot result is an optimistic proxy, not full validation.

## Recommended next action

Run a bounded follow-up on saved real-model attention traces comparing causal hot-entry selection policies against full KV and anchor-only compression.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Causal Hot-Entry Selection for Anchor-Indexed KV Compression
- Success threshold: A causal policy reaches median attention-output relative L2 error below 0.05 or task/perplexity degradation within 5% of full KV while preserving at least 8x KV memory reduction and improving CPU decode latency over full KV.
- Stop condition: Stop if causal policies cannot exceed 50% off-anchor target retention or require less than 8x memory reduction to meet the accuracy threshold.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-kv-compression-for-cpu-long-context-inference-bdffbdb289e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
