# Live agent runtime signed provenance ledger integration

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `live-agent-runtime-signed-provenance-ledger-integration-1b54de2acc`
Run ID: `live-agent-runtime-signed-provenance-ledger-integration-1b54de2acc-20260516T022323219274+0000`

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

- Internal Enoch project: Live agent runtime signed provenance ledger integration: internal_generated:live-agent-runtime-signed-provenance-ledger-integration-1b54de2acc

## What looked useful

Batched Ed25519 signing is a practical ablation: it preserved the same tamper-detection outcome as per-event signing in this benchmark while substantially reducing append latency. Most overhead came from canonical hash-chain ledger construction rather than the batch signature itself.

## Boundaries and scale limits

Synthetic single-process event generation only; no real LangGraph/OpenAI Agents SDK integration, concurrent writers, crash recovery, key rotation, remote timestamping, transparency log anchoring, production storage, or real user/task traces. Not a production security proof and not broad paper-grade evidence.

## Claim scope

In a local synthetic live-agent event benchmark with 3 workload shapes, 5 fixed seeds, and 10,000 events per condition, hash-chained Ed25519 provenance ledgers detected all injected post-hoc payload tampering with zero clean verification failures. Batched signing every 64 events kept p95 append latency below 50 us and throughput above 17,000 events/s, but retained only 24.8% to 28.1% of plain JSONL throughput.

## Why it stopped

No-paper closure: Tier 2 local evidence supports the mechanism but only on a synthetic single-process runtime proxy, so it is insufficient for a publication-grade live agent runtime claim.

## Recommended next action

Integrate the signed_batch_64 ledger into a real LangGraph or Agents SDK runtime and rerun the same metrics on concurrent task traces with crash/restart persistence checks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real agent runtime batched signed provenance ledger integration
- Success threshold: 100% tamper/replay detection, zero clean verification failures, and less than 10% mean end-to-end task latency overhead versus plain logging across fixed concurrent task seeds.
- Stop condition: Stop as unsupported if clean verification failures occur, any tamper/replay injection is missed, crash recovery corrupts the ledger, or mean end-to-end task latency overhead is 10% or higher.

## Evidence references

- Artifact root: `<local-path>/projects/live-agent-runtime-signed-provenance-ledger-integration-1b54de2acc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
