# SignSGD Error Feedback CPU Optimizer

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `signsgd-error-feedback-cpu-optimizer-e47f4a414b98`
Run ID: `signsgd-error-feedback-cpu-optimizer-e47f4a414b98-20260529T122409581118+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c79b9e0aa0fd

## What looked useful

Error feedback partly repairs sign quantization on the quadratic but remains 3.10x worse in final loss and 0.735x SGD throughput while requiring residual state; on logistic regression it matches SGD loss but is slower and slightly lower accuracy.

## Boundaries and scale limits

No deep neural network, real dataset, PyTorch integration, or distributed communication-compression setting was tested; results are limited to local dense CPU objectives and three seeds.

## Claim scope

Bounded CPU-only NumPy tests on synthetic logistic regression and an ill-conditioned diagonal quadratic show scaled-sign signSGD with error feedback does not outperform full-gradient SGD as a dense local CPU optimizer.

## Why it stopped

Bounded direct CPU evidence does not support signSGD with error feedback as a better dense local CPU optimizer than SGD; this is not a full distributed/deep-learning falsification.

## Recommended next action

Stop this EF CPU optimizer line as no-paper evidence; a separate bounded branch could test plain unit signSGD on real CPU logistic/classification workloads because it beat SGD on the synthetic logistic task but failed the quadratic control.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Plain SignSGD CPU Classification Probe
- Success threshold: Plain signSGD reaches the same or better validation accuracy than tuned SGD at equal or lower wall-clock time on at least two real CPU classification tasks, without failing the control by more than 2x final loss.
- Stop condition: Stop if signSGD loses to tuned SGD on wall-clock-to-accuracy on both real classification tasks or repeats the severe quadratic-style instability on a realistic control.

## Evidence references

- Artifact root: `<local-path>/projects/signsgd-error-feedback-cpu-optimizer-e47f4a414b98`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
