# Federated learning gradient compression for home GPU clusters

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `federated-learning-gradient-compression-for-home-gpu-clusters-b8b4e411cc3b`
Run ID: `federated-learning-gradient-compression-for-home-gpu-clusters-b8b4e411cc3b-20260610T164428217366+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/6e35676d305a

## What looked useful

On the harder synthetic non-IID task, dense reached 0.9810 accuracy after 27.451 MB sent. q8 reached 0.9812 accuracy with 6.864 MB, sign reached 0.9790 with 0.859 MB, top-k with error feedback reached 0.9631 with 0.550 MB, and random-k reached only 0.4893 with the same 0.550 MB budget. Top-k without error feedback dropped to 0.9067 accuracy and crossed 90% accuracy much later.

## Boundaries and scale limits

Synthetic data, one GPU host, modeled payload bytes only, one main seed, small MLP with 34k-101k parameters, no real home network, no wall-clock distributed training, no secure aggregation or multi-host straggler behavior.

## Claim scope

Single-host GB10 simulation of synchronous federated learning on a synthetic non-IID classification task: q8 and sign update compression preserved dense-like final accuracy with large modeled byte reductions; 1% top-k required error feedback and slower convergence; 1% random sparsification failed.

## Why it stopped

Evidence is a synthetic single-host proxy, not full validation for home GPU clusters; it is sufficient to guide the next test but not to support a paper.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded action is a two-host or network-emulated FL run on a real dataset measuring wall-clock time-to-accuracy and actual bytes on the wire.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-network FL compression comparison for home GPU clusters
- Success threshold: q8 or sign achieves at least 95% of dense final accuracy, no more than 2 percentage points lower absolute accuracy, and at least 2x lower wall-clock time-to-90%-accuracy under a bandwidth cap representative of a home network.
- Stop condition: Stop if compressed modes do not improve wall-clock time-to-target under bandwidth shaping or if final accuracy drops by more than 2 percentage points versus dense in two seeds.

## Evidence references

- Artifact root: `<local-path>/projects/federated-learning-gradient-compression-for-home-gpu-clusters-b8b4e411cc3b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
