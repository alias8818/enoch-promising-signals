# Process-kill rollback ledger validation for concurrent LangGraph tool agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `process-kill-rollback-ledger-validation-for-concurrent-lan-1f6772560b`
Run ID: `process-kill-rollback-ledger-validation-for-concurrent-lan-1f6772560b-20260528T003853173266+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `100`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 35, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- strong evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Durable checkpointed rollback ledger for interrupted LangGraph tool agents: enoch://control-plane/projects/durable-checkpointed-rollback-ledger-for-interrupted-langg-fe31290b22/runs/durable-checkpointed-rollback-ledger-for-interrupted-langg-fe31290b22-20260527T203043312150+0000
- Parent run decision: Rollback ledger in a reversible LangGraph tool-agent harness: enoch://control-plane/projects/rollback-ledger-in-a-reversible-langgraph-tool-agent-harne-1230084593/runs/rollback-ledger-in-a-reversible-langgraph-tool-agent-harne-1230084593-20260527T173313898339+0000

## What looked useful

Naive LangGraph tool execution left 915 orphan side-effect tasks / 1,410 orphan files after 1,654 SIGKILLs; LangGraph in-memory checkpointing without a side-effect ledger left 960 orphan tasks / 1,513 orphan files after 1,652 SIGKILLs; the corrected rollback ledger left 0 orphan tasks / 0 orphan files after 2,336 SIGKILLs, at about 2.75x lower throughput and higher p95 latency.

## Boundaries and scale limits

Evidence is local and synthetic: filesystem writes stand in for tools; no production LangGraph server, persistent checkpoint backend, multi-host scheduler, network API, database transaction, irreversible side effect, or power-loss fault model was validated.

## Claim scope

On one local GB10 host, for synthetic filesystem-backed LangGraph StateGraph tool agents run as concurrent OS processes, a SQLite rollback ledger around each tool side effect eliminated orphan external files after SIGKILL in 10 fixed-seed trials per mode, 384 tasks per trial, and 2,336 killed ledger-mode processes.

## Why it stopped

Bounded local validation supports the rollback-ledger mechanism but remains synthetic and implementation-specific, so it is useful no-paper evidence rather than publication-grade direct evidence.

## Recommended next action

Stop short of paper writing; the next bounded deepen test should replace filesystem tool effects with reversible database/API-style tool adapters and validate the same invariant under a persistent LangGraph checkpointer.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Rollback ledger validation with persistent LangGraph checkpointing and database/API tool adapters
- Success threshold: Across at least 10 fixed seeds and 1000 or more killed ledger-mode processes, rollback-ledger mode has 0 orphan side effects and 0 incomplete commits while both baselines show nonzero orphan rates; recovery p95 remains under 1 second per trial at the tested scale.
- Stop condition: Stop if any corrected ledger trial leaves an orphan or incomplete commit, if persistent checkpointing alone eliminates the issue, or if realistic tool semantics reveal irreversible side effects that cannot be represented by rollback entries.

## Evidence references

- Artifact root: `<local-path>/projects/process-kill-rollback-ledger-validation-for-concurrent-lan-1f6772560b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
