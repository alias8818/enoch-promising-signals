# Volunteer training cheating-resistant validation via lightweight probabilistic verification checks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `volunteer-training-cheating-resistant-validation-via-lightweight-probabilistic-verification-chec-ea8e6c2cebe6`
Run ID: `volunteer-training-cheating-resistant-validation-via-lightweight-probabilistic-verification-chec-ea8e6c2cebe6-20260614T062948034031+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/b71a2bd1b483

## What looked useful

A 13-item randomized check with a 10-correct threshold reached 96.89% detection and 3.42% honest false-fail for a 30% answer-leak adversary, but only 78.09% detection for a 50% answer-leak adversary. Weak honest learning could not reach the 90% detection target while keeping honest false-fail <=5%, even with up to 15 minutes burden.

## Boundaries and scale limits

Synthetic per-item probabilities only; no real volunteers, real training curriculum, real item-bank leakage process, accessibility effects, collusion, retention, or operational administrator workload were measured.

## Claim scope

In a transparent binomial model of randomized volunteer-training verification checks, lightweight probabilistic checks can detect no-mastery or 30% leaked-bank cheating with <=5% honest false-fail and <=10 minutes burden, but not 50% leaked-bank cheating or weak honest learning under the same burden target.

## Why it stopped

Closed as a no-paper useful signal: the local evidence is a synthetic/probabilistic mechanism test, not direct full validation.

## Recommended next action

Run a bounded sandbox study with real volunteer-training content, seeded item leakage, and measured honest-volunteer false-fail before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Sandbox volunteer-training randomized verification with seeded answer leakage
- Success threshold: Randomized verification beats the fixed quiz baseline by >=20 percentage points in cheating detection while keeping honest false-fail <=5% and median added burden <=10 minutes.
- Stop condition: Stop if honest false-fail exceeds 10%, if seeded 30% leakage detection is below 85%, or if item authoring/administration burden exceeds feasible volunteer-program constraints.

## Evidence references

- Artifact root: `<local-path>/projects/volunteer-training-cheating-resistant-validation-via-lightweight-probabilistic-verification-chec`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
