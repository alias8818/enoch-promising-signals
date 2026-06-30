# Toy Trainer Validation of Microbatch Commitment-Challenge Replay Defense

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `toy-trainer-validation-of-microbatch-commitment-challenge-54b71b54d0`
Run ID: `toy-trainer-validation-of-microbatch-commitment-challenge-54b71b54d0-20260607T172639606425+0000`

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

- Parent run decision: Micro-Batch Commitment-Challenge for Gradient Replay Defense: enoch://control-plane/projects/micro-batch-commitment-challenge-for-gradient-replay-defense-f164d0338289/runs/micro-batch-commitment-challenge-for-gradient-replay-defense-f164d0338289-20260607T133145307189+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/db9f9c4c51eb

## What looked useful

Across 3,960 attempted stale replay updates, the undefended baseline accepted 3,960/3,960 while the defended protocol accepted 0/3,960 after the first honest warmup step. Honest defended training accepted 4,000/4,000 updates with zero false rejects.

## Boundaries and scale limits

Tested only on synthetic binary classification with a NumPy toy trainer, 8 seeds, 5 challenge sizes, batch size 32, and 100 steps per run. Not tested on transformer training, distributed data pipelines, real optimizer state, networked trainers, cryptographic proof costs, or adaptive attackers that recompute valid current gradients.

## Claim scope

In a deterministic toy logistic-regression trainer, a microbatch commitment plus post-commit random per-example gradient challenge rejects stale previous-microbatch replay attempts while accepting honest current-microbatch updates.

## Why it stopped

Tier 1 controlled direct test completed with mechanism support, but evidence remains toy-scale and is not publication-grade.

## Recommended next action

Run a medium direct confirmation in a small transformer or GPT-2-small-class trainer with real dataloader microbatch IDs, optimizer state, audit overhead, and adaptive partial-replay attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Transformer Validation of Microbatch Commitment-Challenge Replay Defense
- Success threshold: Defended attack accept rate below 1% across stale and partial replay variants with honest false reject rate 0% and audit overhead below 10% in a bounded small-transformer run.
- Stop condition: Stop if honest false rejects are nonzero under deterministic replayable inputs, defended attack accept rate is 5% or higher, or audit overhead exceeds 25% before any model-quality benefit can be assessed.

## Evidence references

- Artifact root: `<local-path>/projects/toy-trainer-validation-of-microbatch-commitment-challenge-54b71b54d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
