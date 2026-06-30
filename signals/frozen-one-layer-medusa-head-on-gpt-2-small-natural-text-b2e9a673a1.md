# Frozen one-layer Medusa head on GPT-2-small natural text

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `frozen-one-layer-medusa-head-on-gpt-2-small-natural-text-b2e9a673a1`
Run ID: `frozen-one-layer-medusa-head-on-gpt-2-small-natural-text-b2e9a673a1-20260528T123813923646+0000`

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

- Parent run decision: Frozen 1-layer medusa head for local draft: enoch://control-plane/projects/frozen-1-layer-medusa-head-for-local-draft-140fb50ba046/runs/frozen-1-layer-medusa-head-for-local-draft-140fb50ba046-20260528T084043150177+0000
- Provider-backed Research Facility batch: hf:moonshotai/Kimi-K2.6: enoch://research-facility/provider/hf:moonshotai/Kimi-K2.6/f42090396412

## What looked useful

The one-layer frozen-base Medusa head produced a reproducible narrow h2 signal over shuffled-hidden control and unigram top1, but failed to clearly beat unigram top10 at h2 and failed unigram controls at h3 and h4.

## Boundaries and scale limits

Only GPT-2-small and WikiText-2 were tested; only linear heads were tested; validation used token top-k accuracy rather than speculative-decoding acceptance or throughput; a larger 32768-position run was attempted but terminated before metrics.

## Claim scope

Small Tier-1 GPT-2-small frozen-base test on WikiText-2 natural text: one linear vocabulary head per future horizon trained on 8192 positions and validated on 2048 positions across two seeds.

## Why it stopped

No-paper mixed Tier-1 direct result: the mechanism has a small h2 signal but does not meet the stated multi-horizon control threshold.

## Recommended next action

Run one bounded deepen test that isolates h2 with more positions and per-horizon training, then stop unless h2 beats unigram top10 by at least 5 percentage points and shuffled top1 by at least 2 percentage points across 3 seeds.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: H2-only frozen GPT-2-small Medusa head with stronger controls
- Success threshold: Mean h2 top10 at least 5 percentage points above unigram top10 and mean h2 top1 at least 2 percentage points above shuffled-hidden top1 across 3 seeds.
- Stop condition: Stop as no-paper negative if h2 does not meet the success threshold or if the result only improves top1 while remaining tied with unigram top10.

## Evidence references

- Artifact root: `<local-path>/projects/frozen-one-layer-medusa-head-on-gpt-2-small-natural-text-b2e9a673a1`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
