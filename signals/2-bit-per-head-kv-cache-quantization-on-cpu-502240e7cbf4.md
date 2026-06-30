# 2-bit Per-Head KV Cache Quantization on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `2-bit-per-head-kv-cache-quantization-on-cpu-502240e7cbf4`
Run ID: `2-bit-per-head-kv-cache-quantization-on-cpu-502240e7cbf4-20260602T131412948481+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/267e7cf44e81

## What looked useful

Per-head 2-bit affine KV quantization preserves the same approximate 8x storage reduction versus fp16 while improving attention KL and output relative L2 versus a global 2-bit quantizer, especially under head-wise dynamic-range heterogeneity. However, absolute output distortion remains large and the naive CPU dequantize-then-attend path is 4.6-10.4x slower than fp32 attention, so storage compression alone is not a viable CPU decode result.

## Boundaries and scale limits

No real model traces, no perplexity/task evaluation, no multi-layer decode loop, no fused CPU int2 kernel, no production serving stack; results are proxy evidence only.

## Claim scope

Synthetic CPU single-token attention benchmark with 12 heads, head_dim 64, sequence lengths 256/1024/4096, comparing global versus per-head 2-bit affine KV quantization and a naive dequantize-then-attend CPU path.

## Why it stopped

Proxy early falsification of the practical CPU-serving hypothesis for a naive implementation: per-head 2-bit helps versus global 2-bit, but quality is still poor and decode latency is several times slower than fp32 attention.

## Recommended next action

Stop this no-paper run; the concrete next bounded test is a fused/on-the-fly CPU int2 attention microkernel benchmark using the same metrics and a pass/fail threshold versus fp16/fp32 KV attention.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU int2 per-head KV attention microkernel
- Success threshold: Per-head int2 fused decode is at least 6x smaller than fp16 KV, has attention KL below 1.0 on heterogeneous-head tests, and has median decode latency no worse than 1.5x the fp32/fp16 baseline at seq_len 4096.
- Stop condition: Stop if the fused kernel remains above 2x baseline latency or if per-head int2 KL stays above 1.0 after using the same quantization granularity and tested sequence lengths.

## Evidence references

- Artifact root: `<local-path>/projects/2-bit-per-head-kv-cache-quantization-on-cpu-502240e7cbf4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
