# Embedded Shard Watermarks for Free-Rider Detection in Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `embedded-shard-watermarks-for-free-rider-detection-in-volunteer-training-ee5a014a1d89`
Run ID: `embedded-shard-watermarks-for-free-rider-detection-in-volunteer-training-ee5a014a1d89-20260620T003112160616+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/bbf53c67e335

## What looked useful

The mechanism worked reliably in the bounded local proxy: 100% thresholded detection at dilution ratios 0, 1, 3, 7, and 15; 0/20 clean-only controls exceeded the trigger-margin threshold; clean accuracy was approximately 1.0.

## Boundaries and scale limits

Synthetic bag-of-token classifiers only; no generative LLM training, real volunteer corpus, adaptive evasion, watermark removal, paraphrase attack, model merging, privacy analysis, or multi-node/full-scale validation was tested.

## Claim scope

In a controlled synthetic binary text-classification task, 12%-rate shard-specific trigger-token watermarks allowed black-box identification of the source training shard across 800 suspect-model trials and five clean-data dilution ratios without measurable clean-accuracy loss.

## Why it stopped

Closed as no-paper useful signal because the local evidence is synthetic/proxy evidence, not direct validation of volunteer LLM training.

## Recommended next action

Run a bounded direct follow-up that fine-tunes a GPT-2-small-class model on realistic text shards with embedded watermarks, clean controls, paraphrase/removal attacks, and model-merging dilution before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: GPT-2-small shard watermark survival under realistic fine-tuning and evasion controls
- Success threshold: At least 90% correct source-shard detection with false-positive rate at or below 5% and no more than 2% relative degradation in held-out utility across at least 5 seeds and 4 shards.
- Stop condition: Stop early if clean-control false positives exceed 10%, held-out utility degrades by more than 5%, or detection falls below 70% after clean dilution of 3:1.

## Evidence references

- Artifact root: `<local-path>/projects/embedded-shard-watermarks-for-free-rider-detection-in-volunteer-training-ee5a014a1d89`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
