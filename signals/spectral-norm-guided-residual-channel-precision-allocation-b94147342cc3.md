# Spectral-Norm Guided Residual Channel Precision Allocation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `spectral-norm-guided-residual-channel-precision-allocation-b94147342cc3`
Run ID: `spectral-norm-guided-residual-channel-precision-allocation-b94147342cc3-20260602T145055410993+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b3657682c7fa

## What looked useful

Pure spectral ranking beat random, local-weight, and all-low baselines but underperformed activation spread at the default 25% budget. The corrected spectral_range score reduced held-out logit MSE by about 14.4% versus activation-only, 17.9% versus pure spectral, 31.8% versus random, and 48.9% versus all-low at the same 25% high-precision channel budget.

## Boundaries and scale limits

Proxy-only NumPy experiment: no trained real model, no transformer or ResNet task accuracy, no hardware mixed-precision kernel measurement, no comparison to full Hessian/gradient-aware quantization methods, and no large-scale calibration-overhead analysis.

## Claim scope

In synthetic untrained residual MLPs with post-training residual-branch activation quantization, pure downstream spectral/operator-norm channel ranking is useful but incomplete; multiplying downstream spectral sensitivity by activation spread produced the best mixed-precision allocator among tested synthetic heuristics at 12.5%, 25%, and 50% high-precision channel budgets.

## Why it stopped

Closed as no-paper useful synthetic signal: pure spectral norm alone was not supported, while the spectral-plus-range variant needs direct trained-model evidence before any paper claim.

## Recommended next action

Run a bounded trained-model follow-up on a small residual classifier or transformer block to test spectral_range allocation against activation-aware and gradient-aware quantization baselines using real validation accuracy or perplexity.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trained-model validation of spectral-range residual channel precision allocation
- Success threshold: At 2-3 average activation bits, spectral_range should reduce task-metric degradation or logit/perplexity error by at least 10% relative to the best non-spectral heuristic on two seeds or two architectures without materially higher calibration cost.
- Stop condition: Stop if spectral_range fails to beat activation-only on the trained validation metric at matched bit budget, or if computing downstream sensitivity costs more than the quantization benefit justifies for the small model.

## Evidence references

- Artifact root: `<local-path>/projects/spectral-norm-guided-residual-channel-precision-allocation-b94147342cc3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
