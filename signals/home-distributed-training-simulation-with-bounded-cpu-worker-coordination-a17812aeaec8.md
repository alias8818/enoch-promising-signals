# Home distributed training simulation with bounded CPU worker coordination

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `home-distributed-training-simulation-with-bounded-cpu-worker-coordination-a17812aeaec8`
Run ID: `home-distributed-training-simulation-with-bounded-cpu-worker-coordination-a17812aeaec8-20260605T104014408141+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/205a2aa29d04

## What looked useful

Bounded coordination reduced p95 applied staleness to about 4 updates while unbounded async reached p95 staleness up to 35.4 updates. Bounded was best by mean eval loss in 2 of 6 conditions, unbounded async in 4 of 6, and sync in 0 of 6. Mean bounded-minus-unbounded eval loss was +0.000097, while mean bounded-minus-sync eval loss was -0.004730.

## Boundaries and scale limits

Synthetic binary classification, logistic regression, simulated timing/network effects, 5 seeds per condition, 4/8/16 workers, two heterogeneity levels, no real multi-host networking, no deep model training, and no long-horizon validation.

## Claim scope

In a deterministic CPU-only discrete-event simulation of heterogeneous home workers training logistic regression for 40 seconds simulated time, fixed bounded-staleness coordination caps update staleness and beats synchronous coordination on mean eval loss, but does not consistently beat unbounded asynchronous coordination.

## Why it stopped

Proxy simulation produced mixed evidence: fixed bounded coordination controlled stale tails and beat synchronous training, but did not consistently outperform unbounded async, so it is not a publication-grade positive result.

## Recommended next action

Stop this run as a no-paper useful signal; next bounded test should evaluate an adaptive stale-bound/in-flight controller against unbounded async on the same simulator before any real multi-host benchmark.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive stale-bound coordination for heterogeneous home CPU training
- Success threshold: Adaptive bounded coordination is best or statistically tied for best mean eval loss in at least 4 of 6 tested conditions, has lower p95 staleness than unbounded async in all conditions, and does not exceed 1.5x unbounded modeled coordinator CPU time.
- Stop condition: Stop if adaptive coordination is not better than unbounded async in at least 4 of 6 conditions or if its coordinator CPU model exceeds 1.5x unbounded async without loss improvement.

## Evidence references

- Artifact root: `<local-path>/projects/home-distributed-training-simulation-with-bounded-cpu-worker-coordination-a17812aeaec8`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
