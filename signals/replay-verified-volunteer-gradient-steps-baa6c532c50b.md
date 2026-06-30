# Replay-Verified Volunteer Gradient Steps

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `replay-verified-volunteer-gradient-steps-baa6c532c50b`
Run ID: `replay-verified-volunteer-gradient-steps-baa6c532c50b-20260613T084141991940+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/5d4162bfe9c9

## What looked useful

Sampled deterministic replay is a plausible low-cost audit mechanism for volunteered gradient steps when per-example contributions are available, but the un-audited fraction remains a real attack surface and the protocol needs direct training-loop, adaptive-adversary, and privacy/bandwidth tests.

## Boundaries and scale limits

Synthetic data, 32-dimensional logistic regression, non-adaptive corruptions, 500 trials per cell, no real distributed training, no deep model, no privacy-preserving commitment scheme, and an explicit per-example gradient disclosure assumption. This is not production or paper-grade validation.

## Claim scope

In a deterministic toy logistic-regression setting where volunteers disclose per-example gradients for a claimed microbatch, random replay auditing detects sparse corrupted gradient contributions with probability increasing with audit coverage: k=8 of 64 caught about 66-69%, k=16 caught about 89-90%, and full replay caught 100% of tested synthetic corruptions with zero false positives for honest and tiny-roundoff controls.

## Why it stopped

No-paper useful signal: this run produced synthetic mechanism evidence, not direct/full validation of volunteer distributed training.

## Recommended next action

Run a bounded PyTorch or NumPy training-loop follow-up that measures validation-loss impact under bad volunteer updates for no replay, sampled replay, and full replay controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Training-Loop Utility of Replay-Verified Volunteer Gradient Steps
- Success threshold: Sampled replay at <=25% audit coverage achieves validation loss within 5% of full replay while rejecting at least 80% of harmful updates and outperforming no-replay under the same injected attack budget.
- Stop condition: Stop if sampled replay fails to improve validation loss over no replay in two seeded runs, or if overhead approaches full replay without matching full replay utility.

## Evidence references

- Artifact root: `<local-path>/projects/replay-verified-volunteer-gradient-steps-baa6c532c50b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
