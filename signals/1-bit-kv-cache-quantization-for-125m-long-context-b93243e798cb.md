# 1-Bit KV Cache Quantization for 125M Long Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `1-bit-kv-cache-quantization-for-125m-long-context-b93243e798cb`
Run ID: `1-bit-kv-cache-quantization-for-125m-long-context-b93243e798cb-20260524T165041427179+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/43764c537a02

## What looked useful

1-bit KV with fp16 per-token scales gives an estimated 12.8x KV memory compression for a 12-layer, 12-head, head_dim 64 model, reducing 125k-token KV from 4.29 GiB fp16 to 0.335 GiB. However, naive sign KV produced mean attention-output relative L2 around 0.59-0.62, cosine around 0.79-0.80, and attention top-1 preservation only 9-20% across 1k-65k contexts. At 65,536 tokens with noisy needle rho 0.7, full precision and 4-bit controls kept 100% target retrieval while 1-bit fell to 85.9% with mean target rank 5.4.

## Boundaries and scale limits

No real GPT-2-small activation replay, perplexity, generation-quality, bit-packed kernel throughput, or trained long-context model evaluation was performed. The result does not rule out learned, residual, mixed-precision, or activation-calibrated 1-bit KV schemes.

## Claim scope

Naive per-token sign-quantized 1-bit KV cache at GPT-2-small head dimension shows large attention-output distortion despite strong KV memory compression; evidence is from synthetic CUDA attention-cache probes up to 65,536 tokens plus memory estimates for 125k and 1M tokens.

## Why it stopped

Proxy/early falsification: direct synthetic attention-cache probes found large quality distortion for naive sign KV even though memory compression is attractive; full validation would require real model activation replay and perplexity/generation tests.

## Recommended next action

Stop this naive 1-bit drop-in KV path as a no-paper useful signal; only continue with a bounded follow-up that tests a compensated 1-bit method on real GPT-2-small activation replay/perplexity against fp16 and 4-bit controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-Replay Test of Compensated 1-Bit KV Cache for GPT-2-Small
- Success threshold: Compensated 1-bit achieves attention-output relative L2 <= 0.15, next-token loss/perplexity degradation <= 5% versus fp16, and effective KV compression >= 8x while matching or beating the 4-bit control on memory.
- Stop condition: Stop if compensated 1-bit exceeds 0.25 attention-output relative L2 or 10% perplexity degradation on the activation replay, or if metadata reduces effective compression below 8x.

## Evidence references

- Artifact root: `<local-path>/projects/1-bit-kv-cache-quantization-for-125m-long-context-b93243e798cb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
