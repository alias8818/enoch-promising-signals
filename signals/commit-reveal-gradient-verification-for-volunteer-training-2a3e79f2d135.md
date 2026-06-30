# Commit-Reveal Gradient Verification for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `commit-reveal-gradient-verification-for-volunteer-training-2a3e79f2d135`
Run ID: `commit-reveal-gradient-verification-for-volunteer-training-2a3e79f2d135-20260611T173101038502+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/566374f3a4d9

## What looked useful

Commit-reveal converts spot checking from an adaptively avoidable test into a probabilistic detection test: with 64 checked coordinates, malicious pass rates were 0.0274 for 5% poisoned coordinates, 0.0010 for 10%, and 0.0000 observed for 20%, while no-commit adaptive reporting passed at 1.0. In the toy training proxy, mean final loss improved from 68.048 without verification and 65.248 with no-commit spot checks to 55.037 with commit-reveal, versus 47.576 for an honest-all control.

## Boundaries and scale limits

Synthetic 512-dimensional linear regression only; 24 workers, 25% adversarial workers, 80 rounds, 12 replicates. No real volunteer network, neural-network training, privacy setting, Sybil resistance, bandwidth measurement, or large-model validation was tested.

## Claim scope

In a deterministic synthetic CPU-local experiment, commit-before-challenge plus reveal-after-challenge reduced adaptive coordinate-poisoning pass rates according to the expected hypergeometric miss probability and improved toy federated linear-regression loss versus no verification and no-commit spot checks.

## Why it stopped

Proxy-only bounded mechanism test supports the commit-reveal detection mechanism but does not directly validate volunteer training at model or deployment scale.

## Recommended next action

Stop this run as no-paper useful signal; run a bounded deepen follow-up on a small neural-network federated task with verifier overhead measurements.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal Gradient Verification on a Small Neural Federated Task
- Success threshold: Commit-reveal reduces malicious pass rate by at least 90% versus no-commit spot checks and improves final validation loss by at least 10% versus no verification without more than 25% verifier wall-clock overhead on the bounded task.
- Stop condition: Stop if verifier overhead exceeds 50% wall-clock on the small task or if commit-reveal fails to improve validation loss versus no-commit spot checks across matched seeds.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-verification-for-volunteer-training-2a3e79f2d135`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
