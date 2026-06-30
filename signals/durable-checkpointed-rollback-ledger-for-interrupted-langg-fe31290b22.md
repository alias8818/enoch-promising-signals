# Durable checkpointed rollback ledger for interrupted LangGraph tool agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `durable-checkpointed-rollback-ledger-for-interrupted-langg-fe31290b22`
Run ID: `durable-checkpointed-rollback-ledger-for-interrupted-langg-fe31290b22-20260527T203043312150+0000`

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

- Parent run decision: Rollback ledger for multi-step agent error recovery: enoch://control-plane/projects/rollback-ledger-for-multi-step-agent-error-recovery-d01821746136/runs/rollback-ledger-for-multi-step-agent-error-recovery-d01821746136-20260527T144554888264+0000
- Parent run decision: Rollback ledger in a reversible LangGraph tool-agent harness: enoch://control-plane/projects/rollback-ledger-in-a-reversible-langgraph-tool-agent-harne-1230084593/runs/rollback-ledger-in-a-reversible-langgraph-tool-agent-harne-1230084593-20260527T173313898339+0000

## What looked useful

Across 40 fixed seeds, checkpoint_only produced 280 duplicate external effects and duplicates in 40/40 trials; ledger_full produced 0 duplicates in 40/40 trials. Ablations still duplicated: ledger_no_reconcile produced 137 duplicate effects and ledger_after_only produced 121, supporting that both pre-effect intent and reconciliation are necessary.

## Boundaries and scale limits

Synthetic SQLite external-effect table, 24-step single-thread graphs, deterministic in-process exceptions rather than OS-level process kills, no concurrent graph threads, no real third-party APIs, and no production deployment workload.

## Claim scope

For a small actual LangGraph StateGraph tool-agent harness with SQLite checkpointing, deterministic hard-cutover exceptions injected after external side effects but before node checkpointing caused duplicate external effects under checkpoint-only replay, while a durable pre-effect intent plus replay-time reconciliation rollback ledger eliminated duplicates across 40 fixed-seed trials.

## Why it stopped

Tier 2 medium confirmation supports the mechanism but remains too synthetic and small for publication-grade evidence.

## Recommended next action

Run a bounded deepen follow-up using real process kill/restart against concurrent LangGraph threads and at least two realistic tool adapters before considering a scoped systems paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-kill rollback ledger validation for concurrent LangGraph tool agents
- Success threshold: Across at least 50 fixed-seed concurrent trials, full ledger has zero duplicate effects and zero missing operations, reduces duplicate effects by at least 95% versus checkpoint-only, and adds less than 25% median recovery-latency overhead.
- Stop condition: Stop if any full-ledger trial duplicates or loses an operation under a reconciliable completed external effect, or if median overhead exceeds 50% without a clear optimization path.

## Evidence references

- Artifact root: `<local-path>/projects/durable-checkpointed-rollback-ledger-for-interrupted-langg-fe31290b22`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
