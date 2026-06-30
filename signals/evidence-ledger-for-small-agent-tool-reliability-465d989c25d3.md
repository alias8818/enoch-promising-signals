# Evidence ledger for small agent tool reliability

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-for-small-agent-tool-reliability-465d989c25d3`
Run ID: `evidence-ledger-for-small-agent-tool-reliability-465d989c25d3-20260604T080905486702+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/be144912c7ce

## What looked useful

Ledger reliability gains depended on available evidence quality. Checksum validation reached 0 wrong finalizations and 1.0 invalid rejection recall; redundant independent cross-checking reduced wrong finalization from 0.3219 to 0.0597; correlated stale evidence remained unresolved with ledger wrong finalization 0.3992 versus baseline mean 0.3993.

## Boundaries and scale limits

10,000 synthetic trials per suite/policy on simple deterministic policies; no real LLM agents, real APIs, human audit study, production latency/cost analysis, or large-scale tool trace replay.

## Claim scope

In a synthetic small-agent invoice-sum benchmark, an evidence ledger reduced wrong final answers when tool faults were detectable by checksum/invariant validation or independent redundant observations, but did not solve correlated stale wrong observations.

## Why it stopped

No-paper useful signal: this is bounded synthetic evidence with a clear failure boundary, not direct publication-grade validation for real small-agent reliability.

## Recommended next action

Run a bounded real-trace replay with actual small-agent tool calls and predeclared validators to test whether the synthetic ledger gains survive real API and LLM planning noise.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace replay of evidence ledgers for small tool agents
- Success threshold: Evidence ledger reduces wrong finalization by at least 30% relative to retry-only in detectable-fault tasks while correlated/validator-missing tasks are reported separately and not counted as solved.
- Stop condition: Stop if fewer than 100 tasks have ground truth and validator coverage, or if ledger overhead exceeds 3x tool calls without at least 20% wrong-finalization reduction in the detectable subset.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-agent-tool-reliability-465d989c25d3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
