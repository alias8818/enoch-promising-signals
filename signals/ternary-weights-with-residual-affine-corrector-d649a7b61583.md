# Ternary Weights with Residual Affine Corrector

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-weights-with-residual-affine-corrector-d649a7b61583`
Run ID: `ternary-weights-with-residual-affine-corrector-d649a7b61583-20260531T221015542280+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/ca8057bf4126

## What looked useful

Cheap diagonal affine correction preserved compression but did not improve random-layer NMSE and only moved synthetic teacher accuracy from 0.5558 to 0.5718. Low-rank residual affine correction improved accuracy to 0.6014 and linear NMSE from 0.1903 to 0.1806, but raised storage to 0.1293x dense on average for linear layers and 0.3140x dense in the teacher MLP. Full affine correction worked best but cost dense-scale or larger storage in many tested shapes.

## Boundaries and scale limits

No transformer, real dataset, end-to-end training, packed ternary kernel, latency, or GPT-2-small-class validation was run. Evidence is bounded to random/proxy activations and analytic storage-bit estimates.

## Claim scope

PyTorch-only proxy tests of post-hoc affine correction for ternary linear layers on random Gaussian linear maps and a synthetic two-layer dense-teacher classification task.

## Why it stopped

Proxy/mechanism evidence is mixed and not paper-ready: the cheap corrector is mostly ineffective, while stronger affine correction improves quality only by spending substantial dense corrector storage.

## Recommended next action

Run one bounded direct small-model rank sweep on a real dataset or tiny transformer, then stop if low-rank residual correctors do not beat ternary-only by at least 20% relative error reduction at no more than 0.25x dense storage.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rank-swept residual affine correctors on a tiny real model
- Success threshold: Low-rank residual correction reduces ternary-only validation loss/accuracy gap to dense by at least 20% relative at <=0.25x dense FP32 parameter storage, consistently across at least three seeds.
- Stop condition: Stop if diagonal and low-rank correctors fail to beat ternary-only beyond run-to-run variance, or if the rank needed for improvement exceeds 0.25x dense FP32 storage.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-weights-with-residual-affine-corrector-d649a7b61583`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
