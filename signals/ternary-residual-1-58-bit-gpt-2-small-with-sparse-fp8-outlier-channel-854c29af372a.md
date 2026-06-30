# Ternary+Residual: 1.58-bit GPT-2-small with sparse FP8 outlier channel

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `ternary-residual-1-58-bit-gpt-2-small-with-sparse-fp8-outlier-channel-854c29af372a`
Run ID: `ternary-residual-1-58-bit-gpt-2-small-with-sparse-fp8-outlier-channel-854c29af372a-20260614T034702682955+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/8afe4dd041f4

## What looked useful

On 49 real GPT-2-small 2D tensors, sparse FP8 residuals reduced ternary reconstruction MSE by 26.14% at 1% residual density. Across three toy GPT-style training seeds, ternary+1% sparse FP8 residual improved final validation loss by 0.00363 vs ternary-only, recovering about 14.96% of the ternary-vs-dense loss gap.

## Boundaries and scale limits

No full GPT-2-small training or fine-tuning was performed; the language task was synthetic; the residual path simulated FP8 storage but did not use a production sparse FP8 compute kernel or measure real memory-bandwidth gains.

## Claim scope

A sparse FP8 residual/outlier channel can recover a small but reproducible fraction of ternary weight degradation in a bounded proxy: GPT-2-small weight reconstruction plus 834k-parameter GPT-style synthetic language-model training.

## Why it stopped

Proxy-only useful signal; not a full validation of GPT-2-small accuracy, sparse FP8 kernel efficiency, or large-corpus training behavior.

## Recommended next action

Run a bounded real-corpus GPT-2-small-class follow-up with matched dense, ternary-only, and ternary+residual controls before considering paper work.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-corpus GPT-2-small-class ternary residual confirmation
- Success threshold: Ternary+residual recovers at least 10% of the ternary-vs-dense validation-loss gap at no more than 1% residual density without unstable training.
- Stop condition: Stop if the residual channel recovers less than 5% of the ternary-vs-dense validation-loss gap across matched real-corpus runs or requires density above 2% to show a consistent effect.

## Evidence references

- Artifact root: `<local-path>/projects/ternary-residual-1-58-bit-gpt-2-small-with-sparse-fp8-outlier-channel-854c29af372a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
