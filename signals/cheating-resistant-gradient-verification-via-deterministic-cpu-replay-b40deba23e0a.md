# Cheating-Resistant Gradient Verification via Deterministic CPU Replay

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `cheating-resistant-gradient-verification-via-deterministic-cpu-replay-b40deba23e0a`
Run ID: `cheating-resistant-gradient-verification-via-deterministic-cpu-replay-b40deba23e0a-20260629T231120668342+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/00147a51e60a

## What looked useful

Per-shard gradient commitments plus post-commit deterministic CPU replay produced 0 false positives on honest submissions, 100% detection for all-shard noisy corruption and aggregate inconsistency, and 9% to 95% sparse-cheat detection as replay coverage rose from 1/64 to 16/64 shards. The adaptive-known-challenge control had 0% detection, proving the challenge must be hidden until after a binding commit.

## Boundaries and scale limits

Synthetic single-batch CPU-only test; no real distributed trainer, transformer model, optimizer-state attack, mixed-precision path, GPU/CPU numeric mismatch, or networked commitment protocol was evaluated.

## Claim scope

On a synthetic 128-dimensional logistic-regression batch split into 64 shard commitments, deterministic CPU replay of post-commit challenged shards catches all-shard and aggregate-inconsistent cheating, and catches sparse 8-of-64 shard cheating at rates consistent with sampling coverage.

## Why it stopped

No-paper useful signal: evidence is synthetic and mechanism-level, with a central protocol caveat around challenge timing.

## Recommended next action

Run a bounded deepen test by embedding per-shard commitments and post-commit challenge sampling in a real small training loop with optimizer-state and mixed-precision controls.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real Training Loop Gradient Replay With Post-Commit Challenges
- Success threshold: At least 0.1% replay coverage detects all-shard corruption in >=99% of trials, sparse corruption follows the predicted sampling curve within 5 percentage points, honest false positives stay below 0.1%, and replay overhead remains below 5% for the tested small model.
- Stop condition: Stop if honest replay mismatch exceeds 0.1% after tolerance calibration, if post-commit challenge binding cannot be implemented, or if replay overhead exceeds 20% at the minimum useful coverage.

## Evidence references

- Artifact root: `<local-path>/projects/cheating-resistant-gradient-verification-via-deterministic-cpu-replay-b40deba23e0a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
