# Data-Selection Pretraining: Quality-Filter Subset vs Full Corpus at Fixed Budget

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `data-selection-pretraining-quality-filter-subset-vs-full-corpus-at-fixed-budget-8f391d913159`
Run ID: `data-selection-pretraining-quality-filter-subset-vs-full-corpus-at-fixed-budget-8f391d913159-20260630T045109240336+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/258725c218cc

## What looked useful

Quality_top50 reduced clean validation loss by 0.354 vs full_corpus with paired approx 95% CI [-0.363, -0.345]; quality_top25 reduced it by 0.388 with CI [-0.395, -0.381]. Random_top50 matched full_corpus, indicating the gain came from quality-correlated selection. Quality filtering worsened mixed-distribution loss, so the benefit is target-distribution dependent.

## Boundaries and scale limits

Tiny Transformer, synthetic corpus, 5 seeds, 1.43M train tokens per policy/seed; no real web corpus, no real quality classifier, no GPT-2-small-class or larger model, and no downstream benchmark transfer.

## Claim scope

In a controlled synthetic autoregressive pretraining proxy with document-level clean/noisy mixtures and imperfect quality scores, quality-filtered subsets improved clean held-out next-token loss over full-corpus and random-subset controls at the same training-token budget.

## Why it stopped

No-paper closure: the positive result is a synthetic proxy useful signal, not direct real-corpus or publication-grade evidence.

## Recommended next action

Run a bounded real-corpus small-LM confirmation using the same fixed-budget full-vs-quality-vs-random design and separate clean-target from mixed-distribution evaluation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus fixed-budget confirmation of quality-filtered pretraining subsets
- Success threshold: Quality-filtered policy improves clean-target validation loss by at least 3% relative to full_corpus and random-subset controls without an unreported or dominant degradation on the declared target metric.
- Stop condition: Stop if quality filtering fails to beat both full_corpus and random-subset controls on clean-target validation under matched budget, or if setup cannot provide a reproducible quality score.

## Evidence references

- Artifact root: `<local-path>/projects/data-selection-pretraining-quality-filter-subset-vs-full-corpus-at-fixed-budget-8f391d913159`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
