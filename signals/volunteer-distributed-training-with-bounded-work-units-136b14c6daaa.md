# Volunteer distributed training with bounded work units

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-distributed-training-with-bounded-work-units-136b14c6daaa`
Run ID: `volunteer-distributed-training-with-bounded-work-units-136b14c6daaa-20260608T101913446992+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/698d11b7d1cb

## What looked useful

Validated bounded work units stayed within 0.33 percentage points of central SGD under dropout/delay and under 20%-40% anti-gradient malicious workers, while removing validation degraded accuracy by 10.47 percentage points at 20% bad workers and 51.55 percentage points at 40% bad workers. Strict freshness under high delay traded throughput for closer convergence than loose staleness.

## Boundaries and scale limits

No real volunteers, network transport, heterogeneous hardware, privacy boundary, incentive layer, adaptive adversary, real dataset, neural network, or large-model training was tested. Results should not be interpreted as evidence that volunteer distributed training works for GPT-scale or multi-node neural training.

## Claim scope

Single-process NumPy simulation of bounded volunteer work-unit SGD for softmax regression on synthetic non-IID classification shards. The tested protocol used clipped gradients, per-work-unit loss-decrease validation, and freshness bounds under dropout, delay, and anti-gradient malicious workers.

## Why it stopped

Closed as no-paper useful signal: the evidence is a synthetic single-process mechanism proxy, not direct full validation of volunteer distributed training.

## Recommended next action

Run a bounded deepen follow-up with a real multi-process work-unit server and a small neural model on a real dataset before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Multi-process bounded work-unit training on a real small neural workload
- Success threshold: Across at least 5 seeds, validated bounded work-unit training reaches within 2 percentage points of central baseline accuracy and unvalidated malicious control is at least 5 percentage points worse.
- Stop condition: Stop if serialization/validation overhead exceeds useful training time by more than 3x, if validated training is more than 5 percentage points below baseline, or if bad work is not reliably rejected.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-distributed-training-with-bounded-work-units-136b14c6daaa`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
