# Queue-Pressure-Aware Batch Scheduling for SpecDec

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `queue-pressure-aware-batch-scheduling-for-specdec-44c04c8a1cf4`
Run ID: `queue-pressure-aware-batch-scheduling-for-specdec-44c04c8a1cf4-20260610T042925278941+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/89779ce81038

## What looked useful

Queue pressure is useful as a guardrail against over-speculation: large fixed windows collapse tail latency under pressure, while an active-occupancy-aware QPA policy tracks the per-load best fixed-K baseline within 0.623% mean p95 latency and 0.0069% mean throughput. It does not materially beat a strong fixed small-window baseline.

## Boundaries and scale limits

No real model inference, GPU kernel timing, KV-cache pressure, serving framework integration, or measured draft-model acceptance traces were tested. The result supports only scheduling-mechanism guidance, not production performance claims.

## Claim scope

Synthetic discrete-event simulation of queue-pressure-aware speculative decoding batch scheduling across seven offered-load points, five seeds per point, 2500 requests per seed, and fixed-K baselines k=0/1/2/4.

## Why it stopped

Synthetic proxy evidence produced a useful mechanism signal but not direct publication-grade validation; QPA mainly matched the best fixed-K baseline rather than materially improving on it.

## Recommended next action

Do not write a paper from this proxy result; run a bounded real-serving follow-up implementing active-occupancy-aware k=1/2 switching in a SpecDec serving stack and compare against fixed k=0/1/2/4 around saturation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-serving validation of active-occupancy-aware SpecDec window switching
- Success threshold: QPA p95 latency within 2% of the best fixed-K at every load, at least 5% better than fixed k=1 at one low-load point or at least 5% better than fixed k=2 at one transition/high-load point, without reducing output tokens/s by more than 2%.
- Stop condition: Stop if QPA is more than 5% worse than fixed k=1 in p95 latency at two or more transition/high-load points, or if real measured overhead makes the switching policy reduce throughput by more than 5%.

## Evidence references

- Artifact root: `<local-path>/projects/queue-pressure-aware-batch-scheduling-for-specdec-44c04c8a1cf4`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
