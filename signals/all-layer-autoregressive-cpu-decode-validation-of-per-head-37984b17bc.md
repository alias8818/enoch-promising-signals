# All-layer autoregressive CPU decode validation of per-head int8 KV cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `all-layer-autoregressive-cpu-decode-validation-of-per-head-37984b17bc`
Run ID: `all-layer-autoregressive-cpu-decode-validation-of-per-head-37984b17bc-20260605T161915298963+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Natural-text long-context CPU validation of per-head int8 KV cache: enoch://control-plane/projects/natural-text-long-context-cpu-validation-of-per-head-int8-2c5f48ca14/runs/natural-text-long-context-cpu-validation-of-per-head-int8-2c5f48ca14-20260605T095744012656+0000
- Parent run decision: Real-model CPU validation of per-head int8 KV cache: enoch://control-plane/projects/real-model-cpu-validation-of-per-head-int8-kv-cache-6e23fdfd95/runs/real-model-cpu-validation-of-per-head-int8-kv-cache-6e23fdfd95-20260605T051944433397+0000

## What looked useful

Per-layer/head int8 KV cache is a plausible approximate-compression mechanism but not a lossless greedy-decode substitute at this horizon. It achieved about 4x theoretical KV-cache compression with low mean KL drift, but greedy decode diverged on 4/16 prompts at 64 tokens and 6/16 prompts at 128 tokens. A finer per-token/head scaling control was more stable but still diverged on 2/16 prompts at 128 tokens and has more scale metadata.

## Boundaries and scale limits

Tested only GPT-2 small with 16 hand-written prompts, greedy decoding, 64- and 128-token continuations, and a functional quantize/dequantize harness using Transformers DynamicCache. The harness does not implement packed int8 attention, does not reduce observed RSS, does not test larger models, sampling, long contexts beyond 128 generated tokens, perplexity corpora, or production CPU kernels.

## Claim scope

On GPT-2 small CPU autoregressive decode over 16 fixed prompts, all-layer per-layer/head symmetric int8 KV-cache quantization preserves teacher-forced next-token top-1 agreement at 99.4-99.6% and gives about 4x theoretical KV-cache compression, but it does not preserve greedy generation exactly over 64-128 generated tokens.

## Why it stopped

Bounded direct validation found mixed functional behavior: the mechanism mostly preserves teacher-forced top-1 predictions but greedy autoregressive divergence is common enough that the result is not paper-positive or deployment-ready.

## Recommended next action

Stop this run as no-paper useful evidence; next implement a true packed int8 CPU KV-cache attention path and rerun the same 64/128-token protocol with actual RSS and throughput measurements before making systems claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed CPU int8 KV-cache attention validation for GPT-2 decode
- Success threshold: At 512 generated tokens on GPT-2 small CPU decode, show at least 3.5x observed KV-cache memory reduction versus fp32, teacher-forced top-1 match at least 99%, mean KL drift below 0.001 for the chosen scaling mode, and no more than 10% tokens/second regression versus fp32 cache decode.
- Stop condition: Stop if packed-cache attention cannot achieve at least 2x observed KV memory reduction, if teacher-forced top-1 match falls below 98% on the fixed protocol, or if CPU throughput regresses by more than 25% after straightforward vectorization.

## Evidence references

- Artifact root: `<local-path>/projects/all-layer-autoregressive-cpu-decode-validation-of-per-head-37984b17bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
