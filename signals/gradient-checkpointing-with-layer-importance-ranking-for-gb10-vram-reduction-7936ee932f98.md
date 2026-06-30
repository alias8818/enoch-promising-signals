# Gradient Checkpointing with Layer Importance Ranking for gb10 VRAM Reduction

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gradient-checkpointing-with-layer-importance-ranking-for-gb10-vram-reduction-7936ee932f98`
Run ID: `gradient-checkpointing-with-layer-importance-ranking-for-gb10-vram-reduction-7936ee932f98-20260607T004427765613+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/63bd8534a579

## What looked useful

Activation checkpointing itself saved 17.07% peak PyTorch CUDA allocator memory on the main shape, with all-layer overhead around 14.21% and selective k=6 overhead around 7.20-7.72%. Importance-ranked selection tied random selection on peak memory at k=3, k=6, and k=9 and was slightly slower than random at k=6 and k=9. The correctness smoke showed standard checkpointing is mathematically exact here, with max gradient difference 0.0, so layer importance does not provide an accuracy-preservation mechanism under ordinary checkpointing.

## Boundaries and scale limits

Tested synthetic batches only: 12 transformer blocks, dim 768, seq_len 384, batch 4, checkpoint budgets k=3, k=6, and k=9. Did not test real corpus convergence, GPT-2-small-class full training, 7B+ models, sharded optimizers, PyTorch compile planners, or hardware-level UMA residency because GB10 nvidia-smi memory accounting is unavailable.

## Claim scope

On a local GB10 CUDA/PyTorch 12-layer GPT-style transformer benchmark, standard activation checkpointing reduces peak PyTorch allocator memory, but selecting checkpointed layers by a pilot activation-gradient importance score does not outperform a seeded random selective policy at matched checkpoint budgets.

## Why it stopped

Moderate local GB10 evidence is an early falsification of the layer-importance-ranking novelty, not a full validation across large models or real training corpora.

## Recommended next action

Stop this project as an importance-ranking paper candidate; redirect any future local work toward memory-lifetime-aware selective checkpoint planning compared against random and early-layer baselines.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Memory-lifetime-aware selective checkpoint planning on GB10
- Success threshold: At matched checkpoint count or matched overhead, the lifetime-aware selector reduces peak allocator memory by at least 5% relative to the best random/early-layer baseline on two model shapes while preserving gradient equivalence.
- Stop condition: Stop if the selector ties or loses to random/early-layer baselines within measurement noise on two shapes, or if the required confirmation becomes a CPU-only or more-than-15-minute GB10 loop without stronger preliminary GPU evidence.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-checkpointing-with-layer-importance-ranking-for-gb10-vram-reduction-7936ee932f98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
