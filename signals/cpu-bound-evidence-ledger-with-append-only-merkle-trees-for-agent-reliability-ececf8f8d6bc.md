# CPU-bound evidence ledger with append-only merkle trees for agent reliability

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `cpu-bound-evidence-ledger-with-append-only-merkle-trees-for-agent-reliability-ececf8f8d6bc`
Run ID: `cpu-bound-evidence-ledger-with-append-only-merkle-trees-for-agent-reliability-ececf8f8d6bc-20260605T140438459761+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/205a2aa29d04

## What looked useful

Merkle evidence ledgers are locally plausible for agent harness logging: they add about 15.649 us/event over serialization-only logging at 100k x 512-byte-target records and produce small logarithmic proofs. This supports a real-harness follow-up but not a paper claim.

## Boundaries and scale limits

Synthetic records only; single Python process; no production disk fsync, no concurrent writers, no crash recovery protocol, no remote verifier, no adversarial operational tests, and no direct measurement of real agent reliability improvement.

## Claim scope

On a single CPU worker using deterministic synthetic agent evidence records, append-only Merkle commitments and checkpoint inclusion proofs are practical at 100,000-event scale: Merkle append median 29.588 us/event, 33,797 events/s, proof generation 9.918 us/proof, proof verification 34.994 us/proof, and mutation detection succeeded.

## Why it stopped

Bounded synthetic CPU evidence supports mechanism practicality but is not direct production or reliability evidence, so it should not be advanced to paper writing.

## Recommended next action

Stop this run as no-paper useful signal; next run should test the same ledger inside a real agent harness with disk durability, concurrent appenders, restart recovery, and verifier checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-harness Merkle evidence ledger durability and verifier benchmark
- Success threshold: Merkle ledger overhead under 10% of baseline harness runtime or under 100 us/event p95, all sampled proofs verify, all tampered records are rejected, and restart recovery preserves the committed prefix root.
- Stop condition: Stop if durable Merkle logging exceeds 25% runtime overhead or loses/reorders committed events after restart in a reproducible local harness test.

## Evidence references

- Artifact root: `<local-path>/projects/cpu-bound-evidence-ledger-with-append-only-merkle-trees-for-agent-reliability-ececf8f8d6bc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
