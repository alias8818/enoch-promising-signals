# 4-bit AdamW with error feedback vs 8-bit baseline

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `4-bit-adamw-with-error-feedback-vs-8-bit-baseline-e27d90367830`
Run ID: `4-bit-adamw-with-error-feedback-vs-8-bit-baseline-e27d90367830-20260630T182643511232+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/4acaf9c51607

## What looked useful

8-bit quantized AdamW stayed close to fp32 AdamW at about 2.04 optimizer bytes/parameter. 4-bit without EF used about 1.04 bytes/parameter but had materially worse eval loss. 4-bit with persistent fp32/fp16 residual EF failed with NaNs in the calibrated run and used about 9.04/5.04 bytes per parameter, exceeding the 8-bit baseline.

## Boundaries and scale limits

Tiny synthetic language-model task, 240 optimizer steps, 3 seeds on one GB10; not a GPT-2-small/full-corpus/pretraining-scale validation and not a production fused-kernel benchmark.

## Claim scope

Bounded small-transformer CUDA proxy: persistent-residual 4-bit AdamW error feedback for first and second moments did not beat an 8-bit AdamW baseline when residual buffers were included in optimizer-state memory accounting.

## Why it stopped

Early bounded proxy falsification: the tested persistent-residual 4-bit EF variants were unstable and lost the optimizer-state memory advantage versus 8-bit once residual buffers were counted.

## Recommended next action

Stop pursuing persistent full-residual 4-bit AdamW EF as a memory-saving 8-bit replacement; only branch if testing a compressed-residual or update-level EF design with total optimizer state below the 8-bit baseline.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Compressed-residual 4-bit AdamW error feedback under an 8-bit state budget
- Success threshold: Total optimizer state below 2.04 bytes/parameter and three-seed mean eval loss within 2 percent of 8-bit AdamW on the calibrated proxy without NaNs.
- Stop condition: Stop if residual compression pushes total state above 8-bit, causes smoke-test instability, or calibrated eval loss is more than 10 percent worse than 8-bit.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-adamw-with-error-feedback-vs-8-bit-baseline-e27d90367830`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
