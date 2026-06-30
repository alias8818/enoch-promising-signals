# Real-dataset nonlinear validation of async 1% top-k error-feedback multiprocessing training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-dataset-nonlinear-validation-of-async-1--top-k-error-f600a978d3`
Run ID: `real-dataset-nonlinear-validation-of-async-1--top-k-error-f600a978d3-20260608T182500771250+0000`

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

- Parent run decision: Real multiprocessing validation of async 1% top-k error-feedback training on CPU: enoch://control-plane/projects/real-multiprocessing-validation-of-async-1--top-k-error-fe-306118c87d/runs/real-multiprocessing-validation-of-async-1--top-k-error-fe-306118c87d-20260608T162214091598+0000
- Parent run decision: Async gradient compression for home CPU training: enoch://control-plane/projects/async-gradient-compression-for-home-cpu-training-c15204d24630/runs/async-gradient-compression-for-home-cpu-training-c15204d24630-20260608T092742122267+0000

## What looked useful

Error feedback was the decisive control: async 1% top-k EF matched dense_sync mean test accuracy at 0.9741, while async 1% top-k without EF fell to 0.9630 mean accuracy and increased mean test loss by about 0.0504 versus dense_sync under the same sparsity and staleness.

## Boundaries and scale limits

Small real dataset, small MLP, CPU-local multiprocessing, bounded mean staleness about 3 updates, no networked parameter server, no large language model, no multi-node communication, and only 3 seeds.

## Claim scope

On sklearn digits with a 64-128-10 ReLU MLP trained for 2000 minibatch updates over 3 fixed seeds, local 4-worker asynchronous multiprocessing 1% top-k gradient compression with per-worker error feedback matched dense synchronous test accuracy while transmitting 97 of 9610 gradient coordinates per update.

## Why it stopped

Medium local validation supports the mechanism but is not publication-grade broad validation because it lacks larger real workloads and distributed communication effects.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded deepening step is a larger real dataset/model with throughput and communication-byte accounting, not another tiny proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Larger real-dataset async 1% top-k EF validation with communication accounting
- Success threshold: Async 1% top-k EF is within 1 percentage point of the dense baseline mean test accuracy and has no worse than 0.02 absolute loss degradation, while async top-k without EF is worse by at least 0.5 percentage points or materially worse in loss.
- Stop condition: Stop if async 1% top-k EF trails dense by more than 2 percentage points in mean accuracy or diverges/plateaus below the no-error-feedback ablation under matched learning-rate tuning.

## Evidence references

- Artifact root: `<local-path>/projects/real-dataset-nonlinear-validation-of-async-1--top-k-error-f600a978d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
