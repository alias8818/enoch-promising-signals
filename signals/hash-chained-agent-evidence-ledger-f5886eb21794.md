# Hash-Chained Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-agent-evidence-ledger-f5886eb21794`
Run ID: `hash-chained-agent-evidence-ledger-f5886eb21794-20260619T023702164677+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/18122a9b386e

## What looked useful

The mechanism is cheap and effective for local tamper evidence, with append throughput of 151900.82 events/s and verify throughput of 160126.34 events/s on 100000 synthetic events, but prefix truncation is undetectable without external head checkpointing.

## Boundaries and scale limits

Synthetic single-process traces only; no production agent logs, concurrent writers, signed checkpoints, remote transparency log, storage adversary, or baseline runtime integration were tested.

## Claim scope

In a local Python prototype over 100,000 deterministic synthetic agent events, canonical-JSON SHA-256 hash chaining detected event mutation, middle deletion, adjacent reordering, and last-event modification, and it detected prefix truncation only when the verifier retained the original head hash as an external checkpoint.

## Why it stopped

No-paper useful signal: the local synthetic prototype supports the mechanism and exposes the checkpoint dependency, but it is not direct or novel enough for publication-grade evidence.

## Recommended next action

Run a bounded follow-up that adds signed periodic checkpoints and replays production-like multi-agent logs to measure checkpoint cadence, recovery behavior, and overhead against baseline JSONL tracing.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Signed checkpoint cadence for hash-chained agent evidence ledgers
- Success threshold: Detect 100% of injected tamper cases including truncation and forks when the relevant checkpoint exists, while keeping append throughput overhead under 5% and verification throughput above 50000 events/s on the same host.
- Stop condition: Stop if signed checkpoints fail to detect truncation/forks under retained-checkpoint conditions, or if overhead exceeds 20% at all tested checkpoint intervals.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-agent-evidence-ledger-f5886eb21794`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
