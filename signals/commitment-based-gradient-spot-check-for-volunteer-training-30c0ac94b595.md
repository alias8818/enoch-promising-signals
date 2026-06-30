# Commitment-Based Gradient Spot-Check for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `commitment-based-gradient-spot-check-for-volunteer-training-30c0ac94b595`
Run ID: `commitment-based-gradient-spot-check-for-volunteer-training-30c0ac94b595-20260613T003014345835+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/f8f9e63f7a3f

## What looked useful

Commitments are useful as an anti-equivocation binding mechanism, but the security effect in this setup comes from pairing them with recomputation of sampled gradients. At 20 seeds and 60 rounds, recompute auditing increased detection per poisoned submission from 0.17 at 12.5% spot-checking to 1.0 at 100%, and final accuracy rose from 0.8349 with no effective audit to 0.9742 at full audit.

## Boundaries and scale limits

Toy synthetic data, small convex model, simple additive attack, deterministic recomputation, no privacy constraints, no real volunteer network, no large neural network, and no adaptive or colluding adversaries. Results are not full-scale or paper-ready.

## Claim scope

In a synthetic logistic-regression volunteer-training simulation with 8 volunteers, 2 additive-gradient attackers, and coordinator access to assigned batches, hash commitments plus random sampled gradient recomputation detect poisoned submissions in proportion to the audit rate and improve final accuracy by dropping detected bad submissions. Hash-only commitments do not detect incorrect gradients.

## Why it stopped

The result is a bounded synthetic mechanism check, not direct full validation of volunteer training. It supports a scoped follow-up but is insufficient for a paper.

## Recommended next action

Stop this run as no-paper useful signal; the next concrete test should move to a medium non-IID neural-network volunteer simulation with adaptive poisoning and explicit audit overhead measurement.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium Non-IID Neural Volunteer Gradient Spot-Check
- Success threshold: At a spot-check rate of 25% or lower, recomputation auditing should cut accepted poisoned update rounds by at least 30% versus hash-only commitment while preserving or improving clean-task accuracy within one standard deviation of the honest/no-attack baseline.
- Stop condition: Stop if hash-only and recomputation auditing are statistically indistinguishable on accepted poisoned update rate, or if recomputation overhead exceeds the training cost at spot rates below 25%.

## Evidence references

- Artifact root: `<local-path>/projects/commitment-based-gradient-spot-check-for-volunteer-training-30c0ac94b595`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
