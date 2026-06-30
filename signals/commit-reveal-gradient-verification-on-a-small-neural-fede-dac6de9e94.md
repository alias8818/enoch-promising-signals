# Commit-Reveal Gradient Verification on a Small Neural Federated Task

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `commit-reveal-gradient-verification-on-a-small-neural-fede-dac6de9e94`
Run ID: `commit-reveal-gradient-verification-on-a-small-neural-fede-dac6de9e94-20260611T210802450952+0000`

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

- Parent run decision: Commit-Reveal Gradient Verification for Volunteer Training: enoch://control-plane/projects/commit-reveal-gradient-verification-for-volunteer-training-2a3e79f2d135/runs/commit-reveal-gradient-verification-for-volunteer-training-2a3e79f2d135-20260611T173101038502+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/566374f3a4d9

## What looked useful

Commit-reveal is useful as a payload-integrity and naive-replay guard but is not semantic gradient verification. Freshly committed stale, noisy, or sign-flipped gradients passed verification at 100% acceptance because the revealed bytes matched their commitments.

## Boundaries and scale limits

Synthetic 3-class task, 8 clients, 4 clients per round, 60 rounds, one malicious client, no privacy layer, no network adversary, no collusion, and no proof that freshly committed gradients were computed correctly from claimed private data.

## Claim scope

In a five-seed small NumPy MLP federated-learning task with non-IID synthetic clients, commit-reveal verified byte-level gradient payload integrity: it preserved honest training, rejected all post-commit tampering attempts, and rejected all stale reveals of old commitments/metadata.

## Why it stopped

Tier 1 direct small test supports payload integrity but directly falsifies the stronger claim that commit-reveal alone verifies gradient correctness.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should add a semantic acceptance layer or proof/audit mechanism and require rejection of freshly committed bad gradients without harming honest convergence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Semantic Gradient Acceptance Layer for Commit-Reveal FL
- Success threshold: Reject >=95% of fresh bad-gradient recommits while keeping honest final accuracy within 0.02 absolute of the honest baseline and false rejects at 0 or explicitly bounded.
- Stop condition: Stop as negative if the semantic layer rejects less than 80% of fresh bad-gradient recommits or reduces honest final accuracy by more than 0.02 absolute across five seeds.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-gradient-verification-on-a-small-neural-fede-dac6de9e94`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
