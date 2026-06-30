# Adaptive Chunk Sizing for Queue Pressure Relief

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-chunk-sizing-for-queue-pressure-relief-77a399ce4d37`
Run ID: `adaptive-chunk-sizing-for-queue-pressure-relief-77a399ce4d37-20260605T221338647519+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e936b2c85cde

## What looked useful

Adaptive pressure-based chunking reduced average queued work versus fixed-large by 49.2% to 87.2%, but never beat the best fixed policy on p95 latency and was 47.8% worse on p95 in the high-overhead regime.

## Boundaries and scale limits

No production traces, no real executor integration, no GPU/kernel/cache/network effects, and no multi-node queue. The result is a bounded proxy signal, not a full validation.

## Claim scope

Synthetic discrete-event queue simulation with finite workers, heavy-tailed and bursty arrivals, lazy chunk generation, fixed chunk controls, and one pressure-aware adaptive policy.

## Why it stopped

Synthetic proxy evidence is mixed: queue backlog relief appears real, but the latency-improvement claim is not supported and high per-chunk overhead makes adaptive chunking harmful.

## Recommended next action

Stop as no-paper useful signal; only continue with a bounded direct executor or trace-replay test of an overhead-aware adaptive controller against fixed chunk controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Overhead-aware adaptive chunk sizing on executor trace replay
- Success threshold: Overhead-aware adaptive policy reduces average queued work by at least 50% versus fixed-large while keeping p95 latency within 5% of, or below, the best fixed policy in at least three of four workload regimes.
- Stop condition: Stop if p95 latency remains more than 10% worse than the best fixed policy in two or more regimes, or if overhead-aware control reduces queued work by less than 25% versus fixed-large.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-chunk-sizing-for-queue-pressure-relief-77a399ce4d37`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
