# Sharded evidence ledger with raw blob retention and replay audit

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `sharded-evidence-ledger-with-raw-blob-retention-and-replay-ddc426cffa`
Run ID: `sharded-evidence-ledger-with-raw-blob-retention-and-replay-ddc426cffa-20260530T015913334912+0000`

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

- Parent run decision: Evidence ledger for 100M-agent tool-use cascade: enoch://control-plane/projects/evidence-ledger-for-100m-agent-tool-use-cascade-e0175498bcda/runs/evidence-ledger-for-100m-agent-tool-use-cascade-e0175498bcda-20260529T224504311518+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3ff0a491742f

## What looked useful

Raw blob retention materially changes replay audit power: the raw-retained ledger matched the expected final state hash and detected 3/3 injected tamper controls, while metadata-only records lacked raw blob references and failed the raw replay requirement.

## Boundaries and scale limits

Single process, local filesystem, synthetic fixed-size blobs, no concurrent writers, no crash/restart injection, no distributed/object-store semantics, no long retention period, and no production authorization or operator workflow testing.

## Claim scope

In a controlled local synthetic test with 5,000 events, 8 shards, and 10.24 MB of payloads, a raw-retaining sharded append ledger deterministically replayed the final evidence state and detected blob corruption, blob deletion, and within-shard record reordering; a metadata-only control could replay hashes but could not satisfy raw replay audit requirements.

## Why it stopped

Tier 1 direct mechanism test succeeded, but evidence is synthetic and local-only, so it is useful no-paper evidence rather than publication-grade validation.

## Recommended next action

Run a bounded crash/concurrency follow-up with multiple append workers, injected process kills or partial-write faults, and replay verification that accepted records retain rehashable raw bytes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-concurrent replay audit for raw-retained sharded evidence ledger
- Success threshold: Across at least 50,000 attempted appends and 20 injected crash/partial-write events, replay must complete with zero accepted records missing matching raw blobs and must detect 100% of explicit tamper controls.
- Stop condition: Stop early if any accepted record replays without its matching raw blob, if replay cannot distinguish partial writes from committed records, or if any explicit tamper control is not detected.

## Evidence references

- Artifact root: `<local-path>/projects/sharded-evidence-ledger-with-raw-blob-retention-and-replay-ddc426cffa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
