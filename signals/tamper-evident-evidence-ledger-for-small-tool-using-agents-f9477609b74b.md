# Tamper-Evident Evidence Ledger for Small Tool-Using Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tamper-evident-evidence-ledger-for-small-tool-using-agents-f9477609b74b`
Run ID: `tamper-evident-evidence-ledger-for-small-tool-using-agents-f9477609b74b-20260525T214530501498+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/e67dcf88cc54

## What looked useful

Anchored ledgers detected 100% of tested tampering while adding about 21.9 microseconds append time, 18.9 microseconds verification time, and 1.88x storage per event in unoptimized Python. The no-anchor condition failed to detect tail truncation, showing that checkpoint custody is essential.

## Boundaries and scale limits

Synthetic events only; no live agent framework integration; no comparison to production transparency logs; no tests for key compromise, process compromise, checkpoint loss, concurrent writers, or distributed anchoring. Results support a local mechanism, not a publication-grade security system.

## Claim scope

In a deterministic synthetic benchmark of 1000 small tool-agent traces with 128 events each, a canonical JSON hash-chain plus per-row HMAC and an out-of-band final anchor detected all tested non-colluding tamper attacks: body mutation, hash mutation, event deletion, adjacent reordering, and tail truncation.

## Why it stopped

Bounded synthetic evidence supports the mechanism but is insufficient for a paper or broad security claim.

## Recommended next action

Stop this run as no-paper useful signal; next run should integrate the ledger into a real small tool-using agent harness and compare against a plain audit-log baseline under live trace tampering.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Live Agent Evidence Ledger With Baseline Audit Log Comparison
- Success threshold: Anchored ledger detects at least 99% of injected live-trace tampering attacks, plain JSONL detects no cryptographic tampering without external metadata, p95 append overhead stays below 1 ms per event, and the missing-anchor control demonstrates expected truncation weakness.
- Stop condition: Stop if live integration requires privileged/private services unavailable locally, p95 append overhead exceeds 10 ms per event in a minimal implementation, or anchored verification misses any non-colluding mutation/deletion/reorder attack other than explicitly modeled checkpoint loss.

## Evidence references

- Artifact root: `<local-path>/projects/tamper-evident-evidence-ledger-for-small-tool-using-agents-f9477609b74b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
