# Real-Transport Volunteer FedAvg on Small Standard Dataset

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-transport-volunteer-fedavg-on-small-standard-dataset-8b62f891dd`
Run ID: `real-transport-volunteer-fedavg-on-small-standard-dataset-8b62f891dd-20260613T014921059332+0000`

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

- Parent run decision: Volunteer Bounded Training Run for Distributed Proof-of-Concept: enoch://control-plane/projects/volunteer-bounded-training-run-for-distributed-proof-of-concept-abccf34ce8f6/runs/volunteer-bounded-training-run-for-distributed-proof-of-concept-abccf34ce8f6-20260613T005735506999+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/0070cdeede09

## What looked useful

Across three seeds, 8-client HTTP FedAvg reached 0.9644 mean test accuracy with 0 stale updates, about 0.0081 below centralized training and 0.3569 above mean local-only training.

## Boundaries and scale limits

Only loopback transport, honest homogeneous clients, 8 clients, sklearn digits, 650-parameter softmax classifier, 15 FedAvg rounds, no WAN latency/dropout/security/privacy/mobile constraints, and no large model or full-scale volunteer deployment.

## Claim scope

Separate local volunteer-like client processes can run FedAvg over real localhost HTTP JSON transport on sklearn digits non-IID partitions and obtain a useful global softmax model close to a centralized same-model baseline.

## Why it stopped

Tier 1 direct test succeeded as mechanism evidence, but the result is local-loopback and small-model only, so it is no-paper useful signal rather than publication-grade validation.

## Recommended next action

Run a bounded deepen test with WAN-like latency, client dropout, and partial participation before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Intermittent Volunteer FedAvg with WAN-Like Latency and Partial Participation
- Success threshold: Median FedAvg test accuracy at least 0.90, no coordinator deadlocks, stale updates below 5% of submitted updates, and accuracy gain over mean local-only at least 0.20 across five seeds.
- Stop condition: Stop as a negative if two or more seeds deadlock/time out, stale updates exceed 10%, or median accuracy falls below 0.85 under the injected volunteer conditions.

## Evidence references

- Artifact root: `<local-path>/projects/real-transport-volunteer-fedavg-on-small-standard-dataset-8b62f891dd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
