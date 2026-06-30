# Curriculum ordering vs random for tiny GPT-2-scale pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `curriculum-ordering-vs-random-for-tiny-gpt-2-scale-pretraining-010b801fe41e`
Run ID: `curriculum-ordering-vs-random-for-tiny-gpt-2-scale-pretraining-010b801fe41e-20260630T022908243043+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/1c0250eb2d34

## What looked useful

The simple sorted easy-to-hard curriculum showed a small early optimization advantage but was worse than random at 500 steps in all 3 seeds; mean curriculum-minus-random final validation loss was +0.0400 nats/token, while reverse hard-to-easy was close to random at +0.0073.

## Boundaries and scale limits

This run did not test GPT-2-small parameter count, larger corpora, longer training horizons, production tokenizers, or alternative curricula such as paced sampling, loss-model scoring, bucketed reshuffling, domain curricula, or curriculum-to-random annealing.

## Claim scope

In a local Wikitext-2 pretraining proxy with a 2.59M-parameter GPT-2-like decoder, 8,192 training blocks, 512 validation blocks, 500 optimizer steps, and 3 seeds, unigram-difficulty easy-to-hard curriculum ordering produced higher final held-out next-token loss than random ordering.

## Why it stopped

Bounded direct small-scale evidence consistently falsified the tested simple easy-to-hard unigram curriculum against random ordering; this is not a full-scale validation of all curriculum-learning variants.

## Recommended next action

Stop this project as a no-paper useful negative signal; a separate bounded follow-up should test whether bucketed reshuffling or curriculum-to-random annealing preserves the early curriculum advantage without the later loss penalty.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Bucketed and annealed curricula for tiny GPT-2 pretraining
- Success threshold: A curriculum variant beats random by at least 0.015 nats/token mean final validation loss across 3 seeds, with at least 2 of 3 seed wins and no worse-than-random late-regression pattern.
- Stop condition: Stop if all curriculum variants are at least 0.01 nats/token worse than random at 500 or 1000 steps, or if gains appear only before 200 steps and vanish by final evaluation.

## Evidence references

- Artifact root: `<local-path>/projects/curriculum-ordering-vs-random-for-tiny-gpt-2-scale-pretraining-010b801fe41e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
