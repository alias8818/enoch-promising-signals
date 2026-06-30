# Evidence ledger for small local agents with hash rollback

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-for-small-local-agents-with-hash-rollback-285fb95e160d`
Run ID: `evidence-ledger-for-small-local-agents-with-hash-rollback-285fb95e160d-20260523T060034565690+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/01c8b93e0fc7

## What looked useful

The prototype passed 3/3 mechanism tests and repeated 10k-event benchmarks. Median ledger throughput was 92268 writes/s, mean append latency was 0.0107 ms/event, verification throughput was 223874 entries/s, rollback to 6000 retained entries took 0.0798 s, first-record tampering was detected, and storage overhead was 1.35x versus plain JSONL.

## Boundaries and scale limits

Evidence is limited to synthetic events, one Python process, local temporary files, in-memory checkpoint objects, and 10k-event traces. It does not validate real agent integration, crash/restart durability, concurrent writers, external checkpoint anchoring, privacy redaction, or adversarial deletion of both ledger and checkpoint state.

## Claim scope

A dependency-free JSONL SHA-256 hash-chain ledger can detect in-place tampering and roll back to named checkpoints for a 10k-event synthetic single-process local-agent trace with about 11 microseconds median-scale append latency and 1.35x storage overhead versus plain JSONL on this host.

## Why it stopped

No-paper useful signal: the current result supports the mechanism on a synthetic single-process trace, but it is not direct real-agent or durability evidence.

## Recommended next action

Run a bounded integration follow-up inside a real local agent loop with persisted external checkpoints, crash/restart recovery, and a SQLite WAL baseline before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-restart evidence ledger integration for a real local agent loop
- Success threshold: Across at least 50 real traces, detect 100% of injected in-place mutations and checkpoint-inconsistent truncations after restart, recover to the last checkpoint in under 1 second for 10k-event ledgers, and keep median append overhead under 10x a durable SQLite WAL baseline.
- Stop condition: Stop as negative if restart recovery loses checkpoint integrity, any injected tampering is accepted as valid, or median append overhead exceeds 10x the durable baseline on 10k-event traces.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-for-small-local-agents-with-hash-rollback-285fb95e160d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
