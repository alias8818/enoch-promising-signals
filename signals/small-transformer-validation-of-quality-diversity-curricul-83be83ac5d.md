# Small-transformer validation of quality-diversity curriculum selection on real corpus shards

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `small-transformer-validation-of-quality-diversity-curricul-83be83ac5d`
Run ID: `small-transformer-validation-of-quality-diversity-curricul-83be83ac5d-20260628T012538782303+0000`

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

- Parent run decision: Curriculum data selection for tiny CPU pretraining of GPT-2-small class: enoch://control-plane/projects/curriculum-data-selection-for-tiny-cpu-pretraining-of-gpt-2-small-class-9839903b3584/runs/curriculum-data-selection-for-tiny-cpu-pretraining-of-gpt-2-small-class-9839903b3584-20260622T012514534673+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f2f77c424514

## What looked useful

Quality-diversity shard selection did not satisfy the strict threshold: mean final validation loss was 2.7603 versus 2.7661 for quality-only and 2.7417 for random. QD improved over quality-only by only 0.0057 nats and was 0.0186 nats worse than random. All strategies selected a mean of 4.0 diversity bins, indicating weak mechanism separation in this setup.

## Boundaries and scale limits

Single public corpus, character-level model, two seeds, short training horizon, cheap quality proxy, and four occupied diversity bins. Not a GPT-2-small-class or multi-corpus validation.

## Claim scope

A Tier 1 small direct test on Tiny Shakespeare real text shards with a 37,745-parameter character-level causal transformer, two seeds, and 60 equal-budget updates per run.

## Why it stopped

The direct small real-corpus test missed the stated 0.02-nat improvement threshold and lost to the random control, so the tested QD curriculum is not validated.

## Recommended next action

Stop this run as no-paper useful evidence; if continuing, first run a bounded mechanism follow-up with finer diversity features and a tighter shard budget that demonstrably increases QD coverage before any larger training.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Mechanism-isolating QD curriculum test with finer diversity bins and tighter shard budget
- Success threshold: QD must beat both quality-only and random by at least 0.02 nats mean final validation loss and show at least 2x occupied-bin coverage versus quality-only.
- Stop condition: Stop if QD does not create a measurable diversity-coverage advantage before training, or if it creates coverage but fails to beat both controls by 0.02 nats over at least three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-validation-of-quality-diversity-curricul-83be83ac5d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
