# Simplified Commitment Ledger for Agent Plan Adherence

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `simplified-commitment-ledger-for-agent-plan-adherence-bfde17a8bbdf`
Run ID: `simplified-commitment-ledger-for-agent-plan-adherence-bfde17a8bbdf-20260524T181857854854+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/0f353212c01e

## What looked useful

Ledger plus repair improved full-success rate from 0.1132 to 0.8174 in the main setting and from 0.0378 to 0.7083 in the stress setting, while ledger without repair was indistinguishable from a checklist-style pending-item selector.

## Boundaries and scale limits

10,000 synthetic trials per policy under two stochastic settings; no LLM agents, no real tool-use tasks, no human/blinded scoring, and repair actions are modeled rather than executed by a real model.

## Claim scope

In a controlled stochastic simulator of plan commitments, a simplified commitment ledger improves plan adherence only when paired with an explicit final reconciliation/repair pass; pending-item selection alone behaves like a checklist control.

## Why it stopped

Proxy-only useful signal: the synthetic mechanism is supported, but real agent-plan adherence remains unvalidated and this run is not paper-ready.

## Recommended next action

Run a bounded real-agent follow-up on observable commitment-completion tasks with randomized ledger/no-ledger assignment and blinded scoring.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent commitment ledger adherence benchmark
- Success threshold: At least +10 percentage points absolute full-commitment completion over checklist control with 95% confidence intervals excluding zero, and less than 25% median action overhead.
- Stop condition: Stop if ledger-with-reconciliation fails to beat checklist completion by 5 percentage points or if action overhead exceeds 50% median without a compensating completion gain.

## Evidence references

- Artifact root: `<local-path>/projects/simplified-commitment-ledger-for-agent-plan-adherence-bfde17a8bbdf`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
