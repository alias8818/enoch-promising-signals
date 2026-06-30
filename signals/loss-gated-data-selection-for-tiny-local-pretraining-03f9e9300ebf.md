# Loss-gated data selection for tiny local pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `loss-gated-data-selection-for-tiny-local-pretraining-03f9e9300ebf`
Run ID: `loss-gated-data-selection-for-tiny-local-pretraining-03f9e9300ebf-20260607T054909075615+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/2b828dab0d6c

## What looked useful

Random selection beat low-loss, middle-loss, and high-loss probe-based selection on all 10 seeds. The middle-loss gate was +0.00679 validation loss worse than random on average; high-loss was +0.00637 worse; low-loss was +0.04798 worse.

## Boundaries and scale limits

This does not test tokenizer-level GPT-2-small-class pretraining, larger corpora, longer training horizons, downstream transfer, adaptive loss gates, or diversity-preserving loss gates.

## Claim scope

In a 10-seed WikiText-2 character-level tiny causal-Transformer proxy with fixed candidate scoring, fixed token/update budget, and held-out next-character validation loss, a static 35th-65th percentile probe-loss gate did not improve tiny local pretraining over random selection.

## Why it stopped

Early proxy falsification rather than full validation: the directly tested static middle-loss gate consistently underperformed random selection on real-text tiny-LM pretraining.

## Recommended next action

Stop this static middle-loss-gate variant; only pursue a bounded deepen follow-up if it adds adaptive gating or explicit diversity preservation and compares against random at equal token budget.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive diversity-preserving loss gates for tiny tokenized LM pretraining
- Success threshold: Adaptive diversity-preserving loss gate improves mean held-out perplexity by at least 2 percent versus random with no worse than 4 wins out of 5 seeds and no material diversity collapse.
- Stop condition: Stop if adaptive or diversity-preserving gates fail to beat random on at least 4 of 5 seeds or if selected-data diversity falls below 80 percent of the random baseline.

## Evidence references

- Artifact root: `<local-path>/projects/loss-gated-data-selection-for-tiny-local-pretraining-03f9e9300ebf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
