# Residual nonlinear activation verifier with actual verifier-model correction

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `residual-nonlinear-activation-verifier-with-actual-verifie-458ccb1b76`
Run ID: `residual-nonlinear-activation-verifier-with-actual-verifie-458ccb1b76-20260517T184003384238+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Residual nonlinear activation verifier with actual verifier-model correction: internal_generated:residual-nonlinear-activation-verifier-with-actual-verifie-458ccb1b76

## What looked useful

The mechanism is real but conditional: coarse 5-knot surrogates plus 131072 verifier samples achieved 0.951 in-distribution MSE reduction and verifier/ridge MSE ratio 0.201, but nominal 0.90 OOD residual coverage fell to 0.660. Fine 11-knot surrogates recovered OOD coverage near 0.906 only when verifier MSE was essentially at ridge parity.

## Boundaries and scale limits

Validated on random MLP teachers with input_dim=32, hidden_dim=256, output_dim=10, 3 to 5 fixed seeds, train_n up to 131072, and simple scale/shift OOD splits on one GB10 machine. Not validated on trained language models, deeper networks, real verification workloads, or broad distribution shifts.

## Claim scope

In a synthetic one-hidden-layer SiLU MLP verifier benchmark, learned residual correction can substantially reduce in-distribution piecewise-linear activation approximation error for coarse surrogates with enough verifier data, but robustness and calibrated OOD coverage are not reliable.

## Why it stopped

Bounded validation found useful mechanism support but not a robust paper-positive result: high in-distribution gains fail OOD coverage, while OOD-safe settings are near ridge parity.

## Recommended next action

Stop the current paper path; if continuing within the controller lineage, run one bounded deepen test of distribution-aware residual calibration for the same verifier correction benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distribution-aware calibration for residual activation verifier correction
- Success threshold: For knots=5/train_n=131072, maintain OOD verifier/ridge MSE ratio <= 0.70 and achieve OOD 90% interval coverage >= 0.88 with mean interval width <= 1.5x the current verifier width.
- Stop condition: Stop if OOD coverage remains below 0.88 at <=1.5x interval width or if restoring coverage removes the verifier's MSE advantage over ridge.

## Evidence references

- Artifact root: `<local-path>/projects/residual-nonlinear-activation-verifier-with-actual-verifie-458ccb1b76`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
