# Per-channel int8 KV cache for CPU inference memory reduction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-channel-int8-kv-cache-for-cpu-inference-memory-reduction-c60b1efa9419`
Run ID: `per-channel-int8-kv-cache-for-cpu-inference-memory-reduction-c60b1efa9419-20260522T134734333449+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c1981d2fd8ee

## What looked useful

The memory-reduction mechanism is directly supported and numerical error is low on synthetic attention tensors, but latency benefit appears context-dependent in the scalar CPU path and the result is not paper-ready.

## Boundaries and scale limits

No real model, tokenizer, perplexity, downstream task, production runtime, multi-layer end-to-end serving, or optimized AVX512/VNNI kernel was tested. Largest proxy was 16 heads x 4096 sequence x 64 head dimension on synthetic tensors.

## Claim scope

Synthetic single-thread CPU attention microbenchmark: per-channel int8 K/V cache with fp32 scales per head-dimension channel reduces estimated KV-cache bytes to about 25.0-25.8% of fp32 and 50.0-51.6% of fp16-equivalent, with max relative L2 output error about 0.0042; scalar latency is slower at 128-512 tokens and faster at 2048-4096 tokens.

## Why it stopped

Closed as no-paper useful signal because evidence is a synthetic attention microbenchmark, not direct end-to-end model inference validation.

## Recommended next action

Run a bounded real CPU LLM-runtime follow-up on a small open model, comparing fp16/bf16 KV cache against per-channel int8 KV cache for RSS, tokens/sec, and perplexity or task quality over long-context prompts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real CPU runtime validation of per-channel int8 KV cache
- Success threshold: At long context, measured peak RSS drops by at least 35%, tokens/sec is no worse than 10% below fp16/bf16 baseline, and perplexity or task quality remains within 1% relative of baseline.
- Stop condition: Stop if real-model quality degrades by more than 1% relative at the target context length or tokens/sec regresses by more than 10% after a reasonable vectorized implementation attempt.

## Evidence references

- Artifact root: `<local-path>/projects/per-channel-int8-kv-cache-for-cpu-inference-memory-reduction-c60b1efa9419`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
