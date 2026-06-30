# Hash-Chained Agent Ledger

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `hash-chained-agent-ledger-1748776afe97`
Run ID: `hash-chained-agent-ledger-1748776afe97-20260521T222825596278+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2eeb37ddb77e

## What looked useful

Hash chaining is useful as a low-cost tamper-evidence primitive for agent logs, but unanchored chains are insufficient for provenance because internally valid truncated or replacement ledgers pass verification. Anchoring count plus tail hash fixed those misses in the local experiment.

## Boundaries and scale limits

Tested locally on synthetic events only: 50,000 records per trial, 3 trials, single writer, no fsync durability policy, no concurrent appenders, no crash recovery, no real agent traces, and no deployed anchor/signature service.

## Claim scope

In a single-process synthetic JSONL agent-event workload, SHA-256 or HMAC-SHA-256 hash chaining detects interior payload edits, record deletion, and adjacent record reorder at modest append and storage overhead, but only detects tail truncation or wholesale replacement when an external expected count and tail hash are retained.

## Why it stopped

Closed as no-paper useful signal: local evidence supports the mechanism only with external anchoring and falsifies standalone unanchored ledger provenance for truncation/replacement attacks.

## Recommended next action

Run a bounded deepen test that adds multi-process append locking, crash-recovery cases, fsync policy variants, and signed external checkpoints over realistic agent traces.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Anchored Multi-Writer Agent Ledger Durability Test
- Success threshold: Across at least 1 million replayed events, detect 100% of edit/delete/reorder/truncate/replacement attacks with signed checkpoints, recover cleanly from injected partial-write crashes, and keep median append overhead below 3x plain JSONL.
- Stop condition: Stop if concurrent append or fsync/checkpoint overhead exceeds 5x plain JSONL before crash recovery succeeds, or if signed checkpoints still miss truncation/replacement attacks.

## Evidence references

- Artifact root: `<local-path>/projects/hash-chained-agent-ledger-1748776afe97`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
