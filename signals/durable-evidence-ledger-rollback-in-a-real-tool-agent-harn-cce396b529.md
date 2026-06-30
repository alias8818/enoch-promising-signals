# Durable evidence-ledger rollback in a real tool-agent harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `durable-evidence-ledger-rollback-in-a-real-tool-agent-harn-cce396b529`
Run ID: `durable-evidence-ledger-rollback-in-a-real-tool-agent-harn-cce396b529-20260526T193511381023+0000`

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

- Parent run decision: Evidence-ledger tool agent with local rollback: enoch://control-plane/projects/evidence-ledger-tool-agent-with-local-rollback-0348276a0352/runs/evidence-ledger-tool-agent-with-local-rollback-0348276a0352-20260525T111521496628+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/625d0a40f048

## What looked useful

Ledger runner had 0/100 residual side-effect trials after crash recovery; baseline had 100/100 residual side-effect trials; commit control preserved a completed 12-tool transaction with zero rollback events.

## Boundaries and scale limits

Small deterministic single-host harness only; no real LangGraph ToolNode integration, concurrent tool calls, remote APIs, streaming outputs, or exhaustive crash-window coverage.

## Claim scope

In a controlled local tool-agent harness using real filesystem writes, subprocess-created files, and SQLite application-table mutations, a durable pre-effect evidence ledger restored all open/crashed transactions across 100 injected hard-exit trials while preserving committed transactions.

## Why it stopped

Small direct Tier 1 evidence supports the mechanism but is not paper-positive or production-general evidence.

## Recommended next action

Run a bounded deepen follow-up that integrates the rollback ledger into an actual LangGraph-style tool executor and injects crashes across before-ledger, after-tool, after-ledger, and commit windows.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-window rollback coverage inside a real LangGraph-style tool executor
- Success threshold: Zero residual side effects in all rollback-eligible crash trials, nonzero residual side effects in the no-rollback baseline, and zero false rollbacks of committed transactions.
- Stop condition: Stop as negative if any rollback-eligible crash window leaves residual local side effects in a reproducible case after one implementation fix pass.

## Evidence references

- Artifact root: `<local-path>/projects/durable-evidence-ledger-rollback-in-a-real-tool-agent-harn-cce396b529`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
