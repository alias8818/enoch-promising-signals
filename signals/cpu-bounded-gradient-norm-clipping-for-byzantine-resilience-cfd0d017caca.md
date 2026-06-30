# CPU-Bounded Gradient Norm Clipping for Byzantine Resilience

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cpu-bounded-gradient-norm-clipping-for-byzantine-resilience-cfd0d017caca`
Run ID: `cpu-bounded-gradient-norm-clipping-for-byzantine-resilience-cfd0d017caca-20260530T013743245339+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/af9cadb02690

## What looked useful

Clipping kept 40% random-large Byzantine runs near clean accuracy (0.9119 vs 0.9167 baseline) and rescued 20% large sign-flip runs (0.9095 vs 0.1365 plain mean), with about 1.2-1.8 ms/round CPU cost. It failed at 40% sign-flip and was brittle to bounded opposite-direction updates, where clip_mean at 40% Byzantine fell to 0.5410 accuracy while plain mean remained 0.8953.

## Boundaries and scale limits

Evidence is limited to NumPy CPU simulations with 40 clients, 50-dimensional logistic regression, synthetic client shifts, 8 seeds, fixed-round full participation, and a small attack suite. No real FL dataset, deep model, secure aggregation, partial participation, or datacenter-scale training was tested.

## Claim scope

In a small synthetic federated logistic-regression simulation, CPU-side per-client L2 gradient norm clipping cheaply limits large-magnitude Byzantine updates and preserves accuracy for random large-norm attacks, but it is not sufficient as a standalone Byzantine-resilience method.

## Why it stopped

Bounded local evidence is mixed: clipping is useful against large-norm attacks but fails as a standalone Byzantine-resilience claim under high Byzantine fractions and bounded adversarial gradients.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should test adaptive robust-center clipping on a real small FL benchmark with the bounded_opposite attack included.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive robust-center norm clipping on small real federated benchmarks
- Success threshold: A robust-center clipping variant keeps clean-accuracy gap below 3 percentage points at 30% Byzantine clients for all three attacks and adds less than 2x CPU aggregation overhead versus clip_mean.
- Stop condition: Stop if bounded_opposite still causes more than a 10 percentage point clean-accuracy gap at 20%-30% Byzantine clients or if overhead exceeds 2x without a robustness gain.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bounded-gradient-norm-clipping-for-byzantine-resilience-cfd0d017caca`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
