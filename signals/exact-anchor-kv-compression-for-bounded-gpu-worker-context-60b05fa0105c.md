# Exact-Anchor KV Compression for Bounded GPU Worker Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-kv-compression-for-bounded-gpu-worker-context-60b05fa0105c`
Run ID: `exact-anchor-kv-compression-for-bounded-gpu-worker-context-60b05fa0105c-20260612T022234055631+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f0e02bdbdc90

## What looked useful

Exact anchors cut relative MSE to 0.3305 of the uniform-compression baseline in the anchor-sensitive synthetic regime with 24/24 wins, but were neutral or slightly worse in mixed and no-anchor controls where anchor attention mass was low.

## Boundaries and scale limits

No real LLM generation, no real long-context dataset, no layerwise/headwise transformer KV traces, no optimized FlashAttention integration, and no comparison against production KV-cache policies beyond uniform block compression and anchor-only sanity baseline.

## Claim scope

Synthetic attention reconstruction at seq_len 4096, dim 128, batch 128, 32 exact anchors, and 128/256/512 compressed KV slots: exact-anchor plus count-corrected block-mean residual compression reduces output relative MSE versus uniform block compression only when selected anchors receive meaningful attention mass.

## Why it stopped

Synthetic proxy evidence supports a conditional mechanism but is not direct/full validation of LLM KV-cache compression or serving quality.

## Recommended next action

Stop this worker run as no-paper useful signal; next bounded action is a real-model retrieval benchmark with online anchor selection, count-corrected residual compression, and equal-memory baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model exact-anchor KV compression on bounded retrieval tasks
- Success threshold: At least 10 percentage-point retrieval accuracy improvement over uniform compression at the same KV slot budget with less than 10% decode latency overhead on a bounded local model run.
- Stop condition: Stop if exact-anchor compression fails to beat uniform compression on retrieval accuracy in two distinct prompt templates or if latency overhead exceeds 25% at the tested budget.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-kv-compression-for-bounded-gpu-worker-context-60b05fa0105c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
