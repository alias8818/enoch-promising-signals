# Packed q4 activation trace overhead in a fused or bit-packed path

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `packed-q4-activation-trace-overhead-in-a-fused-or-bit-pack-172246c718`
Run ID: `packed-q4-activation-trace-overhead-in-a-fused-or-bit-pack-172246c718-20260529T181113381320+0000`

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

- Parent run decision: Transformer-trace residual overhead test for q4 activations: enoch://control-plane/projects/transformer-trace-residual-overhead-test-for-q4-activation-32476fe9ea/runs/transformer-trace-residual-overhead-test-for-q4-activation-32476fe9ea-20260528T145015534305+0000
- Parent run decision: Principled Residuals for 4-Bit Activations: enoch://control-plane/projects/principled-residuals-for-4-bit-activations-6f6c21c2d840/runs/principled-residuals-for-4-bit-activations-6f6c21c2d840-20260528T011103144472+0000

## What looked useful

Packed q4 tracing appears cheap when the q4 activation stream is already packed inside a compute-heavy path: medium shape packed dump overhead averaged -0.73% and packed histogram overhead averaged 0.92%; activation-heavy shape averaged -2.76% and -1.00%. The broad claim is bounded by a trace-dominated edge case where packed dump overhead was 9.43% and naive histogram tracing was 111.40%.

## Boundaries and scale limits

Evidence is limited to local CPU scalar microbenchmarks with synthetic activations and weights. No actual fused GPU kernel, tensor-core path, transformer layer, serving stack, or real activation distribution was tested.

## Claim scope

On a deterministic CPU q4 matrix-vector benchmark with fixed seeds, packed q4 activation dump tracing and compact histogram tracing stayed within a 5% overhead target for compute-heavy fused-style paths, but not for a trace-dominated rows=1 edge case.

## Why it stopped

Tier-2 CPU evidence supports a bounded mechanism signal but also falsifies the broad version in a trace-dominated control; this is not direct publication-grade evidence for real fused model kernels.

## Recommended next action

Stop short of paper claims; run one bounded deepen follow-up on an actual fused GPU or vectorized kernel path and require packed dump tracing to remain under 5% overhead against the no-trace kernel while the trace-dominated control is reported separately.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Packed q4 activation trace overhead in a real fused GPU kernel
- Success threshold: For all transformer-layer-like compute-heavy shapes, packed byte trace overhead is <=5% mean wall-time overhead over no-trace with no per-seed result above 8%; trace-dominated control may exceed the threshold but must be reported as a scope limit.
- Stop condition: Stop if any compute-heavy fused GPU shape exceeds 8% packed dump overhead on two fixed seeds, or if no correct no-trace fused kernel baseline can be produced.

## Evidence references

- Artifact root: `<local-path>/projects/packed-q4-activation-trace-overhead-in-a-fused-or-bit-pack-172246c718`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
