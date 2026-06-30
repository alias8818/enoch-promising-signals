# Activation-Aware Calibration Data Selection for INT8 CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `activation-aware-calibration-data-selection-for-int8-cpu-inference-ec4e8faedbb7`
Run ID: `activation-aware-calibration-data-selection-for-int8-cpu-inference-ec4e8faedbb7-20260608T055615197668+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/c21b4dafbe61

## What looked useful

Activation-aware selection improved logit MSE by 42x to 65x over random at budgets 4-16 and gave small accuracy gains over random, but input-norm top selection matched or beat it on most accuracy comparisons.

## Boundaries and scale limits

Synthetic MLP only; no real pretrained transformer/CNN, no production CPU quantization runtime, no real calibration corpus, and no serving latency validation.

## Claim scope

In a controlled NumPy MLP post-training INT8 proxy, activation-aware calibration subsets reduce quantized logit distortion versus random tiny calibration subsets, but do not show a distinct accuracy advantage over a simple high-input-norm calibration baseline.

## Why it stopped

No-paper useful signal: bounded proxy supports the range-coverage mechanism versus random, but the novelty claim is mixed because a cheap input-norm baseline is competitive or stronger.

## Recommended next action

Run a bounded deepen study on one real pretrained CPU PTQ workload, comparing activation-aware selection against random, input-norm top, and diversity baselines before investing in scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model CPU PTQ calibration selector baseline check
- Success threshold: Activation-aware selection beats all listed baselines by at least 0.5 percentage points task accuracy or at least 20% distortion reduction without accuracy loss across two budgets.
- Stop condition: Stop if activation-aware does not beat the input-norm or diversity baseline on the first real-model workload, because this run already showed random-only comparisons are insufficient.

## Evidence references

- Artifact root: `<local-path>/projects/activation-aware-calibration-data-selection-for-int8-cpu-inference-ec4e8faedbb7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
