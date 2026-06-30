# Real Agent Runtime Evidence Ledger Integration

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-agent-runtime-evidence-ledger-integration-a6c950eea3`
Run ID: `real-agent-runtime-evidence-ledger-integration-a6c950eea3-20260620T020900280576+0000`

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

- Parent run decision: Agent Evidence Ledger with Hash-Chained Action Trace: enoch://control-plane/projects/agent-evidence-ledger-with-hash-chained-action-trace-c8b4b4daf526/runs/agent-evidence-ledger-with-hash-chained-action-trace-c8b4b4daf526-20260620T014742559673+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a20ab1ddc3ea

## What looked useful

Ledger-wrapped LangGraph nodes preserved final outputs, captured 1000/1000 expected events, verified the hash chain, and detected tampering, but synchronous SQLite persistence failed the <=3x mean latency overhead threshold: 14.58x with per-event commits and 7.92x with per-run commits.

## Boundaries and scale limits

Single-process CPU-only run; no concurrent writers, no long-running resumable agents, no production traffic, no async/background writer, no external evidence store, and no model/GPU serving workload.

## Claim scope

Tier 1 small direct LangGraph StateGraph integration with deterministic four-node agent, SQLite hash-chain evidence ledger, 250 measured invocations, and tamper check on a copied ledger.

## Why it stopped

No-paper useful signal: the direct small runtime integration supports the mechanism but falsifies the lightweight synchronous durable SQLite overhead threshold; this is not a full production validation.

## Recommended next action

Run a bounded deepen follow-up with an async or buffered ledger writer that preserves crash-recovery semantics and targets <=3x mean overhead on the same LangGraph workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Async buffered evidence ledger for LangGraph runtime integration
- Success threshold: All correctness checks pass, acknowledged evidence survives a forced process stop, and mean latency overhead is <=3x versus baseline on the same workload.
- Stop condition: Stop if async/buffered persistence either loses acknowledged events, fails tamper verification, changes final outputs, or remains >3x mean latency overhead after one bounded implementation pass.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-runtime-evidence-ledger-integration-a6c950eea3`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
