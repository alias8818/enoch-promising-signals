# Commit-Reveal Lottery Against Volunteer Cheating

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `commit-reveal-lottery-against-volunteer-cheating-9773349d2712`
Run ID: `commit-reveal-lottery-against-volunteer-cheating-9773349d2712-20260530T050231107229+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Likely stale/low-value archive
- Score: `53`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": -15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- unsupported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/12c22dd7eb68

## What looked useful

Withholding attacks gave colluder winner-share lifts up to +0.7993 when missing secrets were omitted but all committed volunteers stayed eligible, up to +0.7767 when only revealers stayed eligible, and abort-on-missing produced up to 0.9599 abort rate while preserving winner share.

## Boundaries and scale limits

Tested n in {3,5,10,25}, colluder counts up to 5, 50,000 Monte Carlo trials per case plus small exact aggregate enumerations; not a formal proof or deployed-system audit.

## Claim scope

Simple commit-reveal volunteer lotteries with post-commit reveal withholding and naive missing-reveal handling are not cheat-resistant in the tested local mechanism models.

## Why it stopped

Bounded local mechanism evidence falsifies the simple commit-reveal anti-cheating hypothesis for common variants; broader claims would require a fully specified incentive mechanism and formal or deployment-grade validation.

## Recommended next action

Stop this run as a no-paper useful negative result; a future bounded follow-up should test incentive-complete designs with deposits, slashing, and explicit reveal-failure rules.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Incentive-complete commit-reveal lottery with slashing and fallback randomness
- Success threshold: For every tested coalition, expected utility from optimal withholding is no greater than honest reveal by more than 1% of prize value, and attacker-induced abort probability remains below 1% when deposits are rationally enforced.
- Stop condition: Stop negative if any tested coalition can gain more than 1% expected utility or induce more than 1% cheap aborts under the proposed incentive parameters.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-lottery-against-volunteer-cheating-9773349d2712`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
