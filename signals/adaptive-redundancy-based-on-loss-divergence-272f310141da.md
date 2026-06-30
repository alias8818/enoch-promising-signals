# Adaptive Redundancy Based on Loss Divergence

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-redundancy-based-on-loss-divergence-272f310141da`
Run ID: `adaptive-redundancy-based-on-loss-divergence-272f310141da-20260601T060734089513+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/7c1ce4c99f51

## What looked useful

Loss divergence is useful as an error-prone-example selector, capturing about 76-80% of base errors with 20% extra routing and over 92% with 40% extra routing, but the tested redundancy path is too correlated to turn that targeting into meaningful accuracy gains.

## Boundaries and scale limits

Synthetic 2D task only; oracle loss divergence requires labels and is not deployable at inference; deployable JS prediction divergence is weaker; no GPT-2-small-class, real dataset, production serving, or large-model validation was run.

## Claim scope

On a synthetic nonlinear classification benchmark with 8 independently trained small MLP replicas, true-label loss divergence strongly prioritizes examples where a cheap 2-replica base is wrong, but adaptive routing to the full ensemble yields only tiny accuracy gains because the redundant path has little headroom over the base.

## Why it stopped

Proxy/medium evidence is mixed rather than publication-grade: oracle loss divergence finds errors, but adaptive redundancy with same-family replicas produces negligible accuracy lift and the inference-time proxy is weaker.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use a more diverse or specialized redundant path and a deployable divergence proxy on a real small benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Diversity-enhanced adaptive redundancy routing
- Success threshold: At 20-40% extra routed compute, deployable divergence routing improves NLL by at least 1% relative to the base and beats random and entropy controls on paired seeds without losing accuracy.
- Stop condition: Stop if the full redundant path improves less than 0.5 percentage points accuracy or less than 1% NLL over the cheap path, because adaptive routing then has insufficient headroom.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-redundancy-based-on-loss-divergence-272f310141da`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
