# Per-head KV cache quantization for CPU long-context inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `per-head-kv-cache-quantization-for-cpu-long-context-inference-a64cfca1b372`
Run ID: `per-head-kv-cache-quantization-for-cpu-long-context-inference-a64cfca1b372-20260524T195336519024+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5cef9dde20c1

## What looked useful

Per-head scaling is an accuracy mechanism: in the head-scale stress case at context 8192, output relative L2 error fell from 0.436 for global int8 to 0.0295 for per-head int8, while both int8 caches used about 25% of FP32 KV memory. Latency was negative in the tested implementation: per-head int8 took about 64 ms versus 38 ms FP32 single-thread at context 8192, and remained slower in the 8-thread check.

## Boundaries and scale limits

Synthetic K/V tensors only; no real transformer KV traces, no language-model perplexity, no end-to-end inference engine, no fused SIMD int8 attention kernel, contexts limited to 8192, and timing measured on one CPU worker.

## Claim scope

On synthetic CPU decode attention with target-shaped KV caches (8 heads, head_dim 64, contexts up to 8192), per-head int8 scales materially reduce quantization error versus one global int8 scale when head dynamic ranges differ, with negligible extra KV-cache metadata. The tested unfused NumPy CPU path does not improve latency because dequantization is included in the attention call.

## Why it stopped

Proxy/local experiment supports the per-head accuracy mechanism but early-falsifies a broad naive CPU speedup claim; this is not full validation on real model serving.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should use real small-transformer KV traces and a fused CPU int8 decode kernel before making any serving-speed claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-KV fused CPU decode test for per-head int8 cache quantization
- Success threshold: At context >=8192 on real model KV traces, per-head int8 should use <=30% of FP32 KV memory, reduce output error by at least 3x versus global int8 when head ranges differ, and achieve >=0.95x FP32 decode throughput with no material perplexity regression.
- Stop condition: Stop if real KV traces show no meaningful per-head error advantage over global int8, or if a fused implementation remains below 0.8x FP32 decode throughput at context >=8192.

## Evidence references

- Artifact root: `<local-path>/projects/per-head-kv-cache-quantization-for-cpu-long-context-inference-a64cfca1b372`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
