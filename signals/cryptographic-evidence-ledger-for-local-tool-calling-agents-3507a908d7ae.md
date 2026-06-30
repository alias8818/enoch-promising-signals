# Cryptographic Evidence Ledger for Local Tool-Calling Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cryptographic-evidence-ledger-for-local-tool-calling-agents-3507a908d7ae`
Run ID: `cryptographic-evidence-ledger-for-local-tool-calling-agents-3507a908d7ae-20260607T181027015996+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/98febe24a9fe

## What looked useful

Mechanism works for tamper evidence when a receipt is retained, including 100% detection in the tested tamper campaign with receipt anchoring. Tail truncation is missed without an external/retained receipt. Write overhead was 12.50x at 1k events, 14.65x at 10k, and 21.14x at 50k versus plain JSONL, exceeding the 10x low-overhead threshold.

## Boundaries and scale limits

Synthetic single-process CPU-only traces only; no real agent integration, concurrent writers, crash recovery, key isolation, key rotation, public transparency service, or adversarial signer compromise test.

## Claim scope

A local JSONL tool-call ledger using SHA-256 hash chaining, Ed25519 per-event signatures, Merkle checkpoints, and retained final receipts detects edits, middle deletions, reordering, and receipt-anchored tail truncation on synthetic traces up to 50,000 events, but the naive per-event-signature design is not low overhead versus plain JSONL.

## Why it stopped

Bounded synthetic evidence supports the tamper-evidence mechanism but falsifies the low-overhead claim for the naive per-event-signature prototype; this is not full validation on real agents.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should replace per-event Ed25519 with hash-chain records plus periodic or batch signatures and require under 3x write overhead with unchanged tamper detection.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Batch-Signed Agent Evidence Ledger Overhead Test
- Success threshold: 100% detection for the tested tamper campaign with retained receipts, tail truncation explicitly missed without receipts, median write overhead under 3x plain JSONL, and verification throughput above 10,000 events/s on at least 50,000 events.
- Stop condition: Stop if periodic/batch signing still exceeds 5x plain JSONL write overhead or fails any edit, deletion, reorder, or receipt-anchored truncation detection case.

## Evidence references

- Artifact root: `<local-path>/projects/cryptographic-evidence-ledger-for-local-tool-calling-agents-3507a908d7ae`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
