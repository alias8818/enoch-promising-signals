# Anchor-Indexed KV Cache for CPU Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `anchor-indexed-kv-cache-for-cpu-long-context-982e94c92a3e`
Run ID: `anchor-indexed-kv-cache-for-cpu-long-context-982e94c92a3e-20260528T003343002695+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/93859ccdeb1f

## What looked useful

Mean-key anchors carry coarse relevance: clustered synthetic cases reached 98.6% average any-top-8 recall at a 12.5% candidate budget. But they are not accurate enough for drop-in approximate KV attention: clustered top-1 recall averaged only 52.8%, 65K clustered top-1 recall was 49.0%, attention mass recall stayed below 19%, and output cosine stayed near 0.5. CPU speedup was inconsistent and disappeared at 65K for larger candidate budgets.

## Boundaries and scale limits

Synthetic keys/values only; no real transformer KV tensors, no task accuracy, no multi-layer model evaluation, no production cache layout, and no optimized custom kernels. Context length capped at 65K tokens and dimension at 128.

## Claim scope

Synthetic CPU single-query decode benchmark for mean-key block anchors over 8K, 32K, and 65K cached-token contexts with exact dense attention as the control.

## Why it stopped

Proxy/synthetic early falsification of the mean-anchor mechanism as a faithful drop-in CPU long-context KV-cache approximation, not a full validation of all possible anchor-indexed cache designs.

## Recommended next action

Stop this mean-anchor variant as no-paper evidence; a bounded follow-up should test multi-anchor or learned-anchor block retrieval on real model KV tensors before any larger systems effort.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-anchor KV block retrieval on real decoder KV tensors
- Success threshold: At 32K and 65K contexts, achieve >=0.95 exact top-1 recall, >=0.95 output cosine, and >=2x median CPU latency speedup versus dense attention at <=12.5% candidate-token budget on real KV tensors.
- Stop condition: Stop if multi-anchor or learned-anchor retrieval at a 12.5% candidate-token budget remains below 0.90 top-1 recall or below 0.90 output cosine on real KV tensors, because larger systems optimization would be premature.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-indexed-kv-cache-for-cpu-long-context-982e94c92a3e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
