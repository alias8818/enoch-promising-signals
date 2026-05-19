# Model-integrated cache-aware n-gram drafting on code and repeated-document long-context prompts

Status: `useful_signal`
Project ID: `model-integrated-cache-aware-n-gram-drafting-on-code-and-r-16dea29f32`
Run ID: `model-integrated-cache-aware-n-gram-drafting-on-code-and-r-16dea29f32-20260514T025906739773+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Model-integrated cache-aware n-gram drafting on code and repeated-document long-context prompts: internal_generated:model-integrated-cache-aware-n-gram-drafting-on-code-and-r-16dea29f32

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge only; no new evidence was added, and validation remains limited to the original run scale.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Tier 2 evidence shows target-pass reductions versus no draft, but repeated-document performance is much worse than full-prefix lookup and selection controls undermine the cache-aware mechanism claim; the result remains partly proxied rather than a full long-context serving validation.

## Recommended next action

Stop this run as a no-paper mixed result: the proxy and GPT-2 checks support n-gram drafting as a mechanism, but cache-aware lookup does not beat full-prefix and random-candidate controls strongly enough for publication.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Long-context model-integrated candidate ranking for cache-aware n-gram drafting
- Success threshold: At least 10% wall-clock decode throughput improvement over full-prefix prompt lookup and at least 95% of full-prefix target-pass reduction on both code and repeated-document domains, with bounded cache-window lookup overhead and no degradation versus no-draft correctness.
- Stop condition: Stop if the integrated cache-aware policy remains below 95% of full-prefix target-pass reduction on repeated-document prompts or fails to improve wall-clock throughput by at least 10% in paired runs.

## Evidence references

- Artifact root: `<local-path>/projects/model-integrated-cache-aware-n-gram-drafting-on-code-and-r-16dea29f32`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
