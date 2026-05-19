# Long-context copy-heavy prompt n-gram speculative decoding benchmark

Status: `compute_scale_blocked`
Curation bucket: `compute_scale_blocked`
Curation score: `78`
Project ID: `long-context-copy-heavy-prompt-n-gram-speculative-decoding-9afd8b765d`
Run ID: `long-context-copy-heavy-prompt-n-gram-speculative-decoding-9afd8b765d-20260515T100022604455+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Deterministic curation

- Bucket: Compute-scale blocked
- Score: `78`
- Score breakdown: `{"bounded_evidence": 20, "evidence_strength": 25, "followup": 10, "hypothesis_status": 15, "source_lineage": 8}`

Reasons:
- moderate evidence_strength
- mixed hypothesis_status
- source lineage present
- bounded follow-up is specified
- follow-up depth is already high
- local evidence artifact paths are present
- metrics artifact is present
- project decision artifact is present

## Source

- Internal Enoch project: Long-context copy-heavy prompt n-gram speculative decoding benchmark: internal_generated:long-context-copy-heavy-prompt-n-gram-speculative-decoding-9afd8b765d

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Bounded full validation on Qwen/Qwen3-0.6B showed copy-heavy median speedup of only 0.986x overall, consistent slowdown at 16k context, and exact greedy-output match in only 4 of 18 copy-heavy comparisons despite deterministic repeated greedy outputs.

## Recommended next action

Stop this paper path: bounded direct validation found non-robust speedups and frequent greedy-output divergence; only a final depth-4 exactness audit should be considered before abandoning prompt lookup as an exact long-context copy accelerator.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Exactness audit for prompt lookup speculative decoding
- Success threshold: At least 1.30x median speedup at 32k or longer copy-heavy contexts, no slowdown at 16k, and 100% token-id equality with greedy on all audited prompts.
- Stop condition: Stop if any exactness divergence remains after deterministic token-id auditing, or if exact runs fail to exceed 1.10x median speedup at 32k.

## Evidence references

- Artifact root: `<local-path>/projects/long-context-copy-heavy-prompt-n-gram-speculative-decoding-9afd8b765d`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
