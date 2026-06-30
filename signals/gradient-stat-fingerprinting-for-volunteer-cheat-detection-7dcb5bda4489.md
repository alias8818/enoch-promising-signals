# Gradient-stat fingerprinting for volunteer cheat detection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-stat-fingerprinting-for-volunteer-cheat-detection-7dcb5bda4489`
Run ID: `gradient-stat-fingerprinting-for-volunteer-cheat-detection-7dcb5bda4489-20260609T094212564262+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/0601e9a052fe

## What looked useful

Across three 80-round seeds, norm-only AUROC averaged 0.525, intrinsic-stat AUROC averaged 0.842, and intrinsic+consensus AUROC averaged 0.941. Stale replay remained weak with mean AUROC 0.683, showing that replay-like cheats need explicit temporal/provenance handling.

## Boundaries and scale limits

Synthetic data only; tiny 837-parameter model; 80 rounds per seed; 30 submissions per round; 33% cheats; no real volunteer traces, adaptive adversaries, collusion-majority setting, non-IID private clients, or production-scale model validation.

## Claim scope

In a synthetic federated/volunteer-gradient simulation with a tiny PyTorch classifier, compact intrinsic gradient statistics plus round-level consensus statistics detect several common fake or corrupted gradient submissions much better than norm-only screening.

## Why it stopped

No-paper useful signal: the evidence is synthetic and bounded, and the hardest tested cheat mode, stale replay, is only partially detected.

## Recommended next action

Run a bounded deepen follow-up targeting stale replay with temporal consistency features and replay/provenance controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Temporal fingerprinting for stale gradient replay detection
- Success threshold: Mean stale-replay AUROC >= 0.85 across at least three seeds and honest acceptance >= 90% at the selected threshold.
- Stop condition: Stop if temporal features fail to improve stale-replay AUROC by at least 0.10 over the current mean of 0.683 or if honest acceptance falls below 90%.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-stat-fingerprinting-for-volunteer-cheat-detection-7dcb5bda4489`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
