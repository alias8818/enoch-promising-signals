# Blockwise Int8 Weight Quantization for CPU Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `blockwise-int8-weight-quantization-for-cpu-inference-43a9e14255e0`
Run ID: `blockwise-int8-weight-quantization-for-cpu-inference-43a9e14255e0-20260604T040904314754+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/d1eff6718125

## What looked useful

Blockwise int8 weight-only GEMV is a plausible CPU inference optimization for bandwidth-favorable batch-1 linear layers, but the evidence only supports a local mechanism and not a paper-ready broad inference claim.

## Boundaries and scale limits

Synthetic single-layer GEMV only; no real model weights, no end-to-end transformer accuracy/perplexity, no vendor-optimized oneDNN/FBGEMM/llama.cpp baselines, and visible scheduling variability in some threaded cases.

## Claim scope

On this 8-thread-visible Intel Xeon Silver 4114 CPU, a self-contained GEMV microbenchmark with random weights/activations showed that per-row blockwise int8 weight-only quantization reduced weight storage to 25.4-28.1% of fp32 and improved mean latency in 23 of 24 shape/group/thread cases, with 0.00526-0.00694 relative RMSE versus fp32 outputs.

## Why it stopped

No-paper closure: the current result is synthetic kernel-local evidence, useful for prioritizing the next test but insufficient for publication-grade validation.

## Recommended next action

Run a bounded deepen test against optimized CPU kernels on a small real transformer/LLM block and require both latency improvement and quality preservation before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Optimized CPU kernel and small-model validation for blockwise int8 weight-only inference
- Success threshold: At least 1.25x median latency improvement over the optimized fp32 baseline for target linear layers or end-to-end decode, weight storage at or below 30% of fp32, and quality degradation below 1% relative or below a predeclared perplexity delta.
- Stop condition: Stop if optimized baselines eliminate the speedup below 1.10x, if quality degradation exceeds the tolerance for all tested group sizes, or if timing remains too noisy to distinguish a 1.25x effect after affinity-controlled repeats.

## Evidence references

- Artifact root: `<local-path>/projects/blockwise-int8-weight-quantization-for-cpu-inference-43a9e14255e0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
