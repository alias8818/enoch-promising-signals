# Medium real-text validation of INT8 fake-quantized transformer training with per-channel smoothing

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `medium-real-text-validation-of-int8-fake-quantized-transfo-723f5f9f7e`
Run ID: `medium-real-text-validation-of-int8-fake-quantized-transfo-723f5f9f7e-20260609T182403555001+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: INT8 quantized training with per-channel smoothing: enoch://control-plane/projects/int8-quantized-training-with-per-channel-smoothing-4993d2442ea2/runs/int8-quantized-training-with-per-channel-smoothing-4993d2442ea2-20260609T081940735847+0000
- Parent run decision: Bounded transformer validation of INT8 fake-quantized training with per-channel smoothing: enoch://control-plane/projects/bounded-transformer-validation-of-int8-fake-quantized-trai-0183d2a5fc/runs/bounded-transformer-validation-of-int8-fake-quantized-trai-0183d2a5fc-20260609T131611911056+0000

## What looked useful

Plain INT8 fake-quantized training matched the unquantized baseline within +0.0007 mean validation loss across three seeds, while the per-channel smoothing variant was worse by +0.0115 mean validation loss at step 800 and showed reproducible SIGTERM fragility under frequent-evaluation runs after step 500.

## Boundaries and scale limits

This is medium local evidence, not publication-grade full-scale validation: character tokenizer, about 2M cached text characters, 800 steps, one compact GPT-style model size, one smoothing alpha, simulated fake quantization rather than real INT8 kernels, and no GPT-2-small/subword/downstream benchmark.

## Claim scope

On cached WikiText-2 real text with a 6-layer 384-wide character GPT, 800 training steps, fixed seeds 1-3, and fake-quantized linear layers, SmoothQuant-style per-input-channel smoothing did not improve INT8 fake-quantized training versus a no-smoothing INT8 control or an unquantized baseline.

## Why it stopped

Tier-2 direct target metrics with fixed seeds, a real baseline, and an ablation/control did not support the per-channel smoothing hypothesis; further work would be a new hyperparameter or scale study rather than closure for this run.

## Recommended next action

Stop this follow-up as a no-paper negative for the smoothing mechanism; retain results/medium_summary.json and run_notes.md as evidence that no-smoothing INT8 is the stronger local baseline.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/medium-real-text-validation-of-int8-fake-quantized-transfo-723f5f9f7e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
