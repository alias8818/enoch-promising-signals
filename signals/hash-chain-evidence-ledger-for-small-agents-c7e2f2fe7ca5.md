# Hash-chain evidence ledger for small agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `hash-chain-evidence-ledger-for-small-agents-c7e2f2fe7ca5`
Run ID: `hash-chain-evidence-ledger-for-small-agents-c7e2f2fe7ca5-20260602T205920905641+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/4174e93ed6b9

## What looked useful

For 20,000 events with 1 KiB payloads, global and per-agent chains wrote at about 5.5k events/s with about 1.02x slowdown and 1.13-1.14x byte overhead versus raw JSONL. For 50,000 metadata-only events, hash-chain writes were about 164k-166k events/s with about 2.0x slowdown and 1.82-1.85x byte overhead. Unanchored global chains detected corrupt payloads, middle deletion, and reordering, but not tail truncation.

## Boundaries and scale limits

Synthetic single-process local-file tests only; no fsync durability stress, crash injection, external trusted anchoring, real agent traces, concurrent writers, signatures, or distributed consensus. Tail truncation is missed without an external expected count/head/checkpoint anchor, and per-agent chains miss cross-agent order-only changes without a global anchor.

## Claim scope

Local synthetic benchmarks show that raw JSONL evidence logs can be upgraded to global or per-agent SHA-256 hash-chain ledgers with practical overhead for small-agent event volumes, and that hash chains detect internal record corruption, middle deletion, and chain-order tampering when verified.

## Why it stopped

Closed as no-paper useful signal: local synthetic evidence supports mechanism viability, but paper-grade claims require real traces, durability testing, adversarial anchoring, and stronger baselines.

## Recommended next action

Run a bounded deepen experiment that adds external head anchoring plus crash-recovery/fsync testing and compares against a signed SQLite append-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored crash-safe hash-chain ledger for small agents
- Success threshold: With four concurrent small-agent writers and 1 KiB evidence records, anchored hash-chain logging detects all post-checkpoint tamper probes and keeps p95 append latency under 25 ms with fsync batching, with no more than 2x storage overhead versus raw JSONL.
- Stop condition: Stop if crash recovery loses acknowledged events, if post-checkpoint tail truncation is not detected, or if p95 append latency exceeds 25 ms under fsync batching for the target trace.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chain-evidence-ledger-for-small-agents-c7e2f2fe7ca5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
