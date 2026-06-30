# INT4 KV Cache for GPT-2 on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-kv-cache-for-gpt-2-on-cpu-412db3307707`
Run ID: `int4-kv-cache-for-gpt-2-on-cpu-412db3307707-20260609T034754577390+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0b02e3d6188e

## What looked useful

At 1024 tokens, FP32 KV cache is 6.000 MiB/layer and 72.000 MiB for 12 layers; INT4 is 0.844 MiB/layer and 10.125 MiB for 12 layers. The measured INT4 path was 3.5797 ms/layer-token versus 1.4116 ms for FP32, a 2.54x slowdown, with mean absolute attention-output error 0.0063 and max absolute error 0.0346.

## Boundaries and scale limits

Tested only one-layer decode attention at GPT-2-small dimensions with synthetic normally distributed Q/K/V and prefixes up to 1024 tokens. Did not test full GPT-2 logits, perplexity, end-to-end tokens/sec, batching, or hand-optimized AVX2/AVX512 INT4 kernels.

## Claim scope

For a standalone GPT-2-small-shaped CPU decode-attention microbenchmark using packed symmetric INT4 K/V with per-token/head FP32 scales, INT4 reduces KV-cache bytes by 7.11x and keeps synthetic attention-output absolute error small, but is slower than FP32 attention on the tested CPU implementation.

## Why it stopped

Bounded direct microbenchmark found useful memory compression and acceptable synthetic attention error, but the tested CPU INT4 decode path was 2.1x-3.2x slower than FP32 and GPT-2-small KV cache memory is modest.

## Recommended next action

Stop this run as no-paper useful evidence; only pursue a follow-up if implementing a native AVX2/AVX512 INT4 dequantized attention kernel and measuring full GPT-2-small perplexity/logit drift is in scope.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: AVX2/AVX512 INT4 KV decode-attention kernel for GPT-2-small CPU inference
- Success threshold: At 1024-token prefix, INT4 attention latency no worse than 1.1x FP32 attention, at least 6x KV-cache memory reduction after metadata, and full-model perplexity/logit drift within a predeclared acceptable tolerance.
- Stop condition: Stop if the optimized kernel remains more than 1.5x slower than FP32 at 1024 tokens or if full-model quality drift is unacceptable despite the memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/int4-kv-cache-for-gpt-2-on-cpu-412db3307707`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
