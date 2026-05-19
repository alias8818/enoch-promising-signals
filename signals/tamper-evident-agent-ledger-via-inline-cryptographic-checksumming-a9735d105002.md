# Tamper-Evident Agent Ledger via Inline Cryptographic Checksumming

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `tamper-evident-agent-ledger-via-inline-cryptographic-checksumming-a9735d105002`
Run ID: `tamper-evident-agent-ledger-via-inline-cryptographic-checksumming-a9735d105002-20260515T211459496395+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/49b2b878513b

## What looked useful

Inline checksum chains are practical at this scale, with median write overhead from about 1.13x to 1.99x depending on payload size and digest type, but local-only verification misses valid-prefix truncation and rewritten valid chains. External anchoring is required for the broad tamper-evident claim.

## Boundaries and scale limits

Synthetic events only; Python stdlib implementation; single-process local filesystem; no real agent runtime, concurrent writers, crash recovery, log rotation, distributed storage, remote notarization, or production key-management validation.

## Claim scope

Local synthetic JSONL agent-ledger experiment: inline SHA-256 or HMAC-SHA256 hash chaining detects midstream row edits, insertions, deletions, and reordering; with an external expected final head/count it also detects tail truncation and full-chain rewrites.

## Why it stopped

Proxy/local evidence supports the mechanism only with external anchoring and directly falsifies the broad inline-only tamper-evidence claim for tail truncation and full-chain rewrite attacks.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should integrate anchored HMAC/signature checkpoints into a real agent runtime and verify crash, rotation, and concurrent-writer behavior.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored HMAC Checkpoints in a Real Agent Runtime
- Success threshold: Detect all specified tamper modes in anchored verification with zero false accepts over at least 1 million real or trace-replayed events, while maintaining p95 write overhead below 2x versus plain JSONL.
- Stop condition: Stop if anchored verification misses any specified tamper mode, produces unrecoverable false rejects after normal crash/restart or rotation, or p95 write overhead exceeds 2x after straightforward implementation tuning.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-agent-ledger-via-inline-cryptographic-checksumming-a9735d105002`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
