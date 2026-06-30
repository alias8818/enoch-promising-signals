# Suffix-Tree Speculative Decoding Drafts for CPU Inference

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `suffix-tree-speculative-decoding-drafts-for-cpu-inference-1c8a584e7f3d`
Run ID: `suffix-tree-speculative-decoding-drafts-for-cpu-inference-1c8a584e7f3d-20260629T061107532400+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/084f73bed7c6

## What looked useful

Variable-length suffix lookup is a plausible draft source for repetitive CPU decoding workloads, but acceptance collapsed on low-repeat/randomish streams and stayed modest on noisy streams; this should be treated as a bounded mechanism signal rather than paper-ready evidence.

## Boundaries and scale limits

No real LLM inference loop, no verifier overhead, no tokenizer/prompt trace validation, no production suffix-tree memory optimization, and only 30k-token synthetic streams were tested.

## Claim scope

On deterministic synthetic token streams with repeated spans, a longest-suffix exact-match history drafter produced more accepted tokens per proposal than fixed 4-gram and 8-gram exact-match baselines, but only high-repeat low-noise streams reached practically interesting absolute acceptance.

## Why it stopped

Closed as a no-paper useful signal: the run produced synthetic mechanism evidence and clear failure modes, but not direct CPU LLM inference speedup.

## Recommended next action

Run a bounded deepen follow-up that integrates the suffix-history drafter into a small CPU decoder or real generated-token trace replay and requires net wall-clock tokens/sec improvement over no drafting and fixed n-gram drafting.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: CPU decoder trace replay for suffix-history speculative drafts
- Success threshold: At least 10% net wall-clock tokens/sec improvement on a repeated-span trace suite, with no regression greater than 5% on low-repeat traces and memory bounded under a documented cap.
- Stop condition: Stop if verifier/index overhead eliminates net speedup or if acceptance on real traces remains below 0.25 token acceptance for draft length 4.

## Evidence references

- Artifact root: `<local-path>/projects/suffix-tree-speculative-decoding-drafts-for-cpu-inference-1c8a584e7f3d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
