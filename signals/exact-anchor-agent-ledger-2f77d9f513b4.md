# Exact-Anchor Agent Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `exact-anchor-agent-ledger-2f77d9f513b4`
Run ID: `exact-anchor-agent-ledger-2f77d9f513b4-20260607T234045573302+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/de208cd5fa47

## What looked useful

Exact anchors provide a strong local integrity mechanism for agent evidence ledgers compared with plain and offset-only logs, but an unsealed chain needs a committed manifest to close tail-truncation misses.

## Boundaries and scale limits

Synthetic documents and tamper scenarios only; no real multi-agent traces, concurrent writers, signed storage, production append-only substrate, adversarial rewriting, or human audit study. CPU-only local run completed in 28.81s with 27 MB max RSS.

## Claim scope

In a deterministic synthetic benchmark of 1,000 trials with 500-entry ledgers over generated source documents, byte-span anchors plus span hashes and hash-chain links detected source edits inside cited spans, claim tampering, and entry reordering at 100% with zero clean/outside-anchor false positives; unsealed hash-chain deletion detection was 99.9% because tail truncation can pass without an external head/count commitment.

## Why it stopped

Bounded synthetic mechanism evidence supports the core anchor idea but is not direct production or paper-grade validation, and it exposed a specific unsealed hash-chain tail-truncation limitation.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add a signed or append-only manifest committing to entry_count and head_hash, then rerun the same deletion/reorder/source-edit benchmark on synthetic and small real agent traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sealed Manifest Exact-Anchor Ledger
- Success threshold: Deletion, reorder, claim-tamper, and inside-anchor source-edit detection all equal 1.000; clean and outside-anchor false-positive rates equal 0.000; mean 500-entry verification latency remains below 5 ms.
- Stop condition: Stop if manifest sealing still misses deletion/truncation, introduces any clean/outside-anchor false positives in 1,000 trials, or pushes mean 500-entry verification above 5 ms without a clear implementation bug.

## Evidence references

- Artifact root: `<local-path>/projects/exact-anchor-agent-ledger-2f77d9f513b4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
