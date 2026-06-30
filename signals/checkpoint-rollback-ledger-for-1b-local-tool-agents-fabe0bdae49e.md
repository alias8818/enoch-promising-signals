# Checkpoint-Rollback Ledger for 1B Local Tool Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `checkpoint-rollback-ledger-for-1b-local-tool-agents-fabe0bdae49e`
Run ID: `checkpoint-rollback-ledger-for-1b-local-tool-agents-fabe0bdae49e-20260530T023543421316+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/36b9f72c1481

## What looked useful

The ledger correctly recovered and rolled back all checked states and reduced storage 31.9-36.1% for long-lived active-agent workloads, but regressed by 11.4-19.0% on sparse/cold 100k-agent workloads because creation/checkpoint overhead dominates short histories.

## Boundaries and scale limits

Tested up to 100,000 agent IDs, 86,259 active agents, and 200,000 mutation steps. Did not test real LLM tool traces, disk durability, fsync, crash restart, concurrent writers, compaction, or a true 1B-agent deployment.

## Claim scope

Synthetic single-process Python benchmark of an in-memory per-agent checkpoint/delta ledger versus compressed full per-step snapshots for local tool-agent-like key/value state.

## Why it stopped

Mixed synthetic evidence: the mechanism works for long-lived agents but a proxy sparse/cold workload falsifies the broad 1B-local-agent storage-efficiency claim without a better cold-agent encoding.

## Recommended next action

Stop this run as no-paper useful signal; next run should implement cold-agent optimized creation records and durable append-log recovery, then rerun the sparse 100k workload against full snapshots.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cold-Agent Optimized Durable Checkpoint Ledger
- Success threshold: On the 100k sparse/cold workload, ledger storage must be <= full-snapshot storage while all recovery and rollback checks pass; on long-lived workloads, storage reduction must remain >=25% with P95 rollback under 1 ms locally.
- Stop condition: Stop if cold-agent optimized durable encoding still uses more bytes than full snapshots on the sparse 100k workload or fails any restart recovery correctness check.

## Evidence references

- Artifact root: `<local-path>/projects/checkpoint-rollback-ledger-for-1b-local-tool-agents-fabe0bdae49e`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
