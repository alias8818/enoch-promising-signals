# Easy-to-hard data curriculum for tiny pretraining: does ordering matter at fixed tokens on GB10

Status: `useful_signal`
Curation bucket: `top_external_researcher_candidates`
Curation score: `98`
Project ID: `easy-to-hard-data-curriculum-for-tiny-pretraining-does-ordering-matter-at-fixed-tokens-on-gb10-0f4623c4c3ee`
Run ID: `easy-to-hard-data-curriculum-for-tiny-pretraining-does-ordering-matter-at-fixed-tokens-on-gb10-0f4623c4c3ee-20260619T113821959212+0000`

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

- Provider-backed Research Facility batch: minimax/minimax-m3: enoch://research-facility/provider/minimax/minimax-m3/b8e093e8ed29

## What looked useful

Ordering mattered, but the useful mechanism was negative for block curricula: each block schedule forgot the distribution seen first, while mixed interleaving preserved both easy and hard validation performance.

## Boundaries and scale limits

459,840-parameter model, synthetic non-IID token distributions, 8.192M train tokens per run, five seeds per schedule, one GB10 worker. This does not validate natural-language pretraining curricula, GPT-2-small-class scaling, or publication-grade robustness.

## Claim scope

In a five-seed synthetic tiny causal-transformer pretraining probe with fixed tokens, block ordering of easy and hard data changes final validation loss strongly; interleaved mixed sampling outperforms both easy-to-hard and hard-to-easy block schedules on balanced mixed validation.

## Why it stopped

Synthetic direct probe supports an ordering effect but falsifies the simple block easy-to-hard benefit; evidence is not natural-corpus or scale-robust enough for paper-positive closure.

## Recommended next action

Stop this run as no-paper useful signal; next bounded test should compare mixed sampling against replayed or gradual easy-to-hard curricula on a small real text corpus at fixed tokens.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Replay-buffer easy-to-hard curriculum on small real text at fixed tokens
- Success threshold: Replayed or gradual easy-to-hard achieves lower final mixed validation loss than uniform mixed sampling without worsening either easy or hard validation loss by more than 5% across repeated seeds.
- Stop condition: Stop if replayed or gradual curricula still show worse mixed validation than uniform mixed sampling or any clear first-distribution forgetting after the same token budget.

## Evidence references

- Artifact root: `<local-path>/projects/easy-to-hard-data-curriculum-for-tiny-pretraining-does-ordering-matter-at-fixed-tokens-on-gb10-0`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
