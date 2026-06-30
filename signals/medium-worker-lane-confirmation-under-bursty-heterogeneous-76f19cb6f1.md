# Medium Worker-Lane Confirmation Under Bursty Heterogeneous Load

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-worker-lane-confirmation-under-bursty-heterogeneous-76f19cb6f1`
Run ID: `medium-worker-lane-confirmation-under-bursty-heterogeneous-76f19cb6f1-20260601T084940919508+0000`

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

- Parent run decision: Bounded Work Lane Feed Pressure Control: enoch://control-plane/projects/bounded-work-lane-feed-pressure-control-05973c7044cc/runs/bounded-work-lane-feed-pressure-control-05973c7044cc-20260531T194810907752+0000
- Parent run decision: Real Worker-Lane Prototype for Bounded Feed Pressure: enoch://control-plane/projects/real-worker-lane-prototype-for-bounded-feed-pressure-ad8e70da6b/runs/real-worker-lane-prototype-for-bounded-feed-pressure-ad8e70da6b-20260601T022410824110+0000

## What looked useful

Tier 2 confirmation found a bounded mechanism signal: fresh slack confirmation plus compatible spillover improved p95 latency on 10/10 seeds in moderate and heavy balanced bursty workloads, while ablations without spillover, fresh confirmation, or confirmation itself were worse. The mechanism failed on skewed hot-lane saturation, showing it cannot compensate for insufficient compatible capacity.

## Boundaries and scale limits

Synthetic simulator only; no production traces, no real task runtime, no distributed coordination overhead, no autoscaling, and only 10 seeds across three medium workloads. Heavy-bursty SLO miss rates remained near saturation, limiting practical service-quality claims.

## Claim scope

In a fixed-seed synthetic discrete-event queue simulation with heterogeneous workers and bursty arrivals, worker-lane confirmation with compatible spillover reduced median p95 latency versus a compatibility-aware JSQ baseline in balanced moderate and heavy bursty workloads, with no throughput loss. It did not improve p95 latency under skewed hot-lane saturation.

## Why it stopped

Tier 2 synthetic evidence is mixed: WLC passed the p95/throughput/ablation threshold in two of three workloads but failed on skewed hot-lane saturation and remains simulator-only, so it is useful no-paper evidence rather than paper-positive support.

## Recommended next action

Run a bounded deepen follow-up that adds SLO-aware confirmation thresholds and admission/spillover controls, then test against the same fixed seeds plus at least one trace-derived workload.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: SLO-Aware Worker-Lane Confirmation Under Hot-Lane Saturation
- Success threshold: Improve median p95 latency by at least 10% versus compatibility-aware JSQ in at least two workloads, reduce or match SLO miss rate versus current WLC in every workload, and show a positive p95 improvement on at least 7/10 seeds in the skewed hot-lane workload without more than 1% throughput loss.
- Stop condition: Stop if SLO-aware WLC cannot improve skewed hot-lane p95 on at least 7/10 seeds or if it trades more than 1% throughput loss for tail-latency gains.

## Evidence references

- Artifact root: `<local-path>/projects/medium-worker-lane-confirmation-under-bursty-heterogeneous-76f19cb6f1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
