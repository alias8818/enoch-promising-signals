# Replay Realistic Agent Tool Traces Through a Provenance Evidence Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-realistic-agent-tool-traces-through-a-provenance-ev-fa3579e0d8`
Run ID: `replay-realistic-agent-tool-traces-through-a-provenance-ev-fa3579e0d8-20260527T233341468950+0000`

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

- Parent run decision: Tiny Agent Evidence Ledger for Tool Safety: enoch://control-plane/projects/tiny-agent-evidence-ledger-for-tool-safety-d6bc36179d7d/runs/tiny-agent-evidence-ledger-for-tool-safety-d6bc36179d7d-20260527T205101480337+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/c64e4140781c

## What looked useful

The Tier 1 direct test supports the mechanism: provenance ledger replay can preserve a verifiable clean root and detect output tampering, dropped completion, lifecycle reorder, and injected completion on a real Codex trace. This is useful implementation evidence but not paper-ready.

## Boundaries and scale limits

Single trace, small event count, local CPU-only replay, no heterogeneous framework corpus, no multi-agent concurrency, no large-scale throughput/storage study, and no adversarial logger or root-anchor compromise test.

## Claim scope

On one realistic local Codex agent/tool JSONL trace with 54 events, a SHA-256 hash-chained provenance evidence ledger replayed the clean trace with zero chain or replay errors and detected four controlled tamper cases when anchored to the clean root hash.

## Why it stopped

Tier 1 direct mechanism test passed, but the evidence is a single small trace and therefore supports only a no-paper useful signal, not publication readiness.

## Recommended next action

Run a bounded deepen follow-up on at least 10 heterogeneous real agent traces with a predefined tamper suite and compare detection/overhead against plain JSONL plus post-hoc lifecycle validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Heterogeneous Trace Corpus Replay for Provenance Evidence Ledgers
- Success threshold: Clean replay succeeds on all traces; all predefined tamper cases are detected; false positives are zero on clean traces; replay throughput is at least 10000 events/s; storage overhead is below 2x compared with source JSONL.
- Stop condition: Stop if clean replay fails on more than one trace due to schema mismatch, if any predefined tamper case is missed when a clean root anchor is available, or if storage overhead exceeds 2x without a clear compression path.

## Evidence references

- Artifact root: `<local-path>/projects/replay-realistic-agent-tool-traces-through-a-provenance-ev-fa3579e0d8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
