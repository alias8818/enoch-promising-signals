# Home pretraining of 90M model with 2/4/8-bit residual precision curriculum

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `38`
Project ID: `home-pretraining-of-90m-model-with-2-4-8-bit-residual-precision-curriculum-711fa93922ae`
Run ID: `home-pretraining-of-90m-model-with-2-4-8-bit-residual-precision-curriculum-711fa93922ae-20260619T192632214539+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `38`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 0, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9f3fe48dda52

## What looked useful

Fixed 8-bit residual fake quantization matched full precision within noise, fixed 4-bit incurred a small loss penalty, and schedules involving an initial 2-bit residual phase produced substantially worse final validation loss. Mean final validation loss over three seeds: fp 2.2596, 8-bit 2.2575, 4-bit 2.3142, 2-bit 2.7330, 2->4->8 2.6274.

## Boundaries and scale limits

This does not validate or fully falsify 90M-parameter home pretraining, long-token training, broad-corpus behavior, other curriculum schedules, or hardware-efficient packed low-bit kernels. It is a short proxy/early falsification of this exact low-to-high residual precision schedule.

## Claim scope

In a 3.26M-parameter GPT-style byte-language-model proxy on Tiny Shakespeare, with per-token STE fake quantization applied to residual activations and matched 300-step training budgets over three seeds, an equal-thirds 2->4->8 residual precision curriculum underperformed fixed 4-bit, fixed 8-bit, and full-precision residual training.

## Why it stopped

Proxy/early falsification rather than full validation: the tested 2->4->8 residual precision curriculum consistently lost to fixed 4-bit, fixed 8-bit, and full precision across three short CUDA runs.

## Recommended next action

Stop this exact curriculum as a paper path; if revisiting, first test a bounded adjacent schedule that avoids a long initial 2-bit phase before attempting 90M-scale pretraining.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/home-pretraining-of-90m-model-with-2-4-8-bit-residual-precision-curriculum-711fa93922ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
