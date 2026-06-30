# Small Agent Swarm Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `small-agent-swarm-ledger-211bf132ef10`
Run ID: `small-agent-swarm-ledger-211bf132ef10-20260525T051133010319+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/fa784b59fdfb

## What looked useful

The small-swarm ledger mechanism is promising for low-latency coordination: it removed duplicate completions in all tested synthetic scenarios and improved mean efficiency versus gossip at 20 ms latency, but the advantage is latency-sensitive and not paper-ready without a live persistent-ledger harness.

## Boundaries and scale limits

Proxy-only local simulation; no live LLM agents, real tool side effects, persistent database durability, network partitions, adversarial agents, or human utility were tested. Latency sensitivity showed the ledger becomes slower than gossip once claim latency reaches about 25% of mean task duration.

## Claim scope

In a deterministic synthetic task-claim simulator for 2 to 12 agents, 50 to 100 tasks, delayed peer visibility, and 0 to 5% task failure probability, a linearizable claim ledger at 20 ms latency eliminated duplicate task completions and stayed within 10% of gossip makespan in all 48 tested scenario groups.

## Why it stopped

Stopped after bounded proxy validation: the mechanism has useful synthetic support, but this is not direct/full validation and cannot support a publication-grade claim.

## Recommended next action

Run a bounded live asyncio or process-based agent harness with SQLite-backed append-only claims, idempotency keys, crash/restart tests, and no-ledger/gossip controls before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live SQLite Ledger Harness for Small Agent Swarms
- Success threshold: Ledger reduces duplicate side effects by at least 90% versus gossip, completes all tasks after crash/restart recovery, and keeps median makespan within 10% of gossip for ledger latency below 10% of mean task duration.
- Stop condition: Stop as negative if duplicate reduction is below 50%, crash recovery loses or permanently strands tasks, or median makespan exceeds gossip by more than 25% in low-latency conditions.

## Evidence references

- Artifact root: `<local-path>/projects/small-agent-swarm-ledger-211bf132ef10`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
