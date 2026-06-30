# Commit-Reveal Gradient Validation for Volunteer Training

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-gradient-validation-for-volunteer-training-a86fea329e1d`
Run ID: `commit-reveal-gradient-validation-for-volunteer-training-a86fea329e1d-20260526T114801139236+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/e560ee96bbc0

## What looked useful

Commit-reveal prevents adaptive evasion of sampled validation: detection matched sample rate (about 5%, 10%, and 25%) while pre-announced challenges detected 0% because malicious workers behaved honestly on known checks. However, sampled validation alone leaves most bad gradients accepted at low sampling rates and is not sufficient evidence for robust volunteer training.

## Boundaries and scale limits

CPU-only synthetic model, 30 seeds, 64 volunteers, 100 rounds, 128-dimensional logistic regression, public recomputable shards only; no neural network, private data, quantization, network adversary, Sybil model, validator compromise, or reputation penalty was tested.

## Claim scope

Synthetic logistic-regression volunteer training with deterministic public shards and exact validator recomputation: commit-reveal post-commit challenges provide accountable sampled detection of bad gradients at approximately the validation sample rate.

## Why it stopped

Proxy/local synthetic evidence supports the accountability mechanism but does not validate robust volunteer neural training or private-data gradient correctness.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add reputation/penalty dynamics to measure whether sampled accountable detection changes attacker payoff and training quality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal Gradient Validation with Reputation Penalties
- Success threshold: At 10% validation or lower, reputation-backed commit-reveal reduces accepted malicious gradients by at least 50% after warmup with no more than 1% honest false exclusions and improves final validation accuracy versus no validation in the 50% malicious stress condition.
- Stop condition: Stop if reputation penalties fail to reduce accepted malicious gradients by at least 25% at 10% validation, or if honest false exclusions exceed 1% under exact recomputation.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-validation-for-volunteer-training-a86fea329e1d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
