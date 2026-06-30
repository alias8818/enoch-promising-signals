# Volunteer Bounded Training Run for Distributed Proof-of-Concept

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `volunteer-bounded-training-run-for-distributed-proof-of-concept-abccf34ce8f6`
Run ID: `volunteer-bounded-training-run-for-distributed-proof-of-concept-abccf34ce8f6-20260613T005735506999+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0070cdeede09

## What looked useful

Across 5 seeds, baseline volunteer-bounded FedAvg reached 0.9944 mean accuracy vs 0.9963 for all-client sync and 0.9938 for pooled central SGD, using about 6.75 MB estimated communication vs 20.49 MB for sync. Stress and severe deadline cases degraded to 0.9923 and 0.9901 mean accuracy while dropping many more updates, showing graceful but measurable degradation on the toy task.

## Boundaries and scale limits

Evidence is synthetic and single-host only. It does not validate real volunteer machines, network transport, secure aggregation, adversarial behavior, privacy, checkpoint logistics, real datasets, or large-model training.

## Claim scope

On a local synthetic non-IID classification task, a deadline-bounded volunteer FedAvg simulation can preserve most accuracy relative to all-client synchronous FedAvg while reducing accepted updates, estimated communication, and simulated round time.

## Why it stopped

Closed as no-paper useful signal: the mechanism worked in a synthetic local simulation, but the evidence is not a real distributed proof-of-concept.

## Recommended next action

Run a bounded direct-evidence follow-up with actual localhost or LAN worker processes, real transport, checkpoint/restart behavior, and a standard small dataset before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Transport Volunteer FedAvg on Small Standard Dataset
- Success threshold: Volunteer deadline-bounded run reaches within 1 percentage point of synchronous FedAvg validation accuracy or perplexity-equivalent target while using <=50% of sync communication on the same task.
- Stop condition: Stop if real transport overhead or churn causes >3 percentage point quality loss versus sync FedAvg after matched update budget, or if checkpoint/restart cannot recover from simulated worker loss.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-bounded-training-run-for-distributed-proof-of-concept-abccf34ce8f6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
