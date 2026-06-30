# Micro-Sharded Gradient Accumulation with On-Device Cheating Probes

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `micro-sharded-gradient-accumulation-with-on-device-cheating-probes-a0c0499425fd`
Run ID: `micro-sharded-gradient-accumulation-with-on-device-cheating-probes-a0c0499425fd-20260530T051240898620+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12c22dd7eb68

## What looked useful

Maximum relative gradient difference was 2.08e-07. The synthetic cheating feature was the top probe feature in 100% of unmasked cheating shards, probe-triggered masking flagged in 100% of seeds at step 0, and honest-test accuracy improved from 0.5478 to 0.7678 mean across 10 seeds.

## Boundaries and scale limits

Single-device synthetic tabular task with a linear model, 64 features, 10 seeds, 80 training steps per condition. No transformer, language-model, distributed, long-run, or realistic data-contamination validation was performed.

## Claim scope

In a controlled synthetic binary task on one GB10 GPU, micro-sharded gradient accumulation matched full-batch gradients to floating-point tolerance and enabled shard-local on-device feature-label probes to flag a strong label-leakage feature; probe-triggered masking improved honest-test accuracy across 10 seeds.

## Why it stopped

The result is a bounded synthetic/proxy mechanism test, not direct or full-scale validation of micro-sharded gradient accumulation with cheating probes in model training.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same probe in a small transformer or GPT-2-small-class training loop with a realistic leakage channel and matched standard accumulation baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Transformer-Loop Cheating Probe Validation
- Success threshold: Across at least 5 seeds, probe-triggered intervention improves honest validation by at least 5 relative percentage points or equivalent loss reduction while keeping gradient/loss parity within expected floating-point noise and overhead below 10%.
- Stop condition: Stop if the probe fails to distinguish leakage from clean controls above a calibrated threshold, if intervention does not improve honest validation, or if overhead exceeds 10% in the small transformer loop.

## Evidence references

- Artifact root: `<local-path>/projects/micro-sharded-gradient-accumulation-with-on-device-cheating-probes-a0c0499425fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
