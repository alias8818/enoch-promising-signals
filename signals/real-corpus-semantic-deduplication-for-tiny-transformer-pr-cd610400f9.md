# Real-corpus semantic deduplication for tiny transformer pretraining

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-semantic-deduplication-for-tiny-transformer-pr-cd610400f9`
Run ID: `real-corpus-semantic-deduplication-for-tiny-transformer-pr-cd610400f9-20260602T122310687529+0000`

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

- Parent run decision: Semantic Deduplication Boosts Tiny Corpus Pretraining Efficiency: enoch://control-plane/projects/semantic-deduplication-boosts-tiny-corpus-pretraining-efficiency-4c9b2a310a33/runs/semantic-deduplication-boosts-tiny-corpus-pretraining-efficiency-4c9b2a310a33-20260601T054711934474+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/aa233e0bb664

## What looked useful

At semantic threshold 0.82, semantic dedup failed to beat raw/lexical controls: seed 13 was +0.0869% worse in validation loss and seed 17 was indistinguishable. A stricter 0.65 threshold removed 622 of 1799 lexical-unique docs and improved validation loss by only 0.1217%, far below the 2% success threshold.

## Boundaries and scale limits

WikiText-2 download was blocked, so the preferred LM corpus was not tested. Runs used 60k training tokens, 220 updates per condition, two seeds at threshold 0.82, and one aggressive threshold stress run; no larger model, longer schedule, or embedding-based semantic dedup was evaluated.

## Claim scope

Small direct CPU test on 20 Newsgroups real-corpus tiny causal-transformer pretraining with matched token and update budgets; semantic dedup used TF-IDF plus LSA cosine greedy filtering.

## Why it stopped

Controlled small direct real-corpus test did not meet the >=2% semantic-dedup validation-loss improvement threshold; the only positive result was a sub-threshold aggressive-filter signal.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on an accessible LM corpus with 3 seeds, stream-difference diagnostics, and a pre-registered threshold sweep before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-seed LM-corpus semantic dedup threshold sweep for tiny transformer pretraining
- Success threshold: Semantic dedup beats both raw and lexical controls by >=2% mean validation loss across seeds, with no seed worse than the best control by more than 0.5%.
- Stop condition: Stop if no semantic threshold reaches >=1% mean validation-loss improvement after 3 seeds, or if improvements occur only when the retained corpus collapses below 60% of lexical-unique documents.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-semantic-deduplication-for-tiny-transformer-pr-cd610400f9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
