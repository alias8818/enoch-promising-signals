# Deterministic CPU replay across process restarts with DataLoader workers and threaded kernels

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `deterministic-cpu-replay-across-process-restarts-with-data-5c2ec58fee`
Run ID: `deterministic-cpu-replay-across-process-restarts-with-data-5c2ec58fee-20260610T174352036934+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Top external-researcher candidates
- Score: `98`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 15, "hypothesis_status": 30, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- supported hypothesis_status
- source lineage present
- bounded follow-up is specified
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Parent run decision: Deterministic-Replay Gradient Verification on CPU: enoch://control-plane/projects/deterministic-replay-gradient-verification-on-cpu-d87145400ce6/runs/deterministic-replay-gradient-verification-on-cpu-d87145400ce6-20260610T144111964244+0000
- Parent run decision: Framework-level deterministic CPU gradient replay with process restarts: enoch://control-plane/projects/framework-level-deterministic-cpu-gradient-replay-with-pro-ae63f60887/runs/framework-level-deterministic-cpu-gradient-replay-with-pro-ae63f60887-20260610T152729884910+0000

## What looked useful

Exact restart replay is achievable and verifiable with batch, loss, prediction, model-state, and optimizer-state hashes, but the full replay capsule did not beat the simple main-process seeding baseline: both achieved 12/12 exact groups in the medium matrix, while the unseeded control achieved 0/12.

## Boundaries and scale limits

The evidence is bounded to synthetic map-style datasets, 60-step small-model CPU training, DataLoader workers up to 4, and one host/library stack; it does not cover GPU, distributed training, IterableDataset, persistent long-running workers, larger models, or third-party augmentation pipelines.

## Claim scope

In PyTorch 2.12 CPU subprocess restarts on this host, exact replay was achieved for a small MLP with map-style DataLoader workers, torch/Python/NumPy random augmentation, fixed seeds, and CPU thread counts 1 and 4.

## Why it stopped

Medium direct validation supported deterministic replay but falsified the incremental novelty threshold because the real main_seed_only baseline matched the capsule across all tested groups.

## Recommended next action

Stop this line as no-paper evidence unless a harder realistic pipeline is introduced where a full replay capsule can be compared against PyTorch's modern seeding baseline.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay stress test for realistic augmentation and persistent worker pipelines
- Success threshold: Full capsule achieves at least 95% exact replay groups and improves by at least 30 percentage points over main_seed_only on at least one realistic pipeline, with unseeded controls failing as expected.
- Stop condition: Stop if main_seed_only remains exact across all realistic stress pipelines or if capsule failures cannot be traced to controllable replay state.

## Evidence references

- Artifact root: `<local-path>/projects/deterministic-cpu-replay-across-process-restarts-with-data-5c2ec58fee`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
