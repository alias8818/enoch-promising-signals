# Gradient Spot-Check Consensus for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-spot-check-consensus-for-volunteer-training-c0f0892d38b7`
Run ID: `gradient-spot-check-consensus-for-volunteer-training-c0f0892d38b7-20260605T020012464826+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/47a251bb1026

## What looked useful

Dense gradient corruptions are easy to catch with tiny random coordinate checks in the toy setup, and filtering them can rescue training from sign-flip Byzantine failure. However, 2 of 162 checked coordinates gives only about 1.23% single-round detection for a one-coordinate sparse corruption, so the mechanism needs adaptive/sparse robustness and true partial-gradient cost validation before any paper claim.

## Boundaries and scale limits

Toy synthetic data, small model, IID local batches, trusted full-gradient recomputation before coordinate sampling, non-adaptive dense attacks for training runs, and no production communication/privacy/partial-autograd overhead measurement. Sparse/adaptive attacks are only analytically bounded and are weakly detected at the tested spot-check fraction.

## Claim scope

In a synthetic 24-volunteer synchronous SGD setup with a 162-parameter MLP, 25% dense malicious volunteers, and 2 randomly checked coordinates per submitted gradient, spot-check filtering rejected dense corrupted gradients with 100% detection and 0% false rejects across 8 seeds and preserved clean-oracle validation accuracy under sign-flip attack.

## Why it stopped

No-paper useful signal: bounded toy evidence supports dense-corruption filtering but does not validate production cost savings or robustness to sparse/adaptive attacks.

## Recommended next action

Run a bounded deepen follow-up implementing true partial-coordinate verification and sparse/adaptive attacks on a medium non-IID volunteer simulation; stop paper consideration unless sparse detection and overhead are both favorable.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Partial-coordinate verifier under sparse adaptive volunteer attacks
- Success threshold: At least 95% dense-attack detection, at least 80% detection of harmful sparse/adaptive attacks within 10 rounds, false reject rate below 2%, final accuracy within 1 percentage point of clean oracle under harmful attacks, and verifier overhead below 25% of full-gradient verification.
- Stop condition: Stop if true partial-coordinate verification is not materially cheaper than full recomputation, or if sparse/adaptive attacks that harm training evade detection in more than 20% of 10-round windows at practical check rates.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-spot-check-consensus-for-volunteer-training-c0f0892d38b7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
