# Hierarchical Memory: Exact L1 Anchors, Compressed L2 State

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hierarchical-memory-exact-l1-anchors-compressed-l2-state-8ccd303d0510`
Run ID: `hierarchical-memory-exact-l1-anchors-compressed-l2-state-8ccd303d0510-20260528T012143979674+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/9bff071dd906

## What looked useful

Exact L1 anchors substantially reduce dense-attention approximation error when the dense target is an anchor, but they do not materially improve non-anchor copy or generic random-query attention over L2-only block summaries. Fixed periodic anchors are therefore a narrow recall aid, not a general replacement for dense memory.

## Boundaries and scale limits

No trained model, no real text corpus, no learned compression, no learned anchor selection, no downstream task quality, and no GPU efficiency study. The result supports only a mechanism-level conclusion for periodic anchors and mean L2 compression.

## Claim scope

Synthetic inference-time attention approximation with 4096-token random key/value memory, periodic exact L1 anchors, per-block mean-compressed L2 state, and dense softmax attention as the reference.

## Why it stopped

Proxy early falsification of the broad claim: periodic exact anchors plus compressed L2 state only help anchor-targeted retrieval and do not solve arbitrary non-anchor memory loss.

## Recommended next action

Stop this run as a no-paper useful signal; test content-adaptive exact anchors or residual top-k exact slots in a bounded follow-up before considering model-scale validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Content-Adaptive Exact Anchors for Compressed L2 Memory
- Success threshold: At 32x or better dense-memory compression, content-adaptive anchors reduce non-anchor copy relative error by at least 25% versus L2-only and improve a small downstream associative-recall metric without degrading anchor-copy performance.
- Stop condition: Stop if adaptive anchors fail to improve non-anchor copy error by at least 10% versus L2-only across 5 seeds, or if the method requires oracle future/query information unavailable in a causal deployment.

## Evidence references

- Artifact root: `<local-path>/projects/hierarchical-memory-exact-l1-anchors-compressed-l2-state-8ccd303d0510`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
