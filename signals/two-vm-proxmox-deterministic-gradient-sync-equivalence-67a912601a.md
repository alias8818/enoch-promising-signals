# Two-VM Proxmox Deterministic Gradient Sync Equivalence

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `two-vm-proxmox-deterministic-gradient-sync-equivalence-67a912601a`
Run ID: `two-vm-proxmox-deterministic-gradient-sync-equivalence-67a912601a-20260612T205855558247+0000`

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

- Parent run decision: Home Distributed Training: First-Proof Toy Sync on Local Proxmox: enoch://control-plane/projects/home-distributed-training-first-proof-toy-sync-on-local-proxmox-bec0057ff789/runs/home-distributed-training-first-proof-toy-sync-on-local-proxmox-bec0057ff789-20260611T220941882128+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/64970e5b76f9

## What looked useful

Fixed-order synchronous gradient averaging can provide bitwise trajectory equivalence to a matching deterministic two-shard baseline in a controlled two-process TCP setting; broken controls diverged from intended full-batch behavior.

## Boundaries and scale limits

Not run on actual Proxmox guest VMs, multi-host networking, GPU collectives, PyTorch DDP, or large models. Monolithic full-batch comparison is limited by floating-point reduction-order roundoff.

## Claim scope

In a bounded local CPU test, two independent Python worker processes exchanging deterministic gradient tensors over TCP loopback exactly matched each other and the deterministic two-shard single-process baseline across 8 seeds, 60 steps, and a small MLP regression workload.

## Why it stopped

Tier 1 local direct mechanism test completed with useful support, but actual two-VM Proxmox evidence was not available in this worker and the result is not paper-positive.

## Recommended next action

Run the same harness across two actual Proxmox guest VMs over a virtual bridge and require exact rank-to-rank and deterministic-baseline equivalence under light scheduling/network jitter before considering broader validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Actual Proxmox Two-VM Deterministic Gradient Sync Equivalence
- Success threshold: Across at least 20 seeds and 100 steps on two actual Proxmox VMs, synchronized ranks and deterministic two-shard baseline have max absolute parameter difference 0.0, while both controls diverge from monolithic full-batch by greater than 1e-6.
- Stop condition: Stop as unsupported if any correctly configured seed produces nonzero rank-to-rank or deterministic-baseline parameter difference, or if VM setup cannot expose reproducible configuration and logs.

## Evidence references

- Artifact root: `<local-path>/projects/two-vm-proxmox-deterministic-gradient-sync-equivalence-67a912601a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
