# Tamper-Evident Evidence Ledger for Small Tool Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tamper-evident-evidence-ledger-for-small-tool-agents-ea814a10fc40`
Run ID: `tamper-evident-evidence-ledger-for-small-tool-agents-ea814a10fc40-20260529T040413314394+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f91fc069d69e

## What looked useful

The first smoke test exposed that an unanchored hash chain misses tail truncation. Adding an authenticated final-hash/count manifest detected all 6/6 tested attacks while sustaining median 101,916 ledger events/s and 154,884 verification events/s, at 4.61x median write-time overhead and 2.23x median size overhead versus plain JSONL.

## Boundaries and scale limits

Synthetic events only; single-process CPU-only writer/verifier; no real agent trace corpus, concurrent writers, crash recovery, external notarization, remote adversary, key rotation, or distributed multi-agent validation.

## Claim scope

An authenticated final-hash/count manifest plus per-record canonical JSON, SHA-256 hash chaining, and HMAC-SHA256 detects six common post-hoc tampering operations on deterministic synthetic small tool-agent traces up to 100k events, with measured local CPU write and verification overhead.

## Why it stopped

No-paper useful signal: the local synthetic mechanism test supports viability but lacks real trace, persistence, and operational adversary evidence required for publication-grade claims.

## Recommended next action

Run a bounded deepen follow-up on real small-agent tool traces with crash/restart persistence and an external anchoring baseline before considering a paper.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Trace Persistence Test for Anchored Tool-Agent Evidence Ledgers
- Success threshold: Detect 100% of specified attacks across all real/replayed traces after crash/restart, with median write-time overhead under 5x and median storage overhead under 2.5x versus plain JSONL.
- Stop condition: Stop as negative if any specified tamper class is accepted with a valid manifest, or if median write-time overhead is 5x or greater on real/replayed traces without a clear optimization path.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-evidence-ledger-for-small-tool-agents-ea814a10fc40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
