# Direct CPU transformer tiny-draft speculative decoding vs prompt n-gram baseline

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `direct-cpu-transformer-tiny-draft-speculative-decoding-vs-80f5018536`
Run ID: `direct-cpu-transformer-tiny-draft-speculative-decoding-vs-80f5018536-20260620T102701297220+0000`

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

- Parent run decision: Tiny Draft Spec-Decoding vs N-gram Baseline on CPU: enoch://control-plane/projects/tiny-draft-spec-decoding-vs-n-gram-baseline-on-cpu-70c0a63ce877/runs/tiny-draft-spec-decoding-vs-n-gram-baseline-on-cpu-70c0a63ce877-20260620T101402013331+0000
- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/43a0ad0c6bd9

## What looked useful

Transformer proposer acceptance was 0.1923 versus n-gram 0.0997, and ideal batched target-forward reduction was 41.0% versus 26.6%; however measured exact CPU wall time was 8.215 s for transformer speculative decoding versus 6.137 s for n-gram and 4.963 s for greedy.

## Boundaries and scale limits

Small local character-level models, deterministic synthetic/control corpus, no KV cache, no pretrained subword model, no exact batched verifier in the measured wall-clock path, and no broad prompt/corpus robustness suite.

## Claim scope

In a bounded CPU-only character-level transformer test with 12 held-out prompts, a 15k-parameter tiny transformer drafter improved proposal acceptance and ideal batched target-call reduction versus a prompt n-gram proposer, but failed the practical wall-clock threshold under strict exact verification.

## Why it stopped

The calibrated direct CPU test failed the practical success threshold: transformer speculative decoding was 0.747x the speed of the n-gram baseline despite higher acceptance; this is a controlled small direct result, not a full-scale validation.

## Recommended next action

Stop this run as no-paper useful signal; a bounded deepen follow-up should implement an exact batched or KV-cache verifier and require at least 1.05x wall-clock speedup versus prompt n-gram while preserving exact target output.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exact batched CPU verifier for tiny-draft speculative decoding
- Success threshold: Transformer speculative decoding must preserve exact target output and achieve at least 1.05x wall-clock speedup versus prompt n-gram and at least 1.05x versus greedy target decoding on the bounded CPU suite.
- Stop condition: Stop if exact batched/KV verification cannot preserve target output, or if measured transformer speculative wall-clock remains below 1.05x speedup versus prompt n-gram after one calibrated run.

## Evidence references

- Artifact root: `<local-path>/projects/direct-cpu-transformer-tiny-draft-speculative-decoding-vs-80f5018536`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
