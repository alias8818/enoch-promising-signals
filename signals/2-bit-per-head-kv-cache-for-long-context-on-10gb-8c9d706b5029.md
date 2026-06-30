# 2-Bit Per-Head KV Cache for Long Context on 10GB

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `2-bit-per-head-kv-cache-for-long-context-on-10gb-8c9d706b5029`
Run ID: `2-bit-per-head-kv-cache-for-long-context-on-10gb-8c9d706b5029-20260529T234743767510+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3f2524755b31

## What looked useful

Coarse per-head int2 is an early negative as a drop-in KV cache: synthetic relative L2 attention-output error was 2.14-4.39 with top-1 attention agreement 0.12-0.27, and GPT-2 top-1 changed. Per-token/head metadata improved some metrics and preserved GPT-2 top-1 in one prompt but still had high drift and only 5.33x compression.

## Boundaries and scale limits

Synthetic attention only up to sequence length 16384 with 16 heads and head_dim 64, plus one GPT-2-small 512-token real-activation probe; no dataset perplexity, no optimized packed-int2 CUDA kernel, no multi-prompt generation quality, and no 7B+ validation.

## Claim scope

Bounded GB10 tests show naive affine 2-bit per-head KV quantization reaches near-8x theoretical cache compression but produces large synthetic decode-attention output error and changes GPT-2-small next-token top-1 after all-layer cache quantization for one 512-token prompt.

## Why it stopped

Proxy plus small real-activation evidence falsified the original coarse per-head 2-bit KV cache quality target; this is not a full validation, but a kernel-speed follow-up would not address the observed fidelity failure.

## Recommended next action

Stop this project as an early negative for coarse per-head int2; if continuing adjacent work, run a bounded GPT-2-small dataset perplexity probe for per-token/head or mixed-precision residual KV quantization before any larger model scale-up.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dataset perplexity probe for finer-grained 2-bit KV cache variants
- Success threshold: Perplexity degradation <=10% versus FP16, top-1 agreement >=90% over sampled next-token probes, and effective KV-cache compression >=4x including metadata.
- Stop condition: Stop if perplexity degradation exceeds 25% or top-1 agreement is below 75% on the bounded validation subset, because that would confirm the fidelity problem before scale-up.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-per-head-kv-cache-for-long-context-on-10gb-8c9d706b5029`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
