# Neural Chunk-Commitment Gradient Validation Under Adaptive Lazy Workers

Status: `useful_signal`
Project ID: `neural-chunk-commitment-gradient-validation-under-adaptive-735638b6db`
Run ID: `neural-chunk-commitment-gradient-validation-under-adaptive-735638b6db-20260518T073144311066+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/87ce680fc6cc

## What looked useful

Adaptive fastest-k selection produced lower-loss selected chunks, mean projection ratio 0.474 versus 1.000 all-sync, and -1.29 percentage point final accuracy delta. Random and neural committed HT stayed near all-sync projection and accuracy; neural commitment did not materially beat random commitment.

## Boundaries and scale limits

Small classifier, synthetic latency model, 5 seeds, 180 steps, 16 chunks and 6 committed samples per batch; no real distributed cluster, no transformer/GPT-2-small-class model, and no large-corpus language-model validation.

## Claim scope

In a small PyTorch MLP on sklearn digits with simulated adaptive lazy workers, accepting fastest workers after latency observation biases gradients when latency is correlated with chunk loss/gradient norm; pre-latency committed HT chunk sampling preserves gradient projection and final accuracy near the exact all-sync control.

## Why it stopped

Tier 1 direct evidence supports the commitment mechanism but is not paper-ready and does not establish a neural scorer advantage over random commitment.

## Recommended next action

Run a medium direct transformer language-modeling follow-up with trace-driven or real straggler timing, comparing all-sync, fastest-k, random committed HT, and neural committed HT on validation loss, gradient projection, throughput, and wall-clock-to-target-loss.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Transformer Validation of Neural Chunk Commitment Under Trace-Driven Lazy Workers
- Success threshold: Neural committed HT must match all-sync/reference gradient projection within 10% relative projection error, beat fastest-k validation loss at matched compute, and improve wall-clock-to-target-loss by at least 10% over random committed HT without worse final validation loss.
- Stop condition: Stop if neural committed HT fails to beat random committed HT by at least 5% wall-clock-to-target-loss in two pilot seeds or shows systematic projection bias greater than random committed HT.

## Evidence references

- Artifact root: `<local-path>/projects/neural-chunk-commitment-gradient-validation-under-adaptive-735638b6db`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
