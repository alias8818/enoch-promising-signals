# Integrated Small-LM Serving Benchmark for CPU N-Gram Suffix Drafting

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `integrated-small-lm-serving-benchmark-for-cpu-n-gram-suffi-608cd4ffe5`
Run ID: `integrated-small-lm-serving-benchmark-for-cpu-n-gram-suffi-608cd4ffe5-20260527T121750952152+0000`

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

- Parent run decision: Small-LM Direct Verification of CPU N-Gram Suffix Drafting: enoch://control-plane/projects/small-lm-direct-verification-of-cpu-n-gram-suffix-drafting-ffe1ccbc8f/runs/small-lm-direct-verification-of-cpu-n-gram-suffix-drafting-ffe1ccbc8f-20260527T103913046721+0000
- Parent run decision: CPU N-Gram Suffix Speculative Decoding: enoch://control-plane/projects/cpu-n-gram-suffix-speculative-decoding-32a867f96f3a/runs/cpu-n-gram-suffix-speculative-decoding-32a867f96f3a-20260525T225601013275+0000

## What looked useful

Order-3/order-4 exact n-gram suffix drafting preserved greedy outputs and reached 2.13x-2.91x mean speedup with 73%-85% target-call reduction on repetition-rich prompts, but only 1.08x-1.18x mean speedup and 0% median call reduction on general prompts. The order-2 ablation failed exactness and should not be used without repair.

## Boundaries and scale limits

Validated on one small LM, 12 general prompts, 12 repetition-rich prompts, 48 generated generated items per prompt, PyTorch/Hugging Face CPU inference with 4 threads; not validated on production traces, larger models, tuned CPU runtimes, or long-running serving workloads.

## Claim scope

On a local CPU worker with distilgpt2 greedy decoding, exact n-gram suffix drafting improves throughput substantially for repetition-rich prompts, but provides only sparse and small gains on ordinary short prompts.

## Why it stopped

Medium local validation supports the mechanism in repetition-rich contexts but not broad prompt robustness or publication readiness; one ablation also failed exactness.

## Recommended next action

Stop this run as no-paper useful evidence; next run should use a public long-context/code/RAG trace suite in a tuned CPU serving runtime and keep exactness checks mandatory.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Trace-Based CPU N-Gram Suffix Drafting in a Tuned Serving Runtime
- Success threshold: At least 1.5x median tokens/s improvement and at least 35% median target-call reduction on the repeated-context subset, no exactness failures, and no more than 5% regression on ordinary prompts.
- Stop condition: Stop if exactness fails for any intended deployable configuration, or if median speedup is below 1.2x on repeated-context traces after tuning n-gram order and draft length.

## Evidence references

- Artifact root: `<local-path>/projects/integrated-small-lm-serving-benchmark-for-cpu-n-gram-suffi-608cd4ffe5`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
