# 4-Bit KV Cache with N-Gram CPU Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-kv-cache-with-n-gram-cpu-drafting-b314f727bb41`
Run ID: `4-bit-kv-cache-with-n-gram-cpu-drafting-b314f727bb41-20260608T230513332333+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/767958d5e25e

## What looked useful

Memory compression alone was not enough: unfused 4-bit KV dequantization dominated decode latency, and ordinary CPU n-gram drafting accepted only 0.003-0.077 tokens per evaluated context in the trace.

## Boundaries and scale limits

Not an end-to-end LLM serving run; no fused int4 attention kernel; no production transformer cache integration; n-gram drafting measured on Tiny Shakespeare token traces rather than real model speculative decoding.

## Claim scope

On GB10, a self-contained proxy benchmark found that a naive packed-int4 KV cache with per-step unpack/dequant saves about 3.76x KV memory but is 4.3x-11.1x slower than fp16 decode attention for the tested shapes; CPU n-gram drafting is cheap but has low exact-match acceptance on the tested text trace.

## Why it stopped

Proxy/early falsification of the naive implementation path: the tested packed-int4 KV cache was materially slower than fp16 despite memory savings, and the tested n-gram drafting acceptance was too low to compensate.

## Recommended next action

Stop this run as a no-paper useful signal; only continue if implementing a fused packed-int4 decode-attention kernel and measuring integrated speculative decoding acceptance.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused packed-int4 KV attention with real-model n-gram speculative decoding
- Success threshold: Combined fused-int4 plus n-gram decoding improves end-to-end tokens/sec or fixed-latency concurrency by at least 20% versus fp16 baseline at 16k context, with no more than 1% task-quality degradation on the chosen evaluation set.
- Stop condition: Stop if fused int4 attention remains more than 1.2x slower than fp16 at 16k context, or if real-model n-gram drafting accepts fewer than 0.2 tokens per target forward pass.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-kv-cache-with-n-gram-cpu-drafting-b314f727bb41`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
