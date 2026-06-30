# Verifiable Microbatch Replays for Volunteer Training

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `verifiable-microbatch-replays-for-volunteer-training-d7c3c0433735`
Run ID: `verifiable-microbatch-replays-for-volunteer-training-d7c3c0433735-20260525T060020891522+0000`

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

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/4f14132308e8

## What looked useful

Observed detection tracked 1 - (1 - audit_rate)^corrupted_microbatches with mean absolute error 0.0249 and max error 0.0656 across four attack classes and four audit rates; 20% audit detected about 94% of corrupted 500-step runs with about 100 audited microbatches.

## Boundaries and scale limits

Synthetic integer perceptron-style updates only; no real deep-learning framework, floating-point nondeterminism, GPU kernels, adaptive adversaries, real volunteers, privacy constraints, checkpoint storage optimization, or distributed network costs were tested.

## Claim scope

In a dependency-free synthetic exact-integer microbatch training simulation, SHA-256 committed pre-state/delta/post-state records plus random deterministic replay audits detected corrupted volunteer update claims with run-level probability close to the independent sampling expectation and produced zero false rejects across 1,280 trial runs.

## Why it stopped

No-paper closure: the current result is useful but proxy-only synthetic evidence, not a full validation of volunteer model training.

## Recommended next action

Run a bounded deepen test on a real deterministic PyTorch training loop to measure false rejects, replay tolerance, checkpoint overhead, and detection under the same audit-rate grid.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Deterministic PyTorch Microbatch Replay Audit
- Success threshold: False rejects below 0.1%, mean absolute detection-probability error below 0.10, and replay/checkpoint overhead measured for at least 1,000 real microbatches.
- Stop condition: Stop as negative if deterministic replay cannot reproduce honest updates reliably or if false rejects exceed 1% after applying documented deterministic settings.

## Evidence references

- Artifact root: `<local-path>/projects/verifiable-microbatch-replays-for-volunteer-training-d7c3c0433735`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
