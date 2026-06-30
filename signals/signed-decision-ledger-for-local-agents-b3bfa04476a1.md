# Signed Decision Ledger for Local Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `signed-decision-ledger-for-local-agents-b3bfa04476a1`
Run ID: `signed-decision-ledger-for-local-agents-b3bfa04476a1-20260628T205431145849+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9213839e1be7

## What looked useful

The mechanism is practical for local logging but incomplete as a standalone security claim: tail truncation is accepted without a trusted head/length checkpoint, and identity spoof appends are accepted without a trusted agent-id to public-key registry.

## Boundaries and scale limits

Synthetic local 10k-entry CPU-only probe only; no real agent integration, concurrent writer test, crash recovery, durable fsync benchmark, key rotation, hardware-backed keys, or distributed checkpoint publication was tested.

## Claim scope

A local Python Ed25519 hash-chained decision ledger with 10,000 synthetic entries and 4 simulated agents can verify cleanly, detect payload mutation, middle deletion, reordering, and unsigned identity mutation, and run at about 32.9k signed appends/s and 17.5k verified entries/s on this host.

## Why it stopped

Bounded local evidence supports a useful mechanism but falsifies the standalone signed-ledger framing: checkpointing and key-registry trust anchors are required.

## Recommended next action

Do not write a paper from this run; deepen with a real local-agent integration that persists trusted checkpoints and an agent-key registry, then tests crash/replay and concurrent append behavior.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Checkpointed Agent-Key Registry Ledger in a Real Local Agent Loop
- Success threshold: Across at least 10,000 real decision records, all mutation, rollback, identity-spoof, crash-replay, and concurrent append fault injections are rejected or recovered without ledger corruption, while durable append overhead remains below 50 ms per decision at p95.
- Stop condition: Stop if checkpoint or registry persistence cannot reject rollback and identity spoofing, or if durable append p95 exceeds 50 ms per decision in the target local-agent loop.

## Evidence references

- Artifact root: `<local-path>/projects/signed-decision-ledger-for-local-agents-b3bfa04476a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
