# Agent Reliability via Evidence Ledger for Tool Use

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-reliability-via-evidence-ledger-for-tool-use-cf3926f9566e`
Run ID: `agent-reliability-via-evidence-ledger-for-tool-use-cf3926f9566e-20260605T054044068601+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/28a3c5acb135

## What looked useful

Evidence ledgers appear useful as a reliability gate for missing, inconsistent, or independently corrupted tool outputs, but they trade coverage for reliability and cannot guarantee correctness when multiple sources agree on the same wrong value.

## Boundaries and scale limits

Model-free synthetic simulator only; no real LLM, no production tools, no human support judgments, no real retrieval traces, and no broad task diversity. Correlated wrong evidence remains a clear failure mode.

## Claim scope

In a bounded synthetic four-field tool-use reconciliation benchmark, a source-tagged evidence ledger with consistency verification reduced unsupported answers to zero and reduced mean wrong-answer rate from 0.615 to 0.141 across 27 noise/missing/correlation conditions, at the cost of lower coverage and more tool calls.

## Why it stopped

Closed as no-paper useful signal because the result is synthetic/proxy-only and does not validate real agent behavior.

## Recommended next action

Run a deepen follow-up on real LLM tool-use traces with matched ledger and no-ledger controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Evidence Ledger Gate on Real LLM Tool-Use Traces
- Success threshold: Ledger condition reduces unsupported-answer rate by at least 30% and wrong-answer rate by at least 20% versus control, with abstention below 40% and mean tool-call overhead below 2.5x.
- Stop condition: Stop if the ledger condition fails to reduce either unsupported-answer rate or wrong-answer rate on the real-trace benchmark, or if abstention reaches 40% or higher.

## Evidence references

- Artifact root: `<local-path>/projects/agent-reliability-via-evidence-ledger-for-tool-use-cf3926f9566e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
