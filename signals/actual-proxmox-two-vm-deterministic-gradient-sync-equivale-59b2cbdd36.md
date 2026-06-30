# Actual Proxmox Two-VM Deterministic Gradient Sync Equivalence

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `actual-proxmox-two-vm-deterministic-gradient-sync-equivale-59b2cbdd36`
Run ID: `actual-proxmox-two-vm-deterministic-gradient-sync-equivale-59b2cbdd36-20260612T230906357185+0000`

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

- Parent run decision: Two-VM Proxmox Deterministic Gradient Sync Equivalence: enoch://control-plane/projects/two-vm-proxmox-deterministic-gradient-sync-equivalence-67a912601a/runs/two-vm-proxmox-deterministic-gradient-sync-equivalence-67a912601a-20260612T205855558247+0000
- Parent run decision: Home Distributed Training: First-Proof Toy Sync on Local Proxmox: enoch://control-plane/projects/home-distributed-training-first-proof-toy-sync-on-local-proxmox-bec0057ff789/runs/home-distributed-training-first-proof-toy-sync-on-local-proxmox-bec0057ff789-20260611T220941882128+0000

## What looked useful

Weighted synchronous gradient averaging is mechanism-supported locally: max parameter deltas were 1.6653345369377348e-16 for float64 and 5.960464477539063e-08 for float32 across five seeds, below the configured thresholds. The unweighted reducer and local-no-sync controls exceeded the mismatch threshold.

## Boundaries and scale limits

No second Proxmox guest VM was available in this project workspace, so VM boundary effects, network transport, guest heterogeneity, and actual two-VM orchestration were not tested. The model/data are synthetic medium-scale NumPy MLP runs, not framework DDP or large-model training.

## Claim scope

On one Proxmox-kernel CPU worker, a deterministic two-local-process weighted gradient synchronization harness matched a single-process full-batch MLP baseline across five fixed seeds in float64 and float32, while wrong-reducer and no-sync controls diverged.

## Why it stopped

The Tier 2 local-process mechanism confirmation passed, but the literal actual two-VM Proxmox claim remains unvalidated because this worker exposes only one Proxmox-kernel CPU VM.

## Recommended next action

Stop this run as no-paper useful-signal evidence; rerun the same harness with one worker in each of two actual Proxmox guest VMs before making the project-title claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two Proxmox Guest VM Gradient Sync Equivalence Replay
- Success threshold: For five fixed seeds, weighted two-VM sync has max final parameter delta <= 1e-10 in float64 and <= 1e-5 in float32 versus the full-batch baseline, while both controls exceed 1e-4.
- Stop condition: Stop if either weighted sync threshold fails on any seed, if controls do not diverge, or if Proxmox guest/network nondeterminism prevents reproducible fixed-seed runs after one clean retry.

## Evidence references

- Artifact root: `<local-path>/projects/actual-proxmox-two-vm-deterministic-gradient-sync-equivale-59b2cbdd36`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
