# 4-bit Lion Optimizer State for Memory-Cheap CPU Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `4-bit-lion-optimizer-state-for-memory-cheap-cpu-training-55272d610bde`
Run ID: `4-bit-lion-optimizer-state-for-memory-cheap-cpu-training-55272d610bde-20260604T080405174692+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/0efddd0f401e

## What looked useful

The memory mechanism works as expected: medium-run 4-bit Lion used 0.1376 MiB optimizer state versus 1.0665 MiB for FP32 Lion and 2.1329 MiB for AdamW. However, it ended at validation loss 1.5263 and accuracy 0.5845 versus FP32 Lion loss 1.2317 and accuracy 0.6227, and ran 1.68x slower than FP32 Lion in the NumPy implementation.

## Boundaries and scale limits

Only synthetic MLP CPU training was tested. No transformer, language-model corpus, multiple-seed robustness, memory-pressure scaling, or fused production optimizer implementation was tested.

## Claim scope

In a bounded NumPy CPU MLP classification benchmark, packed blockwise 4-bit Lion momentum reduced optimizer-state bytes by about 7.7x versus FP32 Lion, but showed materially worse medium-run validation loss/accuracy and higher runtime than FP32 Lion.

## Why it stopped

Bounded CPU proxy, not full validation, found the intended optimizer-state compression but also a medium-run convergence gap and runtime overhead relative to FP32 Lion.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded action is to test whether stochastic rounding or error-feedback 4-bit Lion removes the observed quality gap on the same benchmark before attempting larger language-model validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Error-feedback 4-bit Lion momentum on bounded CPU training
- Success threshold: Across three seeds, best 4-bit variant has final validation loss within 5% of FP32 Lion, accuracy within 1 percentage point of FP32 Lion, at least 6x lower optimizer-state bytes, and no more than 25% runtime overhead in an optimized or vectorized implementation.
- Stop condition: Stop if all 4-bit variants remain more than 5% worse in validation loss or more than 1 percentage point worse in accuracy than FP32 Lion on the medium benchmark, or if the implementation cannot keep at least 6x state-memory reduction.

## Evidence references

- Artifact root: `<local-path>/projects/4-bit-lion-optimizer-state-for-memory-cheap-cpu-training-55272d610bde`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
