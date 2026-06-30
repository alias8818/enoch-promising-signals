# Compressed State Checkpoints for Fault-Tolerant Home Agents

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `compressed-state-checkpoints-for-fault-tolerant-home-agents-450d8026609d`
Run ID: `compressed-state-checkpoints-for-fault-tolerant-home-agents-450d8026609d-20260603T213953830612+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/3b9552bce518

## What looked useful

zlib-level compressed checkpoints look viable for a real checkpoint backend follow-up: zlib6 every 100 events used 1.484 MB total checkpoint bytes versus 6.292 MB uncompressed and recovered in 0.345 ms mean versus 1.944 ms replay-only, with all sampled recovery digests verified.

## Boundaries and scale limits

Synthetic single-process CPU-only Python benchmark only; no real LangGraph/home-agent runtime, no real home automation traces, no fsync/power-loss durability, no encryption/redaction, no concurrent processes, and no multi-day deployment.

## Claim scope

In a deterministic synthetic JSON-like home-agent state benchmark with 8,000 events and 120 sampled crash points, compressed full-state checkpoints restore correctly, reduce checkpoint storage to about 22-29% of uncompressed same-interval snapshots, and recover about 2.5-5.9x faster than replay-only depending on codec and interval.

## Why it stopped

No-paper closure: the local evidence is a useful synthetic mechanism signal, not direct deployment-grade validation.

## Recommended next action

Run a bounded real-runtime follow-up using the target LangGraph or home-agent checkpoint backend, SQLite or filesystem persistence with fsync, process-kill crash injection, and a replayable home automation trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-injected LangGraph checkpoint compression for home-agent traces
- Success threshold: At least 3x retained storage reduction versus uncompressed checkpoints, 100% recovery correctness across injected crashes, restore-to-next-action latency no more than 2x uncompressed checkpoint restore and faster than replay-only median and p95.
- Stop condition: Stop if compressed checkpoints fail any recovery correctness check, if fsync plus compression makes p95 restore-to-next-action slower than replay-only, or if real state compresses to less than 1.5x storage reduction.

## Evidence references

- Artifact root: `<local-path>/projects/compressed-state-checkpoints-for-fault-tolerant-home-agents-450d8026609d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
