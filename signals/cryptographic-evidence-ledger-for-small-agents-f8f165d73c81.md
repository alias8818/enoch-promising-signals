# Cryptographic Evidence Ledger for Small Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cryptographic-evidence-ledger-for-small-agents-f8f165d73c81`
Run ID: `cryptographic-evidence-ledger-for-small-agents-f8f165d73c81-20260607T135205367284+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/a62e72f4c9fb

## What looked useful

The mechanism appears practical for small local agents: signed hash-chained records have sub-0.1 ms mean append latency and deterministic detection for payload modification, deletion, reordering, unsigned forgery, and checkpoint-detected truncation in this prototype.

## Boundaries and scale limits

Not tested on real agent traces, multiple agents, remote timestamping or anchoring, key rotation, crash recovery, partial-write recovery, concurrent writers, or signing-key compromise. The result is a bounded prototype benchmark, not a publication-grade system validation.

## Claim scope

On one local CPU process with synthetic 512-byte tool-result payloads, a canonical JSON SHA-256 hash chain with periodic Merkle checkpoints and Ed25519 signatures sustained about 10,219 signed appends/s, verified about 5,067 records/s, added about 385 JSONL bytes/record versus baseline logging, and rejected 5/5 scripted tamper cases.

## Why it stopped

Closed as no-paper useful signal because the evidence is synthetic/local and does not validate multi-agent or operational audit settings.

## Recommended next action

Run a bounded real-trace follow-up with crash-consistency, key-rotation, and remote checkpoint anchoring tests before considering a paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-trace crash-safe evidence ledger for small agents
- Success threshold: Signed ledger p95 append latency below 1 ms, storage overhead below 2x baseline JSONL, 100% detection of scripted tampering after recovery, and no committed-record loss across crash injection.
- Stop condition: Stop if signed append p95 exceeds 5 ms on real traces, recovery loses committed records, or any scripted tamper case is accepted.

## Evidence references

- Artifact root: `<local-path>/projects/cryptographic-evidence-ledger-for-small-agents-f8f165d73c81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
