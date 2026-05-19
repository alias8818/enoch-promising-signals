# Anchor-Gated KV Compression with Exact Positional Retrieval

Status: `useful_signal`
Project ID: `anchor-gated-kv-compression-with-exact-positional-retrieval-2578d1fa81f9`
Run ID: `anchor-gated-kv-compression-with-exact-positional-retrieval-2578d1fa81f9-20260516T061020279970+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b95f71247f67

## What looked useful

Anchor positions are retrieved exactly, but non-anchor exact retrieval fails whenever compression causes multiple offsets to share a slot. Exact accuracy reaches 1.0 only when slots equal block size, which has compression ratio 1.0 and is dense storage.

## Boundaries and scale limits

No trained Transformer, language-model perplexity, real KV-cache throughput, learned routing, or semantic redundancy evaluation was run. The result is a direct synthetic falsification of exact arbitrary retrieval, not a full model-scale validation.

## Claim scope

Synthetic exact positional retrieval of arbitrary random per-position values using anchor-gated folded-slot KV compression at sequence lengths 512, 2048, and 8192 with block sizes 8, 16, and 32.

## Why it stopped

A direct synthetic proxy for exact arbitrary positional retrieval showed that anchor-gated compression loses non-anchor identity under real compression; this is not a full trained-model validation.

## Recommended next action

Stop this exact-retrieval claim as a proxy early falsification; only pursue a narrowed follow-up that targets approximate or semantically redundant retrieval under a fixed KV budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Content-aware anchor KV compression for approximate redundant retrieval
- Success threshold: At the same KV memory budget, the content-aware anchor method improves non-anchor retrieval accuracy or task loss by at least 10% relative over fixed-stride compressed controls while preserving anchor-position accuracy near dense.
- Stop condition: Stop if non-anchor retrieval remains within 2% relative of fixed compressed controls or if gains vanish when labels are not redundant.

## Evidence references

- Artifact root: `<local-path>/projects/anchor-gated-kv-compression-with-exact-positional-retrieval-2578d1fa81f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
