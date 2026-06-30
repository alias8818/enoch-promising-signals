# Online exact-anchor ledger tailing across live small-agent tool events

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `online-exact-anchor-ledger-tailing-across-live-small-agent-579cfa14f1`
Run ID: `online-exact-anchor-ledger-tailing-across-live-small-agent-579cfa14f1-20260528T072031145547+0000`

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

- Parent run decision: Exact-anchor ledger on real small-agent traces: enoch://control-plane/projects/exact-anchor-ledger-on-real-small-agent-traces-062e6318fb/runs/exact-anchor-ledger-on-real-small-agent-traces-062e6318fb-20260528T034503278129+0000
- Parent run decision: Exact-Anchor Ledger for Small-Agent Tool Calls: enoch://control-plane/projects/exact-anchor-ledger-for-small-agent-tool-calls-ad63afd98676/runs/exact-anchor-ledger-for-small-agent-tool-calls-ad63afd98676-20260528T012713250114+0000

## What looked useful

Across 20,000 events and five fixed seeds, exact-anchor ledger tailing achieved 1.0 mean recall with 0 missed events, 0 duplicates, 0 false positives, p95 latency 10 poll ticks, and 1 detected corruption per seed. Active-file offset baseline averaged 0.97905 recall and timestamp-watermark baseline averaged 0.91330 recall. The offset-no-hash ablation recovered events but detected 0 corruptions.

## Boundaries and scale limits

Synthetic event distributions only; no captured production agent traces, no real collector baselines such as Fluent Bit/vector/journald, no multi-host clocks, no network filesystem, no compressed rotation, and no crash/restart persistence test beyond in-process polling.

## Claim scope

In a fixed-seed, live-filesystem JSONL simulation of small-agent tool events with partial writes, periodic polling, log rotation, and one injected post-hoc corruption per seed, exact byte/file-identity anchors plus content hashes recovered all events with no duplicates or false positives and detected each injected corruption.

## Why it stopped

Tier 2 synthetic/live-filesystem evidence supports the scoped mechanism but is not publication-grade because real agent traces and real collector baselines were not tested.

## Recommended next action

Stop for this run; the result is useful no-paper mechanism evidence. A bounded deepen follow-up should test captured live agent traces with real collector baselines and restart/crash persistence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact-anchor ledger tailing on captured agent traces and real collector baselines
- Success threshold: Exact-anchor ledger tailing reaches >=99.99% recall, zero duplicates, zero false positives, and detects all injected corruptions while every baseline loses events, duplicates events, or misses at least one corruption on the same traces.
- Stop condition: Stop if exact-anchor recall falls below 99.99%, duplicates or false positives appear, corruption detection misses any injected divergence, or real collector baselines match exact-anchor recovery and integrity under the same restart/rotation conditions.

## Evidence references

- Artifact root: `<local-path>/projects/online-exact-anchor-ledger-tailing-across-live-small-agent-579cfa14f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
