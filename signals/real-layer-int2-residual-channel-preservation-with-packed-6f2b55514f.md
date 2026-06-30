# Real-layer INT2 residual-channel preservation with packed CPU kernels

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-layer-int2-residual-channel-preservation-with-packed-6f2b55514f`
Run ID: `real-layer-int2-residual-channel-preservation-with-packed-6f2b55514f-20260613T224650364901+0000`

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

- Parent run decision: Extreme INT2 Quantization with Principled Residual Channel Preservation on CPU: enoch://control-plane/projects/extreme-int2-quantization-with-principled-residual-channel-preservation-on-cpu-0cc00731f115/runs/extreme-int2-quantization-with-principled-residual-channel-preservation-on-cpu-0cc00731f115-20260613T223039853441+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/74ea33d242ca

## What looked useful

Residual-channel preservation recovered 7.6% MSE at 6.25% preserved channels and 15.3% MSE at 12.5% preserved channels on Pythia-70M, while residual total runtime was 1.17x to 1.19x slower than plain packed INT2 and no faster than FP32.

## Boundaries and scale limits

Tested only first-layer MLP weights from Pythia-14M and Pythia-70M; inputs were synthetic controlled activations, not real corpus traces; kernels were scalar reference implementations without SIMD or full-model integration.

## Claim scope

On two real pretrained Pythia MLP up-projection layers with controlled LayerNorm-like inputs, preserving high-norm input channels in an exact FP32 side path monotonically reduced packed INT2 output error, but the scalar packed CPU kernels did not improve latency over a naive FP32 loop.

## Why it stopped

Tier 1 direct test produced useful mechanism support but also showed the current packed CPU implementation is not practically faster, so this is no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded SIMD-kernel follow-up using real activation traces; stop if an optimized fused residual path cannot beat FP32 by at least 1.2x while preserving at least 15% MSE recovery at 12.5% or fewer residual channels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SIMD fused residual side path for real-layer packed INT2 CPU inference
- Success threshold: At 12.5% or fewer preserved channels, fused residual packed INT2 achieves at least 15% MSE reduction versus plain INT2 and at least 1.2x speedup versus FP32 on a real layer trace.
- Stop condition: Stop if the optimized packed core remains slower than FP32 or if the fused residual side path erases the speedup at residual fractions needed for at least 15% MSE recovery.

## Evidence references

- Artifact root: `<local-path>/projects/real-layer-int2-residual-channel-preservation-with-packed-6f2b55514f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
