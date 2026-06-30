# Cryptographic Evidence Ledger for Agent Claims

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cryptographic-evidence-ledger-for-agent-claims-f2e39ac22977`
Run ID: `cryptographic-evidence-ledger-for-agent-claims-f2e39ac22977-20260613T100821989066+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/274266e08693

## What looked useful

Across 6 benchmark trials, all clean signed ledgers verified, all clean unsigned hash-chain ledgers verified, and 30/30 tamper probes were rejected. Median signed append throughput was 31,288 records/s, median signed verify throughput was 18,247 records/s, and median signed record size was 977 bytes.

## Boundaries and scale limits

Synthetic in-memory claims only; no real agent traces, persistent append-only storage, crash recovery, concurrent writers, key rotation, external timestamping, fork/equivocation handling, or million-record scale were tested.

## Claim scope

A single-writer local append-only ledger using canonical JSON, SHA-256 record hashes, hash chaining, Merkle batch roots, and Ed25519 signatures can verify clean synthetic agent-claim ledgers and reject tested tamper classes up to 5,000 records with about 31k signed appends/s and 18k signed verifies/s on this host.

## Why it stopped

No-paper useful signal: the synthetic local probe supports the mechanism, but publication-grade claims require real traces and persistence/concurrency/adversarial validation.

## Recommended next action

Run a bounded deepen study that persists the ledger to disk, uses real agent execution traces, and tests crash recovery, concurrent writers, key rotation, and fork detection against JSONL and database audit-log baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Persistent Multi-Writer Evidence Ledger on Real Agent Traces
- Success threshold: On at least 100,000 real or replayed claims, reject all injected tamper/fork/crash-corruption cases, recover a valid prefix after forced termination, and keep median append throughput within 5x of JSONL with signed verification above 5,000 records/s.
- Stop condition: Stop if persistence or multi-writer semantics allow an injected mutation, fork, or crash-corrupted suffix to verify as valid, or if append throughput falls below 1,000 records/s before reaching 100,000 claims.

## Evidence references

- Artifact root: `<local-path>/projects/cryptographic-evidence-ledger-for-agent-claims-f2e39ac22977`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
