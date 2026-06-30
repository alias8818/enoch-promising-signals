# Joint INT2 Weights and Activations with Single Shared Residual

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `joint-int2-weights-and-activations-with-single-shared-residual-5d056e063e23`
Run ID: `joint-int2-weights-and-activations-with-single-shared-residual-5d056e063e23-20260630T082140703607+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5ae17bc3184a

## What looked useful

The single shared residual acts as a mean-error correction: it reduced fc3/logit MSE by about 79.7% and W2A2 cross entropy from 10.61 to 7.35, but top-1 accuracy fell from 0.4767 for raw W2A2 to 0.3411 with the residual across 10 seeds.

## Boundaries and scale limits

Small MLP synthetic classification only; no transformer, language modeling, QAT, packed INT2 kernels, real dataset, or long/full-scale validation.

## Claim scope

In a self-contained 10-seed synthetic teacher/student MLP probe, post-training W2A2 quantization with one calibrated shared output residual vector per Linear layer reduces layer/logit MSE and average cross entropy but does not recover top-1 accuracy.

## Why it stopped

Proxy early falsification: a mean calibrated single shared residual corrected logit MSE but consistently worsened top-1 accuracy, so this run does not support the practical W2A2 accuracy-recovery claim.

## Recommended next action

Stop this run as a bounded negative/useful-signal result; the next cheap test is a margin-aware or task-loss-trained shared residual, not a paper claim from mean-error calibration.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Task-loss-trained shared residual for W2A2 margin preservation
- Success threshold: Recover at least 50% of the FP32-to-W2A2 top-1 accuracy loss on average while not increasing cross entropy versus raw W2A2, with no worse than 2/10 seeds regressing.
- Stop condition: Stop if task-loss-trained residual improves cross entropy but still fails to improve mean top-1 accuracy over raw W2A2, or if gains only appear on the calibration split.

## Evidence references

- Artifact root: `<local-path>/projects/joint-int2-weights-and-activations-with-single-shared-residual-5d056e063e23`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
