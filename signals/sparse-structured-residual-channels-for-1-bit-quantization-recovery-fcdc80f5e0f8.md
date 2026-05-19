# Sparse Structured Residual Channels for 1-Bit Quantization Recovery

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `sparse-structured-residual-channels-for-1-bit-quantization-recovery-fcdc80f5e0f8`
Run ID: `sparse-structured-residual-channels-for-1-bit-quantization-recovery-fcdc80f5e0f8-20260519T025222312438+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/eef056bc5fd5

## What looked useful

Oracle top-k residual channels improved weight reconstruction but usually failed to improve accuracy over plain 1-bit quantization. A narrow +0.75 point gain appeared only on the sparse-feature task at 12.5% channel budget, while the low-rank control remained about 7 points better.

## Boundaries and scale limits

Tested only small synthetic classification MLPs on GB10, five seeds per condition, residual budgets of 3.125%, 6.25%, and 12.5%. Did not test transformer language models, real corpora, learned residual retraining, activation-aware channel selection, inference kernels, or long/full-scale validation.

## Claim scope

Bounded synthetic MLP post-training quantization probe: weight-error top-k sparse residual input channels reduce relative weight MSE for 1-bit quantized linear layers, but do not reliably recover task accuracy and are dominated by same-budget low-rank residual controls.

## Why it stopped

Proxy/local early falsification: the directly tested oracle structured-channel residual reduced weight MSE but did not deliver reliable accuracy recovery and was consistently weaker than a same-budget low-rank residual baseline.

## Recommended next action

Stop this simple top-k weight-error channel formulation as no-paper evidence; the only justified next test is a bounded activation-aware or learned residual-channel selection study against low-rank controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Activation-aware learned residual channels for 1-bit recovery
- Success threshold: Mean task metric improves over plain 1-bit by at least 50% of the fp32-to-1bit gap and is not worse than the same-budget low-rank control by more than 1% relative across at least two budgets.
- Stop condition: Stop if activation-aware or learned channels fail to beat random channels by at least 1 accuracy point or equivalent perplexity/NLL improvement on the first real-model proxy, or remain more than 3 points behind the low-rank control at matched budget.

## Evidence references

- Artifact root: `<local-path>/projects/sparse-structured-residual-channels-for-1-bit-quantization-recovery-fcdc80f5e0f8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
