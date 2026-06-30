# Real CPU LLM Runtime Validation of Int8 KV Cache Compression

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-cpu-llm-runtime-validation-of-int8-kv-cache-compressi-1aa129ff0c`
Run ID: `real-cpu-llm-runtime-validation-of-int8-kv-cache-compressi-1aa129ff0c-20260609T220351864587+0000`

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

- Parent run decision: KV Cache Compression for CPU-Bounded Inference: enoch://control-plane/projects/kv-cache-compression-for-cpu-bounded-inference-2170028bcd69/runs/kv-cache-compression-for-cpu-bounded-inference-2170028bcd69-20260609T155214900888+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/11df40c64e18

## What looked useful

Int8 KV compression achieved 3.9995x-4.0000x storage reduction with about 1.25%-1.51% relative L2 output error, but median decode latency was 2.62x-9.51x slower than fp32 across tested context lengths because per-step dequantization dominated the simple CPU path.

## Boundaries and scale limits

Single-process NumPy CPU kernel on one 8-logical-CPU x86_64 host with BLAS thread caps set to 1; sequence lengths 512, 2048, and 8192; not an end-to-end LLM runtime, not a fused SIMD int8 attention kernel, and not a model-quality validation.

## Claim scope

Tier 1 direct CPU decode-attention microbenchmark: per-head symmetric int8 KV storage reduced KV bytes by about 4x but was slower than fp32 KV when K/V were dequantized to fp32 inside each decode step.

## Why it stopped

Bounded early falsification, not full validation: the direct CPU decode-kernel test failed the predefined runtime threshold even though memory compression worked.

## Recommended next action

Stop this no-paper run; the bounded next test is a fused int8 dot-product attention kernel that avoids materializing fp32 K/V, compared against the same fp32 baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused CPU Int8 KV Attention Without Full Dequantization
- Success threshold: At seq_len >= 2048, fused int8 KV median latency <= 1.10x fp32 while preserving at least 3.8x KV storage reduction and relative L2 attention-output error <= 0.03.
- Stop condition: Stop if fused int8 remains >1.25x slower than fp32 at seq_len >= 2048 or output relative L2 error exceeds 0.03 under the same quantization scheme.

## Evidence references

- Artifact root: `<local-path>/projects/real-cpu-llm-runtime-validation-of-int8-kv-cache-compressi-1aa129ff0c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
