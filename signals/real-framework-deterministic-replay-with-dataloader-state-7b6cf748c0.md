# Real Framework Deterministic Replay With DataLoader State And Atomic Faults

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `78`
Project ID: `real-framework-deterministic-replay-with-dataloader-state-7b6cf748c0`
Run ID: `real-framework-deterministic-replay-with-dataloader-state-7b6cf748c0-20260514T043637472388+0000`

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

- Internal Enoch project: Real Framework Deterministic Replay With DataLoader State And Atomic Faults: internal_generated:real-framework-deterministic-replay-with-dataloader-state-7b6cf748c0

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 3 bounded validation found exact replay for single-worker sampler-state plus atomic checkpoints, but a common multi-worker DataLoader configuration failed 0/9 replay cases, so the current mechanism is not paper-positive.

## Recommended next action

Stop this run as no-paper: bounded PyTorch validation supports single-worker replay but the num_workers=2 stress probe falsifies the broader real-framework DataLoader-state claim; next work should implement and test prefetch-aware DataLoader replay state.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Prefetch-aware PyTorch DataLoader replay state for multi-worker checkpoint recovery
- Success threshold: For num_workers=2 and num_workers=4, proposed replay matches the uninterrupted final digest in 100% of overwrite-fault cases across three seeds and at least four checkpoint positions, while missing-state and non-atomic controls fail as expected.
- Stop condition: Stop if proposed multi-worker replay has any digest mismatch in overwrite-fault recovery after the DataLoader state mechanism is implemented, or if framework internals make in-flight state capture impossible without unsupported private APIs.

## Evidence references

- Artifact root: `<local-path>/projects/real-framework-deterministic-replay-with-dataloader-state-7b6cf748c0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
