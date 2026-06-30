# INT3-FP16 Residual Channel Quantization for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int3-fp16-residual-channel-quantization-for-cpu-inference-3d28d256febd`
Run ID: `int3-fp16-residual-channel-quantization-for-cpu-inference-3d28d256febd-20260613T070652389344+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e939cac20e2f

## What looked useful

Error-ranked FP16 residual columns consistently improve INT3 over INT3-only and random residual selection. At a 4-bit nominal budget, residual INT3 loses to INT4 in the default outlier proxy but beats INT4 accuracy under a stronger concentrated outlier regime, while remaining slower in the CPU proxy.

## Boundaries and scale limits

Not a packed INT3 CPU kernel, not real transformer weights or activations, no perplexity/task benchmark, no tokens/sec serving measurement, and residual latency is represented as an added NumPy GEMM.

## Claim scope

Synthetic 1024x1024 dense linear CPU proxy with per-row INT3/INT4 quantization and FP16/FP32 residual input-column correction, batch 64, three seeds, single-thread NumPy BLAS.

## Why it stopped

Current evidence is a bounded synthetic mechanism test with mixed results and no packed-kernel or real-model validation, so it is useful but not paper-ready.

## Recommended next action

Run a bounded deepen test on real transformer MLP layers with captured activations and packed or faithful INT3/INT4 CPU kernels before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-layer packed CPU test for INT3 plus FP16 residual columns
- Success threshold: At 4.0 effective bits/weight, residual INT3 improves model-level accuracy or perplexity versus INT4 while matching or exceeding INT4 CPU tokens/sec within measurement noise.
- Stop condition: Stop if residual INT3 fails to beat INT4 on real-layer output error or is more than 10% slower than INT4 in a packed/fair CPU implementation.

## Evidence references

- Artifact root: `<local-path>/projects/int3-fp16-residual-channel-quantization-for-cpu-inference-3d28d256febd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
