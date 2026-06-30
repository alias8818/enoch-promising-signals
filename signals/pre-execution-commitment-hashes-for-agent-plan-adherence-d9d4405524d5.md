# Pre-Execution Commitment Hashes for Agent Plan Adherence

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `pre-execution-commitment-hashes-for-agent-plan-adherence-d9d4405524d5`
Run ID: `pre-execution-commitment-hashes-for-agent-plan-adherence-d9d4405524d5-20260527T235351937839+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/ca1df01e51ec

## What looked useful

Hash-only commitments produced 0.0 drift reduction across 20 swept parameter cells. With audit probability 0.2 and penalty 5.0, enforced hashes reduced drift from 1.00000 to 0.36594 in the main 50k-trial-per-policy run.

## Boundaries and scale limits

Synthetic single-process simulation only; no real LLM agents, natural-language semantic adjudication, tool traces, multi-step tasks, adversarial plan wording, or production monitor reliability were tested.

## Claim scope

In a reproducible synthetic utility model, pre-execution plan hashes do not reduce plan drift without enforcement, but hashes paired with audit probability and drift penalties substantially reduce drift.

## Why it stopped

Standalone commitment hashes were falsified as an adherence mechanism in the synthetic model; the positive effect requires audit/reveal enforcement, and the evidence is proxy-only rather than full validation.

## Recommended next action

Stop as no-paper useful signal; test the enforcement-dependent mechanism next on real tool-using LLM agents with blind semantic drift adjudication.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent audit-enforced commitment hash benchmark
- Success threshold: Audit-enforced hashes reduce adjudicated drift by at least 20 percentage points versus no commitment and by at least 15 percentage points versus hash-only, with hash-only not credited as adherence-improving unless it independently reduces drift.
- Stop condition: Stop if hash-only and audit-enforced arms both fail to reduce drift by at least 10 percentage points after 100 tasks, or if adjudicator agreement is too low to distinguish plan drift from legitimate replanning.

## Evidence references

- Artifact root: `<local-path>/projects/pre-execution-commitment-hashes-for-agent-plan-adherence-d9d4405524d5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
