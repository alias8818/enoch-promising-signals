# Bounded Work Validation for Volunteer Distributed Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `bounded-work-validation-for-volunteer-distributed-training-1ea9571e1d3f`
Run ID: `bounded-work-validation-for-volunteer-distributed-training-1ea9571e1d3f-20260610T143105822320+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e459d80f48bf

## What looked useful

Bounded audits are useful as detectors, but rejection alone is not sufficient: dropping rejected shards worsened aggregate-gradient error. The practical pattern supported by this run is audit plus repair/requeue/redundancy.

## Boundaries and scale limits

No real distributed system, secure commitment layer, adaptive adversary, privacy mechanism, GPU kernel validation, multi-step convergence run, or large-model training was tested. Rejected shards were repaired by trusted recomputation in simulation rather than by a live requeue/redundancy protocol.

## Claim scope

In a synthetic single-step logistic-regression gradient-shard simulation, post-submission bounded recomputation of k sampled per-example receipts detects lazy or corrupted volunteer worker submissions at rates matching the sampling model; for 10% corruption across 4 of 16 workers, k=8 detected 95.6% to 97.4% of trials with 3.12% audit overhead.

## Why it stopped

No-paper closure: this run provides synthetic mechanism evidence, not direct volunteer distributed training validation or publication-grade evidence.

## Recommended next action

Build a bounded end-to-end prototype with commit-before-audit, rejected-shard requeue or redundancy, and multi-step training comparison against a trusted baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-End Requeue Validation for Bounded Volunteer Training Audits
- Success threshold: Across at least three seeds, final validation loss is within 2% of trusted training, accepted aggregate-gradient relative error is lower than no-validation, and total trusted recomputation plus repair remains below 25% for 10% corrupted work.
- Stop condition: Stop if repair/requeue overhead exceeds 50% or validation loss degrades by more than 5% versus trusted training in two consecutive seeds at corruption rates of 10% or lower.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-work-validation-for-volunteer-distributed-training-1ea9571e1d3f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
