# Agent Evidence Ledger with Hash-Chained Action Trace

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `agent-evidence-ledger-with-hash-chained-action-trace-c8b4b4daf526`
Run ID: `agent-evidence-ledger-with-hash-chained-action-trace-c8b4b4daf526-20260620T014742559673+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/a20ab1ddc3ea

## What looked useful

Anchored hash chaining gave deterministic tamper evidence for modified fields, prev_hash edits, deletions, reorders, suffix truncation, and forged single-entry hashes in the bounded test. The same verifier missed 30/30 suffix truncations without an external anchor. Append overhead was 4.56x versus plain JSONL without fsync and 106.88x with per-entry fsync.

## Boundaries and scale limits

Evidence is limited to 1,000-row synthetic traces, one local Python writer, local file storage, no concurrent writes, no real agent runtime integration, no remote notarization, and no adversary capable of rewriting both ledger and anchor.

## Claim scope

In a single-process synthetic agent-action trace, a canonical JSON/SHA-256 hash-chained ledger with an externally anchored final head hash and entry count detected all tested local tamper mutations across 180 trials; unanchored verification did not detect suffix truncation.

## Why it stopped

No-paper closure: the local synthetic mechanism is supported, but evidence is not direct enough for publication-grade claims about real agent evidence ledgers.

## Recommended next action

Run a bounded real-runtime follow-up that instruments actual Codex/LangGraph tool calls, uses periodic anchor checkpoints, and tests concurrent write behavior before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Agent Runtime Evidence Ledger Integration
- Success threshold: At least 10 real tasks complete without lost ledger entries; periodic-anchor mode has under 10 ms p95 append latency; anchored verification detects 100% of tested tamper cases including suffix truncation; concurrency strategy has no verifier failures.
- Stop condition: Stop if instrumentation loses events, p95 append latency exceeds 10 ms in periodic-anchor mode, or anchored verification misses any tested tamper case.

## Evidence references

- Artifact root: `<local-path>/projects/agent-evidence-ledger-with-hash-chained-action-trace-c8b4b4daf526`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
