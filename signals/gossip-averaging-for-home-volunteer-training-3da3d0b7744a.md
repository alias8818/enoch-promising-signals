# Gossip Averaging for Home Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gossip-averaging-for-home-volunteer-training-3da3d0b7744a`
Run ID: `gossip-averaging-for-home-volunteer-training-3da3d0b7744a-20260522T173954324267+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/79d3f7dbc52f

## What looked useful

Single-step gossip averaging is the promising operating point: it nearly matched the central baseline on validation accuracy in the non-IID proxy and improved loss versus isolation, while four gossip steps mainly reduced consensus error at higher-than-central communication cost. Near-IID partitions showed little practical loss benefit over isolated local training.

## Boundaries and scale limits

Synthetic binary logistic regression only; no real dataset, neural model, asynchronous peer timing, heterogeneous hardware, real bandwidth/latency constraints, compression, privacy/security, NAT traversal, or large-scale volunteer deployment was tested.

## Claim scope

In a small synthetic convex logistic-regression simulation with 32 churny volunteers and label-skewed non-IID shards, one randomized pairwise gossip averaging exchange per online round matched centralized averaging accuracy within about 0.05 percentage points while reducing consensus variance versus isolated local training and using about 48-50% of the central upload/broadcast parameter traffic.

## Why it stopped

Closed as a no-paper useful-signal proxy result: the mechanism is supported in a small synthetic setting but this is not direct/full validation of home volunteer training.

## Recommended next action

Run a bounded real-dataset neural follow-up with asynchronous churn and matched byte budgets before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Asynchronous gossip averaging on a real small-vision dataset under matched byte budgets
- Success threshold: Gossip reaches within 1.0 validation accuracy point of FedAvg while transferring <=60% of FedAvg bytes and improving validation loss over isolated local training in the non-IID/churn condition.
- Stop condition: Stop negative if gossip is more than 2.0 accuracy points below FedAvg or fails to improve validation loss over isolated training at <=60% FedAvg bytes across at least 3 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/gossip-averaging-for-home-volunteer-training-3da3d0b7744a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
