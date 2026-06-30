# Consistency-Gated Agent Action Selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `consistency-gated-agent-action-selection-8ec18d527556`
Run ID: `consistency-gated-agent-action-selection-8ec18d527556-20260523T214843257222+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/b49cd735f64b

## What looked useful

Agreement gating raised executed-action accuracy from 0.6017 single-sample accuracy to 0.9927 at 0.3566 coverage with no systematic misconception, but at 5% systematic misconception the best at-least-30%-coverage gate still executed 95.04% of misled tasks and had 10.17% wrong executed actions; stricter 0.90 agreement gates became confidently wrong as systematic bias increased.

## Boundaries and scale limits

CPU-only synthetic simulation; no real LLM calls, no tool-use environment, no prompt/model distribution shift, no latency or cost-normalized task success measurement.

## Claim scope

In a synthetic 5-action oracle-graded decision model, repeated-sample agreement is an effective executed-action accuracy filter when sampling errors are mostly independent, but it is not a reliable safety certificate when samples share a confidently wrong systematic bias.

## Why it stopped

No-paper useful signal: the local evidence is synthetic and shows a clear shared-misconception failure mode, so this should not be promoted as a publication-grade validation.

## Recommended next action

Run a bounded real-agent trace replay comparing agreement-only gating with agreement plus an independent verifier or critique check, using oracle-graded actions and cost-normalized task success.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Replay of Agreement Gating With Shared-Wrong Detection
- Success threshold: At least 30% action coverage, at least 15 percentage-point executed-action accuracy lift over single-sample selection, and fewer than 5% high-agreement shared-wrong executions among executed actions.
- Stop condition: Stop if agreement plus verification cannot reduce high-agreement shared-wrong executions below 5% at 30% or higher coverage, or if the accuracy lift over single-sample selection is below 15 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/consistency-gated-agent-action-selection-8ec18d527556`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
