# Intermittent Volunteer FedAvg with WAN-Like Latency and Partial Participation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `intermittent-volunteer-fedavg-with-wan-like-latency-and-pa-8c0c0c6395`
Run ID: `intermittent-volunteer-fedavg-with-wan-like-latency-and-pa-8c0c0c6395-20260613T021531604325+0000`

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

- Parent run decision: Volunteer Bounded Training Run for Distributed Proof-of-Concept: enoch://control-plane/projects/volunteer-bounded-training-run-for-distributed-proof-of-concept-abccf34ce8f6/runs/volunteer-bounded-training-run-for-distributed-proof-of-concept-abccf34ce8f6-20260613T005735506999+0000
- Parent run decision: Real-Transport Volunteer FedAvg on Small Standard Dataset: enoch://control-plane/projects/real-transport-volunteer-fedavg-on-small-standard-dataset-8b62f891dd/runs/real-transport-volunteer-fedavg-on-small-standard-dataset-8b62f891dd-20260613T014921059332+0000

## What looked useful

Accepting delayed volunteer updates beat deadline-only dropping by +1.32 to +1.48 percentage points final accuracy at identical logical time across 5/5 fixed seeds. However, exponential staleness weighting was slightly worse than the unweighted stale-update ablation, so the specific weighting mechanism is not supported.

## Boundaries and scale limits

Synthetic classification only; no real WAN traces, no real volunteer device churn, no secure aggregation overhead, no privacy accounting, no deep nonconvex model, and no public FL benchmark dataset.

## Claim scope

In a deterministic synthetic non-IID FedAvg simulator with WAN-like sampled latency, partial volunteer availability, 60 clients, 5 fixed seeds, and a logistic classifier, accepting late volunteer updates with a max-staleness cap recovered most of synchronous FedAvg final accuracy at deadline-style logical wall time.

## Why it stopped

Tier 2 medium synthetic evidence produced a useful mixed signal but is not paper-positive; the proposed staleness weighting failed its ablation against unweighted stale acceptance.

## Recommended next action

Run a bounded real-dataset FL benchmark comparing sync FedAvg, deadline dropping, unweighted stale acceptance, and staleness-weighted acceptance on FEMNIST or CIFAR non-IID with the same fixed seeds and latency model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-dataset validation of capped stale volunteer FedAvg under WAN latency
- Success threshold: Unweighted or weighted stale acceptance beats deadline-only dropping by at least 1 percentage point final accuracy or 10% time-to-threshold on 4/5 seeds, while staying within 1 percentage point of synchronous FedAvg final accuracy at less than half its logical time.
- Stop condition: Stop if stale acceptance fails to beat deadline-only dropping on at least 3/5 seeds or if staleness weighting again underperforms unweighted acceptance without a latency-tail regime where it helps.

## Evidence references

- Artifact root: `<local-path>/projects/intermittent-volunteer-fedavg-with-wan-like-latency-and-pa-8c0c0c6395`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
