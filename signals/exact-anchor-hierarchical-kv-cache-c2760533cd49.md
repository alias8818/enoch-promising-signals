# Exact-Anchor Hierarchical KV Cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-hierarchical-kv-cache-c2760533cd49`
Run ID: `exact-anchor-hierarchical-kv-cache-c2760533cd49-20260604T105614290827+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/2322373383a0

## What looked useful

Exact anchors preserve exact retrieval for anchor positions and reduce cache entries, but block summaries cannot preserve exact non-anchor retrieval because the exact non-anchor key/value slot and index are absent. Across strides 4, 8, 16, and 32, full KV achieved 100% non-anchor top-1 retrieval while the hierarchical cache achieved 0%.

## Boundaries and scale limits

No trained transformer, tokenizer, multi-layer residual dynamics, autoregressive generation loop, GPU serving kernel, or real long-context benchmark was tested. Results are proxy evidence for the cache mechanism, not full deployment validation.

## Claim scope

Synthetic single-head attention probe of exact-anchor hierarchical KV caching with fixed anchors and block-mean summaries at sequence lengths up to 4096, dimension 64, and 300 trials.

## Why it stopped

The current exact-anchor plus block-summary mechanism fails a direct synthetic exact-retrieval requirement for non-anchor tokens; this is not a full validation, but it is sufficient no-paper evidence against the broad cache claim as tested.

## Recommended next action

Stop this run as a proxy early falsification of exact non-anchor retrieval; run a bounded adjacent test of adaptive exact-token promotion if continuing the line.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Exact-Token Promotion for Hierarchical KV Cache
- Success threshold: At no more than 25% of full KV entries, achieve at least 95% exact top-1 retrieval for both anchor and non-anchor targets and hierarchical output cosine at least 0.80 on seq_len 2048 and dim 64.
- Stop condition: Stop if non-anchor exact top-1 remains below 95% at 25% memory after testing promotion budgets and strides 4, 8, and 16.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-hierarchical-kv-cache-c2760533cd49`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
