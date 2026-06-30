# Live Agent Runtime Merkle Ledger Crash Harness

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `93`
Project ID: `live-agent-runtime-merkle-ledger-crash-harness-f67045ab75`
Run ID: `live-agent-runtime-merkle-ledger-crash-harness-f67045ab75-20260528T134621531607+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `93`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Crash-Recovered Agent-Framework Merkle Ledger with Model-Parsed Tool Calls: enoch://control-plane/projects/crash-recovered-agent-framework-merkle-ledger-with-model-p-468fad3167/runs/crash-recovered-agent-framework-merkle-ledger-with-model-p-468fad3167-20260528T094943363419+0000
- Parent run decision: Real 1B-Agent Trace Integration for Merkle Evidence Ledger: enoch://control-plane/projects/real-1b-agent-trace-integration-for-merkle-evidence-ledger-1fa21c996d/runs/real-1b-agent-trace-integration-for-merkle-evidence-ledger-1fa21c996d-20260528T054643294794+0000

## What looked useful

Merkle JSONL detected 2,044/2,048 injected faults (99.80%) versus 1,552/2,048 (75.78%) for plain JSONL, with 0 clean false positives for both. The Merkle gain came mainly from payload bitflips: 512/512 detected versus 20/512 for plain JSONL. Mean write throughput was 7,163 events/s for Merkle versus 7,747 events/s for plain JSONL, and storage was 1.176x higher.

## Boundaries and scale limits

5,120 local file-level trials with fixed seeds; no real LangGraph/live-agent integration, no concurrent multi-writer runtime, no device power-loss testing, and no SQLite WAL or production event-store baseline.

## Claim scope

In a deterministic Python JSONL crash/corruption harness for live-agent-style event streams, a Merkle hash chain preserves valid-prefix recovery and detects committed payload mutation that a plain sequence-checked append log usually accepts silently.

## Why it stopped

No-paper useful signal: the local harness supports the integrity mechanism but lacks direct production-runtime crash evidence and a production-grade baseline required for publication.

## Recommended next action

Run one final depth-4 bounded follow-up inside an actual resumable agent runtime with kill -9 crash injection, concurrent writers, durable root persistence, recovery latency metrics, and a SQLite WAL or production event-store baseline; otherwise stop as no-paper mechanism evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Runtime-integrated Merkle ledger crash recovery against SQLite WAL
- Success threshold: Across at least 1,000 runtime-level crash/resume trials, Merkle replay has zero undetected committed-record mutations, zero invalid-prefix accepts, no more than 20% write throughput overhead versus the production-grade baseline, and no clean-control false positives.
- Stop condition: Stop if Merkle replay accepts any invalid prefix, misses any committed-record mutation under the runtime fault model, or exceeds 20% write throughput overhead without a compensating correctness advantage.

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-runtime-merkle-ledger-crash-harness-f67045ab75`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
