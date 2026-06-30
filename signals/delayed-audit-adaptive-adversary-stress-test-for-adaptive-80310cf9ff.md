# Delayed-audit adaptive adversary stress test for adaptive-fair ledger admission

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `delayed-audit-adaptive-adversary-stress-test-for-adaptive-80310cf9ff`
Run ID: `delayed-audit-adaptive-adversary-stress-test-for-adaptive-80310cf9ff-20260620T204322819571+0000`

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

- Parent run decision: Adaptive-source and fairness stress test for evidence-ledger queue admission: enoch://control-plane/projects/adaptive-source-and-fairness-stress-test-for-evidence-ledg-f29831c3bc/runs/adaptive-source-and-fairness-stress-test-for-evidence-ledg-f29831c3bc-20260620T201201440855+0000
- Parent run decision: Evidence-Ledger-Gated Queue Admission Simulation: enoch://control-plane/projects/evidence-ledger-gated-queue-admission-simulation-295b8c09eba4/runs/evidence-ledger-gated-queue-admission-simulation-295b8c09eba4-20260620T092704033765+0000

## What looked useful

Tier 2 fixed-seed matrix found a reproducible failure mode: delayed-audit adaptive fairness can make the fairness incentive itself exploitable. Against static concentrated attackers, adaptive_fair reduces malicious admissions but creates large benign cohort disparity; against adaptive attackers, it maintains benign parity while admitting nearly all malicious traffic.

## Boundaries and scale limits

Synthetic simulator only; no real ledger trace, identity-cost model, production audit labels, multi-cohort setting, or real fee-market calibration. The result validates a local stress-test failure mode, not a broad production claim.

## Claim scope

In a two-cohort synthetic ledger admission simulator with fixed seeds, an adaptive cohort-switching adversary exploits the adaptive-fair admission controller: adaptive_fair preserves near-zero benign cohort gap but admits about 96% malicious transactions, worse than static_quota at about 49.6% and fee_priority at about 93.9%.

## Why it stopped

Tier 2 synthetic evidence directly falsified the positive robustness threshold for this adaptive-fair design: adaptive_fair was about 46 percentage points worse than static_quota under adaptive attack.

## Recommended next action

Stop this run as no-paper useful evidence; next bounded work should test a hardened adaptive-fair controller with explicit adversary-resistance constraints on the same fixed-seed matrix.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Harden adaptive-fair admission against cohort-switching audit-delay attacks
- Success threshold: Under adaptive attack at every tested delay, hardened adaptive fairness has malicious admission rate below static_quota mean 0.4963 and benign fairness gap at or below static_quota mean 0.0070, without regressing static-attack malicious admission above 0.05.
- Stop condition: Stop if no hardened policy beats static_quota on adaptive-attack malicious admission while matching static_quota benign fairness across all delays.

## Evidence references

- Artifact root: `<local-path>/projects/delayed-audit-adaptive-adversary-stress-test-for-adaptive-80310cf9ff`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
