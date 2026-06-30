# Cryptographic Evidence Ledger for Agent Tool Calls

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cryptographic-evidence-ledger-for-agent-tool-calls-d9ae2dca1f70`
Run ID: `cryptographic-evidence-ledger-for-agent-tool-calls-d9ae2dca1f70-20260630T114733882392+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/98942fa828f9

## What looked useful

The mechanism is practical enough for local agent tool-call logging and catches common interior log mutations, but append-only evidence is incomplete without external anchoring. The benchmark also quantifies a roughly 2.2x serialized size overhead and 2.7x to 6.4x append slowdown versus plain canonical JSONL serialization.

## Boundaries and scale limits

Evidence is synthetic and local only. It does not cover real agent runtimes, concurrent writers, fsync durability, key compromise, public verification, key rotation, transparency-log gossip, remote timestamping, or large production audit stores. Suffix truncation is not detected unless the verifier has an external expected count/final digest or equivalent anchor.

## Claim scope

A standard-library prototype using canonical JSON, SHA-256, HMAC-SHA256 hash chaining, and periodic Merkle-style checkpoints detected body tampering, middle deletion, insertion, reordering, and checkpoint tampering on synthetic agent tool-call ledgers up to 50,000 events, with median append throughput from 47,216 to 111,446 events/s and verify throughput from 54,165 to 122,225 events/s.

## Why it stopped

Synthetic local evidence supports the mechanism but also shows that unanchored suffix truncation passes verification, so the ledger alone cannot justify an append-only evidence claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the ledger with a real agent tool-call wrapper and an external final-digest anchor, then replay storage-compromise attacks against captured traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Evidence Ledger on Real Agent Tool Traces
- Success threshold: All replayed attacks, including suffix truncation, are detected with the external anchor; median append throughput remains at or above 10,000 events/s on 10,000 or more real/replayable events.
- Stop condition: Stop if suffix truncation is not detected with the external anchor, if durable append throughput drops below 1,000 events/s, or if no real/replayable tool-call trace can be produced locally.

## Evidence references

- Artifact root: `<local-path>/projects/cryptographic-evidence-ledger-for-agent-tool-calls-d9ae2dca1f70`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
