# Adversarial Cheating Simulation Harness for Volunteer Training Validation

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `adversarial-cheating-simulation-harness-for-volunteer-training-validation-0f4c1ff86e5b`
Run ID: `adversarial-cheating-simulation-harness-for-volunteer-training-validation-0f4c1ff86e5b-20260613T225729395036+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/9ba846459ffd

## What looked useful

On 50,000 holdout simulations after a separate 10,000-row calibration split, quiz-only validation had 61.92% simulated cheater pass-through and 25.93% trained-honest false rejection; calibrated adversarial validation had 1.79% cheater pass-through and 18.28% trained-honest false rejection.

## Boundaries and scale limits

Evidence is synthetic-only: no real volunteer data, no live adversarial pilot, no real training material, no demographic or item-quality validation, and no adaptive human adversary. The 50,000-row holdout is simulation scale, not operational validation.

## Claim scope

In a seeded synthetic simulation of volunteer training validation, an adversarial policy using randomized scenarios, repeated consistency checks, canary items, and timing anomaly penalties reduced simulated cheater pass-through compared with quiz-only and quiz-plus-scenario baselines while staying under a 20% trained-honest false-reject target on holdout.

## Why it stopped

Synthetic-only evidence supports the mechanism but is not direct/full validation of real volunteer training programs.

## Recommended next action

Stop this run as no-paper useful signal; next run should validate the same harness on anonymized historical volunteer validation records or a small consented red-team volunteer pilot with a pre-registered false-reject ceiling.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Held-out volunteer pilot for adversarial training validation
- Success threshold: At least 50% lower cheating pass-through than quiz-plus-scenario on held-out labeled data with trained-honest false rejection <= 20% and no evidence that gains come from a single brittle canary item.
- Stop condition: Stop if adversarial features fail to improve cheating pass-through by 25% relative to quiz-plus-scenario at the same false-reject ceiling, or if labels/data access are insufficient to estimate both cheater pass-through and trained-honest false rejection.

## Evidence references

- Artifact root: `<local-path>/projects/adversarial-cheating-simulation-harness-for-volunteer-training-validation-0f4c1ff86e5b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
