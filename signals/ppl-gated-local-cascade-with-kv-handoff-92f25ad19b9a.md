# PPL-Gated Local Cascade with KV Handoff

Status: `compute_scale_blocked`
Project ID: `ppl-gated-local-cascade-with-kv-handoff-92f25ad19b9a`
Run ID: `ppl-gated-local-cascade-with-kv-handoff-92f25ad19b9a-20260515T071417455427+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/74ae32019ff3

## What looked useful

Backfilled from recent supported/mixed moderate-or-strong no-paper decision so the dashboard can distinguish useful local signals from hard negatives.

## Boundaries and scale limits

Historical rejudge found scale/full-validation limits in the original stop reason or next action; park unless a cheaper bounded test is defined.

## Claim scope

Historical bounded rejudge only: preserves the original local/toy/small/medium evidence as a useful signal without asserting full-scale validation.

## Why it stopped

Direct distilgpt2-to-gpt2 KV handoff failed in 24/24 attempts while a gpt2 self-cache positive control passed in 24/24 attempts; the PPL gate signal was promising but does not rescue the failed no-recompute handoff claim.

## Recommended next action

Stop this exact direct small-to-large KV-handoff variant; the result is an early/proxy falsification, not a full validation, and any next run should test a PPL-gated cascade with recompute/speculative verification or an explicit learned KV translation mechanism.

## Follow-up

- Recommended: `true`
- Type: `branch`
- Title: PPL-gated cascade without direct KV reuse
- Success threshold: At least 20% end-to-end decode latency reduction versus always-large with no more than 1% relative NLL degradation on a held-out text corpus and statistically stable results across at least three seeds or shards.
- Stop condition: Stop if thresholded cascading cannot beat always-large latency by 10% at matched NLL, or if recomputation overhead removes the benefit across the threshold sweep.

## Evidence references

- Artifact root: `<local-path>/projects/ppl-gated-local-cascade-with-kv-handoff-92f25ad19b9a`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
