# Commit-Reveal Gradient Validation for Untrusted Volunteers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-gradient-validation-for-untrusted-volunteers-2cc728b5a084`
Run ID: `commit-reveal-gradient-validation-for-untrusted-volunteers-2cc728b5a084-20260602T133011015380+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/6ddf27822c98

## What looked useful

For 1% large coordinate corruption, detection was about 7-8% with 8 audited coordinates, 27-29% with 32, 70-76% with 128, and 99.6% with 512; honest false positives were 0%. Commit-reveal eliminates the modeled no-commit adaptive challenge failure but does not by itself validate gradients.

## Boundaries and scale limits

Synthetic 10,000-dimensional float32 gradients, 500 trials per setting, six attack modes, no real model training, no networked volunteers, no bandwidth or validator recomputation benchmark beyond SHA-256 hashing.

## Claim scope

Commit-reveal is useful as a binding step that prevents post-challenge adaptation in random coordinate gradient audits, but sampled-coordinate audits only detect corruption with probability determined by audit coverage and corruption density.

## Why it stopped

No-paper useful signal: bounded synthetic evidence supports commit-reveal as an anti-adaptation component, but also shows it is not a general cheap gradient correctness validator without substantial audit coverage or additional mechanisms.

## Recommended next action

Run a bounded deepen follow-up on a small real model with malicious worker updates, comparing training quality and validation overhead against redundancy or robust aggregation baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-model audit-cost curve for commit-reveal gradient validation
- Success threshold: Show a regime where malicious-worker training quality remains within 2% relative validation metric of honest training while validator overhead is below a clearly reported baseline such as full redundant recomputation.
- Stop condition: Stop if audit coverage needed to preserve training quality is within a small constant factor of full recomputation or if adaptive/non-adaptive malicious workers are not measurably distinguished.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-validation-for-untrusted-volunteers-2cc728b5a084`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
