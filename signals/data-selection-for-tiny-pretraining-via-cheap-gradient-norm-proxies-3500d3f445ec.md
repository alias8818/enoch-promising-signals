# Data selection for tiny pretraining via cheap gradient-norm proxies

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `data-selection-for-tiny-pretraining-via-cheap-gradient-norm-proxies-3500d3f445ec`
Run ID: `data-selection-for-tiny-pretraining-via-cheap-gradient-norm-proxies-3500d3f445ec-20260628T013522183742+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/d9ddc8cc00d2

## What looked useful

Across seeds 7, 11, 19, and 23, cheap_bigram_bottom improved mean validation NLL by 0.01771 versus random and selected 100% target examples, while cheap_bigram_top worsened NLL by 0.01618 and selected 0% target examples. Cheap proxy scores were negatively correlated with true calibrated bigram gradient norms, showing useful target information but inverted ordering semantics.

## Boundaries and scale limits

Synthetic Markov/noise data, 64-token vocabulary, 4096-example pools, 512-example selection budgets, bigram model only, four seeds; no transformer, real text corpus, downstream transfer, or large-scale pretraining validation.

## Claim scope

On a synthetic tiny-token pretraining benchmark with a trainable bigram LM, cheap count-model gradient residual proxies improved target validation NLL when used as low-score target-likeness selectors; naive top-gradient selection was harmful.

## Why it stopped

No-paper closure: this is a reproducible synthetic/tiny useful signal and directionality warning, not direct evidence for real pretraining.

## Recommended next action

Run a bounded real-text small-transformer follow-up that compares low-score and high-score cheap proxy selection against random, target-filter, and true-gradient controls at fixed token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-text small-transformer check for cheap gradient proxy directionality
- Success threshold: Low-score cheap proxy selection improves held-out target validation NLL or perplexity by at least 1% over random in at least two of three seeds and does not lose to a target-filter baseline by more than 0.5%.
- Stop condition: Stop as a negative if low-score cheap proxy selection fails to beat random in at least two of three seeds or if high-score and low-score directions are indistinguishable within run-to-run noise.

## Evidence references

- Artifact root: `<local-path>/projects/data-selection-for-tiny-pretraining-via-cheap-gradient-norm-proxies-3500d3f445ec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
