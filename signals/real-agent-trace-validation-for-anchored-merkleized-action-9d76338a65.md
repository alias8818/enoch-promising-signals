# Real-Agent Trace Validation for Anchored Merkleized Action Ledgers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-agent-trace-validation-for-anchored-merkleized-action-9d76338a65`
Run ID: `real-agent-trace-validation-for-anchored-merkleized-action-9d76338a65-20260519T172204016126+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/a632fe50dec5

## What looked useful

Tier 1 direct evidence supports the basic integrity mechanism for real-agent traces: chained per-entry hashes, batch Merkle roots, chained anchors, and a final manifest detected payload tamper, entry drop, reorder, hash tamper, anchor tamper, and tail truncation while adding low local overhead.

## Boundaries and scale limits

Single local worker trace; local manifest/anchor only; controlled mutation suite; replay stress repeated the same real event shapes to 2,200 events and is not independent multi-agent evidence.

## Claim scope

A deterministic anchored Merkleized action ledger built from one real Enoch/Codex worker JSONL trace accepted the intact 47-event trace, rejected 6/6 controlled integrity mutations, and verified at about 26 microseconds per event locally.

## Why it stopped

No-paper useful signal: the controlled direct test supports the mechanism but is not a full validation because it uses one local trace, local anchors, and a limited mutation suite.

## Recommended next action

Run a bounded deepen follow-up on multiple independent real agent traces with an external append-only anchor witness and a chained-hash-only baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-Trace External-Witness Validation for Anchored Merkleized Agent Ledgers
- Success threshold: Intact traces verify with zero false rejects; all controlled integrity mutations are rejected; external witness detects stale or replayed anchor manifests; overhead remains below 100 microseconds per event on median for traces up to at least 10,000 events.
- Stop condition: Stop if any controlled mutation is accepted, if external witness integration cannot distinguish stale/replayed anchors, or if median verification overhead exceeds 100 microseconds per event before 10,000 events.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-trace-validation-for-anchored-merkleized-action-9d76338a65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
