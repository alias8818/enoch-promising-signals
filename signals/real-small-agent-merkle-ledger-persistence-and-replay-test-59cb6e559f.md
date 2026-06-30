# Real small-agent Merkle ledger persistence and replay test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-small-agent-merkle-ledger-persistence-and-replay-test-59cb6e559f`
Run ID: `real-small-agent-merkle-ledger-persistence-and-replay-test-59cb6e559f-20260604T164311104981+0000`

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

- Parent run decision: Merkle-ledger agent state commitment for small local models: enoch://control-plane/projects/merkle-ledger-agent-state-commitment-for-small-local-models-c3b1d0cffbb3/runs/merkle-ledger-agent-state-commitment-for-small-local-models-c3b1d0cffbb3-20260604T073333905585+0000
- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a88e0eff45b3

## What looked useful

Tier 1 direct mechanism test passed: 5 clean ledgers replayed successfully and 25/25 injected corruption cases were detected. Median write throughput was 2717 events/s with fsync per event; median replay throughput was 119068 events/s.

## Boundaries and scale limits

Single-process Python harness only; no concurrent writers, no distributed consensus, no adversarial key management, no crash during partial write beyond truncation, no production agent trace, and no long-horizon durability or storage-failure study.

## Claim scope

In a local deterministic small-agent harness, an append-only JSONL Merkle ledger with a trusted manifest persisted 5 x 1000 state transitions, replayed them to identical terminal Merkle roots and state hashes, and detected payload mutation, parent-root mutation, event-order mutation, last-event truncation, and full rechain-without-manifest mutation.

## Why it stopped

Tier 1 direct validation supports the persistence/replay mechanism but is too small and controlled for publication readiness.

## Recommended next action

Stop this run as no-paper useful signal; next run should deepen with concurrent small agents, crash-at-random-byte recovery, and an external signed checkpoint manifest.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Concurrent small-agent Merkle ledger crash-recovery test
- Success threshold: 100/100 crash-recovery attempts replay to the last fully fsynced checkpoint with no undetected corruption and median recovery latency under 1 second for a 10000-event ledger.
- Stop condition: Stop if any corruption or ordering mutation is accepted as valid, if deterministic replay diverges after recovery, or if recovery semantics require manual intervention.

## Evidence references

- Artifact root: `<local-path>/projects/real-small-agent-merkle-ledger-persistence-and-replay-test-59cb6e559f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
