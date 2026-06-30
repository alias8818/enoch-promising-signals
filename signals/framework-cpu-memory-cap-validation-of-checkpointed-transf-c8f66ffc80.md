# Framework CPU memory-cap validation of checkpointed transformer training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `framework-cpu-memory-cap-validation-of-checkpointed-transf-c8f66ffc80`
Run ID: `framework-cpu-memory-cap-validation-of-checkpointed-transf-c8f66ffc80-20260610T181300249460+0000`

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

- Parent run decision: Gradient Checkpointing for CPU Memory-constrained Training: enoch://control-plane/projects/gradient-checkpointing-for-cpu-memory-constrained-training-ca5e7e16a7b9/runs/gradient-checkpointing-for-cpu-memory-constrained-training-ca5e7e16a7b9-20260610T143101910536+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7ed7bd294395

## What looked useful

Activation checkpointing gave a reproducible modest CPU RSS reduction in a direct transformer training step, but optimizer/transient allocation pressure dominated the cap boundary enough that the checkpointed run did not pass under a lower runtime headroom cap than baseline.

## Boundaries and scale limits

Single CPU worker, synthetic tokens, 4-layer d_model=256 transformer, one optimizer step, AdamW, post-setup RLIMIT_AS headroom cap rather than true child cgroup memory.max RSS cap; no GPU/UMA, GPT-2-small-class, larger model, or multi-step validation.

## Claim scope

On a CPU-only PyTorch 2.12 small transformer training step, block-level activation checkpointing reduced parent-sampled peak RSS by about 26-32 MiB on successful runs, but did not improve the observed post-setup RLIMIT_AS runtime-headroom pass/fail threshold: both baseline and checkpointed failed at 325 MiB headroom and passed at 350 MiB.

## Why it stopped

Tier 1 direct CPU test completed; result is mixed/negative for cap-threshold improvement under the available RLIMIT_AS headroom cap and not strong enough for publication.

## Recommended next action

Stop this run as no-paper useful signal; the concrete next test is a true cgroup memory.max RSS-cap validation with optimizer ablations to determine whether AdamW state masks checkpointing's cap-threshold benefit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: True cgroup RSS-cap validation with optimizer ablations for checkpointed transformer training
- Success threshold: Checkpointed training must pass at least one cgroup RSS cap where baseline reproducibly fails, with a threshold shift of at least 5% or 64 MiB and identical loss/backward/step semantics.
- Stop condition: Stop if both modes have the same cgroup RSS pass/fail threshold after optimizer ablation, or if checkpointing reduces RSS by less than 5% on the successful uncapped control.

## Evidence references

- Artifact root: `<local-path>/projects/framework-cpu-memory-cap-validation-of-checkpointed-transf-c8f66ffc80`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
