# Medium KV-cache benchmark for prompt n-gram speculative decoding

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `medium-kv-cache-benchmark-for-prompt-n-gram-speculative-de-83b47bbef2`
Run ID: `medium-kv-cache-benchmark-for-prompt-n-gram-speculative-de-83b47bbef2-20260515T095023039221+0000`

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

- Internal Enoch project: Medium KV-cache benchmark for prompt n-gram speculative decoding: internal_generated:medium-kv-cache-benchmark-for-prompt-n-gram-speculative-de-83b47bbef2

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium direct real-model evidence supports the mechanism but not publication readiness: greedy-equivalent safe variants had only 1.013-1.024x median speedup, 18.75-29.17% slower prompts, and the aggressive 2-gram ablation produced one correctness mismatch.

## Recommended next action

Stop the paper path for this run; only reopen via a bounded long-context copy-heavy benchmark that must show at least 1.15x median decode speedup with 100% greedy equality.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Long-context copy-heavy prompt n-gram speculative decoding benchmark
- Success threshold: At least 1.15x median decode speedup versus KV-cache greedy, 100% output equality, no more than 5% slower prompts, and a positive p10 speedup over fixed seeds.
- Stop condition: Stop if any greedy-equivalent variant fails to reach 1.15x median speedup, has more than 5% slower prompts, or shows any output mismatch on the fixed-seed benchmark.

## Evidence references

- Artifact root: `<local-path>/projects/medium-kv-cache-benchmark-for-prompt-n-gram-speculative-de-83b47bbef2`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
