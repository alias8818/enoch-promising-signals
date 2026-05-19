# Small-transformer shard dropout versus routing-knowledge ablation

Status: `useful_signal`
Project ID: `small-transformer-shard-dropout-versus-routing-knowledge-a-22ae468db7`
Run ID: `small-transformer-shard-dropout-versus-routing-knowledge-a-22ae468db7-20260518T232704219290+0000`

> This is a promising-signal record, not a paper. It is bounded local evidence preserved for possible larger-compute follow-up.

## Source

- Internal Enoch project: Small-transformer shard dropout versus routing-knowledge ablation: internal_generated:small-transformer-shard-dropout-versus-routing-knowledge-a-22ae468db7

## What looked useful

Across 8-shard and 16-shard settings, no-dropout baselines reached 100% clean accuracy but fell to 0.23-0.28 route-wrong accuracy, while 0.5 route dropout kept 100% clean accuracy and achieved 0.95-0.97 route-wrong accuracy. Clue corruption then became catastrophic, confirming the intervention shifted reliance from explicit routing to content evidence.

## Boundaries and scale limits

Synthetic associative recall only; no natural language modeling, learned MoE router, GPT-2-small-class baseline, pretrained model, or long-horizon training was tested.

## Claim scope

In a fixed-seed synthetic sharded associative-recall benchmark with 238k-240k parameter transformers, route-token dropout preserved clean accuracy and made performance robust to route masking/corruption by shifting reliance to content clue tokens.

## Why it stopped

The run produced a useful synthetic mechanism signal but did not satisfy the Tier 4 paper-readiness target; the remaining validation would require a new learned-router or language-modeling study, and controller lineage is already at follow-up depth 4.

## Recommended next action

Stop this follow-up at depth 4: keep the synthetic mechanism result as no-paper evidence rather than chaining another deepen/retry run.

## Follow-up

- Recommended: `false`
- Type: ``
- Title: 
- Success threshold: 
- Stop condition: 

## Evidence references

- Artifact root: `<local-path>/projects/small-transformer-shard-dropout-versus-routing-knowledge-a-22ae468db7`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
