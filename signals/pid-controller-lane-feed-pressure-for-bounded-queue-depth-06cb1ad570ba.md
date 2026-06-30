# PID-controller lane feed pressure for bounded queue depth

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `pid-controller-lane-feed-pressure-for-bounded-queue-depth-06cb1ad570ba`
Run ID: `pid-controller-lane-feed-pressure-for-bounded-queue-depth-06cb1ad570ba-20260527T155101025892+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/5b7333bad206

## What looked useful

PID pressure reduced mean absolute target-depth error versus hysteresis by about 27% in stable service, 35% in transient slowdown, and 36% in bursty-tail service, with zero overflow ticks and roughly equal throughput. Fixed near-capacity feed hit the hard queue bound in variable-service regimes with about 17% overflow-tick ratio.

## Boundaries and scale limits

Synthetic simulator only: 6000 ticks, 40 replicates per controller/scenario, no production Enoch lane implementation, no trace replay, no delayed/noisy observation model, no distributed scheduler effects, and no gain robustness sweep.

## Claim scope

In a deterministic synthetic 8-lane bounded-queue simulator with always-backlogged upstream feed, hand-tuned PID feed pressure kept queue depth closer to a target than fixed-rate and hysteresis controls while avoiding hard-bound saturation across stable, transient-slowdown, and bursty-tail service-time regimes.

## Why it stopped

Local synthetic evidence is useful and supports the mechanism, but it is not production-direct or robust enough for a paper-positive claim.

## Recommended next action

Run a bounded direct trace-replay or scheduler-in-loop follow-up comparing PID against hysteresis, token-bucket, adaptive-concurrency, and PI-only controls under observation delay.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Scheduler-in-loop PID lane feed pressure with delayed observations
- Success threshold: PID or PI must reduce mean absolute target-depth error by at least 20% versus the best non-PID baseline while keeping bound violation rate at zero and throughput within 2% of the best safe baseline on at least three trace families.
- Stop condition: Stop if PID/PI loses the target-error advantage, causes any bound violations, or requires gains that are unstable across trace families.

## Evidence references

- Artifact root: `<local-path>/projects/pid-controller-lane-feed-pressure-for-bounded-queue-depth-06cb1ad570ba`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
