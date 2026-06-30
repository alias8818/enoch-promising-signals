# Real-Trace Replay Screen for Withheld Benchmark Rotations

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `real-trace-replay-screen-for-withheld-benchmark-rotations-19cec89958`
Run ID: `real-trace-replay-screen-for-withheld-benchmark-rotations-19cec89958-20260529T203313353078+0000`

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

- Parent run decision: Trace Replay Validation of Rotating Private Challenge Banks: enoch://control-plane/projects/trace-replay-validation-of-rotating-private-challenge-bank-1dc87ee4fc/runs/trace-replay-validation-of-rotating-private-challenge-bank-1dc87ee4fc-20260529T163552340268+0000
- Parent run decision: Challenge-Batch Cheating Detection for Volunteer Training: enoch://control-plane/projects/challenge-batch-cheating-detection-for-volunteer-training-8778ac14b9d5/runs/challenge-batch-cheating-detection-for-volunteer-training-8778ac14b9d5-20260529T130113393905+0000

## What looked useful

Trace replay reached 0.975 withheld flag accuracy and 0.958 bad-rotation recall across 40 withheld rotations, beating the metadata baseline's 0.875 flag accuracy and 0.792 bad recall. Ablations showed family conditioning, difficulty/frontier comparison, and duplicate screening are all required components.

## Boundaries and scale limits

No real LLM submissions, real benchmark task semantics, private production challenge-bank rotations, adversarial contamination beyond near-duplicate leakage, or human scoring were tested. The run is medium controlled evidence, not publication-grade real benchmark evidence.

## Claim scope

In a fixed-seed controlled private-bank simulator with recorded prior traces, synthetic agents, deterministic live reruns, withheld candidate rotations, a metadata-only baseline, and mechanism ablations, per-family difficulty-frontier trace replay plus duplicate screening screened withheld rotations better than the metadata-only baseline.

## Why it stopped

Tier 2 controlled evidence supports the mechanism but remains generated-trace/synthetic-agent evidence, so it is useful no-paper evidence rather than paper-positive validation.

## Recommended next action

Run the same replay screen on actual public benchmark/model trace data with withheld rotations and preserve the metadata baseline plus family/difficulty/duplicate ablations before considering any paper claim.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Public Benchmark Model-Trace Replay for Withheld Rotations
- Success threshold: Across withheld real/model rotations, trace replay must achieve at least 0.90 bad/good flag accuracy, at least 0.90 bad-rotation recall, balanced-rotation per-model pass-rate MAE <= 0.08, balanced Spearman rank correlation >= 0.90, and strictly beat the metadata-only baseline on flag accuracy.
- Stop condition: Stop as no-paper or negative if trace replay fails to beat the metadata-only baseline, misses more than 10% of bad rotations, or the required real/model trace surface cannot be obtained without private external evidence.

## Evidence references

- Artifact root: `<local-path>/projects/real-trace-replay-screen-for-withheld-benchmark-rotations-19cec89958`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
