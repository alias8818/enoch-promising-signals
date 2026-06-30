# Replay Bounded Evidence Ledger on Real Agent Tool Traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-bounded-evidence-ledger-on-real-agent-tool-traces-d3748df8ac`
Run ID: `replay-bounded-evidence-ledger-on-real-agent-tool-traces-d3748df8ac-20260607T062038975331+0000`

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

- Parent run decision: Bounded Evidence Ledger for Agent Reliability: enoch://control-plane/projects/bounded-evidence-ledger-for-agent-reliability-94bd73bc056a/runs/bounded-evidence-ledger-for-agent-reliability-94bd73bc056a-20260607T040905432796+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d189e1faa4bf

## What looked useful

Tier 1 direct test supports the mechanism: content-addressed command evidence can be replayed from a real agent trace and detects dropped, tampered, exit-code-changed, and reordered completed-command evidence.

## Boundaries and scale limits

Single trace snapshot from one worker run; command-execution events only; no semantic claim-to-evidence validation; no cross-agent or cross-tool corpus; no adversarial redaction or streaming-output stress test.

## Claim scope

A bounded evidence ledger reconstructed from one real Codex JSONL trace snapshot with 39 events and 12 completed command executions replayed exactly and detected four deterministic command-evidence mutations.

## Why it stopped

Tier 1 mechanism threshold passed on a real trace, but the result is too narrow for publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up across 20 independent real agent traces with semantic final-claim-to-ledger checks; stop paper work for this run because the current result is useful no-paper evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-Trace Bounded Evidence Ledger Replay with Semantic Claim Checks
- Success threshold: At least 95% completed-tool-event ledger coverage, 100% unmodified replay pass rate for parseable traces, 100% syntactic mutation detection, and at least 90% detection of injected unsupported final-report claims.
- Stop condition: Stop if more than 20% of ordinary real traces cannot be parsed/replayed, or if semantic unsupported-claim detection stays below 70% after the agreed checker/rubric is implemented.

## Evidence references

- Artifact root: `<local-path>/projects/replay-bounded-evidence-ledger-on-real-agent-tool-traces-d3748df8ac`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
