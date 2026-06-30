# Block-wise stochastic optimizer state quantization with per-block scale tracking

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `block-wise-stochastic-optimizer-state-quantization-with-per-block-scale-tracking-c5f19b1cfb8c`
Run ID: `block-wise-stochastic-optimizer-state-quantization-with-per-block-scale-tracking-c5f19b1cfb8c-20260629T174829680548+0000`

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

- Provider-backed Research Facility batch: z-ai/glm-5.2: enoch://research-facility/provider/z-ai/glm-5.2/9e7c6374ebc0

## What looked useful

Int8 per-block Adam state quantization appears viable as a convergence-preserving compression mechanism in small local probes, but stochastic rounding plus scale tracking was not clearly superior to deterministic int8 or no-tracking int8; int4 failed strongly.

## Boundaries and scale limits

Synthetic linear regression and teacher-generated MLP classification only, 3 seeds, short runs, no real packed-state allocator, no checkpoint/restart test, no fused kernels, and no real transformer or large-model training.

## Claim scope

On two small synthetic GB10 PyTorch probes, int8 block-wise quantize/dequantize dynamics for Adam moment states preserved convergence within about 1% final loss and near-zero MLP accuracy delta while reducing analytical packed optimizer-state bytes to about 25.4% of FP32 Adam state; int4 was unstable.

## Why it stopped

Evidence is local and partly proxy-based because optimizer-state storage was analytically estimated rather than actually packed; sufficient for a useful signal, not for publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next implement a truly packed int8 Adam state optimizer and validate checkpoint/load plus a small real-model workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed int8 block-wise Adam state with checkpoint fidelity on a small real model
- Success threshold: Actual optimizer-state memory at or below 30% of FP32 Adam state with final validation metric within 1% relative loss or 0.5 percentage points accuracy/perplexity-equivalent of FP32 Adam, no checkpoint fidelity failures, and no systematic divergence across 3 seeds.
- Stop condition: Stop if packed int8 state cannot reduce measured optimizer memory below 40% after scale overhead, if checkpoint reload changes validation loss beyond 0.5%, or if final real-workload quality is worse than FP32 by more than 2% relative loss or 1 percentage point accuracy/perplexity-equivalent across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/block-wise-stochastic-optimizer-state-quantization-with-per-block-scale-tracking-c5f19b1cfb8c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
