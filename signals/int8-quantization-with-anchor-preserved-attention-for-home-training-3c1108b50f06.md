# INT8 Quantization with Anchor-Preserved Attention for Home Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `int8-quantization-with-anchor-preserved-attention-for-home-training-3c1108b50f06`
Run ID: `int8-quantization-with-anchor-preserved-attention-for-home-training-3c1108b50f06-20260608T063655249948+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/169ffbf25cd5

## What looked useful

Anchor-preserved INT8 K/V reduced relative attention-output MSE by 74.46% on average, but all-INT8 K/V was already task-loss neutral: mean all-INT8 loss delta vs FP was +2.03e-7 and mean anchor-preserved loss delta vs FP was +2.80e-7. Anchor preservation added 5.51% estimated K/V memory overhead versus all-INT8 without measurable task-level recovery.

## Boundaries and scale limits

Five seeds, 240 training steps per seed, tiny 2-layer 128-dim transformer, synthetic data only, simulated quantize/dequantize numerics rather than production INT8 kernels, no real language corpus, no GPT-2-small-class baseline, no optimizer-state quantization, and no wall-clock speed or true memory-residency validation.

## Claim scope

Tiny synthetic anchor-dependent causal-transformer probe with simulated per-token INT8 K/V attention: preserving 8 anchor positions reduced internal attention-output relative MSE but did not improve held-out loss or token accuracy versus all-INT8.

## Why it stopped

No-paper useful signal: the mechanism reduced internal quantization error, but the direct task metric showed no benefit because per-token INT8 K/V was already effectively lossless in the tested setting.

## Recommended next action

Stop this as a paper claim; only run a bounded follow-up if it makes quantization materially harmful first, then tests whether anchor preservation recovers task loss rather than only internal MSE.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harder Quantization Regime for Anchor-Preserved Attention
- Success threshold: All-quantized K/V loss delta vs FP >= 0.02 and anchor-preserved K/V reduces that delta by >=25% with <=65% FP K/V memory.
- Stop condition: Stop if all-quantized K/V remains loss-neutral after harder settings, or if anchor preservation improves internal MSE but recovers less than 10% of the task-loss gap.

## Evidence references

- Artifact root: `<local-path>/projects/int8-quantization-with-anchor-preserved-attention-for-home-training-3c1108b50f06`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
