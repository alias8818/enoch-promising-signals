# Measured IPC ring gossip versus FedAvg on a small real dataset

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `measured-ipc-ring-gossip-versus-fedavg-on-a-small-real-dat-e1b5a2cdde`
Run ID: `measured-ipc-ring-gossip-versus-fedavg-on-a-small-real-dat-e1b5a2cdde-20260529T153820937662+0000`

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
- Parent run decision: Measured multiprocessing CPU gossip versus FedAvg: enoch://control-plane/projects/measured-multiprocessing-cpu-gossip-versus-fedavg-29d8d02f7c/runs/measured-multiprocessing-cpu-gossip-versus-fedavg-29d8d02f7c-20260529T102333398350+0000

## What looked useful

Ring gossip over IPC produced a reproducible small-real-dataset mechanism signal: non-IID alpha=0.3 accuracy was 0.9388 versus FedAvg 0.9410, with 0.50x estimated IPC bytes and 0.629x wall time; IID-ish alpha=10 accuracy was 0.9421 versus FedAvg 0.9427 with the same byte reduction.

## Boundaries and scale limits

Small tabularized image dataset, small convex model, local multiprocessing queues, estimated payload bytes rather than instrumented OS/network traffic, 8 clients, synchronous rounds, no straggler or network transport study.

## Claim scope

On UCI Optical Digits with 8 local multiprocessing clients, fixed non-IID and IID-ish partitions, and a NumPy softmax classifier, synchronous one-neighbor IPC ring gossip matched FedAvg within about 0.3 percentage points while using half the estimated model-transfer bytes and lower wall time.

## Why it stopped

Tier-2 evidence supports the local mechanism but is not publication-grade; the run is intentionally closed as no-paper useful signal rather than a broad FedAvg replacement claim.

## Recommended next action

Run a bounded deepen follow-up with a larger real dataset/model, instrumented IPC or network bytes, 16-32 clients, and ring-degree/topology plus straggler ablations before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Instrumented ring-gossip FedAvg comparison on a larger real federated workload
- Success threshold: Across at least 5 fixed seeds, ring gossip remains within 0.5 percentage points of FedAvg accuracy while reducing measured communication or coordinator bottleneck cost by at least 30%.
- Stop condition: Stop if ring gossip loses more than 1.0 percentage point versus FedAvg in both IID-ish and non-IID settings, or if measured communication savings disappear once full IPC/network overhead is instrumented.

## Evidence references

- Artifact root: `<local-path>/projects/measured-ipc-ring-gossip-versus-fedavg-on-a-small-real-dat-e1b5a2cdde`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
