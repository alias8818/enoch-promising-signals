# Framework-integrated deterministic replay under partial participation and dropout

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `framework-integrated-deterministic-replay-under-partial-pa-5ca6301c29`
Run ID: `framework-integrated-deterministic-replay-under-partial-pa-5ca6301c29-20260620T133321992044+0000`

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

- Parent run decision: Framework-level deterministic replay for non-IID federated gradient validation: enoch://control-plane/projects/framework-level-deterministic-replay-for-non-iid-federated-6ff8b31f2a/runs/framework-level-deterministic-replay-for-non-iid-federated-6ff8b31f2a-20260620T131632459404+0000
- Parent run decision: Deterministic Replay Verification for CPU Federated Gradient Validation: enoch://control-plane/projects/deterministic-replay-verification-for-cpu-federated-gradient-validation-4e601681087a/runs/deterministic-replay-verification-for-cpu-federated-gradient-validation-4e601681087a-20260620T123552224540+0000

## What looked useful

Medium-grid evidence supports the mechanism: integrated event replay reached 1.000 exact replay over 120 trials and 1,343,880 replayed events, while global RNG replay reached 0.000, per-participant replay without the event log reached 0.200, and event-log replay with noncanonical order-sensitive aggregation reached 0.333.

## Boundaries and scale limits

Synthetic integer-state participant updates only; not integrated with a real LangGraph/Ray/Flower/PyTorch DDP runtime; no model gradients, network faults, process crashes, storage durability testing, or multi-node scale.

## Claim scope

In a deterministic local simulator with 8 fixed seeds, 64 participants, 240 rounds, five dropout rates, and three delivery reorder rates, event-sourced replay with per-participant deterministic streams and canonical aggregation exactly reproduced all original state digests while baseline and ablation strategies diverged.

## Why it stopped

Tier 2 simulator evidence supports the mechanism but remains proxy evidence for framework-integrated replay, so this run is no-paper useful signal rather than paper-positive validation.

## Recommended next action

Run one bounded deepen follow-up that implements the replay contract inside a real local orchestration framework and repeats the same dropout/reorder baseline and ablation grid; do not write a paper from the simulator-only evidence.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-framework deterministic replay adapter under injected dropout
- Success threshold: Integrated adapter exact replay rate is 1.000 over at least 5 seeds x 3 dropout rates x 2 reorder settings, while every baseline or ablation has exact replay rate <= 0.5 and at least one baseline fails by round 1 median.
- Stop condition: Stop if the real framework cannot expose enough deterministic scheduling or event hooks to replay outputs, or if integrated replay exact rate falls below 1.000 after fixing implementation bugs documented in failure cases.

## Evidence references

- Artifact root: `<local-path>/projects/framework-integrated-deterministic-replay-under-partial-pa-5ca6301c29`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
