# Real multi-host volunteer CPU gradient-compression benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-multi-host-volunteer-cpu-gradient-compression-benchma-19b8afc317`
Run ID: `real-multi-host-volunteer-cpu-gradient-compression-benchma-19b8afc317-20260609T214331885188+0000`

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

- Parent run decision: Volunteer CPU Training with Gradient Compression for Home Hardware: enoch://control-plane/projects/volunteer-cpu-training-with-gradient-compression-for-home-hardware-36df1dd6923c/runs/volunteer-cpu-training-with-gradient-compression-for-home-hardware-36df1dd6923c-20260609T153632797187+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/11df40c64e18

## What looked useful

Bandwidth-sensitive mechanism support: q8 is a practical candidate for volunteer CPU gradient exchange when uplink bandwidth is constrained; 1% top-k is byte-efficient but too lossy in this direct reconstruction test without further optimizer evidence.

## Boundaries and scale limits

No physical multi-host volunteer deployment, no real WAN loss/jitter, no kernel-level traffic shaping, no live model training loop, no convergence or final accuracy measurement, and only 4 local worker processes on one 8-core CPU host.

## Claim scope

Controlled single-host multi-process TCP benchmark with deterministic synthetic float32 gradients. q8 gradient compression reduced wire bytes by 4x, improved shaped 100 Mbps/10 ms wall-clock from 4.802 s to 2.310 s, and introduced about 7.0% aggregate relative L2 error. 1% top-k reduced bytes about 50x but produced about 63% aggregate relative L2 error.

## Why it stopped

No-paper useful signal: the run met the controlled small direct TCP benchmark target, but evidence remains single-host and synthetic, so it cannot validate the real multi-host volunteer training claim.

## Recommended next action

Run the same harness across 2-4 actual commodity hosts or VMs with a small model training loop and compare dense vs q8 on wall-clock-to-target-loss, bytes, and final validation quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Two-to-four-host q8 gradient compression training benchmark
- Success threshold: q8 achieves at least 1.5x faster wall-clock-to-target-loss or epoch completion than dense, with at least 3.5x fewer transmitted bytes and no more than 2% relative final validation-metric regression.
- Stop condition: Stop if q8 is slower than dense at matched training quality, fails to reach the dense target loss, or shows more than 2% relative validation degradation in two controlled repeats.

## Evidence references

- Artifact root: `<local-path>/projects/real-multi-host-volunteer-cpu-gradient-compression-benchma-19b8afc317`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
