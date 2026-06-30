# Crash-injected LangGraph checkpoint compression for home-agent traces

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `crash-injected-langgraph-checkpoint-compression-for-home-a-e76bcd709c`
Run ID: `crash-injected-langgraph-checkpoint-compression-for-home-a-e76bcd709c-20260604T004535801389+0000`

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

- Parent run decision: Compressed State Checkpoints for Fault-Tolerant Home Agents: enoch://control-plane/projects/compressed-state-checkpoints-for-fault-tolerant-home-agents-450d8026609d/runs/compressed-state-checkpoints-for-fault-tolerant-home-agents-450d8026609d-20260603T213953830612+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3b9552bce518

## What looked useful

Checkpoint compression is a plausible practical mechanism for repeated home-agent traces: zstd3(msgpack) was 88.76% smaller than JSON payload bytes and passed 0/48 zstd crash-recovery failures under the tested atomic write stages. The result is useful for deciding to test a real LangGraph checkpointer wrapper, but is not paper-positive.

## Boundaries and scale limits

Synthetic traces only; local file checkpointer only; no real Home Assistant private traces; no full LangGraph graph replay; no SQLite/Postgres/cloud backend validation; no concurrent writers; no power-loss or filesystem-journaling fault injection; 120 checkpoints and 144 injected process crashes total.

## Claim scope

In a controlled local Tier 1 test using 120 synthetic home-agent LangGraph-shaped checkpoints serialized with LangGraph JsonPlusSerializer, zstd level 3 over msgpack reduced mean framed checkpoint bytes by 88.76% versus JSON payload bytes, added sub-millisecond codec overhead, and recovered successfully from all tested process-exit crash points in a checksum-framed atomic file protocol.

## Why it stopped

Stopped after the required Tier 1 controlled small direct test because the mechanism threshold passed but evidence remains bounded local no-paper validation.

## Recommended next action

Run a bounded deepen follow-up that wraps an actual LangGraph SQLite or file checkpointer with zstd compression, executes replayable Home Assistant traces through a graph, injects process exits during graph execution, and verifies post-restart state equality plus checkpoint byte and latency metrics.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-injected zstd wrapper on real LangGraph checkpointer replay traces
- Success threshold: Across at least 300 checkpoints and 100 injected crashes, compressed checkpoint bytes are at least 50% lower than baseline, median added checkpoint latency is below 5 ms, and recovery/replay state mismatch count is 0.
- Stop condition: Stop if any checksum-valid compressed checkpoint cannot replay to the same final graph state as baseline, if crash recovery has any unrecovered committed checkpoint, or if median checkpoint overhead exceeds 5 ms after basic tuning.

## Evidence references

- Artifact root: `<local-path>/projects/crash-injected-langgraph-checkpoint-compression-for-home-a-e76bcd709c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
