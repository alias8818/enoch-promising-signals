# Micro-Batch Commitment-Challenge for Gradient Replay Defense

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `micro-batch-commitment-challenge-for-gradient-replay-defense-f164d0338289`
Run ID: `micro-batch-commitment-challenge-for-gradient-replay-defense-f164d0338289-20260607T133145307189+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/db9f9c4c51eb

## What looked useful

The mechanism is viable as a probabilistic audit: detection rises predictably with challenge budget, reaching 0.76 for 4 of 16 replayed microbatches with 4 of 16 challenged and 1.00 for 8 of 16 replayed with 8 of 16 challenged. Sparse replay remains weakly covered: 1 of 16 replayed microbatches was detected only 0.48 even when challenging 8 of 16. Highest mean measured overhead was 0.689x the simulated honest gradient-compute time.

## Boundaries and scale limits

No real distributed trainer, real dataset, large model, networked client, adaptive adversary, nondeterministic kernel tolerance study, or multi-round convergence impact was tested. The result is bounded to one-step synthetic replay detection on a small MLP.

## Claim scope

In a local PyTorch synthetic microbatch simulator with deterministic recomputation, per-microbatch commitments plus random challenges detect stale gradient replay exactly when replayed microbatches are challenged, with empirical detection matching the expected sampling probability and 0/2000 false positives.

## Why it stopped

Local simulator produced a useful mechanism signal but not direct trainer-level or publication-grade evidence; sparse replay coverage is probabilistic and weak at low challenge budgets.

## Recommended next action

Run a bounded toy federated/data-parallel trainer confirmation with no-defense and commitment-challenge arms, fixed challenge budgets, replay attackers, false-positive tracking, convergence impact, and wall-clock overhead.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Toy Trainer Validation of Microbatch Commitment-Challenge Replay Defense
- Success threshold: At 25 percent challenge budget, detect at least 70 percent of attacks replaying 4 of 16 microbatches, keep honest false positives below 1 percent, reduce accepted replay distortion versus no defense, and add less than 50 percent wall-clock overhead in the toy trainer.
- Stop condition: Stop if false positives exceed 1 percent under honest clients after tolerance tuning, if overhead exceeds 100 percent at 25 percent challenge budget, or if replay detection materially underperforms the combinatorial challenge probability.

## Evidence references

- Artifact root: `<local-path>/projects/micro-batch-commitment-challenge-for-gradient-replay-defense-f164d0338289`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
