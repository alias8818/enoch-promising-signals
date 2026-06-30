# Real-Agent Evidence Ledger Queue Benchmark

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `real-agent-evidence-ledger-queue-benchmark-ef28821d11`
Run ID: `real-agent-evidence-ledger-queue-benchmark-ef28821d11-20260605T221439170303+0000`

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

- Parent run decision: Bounded Queue Depth Falsifiable Agent Reliability via Evidence Ledger: enoch://control-plane/projects/bounded-queue-depth-falsifiable-agent-reliability-via-evidence-ledger-66c392d41015/runs/bounded-queue-depth-falsifiable-agent-reliability-via-evidence-ledger-66c392d41015-20260605T203008599308+0000
- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d7ba9c7bd4a7

## What looked useful

Queue-backed ledger writing is useful for avoiding concurrent SQLite write-conflict loss and improving persisted throughput under local multi-agent contention, but queue backpressure can worsen p95 submit latency. Treat it as an engineering reliability pattern needing tuning, not a paper-ready result.

## Boundaries and scale limits

Single host, Python multiprocessing, SQLite WAL only, no production LLM/tool-agent traces, no crash/recovery injection, no distributed queue, no multi-backend comparison, and only two controlled timeout settings.

## Claim scope

In a local 8-process Python agent benchmark writing 40,000 deterministic evidence records to SQLite WAL, a queue-backed single writer preserved all records and improved persisted throughput versus direct concurrent appends, but did not consistently improve p95 agent-facing submit latency.

## Why it stopped

Tier 1 direct benchmark completed; result is a useful mixed signal but not paper-positive because the p95 latency threshold was not met and the workload is local/synthetic.

## Recommended next action

Run a bounded deepen follow-up using replayed real-agent traces with crash/recovery injection and queue backpressure tuning; stop if queue mode cannot maintain zero loss while matching or beating direct p95 latency.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Agent Trace Replay With Queue Backpressure and Recovery Checks
- Success threshold: Queue mode must have zero missing/duplicate evidence after recovery, no writer errors, throughput at least 1.5x direct append, and p95 submit latency no worse than direct append by more than 10%.
- Stop condition: Stop if any queue variant loses evidence, duplicates keys, fails recovery, or remains more than 10% worse than direct append p95 latency across three repetitions.

## Evidence references

- Artifact root: `<local-path>/projects/real-agent-evidence-ledger-queue-benchmark-ef28821d11`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
