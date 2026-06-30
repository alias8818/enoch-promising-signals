# Gradient-Norm Data Selection for 10x Faster CPU Pretraining

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `gradient-norm-data-selection-for-10x-faster-cpu-pretraining-079f3515d2dc`
Run ID: `gradient-norm-data-selection-for-10x-faster-cpu-pretraining-079f3515d2dc-20260602T111504403679+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/66e0858ba973

## What looked useful

Gradient-norm selection was slower than uniform in wall-clock efficiency: 0.769x at 2x candidates, 0.401x at 4x, and 0.192x at 8x. Candidate scoring consumed 15.8%, 27.6%, and 54.6% of elapsed time for gradient-norm selection.

## Boundaries and scale limits

Not a transformer or full-scale pretraining validation; tested small character LM, 250 update steps, candidate multipliers 2/4/8, 7 total seeds across sweeps, one real text corpus.

## Claim scope

Bounded CPU proxy on Tiny Shakespeare using a NumPy tiny character language model: gradient-norm top-k data selection did not improve time-to-validation-loss improvement versus uniform random sampling.

## Why it stopped

Proxy early falsification rather than full validation: on the tested CPU LM, gradient-norm selection reduced validation improvement per wall-clock second instead of producing a speedup.

## Recommended next action

Stop this 10x CPU-pretraining claim unless a future direct transformer experiment can show end-to-end time-to-target validation loss beating uniform sampling despite selection overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Direct tiny-transformer CPU time-to-target test for gradient-norm data selection
- Success threshold: Gradient-norm selection must reach the same validation loss at least 1.5x faster wall-clock than uniform sampling on a CPU-only tiny-transformer setup; otherwise stop.
- Stop condition: Stop if gradient-norm selection is not faster than uniform after the first calibrated three-seed tiny-transformer run or if candidate scoring exceeds 25% of elapsed time without compensating loss gains.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-norm-data-selection-for-10x-faster-cpu-pretraining-079f3515d2dc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
