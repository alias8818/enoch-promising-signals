# Instrumented ring-gossip FedAvg comparison on a larger real federated workload

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `instrumented-ring-gossip-fedavg-comparison-on-a-larger-rea-916b0ded69`
Run ID: `instrumented-ring-gossip-fedavg-comparison-on-a-larger-rea-916b0ded69-20260529T201420984670+0000`

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

- Parent run decision: Measured IPC ring gossip versus FedAvg on a small real dataset: enoch://control-plane/projects/measured-ipc-ring-gossip-versus-fedavg-on-a-small-real-dat-e1b5a2cdde/runs/measured-ipc-ring-gossip-versus-fedavg-on-a-small-real-dat-e1b5a2cdde-20260529T153820937662+0000
- Parent run decision: Measured multiprocessing CPU gossip versus FedAvg: enoch://control-plane/projects/measured-multiprocessing-cpu-gossip-versus-fedavg-29d8d02f7c/runs/measured-multiprocessing-cpu-gossip-versus-fedavg-29d8d02f7c-20260529T102333398350+0000

## What looked useful

Ring gossip achieved mean global accuracy 0.4074 +/- 0.0108 versus central FedAvg 0.4115 +/- 0.0165 at equal 9,344.64 MB communication, but did not beat central and had much lower personalized accuracy than local-only training: 0.3319 +/- 0.0065 versus 0.4737 +/- 0.0029.

## Boundaries and scale limits

Validation used 300 of 3,597 FEMNIST writers per seed and a shallow logistic model, not a CNN/deep model, full-client run, asynchronous network, compression, privacy mechanism, or datacenter-scale system. It is direct real federated evidence but not broad publication-grade evidence.

## Claim scope

On a bounded real FEMNIST writer-partitioned workload with 300 clients, 80 rounds, three fixed seeds, and a 48,670-parameter NumPy multinomial logistic-regression model, one-hop ring-gossip FedAvg nearly matched centralized FedAvg global pooled test accuracy at matched float32 model-byte communication.

## Why it stopped

Direct bounded validation on a larger real federated workload produced a mixed result: ring gossip was viable and close to centralized FedAvg on global accuracy, but it did not outperform the real baseline and substantially underperformed the local-only control on personalized accuracy.

## Recommended next action

Stop this run as no-paper useful evidence; a bounded adjacent follow-up should test whether denser or time-varying decentralized mixing closes the personalized-accuracy and consensus-drift gap without losing the central-FedAvg global-accuracy match.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Compare one-hop ring with denser time-varying gossip on FEMNIST personalization and consensus drift
- Success threshold: A decentralized topology must keep mean global accuracy within 1 percentage point of central FedAvg, improve personalized accuracy by at least 5 percentage points over one-hop ring, and reduce mean consensus drift below 0.35 across all three seeds without using more than 2x ring communication.
- Stop condition: Stop if no decentralized variant improves personalized accuracy by at least 3 percentage points over one-hop ring by round 80 or if all variants remain more than 2 percentage points below central FedAvg global accuracy.

## Evidence references

- Artifact root: `<local-path>/projects/instrumented-ring-gossip-fedavg-comparison-on-a-larger-rea-916b0ded69`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
