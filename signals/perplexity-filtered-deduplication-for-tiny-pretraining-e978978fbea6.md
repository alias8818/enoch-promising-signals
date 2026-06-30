# Perplexity-Filtered Deduplication for Tiny Pretraining

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `perplexity-filtered-deduplication-for-tiny-pretraining-e978978fbea6`
Run ID: `perplexity-filtered-deduplication-for-tiny-pretraining-e978978fbea6-20260604T200315847733+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/fd0adc3b10ec

## What looked useful

Across 4 seeds, perplexity-filtered dedup selected clean exemplars for 100% of clusters versus 17.78% for arbitrary first dedup, and reduced mean held-out clean validation perplexity to 2.5599 from 3.0503 for first dedup and 3.1441 for raw duplicate/noisy training.

## Boundaries and scale limits

Synthetic corpus only; exact cluster membership is known; reference character model is trained on the same synthetic grammar family; tiny 2-layer Transformer only; no real web corpus, real near-duplicate detection, pretrained reference LM, downstream task evaluation, or long pretraining run.

## Claim scope

In a controlled synthetic tiny-pretraining proxy where each near-duplicate cluster contains one clean factual record and five noisy/corrupt variants, selecting the lowest-reference-perplexity exemplar per cluster improved held-out clean synthetic validation perplexity versus raw duplicates and arbitrary first-exemplar deduplication.

## Why it stopped

No paper-ready result: this is a controlled synthetic proxy supporting the mechanism, not a real tiny-pretraining validation.

## Recommended next action

Run a bounded real-corpus confirmation on actual near-duplicate clusters before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus confirmation for perplexity-filtered deduplication in tiny pretraining
- Success threshold: Perplexity-filtered dedup achieves at least 5% lower mean held-out real-text perplexity than arbitrary dedup across at least 3 seeds without increasing memorization diagnostics.
- Stop condition: Stop if real-corpus cluster selection does not improve clean/quality proxies or if held-out perplexity improvement is under 2% versus arbitrary dedup across seeds.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-filtered-deduplication-for-tiny-pretraining-e978978fbea6`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
