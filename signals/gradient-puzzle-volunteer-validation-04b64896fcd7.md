# Gradient Puzzle Volunteer Validation

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-puzzle-volunteer-validation-04b64896fcd7`
Run ID: `gradient-puzzle-volunteer-validation-04b64896fcd7-20260526T122821393734+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/1f6642089444

## What looked useful

Strict validation reliability was achieved only in the optimistic trained-volunteer regime, requiring at least 11 independent votes per item. Mixed-public, fatigued-public, and subtle-gradient regimes did not meet the threshold even at 21 votes per item.

## Boundaries and scale limits

No real human volunteers were recruited, no real gradient-puzzle UI was deployed, and the volunteer behavior model is a proxy. The result is not direct publication-grade evidence for human performance.

## Claim scope

Synthetic Monte Carlo protocol probe for volunteer majority-vote validation of binary gradient-puzzle validity under four plausible volunteer-quality regimes.

## Why it stopped

Proxy simulation supports the mechanism only under trained/optimistic volunteer assumptions and early-falsifies casual-public majority-vote validation as insufficient, but it is not full human validation.

## Recommended next action

Stop this run as a no-paper useful signal; run a bounded human pilot only if it includes training/qualification and measures individual volunteer accuracy before scaling labels.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small Human Pilot for Trained Gradient-Puzzle Validators
- Success threshold: The lower 5th percentile or bootstrap lower bound of item accuracy is at least 0.90, the upper bound of false accept rate is at most 0.05, and false reject rate is at most 0.10 with 11 or fewer votes per item.
- Stop condition: Stop if qualified individual volunteer accuracy remains below 0.75 or if 15-vote aggregation cannot meet the false accept threshold.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-puzzle-volunteer-validation-04b64896fcd7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
