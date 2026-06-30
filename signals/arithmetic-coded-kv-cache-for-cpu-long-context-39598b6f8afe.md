# Arithmetic-Coded KV-Cache for CPU Long-Context

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `arithmetic-coded-kv-cache-for-cpu-long-context-39598b6f8afe`
Run ID: `arithmetic-coded-kv-cache-for-cpu-long-context-39598b6f8afe-20260528T210643228043+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2f06b4594a63

## What looked useful

Packed int4 plus scales reduced raw fp16 KV size by 3.56x with median cosine 0.9943. Empirical arithmetic-coding lower bound improved this to median 4.00x, while zlib entropy proxy achieved median 3.94x. Entropy decode plus int4 unpack/dequantize/attention was median 18.1x slower than raw fp16 attention proxy, so arithmetic-coded KV is not attractive without a much faster block-random-access codec and real-trace entropy advantage.

## Boundaries and scale limits

No real model KV traces, no compiled arithmetic/range/ANS codec, no random-access cache layout, no end-to-end transformer perplexity or token-latency measurement. Tested sequence lengths 1024, 4096, and 8192 with 8 heads and 64-dimensional heads on one CPU worker.

## Claim scope

Bounded CPU proxy on synthetic KV-cache-shaped tensors shows blockwise int4 compression gives useful memory reduction, but entropy/arithmetic-style coding has limited incremental size headroom and large decode/dequantization overhead relative to raw attention proxy.

## Why it stopped

Proxy evidence supports compression but early-falsifies the practical CPU-serving value of arithmetic coding as implemented or bounded here: the incremental size gain over packed int4 is small and decode/dequantization overhead dominates raw attention proxy time.

## Recommended next action

Stop this as a no-paper useful signal; any next test should first use real model KV traces and a compiled block-random-access entropy codec against a packed-int4 baseline before claiming latency viability.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace block entropy coding against packed-int4 KV baseline
- Success threshold: Entropy-coded int4 must reduce total KV bytes by at least 20% versus packed int4 including metadata, keep p95 token latency no more than 10% worse than packed int4, and show no material quality regression beyond the packed-int4 baseline.
- Stop condition: Stop if real-trace int4 entropy bound is less than 15% better than packed int4, or if compiled decode plus dequantization is more than 2x slower than packed-int4 decode/dequantization before attention.

## Evidence references

- Artifact root: `<local-path>/projects/arithmetic-coded-kv-cache-for-cpu-long-context-39598b6f8afe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
