# 8-bit Optimizer State Quantization with Standard Learning Rates

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `8-bit-optimizer-state-quantization-with-standard-learning-rates-82d0fd986ce5`
Run ID: `8-bit-optimizer-state-quantization-with-standard-learning-rates-82d0fd986ce5-20260609T155925493640+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/32992304ea4c

## What looked useful

Block granularity and task sensitivity dominate: block32 preserved logistic validation metrics at 26-29% of fp32 Adam state memory, while block256 failed on logistic and both tested 8-bit variants were unstable on the MLP despite low aggregate state reconstruction error.

## Boundaries and scale limits

CPU-only synthetic tasks, small models, 5 seeds, 800 minibatch steps, no real datasets, no transformer-scale training, no fused GPU optimizer implementation, and no long-horizon schedule validation.

## Claim scope

Bounded NumPy experiments on synthetic logistic and 1-hidden-layer MLP classification show that naive blockwise 8-bit Adam moment-state storage can match fp32 Adam on an easy logistic task with block size 32, but does not reliably preserve standard-learning-rate Adam on the nonlinear MLP task or with block size 256.

## Why it stopped

Bounded direct optimizer-state tests reject the naive broad claim as paper-ready; this is not full-scale validation, but it is a proxy/direct small-model falsification of reliability at unchanged learning rates.

## Recommended next action

Stop this run as a no-paper useful signal; next test a more robust second-moment quantization scheme on the reproduced MLP failure case before considering scale.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Robust 8-bit Adam second-moment quantization on the MLP failure case
- Success threshold: At both learning rates, modified q8 Adam mean validation accuracy is within 1 percentage point of fp32 Adam, mean validation loss is within 0.03, no more than one of five seeds is a clear failure, and state memory remains below 35% of fp32 Adam.
- Stop condition: Stop if the modified quantizer still loses more than 3 validation accuracy points or more than 0.10 validation loss versus fp32 Adam at either learning rate after 5 seeds.

## Evidence references

- Artifact root: `<local-path>/projects/8-bit-optimizer-state-quantization-with-standard-learning-rates-82d0fd986ce5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
