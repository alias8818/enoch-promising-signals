# Proof-of-Step Consensus for Volunteer Training Schedules

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `proof-of-step-consensus-for-volunteer-training-schedules-725d4a398d97`
Run ID: `proof-of-step-consensus-for-volunteer-training-schedules-725d4a398d97-20260607T164655794329+0000`

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

Across adversarial cells, PoStep k=2 reduced unsafe rate by 0.0268 versus self-report with 0.0225 higher vacancy rate; PoStep k=3 reduced unsafe rate by 0.0499 with 0.0737 higher vacancy rate. Against single-verifier, k=2 and k=3 reduced unsafe rate by 0.0641 and 0.0873 respectively, but increased vacancies.

## Boundaries and scale limits

Synthetic only: 240 volunteers, 5 mentors, 10 weeks, 4 training steps, 200 trials per grid cell. No real volunteer traces, no correlated collusion clusters, no administrative overhead measurement, and no field validation.

## Claim scope

In a bounded synthetic volunteer-training schedule model with independent mentor attestations, Proof-of-Step threshold eligibility reduced unsafe assignments under false self-reporting and verifier error, with an explicit vacancy/recall tradeoff.

## Why it stopped

Synthetic proxy evidence supports the mechanism but is not direct/full validation of volunteer scheduling practice or enough for a paper.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded follow-up that tests adaptive PoStep thresholds under correlated mentor error and collusion clusters before seeking real trace validation.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Adaptive Proof-of-Step Thresholds Under Correlated Attestation Failure
- Success threshold: Adaptive PoStep reduces unsafe assignment rate by at least 50% versus self-report and by at least 30% versus single-verifier, while increasing vacancy rate by no more than 0.04 versus self-report across correlated-failure scenarios.
- Stop condition: Stop if correlated/collusion scenarios erase the safety improvement or if meeting the safety target requires vacancy-rate increase above 0.04 in most tested cells.

## Evidence references

- Artifact root: `<local-path>/projects/proof-of-step-consensus-for-volunteer-training-schedules-725d4a398d97`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
