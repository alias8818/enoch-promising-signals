# 2-bit KV cache with outlier residual channel for long-context inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-outlier-residual-channel-for-long-context-inference-4206b3381717`
Run ID: `2-bit-kv-cache-with-outlier-residual-channel-for-long-context-inference-4206b3381717-20260611T203827638642+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/083e54a74394

## What looked useful

At 3% retained channels, fixed-channel outlier relative output MSE fell from 4.2774 for plain 2-bit to 0.4048 at about 2.44 idealized bits/element, while moving-token outlier MSE remained high at 23.1628. A 128-token recent residual alone did not help the fixed-channel case.

## Boundaries and scale limits

Tested only synthetic K/V tensors at seq_len 8192, dim 128, 128 decode queries, up to 5 seeds. No real transformer KV traces, perplexity, downstream tasks, kernel packing, metadata overhead, or serving throughput were measured.

## Claim scope

Synthetic long-context decode-attention probes show that a small fp16 residual over fixed high-magnitude feature channels can greatly reduce 2-bit KV attention-output error when outliers are stable channels, but it does not solve moving token-local outlier error.

## Why it stopped

No-paper closure: proxy evidence supports a conditional mechanism but is insufficient for a publication-grade long-context inference claim.

## Recommended next action

Run a bounded deepen follow-up that captures real per-layer KV traces from a small long-context transformer and repeats the same residual-channel versus recent-token comparison before considering kernel or task-level work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model KV trace test for 2-bit residual outlier channels
- Success threshold: At matched or lower effective memory than a 128-token recent residual, residual channels reduce mean per-layer attention-output error by at least 50% versus plain 2-bit on real KV traces and show consistent benefit across most tested layers/heads.
- Stop condition: Stop if real KV outliers are not persistent channels or residual-channel retention improves attention-output error by less than 20% versus plain 2-bit at comparable memory.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-outlier-residual-channel-for-long-context-inference-4206b3381717`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
