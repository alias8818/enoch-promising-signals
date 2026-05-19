# Commit-Reveal Gradient Validation for Cheating-Resistant Volunteer Training

Status: `useful_signal`
Project ID: `commit-reveal-gradient-validation-for-cheating-resistant-volunteer-training-10aad0bda5d9`
Run ID: `commit-reveal-gradient-validation-for-cheating-resistant-volunteer-training-10aad0bda5d9-20260518T045351978854+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/cc45d3b9e238

## What looked useful

Commit-reveal reduced harmful hidden-gradient acceptance relative to public validation, especially with larger hidden validation batches. In five-seed replication at validation batch 1024, public harmful acceptance averaged 0.7904 while commit-reveal harmful acceptance averaged 0.0456. Small validation batches remained vulnerable, so commit-reveal alone is insufficient.

## Boundaries and scale limits

Synthetic binary logistic regression only; no LLM-scale gradients, no real volunteer network, no multi-step distributed training, no collusion/Sybil/security-system validation, and only local SHA-256 commitment consistency.

## Claim scope

Toy logistic-regression mechanism test of public validation versus commit-reveal hidden validation for malicious gradient acceptance under a norm cap and validation-loss check.

## Why it stopped

Proxy/toy mechanism evidence supports validation hiding as useful but does not validate the broad cheating-resistant volunteer-training claim.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should add repeated independent hidden validation challenges and run multi-worker training over many steps with honest-acceptance and harmful-acceptance thresholds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Repeated Hidden Validation for Multi-Step Volunteer Gradient Training
- Success threshold: At least 95% honest-gradient acceptance, less than 1% accepted harmful updates, and final test loss within 2% of all-honest training at a validation overhead no more than 4x the single-check baseline.
- Stop condition: Stop as negative if repeated hidden validation cannot reduce accepted harmful updates below 5% without dropping honest acceptance below 90% or materially degrading final test loss.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-validation-for-cheating-resistant-volunteer-training-10aad0bda5d9`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
