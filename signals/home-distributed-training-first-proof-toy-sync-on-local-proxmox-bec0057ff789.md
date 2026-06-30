# Home Distributed Training: First-Proof Toy Sync on Local Proxmox

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `home-distributed-training-first-proof-toy-sync-on-local-proxmox-bec0057ff789`
Run ID: `home-distributed-training-first-proof-toy-sync-on-local-proxmox-bec0057ff789-20260611T220941882128+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/64970e5b76f9

## What looked useful

The first-proof sync mechanism works at toy scale and exposes a practical latency trap: small synchronous TCP messages can be dominated by delayed ACK/Nagle behavior unless TCP_NODELAY or message batching is used.

## Boundaries and scale limits

Single host only; loopback TCP only; synthetic linear regression only; no actual multi-VM LAN, GPU, PyTorch distributed backend, fault tolerance, checkpoint recovery, large neural model, or long training run was tested.

## Claim scope

On one CPU Proxmox worker, a deterministic toy synchronous gradient-average protocol over localhost TCP across 1, 2, and 4 Python worker processes exactly matched centralized SGD on synthetic linear regression, and TCP_NODELAY reduced tiny-message sync latency from about 85 ms/step to below 2 ms/step in the tested local runs.

## Why it stopped

The result is a bounded local toy proof with exact correctness and useful latency evidence, but it is proxy-only for home multi-VM distributed training and is not publication-grade.

## Recommended next action

Stop this run as no-paper useful signal; if continuing, run the same deterministic equivalence harness across two actual Proxmox VMs over the physical LAN and compare TCP_NODELAY, batching, and a PyTorch distributed baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-VM Proxmox Deterministic Gradient Sync Equivalence
- Success threshold: Distributed two-VM training matches centralized final weights within 1e-9 L-infinity or a justified framework tolerance, final loss differs by less than 1e-9 for the NumPy harness, and median sync latency is below 10 ms with P95 below 25 ms for 4 KiB to 64 KiB per-step payloads.
- Stop condition: Stop if two-VM deterministic equivalence fails after protocol/debug fixes, or if median sync latency remains above 25 ms with TCP_NODELAY and batching for the toy payload sizes.

## Evidence references

- Artifact root: `<local-path>/projects/home-distributed-training-first-proof-toy-sync-on-local-proxmox-bec0057ff789`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
