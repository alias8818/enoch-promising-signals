# Live LangGraph process-kill replay validation for evidence-ledger mismatch halts

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `100`
Project ID: `live-langgraph-process-kill-replay-validation-for-evidence-6ba862869f`
Run ID: `live-langgraph-process-kill-replay-validation-for-evidence-6ba862869f-20260523T183204835098+0000`

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

- Parent run decision: Persistent-checkpoint replay validation for evidence-ledger tool mismatch halts: enoch://control-plane/projects/persistent-checkpoint-replay-validation-for-evidence-ledge-d2a7b34684/runs/persistent-checkpoint-replay-validation-for-evidence-ledge-d2a7b34684-20260523T182155240236+0000
- Parent run decision: LangGraph replay validation for evidence-ledger tool mismatch halts: enoch://control-plane/projects/langgraph-replay-validation-for-evidence-ledger-tool-misma-b61b0d0118/runs/langgraph-replay-validation-for-evidence-ledger-tool-misma-b61b0d0118-20260523T181114672411+0000

## What looked useful

Across 200 real process-kill/replay trials, all first child processes were killed with SIGKILL after the ledger marker and all replays reached attempt 2. Baseline mismatch finalized with ledger divergence in 50/50 trials; guarded mismatch halted before finalization in 50/50 trials; guarded matching control had 0/50 false halts and finalized normally.

## Boundaries and scale limits

Validated on one CPU worker, one child process at a time, one evidence-producing node, local SQLite checkpoint DB, and local SQLite evidence ledger. Not validated for distributed workers, remote checkpointers, concurrent duplicate execution, network partitions, production controller integration, or larger multi-node DAGs.

## Claim scope

In a local single-node LangGraph 1.2.1 StateGraph using SQLite checkpointing, a hard SIGKILL after an external evidence-ledger write and before node checkpoint causes unguarded mismatch replays to finalize with divergent ledger evidence, while a ledger-hash guard halts mismatching replays and allows idempotent matching replays.

## Why it stopped

The scoped mechanism is strongly supported locally, but the validation surface is too narrow for publication-grade claims about live LangGraph controller reliability.

## Recommended next action

Stop this run as no-paper useful evidence; the next bounded deepen test should add concurrent duplicate worker replay and a multi-node DAG before considering any systems-paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent multi-node LangGraph replay validation for evidence-ledger mismatch halts
- Success threshold: Guarded mismatch halts in at least 99% of mismatch trials, guarded match false-halt rate is 0%, and the unguarded baseline exhibits measurable ledger divergence under the same kill/replay schedule.
- Stop condition: Stop if guarded match produces any reproducible false halt, if guarded mismatch fails to halt below the success threshold, or if concurrency cannot be exercised with durable evidence artifacts.

## Evidence references

- Artifact root: `<local-path>/projects/live-langgraph-process-kill-replay-validation-for-evidence-6ba862869f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
