# Multi-trace anchored evidence ledger false-accept evaluation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `multi-trace-anchored-evidence-ledger-false-accept-evaluati-08c5ecb743`
Run ID: `multi-trace-anchored-evidence-ledger-false-accept-evaluati-08c5ecb743-20260628T201906669269+0000`

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

- Parent run decision: Anchored Evidence Ledger on Real Agent Tool Traces: enoch://control-plane/projects/anchored-evidence-ledger-on-real-agent-tool-traces-f4900482e6/runs/anchored-evidence-ledger-on-real-agent-tool-traces-f4900482e6-20260628T194732510180+0000
- Parent run decision: Hash-Chained Evidence Ledger for Agent Reliability: enoch://control-plane/projects/hash-chained-evidence-ledger-for-agent-reliability-7460ad11295e/runs/hash-chained-evidence-ledger-for-agent-reliability-7460ad11295e-20260628T164251261647+0000

## What looked useful

Multi-trace anchored verification appears to close failure modes that pass id-only, keyword-only, and single-anchor checks. Single-anchor validation remained vulnerable to wrong-trace, single-trace-only, and partial-support ledgers.

## Boundaries and scale limits

Synthetic controlled templates only; no real agent transcripts, natural language ambiguity, live tool outputs, or human-labeled production failures were tested.

## Claim scope

On a deterministic synthetic benchmark of 500 base claims and 3,000 total ledger cases, requiring exact span hashes, distinct trace ids, and complete dimension coverage reduced false accepts from 60-100% for weaker validators to 0% without false rejects.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/proxy rather than direct real-trace validation.

## Recommended next action

Run the same verifier comparison on a small replay corpus of real tool-agent traces with manually labeled claim support.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real trace replay test for multi-trace anchored evidence ledgers
- Success threshold: multi_trace_anchor false_accept_rate <= 0.05 and false_reject_rate <= 0.10, with at least 100 invalid and 100 valid labeled cases.
- Stop condition: Stop if false_accept_rate exceeds 0.10 or false_reject_rate exceeds 0.20 after the first 100 labeled cases, unless errors are due to a clearly fixable parser bug.

## Evidence references

- Artifact root: `<local-path>/projects/multi-trace-anchored-evidence-ledger-false-accept-evaluati-08c5ecb743`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
