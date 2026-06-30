# Local Toy Gradient Commitments for Volunteer Anti-Cheating

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `local-toy-gradient-commitments-for-volunteer-anti-cheating-ef6dcb71a525`
Run ID: `local-toy-gradient-commitments-for-volunteer-anti-cheating-ef6dcb71a525-20260529T180241019837+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/3f2818b476db

## What looked useful

Commitments are a valid anti-equivocation primitive: 350000/350000 changed adaptive reveals were detected in the full sweep. Commitment-only is not standalone volunteer anti-cheating: 0/350000 precommitted bogus gradients were detected, and fixed bogus-gradient performance matched the no-commit baseline.

## Boundaries and scale limits

Synthetic objective and attack model only; no real neural network, volunteer network, secure aggregation stack, Sybil model, incentive model, or correctness proof was tested. Runtime was a 2-minute CPU simulation, not large-scale distributed training.

## Claim scope

Local toy sign-gradient simulation with 11 workers, 256 dimensions, 250 rounds, and bounded malicious workers shows hash commit/reveal detects changed gradient reveals and suppresses adaptive last-mover cheating, but does not detect precommitted bogus gradients.

## Why it stopped

No-paper useful signal: the toy evidence supports anti-equivocation but falsifies the stronger standalone volunteer anti-cheating interpretation for precommitted bogus gradients.

## Recommended next action

Stop treating commitment-only as a full anti-cheating mechanism; the next bounded test should add random recomputation audits or redundancy and measure detection/cost on a small real model.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Gradient Commitments Plus Random Audit on a Small Real Model
- Success threshold: At least 90% detection of injected bogus gradients at 20-40% malicious workers with less than 25% wall-clock overhead and no worse than 5% relative validation-loss degradation versus honest training.
- Stop condition: Stop if audit false positives exceed 2%, overhead exceeds 50%, or detection stays below 50% at 30% malicious workers after parameter tuning.

## Evidence references

- Artifact root: `<local-path>/projects/local-toy-gradient-commitments-for-volunteer-anti-cheating-ef6dcb71a525`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
