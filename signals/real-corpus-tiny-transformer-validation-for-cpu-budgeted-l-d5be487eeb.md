# Real-corpus tiny-transformer validation for CPU-budgeted lexical data selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-corpus-tiny-transformer-validation-for-cpu-budgeted-l-d5be487eeb`
Run ID: `real-corpus-tiny-transformer-validation-for-cpu-budgeted-l-d5be487eeb-20260613T103200640600+0000`

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

- Parent run decision: CPU-Budgeted Data Selection for Tiny Local Pretraining: enoch://control-plane/projects/cpu-budgeted-data-selection-for-tiny-local-pretraining-cf22c401268c/runs/cpu-budgeted-data-selection-for-tiny-local-pretraining-cf22c401268c-20260613T100528273706+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/a19fd55a048f

## What looked useful

Lexical rare-word selection increased mean unique train words from 4114.7 random to 5073.0, but mean validation loss was 3.1915 versus 3.1597 random and 3.1574 contiguous, missing the predeclared 3% improvement threshold.

## Boundaries and scale limits

Single real text corpus, byte tokenizer, 3 seeds, 160 update steps, simple lexical selector, tiny model only; no GPT-2-class, multi-corpus, long-training, or production-scale validation.

## Claim scope

On Tiny Shakespeare with a 2-layer byte-level tiny transformer trained for 160 CPU steps on equal 131072-character subsets, a simple rare-word/diversity lexical chunk selector increased lexical coverage but did not improve held-out validation loss versus random or contiguous controls.

## Why it stopped

Tier 1 direct test produced a no-paper useful negative signal: simple rare-word lexical selection improved coverage but worsened validation loss by about 1.0% versus random and 1.1% versus contiguous.

## Recommended next action

Run one bounded deepen test with a frequency-balanced lexical selector on this corpus plus one additional real corpus, using the same equal-token tiny-transformer controls and requiring validation-loss improvement rather than coverage alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Frequency-balanced lexical selection for CPU-budgeted tiny-transformer training
- Success threshold: Mean held-out validation loss improves by at least 3% versus random and does not underperform contiguous on both corpora, while retaining at least 10% higher unique-word coverage than random.
- Stop condition: Stop as negative if the balanced selector still fails to beat random validation loss by 3% on either corpus or if coverage gains disappear.

## Evidence references

- Artifact root: `<local-path>/projects/real-corpus-tiny-transformer-validation-for-cpu-budgeted-l-d5be487eeb`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
