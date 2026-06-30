# Verifiable checkpoint credit system for volunteer GPU workers

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `verifiable-checkpoint-credit-system-for-volunteer-gpu-workers-49bf3de6e914`
Run ID: `verifiable-checkpoint-credit-system-for-volunteer-gpu-workers-49bf3de6e914-20260608T024745258914+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m2.7: enoch://research-facility/provider/minimax/minimax-m2.7/e4978c02a2ea

## What looked useful

Primary 32-chunk audits covered 1.5625% of an 8 MiB synthetic checkpoint and verified in 0.00144 seconds. They detected 10% bad chunks at 96.36%, 5% at 81.52%, and 1% at only 27.26%. Ledger checks detected equivocation, stale root reuse, and broken checkpoint chains, while a valid wrong-objective checkpoint was accepted by checkpoint-only verification.

## Boundaries and scale limits

Tested only on synthetic 8 MiB checkpoints in a single-process CPU simulator. No real GPU training, real model checkpoints, distributed networking, collusion, reward economics, or production ledger behavior was validated.

## Claim scope

A synthetic local checkpoint-credit simulator shows that SHA-256 Merkle checkpoint commitments plus deterministic spot audits can cheaply verify checkpoint possession/integrity and catch simple ledger attacks, but checkpoint-only credit does not verify useful training work and has weak one-shot detection for sparse missing/tampered chunks.

## Why it stopped

The bounded local experiment supports checkpoint integrity as a component but early-falsifies the standalone checkpoint-credit idea as a verifier of useful volunteer GPU work; this is a proxy/local result, not a full production validation.

## Recommended next action

Stop this run as no-paper useful signal; the next bounded test should add real training-progress validation such as loss replay, gradient spot checks, or signed trainer telemetry and compare it against checkpoint-only credit.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Add training-progress audits to checkpoint credit
- Success threshold: Reject at least 95% of wrong-objective/arbitrary-checkpoint submissions and at least 95% of 5% tamper/missing-chunk submissions with false positive rate under 1% and verifier overhead under 5% of worker step time on a small real training workload.
- Stop condition: Stop if progress audits cannot distinguish arbitrary valid checkpoints from real training checkpoints without replaying most of the training step or exceeding 5% verifier overhead.

## Evidence references

- Artifact root: `<local-path>/projects/verifiable-checkpoint-credit-system-for-volunteer-gpu-workers-49bf3de6e914`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
