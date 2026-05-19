# Per-layer attention-only versus adaptive HAKV retention at 25-50%

Status: `useful_signal`
Project ID: `per-layer-attention-only-versus-adaptive-hakv-retention-at-9f783e5b95`
Run ID: `per-layer-attention-only-versus-adaptive-hakv-retention-at-9f783e5b95-20260515T225612921768+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Per-layer attention-only versus adaptive HAKV retention at 25-50%: internal_generated:per-layer-attention-only-versus-adaptive-hakv-retention-at-9f783e5b95

## What looked useful

Across three fixed-seed runs and 130,816 evaluated tokens per policy, HAKV had mean delta loss vs full of +0.170 at 25% retention and +0.036 at 50%, while attention-only had +2.173 and +1.342. Recent-window controls were also much worse. This supports the adaptive attention+recency mechanism in the scoped setting but is not paper-ready.

## Boundaries and scale limits

Single pretrained GPT-2-small model, one WikiText-2 language-modeling dataset, 512-token windows, Python/eager-attention evaluation harness, no optimized serving latency study, no long-context downstream tasks, no larger model families, and no canonical external HAKV specification supplied by the prompt.

## Claim scope

On GPT-2-small WikiText-2 next-token inference with 512-token windows, the locally defined adaptive HAKV attention+recency KV retention policy at 25% and 50% cache budgets substantially outperforms per-layer cumulative attention-only retention and remains close to the full-cache baseline.

## Why it stopped

Scoped direct validation supports the mechanism but remains too narrow for publication-grade claims.

## Recommended next action

Stop this follow-up as no-paper useful-signal evidence; any paper attempt should first define canonical HAKV and validate across additional model sizes, datasets, long-context tasks, and optimized latency/memory measurements.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/per-layer-attention-only-versus-adaptive-hakv-retention-at-9f783e5b95`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
