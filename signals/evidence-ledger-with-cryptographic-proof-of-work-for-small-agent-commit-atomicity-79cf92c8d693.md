# Evidence ledger with cryptographic proof-of-work for small agent commit atomicity

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `evidence-ledger-with-cryptographic-proof-of-work-for-small-agent-commit-atomicity-79cf92c8d693`
Run ID: `evidence-ledger-with-cryptographic-proof-of-work-for-small-agent-commit-atomicity-79cf92c8d693-20260605T094124098892+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/205a2aa29d04

## What looked useful

PoW is orthogonal to commit atomicity in this bounded test. It adds verifiable work and latency, while all-or-nothing publication comes from the storage commit protocol.

## Boundaries and scale limits

Single-host local filesystem, one Python process, 2000 commit attempts, synthetic failure injection, difficulty 3 leading hex zeroes. Not a distributed consensus, object-store, malicious-hashpower, or power-loss storage validation.

## Claim scope

Local file-backed evidence ledger under synthetic small-agent commit failures: proof-of-work on entries did not improve commit atomicity; atomic temp-file, fsync, and rename publication eliminated malformed final records and hash-chain errors with or without proof-of-work.

## Why it stopped

Bounded local evidence directly falsified the core mechanism claim for this setting: naive append had identical malformed and chain-broken records with or without PoW, while atomic publication fixed them without needing PoW.

## Recommended next action

Stop treating PoW as an atomicity primitive; if continuing, test atomic publication with and without PoW admission control on a bounded distributed or object-store backend.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Distributed object-store atomic publication with optional PoW admission control
- Success threshold: Atomic backend protocol has zero malformed final records, zero duplicate published sequence numbers, and zero unrecoverable chain errors; PoW changes admission cost but not atomicity metrics.
- Stop condition: Stop if the backend cannot provide conditional publication or if PoW again has no effect on atomicity metrics while adding material latency.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-with-cryptographic-proof-of-work-for-small-agent-commit-atomicity-79cf92c8d693`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
