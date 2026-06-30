# Volunteer Distributed Training with Bounded Local Backprop

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `volunteer-distributed-training-with-bounded-local-backprop-a9ff9066e0fd`
Run ID: `volunteer-distributed-training-with-bounded-local-backprop-a9ff9066e0fd-20260605T211228723884+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/1fd369b1bf6e

## What looked useful

Bounded local block updates can preserve useful learning signal in a small GPU-resident proxy, and skipped local updates may act as regularization rather than immediately breaking training.

## Boundaries and scale limits

Synthetic task only; no real volunteer networking, heterogeneous clients, stale activations, non-IID worker-owned data, privacy constraints, language modeling, or multi-node training was tested.

## Claim scope

On a deterministic synthetic nonlinear classification task with three MLP blocks, auxiliary-head bounded local backpropagation matched or exceeded a full-backprop baseline across three seeds, and simulated skipped block updates up to 80% did not collapse validation accuracy.

## Why it stopped

No-paper closure: the result is useful synthetic mechanism evidence, not direct validation of volunteer distributed training.

## Recommended next action

Run a bounded real-data volunteer simulation with non-IID shards, client churn, stale activations, and tuned full-backprop/local-backprop baselines before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-data churn and staleness test for bounded local backprop
- Success threshold: Local bounded backprop reaches at least 95% of tuned full-backprop test accuracy while reducing global backprop dependency and without collapse under 20% churn or one-step staleness.
- Stop condition: Stop as negative if local bounded backprop is more than 10 percentage points below the tuned full-backprop baseline on two of three seeds or collapses under mild churn/staleness.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-distributed-training-with-bounded-local-backprop-a9ff9066e0fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
