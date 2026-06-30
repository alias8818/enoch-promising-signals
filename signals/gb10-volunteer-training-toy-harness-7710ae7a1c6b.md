# GB10 Volunteer Training Toy Harness

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gb10-volunteer-training-toy-harness-7710ae7a1c6b`
Run ID: `gb10-volunteer-training-toy-harness-7710ae7a1c6b-20260628T162211301592+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/afca895b5ac5

## What looked useful

Ideal runs converged in 5/5 seeds with mean final accuracy 0.9097. Fixed-deadline churn was brittle: churn and severe_churn each had 2/5 zero-accepted runs, with mean final accuracies 0.7746 and 0.6945. Accepted-update count, not nominal churn label, dominated progress.

## Boundaries and scale limits

Synthetic 2D classification only; 30 rounds; 5 seeds; simulated dropout/stragglers; no real network, privacy, adversarial behavior, heterogeneous devices, or large-model training.

## Claim scope

A local PyTorch/CUDA toy volunteer-training harness with 16 simulated workers can reproduce both convergence under accepted FedAvg updates and update-starvation under strict fixed deadlines.

## Why it stopped

No-paper closure: this is a proxy/toy useful signal showing deadline brittleness, not direct or publication-grade volunteer training validation.

## Recommended next action

Run a bounded follow-up comparing fixed deadlines against adaptive deadline or minimum-quorum aggregation in the same toy harness.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive deadlines for toy volunteer FedAvg
- Success threshold: Adaptive or quorum policy cuts zero-accepted runs by at least 75% versus fixed deadlines and improves mean final accuracy by at least 0.05 absolute without more than 2x wall-clock cost.
- Stop condition: Stop if adaptive/quorum policies do not reduce zero-accepted runs or if their wall-clock overhead exceeds 2x while accuracy remains within 0.02 of fixed deadlines.

## Evidence references

- Artifact root: `<local-path>/projects/gb10-volunteer-training-toy-harness-7710ae7a1c6b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
