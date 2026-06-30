# Larger real-dataset async 1% top-k EF validation with communication accounting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `larger-real-dataset-async-1--top-k-ef-validation-with-comm-8e99182e12`
Run ID: `larger-real-dataset-async-1--top-k-ef-validation-with-comm-8e99182e12-20260608T212845569608+0000`

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

- Parent run decision: Real multiprocessing validation of async 1% top-k error-feedback training on CPU: enoch://control-plane/projects/real-multiprocessing-validation-of-async-1--top-k-error-fe-306118c87d/runs/real-multiprocessing-validation-of-async-1--top-k-error-fe-306118c87d-20260608T162214091598+0000
- Parent run decision: Real-dataset nonlinear validation of async 1% top-k error-feedback multiprocessing training: enoch://control-plane/projects/real-dataset-nonlinear-validation-of-async-1--top-k-error-f600a978d3/runs/real-dataset-nonlinear-validation-of-async-1--top-k-error-f600a978d3-20260608T182500771250+0000

## What looked useful

Error feedback is useful at identical 1% top-k byte cost, improving 20-epoch validation accuracy from 0.7979 to 0.8098 and loss from 0.3670 to 0.3532 versus no-EF, but dense reached 0.9113 accuracy and 0.3276 loss. The 1% async EF setting fails the within-1-percentage-point dense-accuracy threshold.

## Boundaries and scale limits

Single-process CPU simulation, one real sparse binary classification dataset, no real network or multi-node parameter server, 20 epochs maximum, fixed hyperparameters except the 5-to-20 epoch convergence extension.

## Claim scope

On LIBSVM real-sim sparse logistic regression with 8 simulated asynchronous workers, 1% top-k error feedback reduced communicated gradient bytes to 2.004% of dense and consistently beat a no-error-feedback top-k ablation, but did not preserve dense validation accuracy.

## Why it stopped

Bounded real-dataset validation with fixed seeds and a real dense baseline falsified the 1% async top-k EF accuracy-preservation threshold, despite confirming communication reduction and EF-over-noEF benefit.

## Recommended next action

Stop this claim as no-paper evidence; if continuing at depth 3, run a bounded Pareto sweep over top-k fraction, staleness, and learning rate to find the minimum byte ratio that stays within 1 percentage point of dense accuracy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-sim async EF Pareto sweep for minimum accurate top-k budget
- Success threshold: Find a compressed async EF configuration with mean validation accuracy within 1 percentage point of dense and communication ratio below 10% of dense, while outperforming no-EF at identical top-k/staleness.
- Stop condition: Stop if no tested configuration below 10% dense communication reaches within 1 percentage point of dense accuracy, or if the best configuration only matches dense after losing the intended communication advantage.

## Evidence references

- Artifact root: `<local-path>/projects/larger-real-dataset-async-1--top-k-ef-validation-with-comm-8e99182e12`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
