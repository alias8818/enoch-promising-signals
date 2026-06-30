# Commit-Reveal Weight Updates for Volunteer Training Verification

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-weight-updates-for-volunteer-training-verification-3efcf7b20a8b`
Run ID: `commit-reveal-weight-updates-for-volunteer-training-verification-3efcf7b20a8b-20260524T054343888932+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/27bbaca74165

## What looked useful

Commit-reveal is useful as a probabilistic audit mechanism for deterministic replayable training steps, not as a standalone proof of all volunteer training work. With roughly 25-33% unique step coverage, 5% tampering was detected in 96% of trials with zero honest false positives in this simulation; final accuracy/loss moved too little to detect several invalid-work cases.

## Boundaries and scale limits

Pure-Python synthetic logistic regression only: 1024 samples, 16 dimensions, 200 SGD steps, 100 trials per condition, simple SGD, local CPU worker. No neural-network, mixed-precision, distributed, private-data, bandwidth, or adaptive-adversary validation was performed.

## Claim scope

In a deterministic synthetic SGD task where the verifier can recompute audited updates, a per-step SHA-256 commit-reveal chain with random contiguous audit windows detects incorrect committed updates with probability close to sampled-step coverage, while final loss alone can miss mild invalid work.

## Why it stopped

Synthetic proxy evidence supports the narrow audit mechanism but does not validate the broad volunteer-training verification claim or justify paper writing.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should implement the same audit protocol on a small neural network with optimizer-state commitments and measured audit bandwidth/runtime.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Neural optimizer-state commit-reveal audits for volunteer training
- Success threshold: At least 90% detection of 5% tampering with zero false positives across honest trials and documented audit overhead on the small neural-network task.
- Stop condition: Stop if deterministic replay cannot be made stable, honest false positives occur, or 5% tampering detection remains below 75% at audit coverage comparable to this run.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-weight-updates-for-volunteer-training-verification-3efcf7b20a8b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
