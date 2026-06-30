# CUDA salted-gradient replay audit with AMP and dataloader controls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cuda-salted-gradient-replay-audit-with-amp-and-dataloader-01bccc2fbe`
Run ID: `cuda-salted-gradient-replay-audit-with-amp-and-dataloader-01bccc2fbe-20260620T114529352459+0000`

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

- Parent run decision: Real framework salted-gradient replay audit with nondeterminism controls: enoch://control-plane/projects/real-framework-salted-gradient-replay-audit-with-nondeterm-d3b29c83c5/runs/real-framework-salted-gradient-replay-audit-with-nondeterm-d3b29c83c5-20260620T110452106261+0000
- Parent run decision: Deterministic Gradient Replay Audit for Volunteer Submissions: enoch://control-plane/projects/deterministic-gradient-replay-audit-for-volunteer-submissions-d29fd7a12865/runs/deterministic-gradient-replay-audit-for-volunteer-submissions-d29fd7a12865-20260620T104431943061+0000

## What looked useful

Controlled replay conditions had loss_max_abs_diff 0.0, audit_match_rate 1.0, and matching parameter digests across 24-step paired replays; the uncontrolled two-worker DataLoader negative control had loss_max_abs_diff 0.028856754302978516, audit_match_rate 0.0, and nonmatching parameter digests.

## Boundaries and scale limits

No CUDA device or NVIDIA runtime was available on this worker, so CUDA AMP behavior, GPU nondeterminism, GB10 memory behavior, and larger training workloads were not directly tested.

## Claim scope

On a CPU-only PyTorch 2.12.1 synthetic MLP replay task, salted gradient digests were stable under fixed-seed controlled replays with FP32, two DataLoader workers, and CPU bfloat16 autocast, and they detected uncontrolled DataLoader replay drift.

## Why it stopped

Finalizing as no-paper useful signal because this worker produced only CPU direct evidence and CPU AMP proxy evidence, not direct CUDA validation.

## Recommended next action

Run the same harness on a CUDA-enabled GB10/GPU worker with CUDA autocast, fixed seeds, DataLoader worker controls, checkpoint reload replay, and multiple seeds before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CUDA salted-gradient replay audit with checkpoint reload and multi-seed controls
- Success threshold: For controlled CUDA conditions, audit_match_rate >= 0.99 and parameter digest match or documented deterministic numeric tolerance across paired replays; for uncontrolled negative controls, audit_match_rate <= 0.25 or clear loss/parameter divergence.
- Stop condition: Stop if CUDA controlled replays cannot be made stable after deterministic settings and DataLoader seeding, or if the salted audit fails to distinguish controlled replays from uncontrolled negative controls.

## Evidence references

- Artifact root: `<local-path>/projects/cuda-salted-gradient-replay-audit-with-amp-and-dataloader-01bccc2fbe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
