# Real-data tiny GPT quality-filtered selection check

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `real-data-tiny-gpt-quality-filtered-selection-check-27cb291078`
Run ID: `real-data-tiny-gpt-quality-filtered-selection-check-27cb291078-20260628T040752155036+0000`

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

- Parent run decision: Quality-Filtered Data Selection for Tiny GPT-2 Pretraining: enoch://control-plane/projects/quality-filtered-data-selection-for-tiny-gpt-2-pretraining-667bcc841e05/runs/quality-filtered-data-selection-for-tiny-gpt-2-pretraining-667bcc841e05-20260628T034732256355+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/de30b90b0dd7

## What looked useful

The quality-filtered subset had higher heuristic quality scores but worse high-quality validation loss in all 3 seeds: mean loss 2.484887 filtered versus 2.476777 random, a -0.3274% relative reduction where the pre-registered success threshold required at least +3% and at least 2 of 3 seed wins.

## Boundaries and scale limits

Single dataset family, one simple heuristic, character-level tokenization, tiny model, 300 updates per condition, and 3 seeds; not a GPT-2-small-class, BPE, multi-dataset, or publication-grade validation.

## Claim scope

In a Tier 1 controlled direct test on WikiText-2 using a character-level tiny GPT, equal character budgets, equal optimizer/update budgets, and 3 seeds, a simple paragraph-quality heuristic did not improve high-quality held-out validation loss versus random real-text selection.

## Why it stopped

Controlled small direct real-data test failed the pre-registered threshold: filtered selection won 0 of 3 seeds and was slightly worse on the primary high-quality validation metric.

## Recommended next action

Stop this run as a no-paper early falsification of the simple heuristic; the only warranted next action is a bounded deepen test with a stronger quality scorer and BPE/GPT-2-small-class baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: BPE tiny GPT quality selection with stronger scorer
- Success threshold: Quality-selected training must reduce high-quality validation loss by at least 3% on average versus random and win at least 2 of 3 seeds without degrading broad validation loss by more than 1%.
- Stop condition: Stop if the stronger selector fails the 3%/2-of-3 threshold or if broad validation loss degrades by more than 1% under matched compute.

## Evidence references

- Artifact root: `<local-path>/projects/real-data-tiny-gpt-quality-filtered-selection-check-27cb291078`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
