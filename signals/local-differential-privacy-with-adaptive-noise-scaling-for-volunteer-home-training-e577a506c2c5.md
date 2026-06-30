# Local Differential Privacy with Adaptive Noise Scaling for Volunteer Home Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-differential-privacy-with-adaptive-noise-scaling-for-volunteer-home-training-e577a506c2c5`
Run ID: `local-differential-privacy-with-adaptive-noise-scaling-for-volunteer-home-training-e577a506c2c5-20260620T105443160908+0000`

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

- Provider-backed Research Facility batch: qwen/qwen3.7-max: enoch://research-facility/provider/qwen/qwen3.7-max/35b446046754

## What looked useful

Sample-count-aware local-DP noise scaling recovered large utility losses from fixed worst-case noise when client dataset sizes varied, with paired gains of +0.125 accuracy at epsilon 0.5, +0.0566 at epsilon 1.0, and +0.0091 at epsilon 2.0. The advantage disappeared at epsilon 4.0, and inverse-variance aggregation was harmful under non-IID clients.

## Boundaries and scale limits

Synthetic data only; no real volunteer devices, no deep model, no secure aggregation, no membership-inference or gradient-inversion attack evaluation, and no formal multi-round privacy accountant beyond per-round Gaussian local-noise calibration.

## Claim scope

In a synthetic heterogeneous federated logistic-regression simulation with clipped per-example gradients and client-side Gaussian local-DP noise, scaling local noise by each volunteer client's sample count improves accuracy over fixed worst-case local noise at strict privacy budgets (epsilon 0.5 to 2.0), but not at epsilon 4.0.

## Why it stopped

No-paper useful signal: this bounded synthetic/proxy run supports the mechanism under strict local-DP noise but is not a full validation of volunteer home training and is mixed across privacy budgets.

## Recommended next action

Run a bounded real FL benchmark with formal privacy accounting, matched epsilon/delta budgets, and client-size heterogeneity before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real FL benchmark for sample-count-aware local-DP noise scaling
- Success threshold: Adaptive sample-count local-DP noise beats fixed worst-case local-DP noise by >= 3 absolute test-accuracy points at epsilon <= 1.0 without materially increasing attack success or violating the stated privacy accounting.
- Stop condition: Stop if the adaptive method fails to beat fixed worst-case local-DP by 1 absolute accuracy point across 5 seeds, if formal accounting cannot justify the adaptive signal, or if benefits only appear under synthetic-only client distributions.

## Evidence references

- Artifact root: `<local-path>/projects/local-differential-privacy-with-adaptive-noise-scaling-for-volunteer-home-training-e577a506c2c5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
