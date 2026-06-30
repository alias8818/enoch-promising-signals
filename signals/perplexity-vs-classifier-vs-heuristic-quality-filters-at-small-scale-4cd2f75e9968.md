# Perplexity vs classifier vs heuristic quality filters at small scale

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `perplexity-vs-classifier-vs-heuristic-quality-filters-at-small-scale-4cd2f75e9968`
Run ID: `perplexity-vs-classifier-vs-heuristic-quality-filters-at-small-scale-4cd2f75e9968-20260619T204559775078+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b904a67997da

## What looked useful

Tiny learned/perplexity quality filters can suffer severe threshold calibration collapse at small scale, rejecting nearly all held-out good examples, while transparent heuristics retained mean held-out F1 0.7971 and recall 0.9538 on this proxy.

## Boundaries and scale limits

Synthetic small-data proxy only; no real production labels, no human moderation benchmark, no long-form factuality task, no external validation, and no strong pretrained classifier baseline.

## Claim scope

On a deterministic 64-item synthetic text-quality corpus with five seeded train/test splits and train-selected thresholds, transparent surface heuristics were more usable than a char-4 high-quality language-model perplexity filter or a word/character n-gram Naive Bayes classifier.

## Why it stopped

Synthetic early probe produced useful but insufficient evidence; it is not direct production validation or paper-ready evidence.

## Recommended next action

Stop as no-paper useful signal; a next bounded test should use real labeled moderation or answer-quality data with a validation split for calibration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-label calibration test for small quality filters
- Success threshold: Classifier improves held-out F1 by at least 0.10 over heuristics while maintaining recall at or above 0.90 and avoiding all-accept or all-reject calibration collapse.
- Stop condition: Stop if the classifier cannot beat heuristics by 0.05 held-out F1 after calibration, or if real labels are unavailable.

## Evidence references

- Artifact root: `<local-path>/projects/perplexity-vs-classifier-vs-heuristic-quality-filters-at-small-scale-4cd2f75e9968`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
