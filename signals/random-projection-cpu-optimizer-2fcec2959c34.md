# Random Projection CPU Optimizer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `random-projection-cpu-optimizer-2fcec2959c34`
Run ID: `random-projection-cpu-optimizer-2fcec2959c34-20260601T072830839078+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/a71d140b24df

## What looked useful

Fixed random projections are a CPU accelerator only under a low-dimensional-in-subspace assumption; dense high-dimensional objectives show persistent quality loss that is not eliminated cheaply by increasing k.

## Boundaries and scale limits

CPU-only NumPy benchmark; synthetic least-squares objectives only; single-threaded BLAS timing; no logistic, nonconvex, adaptive projection, real-dataset, or multi-threaded validation.

## Claim scope

For synthetic ridge-regression objectives with d=4096, fixed Gaussian random-projection gradient descent gives a clear CPU speedup when the target lies in the chosen k=256 subspace, but it loses solution quality on dense targets because the fixed subspace captures only a small fraction of target energy.

## Why it stopped

No-paper useful signal: bounded synthetic evidence supports the speed mechanism but gives a direct dense-target counterexample to the broad general-purpose fixed random-projection CPU optimizer claim.

## Recommended next action

Do not write a paper from this run; if continuing, test an adaptive or structured projection optimizer on a real dense benchmark with a success threshold of at least 2x end-to-end CPU speedup and no more than 2% test-metric degradation versus full-space GD.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Structured Projection CPU Optimizer on Dense Benchmarks
- Success threshold: At least 2x end-to-end CPU speedup versus full-space GD with no more than 2% test-metric degradation on a dense target benchmark across at least three seeds.
- Stop condition: Stop if dense-target test metric remains more than 5% worse than full-space GD at projection dimensions where end-to-end speedup is below 2x.

## Evidence references

- Artifact root: `<local-path>/projects/random-projection-cpu-optimizer-2fcec2959c34`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
