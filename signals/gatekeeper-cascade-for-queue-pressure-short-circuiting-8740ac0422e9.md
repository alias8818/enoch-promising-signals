# Gatekeeper Cascade for Queue Pressure Short-Circuiting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gatekeeper-cascade-for-queue-pressure-short-circuiting-8740ac0422e9`
Run ID: `gatekeeper-cascade-for-queue-pressure-short-circuiting-8740ac0422e9-20260602T160315358837+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/65b9ae3ac93d

## What looked useful

Pressure-aware short-circuiting improved useful-on-time-per-arrival in 18/18 synthetic aggregate cases, with large gains near saturation, but high overload cases required rejecting valid requests predicted to miss SLO.

## Boundaries and scale limits

Synthetic proxy only; no production trace, real gate classifier, GPU inference server, batching scheduler, multi-server router, or fairness policy was tested.

## Claim scope

In a deterministic synthetic single-server queue model with invalid traffic, lognormal service times, and a 120 ms SLO, a pressure-aware gatekeeper cascade improved useful on-time completions under overload and reduced service CPU per useful on-time completion.

## Why it stopped

Evidence is a bounded synthetic proxy that supports the mechanism but does not provide direct production or publication-grade validation.

## Recommended next action

Stop this run as no-paper useful signal; next run should map break-even thresholds for gate cost, false valid rejects, and pressure-reject policy before attempting a real serving replay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gatekeeper Cascade Break-Even Sensitivity Map
- Success threshold: Find at least one overload region with useful-on-time-per-arrival improvement of 0.10 or greater, CPU per useful completion reduced by 25% or greater, and valid rejection rate below 2%; otherwise close as practically non-viable for strict-serving use cases.
- Stop condition: Stop when all gate-cost/false-reject/pressure-threshold grid cells are evaluated or when no configuration can satisfy the valid-reject cap at 120-180 rps overload.

## Evidence references

- Artifact root: `<local-path>/projects/gatekeeper-cascade-for-queue-pressure-short-circuiting-8740ac0422e9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
