# Activation-Aware INT8 Quantization for CPU Inference

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `activation-aware-int8-quantization-for-cpu-inference-0bb49e5fb4aa`
Run ID: `activation-aware-int8-quantization-for-cpu-inference-0bb49e5fb4aa-20260614T102556583517+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/293290b77429

## What looked useful

Activation-aware clipping produced a median relative-MSE ratio of 0.9515 versus standard INT8, with ratios from 0.9450 to 0.9610 across four benchmark shapes. The result supports the calibration mechanism but not paper-ready CPU inference performance.

## Boundaries and scale limits

Synthetic weights and activations only; one seed; no real transformer/MLP model; no end-task accuracy; no production AVX512/VNNI INT8 kernel; NumPy INT8 matmul was slower than FP32 BLAS and cannot support a serving-speedup claim.

## Claim scope

In a deterministic synthetic NumPy CPU linear-layer probe, activation-second-moment-weighted INT8 weight clipping reduced held-out W8A8 output relative MSE versus standard max-range per-output-channel INT8 on all four tested benchmark shapes.

## Why it stopped

No-paper useful signal only: this run directly tested a synthetic quantization mechanism, while real-model accuracy and production CPU inference speed remain unvalidated.

## Recommended next action

Run a bounded real-model follow-up on transformer MLP/linear layers using real activation traces and an optimized x86 INT8 kernel; stop if activation-aware clipping fails to improve task accuracy or layer MSE at equal or lower latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model activation-aware INT8 CPU linear-layer validation
- Success threshold: At least 10% lower median layer relative MSE or a smaller end-task accuracy/perplexity degradation than standard INT8, with median optimized INT8 latency no worse than 5% above standard INT8.
- Stop condition: Stop as negative if real-model activation-aware quantization does not beat standard INT8 on layer MSE or end-task quality, or if optimized latency exceeds standard INT8 by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-int8-quantization-for-cpu-inference-0bb49e5fb4aa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
