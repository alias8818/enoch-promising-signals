# Gradient coreset selection for tiny pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-coreset-selection-for-tiny-pretraining-0e9b2f01f7c3`
Run ID: `gradient-coreset-selection-for-tiny-pretraining-0e9b2f01f7c3-20260604T171332001346+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/b57543c984e7

## What looked useful

Gradient-norm top selection beat random in 5/5 seeds with mean validation loss delta -0.3147, while gradient-norm plus oracle diversity achieved -0.4114. However, oracle balanced-random also achieved -0.2888, so much of the gain appears to come from correcting domain coverage rather than a uniquely gradient-specific coreset effect. Loss-top selection was consistently worse than random, with mean delta +0.2463.

## Boundaries and scale limits

Synthetic corpus only, 2,048-example selection pool, 256-example subset, 1,024-example validation set, tiny 2-layer transformer, 500 downstream training steps, and no real tokenizer or web-scale corpus. The strongest diverse variant used oracle synthetic domain labels.

## Claim scope

On a five-seed synthetic mixed-domain tiny causal language modeling benchmark, gradient-norm subset selection from a warm probe model improved validation loss over pool-proportional random selection at the same subset and training budget.

## Why it stopped

Closed as no-paper useful signal because evidence is synthetic and the main gain is partly explained by domain balancing; this is not a full validation of gradient coreset selection for real tiny pretraining.

## Recommended next action

Run a bounded real-corpus follow-up using label-free gradient diversity or clustering and compare against random, loss-top, and diversity/stratified controls under equal token and scoring-cost budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Label-free gradient diversity selection on a real tiny pretraining corpus
- Success threshold: Gradient-diverse selection must beat random and the non-gradient diversity control by at least 0.05 validation cross-entropy in at least 4 of 5 seeds without scoring cost dominating the saved training budget.
- Stop condition: Stop if gradient-diverse does not beat the non-gradient diversity control in at least 3 of 5 seeds, or if per-example gradient scoring costs more wall-clock than training the saved tokens in the bounded setup.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-coreset-selection-for-tiny-pretraining-0e9b2f01f7c3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
