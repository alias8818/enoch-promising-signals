# INT4 Weight-Only Quantization for GPT-2-Small on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int4-weight-only-quantization-for-gpt-2-small-on-cpu-c13143537372`
Run ID: `int4-weight-only-quantization-for-gpt-2-small-on-cpu-c13143537372-20260619T074132431731+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8977943e21b7

## What looked useful

Weight-only INT4 compression is mechanically feasible on real GPT-2-small weights, but CPU speedup is unsupported without a true packed INT4 kernel; compression alone should not be treated as a latency win.

## Boundaries and scale limits

This run did not execute full GPT-2 autoregressive inference, did not measure perplexity or generation quality, and did not implement or use a packed INT4 CPU GEMM kernel.

## Claim scope

On six real GPT-2-small projection matrices, symmetric per-input-group INT4 weight-only quantization at group size 32 gives about 6.4x packed weight-plus-scale compression with about 10% mean layer-output relative RMSE on random activation probes, but NumPy CPU dequantization/grouped proxies are slower than FP32 BLAS.

## Why it stopped

Bounded proxy evidence found compression benefits but no CPU speedup in the available implementation path; full validation requires direct packed-kernel and full-model inference evidence.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should implement or plug in a packed AVX2/AVX512 INT4 GEMM path and measure full GPT-2-small decode speed plus perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed INT4 CPU Kernel for GPT-2-Small Decode
- Success threshold: At least 1.2x end-to-end decode tokens/sec over FP32 on CPU with no more than 5% relative perplexity degradation and at least 3x effective model-weight memory reduction.
- Stop condition: Stop if packed-kernel layer benchmarks fail to exceed FP32 by 1.1x on representative GPT-2 projection shapes or if perplexity degradation exceeds 10% in the first direct corpus evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/int4-weight-only-quantization-for-gpt-2-small-on-cpu-c13143537372`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
