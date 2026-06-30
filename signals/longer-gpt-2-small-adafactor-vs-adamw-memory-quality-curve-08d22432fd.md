# Longer GPT-2-small Adafactor-vs-AdamW memory-quality curve

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `longer-gpt-2-small-adafactor-vs-adamw-memory-quality-curve-08d22432fd`
Run ID: `longer-gpt-2-small-adafactor-vs-adamw-memory-quality-curve-08d22432fd-20260614T021229033125+0000`

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

- Parent run decision: Quality-aware GPT-2-small optimizer memory Pareto micro-pretraining: enoch://control-plane/projects/quality-aware-gpt-2-small-optimizer-memory-pareto-micro-pr-547b5ceb38/runs/quality-aware-gpt-2-small-optimizer-memory-pareto-micro-pr-547b5ceb38-20260614T015121059212+0000
- Parent run decision: Optimizer memory Pareto at GPT-2-small scale: enoch://control-plane/projects/optimizer-memory-pareto-at-gpt-2-small-scale-7e6517f802d5/runs/optimizer-memory-pareto-at-gpt-2-small-scale-7e6517f802d5-20260614T012457260393+0000

## What looked useful

AdamW mean eval loss 6.7211 with 944.9 MB optimizer state and 2525 MB peak CUDA allocated. Plain Adafactor mean eval loss 6.9071 with 1.2 MB optimizer state and 1551 MB peak CUDA allocated. Adafactor-beta1 mean eval loss 6.5677 with 473.7 MB optimizer state and 2023 MB peak CUDA allocated. The useful bounded signal is an intermediate-memory Adafactor-beta1 regime rather than maximal-memory-saving Adafactor.

## Boundaries and scale limits

Two seeds, one dataset, one learning rate, 150 optimizer steps per run, sequence length 256, gradient checkpointing enabled, no LR sweep, no long convergence run, and no broader corpus or downstream evaluation.

## Claim scope

On a local GPT-2-small-shape WikiText-2 run from scratch for 150 optimizer steps and 614,400 tokens per seed, Adafactor variants trace a real memory-quality curve versus AdamW: no-momentum Adafactor saves the most memory but trails AdamW early loss, while Adafactor with beta1 saves about half AdamW optimizer-state memory and improves early validation loss in both tested seeds.

## Why it stopped

No-paper useful signal: this medium confirmation produced direct target metrics and a real baseline/control, but the scale and robustness are insufficient for publication-grade claims.

## Recommended next action

Run a bounded deepen test with 3 seeds, at least 1000 optimizer steps, and a small LR sweep for AdamW, Adafactor, and Adafactor-beta1 to test whether the beta1 memory-quality advantage persists beyond the early training phase.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Longer LR-swept GPT-2-small Adafactor-beta1 memory-quality persistence
- Success threshold: Adafactor-beta1 must maintain at least 35% optimizer-state memory reduction versus AdamW and mean eval loss no worse than AdamW by 0.02 across three seeds after LR tuning; plain Adafactor should be reported separately as quality-lagged unless it closes within 0.05 eval loss.
- Stop condition: Stop if tuned AdamW matches or beats Adafactor-beta1 by more than 0.05 eval loss at 1000 steps while the beta1 memory reduction is below 35%, or if the beta1 advantage reverses in at least two of three seeds.

## Evidence references

- Artifact root: `<local-path>/projects/longer-gpt-2-small-adafactor-vs-adamw-memory-quality-curve-08d22432fd`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
