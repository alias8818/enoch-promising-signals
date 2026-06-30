# Loss-based curriculum data selection for tiny local pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `loss-based-curriculum-data-selection-for-tiny-local-pretraining-108c8fcd560a`
Run ID: `loss-based-curriculum-data-selection-for-tiny-local-pretraining-108c8fcd560a-20260610T081623798068+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b85f706b1f3e

## What looked useful

Pure low-loss, high-loss, and median-loss static subset selection underperformed random on mean validation loss. Low-loss easy selection was consistently worse by +0.0717 validation loss; high-loss hard selection was consistently worse by +0.0151. A half-easy/half-hard selected subset was indistinguishable from random with mean delta -0.00008 and 0.0020 delta standard deviation.

## Boundaries and scale limits

This was a bounded local experiment, not GPT-2-small scale, not tokenizer/subword pretraining, not multi-corpus, not long-horizon training, and not a dynamic re-ranking curriculum. Larger models or dynamic loss-diversity sampling could overturn the result.

## Claim scope

On WikiText-2 byte-level tiny causal LM pretraining with 4,200 train chunks, 35% static selected subsets, 100-step probe scoring, 450 final training steps, and three seeds, static probe-loss subset selection did not improve held-out validation loss over random selection.

## Why it stopped

No-paper useful negative signal: a direct bounded local experiment found no reproducible validation-loss improvement over random selection, but this is not a full-scale falsification.

## Recommended next action

Stop paper work for this static loss-ranking idea; if continuing locally, test a dynamic loss-band sampler that preserves diversity rather than selecting easy-only or hard-only subsets.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Dynamic loss-band sampling for tiny local pretraining
- Success threshold: Dynamic loss-band sampling beats random by at least 0.02 mean validation loss and wins at least 4 of 5 seeds at equal update budget.
- Stop condition: Stop if dynamic sampling fails to beat random by 0.01 mean validation loss after five seeds or if gains appear only in one seed without aggregate improvement.

## Evidence references

- Artifact root: `<local-path>/projects/loss-based-curriculum-data-selection-for-tiny-local-pretraining-108c8fcd560a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
