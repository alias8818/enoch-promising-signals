# Rolling-Checksum Evidence Ledger for Tiny Local Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `rolling-checksum-evidence-ledger-for-tiny-local-agents-9c06c24647ed`
Run ID: `rolling-checksum-evidence-ledger-for-tiny-local-agents-9c06c24647ed-20260607T155436544199+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/74bd16827ba8

## What looked useful

CRC32 rolling chains were about 1.7x faster than SHA-256 chains at 100,000 events, but a final CRC32 digest collision was found after 144,679 sampled 8-event ledgers, while SHA-256 chain digests differed.

## Boundaries and scale limits

Synthetic fixed-size random events only; CRC32 representative only; no real agent traces, no adaptive attacker beyond final-state ambiguity, and no evaluation of hybrid cryptographic checkpoint designs.

## Claim scope

A CRC32 rolling-chain final digest for synthetic tiny-agent-like event ledgers is low-overhead but not viable as a standalone tamper-evident evidence root because distinct 8-event ledgers reached the same final checksum in a bounded local collision search.

## Why it stopped

No-paper early falsification of the standalone rolling-checksum ledger as a tamper-evident evidence root; this is a bounded synthetic/proxy result, not full validation of all possible hybrid ledger designs.

## Recommended next action

Stop the standalone rolling-checksum evidence-root idea; run a bounded hybrid-ledger follow-up with rolling checksums for chunk repair plus periodic SHA-256/HMAC anchors against edit/delete/reorder attacks on real tiny-agent traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Hybrid rolling-checksum plus cryptographic-anchor ledger for tiny local agents
- Success threshold: Hybrid ledger detects 100% of scripted edit/delete/insert/reorder attacks between anchors while reducing local repair or resynchronization work by at least 25% versus a pure SHA-256 chain on the same traces.
- Stop condition: Stop if cryptographic anchors erase the overhead benefit or if attacks between anchors cannot be localized without replaying the same amount of data as the SHA-256 baseline.

## Evidence references

- Artifact root: `<local-path>/projects/rolling-checksum-evidence-ledger-for-tiny-local-agents-9c06c24647ed`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
