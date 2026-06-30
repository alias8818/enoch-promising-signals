# Heterogeneous Real Agent Trace Ledger Replay with Restart Persistence

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `heterogeneous-real-agent-trace-ledger-replay-with-restart-e01dae3a71`
Run ID: `heterogeneous-real-agent-trace-ledger-replay-with-restart-e01dae3a71-20260605T193708334889+0000`

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

- Parent run decision: Real Agent Trace Evidence Ledger with Anchored Bounded Replay: enoch://control-plane/projects/real-agent-trace-evidence-ledger-with-anchored-bounded-rep-9c6ddf99a7/runs/real-agent-trace-evidence-ledger-with-anchored-bounded-rep-9c6ddf99a7-20260605T141735240647+0000
- Parent run decision: CPU-Only Agent Evidence Ledger with Bounded Replay: enoch://control-plane/projects/cpu-only-agent-evidence-ledger-with-bounded-replay-7b5fe4c8178e/runs/cpu-only-agent-evidence-ledger-with-bounded-replay-7b5fe4c8178e-20260605T102444602388+0000

## What looked useful

Durable ledger replay is viable for exact restart persistence on heterogeneous real agent trace records, and snapshots reduced mean recovery replay work from 163.56 to 38.99 events with 360/360 paired improvements at a 16-event interval. A volatile no-recovery ablation failed 0/360, confirming persistence is necessary. The result is useful engineering evidence but not paper-ready.

## Boundaries and scale limits

The validation used an offline replay harness over existing JSONL traces, not live LangGraph/Codex process crash-restart, concurrent writers, long production workflows, or idempotent external side-effect replay. Logs were small enough that full raw-log replay was also correct and sometimes faster in wall-clock latency.

## Claim scope

On 120 local real Codex/Enoch JSONL agent traces with 7,938 total events, fixed seeds 101/202/303, and five deterministic injected restarts per trace, a SQLite WAL event ledger with periodic snapshots recovered the exact canonical final replay state in 360/360 runs and reduced recovery replay work versus a no-snapshot durable ledger when the snapshot interval was calibrated to 16 events.

## Why it stopped

Medium local replay evidence supports the restart-persistence mechanism, but the raw replay baseline remains competitive on small traces and the harness does not validate live process restarts or production-scale side effects.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded deepening test should run live agent workflows with OS-level crash injection and side-effect idempotence checks before any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Agent Crash-Restart Ledger Replay with Idempotent Side Effects
- Success threshold: Durable snapshot ledger recovers exact state and side-effect ledger invariants in at least 29/30 live crash-restart runs, volatile control fails under crashes, and snapshot recovery replays less than 25 percent of processed events on average without more than 2x append overhead versus raw logging.
- Stop condition: Stop if any durable recovery produces a mismatched final state, duplicates a side effect, or snapshot replay work is not materially lower than no-snapshot/full replay on live traces.

## Evidence references

- Artifact root: `<local-path>/projects/heterogeneous-real-agent-trace-ledger-replay-with-restart-e01dae3a71`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
