# Lightweight Evidence Ledger for Home GPU Workers

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `lightweight-evidence-ledger-for-home-gpu-workers-b9da40e1e11d`
Run ID: `lightweight-evidence-ledger-for-home-gpu-workers-b9da40e1e11d-20260611T022906027415+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/eb27cdc59ebe

## What looked useful

The ledger reached 58,751 events/s with 17.136 us p95 append latency and 751.17 bytes/event versus plain JSONL at 236,777 events/s and 6.416 us p95. Clean verification passed for 20,000 records, and a deliberate midpoint payload mutation was detected as payload_hash_mismatch at line 10001.

## Boundaries and scale limits

Tested only on 20,000 synthetic events plus one dummy checkpoint artifact on one local host. It did not test real GPU training workloads, multi-process writers, crash consistency, fsync policies, external anchoring, rollback/truncation resistance, or adversarial host compromise.

## Claim scope

A single-process Python hash-chain ledger can record synthetic home GPU worker evidence events and local artifact SHA-256 fingerprints with low microsecond-scale append latency, then detect in-place payload tampering in retained logs.

## Why it stopped

No-paper useful signal: local synthetic evidence supports the mechanism and quantifies overhead, but the run does not provide publication-grade durability, concurrency, rollback, or real-workload validation.

## Recommended next action

Run a bounded crash-consistency and concurrent-writer follow-up that compares fsync policies and a single-writer queue under process kill/restart, then decide whether the ledger is robust enough for real home-worker deployment.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Crash-consistent evidence ledger under concurrent home-worker writes
- Success threshold: After at least 30 forced-crash trials per policy, the recommended mode must always verify to a valid prefix, lose no more than the documented fsync window, and sustain at least 100 events/s with p95 end-to-end append latency under 2 ms.
- Stop condition: Stop if all durability modes either produce unverifiable retained logs or exceed 2 ms p95 latency at 100 events/s, because the lightweight design would not be suitable for always-on home-worker evidence capture.

## Evidence references

- Artifact root: `<local-path>/projects/lightweight-evidence-ledger-for-home-gpu-workers-b9da40e1e11d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
