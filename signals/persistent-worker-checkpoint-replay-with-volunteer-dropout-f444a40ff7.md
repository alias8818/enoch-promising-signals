# Persistent-worker checkpoint replay with volunteer dropout and multiple checkpoints

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `persistent-worker-checkpoint-replay-with-volunteer-dropout-f444a40ff7`
Run ID: `persistent-worker-checkpoint-replay-with-volunteer-dropout-f444a40ff7-20260613T060552239193+0000`

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

- Parent run decision: PyTorch multi-process checkpoint/replay test for volunteer-style SGD: enoch://control-plane/projects/pytorch-multi-process-checkpoint-replay-test-for-volunteer-6aaa18b708/runs/pytorch-multi-process-checkpoint-replay-test-for-volunteer-6aaa18b708-20260613T053349900912+0000
- Parent run decision: Volunteer Distributed Training: Checkpoint-Based Fault Tolerance: enoch://control-plane/projects/volunteer-distributed-training-checkpoint-based-fault-tolerance-b646310a3117/runs/volunteer-distributed-training-checkpoint-based-fault-tolerance-b646310a3117-20260613T051232636974+0000

## What looked useful

Across 40,000 trials, multi-checkpoint replay achieved 1.000 correctness at 30% dropout versus 0.016 no-checkpoint, 0.472 transcript reconstruction, and 0.844 single-latest checkpoint. At 50% dropout it improved over all controls but only reached 0.538 correctness, limiting the robustness claim.

## Boundaries and scale limits

No live persistent-worker controller was exercised. Volunteer dropout, checkpoint loss, task semantics, and transcript reconstruction defects were simulated locally. Evidence is medium synthetic confirmation, not production or publication-grade validation.

## Claim scope

In a deterministic synthetic replay benchmark with fixed seeds, 18-122 step stateful tasks, modeled volunteer dropout, and modeled latest-checkpoint loss, multi-checkpoint replay improves completion/correctness and reduces repeated work versus no-checkpoint and transcript-reconstruction baselines; it also beats a single-latest-checkpoint ablation at 30% and 50% dropout.

## Why it stopped

Tier 2 local synthetic evidence supports the fallback-checkpoint mechanism but does not provide real-system or publication-grade evidence.

## Recommended next action

Stop this run as no-paper useful signal; next run should validate the same mechanism in a real persistent-worker replay harness with induced dropout and recorded checkpoint payloads.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-worker checkpoint replay harness with induced volunteer dropout
- Success threshold: At 30% induced dropout, multi-checkpoint replay must improve correctness by at least 10 percentage points over single-latest checkpoint and by at least 25 percentage points over transcript reconstruction while keeping mean step overhead below 2.5x.
- Stop condition: Stop if multi-checkpoint replay fails to exceed single-latest correctness by 5 percentage points at 30% dropout or if real checkpoint payloads cannot be replayed deterministically.

## Evidence references

- Artifact root: `<local-path>/projects/persistent-worker-checkpoint-replay-with-volunteer-dropout-f444a40ff7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
