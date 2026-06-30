# Mini-transformer Adafactor vs AdamW LR-grid robustness on two real corpora

Status: `useful_signal`
Curation bucket: `followup_recommended`
Curation score: `83`
Project ID: `mini-transformer-adafactor-vs-adamw-lr-grid-robustness-on-4017e2342f`
Run ID: `mini-transformer-adafactor-vs-adamw-lr-grid-robustness-on-4017e2342f-20260620T120121795886+0000`

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

- Parent run decision: Mini-transformer CPU Adafactor vs AdamW real-corpus confirmation: enoch://control-plane/projects/mini-transformer-cpu-adafactor-vs-adamw-real-corpus-confir-c73b6b57f1/runs/mini-transformer-cpu-adafactor-vs-adamw-real-corpus-confir-c73b6b57f1-20260620T095342083718+0000
- Parent run decision: Adafactor Factored Second Moments vs AdamW on CPU Pretraining: enoch://control-plane/projects/adafactor-factored-second-moments-vs-adamw-on-cpu-pretraining-aeb892926838/runs/adafactor-factored-second-moments-vs-adamw-on-cpu-pretraining-aeb892926838-20260620T092941754538+0000

## What looked useful

The conservative grid favored Adafactor slightly in mean validation loss, but the stress grid reversed the result: at 3e-2 Adafactor was worse than AdamW by 0.451 validation loss on Tiny Shakespeare and 0.359 on Frankenstein. No hard divergence occurred, so robustness by finite/improved runs was tied.

## Boundaries and scale limits

Small model, byte-level tokenization, two corpus slices, two seeds, 80 training steps per run, local Adafactor implementation rather than framework-standard relative-step Adafactor, no warmup or schedule sweep, no GPT-2-scale validation.

## Claim scope

In a CPU-bounded byte-level 2-layer mini-transformer trained for 80 steps on Tiny Shakespeare and Gutenberg Frankenstein, Adafactor did not show a learning-rate robustness advantage over AdamW across learning rates 3e-4 through 3e-2. Both optimizers were stable, but AdamW had better high-LR validation loss at 1e-2 and 3e-2.

## Why it stopped

No-paper useful negative signal: direct small-scale evidence does not support an Adafactor LR-grid robustness advantage over AdamW, and the run is not broad or long enough for publication-grade closure.

## Recommended next action

Run one bounded deepen study with framework-standard Adafactor, warmup/schedule controls, at least 3 seeds, and longer training on WikiText-2 or another standard corpus; stop paper escalation unless Adafactor beats AdamW in both stability and validation loss across the high-LR region.

## Follow-up

- Recommended: `true`
- Type: `deepen`
- Title: Standard Adafactor schedule and longer-horizon LR robustness on WikiText-2
- Success threshold: Adafactor must match or exceed AdamW best validation loss and show lower high-LR degradation or fewer unstable runs on both corpora/seeds, with the effect persisting under the schedule ablation.
- Stop condition: Stop if AdamW remains equal or better in high-LR validation loss or if Adafactor's advantage appears only in one corpus, one seed, or only with an unmatched schedule.

## Evidence references

- Artifact root: `<local-path>/projects/mini-transformer-adafactor-vs-adamw-lr-grid-robustness-on-4017e2342f`
- `run_notes.md`
- `.enoch/project_decision.json`
- `.enoch/metrics.json`
- `results/smoke.json`

## Do not overclaim

These are not validated papers, not peer-reviewed results, and not publication-positive Enoch corpus artifacts. This entry preserves bounded local evidence that may be useful for larger-compute follow-up.
