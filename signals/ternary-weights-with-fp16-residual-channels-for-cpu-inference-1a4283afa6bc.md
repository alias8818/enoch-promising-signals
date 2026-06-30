# Ternary Weights with FP16 Residual Channels for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weights-with-fp16-residual-channels-for-cpu-inference-1a4283afa6bc`
Run ID: `ternary-weights-with-fp16-residual-channels-for-cpu-inference-1a4283afa6bc-20260525T111521061274+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a884e882bba0

## What looked useful

Small FP16 residual-channel fractions barely reduced error: relative L2 stayed about 0.41-0.44 for 0-12.5% residual channels on 4096x4096 synthetic weights. Even 50% residual channels left relative L2 0.31 while using more estimated weight bytes than dense FP16. The approach has a narrow speed signal against naive dense FP32, but not an accuracy-preserving compression signal.

## Boundaries and scale limits

Synthetic single-layer matvec only; no real transformer weights, no perplexity, no end-to-end decoder latency, no production BLAS/oneDNN baseline, and no bitpacked SIMD ternary kernel.

## Claim scope

On synthetic 4096x4096 CPU matvec with Gaussian weights, scaled ternary weights plus FP16 residual input channels can beat a naive dense FP32 loop, but the residual-channel correction does not recover accuracy efficiently and is not competitive with dense FP16-storage accuracy.

## Why it stopped

Bounded synthetic CPU evidence is insufficient for a paper and partially falsifies the accuracy-recovery premise; this is an early proxy result, not a full validation.

## Recommended next action

Run a bounded deepen test on real GPT-2-small linear layer weights with the same quantizer, measuring per-layer output error and small validation perplexity before attempting optimized kernels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-weight residual-channel ternary probe on GPT-2-small layers
- Success threshold: At 6.25-12.5% residual channels, median per-layer output relative L2 below 0.10 and validation loss degradation small enough to justify kernel optimization, while retaining lower memory than dense FP16 or a clear latency win.
- Stop condition: Stop if real-layer relative L2 remains above 0.20 at 12.5% residual channels or validation loss degrades sharply versus dense FP16.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weights-with-fp16-residual-channels-for-cpu-inference-1a4283afa6bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
