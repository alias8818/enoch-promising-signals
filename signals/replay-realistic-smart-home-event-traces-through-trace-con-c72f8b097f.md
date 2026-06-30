# Replay Realistic Smart-Home Event Traces Through Trace Consensus Ledger

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `replay-realistic-smart-home-event-traces-through-trace-con-c72f8b097f`
Run ID: `replay-realistic-smart-home-event-traces-through-trace-con-c72f8b097f-20260526T231851360705+0000`

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

- Parent run decision: Multi-Agent Consensus Ledger for Safe Home Actions: enoch://control-plane/projects/multi-agent-consensus-ledger-for-safe-home-actions-1cd7ecb2bf47/runs/multi-agent-consensus-ledger-for-safe-home-actions-1cd7ecb2bf47-20260525T203351264325+0000
- Parent run decision: Trace-Based Consensus Ledger Evaluation for Smart-Home Agent Actions: enoch://control-plane/projects/trace-based-consensus-ledger-evaluation-for-smart-home-age-f8054ed932/runs/trace-based-consensus-ledger-evaluation-for-smart-home-age-f8054ed932-20260526T172301271866+0000

## What looked useful

Consensus_full reached mean F1 0.997830 versus 0.955764 for single_gateway_append and 0.989678 for union_dedupe_merge. Quorum reduced mean false positives from 417.2 in the no-quorum/union control to 0.8. Stable ordering reduced adjacent order inversions from 8443.2 in the no-hash-order ablation to 0.0.

## Boundaries and scale limits

The smart-home traces are real, but reliability/adversarial faults are injected rather than observed in a deployed multi-gateway ledger. The implementation is an evaluator, not a production distributed protocol with signatures, crash recovery, network partitions, or device/storage constraints. Validation covered one CASAS home and five fixed seeds.

## Claim scope

In deterministic replay of 5 fixed-seed, 20,000-event windows from the public CASAS Aruba smart-home trace with injected replica drops, jitter, replay duplicates, and payload mutations, a 5-replica majority trace-consensus ledger improved event-recovery F1 over a single-gateway append baseline and eliminated receipt-time order inversions when stable hash-chain ordering was enabled.

## Why it stopped

Tier 2 mechanism support was achieved with real traces, fixed seeds, baselines, and ablations, but paper-positive closure would require deployed/protocol-level evidence rather than injected-fault replay only.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded deepen test should implement signed persistent ledger blocks and validate across all four CASAS homes with sensitivity sweeps for drop, replay, mutation, quorum size, and clock skew.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Cross-Home Signed Persistent Trace Consensus Ledger Replay
- Success threshold: Across all homes and seeds, consensus_full mean F1 >= 0.995, mean false positives <= 1 per 20,000-event window, zero adjacent order inversions, and explicit latency/storage overhead reported; ablations must show quorum is responsible for false-positive rejection and stable ordering is responsible for inversion removal.
- Stop condition: Stop as negative if any home has consensus_full mean F1 below 0.990, mean false positives above 10 per 20,000-event window, nonzero stable-order inversions after recovery, or overhead that makes the design impractical for commodity smart-home gateways.

## Evidence references

- Artifact root: `<local-path>/projects/replay-realistic-smart-home-event-traces-through-trace-con-c72f8b097f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
