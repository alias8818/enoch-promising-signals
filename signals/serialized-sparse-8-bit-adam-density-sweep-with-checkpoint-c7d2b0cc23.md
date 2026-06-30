# Serialized sparse 8-bit Adam density sweep with checkpoint-resume on larger local CNN and tiny transformer tasks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `serialized-sparse-8-bit-adam-density-sweep-with-checkpoint-c7d2b0cc23`
Run ID: `serialized-sparse-8-bit-adam-density-sweep-with-checkpoint-c7d2b0cc23-20260522T140235406272+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Follow-up recommended
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Serialized sparse 8-bit Adam state on a small transformer or CNN convergence task: enoch://control-plane/projects/serialized-sparse-8-bit-adam-state-on-a-small-transformer-52b774befd/runs/serialized-sparse-8-bit-adam-state-on-a-small-transformer-52b774befd-20260522T104934530037+0000
- Parent run decision: Stabilized sparse 8-bit Adam state with real small-model convergence check: enoch://control-plane/projects/stabilized-sparse-8-bit-adam-state-with-real-small-model-c-410cdc6d22/runs/stabilized-sparse-8-bit-adam-state-with-real-small-model-c-410cdc6d22-20260522T102304594496+0000

## What looked useful

The implementation demonstrates exact checkpoint-resume for serialized sparse int8 Adam and a strong optimizer-state size reduction, but quality is density-sensitive: CNN density 0.5 is usable but materially below dense Adam, density 0.25/0.125 collapse, and the transformer experiment did not establish a learning baseline.

## Boundaries and scale limits

CPU-only local worker, no visible GPU, no Python ML stack, one seed per final configuration, synthetic CNN and synthetic transformer-shaped sequence task only, no real image or language dataset, no GPT-2-scale baseline, no multi-seed robustness.

## Claim scope

On self-contained local synthetic tasks, serialized sparse int8 Adam is checkpoint-resumable and reduces optimizer-state footprint by about 85.9%; at density 0.5 it retains 79.7% of dense Adam CNN validation accuracy, while lower densities fail and the tiny transformer quality result is inconclusive because dense Adam stayed near chance.

## Why it stopped

Bounded local validation produced mixed direct evidence: checkpointing and state reduction worked, but CNN accuracy loss was material and transformer quality retention was not testable because the dense transformer baseline did not learn.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded action is a validated multi-seed transformer/CNN rerun with a dense baseline that reaches a prespecified non-chance target before evaluating sparse8 quality retention.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Validated multi-seed sparse8 Adam retention on learnable CNN and transformer tasks
- Success threshold: Sparse8 density 0.5 retains at least 90% of dense Adam validation accuracy or equivalent loss improvement on both validated tasks across at least 3 seeds, with at least 80% optimizer-state reduction and exact checkpoint-resume within 1e-9 loss difference on one representative run.
- Stop condition: Stop negative if dense baselines fail to learn after task calibration, if sparse8 density 0.5 falls below 90% dense quality on either task, or if checkpoint-resume diverges beyond 1e-9 final loss difference.

## Evidence references

- Artifact root: `<local-path>/projects/serialized-sparse-8-bit-adam-density-sweep-with-checkpoint-c7d2b0cc23`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
