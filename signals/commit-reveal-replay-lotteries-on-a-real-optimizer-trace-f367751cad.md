# Commit-reveal replay lotteries on a real optimizer trace

Status: `compute_scale_blocked`
Project ID: `commit-reveal-replay-lotteries-on-a-real-optimizer-trace-f367751cad`
Run ID: `commit-reveal-replay-lotteries-on-a-real-optimizer-trace-f367751cad-20260515T002456855526+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/37d210749f4c

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 1 small direct validation supports exact commit-reveal replay auditing on one real optimizer trace, but it is not full-scale or publication-grade evidence.

## Recommended next action

Stop this worker run as a Tier 1 mechanism-support result, not paper-ready; next run should perform a bounded medium validation on a larger real optimizer trace.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Medium-scale commit-reveal replay auditing on a larger optimizer trace
- Success threshold: Honest replay has max parameter, optimizer-state, and loss diffs <= 1e-10; commit-reveal detection rates stay within binomial 95% intervals around hypergeometric expectation for all corruption schedules; post-hoc nonce search materially underperforms the committed lottery; verifier replay overhead is reported and bounded.
- Stop condition: Stop if honest replay is nondeterministic above 1e-10 on the larger trace, if detection materially misses the expected sampling curve, or if trace storage/replay overhead is too high for the proposed use case.

## Evidence references

- Artifact root: `<local-path>/projects/commit-reveal-replay-lotteries-on-a-real-optimizer-trace-f367751cad`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
