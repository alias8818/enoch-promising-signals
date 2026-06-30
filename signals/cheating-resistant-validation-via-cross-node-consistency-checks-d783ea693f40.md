# Cheating-Resistant Validation via Cross-Node Consistency Checks

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cheating-resistant-validation-via-cross-node-consistency-checks-d783ea693f40`
Run ID: `cheating-resistant-validation-via-cross-node-consistency-checks-d783ea693f40-20260610T021732129803+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/7021e6dc2932

## What looked useful

Replication sharply reduces silent wrong acceptance only when validator assignment is close to independent: at 20% malicious validators, wrong acceptance fell from about 20.0% at r=1 to 5.82% at r=5 and 1.95% at r=9. Correlated assignment can erase much of the gain: at 20% malicious and r=9, a beta-binomial correlated model with concentration k=4 raised wrong acceptance to 11.01%, 5.64x the independent rate.

## Boundaries and scale limits

Simulation-only CPU run with 100000 tasks x 20 seeds per scenario across 91 scenarios; no live distributed system, real validation workload, adaptive scheduler attack, stake/reputation economics, or network-failure model was tested.

## Claim scope

Monte Carlo and analytic-binomial validation of a strict-majority cross-node digest consistency protocol under independent and correlated validator assignment, using colluding malicious validators that return a shared wrong digest.

## Why it stopped

Moderate evidence came from a bounded simulation/proxy, not a full distributed validation system; it supports the mechanism and identifies a scheduler-correlation failure mode but is not publication-grade direct evidence.

## Recommended next action

Stop this run as no-paper useful signal; next run should build a process-level verifier harness with auditable random assignment and adaptive colluding validators to test whether the simulation mechanism survives implementation effects.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Process-level cross-node verifier harness with adaptive colluding validators
- Success threshold: For 20% malicious validators, r=5 independent assignment should keep wrong acceptance within 25% relative error of the simulated 5.82% rate while correlated assignment should raise wrong acceptance by at least 1.5x, with false-positive rate under 1% in all-honest trials.
- Stop condition: Stop if all-honest false positives exceed 1%, assignment logs cannot prove independence, or independent r=5 wrong acceptance is not at least 2x lower than single-validator baseline at 20% malicious validators.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-validation-via-cross-node-consistency-checks-d783ea693f40`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
