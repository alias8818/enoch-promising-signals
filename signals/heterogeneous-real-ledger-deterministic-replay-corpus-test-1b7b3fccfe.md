# Heterogeneous Real-Ledger Deterministic Replay Corpus Test

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `heterogeneous-real-ledger-deterministic-replay-corpus-test-1b7b3fccfe`
Run ID: `heterogeneous-real-ledger-deterministic-replay-corpus-test-1b7b3fccfe-20260522T101304328718+0000`

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

- Parent run decision: Deterministic Harness for Agent Ledger Consistency: enoch://control-plane/projects/deterministic-harness-for-agent-ledger-consistency-6a6e7ba6f5c8/runs/deterministic-harness-for-agent-ledger-consistency-6a6e7ba6f5c8-20260522T073734083060+0000
- Parent run decision: Deterministic Replay Adapter for a Real Agent Ledger: enoch://control-plane/projects/deterministic-replay-adapter-for-a-real-agent-ledger-afde7186f2/runs/deterministic-replay-adapter-for-a-real-agent-ledger-afde7186f2-20260522T092004428790+0000

## What looked useful

Canonical sorted replay was stable in 20/20 perturbation trials on the full seed and both partial replication seeds, while naive JSON and no-sort ablations had 0/20 matches and 21 unique digests including the original in each evaluated run.

## Boundaries and scale limits

Primary direct run used 15 real ledger units, 390 replay events, and 20 perturbation trials. Two additional seeds were partial because Solana public RPC slowed before completing all five slots. The replay covers sampled transaction identifiers/values and block metadata, not full ledger-native state execution.

## Claim scope

A small-to-medium corpus of real Bitcoin, Ethereum, and Solana ledger records can be normalized into a canonical event stream whose replay digest is stable under record-order and JSON-key-order perturbations; naive raw JSON serialization and no-sort replay controls are unstable.

## Why it stopped

Mechanism support was obtained, but the evidence is limited to canonical corpus digest determinism over sampled real-ledger records and is not publication-grade validation of heterogeneous deterministic ledger replay.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should use reliable archival data sources and full transaction payloads over at least 100 finalized units per ledger with ledger-native consistency checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Full-Payload Heterogeneous Ledger Replay Consistency Test
- Success threshold: Canonical full-payload replay has exactly one digest across at least 50 perturbation trials for every ledger and all ledger-native commitment checks pass, while naive/no-sort controls change digest in at least 95% of perturbation trials.
- Stop condition: Stop if full-payload canonical replay becomes unstable on any ledger, if ledger-native commitment checks cannot be reproduced from the corpus, or if data acquisition requires private/non-reproducible access.

## Evidence references

- Artifact root: `<local-path>/projects/heterogeneous-real-ledger-deterministic-replay-corpus-test-1b7b3fccfe`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
