# Tiny Agent Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tiny-agent-evidence-ledger-a9d14b1b6ca9`
Run ID: `tiny-agent-evidence-ledger-a9d14b1b6ca9-20260528T145913291533+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/5b66d5fcf0a5

## What looked useful

The local prototype produced a reproducible useful signal: 40,000 ledgered synthetic steps ran at 2,596.42 steps/s with 0.3779 ms extra cost per step, verified at 119,144.91 records/s, used 120,988 KiB max RSS, and detected tested tamper/delete/reorder corruptions.

## Boundaries and scale limits

Evidence is limited to deterministic synthetic traces on one local worker, one process, no concurrent writers, no crash-recovery test, no digital signatures, no real tool calls, and no comparison against production observability systems.

## Claim scope

A stdlib-only append-only JSONL SHA-256 hash-chain evidence ledger for synthetic tiny-agent traces can verify untampered logs, detect evidence tampering, record deletion, and record reordering, and keep append overhead below 2 ms per step on local CPU runs up to 40,000 synthetic steps.

## Why it stopped

Synthetic/proxy evidence supports the ledger mechanism but is not full validation or publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; next concrete action is to instrument a real tiny-agent workflow and compare ledger replay/audit outcomes against structured logging under normal, corrupted, and interrupted runs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Tiny-Agent Ledger Replay and Crash-Recovery Test
- Success threshold: Ledger run matches baseline task success, detects all injected corruptions, recovers or clearly fails closed after interrupted writes, and adds less than 2 ms median overhead per step on at least 10,000 real workflow steps.
- Stop condition: Stop if real workflow instrumentation cannot produce replayable traces, if median overhead exceeds 2 ms per step, or if any tested corruption is not detected.

## Evidence references

- Artifact root: `<local-path>/projects/tiny-agent-evidence-ledger-a9d14b1b6ca9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
