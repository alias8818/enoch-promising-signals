# Evidence Ledger: Small Agent Action Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `evidence-ledger-small-agent-action-verification-de3fd724297b`
Run ID: `evidence-ledger-small-agent-action-verification-de3fd724297b-20260609T024512164157+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/480fb0c46c7f

## What looked useful

Authenticated per-record evidence ledgers add tamper-detection capability over plain logs for forged record edits, but unanchored hash chains miss tail truncation. A small terminal anchor closed that gap with negligible extra time and 181 bytes of anchor metadata in this benchmark.

## Boundaries and scale limits

Synthetic traces only; no real agent workloads, compromised-key adversaries, concurrent writers, distributed append-only storage, hardware attestation, or high-throughput production validation were tested.

## Claim scope

On deterministic synthetic small-agent traces with 2,000 records and 50 trials per attack class, an HMAC-authenticated hash-chain evidence ledger detected forged internally consistent record edits that a plain JSON verifier accepted; a terminal final-hash/count anchor was required to detect suffix deletion.

## Why it stopped

Bounded synthetic evidence supports a mechanism and a design requirement, but not a publication-grade or real-world validation.

## Recommended next action

Stop this run as no-paper useful signal; next, deepen with real small-agent traces and a signed append-only-log baseline using anchored checkpoints.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored evidence ledger on real small-agent traces
- Success threshold: Anchored ledger detects at least 95% of injected tamper attacks including suffix truncation, has zero false positives on clean traces, and keeps storage overhead under 3x and verification under 100 ms per 10,000 records on local CPU.
- Stop condition: Stop if the anchored ledger misses suffix truncation/checkpoint replay under the stated threat model, produces false positives on clean traces, or exceeds the overhead threshold without a compensating detection advantage over the signed append-only baseline.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-small-agent-action-verification-de3fd724297b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
