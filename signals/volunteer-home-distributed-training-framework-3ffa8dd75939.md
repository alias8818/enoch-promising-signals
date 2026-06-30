# Volunteer Home Distributed Training Framework

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-home-distributed-training-framework-3ffa8dd75939`
Run ID: `volunteer-home-distributed-training-framework-3ffa8dd75939-20260607T042925343976+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/d189e1faa4bf

## What looked useful

Deadline/quorum scheduling reduced final loss versus sync_random in 20/24 paired seed-churn comparisons and delivered 1.36x-2.30x simulated throughput, but versus async_accept_all it won loss in only 11/24 comparisons and had lower throughput and accuracy at all churn levels.

## Boundaries and scale limits

No real network, NAT, security, adversarial-client, checkpoint-transfer, GPU, transformer, or multi-host evidence was produced. Async staleness is only lightly approximated, and the task is convex logistic regression rather than large neural training.

## Claim scope

In a bounded NumPy simulator of 32 heterogeneous volunteer home nodes training logistic regression on synthetic non-IID data, deadline/quorum scheduling improves simulated throughput and final loss over naive synchronous collection but does not outperform an optimistic always-accept asynchronous baseline.

## Why it stopped

Bounded simulator produced a mixed useful signal: the proposed scheduler beats naive synchronous collection but fails to beat the stronger optimistic async control, so this is no-paper evidence rather than validation.

## Recommended next action

Stop paper path for this run; next build a real multi-process trace-replay prototype with a staleness-aware async control before making any broader volunteer-training claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-replay volunteer training with staleness-aware async controls
- Success threshold: Deadline/quorum must improve median time-to-target quality by at least 20% over staleness-aware async across at least 3 trace regimes while matching final validation quality within 0.2 percentage points and not increasing participation Gini by more than 0.05.
- Stop condition: Stop if deadline/quorum fails to beat staleness-aware async on time-to-target in at least 2 of 3 trace regimes or causes a final-quality drop above 0.2 percentage points.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-home-distributed-training-framework-3ffa8dd75939`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
