# Activation-Hash Spot Checks for Volunteer Gradient Verification

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `activation-hash-spot-checks-for-volunteer-gradient-verification-6194a6f9c1c9`
Run ID: `activation-hash-spot-checks-for-volunteer-gradient-verification-6194a6f9c1c9-20260531T145300926508+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/b744dcbcced0

## What looked useful

Activation-hash spot checks detected tampered activation commitments but accepted zero, random, scaled, and stale-batch gradients with 100% pass rate when those gradients were paired with correct forward activation hashes.

## Boundaries and scale limits

Toy MLP, synthetic minibatches, single-process CPU experiment, 200 verifier trials; not a transformer-scale or distributed volunteer deployment. The negative result targets the activation-only protocol invariant, not production performance.

## Claim scope

In a deterministic NumPy 3-layer MLP protocol test, random spot checks of forward activation hashes did not verify volunteer-submitted gradients when the volunteer supplied correct activation commitments but corrupted the gradient.

## Why it stopped

Proxy-sized but direct protocol counterexamples falsified activation-only hash spot checks as gradient verification; this is not a full deployment validation.

## Recommended next action

Stop treating activation-only hashes as gradient verification; the bounded next test is to add backward/VJP challenge checks that bind sampled activations to claimed gradients.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Backward Challenge Spot Checks for Volunteer Gradient Verification
- Success threshold: Reject at least 95% of the four gradient-forgery strategies with no honest false rejects in at least 200 trials, while verifier work remains below 25% of full gradient recomputation on the toy MLP.
- Stop condition: Stop if any correct-forward gradient forgery still passes above 20% under the fixed challenge budget or if verifier work approaches full recomputation.

## Evidence references

- Artifact root: `<local-path>/projects/activation-hash-spot-checks-for-volunteer-gradient-verification-6194a6f9c1c9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
