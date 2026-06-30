# Trace Replay Validation of Rotating Private Challenge Banks

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `trace-replay-validation-of-rotating-private-challenge-bank-1dc87ee4fc`
Run ID: `trace-replay-validation-of-rotating-private-challenge-bank-1dc87ee4fc-20260529T163552340268+0000`

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

- Parent run decision: Challenge-Batch Cheating Detection for Volunteer Training: enoch://control-plane/projects/challenge-batch-cheating-detection-for-volunteer-training-8778ac14b9d5/runs/challenge-batch-cheating-detection-for-volunteer-training-8778ac14b9d5-20260529T130113393905+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/277f7d0bf68a

## What looked useful

A small direct mechanism test supports trace replay as a predeployment screen for rotations when candidate banks preserve comparable metadata and trace summaries include solved-family difficulty ceilings and duplicate provenance. It caught easy, hard/shifted, and duplicate/leaky rotations while accepting a balanced fresh rotation.

## Boundaries and scale limits

Synthetic task families, synthetic agents, deterministic oracle scoring, explicit family/difficulty metadata, and one seed. No real LLM traces, natural-language challenge semantics, production private challenge banks, adversarial submitters, or human grading were tested.

## Claim scope

In a controlled synthetic private-bank setting with 8 deterministic agents, 56 prior trace tasks, and four 56-task candidate rotations, trace replay predicted balanced-rotation live performance within MAE 0.0446 and Spearman 0.9762, and matched all good/bad rotation screening labels.

## Why it stopped

Tier 1 controlled direct test met its threshold, but evidence remains synthetic and no-paper under the strict paper gate.

## Recommended next action

Run a bounded deepen test on real or high-fidelity benchmark traces with withheld candidate rotations and independent scoring; do not write a paper from this synthetic Tier 1 result alone.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Real-Trace Replay Screen for Withheld Benchmark Rotations
- Success threshold: Balanced rotation replay-vs-live MAE <= 0.08, Spearman >= 0.90, and 100% correct good/bad flags across balanced, shifted, and duplicate/leaky candidate banks.
- Stop condition: Stop as unsupported if balanced rotation MAE exceeds 0.12, Spearman is below 0.80, or any shifted/leaky candidate is missed under predeclared thresholds.

## Evidence references

- Artifact root: `<local-path>/projects/trace-replay-validation-of-rotating-private-challenge-bank-1dc87ee4fc`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
