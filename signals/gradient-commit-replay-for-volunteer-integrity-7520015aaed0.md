# Gradient-Commit Replay for Volunteer Integrity

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `gradient-commit-replay-for-volunteer-integrity-7520015aaed0`
Run ID: `gradient-commit-replay-for-volunteer-integrity-7520015aaed0-20260607T174648404811+0000`

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

- Provider-backed Research Facility batch: moonshotai/kimi-k2.6: enoch://research-facility/provider/moonshotai/kimi-k2.6/95be05aca633

## What looked useful

Replay auditing is viable as a narrow exact-gradient integrity check, but per-update random auditing alone leaves roughly 1 - audit_rate malicious updates unapplied only when audited; at low audit rates the strongest label-flip attack still materially harms accuracy.

## Boundaries and scale limits

Synthetic data, one small MLP, one local GPU process, no real volunteer network, no privacy constraints, no cross-device determinism study, no large model, no worker-level reputation, and only three seeds.

## Claim scope

On a small deterministic PyTorch MLP classification task with 30% malicious simulated volunteers, random replay audits of SHA-256-committed gradients detect sampled zero, random, scaled, and label-flipped gradients with 100% audited detection and zero honest false positives; stale gradients are detected when the stale snapshot differs from the current model.

## Why it stopped

Bounded local evidence supports the replay detection mechanism but does not validate the broader volunteer integrity claim; low audit rates still allow many malicious updates through, so this is not publication-grade positive evidence.

## Recommended next action

Stop this run as no-paper useful evidence; run a bounded follow-up that adds worker-level quarantine or reputation after a failed replay audit and tests whether 5-10% audits can protect accuracy under persistent label-flip attackers.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-triggered quarantine for low-rate volunteer gradient audits
- Success threshold: At 30% persistent malicious workers, 10% auditing with quarantine keeps mean accuracy within 1 percentage point of clean training for label_flip and zero/random attacks, with audited honest false positives remaining zero.
- Stop condition: Stop if quarantine at 10% auditing still leaves label_flip accuracy more than 3 percentage points below clean or introduces any honest false positives under deterministic replay.

## Evidence references

- Artifact root: `<local-path>/projects/gradient-commit-replay-for-volunteer-integrity-7520015aaed0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
