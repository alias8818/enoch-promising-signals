# Merkle-Log Agent Integrity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `merkle-log-agent-integrity-21b003ceee81`
Run ID: `merkle-log-agent-integrity-21b003ceee81-20260526T112741104368+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b47c4530c038

## What looked useful

Merkle/hash-chain logging is practical at local trace scale and detects common edits, deletes, reorders, truncations, and partial hash rewrites when a checkpoint is externally retained. The key boundary is that an unanchored self-contained log can be fully rewritten and remain internally valid.

## Boundaries and scale limits

Synthetic events only; single-process CPU implementation; no real production traces, concurrent writers, hostile runtime compromise, external timestamping service, privacy analysis, or comparison to mature transparency-log systems. Internal self-consistency alone failed to detect a full-log rewrite with recomputed hashes.

## Claim scope

Local synthetic Python benchmark of a hash-chained, batch-Merkle-rooted agent action log with an externally retained checkpoint. At 100,000 synthetic events, checkpointed verification detected all tested post-hoc tamper classes with roughly 1.7x append CPU overhead, 2.16x storage overhead, about 197k events/s verification throughput, and about 725-byte inclusion proofs for 256-record batches.

## Why it stopped

Local synthetic evidence supports the mechanism with an explicit trust-boundary caveat, but it is not publication-grade evidence for a new end-to-end agent integrity system.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should replay the scheme on real agent traces with externally timestamped checkpoints and adversarial fork/rewrite attempts.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Checkpoint-Anchored Merkle Logs on Real Agent Traces
- Success threshold: Across real traces, checkpointed verification detects all tested rewrite/fork/delete/reorder/truncate attacks while keeping storage overhead below 3x and p95 append overhead below 5 ms per event.
- Stop condition: Stop if external checkpoint anchoring is unavailable, if full-log rewrite or fork attacks pass anchored verification, or if measured overhead exceeds 3x storage or 5 ms p95 append latency on realistic traces.

## Evidence references

- Artifact root: `<local-path>/projects/merkle-log-agent-integrity-21b003ceee81`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
