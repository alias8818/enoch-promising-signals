# Agent Evidence Ledger with Hash-Chained Step Records on GB10

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `agent-evidence-ledger-with-hash-chained-step-records-on-gb10-ece334c03ac9`
Run ID: `agent-evidence-ledger-with-hash-chained-step-records-on-gb10-ece334c03ac9-20260621T144632083953+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/66dd9f608611

## What looked useful

Hash-chained step records are cheap and useful as local integrity/continuity checks, but hash chaining alone is insufficient for adversarial evidence ledgers because a ledger rewrite with recomputed suffix hashes verifies cleanly.

## Boundaries and scale limits

The run used 100000 synthetic records with 512-byte payload bodies in one CPU process. It did not test real multi-agent traces, concurrent writers, crash recovery, secure timestamps, signed tips, external anchoring, or long retention. A full suffix rewrite with recomputed hashes passed verification.

## Claim scope

On deterministic synthetic agent-step JSONL records on this GB10 host, a simple SHA-256 hash chain detects naive payload edits and deleted-line continuity breaks at about 105k verified records/s, with about 1.10x generation overhead and 1.20x bench write overhead versus plain JSONL.

## Why it stopped

Proxy/local evidence supports the mechanism for non-adversarial integrity checking but directly falsifies any hash-chain-only tamper-evidence claim against actors able to rewrite and recompute ledger suffixes.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add signed or externally anchored ledger tips and rerun the same adversarial suffix-rewrite harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed or anchored tips for hash-chained agent evidence ledgers
- Success threshold: Suffix rewrite with recomputed hashes must fail verification against a previously signed or externally anchored tip, while end-to-end write throughput remains at least 7500 records/s for 100000 512-byte records on this host.
- Stop condition: Stop if anchored verification still accepts rewritten history, or if anchoring drops bounded throughput below 5000 records/s without a clear batching remedy.

## Evidence references

- Artifact root: `<local-path>/projects/agent-evidence-ledger-with-hash-chained-step-records-on-gb10-ece334c03ac9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
