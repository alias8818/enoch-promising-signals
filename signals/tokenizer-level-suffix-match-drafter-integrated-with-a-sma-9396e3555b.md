# Tokenizer-level suffix-match drafter integrated with a small transformer verifier

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `tokenizer-level-suffix-match-drafter-integrated-with-a-sma-9396e3555b`
Run ID: `tokenizer-level-suffix-match-drafter-integrated-with-a-sma-9396e3555b-20260514T060206742898+0000`

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

- Internal Enoch project: Tokenizer-level suffix-match drafter integrated with a small transformer verifier: internal_generated:tokenizer-level-suffix-match-drafter-integrated-with-a-sma-9396e3555b

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 direct tests with fixed seeds, real baselines, controls, and GPT-2-small-class confirmation support the mechanism but do not provide publication-grade serving or robustness evidence.

## Recommended next action

Stop this run as mechanism-positive but paper-negative; next run should implement a KV-cache serving benchmark against optimized greedy and prompt-lookup baselines.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: KV-cache serving benchmark for tokenizer-level suffix-match drafting
- Success threshold: Exact output preservation plus at least 1.25x median wall-clock speedup over optimized greedy and at least 1.10x over the prompt-lookup baseline on two verifier families.
- Stop condition: Stop if exact-output preservation fails, if optimized wall-clock speedup is below 1.10x on GPT-2-small-class, or if gains vanish when generated-tail self-repetition is excluded.

## Evidence references

- Artifact root: `<local-path>/projects/tokenizer-level-suffix-match-drafter-integrated-with-a-sma-9396e3555b`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
