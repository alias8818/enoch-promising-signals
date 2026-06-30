# Stochastic Microbatch Replay Audit

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `stochastic-microbatch-replay-audit-c4e4b09cd7f7`
Run ID: `stochastic-microbatch-replay-audit-c4e4b09cd7f7-20260628T202911970930+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/afca895b5ac5

## What looked useful

Full event logging and stateless step seeding reproduced losses and final parameters exactly under injected RNG drift. Index-only and initial-seed-only replay diverged with dropout active, while controls showed exact replay when RNG drift or dropout was removed.

## Boundaries and scale limits

Synthetic 8192-example classification task, 160 optimizer steps, 640 microbatch events, one GB10 host, one seed, no dataloader workers, no distributed training, no mixed precision, no checkpoint/restart replay, and no transformer/LLM workload.

## Claim scope

On a small PyTorch CUDA MLP with stochastic microbatch sampling, gradient accumulation, and dropout, exact replay under audit-time RNG drift requires either per-microbatch pre-forward RNG restoration or stateless per-step seeding; initial-seed-only and index-only replay fail when model stochasticity is active.

## Why it stopped

Synthetic proxy evidence is sufficient to falsify naive replay under stochastic RNG drift, but not sufficient for a paper or broad training-stack validation.

## Recommended next action

Stop this run as a bounded no-paper useful signal; next run should test stateless per-sample/per-layer RNG replay in a small transformer stack with dataloader workers and checkpoint/restart.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Checkpointed Transformer Stateless Replay Audit
- Success threshold: Across at least 3 seeds and 3 checkpoint positions, stateless replay has max loss and parameter-delta error <= 1e-7 relative to reference replay while using at least 50x less metadata than full RNG snapshots; naive seed/index baselines must fail under the same injected drift.
- Stop condition: Stop if stateless replay diverges above 1e-7 in any seed/checkpoint after deterministic-kernel and event-boundary bugs are ruled out, or if the run exceeds the local bounded budget without checkpointed metrics.

## Evidence references

- Artifact root: `<local-path>/projects/stochastic-microbatch-replay-audit-c4e4b09cd7f7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
