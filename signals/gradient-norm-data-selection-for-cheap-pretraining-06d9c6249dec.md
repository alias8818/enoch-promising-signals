# Gradient-Norm Data Selection for Cheap Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gradient-norm-data-selection-for-cheap-pretraining-06d9c6249dec`
Run ID: `gradient-norm-data-selection-for-cheap-pretraining-06d9c6249dec-20260609T002508312796+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/48099f486882

## What looked useful

Naive gradient-norm selection was consistently worse than random: mean validation loss was 1.6763 for high-gradient, 2.6521 for middle-gradient, and 2.9680 for low-gradient versus 0.5652 for random. The target oracle reached 0.4973, showing useful target examples existed. Diagnostics showed high gradient norms were confounded by distractors, while low gradient/loss selected only easy target-common data and missed rare target structure.

## Boundaries and scale limits

Synthetic corpus, tiny GRU model, five seeds, short local GB10/CUDA run, equal update budget; does not test large transformers, real corpora, tokenizer/document effects, downstream transfer, or datacenter-scale pretraining.

## Claim scope

In a controlled tiny-GRU next-token pretraining probe with mixed target-common, target-rare, distractor, and random-noise candidate sequences, raw per-example gradient-norm ranking after a small target-domain warmup did not improve cheap pretraining data selection over random selection.

## Why it stopped

Proxy/local controlled falsification rather than full-scale validation: all raw gradient-norm selector variants underperformed random across 5 seeds, while an oracle control beat random.

## Recommended next action

Stop this naive selector as no-paper evidence; run one bounded follow-up testing domain-filtered or band-pass gradient norm against random and loss controls on the same mixed corpus plus one small real-text proxy.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Domain-filtered band-pass gradient-norm selection for cheap pretraining
- Success threshold: Filtered/band-pass gradient selection must beat random validation loss by at least 5% on mean over at least 5 seeds and avoid selecting more distractor/noise examples than random.
- Stop condition: Stop if filtered/band-pass gradient selection fails to beat random on the controlled corpus in at least 4 of 5 seeds or if gains vanish on the small real-text proxy.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-data-selection-for-cheap-pretraining-06d9c6249dec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
