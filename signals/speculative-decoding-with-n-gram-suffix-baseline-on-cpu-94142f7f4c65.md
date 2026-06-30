# Speculative Decoding with N-gram Suffix Baseline on CPU

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `speculative-decoding-with-n-gram-suffix-baseline-on-cpu-94142f7f4c65`
Run ID: `speculative-decoding-with-n-gram-suffix-baseline-on-cpu-94142f7f4c65-20260605T062214439985+0000`

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

- Provider-backed Research Facility batch: openrouter/owl-alpha: enoch://research-facility/provider/openrouter/owl-alpha/57315345ba57

## What looked useful

The n-gram suffix proposer is cheap on CPU and can accept about 0.67-1.23 natural-text tokens per attempt online, but the result is fragile: best natural modeled speedup is 1.84x at 1.2x verification cost, 1.11x at 2.0x, and 0.74x at 3.0x.

## Boundaries and scale limits

No real transformer target model was run; acceptance was against exact corpus continuation, not model logits. Corpora were small natural-text samples plus a synthetic repetitive control. Speedups are cost-model estimates, not measured end-to-end LLM latency.

## Claim scope

Bounded CPU proxy result: byte-token exact-text n-gram suffix drafting on tiny_shakespeare and Pride and Prejudice shows negligible proposer overhead and accepted-token rates that can imply modeled speedup only when target multi-token verification is close to single-token cost.

## Why it stopped

Closed as no-paper useful signal because this run is an exact-text proxy and cost model, not full end-to-end CPU speculative decoding validation.

## Recommended next action

Run a bounded direct CPU LLM follow-up with a small local target model, measuring wall-clock tokens/sec, draft acceptance, target batch verification cost, and output equivalence for draft lengths 2, 4, and 8.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: End-to-end CPU LLM validation of n-gram suffix speculative decoding
- Success threshold: At least 1.15x wall-clock tokens/sec improvement over baseline greedy decoding on two natural prompts with identical target-model outputs or valid lossless speculative sampling.
- Stop condition: Stop if measured target verification cost is at least 2.5x a one-token step or if end-to-end throughput is below 1.05x baseline across draft lengths 2, 4, and 8.

## Evidence references

- Artifact root: `<local-path>/projects/speculative-decoding-with-n-gram-suffix-baseline-on-cpu-94142f7f4c65`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
