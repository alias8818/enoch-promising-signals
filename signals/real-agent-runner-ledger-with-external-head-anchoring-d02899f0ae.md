# Real Agent Runner Ledger With External Head Anchoring

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-runner-ledger-with-external-head-anchoring-d02899f0ae`
Run ID: `real-agent-runner-ledger-with-external-head-anchoring-d02899f0ae-20260619T184102140330+0000`

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

- Parent run decision: Hash-Chained Evidence Ledger for Agent Tool Calls: enoch://control-plane/projects/hash-chained-evidence-ledger-for-agent-tool-calls-2537823ef324/runs/hash-chained-evidence-ledger-for-agent-tool-calls-2537823ef324-20260619T181522075593+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/99835663199a

## What looked useful

External latest-head anchoring added concrete tamper-detection power beyond a local hash chain: 4/4 anchored tamper detections versus 2/4 unanchored detections, with zero false positives on the clean ledger.

## Boundaries and scale limits

Only 12 toy subprocess tasks were tested. The anchor was an independent local process, not a public transparency log or third-party timestamping service. No crash consistency, concurrent writers, production agent traces, blob retention, redaction, or compromise of both ledger and anchor were tested.

## Claim scope

In a controlled local Tier 1 test, a real subprocess-based agent runner with a hash-chained ledger and an independent HTTP latest-head anchor detected content edits, truncation, rehashed fork rewrite, and entry reorder; a local-chain-only control missed truncation and rehashed fork rewrite.

## Why it stopped

Tier 1 direct mechanism threshold was met, but the evidence remains a small local controlled test and is not publication-grade.

## Recommended next action

Run a deepen follow-up using a production-grade external transparency/timestamp anchor with crash-restart and concurrent-runner tamper cases.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Agent Runner Ledger Anchoring With Production Transparency Log And Crash Tests
- Success threshold: Clean verification false positives equal 0; all truncation/fork/content/reorder/replay tamper cases detected; crash recovery either reaches a verified committed prefix or emits an explicit unreconciled state without silently accepting a forged head.
- Stop condition: Stop if the production/external anchor cannot provide monotonic append-only latest-head semantics, or if crash recovery silently accepts a tampered or ambiguous ledger state.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-runner-ledger-with-external-head-anchoring-d02899f0ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
