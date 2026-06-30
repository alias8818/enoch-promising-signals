# Commit-Reveal Gradient Validation for Volunteer Training

Status: `useful_signal`
Curation bucket: `likely_stale_low_value_archive`
Curation score: `53`
Project ID: `commit-reveal-gradient-validation-for-volunteer-training-4a9a98e7a09f`
Run ID: `commit-reveal-gradient-validation-for-volunteer-training-4a9a98e7a09f-20260526T121817440905+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/2e4d3a0f91ea

## What looked useful

Commit-reveal is useful for binding a worker to bytes before reveal, but it is not a correctness check. In the primary 30% malicious run, commit-only accepted 100% of bad gradients and exactly matched no-validation loss across all five attacks. In a 50% sign-flip stress run, commit-only accepted all bad gradients and collapsed to 0.5067 mean accuracy versus 0.9770 clean reference accuracy. Spot audits and redundancy helped only according to their own coverage and assumptions.

## Boundaries and scale limits

Evidence is local and toy-scale: logistic regression, synthetic data, deterministic minibatch recomputation, no real volunteer network, no neural model, no non-IID/private data regime, no blockchain/bulletin-board deployment, and no cryptographic proof system. It supports a mechanism-level negative claim for commit-only validation, not a full production validation result.

## Claim scope

In a toy synchronous volunteer-training simulation with logistic regression, SHA-256 commit-reveal alone did not validate gradients: malicious workers could commit to fabricated gradients and later reveal them successfully, producing behavior identical to no validation.

## Why it stopped

Toy/local evidence directly falsifies the commit-only validation mechanism: commitment verification binds the later reveal to earlier bytes but accepts committed fabricated gradients. This is not a full-scale volunteer-training validation.

## Recommended next action

Stop this run as a proxy/mechanism-level early falsification of commit-only gradient validation; any next work should test a commit-plus-correctness mechanism rather than commit-reveal alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Commit-Reveal Plus Audit Budget for Small Neural Volunteer Training
- Success threshold: Across at least 5 seeds and two attack families, commit-plus-validation keeps final validation loss within 10% of clean reference, rejects at least 90% of malicious gradients, rejects less than 2% of honest gradients, and has measured overhead low enough to justify volunteer use.
- Stop condition: Stop if commit-only is again identical to no validation and every affordable correctness add-on either rejects under 70% of malicious gradients or degrades final validation loss by more than 25% versus clean reference.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-validation-for-volunteer-training-4a9a98e7a09f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
