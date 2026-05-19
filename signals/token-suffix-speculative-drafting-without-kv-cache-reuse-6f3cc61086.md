# Token-Suffix Speculative Drafting Without KV-Cache Reuse

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `token-suffix-speculative-drafting-without-kv-cache-reuse-6f3cc61086`
Run ID: `token-suffix-speculative-drafting-without-kv-cache-reuse-6f3cc61086-20260514T162848740790+0000`

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

- Internal Enoch project: Token-Suffix Speculative Drafting Without KV-Cache Reuse: internal_generated:token-suffix-speculative-drafting-without-kv-cache-reuse-6f3cc61086

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Medium confirmation on a real model, fixed seeds, ablations, shuffled control, and cached greedy baseline found best throughput at 0.912x of cached greedy with only 2.57% acceptance; 4/324 runs diverged from exact no-KV greedy.

## Recommended next action

Stop this no-KV-cache-reuse line as a medium direct falsification: suffix drafting showed above-control acceptance but did not beat cached greedy and had rare exactness failures.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: Token-Suffix Speculative Drafting With KV-Cache Verification Rollback
- Success threshold: On at least 3 fixed seeds and 18 or more prompts, achieve exact-match rate 1.0 and at least 1.10x wall-clock speedup over cached greedy, with suffix-table acceptance at least 5x shuffled control.
- Stop condition: Stop if exactness is below 1.0, or if the best exact configuration is below 1.05x cached greedy after suffix/draft-length ablations.

## Evidence references

- Artifact root: `<local-path>/projects/token-suffix-speculative-drafting-without-kv-cache-reuse-6f3cc61086`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
