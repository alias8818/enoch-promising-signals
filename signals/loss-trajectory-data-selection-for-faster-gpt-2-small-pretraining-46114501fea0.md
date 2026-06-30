# Loss-Trajectory Data Selection for Faster GPT-2 Small Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `loss-trajectory-data-selection-for-faster-gpt-2-small-pretraining-46114501fea0`
Run ID: `loss-trajectory-data-selection-for-faster-gpt-2-small-pretraining-46114501fea0-20260531T113843432705+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4d4231f33a1c

## What looked useful

Loss-trajectory scores filtered irreducible noise, but aggressive progress ranking over-selected easy examples and under-selected medium clean examples; random subset and all-data baselines achieved lower mean clean validation loss at both 50% and 70% keep rates.

## Boundaries and scale limits

Synthetic corpus, small GPT-style model, 3 medium seeds, 240 training steps per policy, and short probe trajectories; not a GPT-2-small real-corpus validation.

## Claim scope

In a small synthetic decoder-only Transformer pretraining proxy, naive top-learning-progress loss-trajectory data selection reduced noisy examples but did not improve fixed-budget clean validation loss versus random subset or all-data baselines.

## Why it stopped

Medium proxy confirmation falsified the tested naive top-progress policy: despite reducing selected noise from about 30% to 12-20%, it was worse than random subset by 0.166-0.196 mean final validation loss.

## Recommended next action

Stop this naive trajectory-selection line as no-paper evidence; a bounded follow-up should test diversity-constrained trajectory filtering before any larger GPT-2-small run.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-Constrained Loss-Trajectory Filtering
- Success threshold: At 70% or lower keep rate, diversity-constrained trajectory selection must beat random subset mean final validation loss by at least 0.05 nats and reach random final loss earlier in at least 4/5 seeds while preserving medium-example coverage within 5 percentage points of random.
- Stop condition: Stop if constrained selection still fails to beat random subset mean final validation loss or if improvements disappear when per-kind validation is separated.

## Evidence references

- Artifact root: `<local-path>/projects/loss-trajectory-data-selection-for-faster-gpt-2-small-pretraining-46114501fea0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
