# Easy-Example Removal for Tiny Model Data Pruning

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `easy-example-removal-for-tiny-model-data-pruning-8da252115607`
Run ID: `easy-example-removal-for-tiny-model-data-pruning-8da252115607-20260525T001909689356+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a7fbc702656d

## What looked useful

Easy-example removal was conditionally useful on clean small datasets, especially at 50% pruning, but failed badly on a 10% label-noise synthetic dataset. Across 8 dataset/fraction cells, remove-easy beat random in 4 cells and had mean accuracy delta versus random of -0.0198, while generally beating hard-example removal on clean data.

## Boundaries and scale limits

Not a language-model pretraining result; no GPT-2-small-class baseline, no token-level corpus, no large dataset, and no long training run. Synthetic label-noise behavior may not fully match real web-scale data noise.

## Claim scope

Bounded CPU probe of easy-example removal for tiny supervised classifiers: four small datasets, 8 seeds, 25% and 50% pruning, out-of-fold logistic easiness scoring, and a one-hidden-layer 16-unit MLP target model.

## Why it stopped

No-paper useful signal: the bounded local experiment found mixed evidence and an early falsification of pure easy-example removal under label noise, not a full validation.

## Recommended next action

Run a bounded deepen test with a noise-aware easy-removal rule that filters likely mislabeled/outlier hard examples before pruning easy examples.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Noise-Aware Easy-Example Removal for Tiny Model Data Pruning
- Success threshold: Noise-aware easy-removal must beat random pruning in at least 6 of 8 current dataset/fraction cells and avoid more than 1 percentage point degradation versus random on the synthetic 10% label-noise 50% pruning cell.
- Stop condition: Stop if the noise-aware variant still underperforms random on the noisy 50% pruning cell by more than 1 percentage point or fails to beat random in a majority of clean dataset/fraction cells.

## Evidence references

- Artifact root: `<local-path>/projects/easy-example-removal-for-tiny-model-data-pruning-8da252115607`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
