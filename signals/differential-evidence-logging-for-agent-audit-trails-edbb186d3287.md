# Differential Evidence Logging for Agent Audit Trails

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `differential-evidence-logging-for-agent-audit-trails-edbb186d3287`
Run ID: `differential-evidence-logging-for-agent-audit-trails-edbb186d3287-20260608T014245394642+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/644b992a27af

## What looked useful

Differential evidence logging preserved exact replay, audit fidelity, unsupported-citation detection, and simple tamper detection in the synthetic harness. Storage improved strongly at low/moderate churn but became slightly worse than full snapshots at 100% churn.

## Boundaries and scale limits

Synthetic traces only; 60 traces per churn condition; no real agent logs, no human audit queries, no online latency measurement, no signed append-only storage, and no adversary able to recompute hash chains.

## Claim scope

In deterministic synthetic 40-step agent traces with structured evidence dictionaries, differential evidence logs exactly reconstructed step-level audit state and reduced storage versus full snapshots when evidence churn was below about 100% per step.

## Why it stopped

Bounded synthetic evidence produced a useful mechanism signal and a clear high-churn failure limit, but it is proxy evidence rather than direct validation on real agent audit trails.

## Recommended next action

Run the same encoding and audit-query comparison on real agent traces with policy-relevant audit tasks before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Differential Evidence Logs on Real Agent Audit Traces
- Success threshold: At least 95% audit-query fidelity versus full snapshots, exact replay for reconstructable states, median differential/full byte ratio below 0.50, and no worse than 20% online logging latency overhead on the trace corpus.
- Stop condition: Stop if real traces have median churn high enough that differential/full byte ratio exceeds 0.75 or if audit-query fidelity falls below 95% without a repairable schema issue.

## Evidence references

- Artifact root: `<local-path>/projects/differential-evidence-logging-for-agent-audit-trails-edbb186d3287`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
