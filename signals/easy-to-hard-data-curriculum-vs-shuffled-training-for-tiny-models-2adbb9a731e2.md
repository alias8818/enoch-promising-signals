# Easy-to-hard data curriculum vs shuffled training for tiny models

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `easy-to-hard-data-curriculum-vs-shuffled-training-for-tiny-models-2adbb9a731e2`
Run ID: `easy-to-hard-data-curriculum-vs-shuffled-training-for-tiny-models-2adbb9a731e2-20260611T211824496247+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/65828253bdb7

## What looked useful

Shuffled training reached higher accuracy throughout most checkpoints, especially on hard examples; easy-to-hard caught up by the final checkpoint but final paired deltas were tiny: overall +0.00025 accuracy and hard-quartile +0.0030 for curriculum over shuffled across 8 seeds.

## Boundaries and scale limits

Synthetic binary classification only; no transformer, no token-level language modeling, no natural data curriculum, no large model scale, and only 2500 steps per schedule. Results are a bounded proxy, not full validation of curriculum learning for language models.

## Claim scope

In an 8-seed tiny 610-parameter NumPy MLP teacher-student classification probe where difficulty is teacher margin, a simple easy-to-hard training-pool schedule did not reliably outperform equal-compute shuffled sampling; it lagged during most of training and ended with effectively zero overall final-accuracy gain.

## Why it stopped

Bounded proxy evidence does not support the hypothesis that simple easy-to-hard curriculum is better than shuffled training for tiny models; this is an early scoped falsification, not a full large-scale validation.

## Recommended next action

Stop this run as no-paper useful evidence; the concrete next bounded test is a tiny transformer/token-level LM curriculum comparison that reports both learning-curve AUC and final validation loss under matched token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Tiny transformer token-level curriculum versus shuffled matched-token training
- Success threshold: Curriculum beats shuffled by at least 1% relative validation loss or perplexity at final budget and improves learning-curve AUC in at least 4 of 5 paired seeds without degrading hard-bin diagnostics.
- Stop condition: Stop if curriculum fails to beat shuffled on both final validation loss and learning-curve AUC after the matched-token paired-seed run, or if variance makes the effect smaller than the predeclared 1% threshold.

## Evidence references

- Artifact root: `<local-path>/projects/easy-to-hard-data-curriculum-vs-shuffled-training-for-tiny-models-2adbb9a731e2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
