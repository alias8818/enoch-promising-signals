# Measured multiprocessing CPU gossip versus FedAvg

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `measured-multiprocessing-cpu-gossip-versus-fedavg-29d8d02f7c`
Run ID: `measured-multiprocessing-cpu-gossip-versus-fedavg-29d8d02f7c-20260529T102333398350+0000`

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

- Parent run decision: Asynchronous gossip averaging for local CPU federated training: enoch://control-plane/projects/asynchronous-gossip-averaging-for-local-cpu-federated-training-51caa8358bac/runs/asynchronous-gossip-averaging-for-local-cpu-federated-training-51caa8358bac-20260529T064833634983+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/05ed41879930

## What looked useful

Across the main 5-seed Tier 1 run, gossip achieved 0.73131 mean accuracy versus FedAvg 0.72875, with a +0.00256 accuracy delta and 0.50 modeled-byte ratio. Alpha 1 and alpha 6 heterogeneity sweeps also passed the same threshold.

## Boundaries and scale limits

Synthetic binary logistic regression only; 8 local CPU processes; modeled communication bytes rather than measured IPC or network transfer; coordinator still schedules the gossip condition; no neural-network, real-dataset, straggler, or multi-machine validation.

## Claim scope

On a small synthetic non-IID logistic-regression task run with Python multiprocessing on 8 CPU worker processes, alternating one-neighbor ring gossip matched FedAvg test accuracy within the predeclared 1 percentage point margin while using 50% of FedAvg modeled model-traffic bytes.

## Why it stopped

Controlled Tier 1 direct test completed and supports the mechanism, but evidence is synthetic and partially modeled, so it is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run a bounded deepen follow-up that replaces modeled bytes with measured IPC or socket transfer on a small real dataset and preserves the same accuracy-with-traffic threshold.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Measured IPC ring gossip versus FedAvg on a small real dataset
- Success threshold: Gossip mean accuracy no worse than 1 percentage point below FedAvg and measured transfer bytes at most 60% of FedAvg, with no more than 10% wall-clock regression on 5 paired seeds.
- Stop condition: Stop as negative if measured transfer is above 60% of FedAvg or gossip mean accuracy falls more than 1 percentage point below FedAvg on the paired real-dataset run.

## Evidence references

- Artifact root: `<local-path>/projects/measured-multiprocessing-cpu-gossip-versus-fedavg-29d8d02f7c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
