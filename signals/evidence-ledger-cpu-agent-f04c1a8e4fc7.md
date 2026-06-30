# Evidence-Ledger CPU Agent

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `evidence-ledger-cpu-agent-f04c1a8e4fc7`
Run ID: `evidence-ledger-cpu-agent-f04c1a8e4fc7-20260607T063118526769+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/bde5126b6812

## What looked useful

A minimal hash-chained local evidence ledger can provide tamper-evident record integrity for CPU-agent event logs with moderate overhead in a bounded Python harness.

## Boundaries and scale limits

Synthetic events only; no live agent loop, concurrent writers, crash recovery, deletion/truncation resistance, external timestamping, key management, remote attestation, append-only filesystem enforcement, or multi-host merge semantics were tested.

## Claim scope

Single-process CPU-worker synthetic benchmark of a SHA-256 hash-chained JSONL evidence ledger for command/result events. The tested ledger verified clean records, detected one in-place payload tamper per trial, and achieved 41,122 median events/s with 2.68x median append overhead versus plain JSONL across five 20,000-event trials.

## Why it stopped

The local synthetic mechanism passed its preset thresholds, but the evidence is not publication-grade because it does not test real agent behavior or adversarial durability beyond in-place payload tampering.

## Recommended next action

Stop this run as a no-paper useful signal; next, run a bounded real-agent integration test with crash/restart and concurrent append controls before considering paper claims.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-agent evidence ledger durability probe
- Success threshold: Across at least 1,000 real local command tasks, clean ledger verification must pass after restart, all specified tamper classes must be detected, and median task wall-time overhead versus plain JSONL must remain below 10%.
- Stop condition: Stop as negative if crash/restart corrupts valid ledgers, any specified tamper class is not detected, or median task overhead is 10% or higher in the real-agent loop.

## Evidence references

- Artifact root: `<local-path>/projects/evidence-ledger-cpu-agent-f04c1a8e4fc7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
