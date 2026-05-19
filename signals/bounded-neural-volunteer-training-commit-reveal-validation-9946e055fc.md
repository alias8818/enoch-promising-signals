# Bounded Neural Volunteer Training Commit-Reveal Validation

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `98`
Project ID: `bounded-neural-volunteer-training-commit-reveal-validation-9946e055fc`
Run ID: `bounded-neural-volunteer-training-commit-reveal-validation-9946e055fc-20260515T013756714875+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/53e2fb90ddba

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Controlled small direct test supports commit-reveal plus bounded validation under a simple adversary, but the evidence is synthetic, small-scale, centrally validated, and not publication-grade.

## Recommended next action

Stop this run as no-paper Tier 1 mechanism support; run one bounded medium direct follow-up with non-IID shards, adaptive bounded adversaries, ablations, and larger parameter-matched neural baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Non-IID Adaptive Validation of Commit-Reveal Volunteer Training
- Success threshold: Full commit-reveal validation rejects at least 80% of malicious revealed updates, preserves at least 90% of honest-only test performance, rescues at least 50% of naive adversarial loss damage versus oracle, and beats all ablations in at least 80% of seeds.
- Stop condition: Stop if malicious rejection falls below 60%, honest-only performance drops more than 10% versus naive, or validation overhead makes the bounded protocol slower than 2x naive aggregation at the tested scale.

## Evidence references

- Artifact root: `<local-path>/projects/bounded-neural-volunteer-training-commit-reveal-validation-9946e055fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
