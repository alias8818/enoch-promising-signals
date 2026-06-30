# Loss-Chain Spot Checks for Volunteer Gradient Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `loss-chain-spot-checks-for-volunteer-gradient-verification-b9ae9b15111c`
Run ID: `loss-chain-spot-checks-for-volunteer-gradient-verification-b9ae9b15111c-20260529T140306456153+0000`

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

At a threshold calibrated to 95% honest acceptance in the harder setting, the check rejected sign-flipped updates 99.6%, label-permuted updates 100%, scaled_50x updates 100%, and scaled_10x updates 65%, but accepted random same-norm updates 42.1%, stale updates 98.8%, and scaled_3x updates 88.8%. This supports using loss-chain checks as a cheap descent screen, not as standalone gradient verification.

## Boundaries and scale limits

Tested only on synthetic 10-class Gaussian data with a linear softmax model, 240 randomized trials per setting, forward-only verifier probes, and non-adaptive attacks. No large neural network, real volunteer network, privacy constraint, or adaptive adversary was tested.

## Claim scope

Synthetic NumPy softmax-classifier verification trials show that held-out loss-chain spot checks can reject wrong-direction, label-poisoned, and severe-overshoot submitted gradients, but do not verify exact worker provenance or freshness.

## Why it stopped

Proxy/local evidence is mixed: the mechanism catches several bad update classes but fails as standalone volunteer gradient verification because stale, aligned-scaled, and many random updates can pass.

## Recommended next action

Stop as no-paper useful signal; a bounded follow-up should test loss-chain plus norm and freshness constraints on a real small neural network task with adaptive attacks.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Loss-chain plus norm/freshness checks on a small neural worker task
- Success threshold: At 95% calibrated honest acceptance, combined checks reject at least 90% of random same-norm, stale, oversized, sign-flipped, and label-poisoned attacks while preserving final validation accuracy within 1 percentage point of an unchecked honest baseline.
- Stop condition: Stop if random or stale attack acceptance remains above 25% after adding norm and freshness checks, or if verifier cost exceeds 10 held-out forward batches per submitted update.

## Evidence references

- Artifact root: `<local-path>/projects/loss-chain-spot-checks-for-volunteer-gradient-verification-b9ae9b15111c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
