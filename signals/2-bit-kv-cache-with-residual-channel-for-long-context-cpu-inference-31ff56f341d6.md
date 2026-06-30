# 2-bit KV cache with residual channel for long-context CPU inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-kv-cache-with-residual-channel-for-long-context-cpu-inference-31ff56f341d6`
Run ID: `2-bit-kv-cache-with-residual-channel-for-long-context-cpu-inference-31ff56f341d6-20260628T030407482442+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1bcbea3c9b85

## What looked useful

Residual channels are worth testing only if real model KV caches show stable channel salience. In the channel-salient proxy at context 8192, relative RMSE improved from 3.94 for plain int2 to 0.493 with 8 residual channels at 3.56x estimated compression; on Gaussian KV, RMSE stayed about 1.10.

## Boundaries and scale limits

No real transformer KV traces, no perplexity/retrieval benchmark, no packed int2 kernel, no end-to-end serving throughput. Contexts were synthetic arrays at 1024, 4096, and 8192 tokens with 8 heads, 64 head dimension, and 3 seeds.

## Claim scope

Bounded NumPy decode-attention proxy over synthetic KV caches: int2 quantization plus 8/64 fp16 residual channels substantially improves attention-output fidelity on channel-salient KV while retaining about 3.56x estimated KV-cache compression, but does not rescue isotropic KV and does not demonstrate CPU inference speed.

## Why it stopped

Proxy evidence is useful but mixed: it supports the residual-channel mechanism only under channel salience and provides no direct full-model quality or CPU throughput validation.

## Recommended next action

Run a bounded deepen follow-up on real small-transformer KV traces with int4 and fp16/bf16 controls before investing in a packed CPU kernel.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real small-transformer KV trace test for int2 residual-channel cache
- Success threshold: At least 3x KV-cache compression versus fp16 with next-token KL/perplexity degradation comparable to or better than int4, and consistent residual-channel salience across most layers/heads tested.
- Stop condition: Stop if real KV traces do not show stable channel salience or if int2 plus residual channels is worse than int4 at similar or lower memory on quality metrics.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-kv-cache-with-residual-channel-for-long-context-cpu-inference-31ff56f341d6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
