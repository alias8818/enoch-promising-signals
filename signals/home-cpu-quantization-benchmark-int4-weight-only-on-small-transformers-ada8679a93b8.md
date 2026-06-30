# Home CPU Quantization Benchmark: INT4 Weight-Only on Small Transformers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-cpu-quantization-benchmark-int4-weight-only-on-small-transformers-ada8679a93b8`
Run ID: `home-cpu-quantization-benchmark-int4-weight-only-on-small-transformers-ada8679a93b8-20260605T112411125941+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0bd4b15288b5

## What looked useful

INT4 weight-only storage gave 7.11x compression and roughly 0.107 output relative RMSE, but corrected 1-thread and 4-thread packed INT4 fallback runs were slower than FP32 for every tested toy256 and GPT-2-small-class projection at M=1, M=16, and M=128.

## Boundaries and scale limits

Synthetic projection-layer benchmark only; no downloaded end-to-end transformer, no perplexity/accuracy task, no fused INT4 CPU kernel, and one unstable 8-thread toy-shape OpenBLAS anomaly excluded from the primary latency claim.

## Claim scope

On this CPU-only worker with NumPy/OpenBLAS, transformer-shaped packed INT4 weight-only projection layers with per-group FP32 scales reduce weight storage but do not improve latency when weights are unpacked/dequantized each call before FP32 matmul.

## Why it stopped

Early direct kernel evidence falsifies the simple packed-INT4 dequantize-then-BLAS latency path; this is not a full validation of all fused INT4 CPU implementations.

## Recommended next action

Stop this run as a no-paper useful signal; next, benchmark a fused INT4 weight-only runtime such as llama.cpp/GGML on the same CPU with a real small transformer and compare token latency plus perplexity against FP32 or FP16 baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Fused INT4 CPU Runtime Benchmark for Small Transformers
- Success threshold: Fused INT4 is at least 1.2x faster than the strongest FP32/FP16 CPU baseline for M=1 decode and short-prompt inference while preserving acceptable perplexity or task quality.
- Stop condition: Stop if fused INT4 is slower than baseline on decode and short-prompt cases or if quality degradation is unacceptable.

## Evidence references

- Artifact root: `<local-path>/projects/home-cpu-quantization-benchmark-int4-weight-only-on-small-transformers-ada8679a93b8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
