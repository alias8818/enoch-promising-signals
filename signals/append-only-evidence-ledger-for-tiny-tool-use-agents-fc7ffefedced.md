# Append-Only Evidence Ledger for Tiny Tool-Use Agents

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `append-only-evidence-ledger-for-tiny-tool-use-agents-fc7ffefedced`
Run ID: `append-only-evidence-ledger-for-tiny-tool-use-agents-fc7ffefedced-20260531T171844834747+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/8deb87dc73eb

## What looked useful

Append-only ledgers are useful for provenance and tamper detection, and they outperform naive last-write/window memories under contradictory observations. A fair best-reliability mutable slot matched ledger accuracy with lower memory, so the accuracy novelty claim is not paper-ready.

## Boundaries and scale limits

No real LLM, real tool API, real source reliability estimation, multi-hop task, prompt injection, storage latency, or long-horizon compaction test was run. The benchmark used 25,000 synthetic tasks in a single CPU process.

## Claim scope

Synthetic lookup traces with one authoritative early tool observation and later noisy contradictory observations show that an append-only hash-chained evidence ledger prevents naive overwrite/eviction failures and provides tamper-evident provenance, but it does not improve answer accuracy over a compact reliability-aware mutable evidence slot.

## Why it stopped

Synthetic direct memory-policy evidence supports the audit mechanism but falsifies the broad accuracy advantage once a compact reliability-aware mutable control is included.

## Recommended next action

Stop this run as no-paper useful signal; next test should compare append-only ledger versus compact reliability-aware evidence cache on real or LLM-generated tool-use traces with correction/audit outcomes.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Realistic tool-trace ledger versus reliability-cache evaluation
- Success threshold: Ledger must improve correction or audit-completeness metrics by at least 10 percentage points over the reliability-aware cache while keeping memory/latency overhead explicitly bounded.
- Stop condition: Stop if the reliability-aware cache matches ledger correction and audit outcomes within 5 percentage points or if ledger memory/latency overhead is unbounded for the trace lengths tested.

## Evidence references

- Artifact root: `<local-path>/projects/append-only-evidence-ledger-for-tiny-tool-use-agents-fc7ffefedced`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
