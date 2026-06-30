# SIMD and runtime validation for page-wise int4 CPU KV cache

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `simd-and-runtime-validation-for-page-wise-int4-cpu-kv-cach-2bdc1f7332`
Run ID: `simd-and-runtime-validation-for-page-wise-int4-cpu-kv-cach-2bdc1f7332-20260524T082502858596+0000`

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

- Parent run decision: Page-wise 4-bit KV cache on CPU: enoch://control-plane/projects/page-wise-4-bit-kv-cache-on-cpu-7aee0bc70464/runs/page-wise-4-bit-kv-cache-on-cpu-7aee0bc70464-20260524T080842923440+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e35c100a1357

## What looked useful

SIMD and metadata validation are functionally viable, but this straightforward AVX2 implementation did not meet the performance threshold: median speedup was 1.09x-1.25x versus scalar and validation overhead exceeded 10% for 512 and 1024 dimensions.

## Boundaries and scale limits

Not end-to-end LLM serving; no real model KV traces, multi-thread serving, allocator effects, token latency, quality checks, or AVX512-specific kernel were tested.

## Claim scope

Single-core AVX2 direct microbenchmark of signed page-wise int4 KV-cache decode/dot with page metadata validation on deterministic synthetic pages.

## Why it stopped

Controlled small direct test passed correctness and invalid-metadata validation but failed the stated performance threshold, so mechanism support is insufficient for publication readiness.

## Recommended next action

Stop this run as a no-paper useful signal; only revisit with a bounded AVX512/layout-specific kernel that can directly target the failed 1.5x speedup and <=10% validation-overhead thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: AVX512/layout-specific int4 KV page kernel against the same scalar baseline
- Success threshold: Median SIMD speedup >=1.5x versus scalar on at least two tested dimensions and median validated SIMD overhead <=10% on all tested dimensions.
- Stop condition: Stop if the optimized kernel remains below 1.5x speedup on all dimensions or validation overhead remains above 10% on two or more dimensions.

## Evidence references

- Artifact root: `<local-path>/projects/simd-and-runtime-validation-for-page-wise-int4-cpu-kv-cach-2bdc1f7332`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
