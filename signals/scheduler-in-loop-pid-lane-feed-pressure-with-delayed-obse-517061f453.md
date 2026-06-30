# Scheduler-in-loop PID lane feed pressure with delayed observations

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `scheduler-in-loop-pid-lane-feed-pressure-with-delayed-obse-517061f453`
Run ID: `scheduler-in-loop-pid-lane-feed-pressure-with-delayed-obse-517061f453-20260527T183543993466+0000`

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

- Parent run decision: PID-controller lane feed pressure for bounded queue depth: enoch://control-plane/projects/pid-controller-lane-feed-pressure-for-bounded-queue-depth-06cb1ad570ba/runs/pid-controller-lane-feed-pressure-for-bounded-queue-depth-06cb1ad570ba-20260527T155101025892+0000
- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5b7333bad206

## What looked useful

Delayed feedback pressure control is useful, but a simple proportional controller captured nearly all of the benefit. Integral action was delay-sensitive; tuned PID was only marginally better than proportional feedback and introduced near-zero but nonzero starvation in the main confirmation.

## Boundaries and scale limits

CPU-only simulated plant; no production scheduler traces, GPU serving workloads, multi-host effects, real telemetry delays, or scheduler overheads were tested.

## Claim scope

In a small stochastic lane-queue simulation with 8 lanes, finite buffers, bursty arrivals, and delayed queue observations, closed-loop feed-pressure control strongly outperformed static equal scheduling, but tuned nonzero-integral PID improved p95 backlog by only 1.8% over delayed proportional feedback at delay 8, below the predeclared 5% threshold.

## Why it stopped

Controlled direct simulation did not meet the PID-specific success threshold versus delayed proportional feedback, although it supported the broader feedback-scheduler mechanism.

## Recommended next action

Stop the current PID claim as no-paper; run a bounded delay-compensated controller follow-up only if testing whether predictor/Smith-style compensation can clear the proportional baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Delay-compensated lane feed-pressure control versus proportional feedback
- Success threshold: At delay 8 and at least one other positive delay, delay-compensated control reduces p95 total backlog by >=8% versus delayed proportional feedback and does not increase dropped work or max starvation.
- Stop condition: Stop if the delay-compensated controller fails to beat delayed proportional feedback by >=5% p95 backlog on a 10-seed calibration sweep or if it increases dropped work in any confirmation run.

## Evidence references

- Artifact root: `<local-path>/projects/scheduler-in-loop-pid-lane-feed-pressure-with-delayed-obse-517061f453`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
