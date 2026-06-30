# Adaptive N-gram Cache Speculation with Context-Order Selection

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `adaptive-n-gram-cache-speculation-with-context-order-selection-ea72e0aae81c`
Run ID: `adaptive-n-gram-cache-speculation-with-context-order-selection-ea72e0aae81c-20260601T025440766080+0000`

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

- Provider-backed Research Facility batch: hf:zai-org/GLM-5.1: enoch://research-facility/provider/hf:zai-org/GLM-5.1/211246bfc7ae

## What looked useful

Adaptive order selection reached 86.2% and 90.6% draft precision at threshold 0.8 on the two corpora, far above the best non-adaptive precision baselines, but coverage was only 0.3% and 1.8%; throughput-proxy gains at threshold 0.0 were small and low precision.

## Boundaries and scale limits

Two public text corpora, regex word/punctuation tokens, train/calibration/test offline cache, max n-gram order 5, draft length 4, no neural verifier, no BPE tokenizer, no serving latency measurement, and no large-domain robustness sweep.

## Claim scope

Offline word-token n-gram cache simulation on Tiny Shakespeare and Pride and Prejudice shows calibrated adaptive context-order selection can identify sparse high-precision draft opportunities, but it does not dominate fixed or highest-order-backoff baselines on accepted tokens per held-out token once confidence thresholds are applied.

## Why it stopped

Moderate offline evidence supports a sparse high-precision mechanism, but the main throughput proxy is mixed and the run lacks direct model-serving evidence, so it is not publication-grade.

## Recommended next action

Stop this run as a no-paper useful signal; the next bounded test should integrate the adaptive cache with a small neural verifier and compare accepted tokens per verifier call and latency against fixed/backoff cache baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Small-LM Verification of Adaptive N-gram Cache Order Selection
- Success threshold: Adaptive policy improves accepted tokens per verifier call by at least 10% over the best non-adaptive baseline while maintaining draft precision at or above 80% and non-trivial coverage of at least 1% of test positions.
- Stop condition: Stop as negative if adaptive coverage remains below 1% at 80% precision or if accepted tokens per verifier call does not exceed the best non-adaptive baseline on the small-LM test.

## Evidence references

- Artifact root: `<local-path>/projects/adaptive-n-gram-cache-speculation-with-context-order-selection-ea72e0aae81c`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
