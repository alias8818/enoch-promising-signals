# Direct Serving Test of CPU N-gram Drafting for Code Contexts

Status: `compute_scale_blocked`
Project ID: `direct-serving-test-of-cpu-n-gram-drafting-for-code-contex-a360e35298`
Run ID: `direct-serving-test-of-cpu-n-gram-drafting-for-code-contex-a360e35298-20260515T083436777782+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/bbda3d5e5c31

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Controlled direct serving test failed the deterministic correctness threshold required for speculative serving; this is a mixed mechanism result, not full validation or publication-grade evidence.

## Recommended next action

Stop this run as a no-paper Tier 1 result: the direct serving test showed 1.82x-2.95x median speedups and fewer target forwards, but even the conservative lookup-2 setting preserved exact greedy output on only 15/24 runs.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Strict-Verifier CPU N-gram Drafting Serving Test
- Success threshold: All deterministic continuations exactly match greedy baseline, median throughput speedup is at least 1.25x, and median target forward calls fall by at least 25%.
- Stop condition: Stop if exact greedy-output preservation fails on any prompt after strict verification and length enforcement, or if median speedup is below 1.10x once correctness is enforced.

## Evidence references

- Artifact root: `<local-path>/projects/direct-serving-test-of-cpu-n-gram-drafting-for-code-contex-a360e35298`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
