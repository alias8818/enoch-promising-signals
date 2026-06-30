# Real multiprocessing validation of async 1% top-k error-feedback training on CPU

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-multiprocessing-validation-of-async-1--top-k-error-fe-306118c87d`
Run ID: `real-multiprocessing-validation-of-async-1--top-k-error-fe-306118c87d-20260608T162214091598+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Async gradient compression for home CPU training: enoch://control-plane/projects/async-gradient-compression-for-home-cpu-training-c15204d24630/runs/async-gradient-compression-for-home-cpu-training-c15204d24630-20260608T092742122267+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/1b9c9a573847

## What looked useful

A direct CPU multiprocessing parameter-server test supports error feedback as the mechanism that lets 1% top-k asynchronous updates preserve dense-like accuracy in this bounded setting; no-EF top-k lost about 7.9 accuracy points while EF stayed within the dense tolerance.

## Boundaries and scale limits

Single host, 4 worker processes, synthetic binary classification, 2048-dimensional linear model, 3 seeds, 2000 updates per mode/seed; no real dataset, nonlinear model, transformer-scale training, networked distributed transport, or long-run convergence validation.

## Claim scope

In a small synthetic logistic-regression task on one CPU worker, real multiprocessing asynchronous 1% top-k SGD with worker-local error feedback matched dense async accuracy within 2 percentage points over 3 seeds while reducing estimated update bytes by about 51x and outperforming 1% top-k without error feedback.

## Why it stopped

Tier 1 direct validation completed and produced a useful mechanism signal, but evidence remains too small and synthetic for publication readiness.

## Recommended next action

Run a bounded deepen follow-up on a real dataset and a small nonlinear model with the same multiprocessing async parameter-server harness, comparing dense, 1% top-k no-EF, and 1% top-k EF over at least 5 seeds and 2 compression fractions.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset nonlinear validation of async 1% top-k error-feedback multiprocessing training
- Success threshold: EF top-k mean accuracy within 2 percentage points of dense async, at least 4 points above no-EF top-k, no worker failures, and at least 40x estimated update-byte reduction at 1% top-k.
- Stop condition: Stop as negative if EF top-k is more than 2 accuracy points below dense or fails to beat no-EF by at least 4 points on the real-dataset nonlinear benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/real-multiprocessing-validation-of-async-1--top-k-error-fe-306118c87d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
