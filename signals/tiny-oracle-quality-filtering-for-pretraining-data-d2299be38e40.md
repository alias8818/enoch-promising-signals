# Tiny-Oracle Quality Filtering for Pretraining Data

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-oracle-quality-filtering-for-pretraining-data-d2299be38e40`
Run ID: `tiny-oracle-quality-filtering-for-pretraining-data-d2299be38e40-20260619T152241908912+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/fc6676296d4e

## What looked useful

Within the synthetic setup, oracle_top mean clean validation loss was 2.8909 versus random 3.7330, shuffled_oracle_top 3.7243, unfiltered_same_budget 3.7686, and anti_oracle 4.3699. The oracle reduced clean validation loss by 0.8421 versus random and 0.8334 versus shuffled-label oracle, meeting the predeclared threshold.

## Boundaries and scale limits

Synthetic generator, highly separable quality labels, tiny GRU LM, 1200 generated documents per seed, 5 training epochs, and clean-distribution validation only. No real corpus, large Transformer, downstream task, tokenizer, deduplication, or web-scale validation was tested.

## Claim scope

Synthetic mechanism test: a tiny MLP quality oracle trained on 120 labeled clean/noisy probe documents selected a 360-document pretraining subset that improved a tiny GRU language model's held-out clean validation loss over random, same-budget unfiltered, anti-oracle, and shuffled-label oracle controls across five seeds.

## Why it stopped

No-paper useful signal: the hypothesis is supported only in a synthetic toy setting, so this is not direct publication-grade evidence for real pretraining data filtering.

## Recommended next action

Run a bounded real-corpus follow-up using externally defined quality labels or proxy labels, standard heuristic baselines, and a small Transformer LM with equal token budgets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus tiny-oracle filtering against heuristic baselines
- Success threshold: Learned oracle selection improves mean held-out clean validation loss by at least 3% versus the best heuristic baseline across at least three seeds, without degrading the downstream/diagnostic probe.
- Stop condition: Stop as negative if the learned oracle does not beat the best heuristic baseline by 3% mean validation-loss reduction or if gains disappear under shuffled-label/feature ablation controls.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-oracle-quality-filtering-for-pretraining-data-d2299be38e40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
