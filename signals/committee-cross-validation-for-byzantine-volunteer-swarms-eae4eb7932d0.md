# Committee Cross-Validation for Byzantine Volunteer Swarms

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `committee-cross-validation-for-byzantine-volunteer-swarms-eae4eb7932d0`
Run ID: `committee-cross-validation-for-byzantine-volunteer-swarms-eae4eb7932d0-20260525T075201105221+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/2ed250168d09

## What looked useful

Committee cross-validation is most useful as a reputation signal rather than as a standalone replacement for majority voting. In the corrected medium simulation, mean final error was 0.1417 for majority, 0.1419 for committee_cv, and 0.0591 for trust_cv; mean wrong-primary acceptance was 0.1216, 0.0513, and 0.0165 respectively.

## Boundaries and scale limits

Synthetic binary tasks only; no real volunteer traces, non-binary outputs, latency/cost model, Sybil churn, adaptive long-horizon adversary, or live distributed system validation. The result is a bounded mechanism signal, not a publication-grade validation.

## Claim scope

In a synthetic 200-worker binary-task swarm with 10-40% Byzantine identities, 92% honest accuracy, committee sizes 3/5/7, and 30 seeds per cell, committee cross-validation alone matched majority-vote final accuracy but reduced wrong-primary acceptance; adding persistent trust updates from committee disagreement substantially reduced final error and bad-primary acceptance.

## Why it stopped

The run produced moderate synthetic evidence for the mechanism but not direct/full evidence from a real or trace-driven volunteer swarm; committee-only accuracy was not better than majority voting, so the scoped result is useful but not paper-positive.

## Recommended next action

Stop this run as no-paper useful signal; next bounded work should test the trust-updating mechanism against identity churn and adaptive Sybil replacement before any scale-up claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trust-Weighted Committee Cross-Validation Under Sybil Churn
- Success threshold: At 20-30% Byzantine control with churn, trust_cv should reduce wrong-primary acceptance by at least 2x versus majority while keeping honest false-flag rate below 15% and final error below committee_cv by at least 25% at the same committee size.
- Stop condition: Stop as negative if adaptive churn removes at least half of the trust_cv error advantage or pushes honest false-flag rate above 20% in two committee sizes.

## Evidence references

- Artifact root: `<local-path>/projects/committee-cross-validation-for-byzantine-volunteer-swarms-eae4eb7932d0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
