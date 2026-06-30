# Deterministic PyTorch Microbatch Replay Audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-pytorch-microbatch-replay-audit-144b4c0c27`
Run ID: `deterministic-pytorch-microbatch-replay-audit-144b4c0c27-20260527T052713206602+0000`

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

- Parent run decision: Verifiable Microbatch Replays for Volunteer Training: enoch://control-plane/projects/verifiable-microbatch-replays-for-volunteer-training-d7c3c0433735/runs/verifiable-microbatch-replays-for-volunteer-training-d7c3c0433735-20260525T060020891522+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4f14132308e8

## What looked useful

Full-state replay was bitwise exact over 23 post-checkpoint microbatches in 5 of 5 seeds. Missing RNG state diverged immediately in stochastic samples/losses, and missing accumulated gradients diverged at the next optimizer update despite matching sample order.

## Boundaries and scale limits

Synthetic dataset, tiny MLP, one process, one CPU thread, no CUDA, no AMP, no distributed training, no multi-worker DataLoader, no transformer-scale model, and no production file-backed checkpoint stack.

## Claim scope

In a controlled CPU-only PyTorch 2.12.0 toy training loop with stochastic sampling, input noise, dropout, AdamW, and gradient accumulation, exact post-interrupt microbatch replay was achieved across 5 seeds when model state, optimizer state, microbatch index, RNG state, and accumulated gradients were restored.

## Why it stopped

Tier 1 controlled direct test met its threshold and produced useful mechanism evidence, but the evidence is too small and local for a paper-ready claim.

## Recommended next action

Run a bounded deepen follow-up in a realistic small transformer trainer with file-backed checkpoints, DataLoader state, AMP disabled/enabled ablation, and GPU if available; keep the same bitwise replay and omitted-state controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Transformer File-Checkpoint Microbatch Replay Audit
- Success threshold: Full-state replay has max loss and parameter absolute difference exactly 0.0 for all seeds over the post-checkpoint window, while every omitted-state control diverges on samples, losses, gradients, or parameters.
- Stop condition: Stop if full-state replay diverges after deterministic settings and checkpoint contents are verified, or if the controls do not distinguish omitted replay-state mechanisms.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-pytorch-microbatch-replay-audit-144b4c0c27`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
